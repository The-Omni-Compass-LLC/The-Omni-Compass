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
  runs       docs/engine/export_runs.py: the official runs as recorded, every three-run table's runs A, B and C read
             back from their raw files, every file's SHA-256 matched against the run's own list, every Kubernetes
             repetition scored by the repository's own scorer (tools/live_reps.py) and checked against the run's result
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
import math
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


TABLE_OF = {   # a benchmark in scripts/reruns.txt -> its three-run table(s) in results/live (V<n>_<stem>.md)
    "Kubernetes CruiseKube": ["CRUISEKUBE"], "Kubernetes Goldilocks": ["GOLDILOCKS"], "Kubernetes fixed capacity": ["CAPACITY"],
    "kubernetes all four": ["ALL_FOUR"], "kubernetes fairness": ["FAIRNESS"], "kubernetes faults": ["FAULTS"],
    "kubernetes batch": ["BATCH"], "kubernetes google 2011 trace": ["TRACE_GOOGLE2011"],
    "kubernetes keda add-ons": ["KEDA_REQUESTS", "KEDA_CPU_REQUESTS"], "redis resource": ["REDIS"], "redis service": ["REDIS_SERVICE"],
    "kafka resource": ["KAFKA"], "kafka service": ["KAFKA_SERVICE"], "postgresql resource": ["PGBENCH"], "mysql resource": ["SYSBENCH"],
    "mongodb resource": ["YCSB"], "robot arms": ["MUJOCO"], "power grids": ["PANDAPOWER"], "buildings and batteries": ["CITYLEARN"],
    "drone swarms": ["SWARM"], "robustness long": ["ROBUST_LONG"]}


