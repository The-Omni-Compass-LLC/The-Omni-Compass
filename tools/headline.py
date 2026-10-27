#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The answer first (the founder's order of 24 October 2026): is Omni-Compass a benefit against native, by how much, in the
three ways it runs, and what the two bills say, at the top of the README and of the live engine page.

Every number is read from a result file of the engine that stands, never typed: the three ways from the newest three-arm record
on GitHub's machines (results/orchestrator/V*_THREE_ARMS_ABC.json: native, Omni-Compass on top of native, Omni-Compass direct;
three runs, class L), each scenario's signal from its own rows by the one key (tools/readings.py: red, the stop-sign octagon,
redlining, when a row reads LOSS; green, the circle, accelerating, when a row reads GAIN and none LOSS; yellow, the diamond,
steady, when every row reads STEADY). The two bills are the two ways a stack is bought (docs/engine/export_whole.py): on-site,
the software on the owner's bare metal; through the cloud, where the cloud is the wire between the two ends. A bill's part that
the engine that stands has not measured is written "not yet measured on <engine>", never filled in, and no price is assumed: a
bill is the measured change in what it is made of (the founder's choice of 24 October: percent, no dollar price). The totals
composed from earlier engines' tables stand beside it, named by their engines and never read as the engine that stands.

  python3 tools/headline.py            write the block into README.md and the live engine page
  python3 tools/headline.py --check    exit 1 when either differs from what the files give
"""
from __future__ import annotations

import html
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import readings as K          # noqa: E402  (the one key)

README = ROOT / "README.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
WHOLE = ROOT / "results" / "WHOLE_SYSTEM.json"
BEGIN, END = "<!-- headline: written by tools/headline.py from the result files; never edited by hand -->", "<!-- end headline -->"
SIGNAL = {"red": ("redlining", "docs/engine/signals/redlining.svg", "the red stop-sign octagon"),
          "lead": ("steady", "docs/engine/signals/steady.svg", "the yellow yield diamond"),
          "ok": ("accelerating", "docs/engine/signals/accelerating.svg", "the green circle")}
PAIRS = (("Omni-Compass on top of native", "Omni on native against native",
          "Omni-Compass on top of Kubernetes' own autoscaling rule on the muscles, never fewer units than the rule"),)
# native and Omni-Compass on native are the only two sides (the founder's order of 25 October: Omni-Compass is never by itself);
# the record's third arm, Omni direct, stays in its own table as the road and is not read here
GAUGES = (("requests", "Work"), ("p95", "Response (95th percentile)"), ("machines", "Machines"), ("units", "Units"))


def newest_record():
    recs = sorted(ROOT.glob("results/orchestrator/V*_THREE_ARMS_ABC.json"), key=lambda p: int(re.match(r"V(\d+)", p.name).group(1)))
    if not recs:
        raise SystemExit("headline: no three-arm record in results/orchestrator/")
    return recs[-1], json.loads(recs[-1].read_text(encoding="utf-8"))


def row_of(rec, pair, gauge):
    for r in rec["rows"]:
        if r["pair"] == pair and r["gauge"].startswith(gauge):
            return r
    return None


def word_of(reading: str) -> str:
    for w in (K.LOSS, K.GIVEN, K.GAIN):
        if reading.startswith(w):
            return w
    return K.STEADY if reading.startswith(("STEADY", "STEADY")) else reading


def mean_change(r) -> float:
    return sum(r["runs"][k]["rel"] for k in sorted(r["runs"])) / len(r["runs"])


def said(r, gauge) -> str:
    """A row as the founder reads it: the word first, then the direction in words, the mean of the three runs and each run."""
    m = mean_change(r)
    way = ("up" if m > 0 else "down") if abs(m) >= 0.0005 else "unchanged"
    what = {"p95": " (faster)" if m < 0 else " (slower)" if m > 0 else "", "machines": " (fewer)" if m < 0 else " (more)" if m > 0 else ""}.get(gauge, "")
    runs = ", ".join(f"{100 * abs(r['runs'][k]['rel']):.1f}%" for k in sorted(r["runs"]))
    return f"{r['reading']}: {way} {100 * abs(m):.1f}%{what}; the runs {runs}"


def signal(rows) -> str:
    words = [word_of(r["reading"]) for r in rows if r]
    if K.LOSS in words:
        return "red"
    return "ok" if K.GAIN in words else "lead"


def whole_beside():
    """The composed totals of earlier engines' tables (tools/whole_system.py), named by their engines."""
    if not WHOLE.exists():
        return None
    d = json.loads(WHOLE.read_text(encoding="utf-8"))
    engines = sorted({t.get("engine", "") for name, ts in d["layers"].items() if not name.startswith("1.") for t in ts},
                     key=lambda e: (len(e), e))
    tot = (d.get("totals") or {}).get("without the card (the cluster, the services and the cloud) | index") or {}
    pct = lambda mu: None if mu is None else 100.0 * (math.exp(mu) - 1.0)     # each total is a log ratio toward the gauge's aim
    g = {k: pct(v[0]) if v else None for k, v in (tot.get("total") or {}).items()}
    return {"engines": [e for e in engines if e], "index": pct((tot.get("index") or {}).get("mu")),
            "work": g.get("work"), "speed": g.get("speed"), "machines": g.get("machines"), "energy": g.get("energy"), "bill": g.get("bill") or 0.0}


def model():
    path, rec = newest_record()
    engine = rec["engine"].split(" (")[0]
    scen = []
    for name, pair, how in PAIRS:
        rows = {g: row_of(rec, pair, g) for g, _ in GAUGES}
        scen.append({"name": name, "how": how, "signal": signal([rows["requests"], rows["p95"]]), "rows": rows,
                     "work": mean_change(rows["requests"]), "p95": mean_change(rows["p95"])})
    azure_v = sorted(ROOT.glob(f"results/live/{engine.upper().replace('OMNI-', '')}_AKS*.md"))
    return {"path": path.relative_to(ROOT).as_posix(), "rec": rec, "engine": engine, "scen": scen, "azure": azure_v, "whole": whole_beside()}


def markdown(m) -> str:
    rec, eng = m["rec"], m["engine"]
    img = lambda lv: f'<img src="{SIGNAL[lv][1]}" alt="{SIGNAL[lv][2]}" height="14">'
    L = [BEGIN, "", "## The answer first: is Omni-Compass a benefit against native?", ""]
    yes = all(s["signal"] == "ok" for s in m["scen"])
    stands = "omni-v" + re.search(r'VERSIONS = \{"v(\d+)"', (ROOT / "tools" / "omni_version.py").read_text()).group(1)
    where = (f"on the engine that stands ({eng})" if eng.startswith(stands + " ") or eng == stands else
             f"on {eng.split(' (')[0]}, the newest engine with its three runs in (the engine that stands, {stands}, runs them again)")
    L.append(f"**{'Yes' if yes else 'Not in every way'}, {where}, measured on real machines (class L), "
             f"three runs (A, B and C).** Omni-Compass on top of native did {100 * m['scen'][0]['work']:.1f}% more work than native "
             f"and answered {100 * abs(m['scen'][0]['p95']):.1f}% faster at the 95th percentile.")
    L += ["", "| Scenario | Signal | Work | Response (95th percentile) | Machines | Units |", "|---|---|---|---|---|---|",
          f"| **Native**: Kubernetes' own autoscaling rule on the muscles | {img('lead')} the baseline | the baseline | the baseline | the baseline | the baseline |"]
    for s in m["scen"]:
        r = s["rows"]
        L.append(f"| **{s['name']}**: {s['how']} | {img(s['signal'])} **{SIGNAL[s['signal']][0]}** | "
                 + " | ".join(said(r[g], g) if r[g] else "not read" for g, _ in GAUGES) + " |")
    L += ["", f"The signals: {img('ok')} accelerating, a GAIN and no LOSS; {img('lead')} steady, every row STEADY; {img('red')} "
          "redlining, a LOSS. Units are the service's own copies: Omni-Compass adds them to buy the work and the speed, power given, "
          f"never a LOSS. Source: [`{m['path']}`]({m['path']}), {rec['what']}; runs {', '.join(f'{k} {v}' for k, v in rec['runs'].items())}; "
          f"commit `{rec['commit'][:12]}`.", ""]
    L += ["### The two bills", "",
          "**THE CLOUD IS ONLY A WIRE BETWEEN THE SOFTWARE END AND THE HARDWARE END. Omni-Compass on the cloud alone can give only a "
          "small cut in the bill, from the machines the cloud's own autoscaler made; the benefit lives at the two ends, in the software "
          "and in the bare metal, and the cloud carries it.**", "",
          "Each route's bill is its native total cost, then Omni-Compass's, then the saving: 1 − (the Omni-Compass total ÷ the native total), "
          "each total the sum of its non-overlapping cost components inside the declared boundary, on a matched workload "
          "(`docs/THE_TUNE.md`, section 8). A component's own percent is a supporting measurement, never the bill. Where a price or a "
          "component is missing the bill reads unresolved; no price is assumed.", "",
          "| Route | The bill: native → Omni-Compass → saving | Supporting measurements |", "|---|---|---|"]
    on = m["scen"][0]["rows"]["machines"]
    L.append(f"| **On-site**: the software on your own bare metal | **unresolved**: no machine-hour or energy price is declared, and the "
             f"energy is not yet measured on {eng} | machines, Omni-Compass on top of native: {said(on, 'machines')} |")
    cloud = (f"read in [`{m['azure'][-1].relative_to(ROOT).as_posix()}`]({m['azure'][-1].relative_to(ROOT).as_posix()})" if m["azure"]
             else f"**unresolved**: not yet measured on {eng}; its Azure sets run now, A, B and C (`scripts/azure_queue.txt`); Google, Amazon "
                  "and the clouds a tester builds are wired and not yet run")
    L.append(f"| **Through the cloud**: the cloud's build, its bare metal at the back end, the software | {cloud} | the software end's, as on-site; "
             f"the provider's energy is not metered to the tenant |")
    w = m["whole"]
    if w and w["index"] is not None:
        bill = "STEADY" if abs(w["bill"]) < 100 * K.SIZE_FLOOR else f"{w['bill']:+.1f}%"
        L += ["", f"Beside it, and never read as {eng}: the totals composed from earlier engines' tables (`tools/whole_system.py`, "
              f"{', '.join(w['engines'])}), the cluster, the services on it and the cloud, by the rule that counts only what held in "
              f"all three runs: work up {w['work']:.1f}%, the 95th percentile {w['speed']:.1f}% faster, machines {w['machines']:.1f}% "
              f"fewer, energy {w['energy']:.1f}% less, the cloud's bill {bill}; the index over the gauges {w['index']:+.1f}%. Each "
              f"benchmark runs again on {eng}, and each total follows its own engine's tables."]
    L += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "", END]
    return "\n".join(L)


