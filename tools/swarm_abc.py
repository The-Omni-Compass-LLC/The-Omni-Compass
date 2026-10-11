#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table for the drone swarms (docs/OMNI_V1.md's readings, docs/SWARM_PREREGISTRATION.md): each cell run three
times as separate GitHub runs on the same frozen engine (tools/run_swarm.py). PyBullet is deterministic for a fixed step,
so the runs must give the same numbers to within one part in a thousand (PyBullet's floating point differs by that much
from one GitHub machine to the next; amendment 1 of the preregistration, made after the first A, B, C were seen and said
so): a gauge reads confirmed better or confirmed WORSE by its sign when all three runs agree, same when the change is
under one part in a million, and "the runs differ" when they do not reproduce. A cell whose
paired physics trial left the cruise native is listed as "nothing for Omni to move"; a cell with a collision in either arm
is void and listed as such. Every row is reported, losses included.
Usage: python tools/swarm_abc.py A_DIR B_DIR C_DIR --out results/live/V3_SWARM.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding swarm-<cell>/swarm-<cell>.json"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.run_swarm import GAUGES, TRIAL_OVERRIDE

SAME_REL = 1e-6
REPRO_REL = 1e-3        # PyBullet reproduces to about one part in a thousand across GitHub's machines, not to the bit (amendment 1)
COUNTS = {"late_share", "reserve_breaches", "near_miss_ticks"}      # differences, not ratios


def load(d):
    out = {}
    for f in sorted(Path(d).glob("swarm-*/swarm-*.json")):
        out[f.stem.replace("swarm-", "")] = json.loads(f.read_text())
    if not out:
        raise SystemExit(f"{d}: no swarm-<cell>/swarm-<cell>.json")
    return Path(d).resolve().name.replace("run-", ""), out


def change(rec, k):
    n, o = (rec.get("native") or {}).get(k), (rec.get("omni") or {}).get(k)
    if n is None or o is None:
        return None
    return (o - n) if (k in COUNTS or n == 0) else (o - n) / abs(n)


def reproduced(recs, k):
    for arm in ("native", "omni"):
        v = [(r.get(arm) or {}).get(k) for r in recs]
        if any(x is None for x in v):
            return all(x is None for x in v)
        if not all(abs(x - v[0]) <= REPRO_REL * max(1.0, abs(v[0])) for x in v):
            return False
    return True


def verdict(recs, k, direction):
    """better / WORSE by the gauge's own direction: lower, higher, never more (any increase is WORSE), never less."""
    if not reproduced(recs, k):
        return "**the runs differ**"
    ch = [change(r, k) for r in recs]
    if any(c is None for c in ch):
        return "no value"
    if direction == "shown":
        return "shown, not judged"
    if all(abs(c) <= SAME_REL for c in ch):
        return "same"
    signs = {(c > 0) - (c < 0) for c in ch}
    if len(signs) > 1:
        return "**the runs differ**"
    up = signs == {1}
    if direction in ("lower", "never more"):
        return "**confirmed WORSE**" if up else "**confirmed better**"
    return "**confirmed better**" if up else "**confirmed WORSE**"          # higher, never less


