#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole organism, two ways, for the live engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html, section 11).

Omni-Compass is wired into every layer of a stack through its own plug: the software (Kubernetes and the services on it),
the bare metal under it (the card, the processor, the kernel) and, where the stack is rented, the cloud that bills the
machines. Each layer was benchmarked on its own, native against Omni-Compass on top of native, and read by the Omni
index's rule (tools/omni_index.py): every measure a ratio oriented so that above 1 is a GAIN (work omni/native; speed,
machines and energy native/omni), counted only where the three-run reading is the same in all three of our runs, exactly
1 otherwise (nothing inside the noise is claimed either way); a test the geometric mean of its measures, a category the
geometric mean of its tests.

This file composes the layers into the two ways a stack is bought:

  on-site bare metal   the software on the bare metal:                        software × hardware
  through the cloud    the cloud's build, its bare metal at the back end, the software:  cloud × hardware × software

The rule of composition, stated once. A unit of work passes through every layer of the stack, so a measure's ratio for
the whole organism is the product of the layers' ratios, R[m] = Π r[ℓ, m] (in logarithms, a sum); a layer's ratio is
the geometric mean of its categories', as the index weights categories; the organism's one number is the geometric mean
of its measures' ratios, minus one, in percent, the index's own arithmetic one level up. Runs A, B and C are composed
run by run (A with A, B with B, C with C) and the composed index is read by the three-run rule. Each 95% interval is
carried through in logarithms: the half-widths of independent layers add in quadrature. The product rule assumes the
layers act independently, which is how the engine that stands is built (every muscle judged on itself, nothing traded
between muscles) and how they were measured (one layer at a time, never all at once on one stack): the composition is
our own arithmetic on measured readings, evidence class S, shown beside the measured categories and never presented as
a measurement. A layer with no three-run table on the engine that stands counts as exactly 1 and says so; what is
recorded for it on earlier engines or on single runs is shown beside it, word for word, never counted.

Every number is read from the repository's own files (results/live/V<n>_*.json, results/gpu/*/GPU_REPS.json,
results/live/V1_AKS_*.json); nothing is typed in.

  python3 docs/engine/export_whole.py [out.json]
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from tools import omni_index as OI                                   # noqa: E402  the index's own rule, reused, never restated
from tools.readings import GAIN, EVEN, LOSS, GIVEN, LOWER, HIGHER, SPENT, NEVER_MORE, WORK_PER, SPENT_GAUGES, word, judged  # noqa: E402

LIVE = ROOT / "results" / "live"
MEASURES = ("work", "speed", "machines", "energy")
MEASURE_WORDS = {"work": "work: more of it", "speed": "speed: a shorter response", "machines": "machines: fewer held",
                 "energy": "energy: less spent (or the bill)"}

# The layers: which of the Omni index's categories each one governs, written once, like the index's own SOURCES. A category
# the index lists as pending has no counted table yet; it stands in its layer as exactly 1 with the index's own reason.
LAYERS = [
    ("software", "Software: Kubernetes, its governors and orchestrators, the services on it",
     ("Real Kubernetes (GitHub)", "Real database (PostgreSQL behind PgBouncer, GitHub)", "Real messaging (Apache Kafka, GitHub)",
      "Real cache (Redis, GitHub)", "Real database cache (MongoDB under YCSB, GitHub)", "Real database buffer pool (MySQL under sysbench, GitHub)")),
    ("hardware", "Bare metal: the card, the processor and the kernel under the software",
     ("Real card (NVIDIA, its own meter)",)),
    ("cloud", "The cloud: the machines it bills, parked and woken under the software",
     ("Real cloud (Azure AKS, billed)",)),
]
SCENARIOS = [
    ("onsite", "On-site bare metal: the software on the bare metal", ("software", "hardware")),
    ("cloud", "Through the cloud: the cloud's build, its bare metal at the back end, the software", ("cloud", "hardware", "software")),
]
# where each pending layer's result lands when its runs finish (only files that exist are named)
LANDING = {
    "hardware": ["docs/CPU_POWER_PREREGISTRATION.md", ".github/workflows/cpu-power.yml", "docs/LAMBDA_SETUP.md", ".github/workflows/lambda-gpu.yml"],
    "cloud": ["docs/K8S_COMPASS_PREREGISTRATION.md", "scripts/azure_queue.txt", ".github/workflows/aks-metered.yml", "results/live/AKS_BILL.md"],
}


def ratio_interval(m, native, omni, ci95):
    """A measure's oriented ratio and the two ends of its 95% interval, from a row's paired difference (omni − native)."""
    r = OI.ratio(m, native, omni)
    if r is None or not ci95 or ci95[0] is None or ci95[1] is None:
        return r, None, None
    ends = [OI.ratio(m, native, native + c) for c in ci95]
    if any(e is None for e in ends):
        return r, None, None
    return r, min(ends), max(ends)


