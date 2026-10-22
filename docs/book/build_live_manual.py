# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The page word for word: the last appendix of the Live Engine Manual, written from the live engine page itself.

The founder's order of 20 October: three manuals in the end, the third reading the live engine top to bottom, so that the book
and the page read each other both ways. The book is docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md, built with the other two by
docs/book/build_book.py --live; its last appendix (Appendix L) is this file's output, docs/engine/PAGE_WORD_FOR_WORD.md: every
section of docs/engine/OMNI_COMPASS_LIVE_ENGINE.html in the page's own order with its number, title, summary and controls line,
every monitor under its own number with its evidence class, its state, the open-source feed that would carry it and its knobs
(docs/engine/monitors.json and the page's own order), every knob, and every LOSS row with its cause and the knob that answers
it, read from the page's embedded records. Nothing in it is typed twice. Rebuild it whenever the page changes, then the book:

  python3 docs/book/build_live_manual.py            docs/engine/PAGE_WORD_FOR_WORD.md
  python3 docs/book/build_live_manual.py --check    exit 1 if it differs from what the page gives
  python3 docs/book/build_book.py --live            the Live Engine Manual, with the appendix bound in
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.legal import NOTICE, TOP, PLAIN, normalize_markdown  # noqa: E402
from tools import readings as R  # noqa: E402

PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
REG = ROOT / "docs" / "engine" / "monitors.json"
OUT_MD = ROOT / "docs" / "engine" / "PAGE_WORD_FOR_WORD.md"
BOOK = "The Live Engine Manual"

CONTACT = ("The Omni-Compass LLC, main office infrastructure. Toll-free direct: 1-888-339-9551. System route asset: 1-888-DEX-YLL-1. "
           "Landline, registered in Florida: 321-746-4411. www.omni-compass.com")


def text(fragment: str) -> str:
    """Visible text of an HTML fragment, entities decoded, whitespace folded."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def embedded(page: str, key: str):
    m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % key, page, re.S)
    return json.loads(m.group(1)) if m else None


def model(page: str) -> dict:
    """The page as a book: the parts and sections in their order, each with its number, title, summary, controls, panels and
    monitors (every canvas, numbered in its order of appearance)."""
    body = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>', "", page, flags=re.S)
    canv = re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', body)
    canv = [c for c in canv if c != "wallCv"]
    number = {c: i + 1 for i, c in enumerate(canv)}
    items = []
    tp = re.search(r'<header class="head" id="title-page">(.*?)</header>', body, re.S)
    if tp:
        words = [("p", text(x)) for x in re.findall(r'<p class="lede"[^>]*>(.*?)</p>|<div class="realDisclose"[^>]*>(.*?)</div>', tp.group(1), re.S) for x in x if x]
        items.append({"kind": "section", "id": "title-page", "n": "iii", "title": "Title page and build", "summary": "", "controls": "", "words": [w for w in words if w[1]], "panels": [], "monitors": []})
    for m in re.finditer(r'<div class="partHead" id="([^"]+)"><span class="pn">([^<]*)</span><span class="pt">([^<]*)</span></div>|<section class="[^"]*" id="([^"]+)"', body):
        if m.group(1):
            items.append({"kind": "part", "id": m.group(1), "n": m.group(2), "title": html.unescape(m.group(3))})
            continue
        sid = m.group(4)
        i, depth, j = m.start(), 0, None
        for mm in re.finditer(r'<section\b|</section>', body[i:]):
            depth += -1 if mm.group(0) == "</section>" else 1
            if depth == 0:
                j = i + mm.end()
                break
        sec = body[i:j]
        h2 = re.search(r'<h2[^>]*>(?:<span class="sn">([^<]*)</span>)?(.*?)</h2>', sec, re.S)
        summ = re.search(r'<p class="plain"><b>Summary\.</b>(.*?)</p>', sec, re.S)
        ctl = re.search(r'<div class="secknobs"[^>]*><b>Controls\.</b>(.*?)</div>', sec, re.S)
        words = []
        for w in re.finditer(r'<h3[^>]*>(.*?)</h3>|<p class="(?:lede|note|plain)[^"]*"[^>]*>(.*?)</p>|<div class="realDisclose"[^>]*>(.*?)</div>|<summary>(.*?)</summary>', sec, re.S):
            if w.group(1) is not None:
                tx = text(w.group(1)); kind = "h"
            elif w.group(4) is not None:
                tx = text(w.group(4)); kind = "h"
            else:
                tx = text(w.group(2) if w.group(2) is not None else w.group(3)); kind = "p"
            if tx and tx not in ("—", "-") and not tx.startswith("Summary.") and len(tx) > 2:
                words.append((kind, tx))
        summ_t = text(summ.group(1)) if summ else ""
        if summ_t in ("", "—"):
            lede = re.search(r'<p class="lede"[^>]*>(.*?)</p>', sec, re.S)
            summ_t = text(lede.group(1)) if lede else ""
        items.append({"kind": "section", "id": sid, "n": (h2.group(1) or "") if h2 else "", "title": text(h2.group(2)) if h2 else sid,
                      "summary": summ_t, "controls": text(ctl.group(1)) if ctl else "", "words": words,
                      "panels": [text(x) for x in re.findall(r"<h3[^>]*>(.*?)</h3>", sec, re.S)],
                      "monitors": [c for c in re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', sec) if c != "wallCv"]})
    return {"items": items, "number": number, "canvases": canv}


READ = {   # how to read a monitor of each layer, and what the engineer in charge does with it
    "switch": ("The wiring from the top down: the master switch above the brain, the brain above the organism, the organism above every muscle, and native's own controllers under every muscle, never switched. The switch's state is the word on it: ON in green while Omni-Compass governs; engaged, the switch red and OFF in white.",
               "Press the kill switch only for security: it is instant, every setting goes back to native and is read back. Watch the governors' table beside it: every governor on the page says OFF and what it handed back."),
    "whole": ("Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.",
              "Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob."),
    "service": ("The four golden signals of a service, one point a decision of the live engine: native in amber, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.",
                "Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises."),
    "cluster": ("A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.",
                "Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries {engine}; an older engine's run is its own record."),
    "cloud": ("The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.",
              "The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands."),
    "orchestrators": ("Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.",
                      "Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's."),
    "chip": ("The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.",
             "Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its {engine} run lands."),
    "host": ("The processor's frequency ceiling (the knob), the clock the kernel's own governor ran at under it, the package power and the busy share, native beside Omni-Compass.",
             "Until a machine with its energy counter runs it, the monitor plays the harness's own modelled machine: read the mechanism, never the numbers."),
    "organism": ("The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.",
                 "Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did."),
    "organisms": ("Each organism or grid square read by the one key: green GAIN, yellow EVEN, red LOSS, grey a single run, dashed not yet run.",
                  "A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs."),
    "muscles": ("Every muscle of the catalog one cell, its word against native on its own load: green GAIN, yellow EVEN (pale: at its limit on native), red LOSS.",
                "Click a cell to read the muscle: its family, realm, template, knob and its word under each load."),
    "analytics": ("The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.",
                  "The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs."),
    "brain": ("The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.",
              "The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it."),
    "verdict": ("A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.",
                "A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it."),
    "console": ("The live engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.",
                "Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone."),
    "proof": ("The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.",
              "Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file."),
    "page": ("This page's own render loop governed by the compass law: the time between frames against its line, native (no governor) beside Omni-Compass.",
             "Load the page with the frame-load knob and watch the governor shed chart frames to keep every frame inside its line."),
    "ci": ("GitHub's runs in flight at the build by workflow, the Azure set's repetitions measured, each cloud's gate with its reason, the chips' runs.",
           "A gate that holds names its fix in its own words; nothing is billed while it holds."),
}


def md_lines() -> list[str]:
    page = PAGE.read_text(encoding="utf-8")
    reg = json.loads(REG.read_text(encoding="utf-8"))
    M = model(page)
    by = {m["id"]: m for m in reg["monitors"]}
    K = reg.get("knobs", {})
    L = reg.get("layers", {})
    build = embedded(page, "build") or {}
    scen = embedded(page, "scen") or {}
    eruns = embedded(page, "engineruns") or {}
    held = embedded(page, "heldout") or {}
    ledger = build.get("ledger") or {}
    eng, dig, commit, built = build.get("engine", ""), build.get("digest", ""), build.get("commit", "")[:12], build.get("built_at", "")
    from tools.omni_version import VERSIONS
    standing = f"omni-{next(iter(VERSIONS))}"    # the engine that stands: the version list's newest
    nmon = len(M["canvases"])
    out = [f"# {BOOK}", "", "How to read, operate, tune and watch the Omni-Compass live engine, native beside Omni-Compass, section by section, monitor by monitor and knob by knob", ""]
    out += ["## Front matter", "", "### What this book is", "",
            f"The third of the three manuals of Omni-Compass. The Operator's Manual shows an engineering team how to embed, wire, tune, run and check Omni-Compass on a stack; the Owner's Manual holds the whole mechanism, its mathematics, its source and every result. This book reads the live engine, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, from its first line to its last, so that an operator can sit at the page with the book open beside it and run it as the engineer in charge: read every gauge, turn every knob, press the switch, watch the organism, and know what every monitor shows, where its numbers come from, how strongly they stand, and what is still waiting for its run.",
            "",
            f"This edition was written from the page on the engine that stands, {eng} (digest {dig[:16]}), as the page was built {built} from commit {commit}. GitHub rebuilds the page's records every few hours; a page rebuilt since carries newer readings in the same sections and monitors, and the book is rebuilt with every change to the page's structure. The book is written from the page itself (`docs/book/build_live_manual.py`): every section, number, title, summary, control line and paragraph below is the page's own, every monitor is the page's own canvas under its own number, so the two read each other both ways.",
            "",
            "### How to use the book with the page", "",
            "- Open the page in a browser (the repository's copy, or its published copy). It runs entirely in the browser: it reads no live system, sends nothing anywhere, and draws every view from the records embedded in it at build time and from the engine's own mathematics running in it.",
            "- The page opens with its table of contents, under the one line of the legal notice; then the front matter (the title page and the key to every reading); then eleven sections from the whole organism down to the smallest part; then the back matter. Part II of this book follows the same order and the same numbers.",
            f"- Every monitor (every chart canvas) carries its number in a badge above it, from 1 at the top of the page to {nmon} at the bottom. The monitor wall in section 1a shows them all at once, numbered, read right to left and then down; this book lists each under its number with what it shows, its evidence, the open-source feed that would carry it on a running system, and its knobs.",
            "- Every section opens with a summary and a controls line saying whether its views are live (the engine running in the page, moved by the console's knobs) or recorded (a run or a table played back, which no knob can change).",
            ""]
    # ---------------------------------------------------------------- Part I
    key = R.key_text().split("\n")
    out += ["## Part I. Reading the live engine", "",
            "### 1. The two arms: native, and Omni-Compass on top of native", "",
            "Every view on the page has two sides and only two. **Native** is the system running by itself under its own controllers: the Kubernetes autoscaler, the card's own driver, the kernel's frequency governor, the cloud's own autoscaler, each muscle's own controller. **Omni-Compass** is the same system with Omni-Compass sitting on top of those native controllers, never in place of them. Native is drawn in amber, Omni-Compass in blue. Where a monitor draws two lanes, native is the left lane and Omni-Compass the right, on one scale, so that a line lying on the other never hides it. A red dashed line is the gauge's own limit (the response line, a temperature line). A red tick is a write the governor made.",
            "",
            "Omni-Compass is a supervisory governor: its one goal is to strengthen the organism and keep it healthy, every muscle working as far as its own limit and never past it (do no harm, `DISCLOSURES.md` section 3). The engine that stands keeps the strictest form of that rule: every muscle is judged on itself, never driven below native, nothing traded between muscles; where it cannot bring a knob a GAIN, the knob stays native.",
            "",
            "### 2. The key: GAIN, EVEN, LOSS and power given", ""]
    out += [ln if ln.strip() else "" for ln in key[1:] if not ln.startswith("<!--")]
    out += ["", f"The founder's floor of 20 October: a change under {100 * R.SIZE_FLOOR:.1f}% either way in every run reads EVEN, under the floor. The number beside a word carries the word's sign (GAIN +, LOSS −, EVEN =), never the gauge's raw direction. Colours follow the word everywhere on the page: GAIN green, EVEN yellow, LOSS red, power given blue.",
            "",
            "### 3. Evidence classes and the state of a monitor", "",
            "Every view says its evidence class: **P**, a physical meter (a card's own power meter, a processor's energy counter); **L**, live software (real Kubernetes, real databases, a real cloud, run on GitHub's own machines or in the cloud, played back from their own SHA-256-checked files); **S**, the repository's own models (the engine's harness, the toy cluster, the organisms, the grid), never presented as proof. Every monitor also says its state:",
            "",
            "- **live**: the engine's own mathematics running in the page (the brain, the compass law, the verdict), proven equal to the Python and the C++ to 1e-12 on every build; the console's knobs move it.",
            "- **replay**: a recorded run played back from its own files, second by second or decision by decision; no knob changes it.",
            "- **record** or **composed**: the repository's tables read at build time, or composed from them by a stated law.",
            "- **model**: a model of a machine standing in for a run not yet made (the CPU host), marked as such on the monitor itself.",
            "- **awaiting its run**: built before its run; its native lane shows what exists, its Omni-Compass lane stays empty, and the page names the run that fills it. Nothing on such a monitor is invented.",
            "",
            "### 4. The kill switch and the master switch", "",
            "One switch governs the whole organism, at the top, above the brain (`omnicompass/master.py`, `tools/omni_switch.py`). While Omni-Compass governs, the switch reads **ON** in green. Pressed, the switch turns **red**: at the next decision every governor puts every setting it wrote back, reads each one back and stops; the word **OFF** stands in white, and every Omni-Compass side of every monitor follows native, drawn in native's colour (a lighter tint of amber, dashed, so both lines stay visible). Native's own controllers under every muscle never stop and never see the switch. A recorded result never changes with it: its colour does, never a value, a word or a row.",
            "",
            "The same switch stands in the control panel at the head of section 1a, at the head of every section, in every monitor's own knobs and in the console (section 7): one press anywhere is one press everywhere. It is for security, and it is instant. The walk back after a crash is a different mechanism, the lease, which returns every setting to native gradually. The master switch's own panel in section 1a draws the wiring and lists every governor on the page with what it handed back.",
            "",
            "### 5. The control panel and the knobs", "",
            "The control panel at the top of section 1a holds the kill switch, the button that runs the Python's own runs in the page, the three manuals and the wall as a Grafana dashboard. The console (section 7) holds every runtime knob of the live engine; every monitor that is live carries the same knobs in its own strip under its canvas, so the organism can be driven from wherever one is looking. Every knob acts on both arms alike: the difference between the lanes is Omni-Compass's doing alone.",
            ""]
    for k, v in K.items():
        out.append(f"- **{v['label']}** ({k}): {v['what']}; on {v['where']}.")
    out += ["",
            "### 6. The monitor wall", "",
            f"The wall (section 1a) shows every monitor of the page at once: {nmon} canvases, each a tile carrying its number and its section. They are numbered in their order of appearance from the top of the page and laid out right to left, then the next row (the founder's order; a button reads them left to right instead). A tile with an accent border is a monitor on screen now. The page's own governor (section 11) rests a monitor while it is off screen; while the wall is in view the resting monitors are drawn in turn, one a frame. A click on a tile goes to the monitor. The inventory under the wall lists every monitor with its feed and its knobs, and names every monitor still awaiting its run.",
            "",
            "### 7. The Python's runs, in the page", "",
            f"The proof monitors in section 1a tie the page to the Python. `tools/engine_runs.py` runs N runs from a base seed: run k's seed is base + k·0x9E3779B9 mod 2³², its random stream mulberry32 (the page's own generator, written in the Python bit for bit). Each run steps the engine that stands through 288 decisions of the brain's state equations integrated by the fourth-order Runge–Kutta step, 80 steps of the compass law and one give-back trial judged by the verdict, and its receipt holds the brain's final state, its pushes and grants, the law's mean and last force and the trial's answer. The digest is the SHA-256 of every receipt at six decimals. The record in this build: {eruns.get('runs', '—')} runs from base {eruns.get('base', '—')}, digest {str(eruns.get('digest', '—'))[:32]}…",
            "",
            "Press **Run the Python's 500 runs here** and the page computes the same runs with its own port of the engine, in the browser's idle time, compares every receipt with the Python's and computes its own digest: the two must be one. **A new set** runs any other base in the page and prints the one command that runs the same set in the Python (`python3 tools/engine_runs.py --runs N --base B`), whose digest must equal the page's. **Print the receipts** opens every receipt, the Python's beside the page's, with both digests and the notice, ready for the printer; **Download** saves them as a file.",
            "",
            "Beside them the page replays the Python's 500 scenarios a seed of `benchmarks/stack_benchmark.py` (the held-out seeds " + ", ".join(str(s.get("seed")) for s in held.get("seeds", [])) + "): each scenario through every arm, native beside the chosen Omni-Compass arm, every scenario's trace hash and the record's own SHA-256. These are replayed from the record, never recomputed in the page; `verify.py` replays them on every push and `verify.py --full-replay` regenerates the whole file byte for byte.",
            "",
            "### 8. Grafana, Prometheus and the open-source feeds", "",
            "Every monitor on the page is the kind of panel an operator already runs in Grafana. The registry `docs/engine/monitors.json` names for each the open-source exporter and the Prometheus series that would carry it on a running system: node_exporter for the machines and the processor (its rapl and cpufreq collectors), kube-state-metrics for the cluster's objects, the NVIDIA DCGM exporter for the card, Kepler for energy by pod, OpenCost for the bill, the service's own request histograms for the golden signals, sloth or pyrra for the service level, and the governor's own exporter (`tools/omni_exporter.py`, read-only, from its audit) for every decision, write, hold and switch state. `docs/engine/export_grafana.py` writes the whole wall as one Grafana dashboard (`deploy/grafana/omni-compass-wall.json`): a panel a monitor, in the page's order and numbering, each on its series, beside the governor's own screen (`deploy/grafana/omni-compass.json`) and its alert rules (`deploy/prometheus/omni-compass-rules.yaml`). A monitor the page draws from the repository's tables or from its own clock becomes a text panel saying so. The control panel downloads the dashboard; the page itself reads no live system.",
            "",
            "### 9. The organisms and the whole stack, every way it is bought", "",
            "The catalog's seven organisms (the spine, 267 muscles, the base every stack runs on; the four realms; the four stacked; the whole tower of 1,107 muscles) each run native and with Omni-Compass on top, under their own load, the climb and work waiting in line. The orchestra stands beside them, every governor's muscles as one body. Section 3 composes the whole stack, the software, the cloud and the hardware, into one body: the founder counts it as the eighth organism running native and the ninth with Omni-Compass on top of every piece. It is composed four ways: on-site bare metal (software × bare metal), through the cloud (cloud × bare metal × software, and the cloud as two pieces), in the device (the bare metal alone) and as a service (the software alone).",
            "",
            "Through the cloud, the bare metal at the back end belongs to the provider: no tenant can meter it, so no run reaches it. The cloud piece is measured as what the provider meters and bills (the machines and the bill, native against Omni-Compass on top of the cloud's own autoscaler), which is also the provider's own benefit on its own hardware. The bare-metal piece is gauged on hardware we can meter and carried to the provider's bare metal only as a modelled factor of the same mechanism on the same kind of part, never as a measurement of the provider's machines (`DISCLOSURES.md` section 9). No run has stacked the layers yet: the composition is class S of class P and L measurements until the stacked run, preregistered in `docs/WHOLE_SYSTEM_PREREGISTRATION.md`, replaces it.",
            ""]
    # ---------------------------------------------------------------- Part II
    out += ["## Part II. The live engine, section by section", "",
            "Each part below is one section of the page, in the page's order and under its number: what the page says it is, its controls, its panels, and every monitor in it under its own number, with what it shows, its evidence and state, the feed that would carry it live, its knobs, how to read it and what to do with it.", ""]
    for it in M["items"]:
        if it["kind"] == "part":
            out += [f"### Part {it['n']} of the page: {it['title']}", ""]
            continue
        title = f"{it['n']} {it['title']}".strip()
        out += [f"### {title}", ""]
        if it["summary"]:
            out += [it["summary"], ""]
        if it["controls"]:
            out += [f"**Controls.** {it['controls']}", ""]
        if it.get("words"):
            out += ["**The page, in its own words.**", ""]
            for kind, tx in it["words"]:
                if tx == it["summary"]:
                    continue
                out += [f"**{tx}**" if kind == "h" else tx, ""]
        out += ["**Its monitors.**" if it["monitors"] else "**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.", ""]
        for cid in it["monitors"]:
            m = by.get(cid, {"name": cid, "what": "", "cls": "", "status": "", "feed": {"exporter": "", "metrics": [], "promql": []}, "knobs": [], "layer": "page"})
            n = M["number"].get(cid, "?")
            out += [f"#### Monitor {n}: {m['name']}", ""]
            if m.get("what"):
                out += [m["what"], ""]
            st = m.get("status", "")
            out += [f"- **Evidence and state.** Class {m.get('cls') or '—'}; {('awaiting its run: ' + m['awaiting']) if m.get('awaiting') else st}."]
            f = m.get("feed", {})
            feed = f.get("exporter") or "this page"
            if f.get("metrics"):
                feed += "; series " + ", ".join(f"`{x}`" for x in f["metrics"])
            if f.get("promql"):
                feed += "; on a running system: " + "; ".join(f"`{x}`" for x in f["promql"])
            out += [f"- **Feed.** {feed}."]
            if m.get("knobs"):
                out += ["- **Knobs.** " + "; ".join(f"{K[k]['label']}: {K[k]['what']}" if k in K else k for k in m["knobs"]) + "."]
            # "the engine that stands" is the version list's newest (tools/omni_version.py, the one list the books read the
            # engine from); the page's own build record says which engine its records were built on, and lags a landing until
            # the page is rebuilt (21 October: omni-v15 landed while the page's records were still omni-v14's)
            rd, act = (x.replace("{engine}", standing) for x in READ.get(m.get("layer", ""), ("", "")))
            if rd:
                out += [f"- **How to read it.** {rd}", f"- **What to do with it.** {act}"]
            out += [""]
    # ---------------------------------------------------------------- Part III
    wf = ledger.get("workflows") or {}
    aks = next((r for r in wf.get("aks-metered.yml", []) if r.get("status") != "completed" and r.get("progress")), None)
    gates = {t: next((r for r in wf.get("cloud-check.yml", []) if r.get("title") == t and r.get("status") == "completed"), None) for t in ("cloud-check google", "cloud-check amazon")}
    out += ["## Part III. Operating it as the engineer in charge", "",
            "### Watching: the first minute and the first hour", "",
            "- **The first minute.** Read the switch (ON green, or engaged red with OFF white). Read the status board's tiles: whether Omni-Compass is engaged, which signals are out of tolerance. Read the alarms, worst first: every LOSS row of every table is raised there with its source record.",
            "- **The first hour.** Watch the golden signals of the live organism (errors, throughput, latency, saturation), native beside Omni-Compass. Turn the console's knobs one at a time (demand, noise, sensor delay, a fault) and read how both arms take the same input. An alert minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an on-call page would be open. Omni-Compass aims at none: an alert minute on its arm is found and fixed, never accepted.",
            "- **No babysitting tax.** Omni-Compass is an autopilot: nobody turns a knob for it and nobody checks its work by hand. Every write is read back, every give-back runs on its own trial, every reason is in its audit; the settings it wrote on its own and its additions made inside the line are shown on every Kubernetes and cloud receipt.",
            "",
            "### When a row reads LOSS", "",
            "A LOSS row is never cut and never tuned away. The rule: first suspect the wiring, the native setup or the scoring; find where the mechanism or its wiring is wrong and correct that, in the toy gate first (`tools/toy_gate.py`), never in a real run; a change that reads no LOSS in the gate lands as the next engine version and every benchmark runs again on it. Where no setting of the muscle's knob brings the row EVEN, the muscle stays native on that stack: if Omni-Compass would hurt something, no mechanism of Omni-Compass is pushed through that muscle. The status board's table of LOSS rows names, for every one, whose row it is (Omni-Compass against its native, or an orchestrator's own cost with no Omni-Compass in either arm), its cause as the repository records it, and the knob that answers it; Appendix C lists them all.",
            "",
            "### Tuning and tweaking", "",
            "- **The dial.** The max, the default brain: every muscle runs at its own limit, never past it and never below native. The tune-down: never more than native; capacity handed back only with the organ's grant and the release gate. In the cloud every set runs at the tune-down on the machines alone, so the bill can only fall or stay.",
            "- **A muscle's own card.** Every muscle is wired on its own setting (`realms/muscle_cards_v5.csv`, the engine's setting otherwise): its band, cushions and glide. The factory tune is the owner's; a licensee may retune, add on or tune down any muscle, and a changed tune's results are its own (`DISCLOSURES.md` section 3).",
            "- **The next version.** Any change to a rule, gain, guard, preset or muscle makes the next engine version: built on its own branch, tried in the toy gate against the engine that stands, landed with `tools/land_engine.py` when it reads no LOSS, and every benchmark run again on it.",
            "",
            "### What waits, and what fills it", "",
            f"- **The GPU card.** The one metered run is the replaced controller's (2 October); the {eng} run on Lambda, from one exact commit given to the founder, replaces it.",
            f"- **The CPU host.** A Linux machine whose processor exposes its energy counter (RAPL) and a writable frequency ceiling (register row 79, `cpu-power.yml`); until then the monitor plays the harness's own modelled machine.",
            f"- **Azure.** " + (f"The set to the paid cap runs now: {aks['progress']['done']} of {aks['progress']['total']} repetitions measured at the build, under the stopping rule (the bill read at 10, 20, 40 and 70 repetitions with 99% intervals); its table is written when the set ends." if aks else "Its sets run from the queue, A, then B, then C."),
            f"- **Google Cloud.** " + ((gates['cloud-check google'].get('reason') or "the hourly gate holds") if gates.get("cloud-check google") else "its hourly gate decides when its first set starts."),
            f"- **Amazon Web Services.** " + ((gates['cloud-check amazon'].get('reason') or "the hourly gate holds") if gates.get("cloud-check amazon") else "its hourly gate decides when its first set starts."),
            "- **The stacked run.** The whole stack in one run, Omni-Compass at every piece at once against native at every piece, preregistered in `docs/WHOLE_SYSTEM_PREREGISTRATION.md`; until it runs, section 3 is a composition.",
            "",
            "### Rebuilding the page and the book", "",
            "The page is rebuilt by GitHub itself (`.github/workflows/live-engine.yml`, `docs/engine/build_live_engine.py`) whenever the engine, a model or a result changes, and every three hours; `build_live_engine.py --check` rebuilds every record in memory and fails if any differs from the page; `docs/engine/check_live_engine.py` proves the page's engine equal to the Python and the C++; `docs/engine/check_records.py` reproduces every record from the repository's own code; `tools/engine_runs.py --verify` runs the page's own loop of the Python's runs in node and compares the digests. This book is rebuilt from the page with `python3 docs/book/build_live_manual.py`.",
            ""]
    # ---------------------------------------------------------------- back matter
    out += ["## Back matter", "", "### Appendix A. Every monitor", "", "| No. | Monitor | Section | Class | State |", "|---|---|---|---|---|"]
    sec_of = {}
    for it in M["items"]:
        if it["kind"] == "section":
            for c in it["monitors"]:
                sec_of[c] = f"{it['n']} {it['title'].split(':')[0]}"
    for c in M["canvases"]:
        m = by.get(c, {"name": c, "cls": "", "status": ""})
        out.append(f"| {M['number'][c]} | {m['name']} | {sec_of.get(c, '')} | {m.get('cls', '')} | {'awaiting its run' if m.get('awaiting') else m.get('status', '')} |")
    out += ["", "### Appendix B. Every knob", "", "| Knob | What it does | Where it is |", "|---|---|---|"]
    for k, v in K.items():
        out.append(f"| {v['label']} | {v['what']} | {v['where']} |")
    out += ["", "### Appendix C. Every LOSS row, whose it is, its cause and the knob that answers it", ""]
    rows = []
    for rc in scen.get("receipts", []):
        way = re.search(r"_4W_(TOP|ORCH|BARE|VS|BOTH)\.md$", rc.get("file", ""))
        omni = (not way) or way.group(1) in ("TOP", "BARE")
        for r in rc.get("rows", []):
            if r.get("w") != "LOSS":
                continue
            cause = next((c for c in rc.get("causes", []) if r["g"].lower().startswith(c["gauge"].lower())), None)
            rows.append((omni, rc, r, cause))
    rows.sort(key=lambda x: not x[0])
    out += [f"{sum(1 for x in rows if x[0])} LOSS rows are Omni-Compass against its native; {sum(1 for x in rows if not x[0])} are an orchestrator's own cost against the organism alone, with no Omni-Compass in either arm. Every one is shown as its table writes it.", ""]
    for omni, rc, r, cause in rows:
        g = r["g"].lower()
        if not omni:
            knob = "nothing of Omni-Compass to turn: the orchestrator's own cost"
        elif re.search(r"pod start wait|start wait", g):
            knob = "the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms"
        elif re.search(r"response time|turnaround|time over the response line|wait", g):
            knob = "the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the toy gate, the muscle stays native on this stack"
        elif re.search(r"fail|lost|not served|unschedulable|no machine", g):
            knob = "the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS"
        else:
            knob = "the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the toy gate is refused and the muscle stays native"
        cz = f" Cause: {cause['title']} (`{cause['file']}`)." if cause else ""
        out.append(f"- **{'Omni-Compass against native' if omni else 'the orchestrator’s own cost'}.** {rc.get('title', '').split(':')[0]} ({rc.get('engine', '')}, `{rc.get('file', '')}`): {r['g']}, A B C {' · '.join(r.get('abc') or [])}.{cz} The knob: {knob}.")
    out += ["", "### Appendix D. Glossary", "",
            "- **Native**: the system under its own controllers alone. **Omni-Compass** (the omni arm): the same system with Omni-Compass on top of those controllers.",
            "- **Muscle**: one knob of the system a native controller turns (replicas, machines, a power limit, a frequency ceiling, a cache size). **Organism**: a body of muscles governed as one.",
            "- **Compass law**: the band with 5% cushions and two antagonist forces, smooth (tanh), that moves a muscle's setting (`omnicompass/compass_law.py`).",
            "- **Brain**: the engine's six state variables, integrated by the fourth-order Runge–Kutta step every decision (`omnicompass/core.py`). **Verdict**: the give-back trial judged against native (`omnicompass/verdict.py`).",
            "- **Kill switch**: the master switch's instant hand-back of every setting to native, for security. **Lease**: the gradual walk back to native after a crash.",
            "- **The max / the tune-down**: the dial's two settings. **Power given**: a resource spent that rose, shown beside what it bought, never a LOSS.",
            "- **A, B and C**: a benchmark's three runs; a reading counts when it holds the same way in all three.",
            "- **Evidence classes**: P a physical meter, L live software, S our own models.",
            "", "### Contact", "", CONTACT, ""]
    return out


# ---------------------------------------------------------------- the PDF
def appendix_lines() -> list[str]:
    """The book's last appendix: the page's sections, monitors and knobs word for word (Part II of md_lines) and the tables of
    every monitor, every knob and every LOSS row (its back matter), one heading level up; the reading guide, the operating
    notes, the glossary and the contact are the book's own chapters and are not repeated here."""
    lines = md_lines()
    def block(start, stop):
        i = next(k for k, ln in enumerate(lines) if ln.startswith(start))
        j = next((k for k, ln in enumerate(lines) if k > i and stop and ln.startswith(stop)), len(lines))
        return lines[i + 1:j]
    up = lambda ls: [ln[1:] if ln.startswith("###") else ln for ln in ls]
    page = PAGE.read_text(encoding="utf-8")
    build = embedded(page, "build") or {}
    out = ["# The Live Engine Page, Word for Word", "",
           "This appendix is the live engine page itself, written from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build of "
           "this book (`docs/book/build_live_manual.py`): every section in the page's own order with its number, title, summary and "
           "controls line; every monitor under the number its badge carries, with its evidence class, its state, the open-source "
           "feed that would carry it on a running system and its knobs; every knob; and every LOSS row with whose it is, its cause "
           "and the knob that answers it. Nothing here is typed twice: what the page says, this appendix says, so the book and the "
           f"page read each other both ways. This edition was written from the page built {build.get('built_at', '')} on "
           f"{build.get('engine', '')} (digest {build.get('digest', '')[:16]}) from commit {build.get('commit', '')[:12]}.", ""]
    out += up(block("## Part II.", "## Part III."))
    tail = block("## Back matter", None)
    keep, skip = [], False
    for ln in tail:
        if ln.startswith("### Appendix D.") or ln.startswith("### Contact"):
            skip = True
        elif ln.startswith("### "):
            skip = False
        if not skip:
            keep.append(ln)
    out += [re.sub(r"^## Appendix [A-C]\. ", "## ", ln) for ln in up(keep)]
    return out


def main() -> int:
    text_md, _ = normalize_markdown("\n".join(appendix_lines()))
    if "--check" in sys.argv:
        same = OUT_MD.exists() and OUT_MD.read_text(encoding="utf-8") == text_md
        print("the page word for word matches the page" if same else "the page word for word differs from the page: python3 docs/book/build_live_manual.py")
        return 0 if same else 1
    OUT_MD.write_text(text_md, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)} ({len(text_md.splitlines())} lines): the Live Engine Manual's Appendix L; "
          "now python3 docs/book/build_book.py --live")
    return 0


if __name__ == "__main__":
    sys.exit(main())
