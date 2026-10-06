# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The A/B/C table for the power grid (docs/OMNI_V1.md): the untouched SimBench grids run three times as separate GitHub
runs on the same frozen engine (tools/run_pandapower.py), both load models each. pandapower is deterministic, so the three
runs must give the same numbers: a gauge reads confirmed better or confirmed WORSE by its sign when all three agree, same
when the change is under one part in a million, and "the runs differ" when they do not reproduce, which is a finding about
the simulator or the harness and is said so. Directions are the preregistration's (docs/PANDAPOWER_PREREGISTRATION.md):
energy drawn, losses and net import lower is better; any increase in bus-steps outside 0.95-1.05 is WORSE; tap operations
lower is better and were declared in advance as Omni's expected cost. Every row is reported, losses included.
Usage: python tools/pandapower_abc.py A_DIR B_DIR C_DIR --out results/live/V1_PANDAPOWER.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding pandapower-<grid>/<grid>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))

SAME_REL = 1e-6          # a change under one part in a million of the value reads "same" (amendment 11)
REPRO_REL = 1e-9         # two runs of a deterministic simulator agree to this, or they did not reproduce
MODELS = [("zip", "ZIP loads (40% Z, 30% I, 30% P)"), ("constant_power", "constant-power loads (SimBench as shipped)")]
GAUGES = [("load_energy_mwh", "energy the loads drew (MWh)", "lower"), ("losses_mwh", "line and transformer losses (MWh)", "lower"),
          ("energy_in_mwh", "net import from the upstream grid (MWh)", "lower"), ("violation_bus_share", "bus-steps outside 0.95-1.05 (share)", "never more"),
          ("tap_operations", "tap operations (wear; declared cost)", "lower"), ("vmin", "lowest voltage seen (per unit)", "shown"),
          ("vmax", "highest voltage seen (per unit)", "shown")]