def half_log(lo, hi):
    return (math.log(hi) - math.log(lo)) / 2 if lo and hi and lo > 0 and hi > 0 else 0.0


def run_cells(m, runs):
    """Each run's oriented ratio with its interval, from the table's own cells."""
    out = []
    for r in runs:
        rr, lo, hi = ratio_interval(m, r.get("native"), r.get("omni"), r.get("ci95"))
        out.append({"native": r.get("native"), "omni": r.get("omni"), "ratio": rr, "lo": lo, "hi": hi})
    return out


def measure_record(m, row):
    """One measure of one test: the index's own ratio (tools/omni_index.measure) and the three runs' cells."""
    mr = OI.measure(row, m)
    cells = run_cells(m, row["runs"])
    counted = judged(row["reading"]) and all(c["ratio"] for c in cells)
    return {"ratio": mr["ratio"], "reading": row["reading"], "counted": counted,
            "runs": cells if counted else [dict(c, ratio=1.0, lo=None, hi=None, shown=c["ratio"]) for c in cells]}


def equal_work():
    return {"ratio": 1.0, "reading": "the same fixed-rate work sent to both arms", "counted": False, "equal": True,
            "runs": [{"native": 1.0, "omni": 1.0, "ratio": 1.0, "lo": None, "hi": None} for _ in range(3)]}


def tests():
    """Every test of the Omni index with its per-run cells: the same walk as tools/omni_index.tests(), the same tables."""
    out = []
    for cat, name, f, measures, work in OI.SOURCES:
        f = OI.newest(f)
        path = LIVE / f
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        rows = data["rows"]
        r = {m: measure_record(m, rows[key]) for m, key in measures.items() if key in rows}
        if work == "equal":
            r["work"] = equal_work()
        elif work == "capacity" and (OI.CAPACITY in rows or OI.CAPACITY_NOW in rows):
            r["work"] = measure_record("work", rows.get(OI.CAPACITY) or rows[OI.CAPACITY_NOW])
        out.append({"category": cat, "test": name, "source": f"results/live/{f}", "engine": engine_of(data["runs"]),
                    "runs": [x["run"] for x in data["runs"]], "measures": r})
    for cat, fname, label, measures_ in OI.WORKLOAD_TABLES:
        fname = OI.newest(fname)
        db = LIVE / fname
        if not db.exists():
            continue
        data = json.loads(db.read_text())
        for wl, gauges in sorted(data["workloads"].items()):
            if wl == "tuning":
                continue                                            # the tuning workload is shown in its table, never counted
            r = {}
            for m, key in measures_.items():
                g = gauges.get(key)
                if not g or any(x is None for x in g["runs"]):
                    continue
                r[m] = measure_record(m, g)
            out.append({"category": cat, "test": label.format(wl=wl), "source": f"results/live/{fname}", "engine": engine_of(data["runs"]),
                        "runs": [x["run"] for x in data["runs"]], "measures": r})
    return out


def engine_of(runs):
    es = sorted({re.sub(r"\s*\(.*$", "", x.get("engine", "")) for x in runs if x.get("engine")})
    return ", ".join(es) if es else "the table's runs name no engine"


def gm_logs(logs):
    """The mean of logarithms (a geometric mean) and nothing where there is nothing."""
    return sum(logs) / len(logs) if logs else None


def quad(hs, n):
    return math.sqrt(sum(h * h for h in hs)) / n if hs and n else 0.0


def compose_category(ts):
    """A category's ratio per measure, overall and run by run, with the interval's half-width in logarithms: the geometric mean
    of its tests, as the index weights them (a test that did not take a measure leaves it out)."""
    out = {}
    for m in MEASURES:
        have = [t["measures"][m] for t in ts if m in t["measures"]]
        if not have:
            continue
        logs = [math.log(x["ratio"]) for x in have]
        runs, halves = [], []
        for k in range(3):
            cells = [x["runs"][k] if k < len(x["runs"]) else None for x in have]
            lk = [math.log(c["ratio"]) if c and c["ratio"] else 0.0 for c in cells]
            hk = [half_log(c["lo"], c["hi"]) if c else 0.0 for c in cells]
            runs.append(gm_logs(lk)); halves.append(quad(hk, len(have)))
        out[m] = {"log": gm_logs(logs), "runs": runs, "half": halves, "n": len(have), "counted": sum(1 for x in have if x["counted"])}
    return out


