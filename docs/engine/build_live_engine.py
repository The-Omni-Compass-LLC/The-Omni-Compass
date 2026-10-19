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
             token is present, the runs GitHub is running now (gh run list) and every run started for the chips and the
             clouds (the ledger, kept in docs/engine/github_ledger.json for a build without a token)

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


LEDGER = {"aks-metered.yml": "Azure", "gke-metered.yml": "Google Cloud", "eks-metered.yml": "Amazon Web Services",
          "cloud-check.yml": "the $0 cloud check", "lambda-gpu.yml": "the GPU on Lambda", "cpu-power.yml": "the CPU package"}
LEDGER_CACHE = HERE / "github_ledger.json"
REPO = "The-Omni-Compass-LLC/The-Omni-Compass"
LEDGER_GAUGES = ["machines billed, machine-hours", "compute bill at list price ($)", "worker nodes in service, mean", "response time (ms), 95th percentile",
                 "failed requests (%)", "time over the response line (% of samples)"]


def ledger() -> dict:
    """Every run GitHub was asked to start for the chips and the clouds (gh run list --event workflow_dispatch, newest
    first), each with the engine its commit stands on (tools/omni_version.py --commit) and whether its raw files are on the
    branch raw. Read from GitHub where a token is present, and kept in docs/engine/github_ledger.json; without a token the
    last reading kept there is used, and the page says when it was read."""
    data = None
    if shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")):
        got = {}
        for wf in LEDGER:
            r = subprocess.run(["gh", "run", "list", "--workflow", wf, "--event", "workflow_dispatch", "--limit", "60", "--json",
                                "databaseId,displayTitle,status,conclusion,createdAt,updatedAt,headSha,headBranch"],
                               capture_output=True, text=True, cwd=ROOT)
            try:
                got[wf] = [{"id": x["databaseId"], "title": x["displayTitle"], "status": x["status"], "conclusion": x["conclusion"] or None,
                            "created": x["createdAt"], "updated": x["updatedAt"], "sha": x["headSha"], "branch": x["headBranch"]}
                           for x in json.loads(r.stdout or "[]")]
            except json.JSONDecodeError:
                got = None
                break
        if got:
            data = {"read_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "source": "GitHub Actions, workflow_dispatch runs of each workflow, newest first", "workflows": got}
            # kept for a build without a token; GitHub's own rebuild reads the list fresh every time and commits only the page,
            # so it never rewrites the cache (19 October: the rewritten cache, left uncommitted, stopped the job's push)
            if os.environ.get("GITHUB_ACTIONS") != "true":
                LEDGER_CACHE.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    if data is None and LEDGER_CACHE.exists():
        data = json.loads(LEDGER_CACHE.read_text(encoding="utf-8"))
    if data is None:
        return {"read_at": None, "workflows": {}}
    import export_runs as XR
    ref, pre = XR.raw_ref()
    raw = set(git("ls-tree", "--name-only", f"{ref}:{pre.rstrip('/')}" if pre else ref).split())
    eng = {}
    for wf, rs in data["workflows"].items():
        for r in rs:
            if r["sha"] not in eng:
                if subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", r["sha"] + "^{commit}"], capture_output=True).returncode:
                    # fetch that one commit; --depth only where the checkout is already shallow (a full clone given --depth turns shallow)
                    shallow = git("rev-parse", "--is-shallow-repository") == "true"
                    subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", *(["--depth", "1"] if shallow else []), "origin", r["sha"]], capture_output=True)
                out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", r["sha"]],
                                     capture_output=True, text=True, cwd=ROOT).stdout
                m = re.search(r"(omni-v\d+) \(digest", out)
                eng[r["sha"]] = m.group(1) if m else None
            r["engine"] = eng[r["sha"]]
            r["raw"] = any(f"run-{r['id']}" in x for x in raw)
            if wf in ("aks-metered.yml", "gke-metered.yml", "eks-metered.yml") and r["status"] != "completed" and shutil.which("gh"):
                # a cloud set runs its repetitions one at a time, and GitHub lists the whole run as queued while it does: its
                # jobs say where it is (the repetitions measured to the end, the one running, how many it may take)
                jobs, page = [], 1
                while page < 5:
                    got = subprocess.run(["gh", "api", f"repos/{REPO}/actions/runs/{r['id']}/jobs?filter=latest&per_page=100&page={page}"],
                                         capture_output=True, text=True, cwd=ROOT)
                    try:
                        js = json.loads(got.stdout or "{}").get("jobs") or []
                    except json.JSONDecodeError:
                        break
                    jobs += js
                    if len(js) < 100:
                        break
                    page += 1
                reps = [j for j in jobs if re.match(r"run \(\d+\)$", j.get("name") or "")]
                if reps:
                    r["progress"] = {"total": len(reps), "done": sum(j["status"] == "completed" and j["conclusion"] == "success" for j in reps),
                                     "running": sum(j["status"] == "in_progress" for j in reps)}
            if wf == "aks-metered.yml" and r["raw"] and r["conclusion"] == "success":   # the bill as the run's own LIVE_REPS.json reads it
                src = f"{ref}:{pre}run-{r['id']}/live-reps-aks/LIVE_REPS.json"
                try:
                    lr = json.loads(git("show", src) or "{}")
                except json.JSONDecodeError:
                    lr = {}
                arm = next(iter((lr.get("paired") or {}).values()), {})
                if arm:
                    r["result"] = {"reps": len((lr.get("repetitions") or {}).get("native") or []),
                                   "gauges": {g: {k: arm[g].get(k) for k in ("native", "omni", "ci95", "significant")} for g in LEDGER_GAUGES if g in arm}}
    # the page shows the runs on omni-v8 and newer, each with its engine; the earlier engines' runs stay in GitHub's own list
    # and in docs/history (the founder's order of 19 October: no version 7 on the page)
    def recent(r):
        m = re.match(r"omni-v(\d+)$", r.get("engine") or "")
        return bool(m) and int(m.group(1)) >= 8
    data["workflows"] = {wf: [r for r in rs if recent(r)] for wf, rs in data["workflows"].items()}
    queues = {}
    for wf, f in (("aks-metered.yml", "azure_queue.txt"), ("gke-metered.yml", "google_queue.txt"), ("eks-metered.yml", "amazon_queue.txt")):
        q = ROOT / "scripts" / f
        sets = []
        for x in (q.read_text(encoding="utf-8").splitlines() if q.exists() else []):
            if "|" in x and not x.startswith("#"):
                label, kv = x.split("|", 1)
                steps = dict(p.split("=", 1) for p in kv.split(";") if "=" in p).get("load_steps")
                sets.append({"label": label, "key": f"burst {steps}" if steps else label})
        queues[wf] = sets
    data["queues"] = queues
    return data


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
    out["register"] = register_places()
    out["card"] = card_record()
    return _clean(out)


