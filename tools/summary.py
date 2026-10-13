#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole summary, right out of the gate (the founder's order of 13 October 2026): what Omni-Compass is, the key to its
words (GAIN, EVEN, LOSS), and every headline result with its word and its evidence class, read from the result files in
this repository. Nothing here is typed in by hand: every number comes from the file named beside it. Standard library only,
so it runs on any Python 3.8 or later straight after a pull.

  python3 tools/summary.py              the summary, as plain text for a terminal
  python3 tools/summary.py --markdown   the same, as Markdown
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import NOTICE                                       # noqa: E402  (the notice, written once)
from tools.readings import (OWN_RUNS, GAIN, EVEN, LOSS, GIVEN, key_lines, key_text, gel_of_label, labelled)  # noqa: E402

WHAT = ("Omni-Compass is a supervisory governor. It always sits on top of a system's own native controller (the Kubernetes "
        "autoscaler, a database's pool, a GPU's firmware, a building's battery controller, a robot's servo) and is never "
        "standalone. It reads every gauge of the system and moves the native controller's own settings, one pedal: push for "
        "more, lift off for less, and lifting hands every setting back toward native. Its first rule is do no harm: no "
        "gauge may be moved past native away from its aim, and a setting it cannot improve stays native. Its default brain is "
        "the max: every muscle rides its own limit, never past it and never below native; the energy that takes is shown as "
        "power given, beside the work and the speed it bought. Every benchmark has exactly two arms, native and omni (Omni on "
        "top of native), and every result runs three times (A, B and C).")

CLASSES = ("Evidence classes: P is a physical meter; L is live software, the real thing (a real Kubernetes cluster, a real "
           "database); S is our own models. S is never presented as proof.")

READ_MORE = [("README.md", "the front page, newest result first"),
             ("docs/HOW_TO_READ_THE_RESULTS.md", "how to read every table, the key at its top"),
             ("docs/OMNI_COMPASS_MANUAL.pdf", "the manual, the key in its front matter"),
             ("results/OMNI_INDEX.md", "the one combined number, test by test"),
             ("docs/BENEFIT_SHEET.md", "one number and one word per benchmark"),
             ("docs/WIRING_VERDICTS.md", "write, watch or the operator's choice, knob by knob"),
             ("results/realms_v5/REALMS_V5.md", "every muscle alone and the six organisms (modelled)"),
             ("results/grid_v5/GRID.md", "the six organisms at 1, 10 and 100 copies and runs")]


def load(path):
    p = ROOT / path
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def pct(x, nd=1):
    return "no number" if x is None else f"{x:+.{nd}f}%"


def word_of_pct(x, loss=False):
    if x is None:
        return ""
    if abs(x) < 0.05:
        return EVEN
    return GAIN if x > 0 else (LOSS if loss else GIVEN)


def evidence(bench: str) -> str:
    """The evidence class of a benefit-sheet row, by what the benchmark is."""
    b = bench.lower()
    if "organisms with the real cluster" in b:
        return "L, the cluster; S, the organism around it"
    if any(w in b for w in ("modelled", "robot arms", "power grids", "buildings and batteries", "drone swarms")):
        return "S"
    return "L"


def engine_line() -> str:
    try:
        from tools import omni_version as ov
        files = ov.engine_files()
        return f"{ov.version_of(files) or 'unversioned'}, fingerprint {ov.digest(files)[:16]} ({len(files)} files)"
    except Exception as e:                                       # the summary never fails for want of the version tool
        return f"unknown ({type(e).__name__})"


def index_part():
    d = load("results/OMNI_INDEX.json")
    if not d:
        return ["The Omni index: not built in this checkout (python3 tools/omni_index.py)."]
    h, s = d.get("headline_pct"), d.get("service_headline_pct")
    out = [f"The Omni index (evidence class L, real machines, every measure the same in all three of our runs; the three-run "
           f"tables of engines v1 and v3, each named in its table): {pct(h)} {word_of_pct(h, s is not None and s < -0.05)} on the "
           f"resource reading (work, speed, machines, energy), {pct(s)} {word_of_pct(s, True)} on the service reading (work and "
           "speed alone). Source: results/OMNI_INDEX.md."]
    for c, v in sorted((d.get("categories") or {}).items(), key=lambda kv: -(kv[1] or 0)):
        sv = (d.get("service_categories") or {}).get(c)
        out.append(f"  {c}: {pct(v)} {word_of_pct(v, sv is not None and sv < -0.05)}")
    return out


