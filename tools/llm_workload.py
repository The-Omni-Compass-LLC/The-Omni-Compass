#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Real AI serving for the GPU bench: a language model served by vLLM (or any OpenAI-compatible server), asked the same
seeded stream of prompts in every arm, so the card's firmware alone and the firmware with Omni-Compass on top get
exactly the same requests at exactly the same moments.

What a buyer reads, measured per request from the stream itself (stream=True):
  time to first token (TTFT)      the wait before the answer starts: prefill, the compute-heavy part
  time per output token (TPOT)    the pace of the answer after that: decode, the memory-heavy part
  response time                    arrival to the last token
Every request asks for exactly --tokens new tokens (ignore_eos), so every request is the same amount of answer; the
prompts differ (seeded lengths of --prompt-min to --prompt-max words, seeded words), so the server's prefix cache cannot
turn the test into a cache test.

  calibrate   --calib requests one at a time; calib.json (service_ms: the median response time; ttft_ms; tpot_ms). The
              bench's response line is ten times service_ms
  run         serve the schedule for --duration seconds then --drain seconds: Poisson arrivals whose rate steps through
              --rates (requests per second, one per phase; --rate R is one phase). Writes
                latency.csv   elapsed_seconds, latency_ms, ok, service_ms   (live, one row per finished request)
                requests.csv  arrival_s, start_s, done_s, latency_ms, ok, ttft_ms, tpot_ms, tokens
                summary.json  requests, served, not served, t0_epoch, tokens per second, the model, the rates
  capacity    the most work inside the line at the same power: the rate climbs through --steps (requests per second),
              --step-s seconds each, and stops at the first step whose 95th-percentile response time passes --slo-ms or
              whose served rate falls short of the asked rate by more than 5%. capacity.json: every step, and the
              capacity (the last step inside the line), in requests and tokens per second