def compose_mean(parts):
    """The geometric mean over parts (categories in a layer), per measure, run by run; half-widths in quadrature over n."""
    out = {}
    for m in MEASURES:
        have = [p[m] for p in parts if m in p]
        if not have:
            continue
        out[m] = {"log": gm_logs([x["log"] for x in have]), "runs": [gm_logs([x["runs"][k] for x in have]) for k in range(3)],
                  "half": [quad([x["half"][k] for x in have], len(have)) for k in range(3)], "n": sum(x["n"] for x in have),
                  "counted": sum(x["counted"] for x in have)}
    return out


def compose_product(parts):
    """The product over the layers of a stack, per measure, run by run (a sum of logarithms); half-widths add in quadrature."""
    out = {}
    for m in MEASURES:
        have = [p[m] for p in parts if m in p]
        if not have:
            continue
        out[m] = {"log": sum(x["log"] for x in have), "runs": [sum(x["runs"][k] for x in have) for k in range(3)],
                  "half": [math.sqrt(sum(x["half"][k] ** 2 for x in have)) for k in range(3)], "n": sum(x["n"] for x in have),
                  "counted": sum(x["counted"] for x in have), "layers": len(have)}
    return out


def readable(comp):
    """Ratios, intervals, words and the one number, from a composition in logarithms."""
    out = {"measures": {}}
    for m, c in comp.items():
        ratio = math.exp(c["log"])
        runs = []
        for k in range(3):
            rk = math.exp(c["runs"][k]); h = c["half"][k]
            runs.append({"ratio": rk, "lo": math.exp(c["runs"][k] - h), "hi": math.exp(c["runs"][k] + h), "word": OI.word_of(m, rk)})
        out["measures"][m] = {"ratio": ratio, "pct": 100 * (ratio - 1), "word": OI.word_of(m, ratio), "runs": runs,
                              "n": c["n"], "counted": c["counted"], "layers": c.get("layers")}
    logs = [c["log"] for c in comp.values()]
    svc = [c["log"] for m, c in comp.items() if m in OI.SERVICE]
    idx = math.exp(gm_logs(logs)) if logs else None
    sv = math.exp(gm_logs(svc)) if svc else None
    out["index_pct"] = None if idx is None else 100 * (idx - 1)
    out["service_pct"] = None if sv is None else 100 * (sv - 1)
    out["word"] = OI.index_word(idx, sv) if idx is not None else ""
    runs = []
    for k in range(3):
        lk = [c["runs"][k] for c in comp.values()]; sk = [c["runs"][k] for m, c in comp.items() if m in OI.SERVICE]
        ik = math.exp(gm_logs(lk)) if lk else None; svk = math.exp(gm_logs(sk)) if sk else None
        hk = quad([c["half"][k] for c in comp.values()], len(comp)) if comp else 0.0
        runs.append({"index_pct": None if ik is None else 100 * (ik - 1),
                     "lo_pct": None if ik is None else 100 * (math.exp(math.log(ik) - hk) - 1),
                     "hi_pct": None if ik is None else 100 * (math.exp(math.log(ik) + hk) - 1),
                     "word": OI.index_word(ik, svk) if ik is not None else ""})
    out["runs"] = runs
    ws = {r["word"] for r in runs if r["word"]}
    out["three"] = (runs[0]["word"] if len(ws) == 1 else "the runs disagree") if ws else ""
    return out


def aim_of(gauge: str) -> str:
    """The aim of a recorded row by its gauge's name, the key's own classes (tools/readings.py)."""
    g = gauge.lower()
    if gauge in SPENT_GAUGES:
        return SPENT
    if re.search(r"work per|per kj|requests per", g):
        return WORK_PER
    if re.search(r"failed|lost", g):
        return NEVER_MORE
    if re.search(r"energy|power|bill|machine-hours|node-hours|nodes|machines|replicas|pods started|cores|cpu|memory|\(w\)|\(j\)|wh\b", g):
        return SPENT
    if re.search(r"served|requests a second|work inside|throughput|completed", g):
        return HIGHER
    return LOWER


def row_word(aim_, diff, ci95):
    if aim_ == NEVER_MORE and diff is not None and diff > 0:
        return LOSS                                                  # a count that must never rise rose
    if ci95 and ci95[0] is not None and ci95[1] is not None and ci95[0] <= 0 <= ci95[1]:
        return EVEN
    if diff is None or diff == 0:
        return EVEN
    return word(diff < 0, aim_)


def record_rows(paired: dict):
    rows = []
    for g, v in paired.items():
        if not isinstance(v, dict) or v.get("native") is None or v.get("omni") is None:
            continue
        n, o = v["native"], v["omni"]
        if isinstance(n, float) and math.isnan(n) or isinstance(o, float) and math.isnan(o):
            continue
        a = aim_of(g)
        rows.append({"g": g, "aim": a, "native": n, "omni": o, "diff": v.get("diff"), "ci95": v.get("ci95"),
                     "pct": None if not n else 100 * (o - n) / n, "word": row_word(a, v.get("diff"), v.get("ci95"))})
    return rows