def load(d):
    """{grid: record} and the run id, from an archived run folder."""
    out = {}
    for f in sorted(Path(d).glob("pandapower-*/*.json")):
        out[f.stem] = json.loads(f.read_text())
    if not out:
        raise SystemExit(f"{d}: no pandapower-<grid>/<grid>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def change(rec, model, k):
    """omni against native on one gauge, as a share of native (absolute for a share-of-steps gauge or a zero native)."""
    m = rec.get(model) or {}
    n, o = (m.get("native") or {}).get(k), (m.get("omni") or {}).get(k)
    if n is None or o is None:
        return None
    if k == "violation_bus_share" or n == 0:
        return o - n
    return (o - n) / abs(n)


def reproduced(recs, model, k):
    for arm in ("native", "omni"):
        v = [((r.get(model) or {}).get(arm) or {}).get(k) for r in recs]
        if any(x is None for x in v):
            if not all(x is None for x in v):
                return False
            continue
        if not all(abs(x - v[0]) <= REPRO_REL * max(1.0, abs(v[0])) for x in v):
            return False
    return True


def verdict(recs, model, k, direction):
    """The gauge's reading over the three runs, by rule."""
    if not reproduced(recs, model, k):
        return "**the runs differ**"
    ch = [change(r, model, k) for r in recs]
    if any(c is None for c in ch):
        return "no value"
    if direction == "shown":
        return "shown, not judged"
    if all(abs(c) <= SAME_REL for c in ch):
        return "same"
    signs = {(c > 0) - (c < 0) for c in ch}
    if len(signs) > 1:
        return "**the runs differ**"
    if direction == "never more":
        return "**confirmed WORSE**" if signs == {1} else "**confirmed better**"
    return "**confirmed WORSE**" if signs == {1} else "**confirmed better**"


def engine(run):
    """The Omni version the run's commit carries, from the GitHub run record; unknown when it cannot be read."""
    try:
        sha = subprocess.run(["gh", "api", f"repos/the-omni-compass-llc/the-omni-compass/actions/runs/{run}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            return "?", "unknown"
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
        return sha[:12], (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "?", "unknown"


def pct(c, k):
    if c is None:
        return "n/a"
    return f"{c:+.1e}" if k == "violation_bus_share" else f"{100 * c:+.2f}%"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# The power grid, every untouched SimBench grid: the A/B/C confirmation (Omni v1)", "",
         "pandapower (Fraunhofer IEE and the University of Kassel) with the SimBench benchmark grids: an independent, "
         "deterministic grid simulator with the grid's own voltage control as native. Omni sits on top of it, moving the "
         "substation setpoint one whole tap at a time under the frozen rules (`docs/PANDAPOWER_PREREGISTRATION.md`). The same "
         "grids ran three times as separate GitHub runs on the same frozen engine, a full year each, both load models. Because "
         "the simulator is deterministic, the runs must reproduce each other: a gauge reads **confirmed better** or "
         "**confirmed WORSE** when all three runs give the same sign, **same** when the change is under one part in a million, "
         "and **the runs differ** when they do not reproduce. Energy drawn, losses and import: lower is better. Bus-steps outside "
         "0.95-1.05: any increase is WORSE. Tap operations: lower is better, and more of them was declared in advance as Omni's "
         "expected cost. Every row is shown, losses included.", "",
         "| Run | GitHub run | Commit | Engine | Grids in the run |", "|---|---|---|---|---:|"]
    off = []
    for tag, (run, recs) in zip("ABC", runs):
        sha, ver = engine(run)
        if not ver.startswith("omni-v"):                     # a fingerprinted engine (docs/OMNI_V2.md; v1 runs keep reading as v1)
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if off:
        L[2:2] = [f"**Not a v1 confirmation: {'; '.join(off)}.**", ""]
    grids = sorted(set().union(*(set(r) for _, r in runs)))
    tally = {}
    for model, title in MODELS:
        L += ["", f"## {title}", ""]
        for g in grids:
            recs = [r.get(g) for _, r in runs]
            if any(x is None for x in recs):
                L += [f"### {g}", "", "missing from a run", ""]; continue
            if any(not (x.get(model) or {}).get("native") or not (x.get(model) or {}).get("omni") for x in recs):
                errs = {str((x.get(model) or {}).get("error") or "no result")[:120] for x in recs}
                L += [f"### {g}", "", f"not run: `{'; '.join(sorted(errs))}`", ""]; continue
            n0 = recs[0][model]["native"]
            L += [f"### {g}: {n0.get('steps', '?'):,} hourly steps" if isinstance(n0.get("steps"), int) else f"### {g}", "",
                  "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
            for k, name, direction in GAUGES:
                v = verdict(recs, model, k, direction)
                if v == "no value":
                    continue
                if direction != "shown":
                    tally.setdefault((model, k), {}).setdefault(v, []).append(g)
                nat, om = n0.get(k), recs[0][model]["omni"].get(k)
                fmt = (lambda x: f"{x:.3g}") if k == "violation_bus_share" else (lambda x: f"{x:,.0f}" if k == "tap_operations" else f"{x:,.4g}")
                L.append(f"| {name} | {fmt(nat)} | {fmt(om)} | {pct(change(recs[0], model, k), k)} | {pct(change(recs[1], model, k), k)} | "
                         f"{pct(change(recs[2], model, k), k)} | {v} |")
            L.append("")
    L += ["## Across the grids", "", "A grid counts only when all three runs agree.", "",
          "| Load model | Gauge | Confirmed better | Confirmed worse | Same | The runs differ |", "|---|---|---:|---|---:|---:|"]
    for model, title in MODELS:
        for k, name, direction in GAUGES:
            t = tally.get((model, k))
            if not t:
                continue
            w = t.get("**confirmed WORSE**", [])
            L.append(f"| {title.split(' (')[0]} | {name} | {len(t.get('**confirmed better**', []))} | {len(w)}{' (' + ', '.join(w) + ')' if w else ''} | "
                     f"{len(t.get('same', []))} | {len(t.get('**the runs differ**', []))} |")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(L)) + "\n")
    nb = sum(len(t.get("**confirmed better**", [])) for t in tally.values()); nw = sum(len(t.get("**confirmed WORSE**", [])) for t in tally.values())
    nd = sum(len(t.get("**the runs differ**", [])) for t in tally.values())
    print(f"{out}: {len(grids)} grids; {nb} gauge-rows confirmed better, {nw} confirmed worse, {nd} where the runs differ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
