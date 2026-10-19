# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The official runs, as recorded, for the live engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html): every three-run
table's runs A, B and C read back from their own raw files in results/live/raw, every file's SHA-256 computed and matched
against the run's own SHA256SUMS_ALL.txt, so what the page plays is the run itself and anyone can check it.

  Kubernetes (class L)  every paired repetition, native and Omni-Compass on top: each request's response time
                        (latency.csv, in 30-second windows: mean, 95th percentile, requests, failures), the cluster every
                        16 seconds (capture.csv: replicas, pods waiting for a place, nodes, processor used, the declared
                        power model), the host's processor (host_cpu.csv), the load generator's steps
                        (load_schedule.log), and Omni-Compass's own audit of every decision (audit.jsonl: the compass's
                        position and force, the writes)
  the databases (class L) every repetition of every workload, both arms: the arm's own result (arm.json)

Each benchmark's newest engine's table names its runs (results/live/V<n>_*.json). Raw files are read from the checkout
where present, else from git: main's tree while it carried them, else the branch raw (scripts/raw_archive.sh). Usage:
python3 docs/engine/export_runs.py OUT.json
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(Path(__file__).resolve().parent))
RAW = "results/live/raw"
BIN = 30                     # seconds in a response-time window
K8S = {   # benchmark file stem (without V<n>_) -> the sub-folder of its runs holding its arms ("" for the run itself)
    "GOLDILOCKS": "", "KEDA_REQUESTS": "http/", "KEDA_CPU_REQUESTS": "both/", "ALL_FOUR": "", "TRACE_GOOGLE2011": "",
    "FAULTS": "", "BATCH": "", "FAIRNESS": "", "CRUISEKUBE": "", "CAPACITY": "", "ROBUST_LONG": ""}
DB = ["REDIS", "REDIS_SERVICE", "PGBENCH", "SYSBENCH", "YCSB", "KAFKA", "KAFKA_SERVICE"]
DB_GAUGES = ["work_inside_line_rps", "rps", "p95_ms", "p99_ms", "mean_ms", "failed", "hit_rate", "cpu_busy_share", "writes"]


def raw_ref():
    """Where the raw files are read from when not checked out: main's own tree while it carried them, else the branch raw
    (fetched by scripts/raw_archive.sh fetch), whose root is what results/live/raw/ held: (ref, prefix inside that ref)."""
    def has(spec):
        return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", spec], capture_output=True).returncode == 0
    if has(f"HEAD:{RAW}"):
        return "HEAD", RAW + "/"
    for ref in ("refs/remotes/origin/raw", "refs/heads/raw"):
        if has(ref):
            return ref, ""
    return "HEAD", RAW + "/"