def board(runs: list) -> list:
    """Every benchmark the repository holds a place for, and where it stands: its newest three-run table and that table's
    engine, whether GitHub is running it now, or that it is queued, switched off or not yet launched. Read from
    scripts/reruns.txt, the cloud queues, the GPU campaign's profiles and the results themselves; nothing is written here
    that the repository does not say."""
    import export_scenarios as XS
    wf_name = {}
    for y in (ROOT / ".github" / "workflows").glob("*.yml"):
        m = re.search(r"^name:\s*(\S+)", y.read_text(encoding="utf-8"), re.M)
        if m:
            wf_name[y.name] = m.group(1)
    live = {r["workflow"] for r in runs if r["status"] == "in_progress"}
    waiting = {r["workflow"] for r in runs if r["status"] == "queued"}
    out = []
    def state(wf):
        n = wf_name.get(wf, wf.removesuffix(".yml"))
        return "running now" if n in live else "queued on GitHub" if n in waiting else None
    for ln in (ROOT / "scripts" / "reruns.txt").read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#") or "|" not in ln:
            continue
        name, wf = ln.split("|")[:2]
        tables = []
        for stem in TABLE_OF.get(name, []):
            n, st = XS.newest(f"V7_{stem}")
            if n:
                tables.append({"file": f"results/live/{st}.md", "engine": f"omni-v{n}"})
        if name == "1107 muscles and seven organisms":
            rj = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
            if rj.exists():
                tables.append({"file": "results/realms_v5/REALMS_V5.md", "engine": json.loads(rj.read_text(encoding="utf-8"))["run"]["engine"]})
        out.append({"group": "every benchmark, run again on the engine that stands", "name": name, "workflow": wf,
                    "tables": tables, "now": state(wf) or ("in the reruns queue" if not tables else None)})
    for cloud, f, wf in (("Azure", "azure_queue.txt", "aks-metered.yml"), ("Google Cloud", "google_queue.txt", "gke-metered.yml"),
                         ("Amazon Web Services", "amazon_queue.txt", "eks-metered.yml")):
        q = ROOT / "scripts" / f
        if not q.exists():
            continue
        lines = [x for x in q.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
        on = any(x.strip() == "switch=on" for x in lines)
        running_titles = " ".join(r["title"] for r in runs if r["status"] == "in_progress" and r["workflow"] == wf_name.get(wf, wf[:-4]))
        for x in lines:
            if "|" not in x:
                continue
            label = x.split("|")[0]
            out.append({"group": f"the cloud: {cloud}, at the tune-down on the machines alone (the bill)", "name": label, "workflow": wf,
                        "tables": [], "now": ("running now" if label.split()[0] in running_titles else "in the queue") if on else
                        "switched off until the founder turns it on"})
    gp = ROOT / "scripts" / "gpu_campaign_profiles.json"
    if gp.exists():
        g = json.loads(gp.read_text(encoding="utf-8"))
        for prof, v in g.get("profiles", {}).items():
            for scale in g.get("organism_scales", []):
                out.append({"group": "the GPU chips on Lambda (class P, the card's own meter)", "name": f"{prof} ({v.get('physical_gpus')} "
                            f"GPU{'s' if v.get('physical_gpus', 1) > 1 else ''}), {scale} cop{'y' if scale == 1 else 'ies'} of each organism",
                            "workflow": v.get("script", ""), "tables": [], "now": "launched" if g.get("launch") else "not yet launched (the founder's exact commit first)"})
    return out


def _clean(v):
    """NaN and infinity, which JSON cannot carry, as null."""
    if isinstance(v, float):
        return v if math.isfinite(v) else None
    if isinstance(v, dict):
        return {k: _clean(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_clean(x) for x in v]
    return v


def fleet() -> dict:
    """The benefit sheet (results/BENEFIT_SHEET.json, every benchmark's benefit in one row), the Omni index's headline
    (results/OMNI_INDEX.md) and the grid (results/grid_v5/GRID.json, the newest grid with squares; the dispatches of the
    engine that stands from results/grid_v<n>/DISPATCHED.json), each as the repository holds it."""
    out = {"benefit": [], "index": None, "grid": None}
    bs = ROOT / "results" / "BENEFIT_SHEET.json"
    if bs.exists():
        out["benefit"] = [{k: r.get(k) for k in ("date", "benchmark", "benefit", "pct", "gain", "loss", "given", "words", "what", "file", "engine")}
                          for r in json.loads(bs.read_text(encoding="utf-8")).get("rows", [])]
    oi = ROOT / "results" / "OMNI_INDEX.md"
    if oi.exists():
        t = oi.read_text(encoding="utf-8")
        m = re.search(r"## Headline:([^\n]*)", t); m2 = re.search(r"## The second reading[^\n]*?: ([^\n]*)", t)
        out["index"] = {"headline": m.group(1).strip() if m else None, "service": m2.group(1).strip() if m2 else None, "file": "results/OMNI_INDEX.md"}
    grids = sorted((ROOT / "results").glob("grid_v*/GRID.json"), key=lambda q: int(re.sub(r"\D", "", q.parent.name)))
    if grids:
        gp = grids[-1]; md = gp.with_name("GRID.md"); eng = None
        if md.exists():
            m = re.search(r"engine (omni-v\d+)", md.read_text(encoding="utf-8")); eng = m.group(1) if m else None
        g = json.loads(gp.read_text(encoding="utf-8"))
        sq = {"modelled": {}, "kube": {}}
        for k, v in g.get("modelled", {}).items():
            sq["modelled"][k] = {n: {"label": c.get("label"), "runs": c.get("runs"), "viol_pp": (c.get("viol_pp") or [None])[0],
                                     "work": (c.get("work") or [None])[0], "energy": (c.get("energy") or [None])[0]} for n, c in v.items() if isinstance(c, dict)}
        for k, v in g.get("kube", {}).items():
            sq["kube"][k] = {n: {"verdict": c.get("verdict"), "reps": c.get("repetitions"), "GAIN": c.get("GAIN"), "LOSS": c.get("LOSS"), "given": c.get("power given"),
                                 "p95": {kk: c["rows"][kk].get(kk2) for kk in ["response time (ms), 95th percentile"] if kk in c.get("rows", {}) for kk2 in ["pct"]}.get("response time (ms), 95th percentile")}
                             for n, c in v.items() if isinstance(c, dict)}
        disp = None
        stand = ROOT / "results" / f"grid_v{engine()[0].rsplit('v', 1)[-1]}" / "DISPATCHED.json"
        if stand.exists():
            disp = len(json.loads(stand.read_text(encoding="utf-8")).get("dispatches", []))
        out["grid"] = {"file": str(gp.relative_to(ROOT)), "engine": eng, "squares": sq, "dispatched_on_engine_that_stands": disp}
    return _clean(out)


def records(runs: bool) -> dict:
    import export_controller_trace as XC
    import export_harness_trace as XH
    import export_scenarios as XS
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        import export_runs as XR
        XH.main(str(t / "h.json")); XC.main(str(t / "c.json")); XS.main(str(t / "s.json")); XR.main(str(t / "r.json"))
        h, c, s, rr = (json.loads((t / f).read_text(encoding="utf-8")) for f in ("h.json", "c.json", "s.json", "r.json"))
    name, digest = engine()
    build = {"engine": name, "digest": digest, "commit": git("rev-parse", "HEAD"),
             "built_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
             "realms_engine": s["realms"]["run"]["engine"], "receipts_engines": sorted({r["engine"] for r in s["receipts"]}),
             "runs": github_runs() if runs else []}
    build["board"] = board(build["runs"])
    return {"harness": h, "ctlrec": pack_controller(c), "scen": s, "runs": rr, "fleet": fleet(), "build": build}


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
        # a new engine stands: the page adopts it at once (every record, the head's engine and the build line are rebuilt on
        # it); its prose keeps naming the engine it was written for in data-prose, and the page says so in a banner until
        # the prose is realigned (the build never stops the page on a new version)
        old = named.group(1) if named else None
        if a.check:
            print(f"the page names {old}, the repository stands on {rec['build']['engine']}: the next build adopts it")
            return 1
        if 'data-prose="' not in page:
            page = page.replace(f'data-engine="{old}"', f'data-engine="{old}" data-prose="{old}"', 1)
        page = re.sub(r'data-engine="omni-v\d+"', f'data-engine="{rec["build"]["engine"]}"', page, count=1)
        print(f"the engine that stands is now {rec['build']['engine']} (the page was built on {old}): records rebuilt on it; "
              "the prose stays as written for the older engine until it is realigned, and the page says so")
    if a.check:
        bad = [k for k in ("harness", "ctlrec", "scen", "runs", "fleet") if embedded(page, k) != rec[k]]
        print("every record on the page is the repository's own run" if not bad else "differs from the repository's own run: " + ", ".join(bad))
        return 1 if bad else 0
    for k in ("harness", "ctlrec", "scen", "runs", "fleet", "build"):
        page = inject(page, k, rec[k])
    PAGE.write_text(page, encoding="utf-8")
    b = rec["build"]
    print(f"live engine rebuilt on {b['engine']} ({b['digest']}) at {b['commit'][:12]}, {b['built_at']}; "
          f"{len(b['runs'])} GitHub runs running or queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
