# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The A/B/C confirmation table (docs/OMNI_V1.md): one v1 benchmark run three times as separate GitHub runs on the same
frozen engine, A the result, B and C the replications. Every judged row gets one of three readings, all three runs shown:
confirmed better or confirmed WORSE when all three runs move the same way and each run's 95% interval of the paired
difference (omni minus native) is clear of zero; no difference beyond the noise when a run's interval includes zero
(native and omni could not be told apart on that measure, which is itself the result, with the count of such runs); the
runs disagree when runs clear of the noise point different ways (the test itself is then unstable, and is looked into).
Rows that are shown but never judged (tools/live_reps.py NEUTRAL) stay unjudged. Every row is reported, losses included.
Usage: python tools/confirm_abc.py "TITLE" A_DIR B_DIR C_DIR --out results/live/V1_<NAME>.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding live-reps/LIVE_REPS.json; its engine is checked."""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from pilot.bench_report import LOWER_BETTER
from tools.live_reps import BATCH, BILL, KEYS, LABEL, NEUTRAL, ROBUST, SAME_REL

ARMS = ("compass", "bowl")        # the Omni arm's name in the run files (bench-bowl-N folders predate the rename)
CAPACITY = "work inside the response line (requests a second; the capacity test's own gauge, higher is better)"
HIGHER_BETTER = {CAPACITY}
LOWER = LOWER_BETTER | BATCH | BILL | ROBUST   # the batch queue's finish time and machines after it, a real cloud's bill, the 120 s after a kill: less is better


def robust_rows(runs):
    """The robustness test's own rows (docs/ROBUSTNESS_PREREGISTRATION.md), from each run's `robust` block (omni arm only, so
    not paired): every setting back within the allowance in every repetition, the seconds it took, the second governor, the
    governor's memory. Returns table lines and the rows as data; empty when no run carries the block."""
    blocks = []
    for _, _, _, rb in runs:
        arm = next((a for a in ARMS if rb and a in rb), None)
        blocks.append(rb[arm] if arm else None)
    if any(b is None for b in blocks):
        return [], {}
    L, rows = [], {}
    kill = all(b.get("kill_repetitions") for b in blocks)
    if kill:
        ok = all(b.get("handed_back_within_allowance_all") for b in blocks)
        v = "**confirmed: handed back within the allowance in every repetition of every run**" if ok else "**WORSE: a repetition was not handed back within the allowance**"
        cells = [f"{'yes' if b['handed_back_within_allowance_all'] else 'NO'} ({b['kill_repetitions']} reps; mean {b['handed_back_s_mean']:.0f} s, max {b['handed_back_s_max']:.0f} s"
                 + (f", never: {b['never_handed_back']}" if b.get('never_handed_back') else "") + ")" if b['handed_back_s_mean'] is not None else f"NO (never handed back in {b['never_handed_back']} reps)" for b in blocks]
        k = f"robust: every setting back at the operator's within {blocks[0]['allowance_s']:.0f} s of the kill, every repetition (the governor killed outright; the watchdog's hand-back)"
        L.append(f"| {k} | {cells[0]} | {cells[1]} | {cells[2]} | {v} |"); rows[k] = {"reading": v.strip("*"), "runs": blocks}
        sg = all(b.get("second_governor_all") for b in blocks)
        v2 = "**confirmed**" if sg else "**WORSE**"
        k2 = "robust: a second governor started after the hand-back and governed to the end, every repetition"
        L.append(f"| {k2} | {'yes' if blocks[0]['second_governor_all'] else 'NO'} | {'yes' if blocks[1]['second_governor_all'] else 'NO'} | {'yes' if blocks[2]['second_governor_all'] else 'NO'} | {v2} |")
        rows[k2] = {"reading": v2.strip("*"), "runs": [b.get("second_governor_all") for b in blocks]}
    if all(b.get("memory_ratio_max") is not None for b in blocks):
        lim = blocks[0]["memory_limit"]
        leak = any(b["memory_ratio_max"] > lim for b in blocks)
        v3 = "**WORSE: a leak (over the preregistered limit)**" if leak else f"no leak (every repetition under {lim})"
        k3 = "robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions"
        L.append(f"| {k3} | {blocks[0]['memory_ratio_max']:.3f} | {blocks[1]['memory_ratio_max']:.3f} | {blocks[2]['memory_ratio_max']:.3f} | {v3} |")
        rows[k3] = {"reading": v3.strip("*"), "runs": [b["memory_ratio_max"] for b in blocks]}
    return L, rows


def load(d):
    """(run id, the paired table of the Omni arm against native, repetitions) from an archived run folder."""
    f = next(Path(d).rglob("LIVE_REPS.json"), None)
    if f is None:
        raise SystemExit(f"{d}: no LIVE_REPS.json")
    j = json.loads(f.read_text())
    arm = next((a for a in ARMS if a in j["paired"]), None)
    if arm is None:
        raise SystemExit(f"{f}: no compass arm in the paired table ({sorted(j['paired'])})")
    run = Path(d).resolve().name.replace("run-", "")
    reps = j.get("repetitions") or {}
    n = len(set(reps.get("native", [])) & set(reps.get(arm, []))) if isinstance(reps, dict) else reps
    paired = dict(j["paired"][arm])
    cap = j.get("capacity")                                # the capacity test (a rising load): its own block in the run file
    if cap and arm in cap and "capacity_rps" in cap.get("native", {}):
        nat, om = cap["native"]["capacity_rps"], cap[arm]["capacity_rps"]
        paired[CAPACITY] = {"native": nat, "omni": om, "diff": om - nat, "ci95": list(cap[arm]["ci95"]),
                            "significant": cap[arm]["ci95"][0] > 0 or cap[arm]["ci95"][1] < 0}
    return run, paired, n, j.get("robust")