def gpu_record():
    """The card's one recorded run (2 October 2026) on the controller since replaced: the record, every row, never counted."""
    runs = sorted((ROOT / "results" / "gpu").glob("run-*/GPU_REPS.json"))
    if not runs:
        return None
    p = runs[-1]
    d = json.loads(p.read_text())
    paired = (d.get("paired") or {}).get("omni") or {}
    rc, fz = d.get("receipt") or {}, d.get("freeze") or {}
    reps = sorted({r for r in ((d.get("checks") or {}).get("native") or {}).keys()}, key=lambda s: int(s) if s.isdigit() else 0)
    return {"title": f"{rc.get('gpu_name', 'the card')}, {len(reps)} paired repetitions, its own meter",
            "file": str(p.relative_to(ROOT)).replace("GPU_REPS.json", "GPU_REPS.md"), "commit": (fz.get("commit") or "")[:12],
            "engine": "a commit before the fingerprinted engines, on the card controller since replaced: obsolete; the rerun on Lambda is pending",
            "cls": "P", "rows": record_rows(paired), "headline": (d.get("headline") or {}).get("verdict")}


def aks_records():
    """Azure's recorded single runs on omni-v1 (one run each, five paired repetitions): the record, every row, never counted."""
    out = []
    for p in sorted(LIVE.glob("V1_AKS_*.json")):
        d = json.loads(p.read_text())
        paired = (d.get("paired") or {}).get("compass") or {}
        reps = (d.get("repetitions") or {}).get("native") or []
        stem = p.stem.replace("V1_AKS_", "").lower()
        out.append({"title": f"Azure AKS, the {stem} set, one run of {len(reps)} paired repetitions", "file": f"results/live/{p.name}",
                    "engine": "omni-v1", "cls": "L", "rows": record_rows(paired)})
    return out


def main(out):
    ts = tests()
    by_cat = {}
    for t in ts:
        by_cat.setdefault(t["category"], []).append(t)
    layers = []
    comps = {}
    for key, name, cats in LAYERS:
        cat_out, parts = [], []
        for c in cats:
            if c in by_cat:
                comp = compose_category(by_cat[c]); parts.append(comp)
                cat_out.append({"name": c, "state": "counted", "tests": by_cat[c], **readable(comp)})
            else:
                cat_out.append({"name": c, "state": "pending", "why": OI.PENDING.get(c, "no three-run table on the engine that stands yet"), "tests": []})
        comp = compose_mean(parts)
        comps[key] = comp
        layer = {"key": key, "name": name, "categories": cat_out, "counted_categories": len(parts), **readable(comp),
                 "landing": [f for f in LANDING.get(key, []) if (ROOT / f).exists()]}
        if key == "hardware":
            layer["records"] = [r for r in [gpu_record()] if r]
        if key == "cloud":
            layer["records"] = aks_records()
        layers.append(layer)
    scenarios = []
    for key, name, ls in SCENARIOS:
        comp = compose_product([comps[l] for l in ls])
        sc = {"key": key, "name": name, "layers": list(ls), **readable(comp)}
        if key == "cloud":                                          # the cloud as two pieces as well: its build and the software, the back-end bare metal untouched
            sc["two_piece"] = {"layers": ["cloud", "software"], **readable(compose_product([comps["cloud"], comps["software"]]))}
        scenarios.append(sc)
    index = {}
    pj = ROOT / "results" / "OMNI_INDEX.json"
    if pj.exists():
        ix = json.loads(pj.read_text())
        index = {"headline_pct": ix.get("headline_pct"), "service_headline_pct": ix.get("service_headline_pct"), "file": "results/OMNI_INDEX.md"}
    data = {"measures": list(MEASURES), "measure_words": MEASURE_WORDS, "layers": layers, "scenarios": scenarios, "index": index,
            "rule": "R[m] = Π r[ℓ, m] over the layers of the stack; a layer is the geometric mean of its categories, a category of its tests, "
                    "a measure counted only where the same in all three of our runs, exactly 1 otherwise; the one number is the geometric "
                    "mean of the measures, minus one; 95% half-widths add in quadrature in logarithms; runs composed A with A, B with B, C with C"}
    Path(out).write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False), encoding="utf-8")
    for s in scenarios:
        print(f"{s['key']:7s} index {s['index_pct']:+.2f}% {s['word']} · runs " + " / ".join(f"{r['index_pct']:+.2f}%" for r in s["runs"]) + f" · three-run {s['three']}")
    for l in layers:
        print(f"  layer {l['key']:9s} {l['counted_categories']} categories counted; " + (f"index {l['index_pct']:+.2f}% {l['word']}" if l["index_pct"] is not None else "nothing counted yet (exactly 1)"))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "whole.json")
