# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's seeded runs through the C++ (cpp/tools/run_engine_runs.cpp) vs the Python's (tools/engine_runs.py): the same
jump generator and draws, every receipt compared number by number and the two SHA-256 digests compared.

The C++ runs the twins of the engine that stands (the governor's RK4 state equations, the nervous system's authority per
organ, the compass law, the verdict), fed by the same mulberry32 stream in the same order as the Python and the live engine
page. compare() is what tools/engine_runs.py --cpp records beside the Python's digest, and what the page's proof monitor
shows in its C++ column.

Usage: python tests/test_cpp_engine_runs_parity.py OC_ENGINE_RUNS [runs] [base]"""
import csv, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools import engine_runs as ER


def cpp_runs(exe, n, base, start=0):
    """The C++'s receipts (as the Python's dicts) and its digest."""
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "runs.csv"
        subprocess.run([str(exe), str(n), str(base), str(out), str(start)], check=True, capture_output=True)
        lines = out.read_text().splitlines()
    assert lines[-1].startswith("digest,"), lines[-1]
    runs = []
    for r in csv.DictReader(lines[:-1]):
        runs.append({"k": int(r["k"]), "seed": int(r["seed"]), "x": [float(r[c]) for c in ("E", "U", "I_U", "S", "B", "B_dot")],
                     "push": float(r["push"]), "expand": int(r["expand"]), "contract": int(r["contract"]), "calm": float(r["calm"]),
                     "tau": float(r["tau"]), "meanF": float(r["meanF"]), "lastF": float(r["lastF"]), "allowed": int(r["allowed"]),
                     "used": int(r["used"])})
    return runs, lines[-1].split(",", 1)[1]


def compare(py, cpp):
    """Per run, the largest absolute difference over every number of its receipt (inf where a count or a seed differs)."""
    out = []
    for a, b in zip(py, cpp):
        w = 0.0 if (a["k"], a["seed"]) == (b["k"], b["seed"]) else float("inf")
        for k in ER.KEYS:
            xs, ys = (a[k], b[k]) if isinstance(a[k], list) else ([a[k]], [b[k]])
            for x, y in zip(xs, ys):
                w = max(w, abs(float(x) - float(y)) if k not in ER.INT_KEYS else (0.0 if int(x) == int(y) else float("inf")))
        out.append(w)
    return out + [float("inf")] * abs(len(py) - len(cpp))


def main(exe, n=50, base=ER.DEFAULT_BASE):
    py = [ER.one_run(k, base) for k in range(n)]
    cpp, dg = cpp_runs(exe, n, base)
    per = compare(py, cpp)
    worst, same = max(per), sum(1 for w in per if w == 0.0)
    assert dg == ER.digest(py), f"digests differ: C++ {dg}, Python {ER.digest(py)}"
    assert worst == 0.0, f"largest difference {worst} ({n - same} of {n} runs differ)"
    print(f"the engine's runs through the C++ vs the Python: {n} runs from base {base}, every receipt identical, digest {dg[:16]}… the same")
    return dg


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 50, int(sys.argv[3]) if len(sys.argv) > 3 else ER.DEFAULT_BASE)