def cell(r):
    """One run's change, in percent of native where native is not zero, with its 95% interval."""
    nat, diff, lo, hi = r["native"], r["diff"], r["ci95"][0], r["ci95"][1]
    if nat:
        return f"{100 * diff / abs(nat):+.1f}% ({100 * lo / abs(nat):+.1f} to {100 * hi / abs(nat):+.1f})"
    return f"{diff:+.4g} ({lo:+.4g} to {hi:+.4g})"


def verdict(k, rs):
    """The row's reading over the three runs, by rule: better, worse, no difference the test can measure, or a
    disagreement between runs. Every judged row gets exactly one."""
    if k in NEUTRAL:
        return "shown, not judged"
    if all(abs(r["diff"]) <= SAME_REL * abs(r["native"]) for r in rs):
        return "same"
    clear = [r["ci95"][0] > 0 or r["ci95"][1] < 0 for r in rs]
    signs = [(r["diff"] > 0) - (r["diff"] < 0) for r in rs]
    if len({s for s, c in zip(signs, clear) if c}) > 1:
        return "**the runs disagree**"
    if not all(clear):
        n = sum(1 for c in clear if not c)
        return "no difference beyond the noise (all three runs)" if n == len(rs) else f"no difference beyond the noise in {n} of {len(rs)} runs"
    lower = signs[0] == -1
    if k in LOWER:
        return "**confirmed better**" if lower else "**confirmed WORSE**"
    if k in HIGHER_BETTER:
        return "**confirmed WORSE**" if lower else "**confirmed better**"
    return f"confirmed {'lower' if lower else 'higher'}"


def engine(run):
    """The Omni version the run's commit carries (tools/omni_version.py), from the GitHub run record."""
    try:
        sha = subprocess.run(["gh", "api", f"repos/the-omni-compass-llc/the-omni-compass/actions/runs/{run}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            return "?", "unknown"                          # a run whose commit cannot be read is never called v1
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
        return sha[:12], (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "?", "unknown"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title"); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = [f"# {a.title}: the A/B/C confirmation (Omni v1)", "",
         "Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C "
         "are the replications. Each cell is omni against native, the paired change in percent of native with its 95% "
         "interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three "
         "runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs "
         "counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the "
         "result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable "
         "there. Every row is shown, losses included.", "",
         "| Run | GitHub run | Commit | Engine | Paired repetitions |", "|---|---|---|---|---:|"]
    off, meta = [], []
    for tag, (run, _, n, _) in zip("ABC", runs):
        sha, ver = engine(run)
        if not ver.startswith("omni-v"):                     # a fingerprinted engine (docs/OMNI_V2.md; v1 runs keep reading as v1)
            off.append(f"{tag} (run {run}: {ver})")
        meta.append({"tag": tag, "run": run, "commit": sha, "engine": ver, "paired_repetitions": n})
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {n if n is not None else '?'} |")
    # the title names the engine the three runs carry (one engine, or it says they differ): never read across versions
    seen = [m["engine"].split(" ")[0] for m in meta]
    label = f"Omni {seen[0][5:]}" if len(set(seen)) == 1 and seen[0].startswith("omni-v") else "the runs' engines differ"
    L[0] = L[0].replace("(Omni v1)", f"({label})")
    if len({r for r, _, _, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if len({m["engine"].split(" ")[0] for m in meta}) > 1:
        off.append("A, B and C are not all on the same engine: " + ", ".join(m["engine"].split(" ")[0] for m in meta))
    if off:
        L[2:2] = [f"**Not a v1 confirmation: {'; '.join(off)}.** The readings below compare runs on different engines.", ""]
    L += ["", "| Measure | A | B | C | Reading |", "|---|---|---|---|---|"]
    tally, rows = {}, {}
    for k in [CAPACITY] + KEYS:
        rs = [p.get(k) for _, p, _, _ in runs]
        if any(r is None for r in rs):
            continue
        v = verdict(k, rs)
        tally[v] = tally.get(v, 0) + 1
        rows[k] = {"reading": v.strip("*"), "runs": [{"native": r["native"], "omni": r["omni"], "diff": r["diff"], "ci95": list(r["ci95"])} for r in rs]}
        L.append(f"| {LABEL.get(k, k)} | {cell(rs[0])} | {cell(rs[1])} | {cell(rs[2])} | {v} |")
    rob_l, rob_rows = robust_rows(runs)           # the robustness test's own rows (omni only, by rule, not paired)
    for line in rob_l:
        v = line.rsplit("|", 2)[-2].strip(); tally[v] = tally.get(v, 0) + 1
    L += rob_l; rows.update(rob_rows)
    L += ["", "Readings: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())) + "."]
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(L)) + "\n")
    # the same table as data, for the Omni index (tools/omni_index.py): every run's values and the reading, by rule
    out.with_suffix(".json").write_text(json.dumps({"title": a.title, "v1": not off, "runs": meta, "rows": rows}, indent=1) + "\n")
    print(f"{out}: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