def benefit_part():
    d = load("results/BENEFIT_SHEET.json")
    if not d:
        return ["The benefit sheet: not built in this checkout (python3 tools/benefit_sheet.py)."]
    out = ["Every benchmark, one number and its word (source: docs/BENEFIT_SHEET.md; class in brackets):"]
    for r in d.get("rows", []):
        n = r.get("pct")
        out.append(f"  {r.get('benefit', '?'):<18} {pct(n):>9}  {r['benchmark']} [{evidence(r['benchmark'])}]")
    return out


def wiring_part():
    p = ROOT / "results" / "WIRING_VERDICTS.csv"
    try:
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
    except OSError:
        return ["The wiring verdicts: not built in this checkout (python3 tools/wiring_verdicts.py)."]
    out = ["Wire in, or watch, knob by knob (source: docs/WIRING_VERDICTS.md; write: Omni holds the knob; watch: the knob stays "
           "native and Omni only reads it; the operator's choice: a trade):"]
    for kind in ("real knob", "modelled simulator", "modelled muscle", "organism with the cluster inside"):
        c = Counter(r["verdict"] for r in rows if r["kind"] == kind and r["counted"] == "yes")
        if c:
            w, ch, wa = c.get("write", 0), c.get("operator's choice", 0), c.get("watch", 0)
            out.append(f"  {kind}: write {w}, the operator's choice {ch}, watch {wa}")
    return out


NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         "stack": "the four stacked", "tower": "the whole tower"}


def realms_part():
    d = load("results/realms_v5/REALMS_V5.json")
    if not d:
        return []
    run = d.get("run", {})
    head = (f"The muscles and the six organisms on engine {run.get('engine', '?')} at the {run.get('dial', '?')} (evidence class S, "
            f"our own models; run {run.get('started', '?')}, commit {str(run.get('commit', '?'))[:12]}, {run.get('muscles', '?')} "
            "muscles; source: results/realms_v5/REALMS_V5.md):")
    out = [head]
    kinds = Counter(gel_of_label(m.get("label")) or m.get("label") for m in d.get("muscles", []))
    out.append("  every muscle alone, over its loads: " + ", ".join(f"{k} {v}" for k, v in kinds.most_common()))
    for load_, orgs in (d.get("organisms") or {}).items():
        parts = []
        for name, o in orgs.items():
            sm = o.get("summary", {})
            v = sm.get("viol_pp", [None])[0]; e = sm.get("energy", [None])[0]
            nm = NAMES.get(name, name)
            parts.append(f"{nm}: {labelled(o.get('label'))}, misses {v:+.3f} pp, power given {100 * e:+.3f}%"
                         if v is not None and e is not None else f"{nm}: {labelled(o.get('label'))}")
        out.append(f"  the organisms under the {load_} load: " + "; ".join(parts))
    return out


def grid_part():
    p = ROOT / "results" / "grid_v5" / "GRID.md"
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return []
    m = re.search(r"^\*\*(Across the grid: .*?)\*\*$", text, re.M)
    return [f"The grid (source: results/grid_v5/GRID.md): {m.group(1)}"] if m else []


def build(markdown=False):
    plain = lambda s: re.sub(r"\*\*|`", "", s) if not markdown else s
    L = [NOTICE if markdown else plain(NOTICE), ""]
    L += ["# Omni-Compass: the whole summary" if markdown else "OMNI-COMPASS: THE WHOLE SUMMARY", ""]
    L += [WHAT, "", CLASSES, "", f"Engine on this checkout: {engine_line()}.", ""]
    L += key_lines() if markdown else key_text().splitlines()
    L += ["", "## The results, each with its word" if markdown else "THE RESULTS, EACH WITH ITS WORD", ""]
    for part in (index_part(), benefit_part(), wiring_part(), realms_part(), grid_part()):
        if part:
            L += part + [""]
    L += ["## Where to read more" if markdown else "WHERE TO READ MORE", ""]
    L += [f"- `{p}`: {w}" if markdown else f"  {p}: {w}" for p, w in READ_MORE]
    L += ["", OWN_RUNS, "", NOTICE if markdown else plain(NOTICE)]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--markdown", action="store_true", help="print Markdown instead of plain text")
    a = ap.parse_args(argv)
    sys.stdout.write(build(markdown=a.markdown))
    return 0


if __name__ == "__main__":
    sys.exit(main())