def card_record():
    """The newest real card run in the repository (results/gpu/run-*/GPU_REPS.json, metered by the card itself, class P):
    its card, its date, its repetitions, the controller commit it froze and the engine that commit stands on
    (tools/omni_version.py --commit), and every gauge's paired difference with its 95% interval, as the run's own file
    holds them."""
    runs = sorted((ROOT / "results" / "gpu").glob("run-*/GPU_REPS.json"))
    if not runs:
        return None
    d = json.loads(runs[-1].read_text(encoding="utf-8"))
    rc, fr = d.get("receipt", {}), d.get("freeze", {})
    rows = [{"g": g, "n": v.get("native"), "o": v.get("omni"), "lo": (v.get("ci95") or [None, None])[0], "hi": (v.get("ci95") or [None, None])[1]}
            for g, v in (d.get("paired", {}).get("omni") or {}).items() if isinstance(v, dict)]
    stamp = runs[-1].parent.name.replace("run-", "")
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", fr.get("commit") or "HEAD"],
                         capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"(omni-v\d+) \(digest", out)
    return {"file": str(runs[-1].relative_to(ROOT)), "card": rc.get("gpu_name"), "reps": rc.get("reps"), "seconds": rc.get("duration_s"),
            "limit_w": rc.get("power_limit_default_w"), "commit": (fr.get("commit") or "")[:12], "engine": m.group(1) if m else None,
            "when": f"{stamp[:4]}-{stamp[4:6]}-{stamp[6:8]}", "rows": rows}


def register_places() -> list:
    """Every open benchmark still to run, in the register's own order (docs/REGISTER.md, section 4): its domain, the open
    benchmark and its owner, the native it runs on top of, Omni-Compass's lever and its status, each as the register writes it
    (markdown stripped), so the benefit board lays out every place that is supposed to be there before its result exists."""
    reg = ROOT / "docs" / "REGISTER.md"
    if not reg.exists():
        return []
    text = reg.read_text(encoding="utf-8")
    sec = text[text.find("## 4."):] if "## 4." in text else ""
    sec = sec[:sec.find("\n## ", 5)] if "\n## " in sec[5:] else sec
    clean = lambda t: re.sub(r"\s+", " ", re.sub(r"\*\*|`|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", t)).strip()
    out = []
    for ln in sec.splitlines():
        if not re.match(r"\|\s*\d+\s*\|", ln):
            continue
        c = [clean(x) for x in ln.strip().strip("|").split("|")]
        if len(c) >= 6:
            out.append({"n": int(c[0]), "domain": c[1], "bench": c[2][:220], "native": c[3][:160], "lever": c[4][:120], "status": c[5][:260]})
    return out


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
    build["ledger"] = ledger()
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