class Git:
    """Raw files by path: from the working tree where checked out, else from git (main's tree or the branch raw) through
    one git cat-file process."""
    def __init__(self):
        self.p = subprocess.Popen(["git", "-C", str(ROOT), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.tree = None
        self.ref, self.inside = raw_ref()

    def spec(self, path: str) -> str:
        return f"{self.ref}:{self.inside}{path[len(RAW) + 1:]}" if path.startswith(RAW + "/") else f"HEAD:{path}"

    def read(self, path: str):
        f = ROOT / path
        if f.is_file():
            return f.read_bytes()
        self.p.stdin.write(f"{self.spec(path)}\n".encode()); self.p.stdin.flush()
        head = self.p.stdout.readline().decode().split()
        if len(head) < 3 or head[1] == "missing":
            return None
        data = self.p.stdout.read(int(head[2])); self.p.stdout.read(1)
        return data

    def files(self, prefix: str) -> list:
        if self.tree is None:
            args = [self.ref, RAW + "/"] if self.inside else [self.ref]
            out = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", *args],
                                 capture_output=True, text=True).stdout.split("\n")
            self.tree = [x if self.inside else f"{RAW}/{x}" for x in out if x]
        return [x for x in self.tree if x.startswith(prefix)]


def run_dir(g: Git, run_id: str):
    for d in {"/".join(x.split("/")[:4]) for x in g.files(RAW + "/") if run_id in x.split("/")[3]}:
        return d
    return None


class Sums:
    """A run's own SHA256SUMS_ALL.txt, and every file read checked against it."""
    def __init__(self, g: Git, d: str):
        self.g, self.d, self.checked, self.ok, self.missing = g, d, 0, 0, []
        raw = g.read(f"{d}/SHA256SUMS_ALL.txt") or b""
        self.sha_of_list = hashlib.sha256(raw).hexdigest() if raw else None
        self.table = {}
        for ln in raw.decode("utf-8", "replace").splitlines():
            parts = ln.split(None, 1)
            if len(parts) == 2:
                self.table[parts[1].strip().lstrip("./")] = parts[0]

    def read(self, rel: str):
        data = self.g.read(f"{self.d}/{rel}")
        if data is None:
            return None
        self.checked += 1
        if self.table.get(rel) == hashlib.sha256(data).hexdigest():
            self.ok += 1
        else:
            self.missing.append(rel)
        return data


def serial(r):
    """The run's whole serial number: the full commit it ran (git), and the full SHA-256 fingerprint of the engine that
    commit carries (OMNI_V<n>.json), so anyone can rerun the same engine on the same commit and check every file."""
    out = {}
    c = str(r.get("commit") or "")
    if re.fullmatch(r"[0-9a-f]{7,40}", c):
        try:
            full = subprocess.run(["git", "rev-parse", "--verify", "--quiet", c + "^{commit}"], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
            if re.fullmatch(r"[0-9a-f]{40}", full):
                out["commit_full"] = full
        except (OSError, subprocess.SubprocessError):
            pass                                          # no git here: the short commit the table names stands alone
    m = re.match(r"omni-v(\d+)", str(r.get("engine") or ""))
    f = ROOT / f"OMNI_V{m.group(1)}.json" if m else None
    if f and f.exists():
        out["engine_digest_full"] = json.loads(f.read_text(encoding="utf-8")).get("digest")
    return out


HIST_MS = [50, 100, 200, 300, 500, 1000, 2000]                     # the heatmap's bucket edges (ms); 500 ms is the line


def pct(xs, q):
    if not xs:
        return None
    s = sorted(xs)
    return s[min(len(s) - 1, int(q * len(s)))]


OFFICIAL = ["response time (ms), mean", "response time (ms), 95th percentile", "response time (ms), 99th percentile",
            "time over the response line (% of samples)", "failed requests (%)",
            "alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)",
            "HPA replicas, mean", "pods started", "worker nodes in service, mean", "node-hours", "energy (Wh)",
            "host CPU busy, the real machine under kind (%)",
            "settings commands the governor wrote on its own (no person touched either arm)"]


def official(s: Sums, rel: str, slo: float) -> dict:
    """The repository's own scorer (tools/live_reps.py arm_gauges) on this repetition's own files, as the three-run
    table's run was scored: every file of the folder laid out as the run wrote it, each SHA-256-checked as it is read."""
    import os
    import tempfile
    from tools import live_reps as LR
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / rel.rsplit("/", 1)[-1]
        d.mkdir(parents=True)
        for x in s.g.files(f"{s.d}/{rel}/"):
            data = s.read(x[len(s.d) + 1:])
            if data is not None:
                (d / x.rsplit("/", 1)[-1]).write_bytes(data)
        old = os.environ.get("SLO_MS"); os.environ["SLO_MS"] = str(slo)
        try:
            import contextlib, io as _io
            with contextlib.redirect_stdout(_io.StringIO()):
                g = LR.arm_gauges(d)
        except Exception as e:                                      # a folder the scorer cannot read: said, never guessed
            return {"error": f"{type(e).__name__}: {e}"[:200]}
        finally:
            if old is None:
                os.environ.pop("SLO_MS", None)
            else:
                os.environ["SLO_MS"] = old
    return {k: (None if (isinstance(g.get(k), float) and math.isnan(g[k])) else g.get(k)) for k in OFFICIAL}


def arm_k8s(s: Sums, rel: str, omni: bool, slo: float = 500.0) -> dict:
    out = {"official": official(s, rel, slo)}
    lat = s.read(f"{rel}/latency.csv")
    if lat:
        rows = list(csv.DictReader(io.StringIO(lat.decode("utf-8", "replace"))))
        bins, allv, fails = {}, [], 0
        for r in rows:
            try:
                t, ms, ok = float(r["elapsed_seconds"]), float(r["latency_ms"]), r.get("ok", "1") == "1"
            except (KeyError, ValueError):
                continue
            b = bins.setdefault(int(t // BIN), [[], 0, []])
            b[0].append(ms); b[2].append((t, ms)); allv.append(ms)
            if not ok:
                b[1] += 1; fails += 1
        last = max(bins) if bins else -1
        # each half minute: mean, 95th percentile, requests, failed; then the candle (the first, highest, lowest and last
        # response of the window, in the order they were answered), the median, the 99th percentile, and the window's
        # responses counted in the buckets of HIST_MS (for the heatmap)
        def window(v, tv):
            tv = sorted(tv)
            return [round(sum(v) / len(v), 1), round(pct(v, 0.95), 1), len(v), None,
                    round(tv[0][1], 1), round(max(v), 1), round(min(v), 1), round(tv[-1][1], 1),
                    round(pct(v, 0.5), 1), round(pct(v, 0.99), 1), [sum(1 for x in v if lo <= x < hi) for lo, hi in zip([0] + HIST_MS, HIST_MS + [math.inf])]]
        out["lat"] = []
        for k in range(last + 1):
            if k in bins and bins[k][0]:
                row = window(bins[k][0], bins[k][2]); row[3] = bins[k][1]
            else:
                row = [None, None, 0, 0]
            out["lat"].append(row)
        out["sum"] = {"requests": len(allv), "failed": fails, "mean_ms": round(sum(allv) / len(allv), 2) if allv else None,
                      "p95_ms": round(pct(allv, 0.95), 1) if allv else None, "p99_ms": round(pct(allv, 0.99), 1) if allv else None}
    cap = s.read(f"{rel}/capture.csv")
    if cap:
        rows = list(csv.DictReader(io.StringIO(cap.decode("utf-8", "replace"))))
        def f(r, k):
            try:
                return float(r.get(k) or "nan")
            except ValueError:
                return float("nan")
        out["cap"] = [[int(f(r, "elapsed_seconds")), f(r, "hpa_current_replicas"), f(r, "pods_pending"), f(r, "nodes_ready"),
                       f(r, "used_cpu_m"), f(r, "power_w")] for r in rows[::2]]
        out["cap"] = [[None if isinstance(v, float) and math.isnan(v) else v for v in row] for row in out["cap"]]
    host = s.read(f"{rel}/host_cpu.csv")
    if host:
        rows = list(csv.DictReader(io.StringIO(host.decode("utf-8", "replace"))))
        try:
            t0 = float(rows[0]["epoch_s"]); hb = {}
            for r in rows:
                hb.setdefault(int((float(r["epoch_s"]) - t0) // BIN), []).append(float(r["busy"]))
            out["host"] = [round(sum(hb[k]) / len(hb[k]), 3) if k in hb else None for k in range(max(hb) + 1)]
        except (IndexError, KeyError, ValueError):
            pass
    load = s.read(f"{rel}/load_schedule.log")
    if load:
        steps, t0 = [], None
        for ln in load.decode("utf-8", "replace").splitlines():
            m = re.match(r"(\d\d):(\d\d):(\d\d) .*-> *(\d+)", ln)
            if m:
                sec = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
                t0 = sec if t0 is None else t0
                steps.append([(sec - t0) % 86400, int(m.group(4))])
        out["load"] = steps
    if omni:
        aud = s.read(f"{rel}/audit.jsonl")
        if aud:
            dec, writes, t0, beats, cores = [], 0, None, [], None
            for ln in aud.decode("utf-8", "replace").splitlines():
                try:
                    a = json.loads(ln)
                except json.JSONDecodeError:
                    continue
                if not isinstance(a, dict):
                    continue
                t0 = a.get("time", t0) if t0 is None else t0
                if "write" in a or "writes" in a:
                    writes += 1
                if isinstance(a.get("decision_ms"), (int, float)) and isinstance(a.get("time"), (int, float)):
                    beats.append([a["time"], a["decision_ms"]])          # the heart: one beat per decision, its own time
                if isinstance(a.get("overhead"), dict) and isinstance(a["overhead"].get("cores_mean"), (int, float)):
                    cores = a["overhead"]["cores_mean"]
                d = a.get("decision") if isinstance(a, dict) else None
                if isinstance(d, dict):
                    law = d.get("compass_law") if isinstance(d.get("compass_law"), dict) else {}
                    dec.append([round(a.get("time", t0) - t0, 1), law.get("position"), law.get("force"), d.get("nodes_recommended"),
                                law.get("verdict_state")])
            step = max(1, len(dec) // 150)
            out["dec"], out["writes"] = dec[::step], writes
            if beats and t0 is not None:
                bs = max(1, len(beats) // 400)
                out["beats"] = [[round(t - t0, 1), round(ms, 1)] for t, ms in beats][::bs]
                out["beats_n"], out["heart_cores"] = len(beats), cores
    return out


def k8s_run(g: Git, run: dict, sub: str):
    d = run_dir(g, str(run["run"]))
    if not d:
        return None
    s = Sums(g, d)
    arms = sorted({x[len(d) + 1:].rsplit("/", 1)[0] for x in g.files(f"{d}/{sub}") if x.endswith("/latency.csv")})
    reps = {}
    for rel in arms:
        m = re.search(r"bench-(native|compass)-(\d+)$", rel)
        if not m:
            continue
        group = rel[:m.start()].strip("/")
        reps.setdefault((group, int(m.group(2))), {})["omni" if m.group(1) == "compass" else "native"] = rel
    out = []
    for (group, n), pr in sorted(reps.items()):
        if "native" in pr and "omni" in pr:
            out.append({"group": group, "n": n, "native": arm_k8s(s, pr["native"], False), "omni": arm_k8s(s, pr["omni"], True)})
    # the run's own scored result, and the page's per-repetition scoring checked against it: the mean over repetitions of
    # the scorer's gauges must equal the run's LIVE_REPS.json means (the table's own numbers)
    lr = None
    for cand in (f"{sub}LIVE_REPS.json", "LIVE_REPS.json", "live-reps/LIVE_REPS.json"):
        if cand in s.table:
            raw = s.read(cand)
            lr = json.loads(raw.decode("utf-8").replace("NaN", "null")) if raw else None
            break
    agree = None
    if lr and out:
        worst = 0.0
        for arm, key in (("native", "native"), ("omni", "compass")):
            for k in OFFICIAL:
                vals = [r[arm]["official"].get(k) for r in out if isinstance(r[arm]["official"].get(k), (int, float))]
                ref = (lr.get("means", {}).get(key) or {}).get(k)
                if vals and isinstance(ref, (int, float)) and math.isfinite(ref):
                    m = sum(vals) / len(vals)
                    worst = max(worst, abs(m - ref) / max(1.0, abs(ref)))
        agree = worst
    paired = {k: v for k, v in ((lr or {}).get("paired", {}).get("compass") or {}).items() if k in OFFICIAL}
    return {"dir": d, "sums_sha256": s.sha_of_list, "checked": s.checked, "ok": s.ok, "unmatched": s.missing[:5],
            "official_paired": paired, "official_agree": agree, "reps": out}


def db_run(g: Git, run: dict):
    d = run_dir(g, str(run["run"]))
    if not d:
        return None
    s = Sums(g, d)
    rows = []
    for x in sorted(g.files(d + "/")):
        m = re.search(r"/([^/]+)/rep-(\d+)/(native|omni)/arm\.json$", x)
        if not m:
            continue
        data = s.read(x[len(d) + 1:])
        try:
            a = json.loads(data)
        except (TypeError, json.JSONDecodeError):
            continue
        rows.append({"workload": m.group(1), "rep": int(m.group(2)), "arm": m.group(3),
                     **{k: a.get(k) for k in DB_GAUGES if isinstance(a.get(k), (int, float))}})
    return {"dir": d, "sums_sha256": s.sha_of_list, "checked": s.checked, "ok": s.ok, "unmatched": s.missing[:5], "rows": rows}


def needed_dirs() -> list:
    """The raw folders the page plays back: the runs every benchmark's newest table names (for a sparse checkout)."""
    import export_scenarios as XS
    g, out = Git(), []
    for base in list(K8S) + DB:
        n, stem = XS.newest(f"V7_{base}")
        meta = json.loads((ROOT / "results" / "live" / f"{stem}.json").read_text(encoding="utf-8"))
        for r in meta.get("runs", []):
            d = run_dir(g, str(r.get("run") if isinstance(r, dict) else r))
            if d:
                out.append(d)
    return sorted(set(out))


def main(out_path):
    import export_scenarios as XS
    g = Git()
    benches = []
    for base, kind in [(b, "k8s") for b in K8S] + [(b, "db") for b in DB]:
        n, stem = XS.newest(f"V7_{base}")
        meta = json.loads((ROOT / "results" / "live" / f"{stem}.json").read_text(encoding="utf-8"))
        runs, raw_runs = [], meta.get("runs", [])
        if raw_runs and not isinstance(raw_runs[0], dict):            # a table that lists its runs by id alone
            eng = meta.get("engines") or [None] * len(raw_runs)
            raw_runs = [{"tag": "ABC"[i] if i < 3 else str(i + 1), "run": x, "engine": eng[i] if i < len(eng) else None}
                        for i, x in enumerate(raw_runs)]
        for r in raw_runs:
            rec = k8s_run(g, r, K8S[base]) if kind == "k8s" else db_run(g, r)
            if rec:
                if not r.get("commit") and rec.get("dir"):          # a table that names its runs by id alone: the run's own RUN.txt names its commit
                    m = re.search(rb"^commit=([0-9a-f]{7,40})", g.read(f"{rec['dir']}/RUN.txt") or b"", re.M)
                    if m:
                        r = dict(r, commit=m.group(1).decode())
                runs.append({"tag": r.get("tag"), "id": str(r.get("run")), "commit": r.get("commit"), "engine": r.get("engine"), **serial(r), **rec})
        title = meta.get("title") or (ROOT / "results" / "live" / f"{stem}.md").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").split(": the A/B/C")[0]
        benches.append({"key": base, "kind": kind, "file": f"results/live/{stem}.md", "engine": f"omni-v{n}", "title": title, "runs": runs})
        ck, okk = sum(r["checked"] for r in runs), sum(r["ok"] for r in runs)
        ag = [r.get("official_agree") for r in runs if r.get("official_agree") is not None]
        print(f"runs {stem:22s} {len(runs)} runs, {ck} files read, {okk} match their run's SHA-256 list"
              + (f"; the scorer per repetition against the run's own result: largest relative difference {max(ag):.1e}" if ag else ""))
    Path(out_path).write_text(json.dumps({"bin_s": BIN, "hist_ms": HIST_MS, "benchmarks": benches}, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--dirs"]:
        print("\n".join("/" + d + "/" for d in needed_dirs()))
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else "runs.json")
