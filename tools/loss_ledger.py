#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The LOSS ledger: every row that reads LOSS across its three runs (in all three, or by their mean), in every benchmark's newest three-run table, on one page.

Built from the verdict audit's one selection (tools/verdict_audit.py: each benchmark's newest whole three-run table from omni-v8
on, tools/readings.py `landed`; the third arm, taken out on 25 October, never counted), never typed in; the live benchmark engine's
appraisal counts the same rows. Every row is placed by what its two arms are:

  against my own native     Omni-Compass on top of a native controller against that native alone (every plain table, and the
                            four ways' TOP and BARE): the readings "do no harm" is judged by (DISCLOSURES.md, section 3)
  in place of a controller  Omni-Compass on the organism alone against an orchestrator as shipped (the four ways' VS): shown,
                            a different question from do no harm
  without me, or compounded the orchestrator against the organism alone (ORCH: neither arm carries Omni-Compass) and
                            Omni-Compass on top of the orchestrator against the organism alone (BOTH: two changes at once)

A row against my own native carries its cause where one is written (CAUSES below names the page), the version that fixed
it where one did, and what decides it. A row with no cause written says so.

  python3 tools/loss_ledger.py            write docs/LOSS_LEDGER.md
  python3 tools/loss_ledger.py --check    exit 1 when docs/LOSS_LEDGER.md differs from what the tables give
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools.readings import classify, judged, landed, with_own_runs  # noqa: E402

OUT = ROOT / "docs" / "LOSS_LEDGER.md"
TABLE_DIRS = (ROOT / "results" / "live", ROOT / "results" / "orchestrator")

ARMS = {"BARE": "against my own native", "TOP": "against my own native", "VS": "in place of a controller",
        "ORCH": "without me, or compounded", "BOTH": "without me, or compounded"}
SECTIONS = ("against my own native", "in place of a controller", "without me, or compounded")

# (benchmark, gauge prefix) -> (cause, the page that states it, fixed in, what decides it). A prefix matches every gauge it
# begins; the benchmark is the table's name without its engine (V12_KUBERAY_4W_BARE -> KUBERAY_4W_BARE).
V13_FIX = ("on a shared host at its top, beside another workload's room, a CPU limit I raised was kept through a saturated batch "
           "queue, so the batch pods ran slower while the web served no faster", "docs/OMNI_V13.md", "omni-v13",
           "the benchmark's three runs on the engine that stands")
CAUSES = {
    ("KUBERAY_4W_BARE", ""): V13_FIX,
    ("ARMADA_4W_BARE", ""): ("suspected: the conveyance fault fixed in omni-v13 (its shape fits: a batch gauge a few percent "
                             "slower on a shared host); not yet shown on this rig", "docs/LOSS_ROWS_UNDER_INVESTIGATION.md",
                             "omni-v13, if the suspicion holds", "the benchmark's three runs on the engine that stands"),
    ("BINPACK", "queue:"): ("suspected: the conveyance fault fixed in omni-v13; the omni-v13 toy gate's batch toy, set from the "
                            "KubeRay runs' own files, read the job turnaround back at native's", "docs/OMNI_V13.md",
                            "omni-v13, if the suspicion holds", "the benchmark's three runs on the engine that stands"),
    ("VANILLA", "queue:"): ("suspected: the conveyance fault fixed in omni-v13; the omni-v13 toy gate's batch toy read the job "
                            "turnaround back at native's", "docs/OMNI_V13.md", "omni-v13, if the suspicion holds",
                            "the benchmark's three runs on the engine that stands"),
    ("OCM_4W_TOP", "alert minutes"): ("under investigation: the third run's size is far from the first two",
                                      "docs/LOSS_ROWS_UNDER_INVESTIGATION.md", "", "the benchmark's three runs on the engine "
                                      "that stands, read repetition by repetition"),
}


def newest_tables():
    """Each benchmark's newest whole table: (engine number, benchmark name, path)."""
    out = []
    for d in TABLE_DIRS:
        groups = defaultdict(list)
        for p in d.glob("V*_*.json"):
            m = re.fullmatch(r"V(\d+)_(.+)\.json", p.name)
            if m:
                groups[m.group(2)].append((int(m.group(1)), p))
        for name, found in groups.items():
            for n, p in sorted(found, reverse=True):
                if landed(p):
                    out.append((n, name, p))
                    break
    return sorted(out, key=lambda t: (t[1], t[0]))


def loss_rows(data):
    """(gauge, row) for every row that reads LOSS across its three runs, wherever the table keeps it (rows, or workloads' gauges)."""
    found = []

    def walk(o, path):
        if isinstance(o, dict):
            r = o.get("reading")
            if isinstance(r, str):
                try:
                    c = classify(r)
                except ValueError:
                    c = None
                if c == "loss" and judged(r):
                    found.append((" / ".join(path), o))
            for k, v in o.items():
                if k not in ("runs", "reading"):
                    walk(v, path + [str(k)])
    walk(data.get("rows") or {}, [])
    for wl, gauges in sorted((data.get("workloads") or {}).items()):
        if wl != "tuning":
            walk(gauges, [f"workload {wl}"])
    return found


def section(name):
    m = re.search(r"_4W_([A-Z]+)$", name)
    return ARMS.get(m.group(1), SECTIONS[0]) if m else SECTIONS[0]


def cause(name, gauge):
    for (bench, prefix), c in CAUSES.items():
        if bench == name and gauge.startswith(prefix):
            return c
    return None


def sizes(row):
    """Each run's change against the first arm, in percent of it, in the run's order; from one value to the other where the
    first arm stood at or near zero, so no percent is printed that a near-zero base inflates past meaning."""
    out = []
    for r in row.get("runs") or []:
        base, other = r.get("native"), r.get("omni")
        if not (isinstance(base, (int, float)) and isinstance(other, (int, float))):
            continue
        pct = abs(other - base) / abs(base) * 100 if base else None
        out.append(f"{pct:.1f}%" if pct is not None and pct < 1000 else f"{base:.4g} to {other:.4g}")
    return ", ".join(out) or "sizes in the table"


def build():
    """Every LOSS row of every standing table, from the verdict audit's one selection (tools/verdict_audit.py): the same tables,
    words and categories the live benchmark engine's appraisal counts, so the two can never differ."""
    from tools.verdict_audit import build as audit
    rec = audit()
    by_t = {t["stem"]: t for t in rec["tables"]}
    section_of = {"against its native": SECTIONS[0], "in place of a controller": SECTIONS[1],
                  "the orchestrator's own": SECTIONS[2], "two changes at once": SECTIONS[2]}
    rows = {s: [] for s in SECTIONS}
    engines = defaultdict(int)
    for r in rec["rows"]:
        t = by_t[r["table"]]
        if r["word"] != "LOSS" or t["status"] != "standing":
            continue
        n, name = int(t["engine"][len("omni-v"):]), t["stem"].split("_", 1)[1]
        where = (f"workload {r['section']} / " if t["stack"] == "Linux services" else f"{r['section']} / ") if r["section"] else ""
        rows[section_of[t["comparison"]]].append((n, name, ROOT / (t["json"] or t["file"]), where + r["gauge"], r, t["title"]))
        engines[n] += 1
    for s in SECTIONS:
        rows[s].sort(key=lambda x: (x[1], x[0]))
    return rows, engines


def render(built):
    rows, engines = built
    mine = rows[SECTIONS[0]]
    L = ["# The LOSS ledger: every row that reads LOSS across its three runs, in every benchmark's newest table", "",
         "Every row of every three-run table stands where its table stands, LOSS included; this page gathers the LOSS rows so "
         "none of them is found only by reading every table. A LOSS row is a gauge that moved away from its declared aim by 0.5% "
         "or more across the benchmark's three runs, A, B and C (the founder's order of 24 October 2026, `tools/readings.py`): in all "
         "three, every run's 95% interval clear of zero, or by the mean of the three, with the count of runs beyond the noise. Each benchmark "
         "is read from its newest whole table; an older engine's table stands only until the engine that stands has run that "
         "benchmark three times, and the engine each row ran on is printed beside it.", "",
         f"Rows that read LOSS across their three runs: **{sum(len(v) for v in rows.values())}**. Against my own native, the readings "
         f"do no harm is judged by: **{len(mine)}**. In place of a controller: **{len(rows[SECTIONS[1]])}**. Without me, or two "
         f"changes at once: **{len(rows[SECTIONS[2]])}**. By engine: "
         + (", ".join(f"omni-v{n}: {c}" for n, c in sorted(engines.items(), reverse=True)) or "none") + ".", ""]
    heads = {SECTIONS[0]: ("Against my own native",
                           "Omni-Compass on top of a native controller, against that native alone: the readings do no harm is "
                           "judged by (`DISCLOSURES.md`, section 3). Each row's cause stands beside it where it is written; a row "
                           "with none says so."),
             SECTIONS[1]: ("In place of a controller",
                           "Omni-Compass on the organism alone against an orchestrator as shipped (the four ways' VS): Omni-Compass "
                           "doing an orchestrator's work without it. Shown; a different question from do no harm, which is "
                           "judged against the native a governor sits on."),
             SECTIONS[2]: ("Without me, or two changes at once",
                           "The orchestrator as shipped against the organism alone (ORCH: neither arm carries Omni-Compass), and "
                           "Omni-Compass on top of the orchestrator against the organism alone (BOTH: the orchestrator and "
                           "Omni-Compass together, two changes at once). Shown because every row is shown.")}
    for s in SECTIONS:
        title, intro = heads[s]
        L += [f"## {title}", "", intro, ""]
        if not rows[s]:
            L += ["No row reads LOSS.", ""]
            continue
        if s == SECTIONS[0]:
            L += ["| Engine | Benchmark | Gauge | Each run's size | Cause | Fixed in | What decides it |", "|---|---|---|---|---|---|---|"]
            for n, name, p, gauge, row, title_ in rows[s]:
                c = cause(name, gauge)
                why, page, fixed, decides = c if c else ("not yet written", "", "", "the benchmark's three runs on the engine that stands")
                L.append(f"| omni-v{n} | `{p.relative_to(ROOT)}` | {gauge} | {sizes(row)} | {why}" + (f" (`{page}`)" if page else "")
                         + f" | {fixed or '—'} | {decides} |")
        else:
            L += ["| Engine | Benchmark | Gauge | Each run's size |", "|---|---|---|---|"]
            for n, name, p, gauge, row, title_ in rows[s]:
                L.append(f"| omni-v{n} | `{p.relative_to(ROOT)}` | {gauge} | {sizes(row)} |")
        L.append("")
    L += ["Each run's size is the change against the comparison's first arm, in percent of it, run by run; the direction is the "
          "gauge's, away from its aim in every run. The tables hold every number, its interval and its arms.", ""]
    return "\n".join(legal_stamp(with_own_runs(L))) + "\n"


def main(argv):
    md = render(build())
    if "--check" in argv:
        same = OUT.exists() and OUT.read_text() == md
        print("loss ledger: docs/LOSS_LEDGER.md " + ("matches the tables" if same else "differs from the tables: run python3 tools/loss_ledger.py"))
        return 0 if same else 1
    OUT.write_text(md)
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
