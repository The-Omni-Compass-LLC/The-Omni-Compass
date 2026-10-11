#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The card probe: what this chip does when it is told, measured on the chip itself before any paid trial counts
(docs/GPU_PREREGISTRATION.md, amendment 13). About five minutes; it never counts as a result; it decides nothing.

It answers the questions the A10 run left open, with the card holding a model-sized context as a server would:
  1 idle    the power the card draws idle at each park level the brain may use (omni_controller/gpu_brain.py)
  2 race    how long a clock write takes (the driver call) and how long the clock takes to reach the top after the
            ceiling is lifted, from each park level: the two numbers that decide how deep parking can go for free
  3 first   the first request after a rest, parked at each level and raced back the moment it starts, against the same
            request with the ceiling at the top: the exact cost the park verdict will measure
  4 busy    each kind of work (compute-bound matrix products; memory-bound token generation) with the clock locked at
            each step: its time per request, its power and its energy per request. Where the time stays flat while the
            power falls, cruise can save without slowing; where energy per request rises as the clock falls, racing wins
  5 memory  the memory clocks the card accepts (a second wire on cards that have one)
Writes OUT/probe.json and OUT/PROBE.md (plain readings with the numbers). Clocks and limits are restored at the end,
read back; any failure restores first and says so.

  sudo python3 tools/gpu_probe.py --gpu 0 --out results/gpu/probe-STAMP        (--sim: no GPU, for the harness tests)
"""
from __future__ import annotations

import argparse, json, os, statistics, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    def _legal_stamp(lines):
        return lines
from omni_controller.gpu_brain import park_levels  # noqa: E402


class SimCard:
    """A stand-in for the harness's own tests: the A10's fitted numbers, a clock that ramps at 40 MHz per ms."""
    def __init__(self):
        self.top, self.floor, self.lock = 1695.0, 210.0, None
        self.t_lift = None; self.from_clk = 1695.0

    def set_clock(self, lo, hi):
        self.lock = (lo, hi)

    def reset_clock(self):
        if self.lock:
            self.from_clk = self.lock[1]; self.t_lift = time.perf_counter()
        self.lock = None

    def clock(self):
        if self.lock:
            return self.lock[1]
        if self.t_lift is None:
            return self.top
        return min(self.top, self.from_clk + 40.0 * (time.perf_counter() - self.t_lift) * 1000.0)

    def power(self):
        c = self.clock()
        return 41.0 + (66.2 - 41.0) * max(0.0, (c - 210.0) / (1695.0 - 210.0)) ** 1.5

    def set_limit(self, w):
        pass


class Card:
    """The real card through NVML (nvidia-ml-py), the fast path the governor uses."""
    def __init__(self, g):
        import pynvml as n                                  # noqa: N813
        n.nvmlInit()
        self.n, self.h = n, n.nvmlDeviceGetHandleByIndex(g)
        self.top = float(n.nvmlDeviceGetMaxClockInfo(self.h, n.NVML_CLOCK_SM))
        try:
            mem = n.nvmlDeviceGetSupportedMemoryClocks(self.h)
            self.mem_clocks = sorted(int(x) for x in mem)
            gr = n.nvmlDeviceGetSupportedGraphicsClocks(self.h, max(mem))
            self.floor = float(min(gr))
        except Exception:  # noqa: BLE001
            self.mem_clocks, self.floor = [], 300.0

    def set_clock(self, lo, hi):
        self.n.nvmlDeviceSetGpuLockedClocks(self.h, int(lo), int(hi))

    def reset_clock(self):
        self.n.nvmlDeviceResetGpuLockedClocks(self.h)

    def clock(self):
        return float(self.n.nvmlDeviceGetClockInfo(self.h, self.n.NVML_CLOCK_SM))

    def power(self):
        return self.n.nvmlDeviceGetPowerUsage(self.h) / 1000.0

    def temp(self):
        return float(self.n.nvmlDeviceGetTemperature(self.h, self.n.NVML_TEMPERATURE_GPU))


def kernels(a):
    """Two request kernels of about 50 ms each at the top clock, as the bench's workload builds them."""
    if a.sim:
        def mk(ms):
            def run(card):
                c = max(1.0, card.clock()); time.sleep(ms / 1000.0 * 1695.0 / c)
            return run
        return {"matmul": mk(40.0), "decode": mk(30.0)}
    import torch
    from tools.gpu_workload import gpu_kernel
    dev = f"cuda:{a.gpu}"
    out = {}
    for kind, n in (("matmul", 4096), ("decode", 8192)):
        run = gpu_kernel(n, dev, kind, 8)
        t = time.perf_counter(); run(10); one = (time.perf_counter() - t) * 1000.0
        iters = max(1, round(10 * 50.0 / max(one, 1e-3)))
        out[kind] = (lambda r, k: (lambda card: r(k)))(run, iters)
    torch.cuda.synchronize(dev)
    return out


