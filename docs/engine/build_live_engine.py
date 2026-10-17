# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Rebuilds the live engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) from the engine that stands and the
repository's own results: the page is a monitor of the engine, never a drawing of it.

Every record the page replays is made again here by the repository's own code on the checkout it runs in:

  harness    docs/engine/export_harness_trace.py: the realms harness (realms/harness.py, the max of
             realms/compass_arm_v5.py with the bone, the twins and the immune system), one organism and each muscle alone
  ctlrec     docs/engine/export_controller_trace.py: the shipped controller (omni_controller/controller.py) on the toy
             cluster, on top of the HPA (the max) and in the cloud's setting, every tick and every audited decision
  scen       docs/engine/export_scenarios.py: the GPU card (realms/gpu_card.py), the Linux host (tools/toy_gate.py's
             conveyance), every muscle and organism of the realms table (results/realms_v5) and every judged row of the
             newest engine's receipts (results/live/V<n>_*.md)
  build      what was built and from what: the engine (tools/omni_version.py), the commit, the time, and, where a GitHub
             token is present, the runs GitHub is running now (gh run list)

The page names the engine it stands on (data-engine on its <html>); the build refuses to write a page whose engine is not
the one tools/omni_version.py reads, so a new engine version is always written into the page's words by a person first.
Usage: python3 docs/engine/build_live_engine.py [--check] [--no-runs]. --check rebuilds in memory and exits 1 if any record
differs from the page (nothing written). Evidence class S for the models; the receipts keep their own classes.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAGE = HERE / "OMNI_COMPASS_LIVE_ENGINE.html"
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))

CDEC = ["E", "U", "calm", "kappa", "h", "sigma", "nu", "gate", "gate_ok", "nodes_ok", "rec", "seen", "rho", "cp", "cv", "cF",
        "cc", "cw", "vs", "va", "verdict", "writes", "q", "law"]       # the page's order of an audited decision (its CDEC)
TICK = ["nodes", "boot", "parked", "pods", "pending", "ms"]


def pack_controller(data: dict) -> dict:
    """export_controller_trace.py's record in the page's compact form: per run, each arm's ticks as columns and each
    decision's audit as one row in CDEC's order."""
    def dec(d):
        sc, ct = d.get("sc", {}), d.get("contract", {})
        val = {**d, "kappa": sc.get("kappa"), "h": sc.get("h"), "sigma": sc.get("sigma"), "nu": sc.get("nu"),
               "gate_ok": int(bool(d.get("gate_ok"))), "nodes_ok": int(bool(ct.get("nodes"))), "verdict": d.get("verdict", "")}
        return [val.get(k) for k in CDEC]
    out = {"slo": data["slo_ms"], "seeds": data["seeds"], "settings": {}}
    for name, sec in data["settings"].items():
        runs = {sd: {arm: {k: [t[k] for t in r[arm]] for k in TICK} for arm in ("native", "omni")} for sd, r in sec["runs"].items()}
        for sd, r in sec["runs"].items():
            runs[sd]["dec"] = [dec(d) for d in r["decisions"]]
        out["settings"][name] = {"readings": sec["readings"], "runs": runs}
    return out


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout.strip()


def engine() -> tuple:
    """(name, digest) of the engine the checkout stands on, as tools/omni_version.py reads it."""
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"(omni-v\d+) \(digest ([0-9a-f]+)", out)
    return (m.group(1), m.group(2)) if m else ("unknown", "")


def github_runs() -> list:
    """The runs GitHub is running or queueing now (gh run list), where a token is present; an empty list otherwise."""
    if not (shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))):
        return []
    out = []
    for status in ("in_progress", "queued"):
        r = subprocess.run(["gh", "run", "list", "--status", status, "--limit", "100", "--json",
                            "databaseId,workflowName,displayTitle,status,createdAt,headBranch"], capture_output=True, text=True, cwd=ROOT)
        try:
            out += json.loads(r.stdout or "[]")
        except json.JSONDecodeError:
            pass
    return [{"id": r["databaseId"], "workflow": r["workflowName"], "title": r["displayTitle"][:140], "status": r["status"],
             "since": r["createdAt"], "branch": r["headBranch"]} for r in out]


def records(runs: bool) -> dict:
    import export_controller_trace as XC
    import export_harness_trace as XH
    import export_scenarios as XS
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        XH.main(str(t / "h.json")); XC.main(str(t / "c.json")); XS.main(str(t / "s.json"))
        h, c, s = (json.loads((t / f).read_text(encoding="utf-8")) for f in ("h.json", "c.json", "s.json"))
    name, digest = engine()
    build = {"engine": name, "digest": digest, "commit": git("rev-parse", "HEAD"),
             "built_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
             "realms_engine": s["realms"]["run"]["engine"], "receipts_engines": sorted({r["engine"] for r in s["receipts"]}),
             "runs": github_runs() if runs else []}
    return {"harness": h, "ctlrec": pack_controller(c), "scen": s, "build": build}


def embedded(page: str, key: str):
    tag = f'<script type="application/json" id="{key}">'
    if tag not in page:
        return None
    a = page.index(tag) + len(tag)
    return json.loads(page[a:page.index("</script>", a)])


def inject(page: str, key: str, value) -> str:
    text = json.dumps(value, separators=(",", ":"), ensure_ascii=False)
    if "</" in text:
        raise ValueError(f"{key}: a record holds '</', which would end its script block")
    tag = f'<script type="application/json" id="{key}">'
    if tag in page:
        a = page.index(tag) + len(tag)
        return page[:a] + text + page[page.index("</script>", a):]
    anchor = '<script type="application/json" id="harness">'
    return page.replace(anchor, f"{tag}{text}</script>\n{anchor}", 1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild in memory; exit 1 if any record differs from the page")
    ap.add_argument("--no-runs", action="store_true", help="leave out GitHub's running and queued runs")
    a = ap.parse_args()
    page = PAGE.read_text(encoding="utf-8")
    named = re.search(r'<html[^>]*data-engine="(omni-v\d+)"', page)
    rec = records(not a.no_runs and not a.check)
    if not named or named.group(1) != rec["build"]["engine"]:
        print(f"the page names {named.group(1) if named else 'no engine'}, the repository stands on {rec['build']['engine']}: "
              "write the new engine into the page's words, then build again")
        return 1
    if a.check:
        bad = [k for k in ("harness", "ctlrec", "scen") if embedded(page, k) != rec[k]]
        print("every record on the page is the repository's own run" if not bad else "differs from the repository's own run: " + ", ".join(bad))
        return 1 if bad else 0
    for k in ("harness", "ctlrec", "scen", "build"):
        page = inject(page, k, rec[k])
    PAGE.write_text(page, encoding="utf-8")
    b = rec["build"]
    print(f"live engine rebuilt on {b['engine']} ({b['digest']}) at {b['commit'][:12]}, {b['built_at']}; "
          f"{len(b['runs'])} GitHub runs running or queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
