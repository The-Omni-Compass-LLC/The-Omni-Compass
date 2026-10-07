#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The A/B/C table for the Redis benchmark (docs/OMNI_V1.md's readings, docs/REDIS_PREREGISTRATION.md): the untouched
workloads run three times as separate GitHub runs on the same frozen engine (tools/run_redis.py), each run holding three
paired repetitions of native and omni. Within a run the paired difference (omni minus native) over its repetitions gives a
95% interval; across the three runs a gauge reads confirmed better or confirmed WORSE when all three move the same way with
every interval clear of zero, no difference beyond the noise when a run's interval includes zero (with the count of such
runs), and the runs disagree when runs clear of the noise point different ways. Failed requests: any increase in any run is
WORSE. The knob's moves are shown, never judged. The tuning workload is shown and not counted. Every row is reported,
losses included; no energy is claimed beyond the host's CPU seconds.
Usage: python tools/redis_abc.py A_DIR B_DIR C_DIR --out results/live/V3_REDIS.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding redis-<workload>/.../<workload>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.run_redis import GAUGES, SAME_REL, paired  # noqa: E402


def load(d):
    """{workload: record} and the run id, from an archived run folder (the artifact may be nested one level)."""
    out = {}
    for f in sorted(Path(d).rglob("redis-*/*.json")):
        rec = json.loads(f.read_text())
        if "reps" in rec and rec.get("reps"):
            rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
            out[rec["workload"]] = rec
    if not out:
        raise SystemExit(f"{d}: no redis-<workload>/<workload>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def engine(run_dir):
    """(commit, engine version) of the run, from its own run file, checked against the fingerprints."""
    for f in Path(run_dir).rglob("redis-*/*.json"):
        e = json.loads(f.read_text()).get("engine") or {}
        sha = e.get("commit", "")
        if sha:
            r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT, capture_output=True, text=True)
            ver = r.stdout.strip().splitlines()[0] if r.stdout.strip() else "unknown"
            return sha[:12], ver
    return "", "unknown"


def verdict(rs, direction):
    """The three-run reading of one gauge, by rule, from its three within-run paired results."""
    if any(r is None for r in rs):
        return "no value"
    if direction == "shown":
        return "shown, not judged"
    if direction == "never more":
        return "**confirmed WORSE**" if any(r["diff"] > 0 for r in rs) else ("same" if all(abs(r["diff"]) <= 1e-12 for r in rs) else "**confirmed better**")
    if all(abs(r["diff"]) <= SAME_REL * max(abs(r["native"]), 1e-12) for r in rs):
        return "same"
    clear = [r for r in rs if r["significant"]]
    signs = {(r["diff"] > 0) - (r["diff"] < 0) for r in clear}
    if len(signs) > 1:
        return "**the runs disagree**"
    if len(clear) < len(rs):
        n = len(rs) - len(clear)
        return f"no difference beyond the noise ({n} of {len(rs)} runs)"
    better = (rs[0]["diff"] > 0) == (direction == "higher")
    return "**confirmed better**" if better else "**confirmed WORSE**"


def cell(r, key):
    if r is None:
        return "n/a"
    nat, d, lo, hi = r["native"], r["diff"], r["ci95"][0], r["ci95"][1]
    if key == "failed" or not nat:
        return f"{d:+.3g} ({lo:+.3g} to {hi:+.3g})"
    return f"{100 * d / abs(nat):+.1f}% ({100 * lo / abs(nat):+.1f} to {100 * hi / abs(nat):+.1f})"


def fmt(v):
    return f"{v:.3g}" if abs(v) < 10 else f"{v:,.1f}" if abs(v) < 1000 else f"{v:,.0f}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dirs", nargs=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in a.dirs]
    eng = [engine(d) for d in a.dirs]
    L = ["# Redis, a cache's operator-set memory ceiling: the A/B/C confirmation", "",
         "Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling "
         "through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit "
         "inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the "
         "paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make "
         "a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the "
         "noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any "
         "increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are "
         "measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every "
         "row is shown, losses included.", "",
         "| Run | GitHub run | Commit | Engine | Workloads |", "|---|---|---|---|---:|"]
    off = []
    for tag, (run, recs), (sha, ver) in zip("ABC", runs, eng):
        if not ver.startswith("omni-v"):
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if len({v.split(" ")[0] for _, v in eng}) > 1:
        off.append("A, B and C are not all on the same engine")
    if off:
        L += ["", "> **Warning:** " + "; ".join(off) + "."]
    wls = sorted(set().union(*[set(r) for _, r in runs]), key=lambda w: (w != "tuning", w))
    better = worse = disagree = 0
    out = {"runs": [{"tag": t, "run": r, "commit": s, "engine": v} for t, (r, _), (s, v) in zip("ABC", runs, eng)], "workloads": {}}
    for wl in wls:
        recs = [r.get(wl) for _, r in runs]
        if any(x is None for x in recs):
            L += ["", f"## {wl}", "", "> not in every run: " + ", ".join(t for t, x in zip("ABC", recs) if x is None) + " lack it."]
            continue
        r0 = recs[0]; tuning = r0.get("tuning", False)
        L += ["", f"## {wl}: {r0['value_bytes']} B values, working set {r0['base_keys']:,} keys × notch; line {r0['line_ms']:.0f} ms, {len(r0['reps'])} paired repetitions a run"
              + (" (the tuning workload, shown and not counted)" if tuning else ""), "",
              f"Redis {r0.get('redis_version', '?')}; {r0['rate_rps']:.0f} requests a second offered; a miss costs the declared {r0['miss_penalty_ms']:.0f} ms store trip; "
              f"steps {r0['steps']} × {r0['step_s']} s; the operator's ceiling {r0['native_mb']} MB, the cover {r0['cover_mb'][0]} to {r0['cover_mb'][1]} MB.", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        out["workloads"][wl] = {}
        for k, label, dr in GAUGES:
            rs = [r["paired"].get(k) for r in recs]
            v = verdict(rs, dr)
            if not tuning:
                better += "better" in v; worse += "WORSE" in v; disagree += "disagree" in v
            nat = fmt(rs[0]["native"]) if rs[0] else "n/a"; om = fmt(rs[0]["omni"]) if rs[0] else "n/a"
            L.append(f"| {label} | {nat} | {om} | " + " | ".join(cell(r, k) for r in rs) + f" | {v} |")
            out["workloads"][wl][k] = {"reading": v.strip("*"), "runs": [None if r is None else {"native": r["native"], "omni": r["omni"], "diff": r["diff"], "ci95": r["ci95"]} for r in rs]}
        hb = all(all(x["omni"].get("handed_back") for x in r["reps"]) for r in recs)
        L += ["", f"The ceiling handed back to the operator's and read back at the end of every omni arm in every run: {'yes' if hb else '**NO**'}."]
    n_wl = sum(1 for w in wls if not any((r.get(w) or {}).get("tuning") for _, r in runs))
    L += ["", f"**Across {n_wl} untouched workloads: {better} gauge-rows confirmed better, {worse} confirmed worse, {disagree} where the runs disagree.**"]
    Path(a.out).write_text("\n".join(_legal_stamp(L)) + "\n")
    Path(a.out).with_suffix(".json").write_text(json.dumps(out, indent=1))
    print(f"{a.out}: {n_wl} untouched workloads; {better} better, {worse} worse, {disagree} disagree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
