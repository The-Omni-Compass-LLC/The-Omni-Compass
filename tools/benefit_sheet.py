#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""The benefit sheet: one number per benchmark, and the sign always means the same thing.

The founder's order of 9 October 2026: next to every benchmark, say whether Omni was a benefit and by how much, in one
number, where plus is always good for Omni and minus is always bad, whatever the gauge measures. Less energy, fewer
machines, less memory, a shorter wait, fewer failures are all plus here; more of any of them is minus. The tables keep
their raw signs (a response time that fell reads "-65%" there); this sheet turns every one the same way round.

How the number is made, the same rule as the Omni index (tools/omni_index.py):

  every judged gauge becomes a ratio oriented so that above 1 is good for Omni (native / omni for a gauge where lower is
  better, omni / native where higher is better); a gauge counts only where its reading is confirmed over all three runs,
  anything else (inside the noise, the same, the runs disagree) counts as exactly 1; the number is the geometric mean of
  those ratios, minus one, in percent. For the tests inside the index the number IS the index's own resource reading of
  that test; for a stack with several workloads the stack's number is its index category. For the simulators and the
  organisms, which the index does not score, the same arithmetic runs over every judged gauge of their tables.

  "Benefit?" reads yes (a confirmed gain, no confirmed loss), no (a confirmed loss, no confirmed gain), none (nothing
  confirmed either way) or trade (gains and losses both; the number says which way the trade nets by this scoring).

  python3 tools/benefit_sheet.py            ->  docs/BENEFIT_SHEET.md, results/BENEFIT_SHEET.json
  python3 tools/benefit_sheet.py --check    ->  exit 1 if the committed files differ from what the tables give
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools import omni_index                                       # noqa: E402
from tools import wiring_verdicts as wv                            # noqa: E402

LIVE = ROOT / "results" / "live"
OUT_MD = ROOT / "docs" / "BENEFIT_SHEET.md"
OUT_JSON = ROOT / "results" / "BENEFIT_SHEET.json"


def gmean(xs):
    xs = [x for x in xs if x and x > 0]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else 1.0


def pct(r):
    return 100.0 * (r - 1.0)


def fmt_pct(x):
    if x is None:
        return "no number"
    if abs(x) < 0.05:
        return "0%"
    return f"{x:+.0f}%" if abs(x) >= 10 else f"{x:+.1f}%"


def fmt_pct_words(x):
    """The one number with its meaning in a word: '+31% gain', '-25% loss', '0% nothing'."""
    if x is None:
        return "no number"
    if abs(x) < 0.05:
        return "0% nothing"
    return fmt_pct(x) + (" gain" if x > 0 else " loss")


def in_words(items):
    """Every confirmed change of a benchmark in words, grouped by gauge: (name, class, range) -> 'p95 cut 65% to 71%: good'.
    A gauge that fell when falling is good reads cut; one that rose when rising is good reads up; each carries good or cost."""
    groups = {}
    for name, cls, rg in items:
        nums = re.findall(r"[-+]?\d+(?:\.\d+)?%", rg or "")
        if not nums:
            continue
        groups.setdefault((name, cls, nums[0].startswith("-")), []).extend(abs(float(n.rstrip("%"))) for n in nums)
    out = []
    for (name, cls, fell), mags in groups.items():
        mags = sorted(mags)
        f = (lambda x: f"{x:.0f}%") if mags[-1] >= 10 else (lambda x: f"{x:.1f}%")
        m = f(mags[0]) if f(mags[0]) == f(mags[-1]) else f"{f(mags[0])} to {f(mags[-1])}"
        v = ("cut" if fell else "up") if cls == "better" else ("down" if fell else "up")
        out.append(f"{name} {v} {m}: {'good' if cls == 'better' else 'cost'}")
    return "; ".join(out) if out else "nothing confirmed either way"


def benefit_word(better, worse):
    if better and worse:
        return "trade"
    if better:
        return "yes"
    if worse:
        return "no"
    return "none"


def shallow():
    """A shallow checkout (GitHub's default) carries no history: the dates must then come from the committed sheet."""
    r = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "--is-shallow-repository"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() == "true"