def page_html(m) -> str:
    """The same answer, as the live engine page's first section (#s-answer)."""
    md = markdown(m)
    body = md.split("\n", 1)[1].rsplit("\n", 1)[0]
    out, table = [], []
    def flush():
        if table:
            head, rows = table[0], table[2:]
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            out.append('<div class="tableWrap"><table class="ans"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in cells(head))
                       + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>" for r in rows)
                       + "</tbody></table></div>")
            table.clear()
    for ln in body.split("\n"):
        if ln.startswith("|"):
            table.append(ln); continue
        flush()
        if ln.startswith("## "):
            continue
        if ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
    flush()
    return ('<section class="stack" id="s-answer" aria-label="The answer first">\n  <h2><span class="sn">0</span>The answer first: is Omni-Compass a benefit against native?</h2>\n  '
            + "\n  ".join(out) + "\n</section>")


def inline(s: str) -> str:
    keep = []
    def stash(x):
        keep.append(x); return f"\x00{len(keep) - 1}\x00"
    s = re.sub(r'<img src="docs/engine/signals/(\w+)\.svg" alt="([^"]+)" height="14">',
               lambda mm: stash(f'<span class="mlamp lv-{ {"redlining": "red", "steady": "lead", "accelerating": "ok"}[mm.group(1)] }" title="{mm.group(2)}"></span>'), s)
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\[`([^`]+)`\]\(([^)]+)\)", r"<code>\1</code>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return re.sub("\x00(\\d+)\x00", lambda mm: keep[int(mm.group(1))], s)


SVG = {"accelerating": '<circle cx="7" cy="7" r="6" fill="#50c878"/>',
       "steady": '<path d="M7 1 L13 7 L7 13 L1 7 Z" fill="#f5c518"/>',
       "redlining": '<path d="M4.5 1 H9.5 L13 4.5 V9.5 L9.5 13 H4.5 L1 9.5 V4.5 Z" fill="#ff4d55"/>'}


def signals():
    d = ROOT / "docs" / "engine" / "signals"
    want = {f"{k}.svg": f'<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" role="img" aria-label="{k}">{v}</svg>\n' for k, v in SVG.items()}
    return d, want


def place(text: str, block: str, anchor: str) -> str:
    if BEGIN in text:
        a = text.index(BEGIN); z = text.index(END, a) + len(END)
        return text[:a] + block + text[z:]
    i = text.index(anchor)
    return text[:i] + block + "\n\n" + text[i:]


def place_readme(text: str, block: str) -> str:
    """The answer in the README: straight under the notice and the one line that says what Omni-Compass is."""
    if BEGIN in text:
        a = text.index(BEGIN); z = text.index(END, a) + len(END)
        return text[:a] + block + text[z:]
    tag = "**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**"
    i = text.index(tag) + len(tag)
    return text[:i] + "\n\n" + block + text[i:]


def place_after_title(page: str, block: str) -> str:
    """The answer on the live engine page: its own section straight under the one line of the legal notice, the first thing on
    the page, above the title page."""
    if BEGIN in page:
        a = page.index(BEGIN); z = page.index(END, a) + len(END)
        return page[:a] + block + page[z:]
    n = page.index('id="notice"'); i = page.index("</p>", n) + len("</p>")
    return page[:i] + "\n" + block + page[i:]


def main(argv) -> int:
    check, m = "--check" in argv, model()
    md = markdown(m)
    new_readme = place_readme(README.read_text(encoding="utf-8"), md)
    page = PAGE.read_text(encoding="utf-8")
    sec = page_html(m)
    blk = f"{BEGIN}\n{sec}\n{END}"
    new_page = place_after_title(page, blk)
    d, svgs = signals()
    differ = [n for n, new, old in (("README.md", new_readme, README.read_text(encoding="utf-8")),
                                    ("the live engine page", new_page, page)) if new != old]
    differ += [f"docs/engine/signals/{f}" for f, s in svgs.items() if not (d / f).exists() or (d / f).read_text(encoding="utf-8") != s]
    if check:
        print("headline: " + ("the README and the live engine page give the answer the files give" if not differ else f"{', '.join(differ)} differ: run python3 tools/headline.py"))
        return 1 if differ else 0
    README.write_text(new_readme, encoding="utf-8"); PAGE.write_text(new_page, encoding="utf-8")
    d.mkdir(parents=True, exist_ok=True)
    for f, s in svgs.items():
        (d / f).write_text(s, encoding="utf-8")
    print(f"headline: written from {m['path']} ({m['engine']}): " + "; ".join(f"{s['name']} {SIGNAL[s['signal']][0]}, work {100 * s['work']:+.1f}%" for s in m["scen"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
