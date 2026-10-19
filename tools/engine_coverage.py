#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How much of the engine the tests run: line coverage of every Python file in the engine that stands, under the whole
test suite (docs/ENGINE_COVERAGE.md).

The measurement runs every test the repository has (the unittest suite, then each file tools/function_tests.py runs) under
coverage.py, counting only the engine's fingerprinted Python files, and keeps one line per file in
results/ENGINE_COVERAGE.json. It takes about a quarter of an hour, so verify.py checks only that the page is what the record
says; the record names the commit it was measured on.

  python3 tools/engine_coverage.py --measure   run the whole suite under coverage and write the record and the page
  python3 tools/engine_coverage.py             write the page from the record
  python3 tools/engine_coverage.py --check     exit 1 if the page is not what the record gives
"""
from __future__ import annotations

import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402

DATA = ROOT / "results" / "ENGINE_COVERAGE.json"
PAGE = ROOT / "docs" / "ENGINE_COVERAGE.md"


def engine_manifest():
    from tools import omni_version as ov
    ver = ov.version_of(ov.engine_files()) or "unversioned"
    files = json.loads((ROOT / f"OMNI_V{ver.split('v')[-1]}.json").read_text())["files"] if ver.startswith("omni-v") else []
    return ver, sorted(f for f in files if f.endswith(".py"))


def measure() -> dict:
    ver, files = engine_manifest()
    inc = ",".join(files)
    with tempfile.TemporaryDirectory() as t:
        env = {**os.environ, "COVERAGE_FILE": str(Path(t) / ".coverage")}
        py = [sys.executable, "-m", "coverage", "run", f"--include={inc}"]
        subprocess.run(py + ["-m", "unittest", "discover", "-s", "tests", "-t", "."], cwd=ROOT, env=env,
                       capture_output=True, text=True)
        listed = subprocess.run([sys.executable, "tools/function_tests.py", "--list"], cwd=ROOT, capture_output=True,
                                text=True).stdout.split("\n")
        for ln in listed:
            parts = ln.split()
            if len(parts) == 2 and parts[1].startswith("tests/") and parts[1].endswith(".py"):
                subprocess.run(py[:3] + ["--append", f"--include={inc}", "tools/function_tests.py", "--one", parts[1]],
                               cwd=ROOT, env=env, capture_output=True, text=True, timeout=900)
        out = Path(t) / "cov.json"
        subprocess.run([sys.executable, "-m", "coverage", "json", "-o", str(out)], cwd=ROOT, env=env, capture_output=True)
        rep = json.loads(out.read_text())
    sha = "commit `" + subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()[:12] + "`"
    per = {f: {"statements": v["summary"]["num_statements"], "missed": v["summary"]["missing_lines"]}
           for f, v in sorted(rep["files"].items())}
    return {"engine": ver, "commit": sha, "files": per}


def page(d: dict) -> str:
    tot = sum(v["statements"] for v in d["files"].values())
    miss = sum(v["missed"] for v in d["files"].values())
    rows = sorted(((f, v) for f, v in d["files"].items() if v["statements"]),        # an empty __init__.py has nothing to run
                  key=lambda kv: (kv[1]["statements"] - kv[1]["missed"]) / kv[1]["statements"])
    L = ["# How much of the engine the tests run", "",
         f"Line coverage of every Python file in the engine that stands ({d['engine']}), under the whole test suite: the "
         "unittest suite and every file `tools/function_tests.py` runs. Measured with coverage.py by `python3 "
         f"tools/engine_coverage.py --measure` on {d['commit']}; `tools/engine_coverage.py --check`, run by "
         "`verify.py`, fails a push where this page is not what `results/ENGINE_COVERAGE.json` records.", "",
         f"**{100 * (tot - miss) / tot:.0f}% of the engine's {tot:,} statements run under the tests** "
         f"({tot - miss:,} run, {miss:,} not). Coverage counts lines a test executes, not what it asserts: the properties "
         "the tests check are in `tests/test_engine_properties.py`, and the proofs of the core in `docs/ENGINE_PROOFS.md`.", "",
         "| Engine file | Statements | Run by the tests | Coverage |", "|---|---:|---:|---:|"]
    for f, v in rows:
        s, m = v["statements"], v["missed"]
        L.append(f"| `{f}` | {s:,} | {s - m:,} | {100 * (s - m) / max(1, s):.0f}% |")
    low = [f for f, v in rows if v["statements"] and (v["statements"] - v["missed"]) / v["statements"] < 0.6]
    L += ["", "## Where the tests reach least", "",
          "Files under 60%: " + (", ".join(f"`{f}`" for f in low) if low else "none") + ". The CityLearn runner is "
          "exercised by its own benchmark on GitHub (`citylearn.yml`, three runs on every engine) rather than by a unit test; "
          "the stack simulator, the shield and the speed and mathdrive modules hold paths the live governors do not call. "
          "Raising each to the level of the rest is the next tests' work: no engine file changes for a test.", ""]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--from-json", help="a coverage.py JSON report to record instead of measuring (its engine and commit given)")
    a = ap.parse_args(argv)
    if a.measure:
        d = measure()
        DATA.write_text(json.dumps(d, indent=1) + "\n")
    elif a.from_json:
        rep = json.loads(Path(a.from_json).read_text())
        ver, _ = engine_manifest()
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()[:12]
        d = {"engine": ver, "commit": sha, "files": {f: {"statements": v["summary"]["num_statements"],
                                                        "missed": v["summary"]["missing_lines"]}
                                                    for f, v in sorted(rep["files"].items())}}
        DATA.write_text(json.dumps(d, indent=1) + "\n")
    d = json.loads(DATA.read_text())
    text = "\n".join(stamp(page(d).split("\n"))) + "\n"
    if a.check:
        ok = PAGE.exists() and PAGE.read_text(encoding="utf-8") == text
        print("engine coverage page: current" if ok else "engine coverage page: out of date (python3 tools/engine_coverage.py)")
        return 0 if ok else 1
    PAGE.write_text(text, encoding="utf-8")
    tot = sum(v["statements"] for v in d["files"].values()); miss = sum(v["missed"] for v in d["files"].values())
    print(f"engine coverage: {100 * (tot - miss) / tot:.0f}% of {tot:,} statements -> {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