def updated(path):
    """The date the file was last changed in the repository (the day the result landed); None where the history is not here."""
    if shallow():
        return None
    r = subprocess.run(["git", "-c", "safe.directory=*", "log", "-1", "--format=%cs", "--", str(path)], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or "uncommitted"


# ------------------------------------------------------------------------------- the tests inside the index
def from_index():
    """One row per Kubernetes test and one per stack. The number is the index's own (the resource reading of the test, or the
    stack's category); the benefit word counts every judged gauge of the test's table, as the wiring page does."""
    cases = wv.real_stacks(wv.load_index())
    rows = []
    names = {"V3_PGBENCH.md": "PostgreSQL, the pooler's pool size", "V3_KAFKA.md": "Kafka, the consumer group's size",
             "V3_REDIS.md": "Redis, the cache's memory ceiling", "V3_YCSB.md": "MongoDB, the storage engine's cache size",
             "V3_SYSBENCH.md": "MySQL, the buffer pool's size"}
    stacks = {}
    for c in cases:
        if not c["counted"]:
            continue
        b, w = len(c["judged"]["better"]), len(c["judged"]["worse"])
        items = [(nm, "better", rg) for _, nm, rg, _ in c["judged"]["better"]] + [(nm, "worse", rg) for _, nm, rg, _ in c["judged"]["worse"]]
        f = c["source"].rsplit("/", 1)[-1]
        if "Kubernetes" in c["domain"]:
            rows.append({"date": updated(LIVE / f), "benchmark": "Real Kubernetes, " + c["case"], "benefit": benefit_word(b, w), "pct": c["resource_pct"],
                         "better": b, "worse": w, "words": in_words(items), "what": "the index's reading of this test: p95, machines, energy, and work where measured", "file": c["source"]})
        else:
            s_ = stacks.setdefault(f, {"ratios": [], "better": 0, "worse": 0, "parts": [], "items": []})
            s_["ratios"].append(1 + (c["resource_pct"] or 0.0) / 100.0); s_["better"] += b; s_["worse"] += w; s_["items"] += items
            s_["parts"].append({"case": c["workload"], "pct": c["resource_pct"] or 0.0, "benefit": benefit_word(b, w), "words": in_words(items)})
    for f, s_ in stacks.items():
        rows.append({"date": updated(LIVE / f), "benchmark": names.get(f, f), "benefit": benefit_word(s_["better"], s_["worse"]), "pct": pct(gmean(s_["ratios"])),
                     "better": s_["better"], "worse": s_["worse"], "words": in_words(s_["items"]),
                     "what": "the index's category: its untouched workloads together (work, p95, the resource held, host CPU)",
                     "file": f"results/live/{f}", "parts": s_["parts"]})
    return rows


def headline_row():
    """The one number over every real test, from the index's own file."""
    p = ROOT / "results" / "OMNI_INDEX.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    hl = d.get("headline_pct", d.get("resource_headline_pct"))
    if hl is None:
        return None
    cases = [c for c in wv.real_stacks(wv.load_index()) if c["counted"]]
    b = sum(len(c["judged"]["better"]) for c in cases); w = sum(len(c["judged"]["worse"]) for c in cases)
    return {"date": updated(ROOT / "results" / "OMNI_INDEX.md"), "benchmark": "Every real test together: the Omni index", "benefit": benefit_word(b, w), "pct": hl,
            "better": b, "worse": w, "words": "the six real categories together; each stack's own words are in its row",
            "what": "the headline: six real categories weighed the same (the index's resource reading)", "file": "results/OMNI_INDEX.md"}


# -------------------------------------------------------------------------- three-run tables outside the index
def from_abc_table(fname, name, what):
    """A Kubernetes-style three-run table (rows keyed by gauge), scored with the index's measures where present and every
    judged gauge otherwise."""
    p = LIVE / fname
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    ratios, better, worse, items = [], 0, 0, []
    for key, row in d["rows"].items():
        try:
            c = wv.classify(row["reading"])
        except ValueError:                                         # a row of its own kind (a hand-back receipt): shown, not a gauge
            continue
        if c == "unjudged":
            continue
        lower = key not in {omni_index.CAPACITY}                      # every judged gauge of these tables is lower-is-better but the capacity
        if c in ("better", "worse"):
            rs = []
            for r in row["runs"]:
                n, o = r.get("native"), r.get("omni")
                if n is None or o is None or n <= 0 or o <= 0:
                    continue
                rs.append(n / o if lower else o / n)
            if rs:
                ratios.append(gmean(rs)); better += c == "better"; worse += c == "worse"
                items.append((wv.K8S_GAUGE.get(key, key), c, wv.pct_range(row["runs"])))
            else:
                ratios.append(1.0)
        else:
            ratios.append(1.0)
    return {"date": updated(LIVE / fname.replace(".json", ".md")), "benchmark": name, "benefit": benefit_word(better, worse), "pct": pct(gmean(ratios)),
            "better": better, "worse": worse, "words": in_words(items), "what": what, "file": f"results/live/{fname.replace('.json', '.md')}"}


# ------------------------------------------------------------------------------------- the simulators (markdown)
def sim_case_ratio(rows):
    """One case's oriented ratio from a simulator table's rows: confirmed gauges only, the direction read from the reading
    and the sign of the change (a confirmed better that fell is a lower-is-better gauge)."""
    head = rows[0]; ridx = len(head) - 1
    abc = [i for i, h in enumerate(head) if h in ("A", "B", "C")]
    ratios, better, worse = [], 0, 0
    for r in rows[1:]:
        if len(r) != len(head):
            continue
        c = wv.classify(r[ridx])
        if c == "unjudged":
            continue
        if c not in ("better", "worse"):
            ratios.append(1.0); continue
        vals = []
        for i in abc:
            s = r[i].replace("−", "-")
            if s.endswith("%"):
                try:
                    vals.append(float(s[:-1]) / 100.0)
                except ValueError:
                    pass
        if not vals:
            ratios.append(1.0); continue
        change = sum(vals) / len(vals)
        lower_is_better = (c == "better" and change < 0) or (c == "worse" and change > 0)
        r_ = (1.0 / (1.0 + change)) if lower_is_better else (1.0 + change)
        if r_ <= 0:
            r_ = 1e-6
        ratios.append(r_); better += c == "better"; worse += c == "worse"
    return gmean(ratios), better, worse


def from_sim(fname, name, moved_titles, what, left_native_title=None):
    p = LIVE / fname
    if not p.exists():
        return None
    cases = []
    for sec in wv.parse_sim(p):
        if left_native_title and sec["title"].startswith(left_native_title):
            for r in sec["table"][1:]:                             # nothing moved: nothing gained, nothing lost
                if r and r[0]:
                    cases.append({"case": r[0] + " (left native by the engine's own trial)", "pct": 0.0, "benefit": "none", "better": 0, "worse": 0, "words": "nothing moved", "items": []})
            continue
        tag = next((t for t in moved_titles if sec["title"].startswith(t)), None)
        if tag is None:
            continue
        for sub in sec["subs"]:
            cname = sub["title"].split(":", 1)[0].strip()
            if fname == "V3_SWARM.md" and cname == "tuning":
                continue
            if not sub["rows"]:
                continue
            r, b, w = sim_case_ratio(sub["rows"])
            j = wv.sim_rows_judged(sub["rows"])
            items = [(nm, "better", rg) for _, nm, rg, _ in j["better"]] + [(nm, "worse", rg) for _, nm, rg, _ in j["worse"]]
            cases.append({"case": cname + (f" ({moved_titles[tag]})" if moved_titles[tag] else ""), "pct": pct(r), "benefit": benefit_word(b, w), "better": b, "worse": w,
                          "words": in_words(items), "items": items})
    if not cases:
        return None
    better = sum(c["better"] for c in cases); worse = sum(c["worse"] for c in cases)
    all_items = [it for c in cases for it in c.get("items", [])]
    for c in cases:
        c.pop("items", None)
    return {"date": updated(p), "benchmark": name, "benefit": benefit_word(better, worse), "pct": pct(gmean([1 + c["pct"] / 100.0 for c in cases])),
            "better": better, "worse": worse, "words": in_words(all_items), "what": what, "file": f"results/live/{fname}", "parts": cases}


# ---------------------------------------------------------------------------------------------- the organisms
def from_organisms(fname, name, what):
    p = LIVE / fname
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    cells, all_items = [], []
    for cell, c in d["organisms"].items():
        ratios, better, worse, items = [], 0, 0, []
        for k, v in c["rows"].items():
            if k.startswith("organism") or v.get("neutral") or v.get("same"):
                continue                                           # the cluster's own gauges decide; the modelled organism is judged in the realms table
            sure = v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
            if not sure or v["native"] <= 0 or v["omni"] <= 0:
                ratios.append(1.0); continue
            lower = v["better"] == (v["omni"] < v["native"])     # the report's own direction: better and fell means lower is better
            ratios.append(v["native"] / v["omni"] if lower else v["omni"] / v["native"])
            better += bool(v["better"]); worse += not v["better"]
            items.append((wv.K8S_GAUGE.get(k, k), "better" if v["better"] else "worse", f"{v['pct']:+.1f}%"))
        all_items += items
        cells.append({"case": cell.replace("@", " at ") + " copies", "pct": pct(gmean(ratios)), "benefit": benefit_word(better, worse), "better": better, "worse": worse,
                      "words": in_words(items)})
    better = sum(x["better"] for x in cells); worse = sum(x["worse"] for x in cells)
    return {"date": updated(LIVE / fname.replace(".json", ".md")), "benchmark": name, "benefit": benefit_word(better, worse),
            "pct": pct(gmean([1 + x["pct"] / 100.0 for x in cells])), "better": better, "worse": worse, "words": in_words(all_items), "what": what,
            "file": f"results/live/{fname.replace('.json', '.md')}", "parts": cells}


def from_realms():
    p = ROOT / "results" / "realms" / "REALMS.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    tower = d["organisms"].get("tower")
    if not tower:
        return None
    prim = tower["summary"]["primary"]
    clear = prim[1] > 0 or prim[2] < 0
    better = int(clear and prim[0] > 0); worse = int(clear and prim[0] < 0)
    return {"date": updated(ROOT / "results" / "realms" / "REALMS.md"), "benchmark": "The 945 modelled muscles as one tower, every muscle written at once",
            "benefit": benefit_word(better, worse), "pct": 100 * prim[0] if clear else 0.0, "better": better, "worse": worse,
            "words": (f"work per energy up {100 * prim[0]:.1f}%: good" if clear and prim[0] > 0 else f"work per energy down {abs(100 * prim[0]):.1f}%: cost" if clear else "nothing confirmed either way"),
            "what": "the tower's work per energy over ten paired seeds; a model, evidence class S", "file": "results/realms/REALMS.md"}


def main(check=False):
    rows = from_index()
    for fname, name, what in [
        ("V3_ROBUST_KILL.json", "Robustness: the governor killed outright mid-run", "the whole window, a kill and a restart inside it; p95, machines, energy"),
        ("V3_ROBUST_LONG.json", "Robustness: the two-hour run", "the two-hour window; p95, machines, energy"),
    ]:
        r = from_abc_table(fname, name, what)
        if r:
            rows.append(r)
    for fname, name, titles, what, *left in [
        ("V3_MUJOCO.md", "Robot arms (MuJoCo), the three untouched robots", {"Robots where Omni moved the override": ""}, "every judged gauge of each robot's table (energy, losses, torque, tracking); a robot the engine left native reads 0", "Robots where the paired trial left the override native"),
        ("V3_PANDAPOWER.md", "Power grids (SimBench), both load models", {"ZIP loads": "ZIP loads", "constant-power loads": "constant-power loads"}, "every judged gauge of every grid, then the grids together"),
        ("V3_CITYLEARN.md", "Buildings and batteries (CityLearn), the districts with batteries", {"Districts with electric batteries": ""}, "every CityLearn score of every district, then the districts together"),
        ("V3_SWARM.md", "Drone swarms, the three untouched cells", {"Cells where Omni moved the cruise": ""}, "every judged gauge of every cell"),
    ]:
        r = from_sim(fname, name, titles, what, left[0] if left else None)
        if r:
            rows.append(r)
    for fname, name, what in [
        ("V3_SIX_KUBE.json", "The six organisms with the real cluster inside, 10 and 100 copies", "the cluster's own gauges in every cell; the modelled organism is judged in the realms table"),
        ("V3_BIG_ORGANISM.json", "The big organisms with the real cluster inside, 1,000 copies on Azure", "the cluster's own gauges in both cells"),
    ]:
        r = from_organisms(fname, name, what)
        if r:
            rows.append(r)
    r = from_realms()
    if r:
        rows.append(r)
    hl = headline_row()
    if hl:
        rows.append(hl)
    if any(r["date"] is None for r in rows):                       # no history here: the dates the sheet already carries, by benchmark
        known = {}
        if OUT_JSON.exists():
            known = {(x["benchmark"], x["file"]): x["date"] for x in json.loads(OUT_JSON.read_text())["rows"]}
        for r in rows:
            if r["date"] is None:
                r["date"] = known.get((r["benchmark"], r["file"]), "unknown")
    rows.sort(key=lambda x: (x["date"], x["benchmark"]), reverse=True)
    if hl:
        rows.remove(hl); rows.insert(0, hl)

    L = ["# The benefit sheet: one number per benchmark, plus always good for Omni, and every change said in words", "",
         "The founder's order of 9 October 2026: next to every benchmark, say whether Omni-Compass was a benefit and by how much, in "
         "one number whose sign always means the same thing, and say every change in words so that nobody has to work out which way a "
         "gauge points. **On this sheet plus is good for Omni and minus is bad, whatever the gauge measures.** The number carries its "
         "word: **gain**, **loss** or **nothing**. Beside it every confirmed change is written out: a gauge that fell when falling is good "
         "reads **cut** (less waiting, fewer machines, less energy, less memory, fewer failures), a gauge that rose when rising is good "
         "reads **up**, and each one carries **good** or **cost**. So \"p95 cut 65%: good\" and \"memory ceiling held up 215%: cost\" "
         "cannot be misread.", "",
         "The result tables (the files in the last column) keep every change with its raw sign: a response time that fell reads \"-65%\" "
         "there, and whether a fall is good is said in the Reading column beside it. Read the words here, not the bare signs there.", "",
         "The number is the Omni index's rule (`results/OMNI_INDEX.md`): each judged gauge becomes a ratio oriented so that above one is "
         "good for Omni; it counts only where confirmed over all three runs, anything else counts as exactly one; the number is the "
         "geometric mean of the ratios, minus one, in percent. For the tests inside the index the number is the index's own resource "
         "reading of that test; for a stack with several workloads it is the stack's index category; for the simulators and the "
         "organisms the same arithmetic runs over every judged gauge of their tables. Built from the tables by `tools/benefit_sheet.py`, "
         "checked by `verify.py`.", "",
         "**Benefit?** reads **yes** (confirmed gains, no confirmed loss), **no** (a confirmed loss, no confirmed gain), **none** "
         "(nothing confirmed either way) or **trade** (gains and losses both; the number says which way the trade nets by this "
         "scoring, and the wiring page `docs/WIRING_VERDICTS.md` says what pays for what).", "",
         "| Date | Benchmark | Benefit? | How much | Every confirmed change, in words | Table |",
         "|---|---|---|---:|---|---|"]
    for r in rows:
        L.append(f"| {r['date']} | {r['benchmark']} | **{r['benefit']}** | **{fmt_pct_words(r['pct'])}** | {r.get('words', '')} | `{r['file']}` |")
    L += ["", "## The parts behind a row", "",
          "Where a row sums several workloads, grids, districts, cells or robots, each part with its own number, the same way round:", ""]
    for r in rows:
        if r.get("parts"):
            L.append(f"- **{r['benchmark']}**: " + "; ".join(f"{p_['case']} {fmt_pct_words(p_['pct'])} ({p_['benefit']}" + (f": {p_['words']}" if p_.get('words') else "") + ")" for p_ in r["parts"]) + ".")
    L += ["", "## Not on the sheet, and why", "",
          "- **Azure's managed Kubernetes, the bill** (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): Omni v1, a 4-worker fleet, every gauge inside the noise: 0%, and too small a fleet to show one machine.",
          "- **The governor's own cost** (`results/live/V3_OWN_COST.md`): 0.6% to 1.3% of one core at every size; a cost shown, not a benchmark against native.",
          "- **The card (NVIDIA)**: every earlier result is obsolete; the current governor has not run on a real card.",
          "- **The index's second reading** (service alone, `results/OMNI_INDEX.md`): a second true number for the same tests, not repeated here; this sheet carries the preregistered one.", ""]
    md = "\n".join(legal_stamp(L)) + "\n"
    js = json.dumps({"rows": rows}, indent=1) + "\n"
    if check:
        bad = [str(p.relative_to(ROOT)) for p, text in ((OUT_MD, md), (OUT_JSON, js)) if not p.exists() or p.read_text() != text]
        if bad:
            print("benefit sheet out of date (python3 tools/benefit_sheet.py): " + ", ".join(bad))
            return 1
        print("benefit sheet: in line with the tables")
        return 0
    OUT_MD.write_text(md); OUT_JSON.write_text(js)
    print(f"{OUT_MD.relative_to(ROOT)}: {len(rows)} rows; {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv[1:]))