def engine(run):
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
    return f"{c:+.3f}" if k in COUNTS else f"{100 * c:+.2f}%"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c"); ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# Drone swarms, gym-pybullet-drones: the A/B/C confirmation (Omni v3)", "",
         "gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position "
         "controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the "
         "cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). "
         "Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw "
         "charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one "
         "part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs "
         "were seen), so a gauge reads **confirmed better** or **confirmed WORSE** when all three runs reproduce to that tolerance and "
         "give the same sign, **same** under one part in a million, and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster "
         "mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell with a "
         "collision in either arm is void. Every row is shown, losses included.", "",
         "| Run | GitHub run | Commit | Engine | Cells in the run |", "|---|---|---|---|---:|"]
    off = []; seen = []
    for tag, (run, recs) in zip("ABC", runs):
        sha, ver = engine(run)
        seen.append(ver.split(" ")[0])
        if not ver.startswith("omni-v"):
            off.append(f"{tag} (run {run}: {ver})")
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {len(recs)} |")
    label = f"Omni {seen[0][5:]}" if len(set(seen)) == 1 and seen[0].startswith("omni-v") else "the runs' engines differ"
    L[0] = L[0].replace("(Omni v3)", f"({label})")
    if len({r for r, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if off:
        L[2:2] = [f"**Not a confirmation on one frozen engine: {'; '.join(off)}.**", ""]
    cells = sorted(set().union(*(set(r) for _, r in runs)), key=lambda c: (c != "tuning", c))
    tally = {}; idle = []; void = []
    L += ["", "## Cells where Omni moved the cruise", ""]
    for c in cells:
        recs = [r.get(c) for _, r in runs]
        if any(x is None for x in recs):
            void.append((c, "missing from a run")); continue
        if any(x.get("void") for x in recs):
            void.append((c, "a collision in an arm: native " + "/".join(str(x["native"]["collisions"]) for x in recs)
                         + ", omni " + "/".join(str(x["omni"]["collisions"]) for x in recs))); continue
        if not all(x.get("omni_moves") for x in recs):
            idle.append((c, recs)); continue
        r0 = recs[0]
        L += [f"### {c}: {r0['drones']} drones x {r0['missions_per_drone']} missions, {r0['distance_m'][0]:.0f} to {r0['distance_m'][1]:.0f} m"
              + (" (the tuning swarm)" if r0.get("tuning") else "") + f"; handed back: {'yes' if all(x['omni'].get('handed_back') for x in recs) else 'NO'}", "",
              "| Gauge | native (A) | omni (A) | A | B | C | Reading |", "|---|---:|---:|---:|---:|---:|---|"]
        for k, name, direction in GAUGES:
            v = verdict(recs, k, direction)
            if v == "no value":
                continue
            if direction != "shown" and not r0.get("tuning"):
                tally.setdefault(k, {}).setdefault(v, []).append(c)
            L.append(f"| {name} | {r0['native'][k]:.4g} | {r0['omni'][k]:.4g} | {pct(change(recs[0], k), k)} | {pct(change(recs[1], k), k)} | "
                     f"{pct(change(recs[2], k), k)} | {v} |")
        L.append("")
    L += ["## Across the untouched cells Omni moved", "", "| Gauge | Confirmed better | Confirmed worse | Same | The runs differ |", "|---|---:|---|---:|---:|"]
    for k, name, direction in GAUGES:
        t = tally.get(k)
        if not t:
            continue
        w = t.get("**confirmed WORSE**", [])
        L.append(f"| {name} | {len(t.get('**confirmed better**', []))} | {len(w)}{' (' + ', '.join(w) + ')' if w else ''} | {len(t.get('same', []))} | "
                 f"{len(t.get('**the runs differ**', []))} |")
    L += ["", "## Cells where the paired trial left the cruise native: nothing for Omni to move", "",
          f"In native mode, before the counted missions, one mission at the planner's cruise and one at {TRIAL_OVERRIDE} x showed a faster "
          "mission no cheaper on the simulator's own figures, or not inside the safe tracking error, so Omni left the cruise at the "
          "planner's and both arms are the same.", "",
          "| Cell | Energy a mission at the planner's cruise (J) | At the trial speed (J) | Reproduced over A, B, C |", "|---|---:|---:|---|"]
    for c, recs in idle:
        t0 = recs[0]["physics_trial"]; f, s = t0["planner_cruise"], [v for kk, v in t0.items() if kk.startswith("override_")][0]
        rep = all(reproduced(recs, k) for k, _, _ in GAUGES)
        L.append(f"| {c} | {f['energy_per_mission_j']:.1f} | {s['energy_per_mission_j']:.1f} | {'yes' if rep else 'no'} |")
    L += ["", "## Void cells", "", "| Cell | Why |", "|---|---|"]
    for c, e in void:
        L.append(f"| {c} | {e} |")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(L)) + "\n")
    nb = sum(len(t.get("**confirmed better**", [])) for t in tally.values()); nw = sum(len(t.get("**confirmed WORSE**", [])) for t in tally.values())
    nd = sum(len(t.get("**the runs differ**", [])) for t in tally.values())
    print(f"{out}: {len(cells) - len(idle) - len(void)} cells moved ({nb} gauge-rows confirmed better, {nw} confirmed worse, {nd} where the runs differ, "
          f"the tuning cell shown and not counted), {len(idle)} nothing to move, {len(void)} void")
    return 0


if __name__ == "__main__":
    sys.exit(main())