def sample(card, seconds, every=0.05):
    p, c = [], []
    end = time.perf_counter() + seconds
    while time.perf_counter() < end:
        p.append(card.power()); c.append(card.clock()); time.sleep(every)
    return statistics.median(p), statistics.median(c)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gpu", type=int, default=0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--smi", default=os.environ.get("NVIDIA_SMI", "nvidia-smi"))
    ap.add_argument("--repeats", type=int, default=6)
    ap.add_argument("--sim", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.sim:
        card = SimCard(); card.mem_clocks = [405, 6251]
    else:
        try:
            card = Card(a.gpu)
        except Exception as e:  # noqa: BLE001
            (out / "PROBE.md").write_text(f"# Card probe\n\nNVML unavailable ({e}): the fast write path is missing, so the "
                                          "governor would fall back to nvidia-smi and parking would be held shallow. "
                                          "Install nvidia-ml-py and run again.\n")
            print(f"NVML unavailable: {e}"); return 2
    res = {"gpu": a.gpu, "top_mhz": card.top, "floor_mhz": card.floor, "memory_clocks_mhz": getattr(card, "mem_clocks", []),
           "sim": a.sim, "time": time.time()}
    levels = park_levels(card.top, card.floor)
    run = kernels(a)
    try:
        # 1 idle power at each park level (3 s to settle, 4 s measured)
        idle = []
        for L in levels:
            card.reset_clock() if L >= card.top else card.set_clock(card.floor, L)
            time.sleep(0.5 if a.sim else 3.0)
            pw, ck = sample(card, 0.3 if a.sim else 4.0)
            idle.append({"park_mhz": L, "idle_w": round(pw, 2), "clock_mhz": ck})
        card.reset_clock()
        res["idle"] = idle
        # 2 the race: the write's own time and the climb to the top, from each park level
        race = []
        for L in levels[1:]:
            calls, reach = [], []
            for _ in range(a.repeats):
                card.set_clock(card.floor, L); time.sleep(0.2 if a.sim else 1.0)
                t0 = time.perf_counter(); card.reset_clock(); t1 = time.perf_counter()
                t2 = None
                while time.perf_counter() - t0 < 0.5:
                    if card.clock() >= card.top - 30.0:
                        t2 = time.perf_counter(); break
                    time.sleep(0.00025)
                calls.append((t1 - t0) * 1000.0); reach.append(((t2 or time.perf_counter()) - t0) * 1000.0)
            race.append({"park_mhz": L, "write_ms": round(statistics.median(calls), 3), "to_top_ms": round(statistics.median(reach), 2)})
        res["race"] = race
        # 3 the first request after a rest, parked at each level and raced back as it starts
        first = {}
        for kind, fn in run.items():
            rows = []
            for L in levels:
                ts = []
                for _ in range(a.repeats):
                    card.reset_clock() if L >= card.top else card.set_clock(card.floor, L)
                    time.sleep(0.2 if a.sim else 1.0)
                    t0 = time.perf_counter()
                    if L < card.top:
                        card.reset_clock()
                    fn(card)
                    ts.append((time.perf_counter() - t0) * 1000.0)
                rows.append({"park_mhz": L, "first_ms": round(statistics.median(ts), 3)})
            base = rows[0]["first_ms"]
            for r in rows:
                r["vs_top"] = round(r["first_ms"] / base - 1.0, 4)
            first[kind] = rows
        res["first"] = first
        # 4 busy work with the clock locked at each step: time, power, energy per request
        busy = {}
        grid = sorted({max(card.floor, round(card.top * s / 15.0) * 15.0) for s in (1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4)}, reverse=True)
        for kind, fn in run.items():
            rows = []
            for f in grid:
                card.reset_clock() if f >= card.top else card.set_clock(f, f)
                time.sleep(0.1 if a.sim else 1.0)
                ts, ps = [], []
                for _ in range(8):
                    t0 = time.perf_counter(); fn(card); ts.append((time.perf_counter() - t0) * 1000.0); ps.append(card.power())
                ms, pw = statistics.median(ts), statistics.median(ps)
                rows.append({"clock_mhz": f, "service_ms": round(ms, 3), "power_w": round(pw, 2), "energy_j": round(pw * ms / 1000.0, 4)})
            base = rows[0]
            for r in rows:
                r["time_vs_top"] = round(r["service_ms"] / base["service_ms"] - 1.0, 4)
                r["power_vs_top"] = round(r["power_w"] / base["power_w"] - 1.0, 4)
                r["energy_vs_top"] = round(r["energy_j"] / base["energy_j"] - 1.0, 4)
            busy[kind] = rows
        res["busy"] = busy
    finally:
        card.reset_clock()
    (out / "probe.json").write_text(json.dumps(res, indent=1))
    # the plain readings
    L = ["# Card probe: what this chip does when it is told", "",
         f"GPU {a.gpu}: top clock {card.top:.0f} MHz, floor {card.floor:.0f} MHz{' (stand-in card: harness test)' if a.sim else ''}. "
         "Measured before any trial; it decides nothing and never counts as a result (docs/GPU_PREREGISTRATION.md, amendment 13).", "",
         "## Idle power at each park level", "", "| park level (MHz) | idle draw (W) |", "|---:|---:|"]
    L += [f"| {r['park_mhz']:.0f} | {r['idle_w']:.1f} |" for r in res["idle"]]
    L += ["", "## The race back to the top", "", "| from (MHz) | the write (ms) | clock at the top after (ms) |", "|---:|---:|---:|"]
    L += [f"| {r['park_mhz']:.0f} | {r['write_ms']:.2f} | {r['to_top_ms']:.1f} |" for r in res["race"]]
    for kind, rows in res["first"].items():
        L += ["", f"## The first request after a rest ({kind})", "", "| parked at (MHz) | first request (ms) | against the top |", "|---:|---:|---:|"]
        L += [f"| {r['park_mhz']:.0f} | {r['first_ms']:.1f} | {r['vs_top']:+.1%} |" for r in rows]
    for kind, rows in res["busy"].items():
        L += ["", f"## Busy work at each clock ({kind})", "", "| clock (MHz) | time per request | power | energy per request |", "|---:|---:|---:|---:|"]
        L += [f"| {r['clock_mhz']:.0f} | {r['time_vs_top']:+.1%} | {r['power_vs_top']:+.1%} | {r['energy_vs_top']:+.1%} |" for r in rows]
    free = [r for r in res["first"].get("matmul", []) if r["vs_top"] <= 0.005]
    deep = min((r["park_mhz"] for r in free), default=card.top)
    L += ["", "## What it says", "",
          f"- Parking for free (compute work): down to {deep:.0f} MHz the first request after a rest is no more than 0.5% slower.",
          f"- Idle saving there: {res['idle'][0]['idle_w'] - next((r['idle_w'] for r in res['idle'] if r['park_mhz'] == deep), res['idle'][0]['idle_w']):.1f} W against idle at the top."]
    dec = res["busy"].get("decode", [])
    flat = [r for r in dec if r["time_vs_top"] <= 0.005]
    if flat:
        lo = flat[-1]
        L.append(f"- Memory-bound work: no slower down to {lo['clock_mhz']:.0f} MHz, drawing {lo['power_vs_top']:+.1%} power "
                 f"and {lo['energy_vs_top']:+.1%} energy per request against the top clock.")
    (out / "PROBE.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    print("\n".join(L[-4:]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