--signal PATH[,PATH] (or OMNI_SIGNAL) reports each arrival ("a <id>") and each finished request ("d <id> <ms>") to the
card's governor(s), the same in every arm: a load balancer in front of a real server sees the same arrivals.
"""
from __future__ import annotations

import argparse, json, os, random, socket, threading, time, urllib.request
from pathlib import Path

WORDS = ("power heat clock memory token answer cluster request rack cooling battery voltage current queue model layer "
         "batch cache server network storage signal sensor valve motor pump turbine grid load price demand supply").split()


class Signal:
    def __init__(self, paths):
        self.paths = [p for p in (paths or "").split(",") if p]
        self.sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) if self.paths else None
        if self.sk:
            self.sk.setblocking(False)

    def send(self, msg):
        for p in self.paths:
            try:
                self.sk.sendto(msg.encode(), p)
            except OSError:
                pass


def prompt_for(i, seed, lo, hi):
    r = random.Random(seed * 1000003 + i)
    return " ".join(r.choice(WORDS) for _ in range(r.randint(lo, hi))) + ". Explain in plain words, step by step."


def ask(url, model, prompt, tokens, timeout):
    """One streamed completion: (ttft_s, total_s, tokens_received). Raises on failure."""
    body = json.dumps({"model": model, "prompt": prompt, "max_tokens": tokens, "temperature": 0.0, "ignore_eos": True,
                       "stream": True, "stream_options": {"include_usage": True}}).encode()
    req = urllib.request.Request(url + "/v1/completions", data=body, headers={"Content-Type": "application/json"})
    t0 = time.perf_counter(); first = None; n = 0; usage = None
    with urllib.request.urlopen(req, timeout=timeout) as r:
        for raw in r:
            line = raw.decode(errors="replace").strip()
            if not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            try:
                obj = json.loads(data)
            except ValueError:
                continue
            if obj.get("usage"):
                usage = obj["usage"].get("completion_tokens")
            ch = obj.get("choices") or []
            if ch and ch[0].get("text"):
                if first is None:
                    first = time.perf_counter() - t0
                n += 1
    total = time.perf_counter() - t0
    return (first if first is not None else total), total, (usage if usage is not None else n)


def calibrate(a):
    ts, tf, tp = [], [], []
    for i in range(a.calib):
        f, tot, n = ask(a.url, a.model, prompt_for(10 ** 6 + i, a.seed, a.prompt_min, a.prompt_max), a.tokens, 120)
        ts.append(tot * 1000.0); tf.append(f * 1000.0); tp.append((tot - f) * 1000.0 / max(1, n - 1))
    med = lambda xs: sorted(xs)[len(xs) // 2]
    c = {"service_ms": med(ts), "ttft_ms": med(tf), "tpot_ms": med(tp), "tokens": a.tokens, "model": a.model,
         "seed": a.seed, "prompt_words": [a.prompt_min, a.prompt_max]}
    Path(a.out).mkdir(parents=True, exist_ok=True)
    (Path(a.out) / "calib.json").write_text(json.dumps(c, indent=1)); print(json.dumps(c))


def schedule(rates, duration, seed):
    rng = random.Random(seed)
    per = duration / len(rates)
    out, t = [], 0.0
    for i, rate in enumerate(rates):
        t = max(t, i * per)
        while rate > 0:
            t += rng.expovariate(rate)
            if t >= (i + 1) * per:
                t = (i + 1) * per
                break
            out.append(t)
    return out


def serve(a, rates, duration, out, tag=""):
    out.mkdir(parents=True, exist_ok=True)
    sched = schedule(rates, duration, a.seed)
    lat = open(out / f"latency{tag}.csv", "w"); lat.write("elapsed_seconds,latency_ms,ok,service_ms\n"); lat.flush()
    rows, lock = [], threading.Lock()
    sig = Signal(a.signal)
    t0, t0_epoch, end = time.perf_counter(), time.time(), duration + a.drain

    def one(i, arr):
        start = time.perf_counter() - t0
        sig.send(f"a {i}")
        try:
            f, tot, n = ask(a.url, a.model, prompt_for(i, a.seed, a.prompt_min, a.prompt_max), a.tokens, max(1.0, end - start))
            done = start + tot
            ok = 1 if n >= a.tokens and done <= end else 0
            ttft, tpot = f * 1000.0, (tot - f) * 1000.0 / max(1, n - 1)
        except Exception:  # noqa: BLE001  a failed or timed-out request is not served
            done, ok, ttft, tpot, n = time.perf_counter() - t0, 0, float("nan"), float("nan"), 0
        sig.send(f"d {i} {(done - start) * 1000.0:.3f}" if ok else f"d {i} nan")
        ms = (done - arr) * 1000.0
        with lock:
            rows.append((arr, start, done, ms, ok, ttft, tpot, n))
            if ok:
                lat.write(f"{done:.3f},{ms:.3f},1,{(done - start) * 1000.0:.3f}\n"); lat.flush()

    threads = []
    for i, arr in enumerate(sched):
        w = arr - (time.perf_counter() - t0)
        if w > 0:
            time.sleep(w)
        th = threading.Thread(target=one, args=(i, arr), daemon=True); th.start(); threads.append(th)
    for th in threads:
        th.join(timeout=max(0.0, end - (time.perf_counter() - t0)) + 5.0)
    left = end - (time.perf_counter() - t0)
    if left > 0:
        time.sleep(left)
    with lock:
        done_rows = sorted(rows)
    served = sum(1 for r in done_rows if r[4] == 1)
    with open(out / f"requests{tag}.csv", "w") as f:
        f.write("arrival_s,start_s,done_s,latency_ms,ok,ttft_ms,tpot_ms,tokens\n")
        for r in done_rows:
            f.write(",".join(f"{v:.4f}" if isinstance(v, float) else str(v) for v in r) + "\n")
    s = {"requests": len(sched), "served": served, "not_served": len(sched) - served, "duration_s": duration,
         "drain_s": a.drain, "t0_epoch": t0_epoch, "tokens_per_request": a.tokens, "model": a.model, "rates": rates,
         "seed": a.seed, "tokens_per_second": served * a.tokens / duration}
    (out / f"summary{tag}.json").write_text(json.dumps(s, indent=1))
    return s, done_rows


def capacity(a):
    out = Path(a.out); steps = []
    cap = None
    for k, rate in enumerate(float(x) for x in a.steps.split(",")):
        s, rows = serve(a, [rate], a.step_s, out, tag=f"-step{k}")
        ok = [r for r in rows if r[4] == 1]
        lat = sorted(r[3] for r in ok)
        p95 = lat[min(len(lat) - 1, int(0.95 * (len(lat) - 1)))] if lat else float("inf")
        got = len(ok) / a.step_s
        inside = p95 <= a.slo_ms and got >= 0.95 * rate
        steps.append({"rate_asked": rate, "rate_served": got, "tokens_per_second": got * a.tokens, "p95_ms": p95,
                      "inside_line": inside})
        print(json.dumps(steps[-1]), flush=True)
        if not inside:
            break
        cap = steps[-1]
    res = {"slo_ms": a.slo_ms, "steps": steps, "capacity_requests_per_s": cap["rate_served"] if cap else 0.0,
           "capacity_tokens_per_s": cap["tokens_per_second"] if cap else 0.0, "model": a.model, "tokens": a.tokens}
    (out / "capacity.json").write_text(json.dumps(res, indent=1)); print(json.dumps(res))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["calibrate", "run", "capacity"])
    ap.add_argument("--out", default=os.environ.get("OUT_DIR", "llm_run"))
    ap.add_argument("--url", default=os.environ.get("LLM_URL", "http://127.0.0.1:8000"))
    ap.add_argument("--model", default=os.environ.get("LLM_MODEL", "Qwen/Qwen2.5-0.5B-Instruct"))
    ap.add_argument("--tokens", type=int, default=int(os.environ.get("LLM_TOKENS", 128)))
    ap.add_argument("--rate", type=float, default=float(os.environ.get("LLM_RATE", 0) or 0))
    ap.add_argument("--rates", default=os.environ.get("LLM_RATES", "2,6,12,4,8,2"),
                    help="requests per second, one per phase (a quiet, busy and peak hour in one run)")
    ap.add_argument("--prompt-min", type=int, default=40)
    ap.add_argument("--prompt-max", type=int, default=400)
    ap.add_argument("--seed", type=int, default=20261003)
    ap.add_argument("--calib", type=int, default=10)
    ap.add_argument("--duration", type=float, default=float(os.environ.get("DURATION", 600)))
    ap.add_argument("--drain", type=float, default=float(os.environ.get("DRAIN", 30)))
    ap.add_argument("--signal", default=os.environ.get("OMNI_SIGNAL", ""))
    ap.add_argument("--steps", default=os.environ.get("LLM_STEPS", "2,4,8,12,16,24,32,48,64"))
    ap.add_argument("--step-s", type=float, default=float(os.environ.get("LLM_STEP_S", 60)))
    ap.add_argument("--slo-ms", type=float, default=float(os.environ.get("SLO_MS", 0) or 0))
    a = ap.parse_args(argv)
    if a.cmd == "calibrate":
        calibrate(a)
    elif a.cmd == "capacity":
        if not a.slo_ms:
            raise SystemExit("capacity needs --slo-ms (the response line)")
        a.drain = min(a.drain, 10.0)
        capacity(a)
    else:
        rates = [a.rate] if a.rate > 0 else [float(x) for x in a.rates.split(",")]
        s, _ = serve(a, rates, a.duration, Path(a.out))
        print(json.dumps(s))


if __name__ == "__main__":
    main()
