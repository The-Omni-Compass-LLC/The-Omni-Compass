# THE OMNI-COMPASS LIVE ENGINE MANUAL

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## How to Read the Live Engine: Its Monitors, Gauges and Knobs, Native beside Omni-Compass

**October 2026**
**The Omni-Compass LLC**

All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.

---

# FRONT MATTER

## The Problem and Omni-Compass's Solution

**What the whole industry faces.** Demand for computing is growing faster than the power, the machines and the budgets
built to carry it. The International Energy Agency puts the world's data centres at about 415 TWh of electricity in 2024,
around 1.5% of all the electricity the world used, and expects that to more than double, to about 945 TWh, by 2030, with
artificial intelligence the largest driver. In the United States, Lawrence Berkeley National Laboratory counts 176 TWh in
2023, 4.4% of the country's electricity, and between 6.7% and 12% by 2028. The usual answer is to build more: more
machines, more megawatts, more cooling and a larger bill.

**Much of what is built sits idle.** Across the Kubernetes clusters Cast AI measured in 2025, the average processor was 8%
busy and the average memory 20% used, read before its own automation was switched on. The organizations Flexera surveyed
estimate that 29% of what they spend on cloud infrastructure and platforms is wasted.

**Not short of control, short of coordination.** In every realm (compute, AI and the cloud; physics, robotics and
autonomy; energy, facilities and industry; distribution and specialized systems) each machine already runs under local
feedback loops: horizontal autoscalers, firmware power and clock governors, building-management loops,
battery-management systems, connection pools, servo controllers. Each loop is tuned on its own, against its own setpoint,
with margins sized for a worst case. Four costs follow, and every operator pays them:

- **Reaction latency.** Reactive loops act on lagging, averaged signals. A Kubernetes Horizontal Pod Autoscaler
  recomputes its replicas every 15 seconds by default and damps its scale-downs over a 5-minute stabilization window; new
  pods then need time to schedule and start. Queues form before capacity arrives.
- **Static over-provisioning.** Worst-case margins persist through the far more common nominal regime. The operating
  point sits well inside the safe region, and the headroom between it and the constraint boundary is paid for and
  rarely used.
- **Uncoordinated coupling.** Loops share resources: power, cooling, connections, memory, network. One loop's correction
  is another loop's disturbance: more web replicas saturate the database's connections; more cooling pushes a power feed
  toward its limit.
- **The gaps closed by hand.** Operators close them with fixed settings, runbooks, alerts and on-call rotations, and the
  settings go stale as the load moves. That is safe, and it leaves the region between the operating point and the safe
  boundary unused nearly all of the time.

**Omni-Compass's solution: govern what is built before building more.** Omni-Compass is a supervisory governor. It
sits on top of every native controller and never in place of one; native keeps running underneath, always. It treats each
setting a native controller already exposes (a replica floor, a power cap, a clock ceiling, a temperature setpoint, a pool
size) as a muscle, and the whole stack as one body, the organism. Through a two-way plug, one wire in (the readings native
already reports) and one wire out (the settings native already exposes), it reads every muscle, places each reading in the
muscle's own band, from calm to its line (the limit it must not cross: a response time, a temperature, a feed's rating),
and moves each setting one bounded, smooth step at a time. By default every muscle is driven up to its own limit, never
past it and never below native; every write is read back; every give-back is tried in its own paired trial (the muscle with and without it, under the same load) and undone if the
muscle loses by it; a raise is held inside the muscle's own bounds and judged afterwards by the three-run tables; and
wherever no gain can be brought, the muscle stays native. One brain governs the whole body, so a step on one muscle stands only while every muscle it couples to stays
inside its own cushion. The aim, in one line: more work, faster, on fewer machines, with less energy. Where Omni-Compass takes more energy to buy more work or speed, that energy is shown beside
what it bought, as power given, and never called a loss.

**How it addresses each cost.**

| What the industry faces, and what it costs | How Omni-Compass addresses it | How it is judged |
|---|---|---|
| **Reaction latency**: waiting, queues and time over the line before capacity arrives | it reads every muscle on its own clock (on Kubernetes its full read of the state every 15 seconds, the autoscaler's own pace, and its fast checks every 5 seconds) and moves as a reading nears its line, not after the line is crossed: proactive as well as reactive, like an immune system | time waited, missed or failed: a fall is GAIN, a rise is LOSS |
| **Static over-provisioning**: machines, energy and a bill paid for headroom rarely used | every muscle driven up to its own limit and never past it, so the machines already paid for carry more work; in a public cloud it parks only a machine the cloud already made, after its own trial, and wakes it on a breach, so the bill can only fall or stay | work done: a rise is GAIN; machines, energy and the bill: a fall is a cut, a GAIN, and a rise is power given |
| **Uncoordinated coupling**: one loop's correction is another loop's disturbance | one brain for one body: a step on one muscle stands only while every muscle it couples to stays inside its own cushion | every muscle judged on itself, and the organism judged whole |
| **The gaps closed by hand**: settings retuned by hand, alert minutes, on-call | an autopilot: every write read back, every give-back on its own trial, every reason written to its audit; an alert minute on Omni-Compass's side is found and fixed, never accepted | the alert minutes, judged; the settings commands it wrote on its own, shown |

**Where the page shows each answer.** Reaction latency: the organism live, every muscle's place in its band and the
decisions past the line, native beside Omni-Compass (6a, `#s-engines`), and the shipped controller's decision trace (5e,
`#s-live`). Static over-provisioning: the benefit board (2, `#s-board`) and the clouds' bills (5a, `#s-cloud`).
Uncoordinated coupling: the whole organism (3, `#s-whole`) and the organism's immune system (6a, `#s-engines`). The gaps
closed by hand: the status board's alarms (1d, `#s-status`) and the golden signals, the event log and the live metrics
(1h, `#s-feed`).

**What it does not do.** It replaces no controller, and it creates no capacity a machine does not have: it uses the
capacity already there, each muscle to its own limit. It promises no number on a system it has not run on: the only number
that applies to a system is the one that system's own paired runs produce. The outside figures above are their authors'
own, quoted for scale; none was measured, checked or endorsed by The Omni-Compass LLC, and none is a result of
Omni-Compass.

**How it is held to account.** Every benchmark has two arms, native and Omni-Compass on top of native, on the same
machines with the same work, run three separate times. Every reading is one word, GAIN, EVEN or LOSS, decided by what the
gauge is for (the key, in this front matter); every result carries its evidence class (**P** a physical meter, **L** live
software, **S** our own models, never shown as proof of hardware); and every row is shown, LOSS included. The governing
rule is do no harm, in its one meaning (`DISCLOSURES.md`, section 3): the aim is an organism never left turning out less
than native, nor less healthy; where a row reads LOSS against native, the row stays, its cause is found and fixed, and the
test runs again. On the page this is section iii (`#s-problem`), the first after the title page; the executive summary under it
reads where the record stands from the records on the page, and this book carries no benchmark results of its own.

**The outside sources.** International Energy Agency, *Energy and AI* (April 2025), its executive summary. Lawrence
Berkeley National Laboratory, *2024 United States Data Center Energy Usage Report* (December 2024), prepared for the U.S.
Department of Energy. Cast AI, *2026 State of Kubernetes Optimization Report*: a seller of Kubernetes optimization,
reporting its own customers' clusters as they ran before its automation. Flexera, *2026 State of the Cloud Report* (March
2026): a survey of 753 cloud decision-makers and users, the figure their own estimate. The Kubernetes documentation,
*Horizontal Pod Autoscaling*: the controller's defaults.


<!-- the key: GAIN, EVEN and LOSS (tools/readings.py) -->
## The key: GAIN, EVEN and LOSS

Every judged reading in Omni-Compass is one of three words: **GAIN**, **EVEN** or **LOSS**. Better, same and worse are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before the runs.

| Word | What each letter stands for | Its sense in underwriting | What it means in a table |
|---|---|---|---|
| **GAIN** | **G** Growth (asset appreciation); **A** Advantage (risk reduction); **I** Improvement (margin expansion); **N** Net-positive (profitable outcome) | surplus and positive variance | the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a resource cut |
| **EVEN** | **E** Equalized (zero variance); **V** Verified baseline (expected norm); **E** Equilibrium (balanced risk); **N** Neutral (no net change) | the break-even baseline: equilibrium | native and Omni could not be told apart: the same, or no difference beyond the noise; a knob native already runs at the top of its range is EVEN, at its limit on native |
| **LOSS** | **L** Leakage (capital drain); **O** Off-track (adverse selection); **S** Setback (claim liability); **S** Subpar (negative variance) | actuarial deficit and exposure | the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures |

How the sign of a number becomes a word:

- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.
- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.
- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak that rose is power given, in a data centre and in a building alike (17 October).
- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; a fall is power given, because it falls when more power is given for the same work.
- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).
- **The floor** (the founder's order of 20 October 2026): a change under half of one percent (0.5%) either way, in every run, reads **EVEN, under the floor**; the row keeps its measured size. From 0.5% up, a change that holds the same way in all three runs reads GAIN or LOSS by the gauge's aim.
- **The sign beside a word** (the same order): the number next to a word carries the word's sign, never the gauge's raw direction, so that no one mistakes which way a number went: GAIN **+**, LOSS **−**, EVEN **=**. A bill cut 3% reads GAIN +3%, failed requests up 2% read LOSS −2%, and a change inside the noise reads EVEN =0.3%.

Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: TOWARD ITS AIMS reads GAIN; BOTH WAYS reads GAIN AND LOSS; AWAY FROM ITS AIMS reads LOSS; SAME AS NATIVE reads EVEN (the same as native); AT ITS LIMIT ON NATIVE reads EVEN (at its limit on native); SUPERIOR WITHIN GUARDRAILS reads GAIN (within the guardrails); ENERGY IMPROVEMENT WITH SERVICE TRADEOFF reads GAIN AND LOSS (energy cut, service traded for it); SERVICE IMPROVEMENT WITH ENERGY TRADEOFF reads GAIN, power given (service GAIN, energy given for it); NONINFERIOR / INCONCLUSIVE reads EVEN (inside the noise, within the guardrails); NOT ESTABLISHED reads EVEN (not established: inside the noise, a guardrail crossed on the mean). A run that breaks its own validity checks reads INVALID and carries no word.

A reading counts only when it holds the same way in all three of our runs, A, B and C, with every 95% interval clear of zero: "GAIN in all three of our runs". The other readings are **EVEN, no difference beyond the noise** (in a run the interval includes zero, so native and Omni could not be told apart: that is the result), **the runs disagree** (clear runs pointing different ways: the test is unstable there and is looked into) and **shown, not judged** (a gauge declared in advance as shown only, such as the knob's own setting).

Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as surplus, break-even or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (EVEN). Its first rule is do no harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit (`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.

Disclosure and disclaimer: GAIN, EVEN and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs measured against native under the declared aims, not a promise about any other system; every number stands beside its word, so a reader can judge it by any other convention. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end of the key -->

## What You Are Looking At: Omni-Compass, Hooked Up, and How to Read Its Report

**What the live engine is.** The live engine is one web page, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, built by the
repository's own code (`docs/engine/build_live_engine.py`) from the engine that stands and from the repository's own
results. It is a monitor of the engine and of the benchmark runs GitHub ran: every number on it is read from a record the
repository holds (a three-run table, a run's raw files, the engine's own audit, the realms table, the models' own readings),
and every word on it (GAIN, EVEN, LOSS, power given) is that record's own reading under `tools/readings.py`. The page decides
nothing about any result and types nothing in. Where it plays the repository's own models (evidence class S) it says so, and
a model is never proof.

**What "native" and "Omni-Compass" mean on the page.** Two names, two sides, nothing else. *Native* is the whole system
running by itself: every autoscaler, scheduler, firmware, thermostat, orchestrator and controller it ships with, every muscle
wired and moving by its own machinery. *Omni-Compass* always means Omni-Compass on top of native: the same whole system with
all of that still running underneath, and the governor on top of all of it, wired in through the two-way plug. No third side
exists anywhere on the page. Native is drawn in amber, Omni-Compass in blue, in every chart, table, tile and number.

**What a monitor is.** The page is laid out as an operations monitor is: a wall of tiles at the top (the status board), each
tile a small copy of a monitor further down the page; then the monitors themselves, section by section, each with its own
knobs in a bar at its head ("Controls"). A knob marked *Live* acts on the live engine, the engine's own mathematics running in
the page; a knob marked *Recorded data* only chooses which record is shown and never modifies it. Every monitor shows native
beside Omni-Compass on the same demand, the same seconds, so the one difference left between the two sides is Omni-Compass.

**What a gauge is.** A gauge is one measured quantity of the system (the work waiting, the work done, a response time, the
machines in service, the energy drawn, a bill). On the page each gauge is drawn for both sides with its paired reading: the
change from native, its 95% interval, and its word. The word is decided by what the gauge is for (the key, above), never by
the sign of its number. A rise in a resource reads *power given*, in blue, Omni-Compass's own colour, never a loss.

**How to read the page, in order.** First the switch and the engine (the master switch at the top of the wall, and the
engine's name, digest and commit in the title block). Then the four signals a service is watched by: the work waiting, the
work done, the decisions past their line and the capacity held, native beside Omni-Compass. Then every reading that went
against native, worst first (the alarms). Then the benefit board (the page's section 2), the whole organism, every way it is bought
(the page's section 3), the measured effect in full (the page's section 4), the evidence stack by stack from the cloud down
to the chip (the page's section 5), the organism live (the page's section 6), the console (the page's section 7) and the
brain (the page's section 8). The back matter of the page (disclosures, governing law, contact) says what the page is and is
not. This manual follows that order, chapter by chapter.

**What this manual is, and is not.** It is the interpretation of the page: how to follow the dashboard, read each gauge,
turn each knob, and see the mechanism of action of Omni-Compass against native as the monitors show it. It does not explain
how the engine is built (the Owner's Manual does), and it does not say how to wire Omni-Compass onto a stack (the Operator's
Manual does). Nothing in it decides a result: the records of authority are the repository's result files, the raw files GitHub
archived with their SHA-256 lists, the two other manuals and `DISCLOSURES.md`.

## Notice and Disclaimer

This manual describes the live engine page as `docs/engine/build_live_engine.py` builds it on the engine that stands
(omni-v13, `OMNI_V13.json`). The page names its engine on its own `<html>` element (`data-engine`); the build stamps the engine that stands
on it and rebuilds every record, and `--check` fails a page whose engine differs; where the page you are reading names a newer engine, the page is right and this manual is realigned with it in the
same push. The page's own table of contents (its section v, "Engine table of contents") is the authority on the order and the
numbering of its sections; this manual names every section by its title and its anchor (`#s-health`, `#s-ops`, and so on), which
do not move when sections are renumbered.

The published benchmarks the page plays are the record of what Omni-Compass did on the systems, loads and engine they name,
each with its evidence class. Where a result on any other system differs from them, or anything on the page looks wrong, the
first presumption is the wiring, the settings, or how Omni-Compass was implemented or read, not the law (`DISCLOSURES.md`, section 4). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Foreword

A governor that cannot be watched cannot be trusted. Every controller a stack already runs has a dashboard somewhere: the
autoscaler's replica count, the card's clock and power, the building's setpoints. What none of them had was one wall where the
whole body is seen at once, native beside the same body governed, decision by decision, with the record each number came
from one click away. The live engine is that wall, and this book is how to read it.

I asked for it to be a monitor and not a drawing: every record on it made again by the repository's own code, every raw file
checked against its own SHA-256 list before a byte of it is drawn, every word on it the run's own reading and never one drawn
from the stream. So the page can be trusted the way a meter is trusted: it shows what the record holds, and when the record
has nothing yet (a cloud set still running, a chip run not yet started) it says so and shows nothing in its place.

Read the key first. Then stand at the wall. The switch and the engine come first, the four signals of the living organism
next, and every reading that went against native is raised before anything that went for it. If a tile reads LOSS, this book
tells you where its record is and what to do: the row stays, its cause is found (our wiring first, native's setup second, the
scoring third), and the test runs again. Nothing on the page is pushed toward GAIN; the only thing forced is the mechanism.

## The Three Manuals: the Operator's, the Owner's and the Live Engine's

Three books stand in the repository, each for a different reader, and each says what it leaves out.

| Book | For whom | What it carries | What it leaves to the others |
|---|---|---|---|
| The Operator's Manual (`docs/OMNI_COMPASS_MANUAL.pdf`) | the engineering team that embeds, wires, tunes, runs and checks Omni-Compass on a stack | the plug, the wire check, the eight levels, every stack, the switches and the lease, the implementer's guide for the cloud, every muscle's wiring and card | nothing on how the engine is built; no benchmark results |
| The Owner's Manual, the master (`docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`) | whoever owns or licenses Omni-Compass and must know the whole mechanism | the philosophy, the mathematics, the mechanism, the engine's source, every result, the wiring | nothing: it is the master |
| The Live Engine Manual (this book, `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`) | the operator at the dashboard | how to follow the live engine page: its monitors, gauges and knobs, and the mechanism of action native beside Omni-Compass as the monitors show it | how the engine is built (the Owner's); how to wire it (the Operator's) |

A reading on the page and a reading in a receipt are the same reading: the page draws the receipt. Where this book and a
receipt seem to differ, the receipt governs, and the page is rebuilt.

## Preface: How to Use This Manual

| You are | Read |
|---|---|
| The operator on shift, at the wall | the Quick Reference card; chapters 4 to 7 (the wall, the switch, the alarms and the feed); chapter 28 (when a tile reads LOSS); Appendix E |
| CTO, architect, head of platform | the front matter; chapters 8 and 9 (the benefit board and the whole organism); chapter 26 (the mechanism of action, side by side); chapter 29 (what the page does not tell you) |
| CEO, CFO, CIO, board member | the Foreword; the front matter's "Disclosures, Declarations and Disclaimers"; chapter 9 (the bills and receipts, every way a stack is bought); section 8.3 (one figure for the whole board); chapter 10 (the bill in a cloud) |
| Site reliability engineer, on call | the Quick Reference card; chapters 4 to 6 (the golden signals, the alarms, the event log, the OpenMetrics exposition); chapter 12 (the heart and the two tickers); Appendix C |
| Control or plant engineer | chapters 19 to 22 (one control cycle, the phase plane, the brain's state, the verdict); chapter 24 (the component specification); chapter 18 (the console's knobs) |
| Auditor, diligence team | chapter 1 (a monitor, not a drawing); chapter 27 (from a tile to its record); chapter 31 (verifying the page); the page's own appraisal, `docs/engine/APPRAISAL.md` |
| Procurement, counsel and attorneys | `LICENSE`, `NOTICE`, `PATENTS.md`, `TRADEMARKS.md`, `DISCLOSURES.md`, `LICENSING_FAQ.md`, `ENTERPRISE_LICENSE.md`, `SECURITY.md`, bound into this book in full (the front matter's Disclosures; Appendices F to K); chapter 30 |

**Conventions.** `code` is a command, file, anchor or switch exactly as typed. "Native" means the system as it runs today,
without Omni-Compass, drawn in amber. "Omni-Compass" means that same native system with Omni-Compass on top of it, drawn in
blue; there is no third side and no other name. "Muscle" means any machine, service or controller Omni-Compass can read and
set. "Knob" or "lever" means one setting on a muscle; on the page, a knob is also a control in a monitor's "Controls" bar, and
the text says which is meant. "The band" is a reading's safe range, from calm (p = 0) through its center (p = 0.5) to its line
(p = 1). "A decision" is one turn of the governor's loop. "A tile" is one small monitor on the wall. "A section" is one
numbered part of the page, named by its anchor. Every step that acts on the live engine is marked **LIVE**; a step that only
chooses a record is marked **RECORDED**. Every number carries its evidence class: **P** a physical meter, **L** live software,
**S** our own models (modelled). A number from a model is never written as if it came from hardware.

**The standards every page of this manual keeps.** The page, and so this book, keeps the following discipline throughout:

1. **Two sides, always.** Every monitor shows native beside Omni-Compass, the same whole system on the same demand, the same
   draw of noise, the same injected fault, at the same second. Omni-Compass is never shown standalone and never as a
   competitor to the controllers it sits on.
2. **Nothing typed in.** Every number is read from a record the repository holds when the page is built or opened; every raw
   file is matched against its run's own SHA-256 list before it is drawn; the brain, the compass law and the verdict running
   in the page are the engine's own code, ported and proven equal to the Python and the C++ on every build
   (`docs/engine/check_live_engine.py`).
3. **The record's own word.** Every word on the page is the reading its record carries under the one key; the page never
   draws a word from the stream it plays, and never prints "up", "down", "better" or "worse".
4. **Every row, LOSS included.** A reading that went against native is raised first, as an alarm, with its source record and
   the repository's root-cause document where one exists. Nothing is cut from the page because it went against Omni-Compass.
5. **Nothing read across engine versions.** The page names the engine it stands on, every record is rebuilt on the engine that stands, and `--check` fails a page whose engine differs; each
   three-run table on it names its own engine, and a table stands on an older engine only until its runs on the engine that
   stands land.
6. **Models are not proof.** Every view says its evidence class. The official Kubernetes and database runs are class L, played
   from their own checked files. The harness, the shipped controller on the toy cluster, the GPU card, the Linux host, the
   realms table and the grid are class S, our own models, shown beside the real runs and never presented as proof.
7. **Do no harm, in its one meaning.** Every knob on the console acts on both sides alike; what Omni-Compass does with it is
   held by its guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another
   on the engine that stands, a give-back tried against native first and refused on a LOSS (`DISCLOSURES.md`, section 3).

**How this manual is organised.** Part I says what the page is: a monitor, how it is built, its table of contents and its
two sides and colours. Part II is the wall and the switch: the numbered monitors, the status board, the master switch, the alarms, the golden-signal
feed, the event log, the metrics exposition and the pipeline that rebuilds the page. Part III is the measured effect and the
whole, in the page's order: the benefit board, the grid and the catalog, then every way a stack is bought, with its bills and
receipts. Part IV is
the evidence stack by stack: the clouds, the orchestrators, the official Kubernetes runs and their playback, the shipped
controller's decision trace, the chip and the host. Part V is the organism live and the console. Part VI is the brain: one
control cycle, the phase plane, the brain's state, the verdict, the failure modes, the component specification and the page
that governs its own drawing. Part VII reads a result off the page: the mechanism of action side by side, the trace from a
tile to its record, what to do when a tile reads LOSS, and what the page does not tell you. Part VIII is the license and how
to verify your copy of the page. The back matter holds the glossary, every section of the page, every control of the console,
every gauge on the wall, the colours and marks, troubleshooting, and the papers counsel asks for.

## Where to Get Help

| You need | Where it is |
|---|---|
| What a tile means | chapter 4 (the wall, tile by tile) and Appendix C (every gauge, its side, its aim, its word) |
| What a knob does | chapter 18 (the console) and Appendix B (every control, what it acts on, what it leaves alone) |
| Why a reading is red | chapter 28 (when a tile reads LOSS), then the record it names (chapter 27) and the Operator's Manual's "wired right or wired wrong" |
| Why a monitor is empty or grey | chapter 29 (what the page does not tell you) and Appendix E (troubleshooting the page) |
| Why the page is slow | the page's section 11 and chapter 25 (the page governs its own drawing; a chart farthest from where you are looking waits a frame) |
| What the engine is | the title block of the page (its name, digest and commit); `python3 tools/omni_version.py`; the Owner's Manual for everything inside it |
| How to wire it | the Operator's Manual, in order; nothing in this book wires anything |
| Licensing, pilots, the Enterprise License | the Contact page at the back; www.omni-compass.com |

## Prelude: A Night at the Wall

It is a quarter past two. The on-call engineer has the wall open on one screen and the cluster's own console on the other.
On the wall the switch is green and reads ON. Under it the four signals of the service: the work waiting, the work done, the
decisions past their line, the capacity held; native in amber on the left of each tile, Omni-Compass in blue on the right,
both moving on the same demand. The amber line of the work waiting climbs as the night's batch starts; the blue line climbs
too, then bends sooner, because the governor's ticker (the page's section 5c) shows the pedal pushed at the first decision
the compass left its center, and two machines recommended before native's autoscaler had seen its first late sample.

A tile in the alarms row turns red. It reads LOSS: the pod start wait, mean, +13% in one run. The engineer clicks it and lands
on the three-run table it came from: run A of the Azure steady set, 33 paired repetitions, the interval −44 to +60 seconds,
*no* in the significant column. The red is the run's own word for this run; in the three-run reading it is not yet a reading at
all, because the interval includes zero. The row stays on the page, as every row does. The engineer opens the root-cause
document the tile links to, `docs/POD_START_WAIT.md`, and reads that a pod's start on a shared host is the test machine's
own unpacking of an image, the same on both sides at the same host load. Nothing to do tonight; the record is complete.

At three the batch is done. The blue line of the capacity held eases back a step at a time toward the amber one: the pedal
lifted, the lease walking every setting toward native. The engineer scrolls to the page's section 8b, the phase plane, and watches sixty
dots drift from the right edge back toward the middle line, native's a few decisions behind. Then back to the wall. Switch
green, four signals calm, the alarms row empty but for the one red tile that will stay until its runs B and C land and the
three of them are read together. The page's own age, in the last tile, reads twelve minutes.

## Introduction: The Page, Its Monitors and What This Manual Covers

**The problem the page answers.** Omni-Compass's answer to the problem the whole industry faces (the first section of this
front matter) is a supervisory governor on top of controllers that each have their own dashboard, and the owner of the
stack has to answer one question about it every day: is it doing what the receipts say, right now, on this
body, and would I see it if it were not? The receipts are tables; a table is read after the fact. The page is the same
record played back in motion, native beside Omni-Compass, with the governor's own decisions and the native controllers' own
moves on two tickers side by side, so the mechanism is seen, not inferred.

**What the page is made of.** Four exporters build its records on the engine that stands: the realms harness (one organism and
each muscle alone; `docs/engine/export_harness_trace.py`), the shipped controller on the toy cluster (on top of the
autoscaler at the max, and in the cloud's setting; `docs/engine/export_controller_trace.py`), the official runs read back from
their raw files and scored again by the repository's own scorer (`docs/engine/export_runs.py`, `tools/live_reps.py`), and the
chip and host models with every judged row of the newest receipts (`docs/engine/export_scenarios.py`). A fifth record is the
build itself: the engine, the commit, the time, and GitHub's own list of the runs in progress and of every run started for
the chips and the clouds (`docs/engine/github_ledger.json`).

**What runs live in the page.** The brain (`omnicompass/core.py`, integrated by the fourth-order Runge–Kutta method), the
compass law (`omnicompass/compass_law.py`) and the verdict (`omnicompass/verdict.py`) run in the page itself, ported to the
browser and proven equal to the Python and the C++ on every build. They govern a stress-test model of sixty muscles, each on
top of its own native controller, and they govern the page's own drawing (the page's section 11). Everything else is a record played
back.

**What this manual covers.** Every section of the page in the page's own order; every gauge, with its side, its aim and its
word; every knob of the console, with what it acts on and what it leaves alone; the two tickers that show the mechanism of
action; the trace from any tile to the record it came from; and what to do when a tile reads LOSS. It covers the page as
built on omni-v13; a later engine renames itself on the page's title block and this book is realigned in the same push.

**What this manual does not cover.** How the engine is built, its equations beyond the ones the page itself prints, the
wiring of Omni-Compass onto any stack, and the benchmark results themselves as a body of evidence: those are the Owner's and
the Operator's Manuals and `docs/STATE_OF_PLAY.md`.

## Quick Reference: The Card for the Glove Box

Keep this card beside the screen that shows the wall. Every line is explained in the chapter named beside it.

**The two sides** (chapter 3). Amber is native, the system by itself. Blue is Omni-Compass on top of native. Nothing else is
drawn.

**The three words** (the key). Green GAIN, yellow EVEN, red LOSS. A resource that rose is *power given*, blue. White with a
dashed edge is *the runs disagree* or *the runs differ*; grey is *shown, not judged*; neither is a reading.

**The switch** (chapter 5). At the top of the wall. Green ON: the governor's outputs reach the muscles. Red: the kill switch
engaged, every setting handed back to native at once, the decisions shaded red. White OFF: the brain reads in shadow and
nothing it computes leaves it; every Omni-Compass side follows native in native's colour.

**The four signals** (chapter 4). The work waiting, the work done, the decisions past their line, the capacity held: latency,
traffic, errors and saturation in site-reliability terms; native beside Omni-Compass on each.

**The alarms row** (chapter 6). Every reading that went against native, worst first, each with its source record and its
root-cause document where one exists. ALERT, WARN, INFO as an operations log grades them.

**Where a number comes from** (chapter 27). Click the tile: it opens the monitor it is a copy of. The monitor names the table,
the run and the file; the file's SHA-256 was matched before it was drawn. Open the table in `results/live/`; open the raw
files on the `raw` branch.

**When a tile reads LOSS** (chapter 28). The row stays. Read the three-run reading, not the one run. Open the root-cause
document. The cause is found in this order: our wiring, native's setup, the scoring. The test runs again. Nothing is tuned
toward GAIN; where Omni-Compass cannot bring a knob a gain, that knob stays native.

**The console** (chapter 18). Every knob acts on both sides alike. Demand ×1 is the day as written; noise σ, sensor delay,
and four faults of 40 decisions each (a surge, half the machines lost, a sense blind, a security hold); the dial (the max or
the tune-down); pause, one decision, 1× to 60×; the same day again or a new day; every knob to its start.

**The age of the page** (chapter 7). The last tile of the wall. The page is rebuilt by GitHub on every change to the engine,
a model or a result, and every three hours.

**What the page is not** (chapter 29). It decides nothing. Class S views are models, not proof. The records of authority are
the result files, the raw files and their SHA-256 lists, the manuals and `DISCLOSURES.md`.

## Table of Contents

Part I. The Page as a Monitor: 1. A Monitor, Not a Drawing; 2. The Engine Table of Contents and the Numbering; 3. The Two
Sides and the Colours. Part II. The Wall and the Switch: 4. The Monitor Wall; 5. The Master Switch; 6. The Alarms, the Feed,
the Event Log and the Metrics; 7. The Pipeline That Rebuilds the Page. Part III. The Measured Effect and the Whole: 8. The Benefit Board, the Grid and the Catalog; 9. The Whole Organism, Every Way It Is Bought. Part IV. Evidence by Stack: 10. The Clouds; 11. The
Orchestrators and Governors; 12. Kubernetes: the Official Run Playback; 13. Kubernetes: Per-Repetition Telemetry; 14. The
Shipped Controller's Decision Trace; 15. The Chip and the Host. Part V. The Organism Live and the Console: 16. The Organism,
Live; 17. The Telemetry Analytics and Omni-Compass in Its Own Words; 18. The Control Console. Part VI. The Brain: 19. One
Control Cycle, Traced; 20. The Phase Plane and the Scoreboard; 21. The Brain's Internal State; 22. The Verdict; 23. Failure
Modes, Controls and Residual Risk; 24. The Component Specification; 25. The Page Governs Its Own Drawing. Part VII. Reading a
Result off the Page: 26. The Mechanism of Action, Side by Side; 27. From a Tile to Its Record; 28. When a Tile Reads LOSS;
29. What the Page Does Not Tell You. Part VIII. License and Your Copy: 30. License and Commercial Terms; 31. Verifying Your
Copy of the Page. Back matter: Glossary; Appendices A to K; Index; Contact.

---

# PART I. THE PAGE AS A MONITOR

## 1. A Monitor, Not a Drawing

### 1.1 What the page is

The live engine is a monitor of the Omni-Compass engine and of the benchmark runs GitHub ran. A
monitor shows what its instrument reads; a drawing shows what its author believes. The page is the former by construction:
every record it replays is made again by the repository's own code on the checkout it is built from, and `--check` fails a
page whose engine is not the one `python3 tools/omni_version.py` reads. So the page never runs ahead of the repository: when
a new engine stands, the build stamps it on the page and rebuilds every record on it, and the page says in a banner that its
prose was written for the older engine until a person realigns the words.

### 1.2 The five records

The page carries five kinds of record, and every monitor says which it plays.

| Record | Made by | What it holds | Class |
|---|---|---|---|
| The harness | `docs/engine/export_harness_trace.py` | the realms harness (`realms/harness.py`, the max of `realms/compass_arm_v5.py` with the bone, the twins and the immune system): one organism of sixty muscles, and each muscle alone, native and with Omni-Compass on top, decision by decision | S |
| The controller | `docs/engine/export_controller_trace.py` | the shipped Kubernetes governor (`omni_controller/controller.py`) on the toy cluster, on top of the autoscaler at the max and in the cloud's setting, every tick and every audited decision, runs A, B and C of six hours | S |
| The runs | `docs/engine/export_runs.py` | the official runs as recorded: every three-run table's runs A, B and C read back from their raw files, every file's SHA-256 matched against the run's own list, every Kubernetes repetition scored by `tools/live_reps.py` and checked against the run's result | L |
| The scenarios | `docs/engine/export_scenarios.py` | the GPU card (`realms/gpu_card.py`), the Linux host (the conveyance of `tools/toy_gate.py`), every muscle and organism of the realms table (`results/realms_v5`), and every judged row of the newest engine's receipts (`results/live/V13_*.md` as they land) | S, with the receipts' own classes |
| The build | `docs/engine/build_live_engine.py` | the engine, its digest and the commit; the time; GitHub's runs in progress and queued; every run started for the chips and the clouds (`docs/engine/github_ledger.json`) | the record of the build |

### 1.3 What runs live

Three parts of the engine run in the page itself: the brain (`omnicompass/core.py`), the compass law
(`omnicompass/compass_law.py`) and the verdict (`omnicompass/verdict.py`), each ported to the browser and proven equal to the
Python and the C++ on every build by `docs/engine/check_live_engine.py`. They drive the stress-test model of sixty muscles
(the page's sections 6a, 7, 8a to 8c) and the page's own render loop (the page's section 11). Nothing else computes on the page: every other
monitor plays a record.

### 1.4 What the page decides

Nothing. Every word on it is the reading its record carries under the one key
(`tools/readings.py`), applied once, in the repository, when the table was written. The page never reads a word off the stream
it draws. When a monitor has no record yet (a cloud set still running, a chip run not yet started), it says what the
repository holds and shows nothing in its place: the empty slot is itself a true reading of the record.

### 1.5 The appraisal

Every view of the page is reproduced from the repository's own code by an independent path and
compared value by value (`docs/engine/APPRAISAL.md`; rerun with `docs/engine/check_live_engine.py` and
`docs/engine/check_records.py`). The brain's mathematics agree to machine precision; the harness views and the live controller
are identical to the repository's own runs on every tick and every plant. Chapter 31 says how to rerun the appraisal on your
copy.

## 2. The Engine Table of Contents and the Numbering

### 2.1 The page's own contents

The page opens with its legal notice (i), then the title page with the build (ii), the problem the whole industry faces and
Omni-Compass's solution (iii), the executive summary with the reading key (iv), and then its own table of contents (v, "Engine
table of contents"): the founder's orders of 21 October, the title, the problem and the solution, the summary and the key first
and the contents after them. Beside the title, on a desktop, stand the owner's two
illustrations, one above the other (on a phone they sit under the title): the stacks Omni-Compass sits on top of as he pictures
them, and under it the Omni-Compass as the unified control authority. Each says under it that it is an illustration, not a result,
that the product marks in it belong to their owners with no endorsement stated or implied, and what the engine draws over it: a
ring at every decision of the live engine; on the rose two hands, native's (amber, the longer) and Omni-Compass's (blue), each at
the mean place of that side's muscles in their bands, calm at north and the line at south; on the control core a glow that grows
with the settings Omni-Compass wrote in that decision; and under each, that decision's counts. The marks are the engine's state
(the page's section 6a), never a number of the picture's own. The body is numbered 1 to 11; the back matter is vi
(disclosures, governing law and contact) and vii (the closing legal notice). A section's number is printed before its title; a
lettered section (1a, 5c) is a section inside the numbered part that holds it, and every one is lettered: part 1 runs from 1a
to 1i, one letter for each of its panels, with no unnumbered entry in the contents.

### 2.2 The sections, as built on omni-v13

Appendix A lists every section with its anchor and the chapter of this book that
reads it. In the page's order: 1 the monitor wall and the control panel (1a the control panel and the kill switch, 1b the
monitor wall, 1c the monitor list, 1d the status board, 1e the master switch's wiring, 1f the Python's runs in the page, 1g
every LOSS row, 1h the golden signals, the event log and the live metrics, 1i the pipeline); 2 the benefit board; 3 the whole organism, every way it is bought; 4 the
measured effect in full (the organisms, every muscle, the register, the grid and every three-run table); 5 the evidence by
stack (5a the clouds, 5b the orchestrators and governors, 5c Kubernetes, the official run playback, 5d Kubernetes,
per-repetition telemetry, 5e the shipped controller's decision trace, 5f the chip and the host); 6 the organism live (6a
native and Omni-Compass, 6b the telemetry analytics and Omni-Compass in its own words); 7 the console; 8 the brain (8a one
cycle, 8b the phase plane, 8c the brain's state, 8d the verdict); 9 the failure modes; 10 the component specification; 11 the
self-governed rendering.

### 2.3 Anchors

Every section has an anchor that does not move when the page is reordered: `#s-problem`, `#s-read`, `#p-health`, `#s-health`,
`#s-wall`, `#s-monlist`, `#s-status`, `#s-master`, `#s-proof`, `#s-loss`, `#s-feed`, `#s-github`, `#s-board`, `#s-whole`, `#s-fleet`, `#p-evidence`, `#s-cloud`, `#s-orch`, `#s-ops`, `#s-runs`, `#s-live`, `#s-stacks`,
`#p-organism`, `#s-engines`, `#s-lab`, `#s-desk`, `#p-brain`, `#s-decision`, `#s-plane`, `#s-brain`, `#s-verdict`, `#s-fail`,
`#s-math`, `#s-self`, `#s-disclose`. A tile on the wall links to the anchor of the monitor it copies; a row of the table of
contents links the same way. When this book names a section it gives its title and its anchor, so the reader finds it on a
page whose numbering has moved.

### 2.4 The order, and why

The founder's order of 20 October: the wall first, then the benefit board, then the whole
organism, then the evidence from the cloud down to the chip, the organism live, the console and the brain. The order is the
order a person reads a system: is it healthy now (the wall), what has it bought (the board and the whole), where is the proof
(the evidence), what is it doing this second (the organism live), what can I do to it (the console), and how does it think (the
brain). The disclosures close the page as they open it.

## 3. The Two Sides and the Colours

### 3.1 The sides

Native is amber, Omni-Compass is blue, everywhere: every line, bar, tile and number that belongs to one
side wears that side's colour, in every chart and table. Where a monitor draws the two sides on one axis, native is the left
lane or the upper row; where it draws them as two instances (the organism, the phase plane), native is on the left.

### 3.2 The words

GAIN is green, EVEN is yellow, LOSS is red. Every reading, in every table, chart, bar and tile, wears one
of those three colours, or blue for power given, and no other. Power given wears blue, Omni-Compass's own colour, because it is
what Omni-Compass put in. *The runs disagree* and *the runs differ* are white with
a dashed edge, and *shown, not judged* is grey, because none of them is a reading. The size printed beside a word is how far
the gauge moved from native and carries the word's own sign (GAIN +, LOSS −, EVEN =), never the gauge's raw direction. A
change under half of one percent either way reads EVEN, under the floor.

**How the executive summary counts** (the consensus audit of 21 October, `docs/engine/CONSENSUS_AUDIT_2026-10-21.md`). Its first
line counts the three-run tables of Omni-Compass against its native apart from the orchestrators' own cost: the four-ways tables in
which Omni-Compass is in neither arm, or on the other side of the comparison, are counted in a sentence of their own and never in
Omni-Compass's words. The floor reads every judged word, GAIN, LOSS and power given alike, in the tables, in the models' live
judges and in the cloud's tally. A model's gauge that has one value a run (the Linux host's pod start wait and its 95th percentile)
has no interval, so it is shown, not judged, with the way it moved and its size. And the line says which engines the tables stand
on, so a reader never takes a table of an older engine for the engine that stands.

### 3.3 The sides are never a reading

Blue does not mean good and amber does not mean bad: they name who is being read.
Where the two sides look the same, they are the same, and that is EVEN. Where Omni-Compass's blue line sits closer to a
muscle's line than native's amber one, that is the max at work: every muscle to its own limit, never past it, and the
capacity it holds there is power given, shown beside the work and the speed it bought.

![Flowchart: how a gauge's number becomes a word. The gauge's declared aim is read first: time waited, missed or failed, where a fall is GAIN; work done, where a rise is GAIN; a resource spent or held, where a fall is a cut (GAIN) and a rise is power given. Then the paired change and its 95% interval: an interval that includes zero reads EVEN; clear of zero, the word follows the aim. Three runs A, B and C: GAIN or LOSS only when all three point the same way with every interval clear of zero; EVEN when any interval includes zero; the runs disagree when clear runs point different ways. The page draws exactly this rule, as tools/readings.py writes it.](book/figures/f_reading.svg)

### 3.4 The marks

A kill-switch window is shaded red across every time axis. A monitor on screen now carries an accent
border on its tile. A tile with no reading says what it shows (a count, a state, an age) and carries no colour of a word. A
row shown and not judged (the knob's own setting, the governor's own commands, Omni-Compass's own processor time) is grey and
counted in no total. A ring that opens and fades at the head of a line is the decision that has just landed on it, and the small
box beside the head prints that line's newest value, as a quote board prints the last price. A box drawn round a row, a cell or a
bar of a record monitor is its reading cursor: it walks the record one row for each decision of the live engine, and the row it
holds is named under the monitor; the record itself changes only when GitHub's next run rebuilds the page. An age printed
beside a reading of GitHub ("read 06:16 UTC, 41 min 07 s ago") counts up every second.

---

# PART II. THE WALL AND THE SWITCH

## 4. The Monitor Wall

### 4.0 The numbered monitors and the control panel

Every monitor of the page (every chart canvas) carries its number in a badge above it, counted in its order of
appearance from 1 at the top of the page to the last at the bottom; the page's section 1b shows them all at once on the
monitor wall, numbered, read left to right and then down, as any page is read (the founder's order of 21 October), and a click
on a tile scrolls to the monitor it copies. Two monitors that sit side by side in their section, native beside Omni-Compass,
sit side by side on the wall too: a pair never splits across two rows, on the wall or on the page at any width. Each section names its monitors in the engine table of contents, and each
badge names its section, so a monitor and its section read each other both ways. Under every monitor a strip carries its
knobs: the kill switch, the console's knobs where the monitor is live, and its own buttons where it replays. The monitor
list beside the wall (the page's section 1c, `#s-monlist`) gives every monitor by its number, what it shows, its section, each monitor's evidence class, its state (live, replay, record, model or awaiting its run), the
open-source exporter and series that would carry it on a running system, and, where it waits, the run that fills it; the
whole wall is also a Grafana dashboard (`deploy/grafana/omni-compass-wall.json`), its panels numbered as the page numbers its
monitors and laid out left to right, each under a row for the page's section that holds it, each carrying its wiring. The control panel (the page's section 1a, `#s-health`)
holds the kill switch, the button that runs the Python's own seeded runs in the page (they also run on their own as the page
opens), the three manuals and the wall's dashboard. The proof monitor (the page's section 1f, `#s-proof`) reads every run three ways: the
Python's set as GitHub ran it (`tools/engine_runs.py`, its run linked), the same draws through the C++ harness on the engine's
C++ twins (`cpp/tools/engine_runs.cpp`), and this page's own port, one SHA-256 digest each beside the digest of the draws
themselves; the three must be one. Once that first check ends, the page checks the set again without end: one run at a time,
about twice a second, each run recomputed from its own seed by the page's engine and held against the Python's receipt; the run
being checked is boxed on all three lanes and its result printed under the digests. Appendix L lists every monitor under its number.

**Every monitor's wiring.** Under every monitor one line names its wiring (`docs/engine/monitors.json`): the page's own code, the
Python it ports or reads, the C++ twin or why there is none, the checks that hold them equal, each file linked at the build's
commit, and how it moves; the monitor list carries the same. A live monitor runs the page's port of the engine, held equal to the
Python by `docs/engine/check_live_engine.py` and the Python to its C++ twins by the parity tests; a replay plays a record the Python
wrote, held equal to its source by `docs/engine/check_records.py`; a record reads a measured table as written, so no C++ applies.

**The motion meter.** The page watches itself as the viewer sees it. Every monitor in view is photographed small once a second;
one whose picture changed in the last three seconds reads **● moving** on its badge and in its row of the list, one in view for
three seconds without a change reads **● still** (and says so when the engine is paused). A monitor off screen rests, as the page's
own governor rests it (chapter 25), and its row keeps what it did when it was last in view; the note under the list counts the
monitors seen so far and how many of them moved. Scroll the page once from top to bottom and every row reads what its monitor does.

### 4.1 What the wall is

The wall (the page's section 1b, `#s-wall`) is every monitor of the page in one view: the same
canvases the sections draw, copied small four times a second, so nothing is drawn twice from different data. Every tile
carries at its top its number and its title in capital letters, what the monitor shows, and under them its section and its state (live, replay,
from the records, a model, or awaiting its run), so a tile says where its monitor is and what it represents before it is
opened. Click a tile and the page scrolls to the monitor it copies. The page's own governor (the page's section 11, chapter 25) leaves a monitor resting while it is
off screen; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to, and while the wall
is in view the resting monitors are drawn in turn, one a frame, each by its own drawing code; a tile with the accent border is
a monitor on screen now.

### 4.2 The order of the board

The board is laid out the way an operations monitor is. The switch and the engine come first.
Next come the live organism's signals, native beside Omni-Compass, in the four a service is watched by (latency, traffic,
errors and saturation in site-reliability practice): here the work waiting, the work done, the decisions past their line and
the capacity held. Then every reading of the real and modelled runs that went against native, worst first. Last come GitHub
(the runs in progress and queued) and the age of this page. A tile's word is its reading against native by the key; a tile
with no reading says what it shows.

### 4.3 Reading a signal tile

Each signal tile holds the last 120 decisions of both sides, native solid amber and
Omni-Compass blue, each side's value now, and the running paired reading in the tables' words. With the master switch OFF the
decisions are shaded red and Omni-Compass's side follows native: its value equals native's and its line is drawn in native's
colour, dashed on top of native's, so both stay in view.

| Signal | What it is | Its aim | A GAIN reads |
|---|---|---|---|
| The work waiting | the queue in front of the muscles: requests, jobs or pods not yet served | time waited: lower | the blue line under the amber one |
| The work done | the requests served, the jobs finished, the work inside the line | work done: higher | the blue line over the amber one |
| The decisions past their line | the share of decisions where a muscle's reading stood past its line (a miss) | missed: lower | the blue line under the amber one |
| The capacity held | the machines, replicas or clock a side holds in service | a resource held: a fall is a cut, a rise is power given | either way is shown beside the three above; a rise that bought nothing is a cost to find |

### 4.4 Reading an alarm tile

An alarm tile is a judged row of a real or modelled run that read LOSS, or a run on the engine
that stands that terminated without a measurement. It names its gauge, its size with the word's sign, the table or run it
came from, and the repository's root-cause document where one exists (`docs/POD_START_WAIT.md`, `docs/TAIL_LATENCY.md`, and
the others). The alarms are ordered worst first by their size. Chapter 28 is what to do with one.

### 4.5 The age of the page

The last tile. It counts from the build's time, printed in the title block, to now on the
viewer's clock. A page older than three hours and a few minutes means the rebuild did not run or did not land (chapter 7); the
records on it are still true for the build they name.

## 5. The Master Switch

### 5.1 One switch for the whole organism

The master switch (the page's section 1e, `#s-master`; its kill switch heads the page's section 1a) is wired at the top of the
organism: switch, brain, organism, every muscle, as the repository builds it (`omnicompass/master.py`,
`tools/omni_switch.py`). It holds the brain's outputs. Every governor on the page is registered with it and obeys it at once;
on a real machine every governor exits at the switch.

### 5.2 The three states and their colours

| State | Colour | What it means on the page | What it means on a real machine |
|---|---|---|---|
| ON | green | the brain's outputs reach every muscle; every monitor shows Omni-Compass acting on top of native | the governors run; every write read back; the lease renewed each beat |
| Kill switch engaged | red | every lever handed to native at once; the decisions shaded red on every time axis; the event log records the engagement and its clearing | `python3 tools/omni_switch.py off`: every governor hands back and exits, and none starts again until `on` |
| OFF | white | the brain keeps reading the native body in shadow, so its monitors keep moving, and nothing it computes leaves it; every Omni-Compass side follows native, drawn in native's colour, dashed | the governor in watch mode writes nothing (the Operator's Manual, level 1); off, it is not running |

No monitor is switched off by the switch. That is deliberate: the operator sees what the brain would do while it does nothing,
which is the watch level of every installation.

### 5.3 The table under the switch

Governor on this page; where it lives (the module, the section); its state; what it does
at the switch. Every governor the page runs (the stress-test model's, the harness's, the live controller's replay, the page's
own render governor) is a row, so there is no governor on the page that the switch does not reach.

![State machine: the governor's modes. OFF is native alone; WATCHING reads and logs and writes nothing; AUTOPILOT pushes, lifts off and idles; CRUISE holds every machine in service while a known queue waits; RESET hands every setting back and reads it back. The kill switch leaves every mode for OFF at once; the lease walks a crashed governor's settings back to native. On the page the switch's three states are ON (green), the kill switch engaged (red) and OFF (white, the brain reading in shadow).](book/figures/g_modes.svg)

### 5.4 What a kill-switch window looks like

Press the kill switch on the console (chapter 18) and every time axis on the
page shades the window red from the press to its clearing. Inside it, Omni-Compass's lines fall onto native's; the governor's
ticker (the page's section 5c) is empty, for nothing decides on top of native; the phase plane's right-hand dots take the left-hand
positions. When the window clears, the lines part again where the governor's first decision lands.

## 6. The Alarms, the Feed, the Event Log and the Metrics

### 6.1 Alarms and watch items, by severity

The alarms table under the wall lists every reading that went against native and
every open item (a run that ended without a measurement, a slot not yet run), graded ALERT, WARN and INFO as an operations
log grades them, each with its item, its reading, its source and the repository's record. Filter by the three grades with the
buttons at its head. An ALERT is a judged LOSS in a three-run table on the engine that stands; a WARN is a LOSS in one run of
a table not yet complete, or a run that stopped before a result; INFO is a watch item.

### 6.2 The golden-signal feed

One point per decision streamed from the live engine, gapless, the last 240 decisions, each
signal on its own axis, with each side's last, mean and maximum as a time-series dashboard reports them; a kill-switch window
shaded red; native in amber, Omni-Compass in blue, the same demand on both. The feed is the four signals of the wall at full
size and full history.

### 6.3 The event log

The live engine's own events as it emits them, newest first, with the wall-clock time and the
decision: a threshold breach and its clearing on either side, every injected fault and its end, the kill switch, the dial, a
new day, and the brain's calm crossing the grant threshold. The log is what an operator reads to answer "what happened at
02:14": the decision number ties it to every other monitor.

### 6.4 The OpenMetrics exposition

The live engine's metrics in the OpenMetrics text format, the exposition format
Prometheus scrapes and Grafana charts, refreshed every two seconds. They are: engagement (the switch), the decision index,
breaches, work, band time, actuator moves and reversals per side, and frame time; then the verdict's keep ratio at each true
cost (chapter 22), the three-run tables' rows by class and reading, and the build's engine, digest and commit. *Copy the
exposition* puts the text on the clipboard, so the page's own metrics can be pasted into a scrape target and charted beside
the stack's.

## 7. The Pipeline That Rebuilds the Page

### 7.1 When the page is rebuilt

GitHub rebuilds the page (`.github/workflows/live-engine.yml`,
`docs/engine/build_live_engine.py`) whenever the engine, a model or a result changes, and every three hours. Every record is
made again by the repository's own code on the engine that stands, checked against the Python and the C++, and committed.
The page's own file is outside its own push filter, so a rebuild never starts another rebuild; a front-page run that did not
succeed starts no rebuild (`tests/test_workflow_triggers.py` holds both).

### 7.2 The CI pipeline monitor (the page's section 1i, `#s-github`)

Every workflow run in progress or queued at the build, as GitHub's
own list at that moment, and the first of them in each state. The hardware and cloud runs, with their terminal status, are in
the page's sections 5a and 5f; every run on the engine that stands that terminated without a measurement is raised on the status board.

### 7.3 Reading the pipeline against the conductor

The conductor (`scripts/dispatch_grid.py`, every 15 minutes) starts
every run of the campaign on the engine that stands, A of every benchmark, then B, then C, a few a tick, and never starts one
twice; it starts nothing while an Azure run, a grid report or a verify waits for a runner. So a pipeline monitor showing one
Azure run queued and nothing else starting is the conductor holding, by its rule, not a fault. A long run on a free runner
(the organisms at 1,000 copies) lists as in progress for its whole shard.

---

# PART III. THE MEASURED EFFECT AND THE WHOLE

## 8. The Benefit Board, the Grid and the Catalog

### 8.1 The benefit board (the page's section 2, `#s-board`)

Every domain, native against Omni-Compass, as the repository's benefit sheet
holds it (`results/BENEFIT_SHEET.json`, `docs/BENEFIT_SHEET.md`): the domain, the benchmark, its evidence class, its engine,
its benefit (one number and one word), its GAIN rows, power given, EVEN and LOSS counts, and where it stands (landed, running,
queued, not yet run). Each bar and square carries its own word; the size beside the word never carries a sign of its own.

### 8.2 Where the benefit lives, gauge by gauge

Every judged row of every newest three-run table, sorted into the family of
gauge it measures. A CTO reads speed, the service level, failures and work. A CFO reads machines, energy and the bill. A plant
engineer reads peaks and swings, wear and accuracy, and misses. Each bar counts the rows that read GAIN in all three runs; the
size beside it is the median of those rows' own sizes; the largest is printed beside the median; power given and LOSS rows are
counted beside them, and the runs that disagree or differ are listed, not counted.

### 8.2a The trading floor: the market map and the quote board

Every three-run table on the page, read the way a trading floor reads its market (the founder's order of 21 October). The
market map is a squarified treemap: one tile a table, grouped by stack, its area the number of gauges the table judged and its
colour its reading: green GAIN, deeper the larger the share of its rows that read GAIN; red wherever any row reads LOSS; yellow
EVEN; the accent where it gave power; grey with a dashed edge a table of an orchestrator's own cost, with no Omni-Compass in
either arm. A reading cursor walks the map one table every one and a half seconds and names it under the map. The quote board
gives every table a quote: its ticker (the table's file) and engine, the gauge that moved most with its mean change across
the three runs, and that gauge in runs A, B and C as a candle: the vertical bar is the run's 95% interval, the tick its value,
the line the zero of no change. The strip under each quote counts the table's rows by word, and a tape runs every headline
across the top. Pointing at a tile or a quote shows its record: the table's title, engine, counts, the headline gauge in each
run and the file. Every figure is the table's own; nothing is typed in.

### 8.3 Aggregate: one figure for the whole board

The Omni index (`results/OMNI_INDEX.md`): the geometric mean of the
ratios of every measure that enters, where a measure enters only as its three-run reading allows (GAIN, LOSS or power given
in all three runs counts; EVEN counts as exactly 1, so nothing inside the noise is claimed either way). Each test is read
from its own newest three-run table, no table is pooled across engines, and every row names its table. The index is one
number for the board; its row of factors under it is the board's own audit.

![The three-run rule. A benchmark runs three times, A, B and C, on one engine version, each a paired run of native against Omni-Compass. A row reads GAIN or LOSS in all three of our runs only when the three agree in sign with every 95% interval clear of zero; EVEN, no difference beyond the noise, when an interval includes zero; the runs disagree when clear runs point different ways. The board and the index count by this rule and no other.](book/figures/readings.svg)

### 8.4 Third-party software still to be benchmarked

The register's slots, in order (`docs/REGISTER.md`): every muscle in
them already runs, modelled, in the 1,107-muscle catalog and the seven organisms, native and with Omni-Compass on top; a slot is
the same test on the outside world's own software, each queued until its three runs land. A slot shows its status in the
register's own words, what is measured (the lines of its preregistration) and the known limits said before the result.

### 8.5 The scale-out grid

Seven organisms × 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs: modelled (the misses)
and with the real cluster inside (the 95th percentile), both values shown in every square. The 1,000 tier runs on GitHub's free
runners only; paid machines stay at 100. Two buttons choose *the engine that stands: its runs as they land* or *the road: the
newest grid with its squares landed*. A square not yet landed says so; a square beyond a free runner's memory or time is listed
as pending runner capacity, never rented. The grid's monitor draws the engine that stands' own campaign as GitHub runs it: each
square filled by its runs started (pale) and measured (solid), as GitHub was read at the build, with the age of that reading in
its heading; the reading cursor walks every started square and names it under the grid. Once the grid's receipt is written, each
square takes its word. The road draws the newest grid with its squares landed, under its own engine's name, never read across.

### 8.6 Every three-run table

Every three-run table in the repository, native against Omni-Compass, every row as written,
each benchmark's newest engine's table; open a row to read every judged row that is not EVEN. The table's own rule is printed
with it; rows shown and not judged are left out of the counts; a tuning case is shown and never counted.

### 8.7 Every muscle and the seven organisms

From `results/realms_v5/REALMS_V5.json`, the realms runner at the max, its
engine and commit named above it (`tools/run_realms_v5.py`, catalog `realms/catalog_v5.csv`), ten paired seeds per muscle and
per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A
muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none
moving the other way; EVEN at its limit on native when its knob already sits at the top of its range; EVEN, the same as
native, when it wrote and nothing moved beyond the noise. Energy is power given where it rose. The seven organisms are listed
spine first, then the four realms, the four stacked and the whole tower, each under its own load, the climb and the work
waiting in line (the three buttons). Evidence class S: a model's energy is not a meter's.

### 8.8 Every family, by stack

Each muscle alone, native and then with Omni-Compass on top, grouped by the family of its
knob and the stack it lives on; *Find a muscle* searches the 1,107 by name. A family reads GAIN when more of its rows read
GAIN than LOSS; the row of a muscle at its limit on native is counted as EVEN.

---

## 9. The Whole Organism, Every Way It Is Bought

### 9.1 Every way a stack is bought

Omni-Compass is wired into every piece of a stack through its own two-way plug: the
software (the cluster, its add-ons, its governors and orchestrators, and the services on it: the pools, the consumers, the
caches), the bare metal under it (the chip's power limit and clock; the machine's kernel and its own meter) and, where the stack
is rented, the cloud that bills the machines. The whole-organism monitor (the page's section 3, `#s-whole`) has a button for each
way a stack is bought: *on-site bare metal*, the software on the owner's own bare metal (software × bare metal, no cloud);
*through the cloud*, the cloud's build, its bare metal at the back end and the software (cloud × bare metal × software), with
the cloud as two pieces beside it; *in the device*, the bare metal alone, for one who buys the chip or the machine and no
software stack on it; and *as a service*, the software alone, for one who runs it on machines someone else meters. The
founder's question of 20 October, which this monitor answers: the cloud is a piece of the stack, bought and billed, and what
Omni-Compass does there composes with what it does on every piece beneath it.

A tenant cannot meter the provider's bare metal at the back of a cloud: the cloud's piece is the bill and the machines the
provider meters, and the bare-metal piece is gauged on hardware the repository meters and carried to the provider's only as a
modelled factor, said so on the monitor (`DISCLOSURES.md`, section 9). A piece with no measured run yet is named and left out
of the whole, never filled with a guess.

### 9.2 The stack, drawn

The stack, native beside Omni-Compass, with the work flowing down through the pieces: the service,
the cluster, the governors, the machines, the chip, and, through the cloud, the provider's bill. The dots move at the live
engine's demand; the picture is of the flow, not a measurement; each piece's measured factor replaces the picture's weight
the moment its three runs land.

### 9.3 The collective synopsis

The benefits, gauge by gauge, added together over every measured piece: work (more), speed (a
shorter 95th percentile), machines (fewer), energy (less), the bill (smaller), and the one number, the index over the gauges.
Two readings are offered by the buttons: *every measured piece, every interval carried* (every factor with its own 95%
interval, the whole their product) and *the strict reading: the index's rule* (only a factor that reads GAIN or power given in
all three of its runs counts; EVEN counts as exactly 1). A third pair of buttons says what to do with a governor that replaces
a native controller: *its one run beside the count* or *its one run in the count*.

### 9.4 The composition

Piece by piece and layer by layer: each factor with its 95% interval, the whole their product. Read
the table left to right: the piece and its layer, the five gauges, the index, and the receipt (the table's own row) each factor
is read from. A factor's interval that includes 1 is EVEN and multiplies the whole by exactly 1 in the strict reading.

### 9.5 Bills and receipts

What native spent (the cost; runs A, B and C), what Omni-Compass spent (the expense; A, B and
C), and the benefit (pooled, with its 95% interval), in the units each receipt bills in: machine-hours, dollars at list price,
watt-hours of the declared model, the meter's watt-hours where a meter exists. The cost is native's, the expense is
Omni-Compass's, and the benefit is their difference read by the key: a smaller bill is GAIN, a larger one is power given,
shown beside the work it bought.

### 9.6 Beyond the count

The governors' tables on this page, the models beside them, the separability test (whether the
pieces' factors may be multiplied: the factors are independent where each piece's run holds every other piece at native), and
where the missing pieces are: every slot not yet measured is named, and the whole is read without it rather than with a guess
in its place.

# PART IV. EVIDENCE BY STACK

## 10. The Clouds

### 10.1 One metric: the bill

In a cloud Omni-Compass shows one thing: the same work as native for a smaller bill, never a
bigger one. Every cloud set runs Omni-Compass at the tune-down on the machines alone (`OMNI_MACHINES_ONLY=1`,
`--give-back-only`): no pod autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's. It parks
only a machine the cloud already made, after its own trial, and wakes it on a breach. The bill and the machines aim lower;
work, speed and failures must read EVEN or GAIN. Azure runs first and is the measure of the other two (Google Cloud, Amazon
Web Services): the same tuning, mechanism and harness.

### 10.2 The monitor (the page's section 5a, `#s-cloud`)

Each provider's four sets (the steady set, the bursts `1 4 1 6 1 9` and
`1 6 1 8 1 6`, the real day of Google 2011 on 1 to 9) and their status: measured to the end (engine, run, started), stopped
before a result, or now. Then every cloud run GitHub has started, set by set; the bill on Azure run by run (machine-hours
billed native · Omni-Compass; the bill; the 95th percentile; the failed requests), each with the engine it ran on; and the
shipped controller in the cloud setting, live: native's machines against Omni-Compass's on the repository's toy cluster (class
S), the cloud's own autoscaler running in both arms, its run and speed following the console's clock. Until a provider's
first set lands, its bill monitor shows the same mechanism live: the machines billed (in service and booting) of native and of
Omni-Compass on the cloud setting's model, decision by decision, marked class S and never that cloud's bill, which arrives with
its first set; under it, the provider's newest check in its own words.

### 10.3 The stopping rule

From 19 October every Azure set runs up to 100 paired repetitions a run, the paid cap, under the
preregistered stopping rule (`tools/stop_rule.py`). After 10, 20, 40 and 70 repetitions the bill's change is read with its
99% interval. The run stops once the bill is read (GAIN, power given, or EVEN within ±2% of native's bill), and never while the
speed or the failed requests read a LOSS. Those runs carry "to the cap, stopping rule" in their title and count as their own
A, B and C. So a cloud set that has run for a day and a half and shows no result on the board is not a fault: its bill has not
yet been read at a look, and `peek` (`.github/workflows/peek.yml`) prints its finished repetitions, paired, while it runs.

### 10.4 Reading a cloud receipt

The rows an operator reads first: machines billed (machine-hours) and the compute bill at
list price, both aiming lower; then the response time's mean, 95th and 99th percentiles, the time over the line, the failed
requests and the alert minutes, all aiming lower and all required EVEN or GAIN; then the rows shown and not judged: the
settings commands the governor wrote on its own (native is 0), the share of its additions decided inside the line, Omni-Compass's
own processor time. A bill row whose interval includes zero is EVEN so far and the run goes on to its next look.

### 10.5 When a cloud is not ready

The conductor starts a cloud's set only after that cloud's newest check passed
(`.github/workflows/cloud-check.yml`, `tools/cloud_key_check.py`: the key whole, the login, the plan, the machine type,
every quota), at no cost. The monitor shows a failed check as the cloud's status, in the check's own words: a Google key stored
cut short (the stored secret shorter than a whole key file) is stored again whole (`docs/GOOGLE_SETUP.md`, section 4); an Amazon
account on the Free plan, whose organization policy denies every machine read, is moved to the Paid plan
(`docs/AMAZON_SETUP.md`, section 1a). Nothing is built and nothing is billed until the check passes.

## 11. The Orchestrators and Governors

### 11.1 What they are

The governors and orchestrators that sit between the work and the cluster: batch schedulers and job
queues (Kueue, Volcano, the KAI scheduler, Armada), multi-cluster governors (Karmada, Open Cluster Management), the default
Kubernetes scheduler and its bin-packing profile, the co-location and rightsizing controllers (Koordinator, Crane, CruiseKube,
Goldilocks), the GPU and edge orchestrators (KubeRay, KubeEdge, Nephio) and Gödel. Each runs live on real Kubernetes as its
project ships it, native and with Omni-Compass on top of it; Omni-Compass never replaces the orchestrator.

### 11.2 The monitor (the page's section 5b, `#s-orch`)

The road to a result, every governor at once: its register row, its
preregistration, its rig on GitHub, runs A, B and C, and its three-run table as it lands. The orchestration stack, live:
Omni-Compass on top, the governor native as shipped, Kubernetes and its nodes beneath, the work dots moving at the live
engine's demand (a picture of the flow, not a measurement, replaced by the governor's readings the moment its three runs
land). The catalog of governors: what each governs, native as shipped, Omni-Compass on top, and what the repository holds
today. Click a governor (a tile, a row of the road or of the catalog) to hold it in every view.

### 11.3 The four ways

The founder's order of 20 October: each governor runs with the organism alone (nativebare), the
orchestrator as shipped (native), Omni-Compass on top of the organism alone (compassbare) and Omni-Compass on top of the
orchestrator (compass), all four in every repetition, each comparison paired within it and read by the one key
(`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6). On the organism alone Omni-Compass sits on top of Kubernetes' own
scheduler. The monitor shows the four as four columns of one table per governor; the comparisons an operator reads first are
native against compass (what Omni-Compass adds on top of the orchestrator) and nativebare against compassbare (what it adds
with no orchestrator at all). In the official-run playback (the page's section 5c) each of a governor's five tables plays its own
two arms of the run's repetitions, named on the lanes, the candles, the heat map and the repetition's table by the table's own
words, the left lane its reference and the right lane its candidate; Omni-Compass's colour is drawn only on an arm that carries
Omni-Compass, so the orchestrator's own cost (the orchestrator as shipped against the organism alone) plays in native's colours on
both lanes.

### 11.4 The orchestra

The eighth organism: every governor's catalog muscles, each governor's a body of its own and all of
them together one body, native and with Omni-Compass on top (modelled, class S; `tools/run_orchestra.py`,
`results/orchestra/ORCHESTRA.md`). It is a grouping of catalog rows like the seven, never an engine file.

## 12. Kubernetes: the Official Run Playback

### 12.1 What plays (the page's section 5c, `#s-ops`)

A real-time operations dashboard over the benchmark runs themselves (class L),
not a model. Every series streams half minute by half minute out of the raw files GitHub archived, each file's SHA-256 matched
before a byte is drawn: native (the whole cluster with everything it ships with) against Omni-Compass, the same load, the
same second. Pick a benchmark, a run (A, B or C) and a repetition at the head of the section; the tiles, the candles, the
heatmap, the bars and the two tickers all move together with the page's section 5d. The data pipeline is its own monitor:
every stage from the GitHub Actions run to the page (the run, the raw files archived, the SHA-256 check, the official scorer,
the three-run tables, the build, the page) drawn whole, the stage being read lit and the data moving between them. Under the
receipt the page holds its own scoring of every repetition against the run's own scored summary (`LIVE_REPS.json`) and prints
the largest relative difference: at machine precision (about 1e-16) for every run, the governors that run a group of two
clusters included, whose every file the scorer reads at its own place in the repetition's folder.

### 12.2 The heart

A supervisory governor is only alive while its loop turns: once every decision it reads the whole body,
decides, writes, and proves it is still there. That turn is the heart. Each beat pumps every reading in through the plug and
the decision out (`omni_controller/controller.py`, its main loop) and renews the governor's lease (`master.heartbeat()`,
`omnicompass/master.py`). If the heart stops, its process gone or its lease older than its limit (the larger of 120 s and five
beats), the watchdog (`tools/omni_switch.py watchdog`) walks every setting back to native: a stopped heart leaves the body
exactly as native runs it. Native has no heart of its own: each of its controllers keeps its own clock, the pod autoscaler
one sync every 15 s, and nothing proves any of them is still there.

![Timing diagram: the lease. The governor renews its lease on every beat; the watchdog reads the lease on its own clock. When the governor dies without handing back, the lease ages past its limit (the larger of 120 s and five beats) and the watchdog walks every setting back to native, a step at a time, reading each back. On the page, the heart monitor shows the beat and how close the lease came to its limit; a stopped heart leaves the body exactly as native runs it.](book/figures/t_lease.svg)

### 12.3 A healthy heart, never pushed

The beat runs at a fixed, calm rate (one decision a minute in these runs, the fast
checks every 5 s between beats) and is never driven faster by the load it governs. What it costs is counted inside the body's
own load (the row *Omni's own CPU*), so the organism never pays for its brain without knowing it. A decision that fails is
recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal
time. Two gauges read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page
calls a heart under strain when a decision takes more than half its beat, or a gap between beats runs past half the lease.

### 12.4 The three charts

Response time, one candlestick per 30-second bin (open, high, low, close of the responses in the
bin), native beside Omni-Compass; the latency heatmap, every response binned by time and by duration, the darker the fuller;
throughput, requests served per 30-second bin. Read the three together: a GAIN in the 99th percentile shows as the candles'
upper wicks shortening on the blue side while the heatmap's upper band thins and the throughput bars stand level or higher.

### 12.5 The governor's ticker

From the repetition's own `audit.jsonl`: the minute and second of the decision, the compass
position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward
native). Then the machines it recommends, and the give-back verdict's state: *left native* means every setting stays
native's; *acting* means a trial on its own measurement. Every line of the ticker is a line of the governor's audit, and the
audit is the record of authority for what it did.

### 12.6 Native's own controllers' ticker

Native has no governor; its own controllers' moves are the second ticker, read
from the native arm's `capture.csv`: the replicas its pod autoscaler holds, the pods waiting for a place and the machines
ready, every change in the same repetition, newest first. With Omni-Compass OFF the first ticker is empty, for nothing
decides on top of native. The two tickers side by side are the mechanism of action in its plainest form (chapter 26).

![One pedal, no brake. Pushing the pedal adds capacity at once; lifting it eases capacity back toward native a step at a time, never below idle, the floor of two machines. Cruise holds every machine in service while a known queue waits. Watching reads and writes nothing. On the governor's ticker, push and lift are the force column, and the machines recommended are what the pedal bought or handed back.](book/figures/pedal.svg)

### 12.7 Every repetition side by side, and the run's receipt

Each repetition of the run as one small pair of lines; the
receipt of this run as the repository wrote it; and this repetition scored by the repository's own scorer, which must equal
the run's own summary over its repetitions (the count of matches is printed). Benchmark status, by block: landed, running,
queued, or not yet run, for every Kubernetes benchmark of the campaign.

## 13. Kubernetes: Per-Repetition Telemetry

### 13.1 What it is (the page's section 5d, `#s-runs`)

The benchmark runs themselves at one-second resolution: each three-run table's
runs A, B and C read back from the raw files GitHub archived (`results/live/raw`, on the `raw` branch), native and
Omni-Compass, repetition by repetition, played second by second. Every file the page reads has its SHA-256 computed and
matched against the run's own `SHA256SUMS_ALL.txt`, and every Kubernetes repetition is scored by `tools/live_reps.py`;
where a run holds its own scored summary, the scorer's mean over its repetitions equals it. Class L: real Kubernetes on kind,
real databases and a real broker.

### 13.2 How to use it

Choose the benchmark, the run and the repetition; the page's section 5c dashboard follows. Read a gauge's
two lines against each other for the whole repetition, then read the receipt of the run under it: the receipt's word is the
reading; the lines are why. A repetition whose job failed and ran again is marked; one that failed three times is listed and
left out.

## 14. The Shipped Controller's Decision Trace

### 14.1 The one place the brain drives the muscles decision by decision (the page's section 5e, `#s-live`)

The shipped controller,
`omni_controller/controller.py`, on the toy cluster of `pilot/selfpilot.py`, wired as the repository wires it. Each decision
runs the chain left to right: the senses, the six-state brain, the nerves and the machine organ's grant, the compass law on
the service (the cloud setting), the verdict's trial, the release gate, the plug. Every value below the chain is the
controller's own audit record of that decision, recorded by `docs/engine/export_controller_trace.py` on runs A, B and C (six
hours each, a decision every 15 s, the controller's own default on omni-v14; class S). Three buttons choose the setting: *on top of the HPA, the max*; *the cloud: the
tune-down, machines only*; and the Linux host and the card (the page's section 5f).

![One decision of the governor. Read the body (the senses), place every reading in its band, let the brain's state evolve, grant or refuse through the nerves, apply the compass law to each muscle (push or lift), run the verdict's trial on a step past native, pass the release gate, write through the plug and read it back, renew the lease. On the decision-trace monitor each box is one column of the audit, and *open the same controller, decision by decision* steps through them.](book/figures/loop.svg)

### 14.2 Reading the trace

The columns, in the audit's order: the stress E, the utility U, the calm, κ, h, σ, ν (the four
scalars of the nerves), the gate and whether it passed, whether machines were in service (a blind reading holds the
decision), the recommendation, the machines seen, the density ρ, the compass position and velocity, the force, the verdict's
word, the writes, the queue, and the law that decided. A row whose gate did not pass wrote nothing; a row whose verdict reads
LOSS kept the setting at native; a row with a write names the lever and the value read back.

### 14.3 The paired change

Per 15-second tick, averaged over ten-minute blocks, with its 95% interval (Student's t) in each
run; GAIN or LOSS only when all three runs point the same way with every interval clear of zero. Machines and power: a fall
is a cut, a GAIN; a rise is power given. Our own models (class S): a model's small numbers are the model's.

## 15. The Chip and the Host

### 15.1 The highest-value point (the page's section 5f, `#s-stacks`)

The silicon itself, the chip at the far end of every stack: there
the max rides each card's own limit, and every watt it takes is power given, shown beside the work it buys. The monitor holds
the slots for the metered GPU and CPU runs (class P: the card's own meter on Lambda; the package's own energy counter,
`tools/run_cpu_power.py`), every hardware run GitHub has started, newest first, and then the models of one GPU card and one
Linux host (class S), native beside Omni-Compass, each run twice on the same load and seed, native first.

### 15.2 The settings

Buttons choose the stack (a GPU card; Linux, one host; Kubernetes, the page's section 5e; the cloud, the page's section 5a),
the load on the card (AI token generation; compute-bound) and the card's power setting (the card as shipped, 150 W; an
operator's cap, 105 W). The table under them, *where the mechanism moves on the chip models*, lists every setting with three
runs each: the seconds held off native, the writes, the power (W) or the host's busy share native · Omni-Compass, and the
response (ms) native · Omni-Compass. Click a setting to play it.

### 15.2a The 8-card node, built and awaiting its run

Under the settings, a node of eight NVIDIA cards stands built before its run (`scripts/gpu_8card.sh`,
`docs/GPU_RUN_GUIDE.md`, section D): eight card slots, each native lane drawn from the repository's one-card model (class S, the
same model on every card until the run, never eight measurements), each Omni-Compass lane empty and marked awaiting its run.
Nothing on it is invented: on a running node the same panel reads the NVIDIA DCGM exporter's series card by card, and the
8-card run fills it when it lands.

### 15.3 Reading a row with nothing held off native

A row with no second held off native is Omni-Compass deciding to stay
native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native. That row is the
engine's own rule at work and is not a fault. The slots marked not yet run are written as the repository holds them and fill
in, played back from their raw files like every Kubernetes run, the moment their three runs land.

---

# PART V. THE ORGANISM LIVE AND THE CONSOLE

## 16. The Organism, Live

### 16.1 The two instances (the page's section 6a, `#s-engines`)

The system rendered as an organism: each node is a muscle (one
controlled actuator) and each ring its operating range. The left instance runs under its native controllers alone; the right
runs the same controllers with Omni-Compass's brain, nerves, heart and immune system supervising them. Three buttons choose
the body: *each muscle alone* (native, then on top, one at a time), *one organism* (the sixty muscles in one body) and the
*stress-test model* (the console's sixty muscles). Evidence class S: our own models, shown beside the real runs and never
presented as proof.

### 16.2 Reading a ring

A ring is a muscle's band drawn as a circle: calm at the inner edge, the line at the outer. The
muscle's live value is the ball on the ring; the reference, the knob at native, is marked. Under the max a muscle is moved only
where it has room above native; a muscle already at its limit on native is left native by design and its ball sits where
native's does. The counters under each ring and the scoreboard (chapter 20) give both sides and the difference. Where the two
sides look the same, they are the same.

![The seven organisms. The spine (267 muscles, every muscle that sits in all four realms), the four realms (Compute/AI/Cloud, Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized), the four stacked, and the whole tower of 1,107 muscles in 70 families. The organism monitor plays one organism of sixty muscles and each muscle alone; the benefit board (chapter 9) carries all seven.](book/figures/organisms.svg)

### 16.3 The body scan

As a scan reads a living body organ by organ, this reads the system playing in the page's section 5c (the
benchmark, run and repetition chosen there), organ by organ, half minute by half minute, from its own SHA-256-checked files:
native beside Omni-Compass. Each organ names what it reads; where native has no such organ (the governor's heart, the nerves)
the cell says so.

### 16.4 The immune system, live

The immune system is Omni-Compass's; native runs on its own controllers. Every room and
every machine pool has a native twin: the same muscle under its own controller, on native's heat and load, the body's memory
of healthy. A room that stands warmer than its twin is inflamed. Where its own knob can cool it, it is cured on the spot.
Where it cannot, it sends the whole body a signal, its heat debt, like a cytokine calling for help, and the other muscles
answer: the machine pools give back what Omni-Compass added until the room stands no warmer than native's. The skeleton (the
bone: the power and cooling lines the whole body shares) grants nothing it cannot carry. A cooling setting is walked back,
never snapped. On the monitor an inflamed room is marked, its heat debt is a bar, and the pools' give-back is seen on their
rings.

### 16.5 The anatomy

Part by part, in the order of control: the brain first, the whole organism last. Each part names what
it reads, where it lives in the code, and its measure on this run.

## 17. The Telemetry Analytics and Omni-Compass in Its Own Words

### 17.1 The tensor (the page's section 6b, `#s-lab`)

The engine's own record is a tensor: two sides × every decision × sixty muscles,
each entry a muscle's compass position (0 calm, 0.5 the center of its band, 1 its line), recorded from `realms/harness.py`
(class S). It fills in decision by decision as the page's section 6a plays: the tensor, the difference matrix and the principal
motions replay that record on the live engine's clock, and no knob of the console changes them. Read it as a sheet of heat: a column (one decision) that is
light on the blue side and dark on the amber side is a body Omni-Compass held nearer calm at that moment.

### 17.2 The difference matrix and the principal motions

The difference between the sides, muscle by decision, with the
sign of the word; and the body's principal motions, the tensor's eigen-decomposition: the few patterns of movement that
account for most of the body's motion, each with the share of the variance it carries. The line across each bar is the
decision on screen: the share of that decision's own departure from the run's mean that lies in the mode. A first motion that is the whole body
rising and falling together is a body breathing with its demand; a motion that is one room against the rest is that room's
inflammation.

### 17.3 The service level and the error budget

The official runs (class L) read as a site-reliability engineer reads a
service: the service level this repetition, the error budget burned, and every gauge of this repetition against native, each
replaying the official run chosen in the page's section 5c.

### 17.4 Omni-Compass in its own words

Omni-Compass speaks for itself: every line is read from its own records at the moment
on screen (the official run playing in the page's section 5c, its governor's own audit, and the engine's harness on the console's clock)
and says what it is doing, beside what native does. *Speak aloud* reads it out on the viewer's own browser voice as the run
plays.

### 17.5 Ask Omni-Compass

Ask in your own words, or pick a question (what are you doing right now; where do you read LOSS,
and why; explain yourself to a buyer; show me your largest GAIN). Omni-Compass answers in the first person, for its own
mechanism and its own runs, reading only this page's records through six tools. The words are composed for it by Claude on
claude.ai, on the viewer's own account and with the viewer's permission; opened anywhere else, the rest of the page runs
whole without it. The answers are drawn from the page's records and are not reviewed by any outside party.

## 18. The Control Console

### 18.1 What the console is (the page's section 7, `#s-desk`)

Runtime parameter control and fault injection on the live engine: load
scaling, noise injection, sensor latency, capacity loss, a demand surge, a sensor blackout, a security hold, the dial, and
the kill switch. Every control is applied to both sides identically; the response is plotted per decision, native beside
Omni-Compass. The engine these knobs turn is the engine's own mathematics running in the page: the brain, the compass law and
the verdict, proven equal to the Python and the C++ on every build. It governs the stress-test model's sixty muscles, each on
top of its own native controller. The knobs move the live engine in the page's sections 6a and 8a to 8c, and the kill switch and the
frame load also move the page's own render governor (the page's section 11).

### 18.2 Do no harm, at the console

Every control acts on both sides alike; what Omni-Compass does with them is held by its
guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another on the engine
that stands, a give-back tried against native first and refused on a LOSS. Its one meaning is written once, in
`DISCLOSURES.md`, section 3, and the page's back matter carries it.

### 18.3 Every control

Appendix B lists each control in a table. In reading order:

| Control | Marked | What it does, on both sides |
|---|---|---|
| Demand (×) | LIVE | scales every muscle's demand from this decision on; ×1 is the day as written |
| Noise σ | LIVE | multiplies each muscle's demand every decision by 1 + σ·z, z a fresh normal draw, one draw per muscle shared by both sides |
| Sensor delay (+8 ms, +16 ms, as it is) | LIVE | adds decisions between what a muscle does and what its controller reads, on both sides: native's controllers and Omni-Compass's law read the same late number |
| Surge ×2 | LIVE, 40 decisions | doubles that body part's demand |
| Lose half its machines | LIVE, 40 decisions | halves a pool's capacity in service |
| A sense goes blind | LIVE, 40 decisions | forbids any hand-back (blind means hold) |
| Security hold | LIVE, 40 decisions | forbids any addition |
| Kill switch | LIVE | every lever to native at once; the window shaded red; the switch at the top of the wall reads red |
| Turn Omni-Compass OFF | LIVE | the brain reads in shadow; every Omni-Compass side follows native in native's colour |
| The dial: the max / tune-down | LIVE | the max: every muscle to its own limit, never below native; tune-down: never more than native, capacity handed back only with the organ's grant and the release gate |
| Pause, one decision, 1×, 4×, 16×, 60× | LIVE | the console's clock: a decision every 0.9 s at 1×; one decision steps once |
| The same day again, a new day | LIVE | replays the seed with the knobs as set; a new day draws a new seed |
| Every knob to its start | LIVE | returns demand, noise and delay to the day as written |

### 18.4 What a fault shows

Press *Surge ×2* and watch the page's section 8b: both sides' dots for that body part move up and right;
native's controllers each see their own reading one to three decisions late and add in the middle of their range; the
compass law pushes at the first decision the position leaves the center, so the blue dots turn back before the right edge
while amber ones cross it. Press *A sense goes blind* and the governor's hand-backs stop while its additions go on (blind means
hold, never a guess). Press *Security hold* and every addition stops while hand-backs go on. In every case the native side is
put through the same fault, so the difference is Omni-Compass alone.

---

# PART VI. THE BRAIN

## 19. One Control Cycle, Traced

### 19.1 What it shows (the page's section 8a, `#s-decision`)

One control cycle traced end to end at reduced speed: the sensed inputs,
the brain's decision, and the actuator (the muscle) it wrote. The max: every muscle to its own limit, never below native; the
capacity it holds is power given. The tune-down: never more than native, and a step back only with the organ's grant and the
release gate. In this model native already sits near its band, so the tune-down finds little to hand back; the scoreboard
(chapter 20) reads its runs A, B and C live when the dial is on the tune-down. Class S.

### 19.2 How to read it

Follow the particles: in along the wires from the muscles' meters to the inner arc of nine senses;
through the brain's six spokes; out through the nerves (the grant), the compass (the force) and the plug (the write). Each
stress on the console lasts 40 decisions from the moment it is pressed, and both sides meet the same demand, so a cycle
watched during a surge shows the push on the blue side and the native controllers' late, middle-of-the-range moves on the
amber one.

## 20. The Phase Plane and the Scoreboard

### 20.1 The plane (the page's section 8b, `#s-plane`)

A phase portrait, the picture control engineers use for a system's state. Across
is where each muscle sits in its band: p is 0 when calm, 0.5 at the center and 1 at its line. Up and down is how fast it
moves there (v, per decision). A muscle at rest sits on the middle line. One climbing toward its line moves up and right, and
past the right edge it is past its line. Native is on the left and Omni-Compass on the right: the same muscles at the same
instant, one dot each. In the stress-test model the shading on the right is the force the compass law would apply there: the
add force toward the line, the hand-back force toward calm. In the realms harness each muscle answers to its own rule, so no
single field is drawn.

![The compass band and the two forces. A reading is placed in its band, p = (r − lo)/(hi − lo), calm at 0, the center at ½, the line at 1, with 5% cushions at each end. Two antagonist forces act on the knob: the add force as the reading climbs toward the line, the hand-back force as it falls toward calm, combined as F = A·tanh((kₚ(p − ½) + k[d]·v)/A), smooth, never hammering. It fails up past 0.95 and never hands back while it climbs above the center. The phase plane's shading is this force at every point.](book/figures/band.svg)

### 20.2 The scoreboard

Each panel is one gauge of the live organism, read every decision on both sides, as an operations
dashboard shows it: native's value now and Omni-Compass's, the last 120 decisions of both (native solid amber, Omni-Compass
blue), and the running paired reading in the tables' words. With the master switch OFF the decisions are shaded red and
Omni-Compass's side follows native.

### 20.3 How each row is read

The paired change, native against Omni-Compass at the same decision, averaged over blocks of
ten decisions so neighbouring decisions do not count twice, with its 95% interval (Student's t over the blocks). *This run*: an
interval that includes zero reads EVEN; clear of zero, the word follows the gauge's aim (work: a rise is GAIN; misses, failed
work, waiting: a fall is GAIN; energy or capacity held: a rise is power given, a fall a cut). *Three runs*: GAIN or LOSS only
when all three runs point the same way with every interval clear of zero; EVEN when an interval includes zero; the runs disagree
when clear runs point different ways. The spread of positions can widen a little under the tune-down, because the calm
muscles it hands back move toward their line while the busy ones stay.

## 21. The Brain's Internal State

### 21.1 What is drawn (the page's section 8c, `#s-brain`)

The brain's six state variables rendered on their potential-energy
landscapes: a state resting at a minimum is stable; a state driven toward a maximum is under load. Each ball is a live value of
the engine's brain, integrated by the Runge–Kutta method every decision. In the stress-test model its push and target feed the
body's levers. In the harness views the harness arm acts muscle by muscle with no brain, so the brain drawn here is the page's
own, fed the harness's readings. Class S.

![The engine's six states. E the stress, U the utility, I[U] the memory of need, S the stance, B the slow tide of physical load and Ḃ its rate, each drawn on its own scale (E, U and I[U] on [0, 1], S on [−1, 1], B on [−0.5, 1], Ḃ on [−0.5, 0.5]). The brain monitor draws each as a ball on its own landscape, live, every decision.](book/figures/engine.svg)

### 21.2 The three landscapes the page prints

The utility's well, V(U) = −μ(U²/2 − U⁴/4) + (Ė/Eₘₐₓ)·U: a rising stress E
tilts the well toward the basin of collapse, and the ball rolls toward it unless the body is relieved. The stance's well,
Φ(S) = αₛS²/2 + βₛS³/4 − δS: S rolls to its minimum S* and the senses pull it back each decision. The tide,
B̈ = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B: the slow tide of physical load, a damped oscillator driven by the stance.

![The double well. The utility U rests in one of two basins: the working basin, where the body does its work inside its lines, and the basin of collapse. The stress E tilts the landscape; the brain's push and the body's relief tilt it back. A ball near the ridge between them is a body under load; the compass law and the nerves exist to keep it on the working side.](book/figures/potential.svg)

### 21.3 Calm and the grant

calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)), where κ is the body's coherence, h the headroom, σ
the stale share of the senses and ν the conflict. An organ may hand capacity back only when calm ≥ its threshold θ, the line is
clean and every sense is live; expanding stays allowed except under a security hold. Under the max, lifting off toward native
never needs this grant; going below native does. The monitor draws calm against θ for each organ, so the operator sees why a
hand-back was refused.

### 21.4 Native, beside

Native has no brain to draw: each of its controllers reads one reading, its own muscle's, and moves.
The amber panel draws, live from the same decisions, the mean position native's muscles' readings put them at, the share of its
muscles past their line, and how many of its own controllers moved their setting this decision. Native has no nerves: nothing
grants or refuses a controller, and a blind sense or a security hold changes nothing it does.

## 22. The Verdict

### 22.1 The change-acceptance test (the page's section 8d, `#s-verdict`)

Before a knob moves one step past native, the step runs as a
trial: costs at native first, then at the step. The engine reads the change exactly as a report reads a row, on the log of
each cost, with its 95% interval. Each step is kept unless the measurement reads LOSS or its estimated cost exceeds the 2%
allowance; an EVEN result (no difference resolvable from the noise) is accepted, so on a high-variance workload a step with a
small true cost can pass, and the lab under the monitor measures that false-acceptance rate.

![Block diagram: the verdict's paired trial around a slow knob, read GAIN, EVEN or LOSS. The reference is the cost of n pieces of work at the deepest step already allowed; the trial is the cost of n pieces at the step. Both on the log of the cost, with the 95% interval of their difference: an interval wholly above zero refuses the step; one inside the allowance keeps it; one wider than the allowance measures on, up to three times n each side. The verdict monitor runs this rule live at any true cost the viewer sets.](book/figures/c_verdict.svg)

### 22.2 The lab

Three knobs: *what the step truly does to the cost*, the *allowance* (tolerance) and the *noise σ of the log
cost*, with the *pieces of work measured each side*. Set what the step truly costs and watch the rule decide: the keep ratio at
each true cost is drawn, beside a rule of medians alone for comparison (the medians alone allow a step when the trial's median
is within the allowance of the reference's; the engine's rule also refuses any step whose interval sits wholly above zero, and
measures on while the interval is wider than the allowance, up to three times the pieces each side, keeping a step only if
both estimates are inside the allowance).

### 22.3 How each muscle wires it

The Kubernetes controller measures 200 requests each side against a 2% allowance
(`--verdict-samples 200 --allow 0.02`), the cost being each request's response time; the noise is measured at every build on
each request of the newest tables' own runs. The GPU card measures 30 requests; in its model the card's own time per request
carries no noise. The toy gate measures 60 (σ 0.25). Native has no trial: its knob never moves past its own setting, so there
is nothing to judge; every step Omni-Compass takes past native has to pass this test first.

![Flowchart: the give-back trial. A trial starts only with the organ's grant and a clean line; it runs to its full measurement and is never ended by the calm it causes; its reading against native decides, GAIN or EVEN keeps the step, LOSS refuses it and the setting stays; the release gate then passes or holds the write. The ticker's state column reads left native until a trial starts and acting while one runs.](book/figures/f_trial.svg)

## 23. Failure Modes, Controls and Residual Risk

### 23.1 The register (the page's section 9, `#s-fail`)

Every known way Omni-Compass can fall short, the control that mitigates it,
that control's coverage and the residual risk where it does not reach, and its implementation in the code; every failure mode
the live engine can be put through has a fault-injection control on the console, named in the row. The register is
`docs/SAFETY_CASE.md` and `docs/THREAT_MODEL.md` read as a table.

### 23.2 The resource costs shown, not judged

Under the register, the rows the three-run tables report but do not judge:
the governor's own commands, its processor time, the pending pods in a snapshot, the energy per core-hour. They are printed so
the cost of the governor is never hidden; they carry no word because their preregistrations declared them shown only.

## 24. The Component Specification

### 24.1 Every part and its equation (the page's section 10, `#s-math`)

The component specification: every part of the engine, its
equation in Unicode as the repository writes it, and the source module that implements it. Items 1 to 5 and 8 are the engine's
code and run in every view; items 6 and 7 as written (the compass law on each muscle, the plug's lever) drive the stress-test
model; in the harness views the max and the plants' own overrides take their place; the live controller runs the compass law
on the service, as the page's section 5e shows.

| Item | Part | What the page prints | Module |
|---|---|---|---|
| 1 | Senses | the muscles' meters read and normalised to nine observations: q, load, power, thermal, network, drift, stale, security, conflict | `adapter.observe_vector` |
| 2 | Assimilate | x ← (1 − a)·x + a·x[obs], a = 0.339: the engine is pulled toward what the senses read | `adapter.assimilate` |
| 3 | Evolve | equations (1) to (7), the Runge–Kutta method, ten micro steps of 0.01, the controller evaluated and not applied | `core.macro_step` |
| 4 | Allocate | push = clip(−f[U] + 12·(1 − U), ±25)/25 and ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρₘᵢₙ, ρ₀) | `adapter.Governor.step` |
| 5 | Nerves | κ, h, σ, ν into calm; calm against each organ's θ grants contraction (the spine to nodes, θ 0.7; compute to pods, 0.5; physics to the processor's clock, 0.3; energy to power, 0.3; distribution to routing, 0.5) | `nervous_system` |
| 6 | Compass | p = (r − lo)/(hi − lo); F = A·tanh((kₚ(p − ½) + k[d]·v)/A); fails up past 0.95; never hands back while climbing above the center; k[d] at three times critical damping from the muscle's own τ, the push | `compass_law.CompassLaw` |
| 7 | Plug | one wire in, one wire out: each write clipped to the cover; the snapshot taken once at the start is what reset restores; each write read back; the kill switch hands every lever to native at once | `compass_law.Plug`, `master.py` |
| 8 | Verdict | the paired trial of chapter 22 | `verdict.py` |

### 24.2 What the specification is for

It lets the reader of the page check that what moves on the monitors is what the
code says: the six spokes at the center of the cycle (E, U, I[U], S, B, Ḃ) are item 3's state, the inner arc of nine segments
is item 1's senses, the force field of the phase plane is item 6's law. The Owner's Manual carries the derivations; this page
carries the statements.

## 25. The Page Governs Its Own Drawing

### 25.1 Omni-Compass inside the page (the page's section 11, `#s-self`)

The engine that runs the page has Omni-Compass in it. Native
is the browser's own loop: every chart on screen drawn on every frame, and when the frame overruns, whole frames dropped.
Omni-Compass is the same loop with the engine's own compass law governing it. Each chart is a muscle whose knob is how many
frames it waits between draws, and the reading is the time between frames. Below the band's center the pedal lifts and every
chart is handed back to native, drawn every frame. Toward the line it pushes: the charts farthest from where you are looking
wait a frame or more, so the frame itself stays inside its line. Evidence class L: live software, on the viewer's own machine.

### 25.2 Reading it

The monitor shows the frame time on both sides, the frames dropped by native's loop, and the frames
waited by each chart under Omni-Compass. On a laptop with the wall in view, the charts on screen draw every frame and the
rest wait; scroll, and the waiting moves with the eye. The kill switch on the console reaches this governor too: engage it and
the page draws as the browser alone would.

---

# PART VII. READING A RESULT OFF THE PAGE

## 26. The Mechanism of Action, Side by Side

### 26.1 What native does

Each native controller reads one reading, its own muscle's, one to three decisions late (the pod
autoscaler one sync every 15 s), and moves its one setting toward the middle of its range, because protecting its one thing is
its whole job. It has no heart (nothing proves it is still there), no brain (no state, no memory of need, no stress, no tide),
and no nerves (nothing grants or refuses it, and a blind sense or a security hold changes nothing it does). Its moves are the
second ticker of the page's section 5c and the amber panel of the page's section 8c.

### 26.2 What Omni-Compass does, on top

Once every decision it reads the whole body through the plug (the senses), places
every reading in its band, lets the brain's state evolve, grants or refuses through the nerves, applies the compass law to each
muscle (push toward more as the reading climbs, lift toward native as it falls, smooth, never hammering), runs the verdict's
trial on any step past native, passes the release gate, writes through the plug and reads it back, and renews its lease. Every
one of those is a column of the audit, a line of the first ticker and a box of the cycle monitor. The native controllers keep
running underneath, untouched; Omni-Compass moves only the settings they already expose.

![Block diagram: the compass control loop. The muscle's reading comes in on the sense terminal, is placed in its band, and the compass law computes a force; the force is a setting written out on the motor terminal, inside the knob's cover, through the plug, and read back; the native controller sits inside the loop, still reading its own gauge and still moving its own setting; the kill switch opens the motor terminal and the lease restores the snapshot. On the page the two tickers show the two loops, native's own and the governor's on top of it, at the same seconds.](book/figures/c_compass_loop.svg)

### 26.3 Where to see the difference

On the official run playback (chapter 12): the first ticker shows the pedal pushed at
the compass position's first move off the center and the machines recommended before native's first late sample; the second
ticker shows native's autoscaler adding replicas a sync or two later. On the phase plane (chapter 20): the blue dots turn back
before the right edge where the amber ones cross it. On the scoreboard: the work waiting lower, the decisions past their line
fewer, the capacity held higher during the climb (power given) and eased back after it (the lift). On the brain (chapter 21):
calm falling under a surge and the grant refused until the line is clean again, which native has no equivalent of.

### 26.4 What the difference is not

It is not a competitor's dashboard. Omni-Compass never replaces the controller it sits
on; every move native makes is still made. A monitor where the two sides are identical is a muscle Omni-Compass left native,
at its limit or with nothing to add, and that reading is EVEN and correct.

## 27. From a Tile to Its Record

### 27.1 The chain

Every number on the wall can be walked back to the file it came from.

1. **The tile** names its gauge and its word, and links to the monitor it copies.
2. **The monitor** names the benchmark, the run (A, B or C) and the repetition, or the table and the row, and the evidence
   class.
3. **The three-run table** is in `results/live/` (`V13_*.md` on the engine that stands; each table names its engine), with
   its runs' ids and its rule printed at its head.
4. **The run's raw files** are on the `raw` branch at `results/live/raw/run-<id>/`, with `SHA256SUMS_ALL.txt`; the page
   matched every file it drew against that list. `scripts/raw_archive.sh open /run-<id>/` places them where the table names
   them.
5. **The governor's audit** is the run's `audit.jsonl`; native's own controllers' moves are its `capture.csv`.
6. **The scorer** is `tools/live_reps.py`; the page's per-repetition score equals the run's own summary over its repetitions.

### 27.2 The engine's name

Every table and every monitor names the engine it ran on; the page's title block names the engine
the page stands on (omni-v13). A table on an older engine stands only until its runs on the engine that stands land, and the
board says which it is. Nothing is read across engines.

## 28. When a Tile Reads LOSS

### 28.1 The rule

Theoretically the word LOSS should never appear: the engine that stands moves a knob only where a paired
trial on the muscle itself shows the muscle never behind for it, and where it cannot bring a knob a gain, that knob stays
native. When LOSS does appear, the row stays, and the founder's order governs: if Omni-Compass hurts something, no mechanism of
Omni-Compass is pushed through that muscle. The cause is found in this order, our own wiring first, native's setup second, the
scoring third; the mechanism or its wiring is corrected; the test runs again on the next engine version, and the earlier
table stands as its engine's record.

### 28.2 Read the three-run reading, not the one run

A red tile from one run of a table still running (the Azure steady set
at 33 of up to 100 repetitions) is that run's own word for that run and not yet a reading: its interval may include zero
(EVEN so far), and a three-run word needs all three runs. The alarms table grades it WARN. Wait for the look.

### 28.3 Open the root-cause document

Where the repository has found the cause it is linked from the tile:
`docs/POD_START_WAIT.md` (a pod's start on one shared host is the test machine's own unpacking of an image, the same on
both sides at the same host load), `docs/TAIL_LATENCY.md` (where a 95th or 99th percentile reads higher, and why),
`docs/BATCH_QUEUE_PREREGISTRATION.md` amendment 11 (the conveyance on a shared host beside another workload's room, fixed in
omni-v13). A tile with a root-cause document is a known cause with its fix landed or on the next version's list.

### 28.4 Which knob, and what to turn

The LOSS row names its gauge; the governor's audit names the knob that moved in that
window and why. Three outcomes follow, and only these:

| What the audit shows | What it means | What is done |
|---|---|---|
| a knob moved and the gauge went against its aim while the muscle stayed inside its limit | the wire or the rule is wrong for this muscle | the mechanism is corrected in the toy gate first, lands as the next engine version with no LOSS, and the benchmark runs again |
| a knob moved and the muscle went past its own limit, or another muscle's room was taken | a guard did not hold | the guard is corrected (as omni-v13 did for the conveyance on a shared host) and lands the same way |
| no knob moved, and the gauge still differs | the test machine, native's setup or the scoring | the rig or the scorer is fixed; a test machine's limit is never reported as Omni-Compass's result |

Nothing is ever tuned to make a row read well; no row is steered. What is held to the letter is the mechanism: the code does
what its rule says, the wire is fastened right, the harness measures as a deployment runs. On the page, each muscle of the stress-test model and of the replay carries its own switch on its card (the page's
section 8a): one muscle handed back to native while the rest stay governed, to see that muscle's part in the result. On a
real machine the same choice is the muscle's wiring, its knob set to watch (the Operator's Manual's wiring of each muscle);
a live switch per muscle on the running engine, beside the kill switch, is the next version's work (`docs/CHANGE_CONTROL.md`).

### 28.5 On your own system

The Operator's Manual's "wired right or wired wrong" (the Operator's Manual's section 4.5) and its drill book (the
Operator's Manual's chapter 28) are the procedure; `DISCLOSURES.md`, section 4, is the rule: where a result elsewhere differs from the published
record, the first presumption is the wiring, the settings or the reading, not the law.

## 29. What the Page Does Not Tell You

### 29.1 It decides nothing

The page is a monitor. Every word on it was decided in the repository when its table was
written. A reading you disagree with is taken up with the table and its runs, never with the page.

### 29.2 Class S is not proof

The harness, the shipped controller on the toy cluster, the GPU card, the Linux host, the
realms table, the grid's modelled half and the orchestra are our own models. They show the mechanism; they do not measure a
machine. A model's energy is not a meter's. The page says the class on every view, and the manuals say it again.

### 29.3 Slots not yet run are empty on purpose

The metered chip runs, the CPU host's meter, the clouds' sets still running
and the register's third-party slots are written as the repository holds them and marked not yet run. An empty slot is a true
reading of the record. Nothing is drawn in its place.

### 29.4 The page's age

A page is true for the build it names. The last tile of the wall is its age; the title block is its
commit. A reading landed after the build is on the next page.

### 29.5 The page's section 10 is measured on your machine

The self-governed rendering is class L on the viewer's own device; its
numbers are the viewer's browser's and prove nothing about any server.

### 29.6 Ask Omni-Compass is composed

Its answers are drawn from the page's records by a language model on the viewer's own
account, are not reviewed by any outside party, and are not a record. The records are the tables and the raw files.

---

# PART VIII. LICENSE AND YOUR COPY

## 30. License and Commercial Terms

The live engine page, this manual and every part of the repository are the property of The Omni-Compass LLC; all rights
reserved; all patents, copyrights and trademarks filed in the USA. Use is evaluation and simulation only under `LICENSE`
(`LicenseRef-OmniCompass-Evaluation-1.0`); any commercial use, commercialization, monetization, production use,
redistribution or hosted service requires a signed, paid Omni-Compass Enterprise License (`ENTERPRISE_LICENSE.md`). The
license is governed by the laws of the State of Delaware and the federal laws of the United States, and the state courts of
Delaware and the United States District Court for the District of Delaware have exclusive jurisdiction. Serving the page to
others is a hosted service and needs the Enterprise License. The license, the licensing questions and answers, the third-party
notices, the Enterprise License's standard terms, the patents and trademarks and the security policy are bound into this book
in full (Appendices F to K). Licensing, pilots and evaluations: the Contact page.

## 31. Verifying Your Copy of the Page

### 31.1 The engine

`python3 tools/omni_version.py` prints the engine the checkout stands on and its digest; the page's
`<html data-engine>` must name the same. `python3 docs/engine/build_live_engine.py --check` rebuilds the page in memory and
exits 1 if any record differs from the page; nothing is written.

### 31.2 The mathematics

`python3 docs/engine/check_live_engine.py` runs the page's brain, compass law and verdict against the
Python and the C++ (`docs/engine/cpp_core_probe.cpp`) and prints the largest difference, which is at machine precision.

### 31.3 The records

`python3 docs/engine/check_records.py` reproduces every record the page carries by an independent path
and compares value by value; `docs/engine/APPRAISAL.md` is the standing result.

### 31.4 The wiring

`python3 -m unittest tests.test_live_monitors` holds every monitor to its wiring: every page function a monitor names is in the
page's script; every Python, C++ and check file it names is in the repository; every monitor sits in a numbered section; every
section of the page closes what it opens; and every panel of the Grafana wall sits under the row of its section, numbered as the
page numbers it.

### 31.5 The whole

`python3 verify.py` runs every check of the repository, this page's included, and ends
`VERIFICATION: PASS`; `python3 tools/release_manifest.py` writes `RELEASE_MANIFEST.json` at the commit and must read 0 FAIL.
A copy whose page, engine or records differ from what these print is not a copy of the record.

---

# BACK MATTER

## Glossary

- **Alarm tile.** A judged row of a real or modelled run that read LOSS, or a run that ended without a measurement, raised on
  the wall worst first with its source and its root-cause document.
- **Anchor.** The part of a page address after `#` (`#s-health`) that names a section and does not move when sections are
  renumbered.
- **Band.** A reading's safe range, from calm (p = 0) through its center (p = 0.5) to its line (p = 1), with 5% cushions.
- **Beat.** One turn of the governor's loop: read, decide, write, renew the lease. The heart.
- **Calm.** κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)): the nerves' one number, against which each organ's threshold θ grants a hand-back.
- **Class (P, L, S).** The evidence class of a number: a physical meter, live software, our own models.
- **Compass position (p).** Where a reading sits in its band; 0 calm, 1 at the line.
- **Console.** The page's section 6: every runtime control of the live engine, acting on both sides alike.
- **Decision.** One turn of the governor; the unit of time on every live monitor.
- **Dial.** The max (every muscle to its own limit, never below native; the default) or the tune-down (never more than native).
- **Engine that stands.** The engine version on main, named on the page's title block and in `python3 tools/omni_version.py`.
- **Golden signals.** Latency, traffic, errors and saturation: on the wall, the work waiting, the work done, the decisions past
  their line and the capacity held.
- **Heart.** The governor's beat and its lease, drawn on the official run playback.
- **Immune system.** Omni-Compass's: native twins, the heat debt, the cure on the spot, the pools' give-back, the bone's grant.
- **Kill switch.** The instant hand-back of every lever to native, for security; red on the switch and on every time axis.
- **Lease.** The governor's proof of life; when it ages past its limit the watchdog walks every setting back to native.
- **Live / Recorded.** A knob marked Live acts on the live engine; one marked Recorded data chooses a record and modifies nothing.
- **Master switch.** The one switch at the top of the organism: ON (green), the kill switch engaged (red), OFF (white).
- **Monitor.** One section of the page that draws a record or the live engine; its small copy on the wall is a tile.
- **Native.** The whole system by itself with everything it ships with; amber.
- **Omni-Compass.** Omni-Compass on top of native; blue.
- **Pedal.** Push for more, lift for less; the force column of the governor's ticker.
- **Power given.** A resource spent or held that rose: what Omni-Compass put in to buy the work and speed beside it; green.
- **Shown, not judged.** A gauge declared in advance as shown only; grey; counted in no total.
- **Stopping rule.** The cloud sets' preregistered looks at 10, 20, 40 and 70 repetitions with 99% intervals (`tools/stop_rule.py`).
- **Ticker.** The governor's decisions (first ticker) and native's own controllers' moves (second ticker), newest first.
- **Tile.** One small monitor on the wall; click it to go to the monitor it copies.
- **Verdict.** The paired trial every step past native must pass: kept unless it reads LOSS or exceeds the 2% allowance.
- **Wall.** Every monitor of the page in one view (the page's section 1b), numbered 1 upward in its order of appearance and read left to right.

## Appendix A - The Page, Section by Section

| Page section | Anchor | Title | Chapter of this book |
|---|---|---|---|
| i | `#notice` | Legal notice | Notice and Disclaimer |
| ii | `#title-page` | Title page and build | 1, 27 |
| iii | `#s-problem` | The problem and Omni-Compass's solution | The Problem and Omni-Compass's Solution |
| iv | `#s-read` | Executive summary and reading key | the key; 3 |
| v | `#contents` | Engine table of contents | 2 |
| 1 | `#p-health` | The monitor wall and the control panel | 4 to 7 |
| 1a | `#s-health` | The control panel and the kill switch | 4, 5 |
| 1b | `#s-wall` | The monitor wall, read left to right | 4 |
| 1c | `#s-monlist` | The monitor list: every monitor by its number | 4 |
| 1d | `#s-status` | The status board: tiles, alarms and watch items | 4, 6 |
| 1e | `#s-master` | The master switch's wiring | 5 |
| 1f | `#s-proof` | The Python's runs, in this page | 4, 31 |
| 1g | `#s-loss` | Every LOSS row: its cause and its knob | 6, 28 |
| 1h | `#s-feed` | The golden signals, the event log and the live metrics | 6 |
| 1i | `#s-github` | CI pipeline: GitHub Actions | 7 |
| 2 | `#s-board` | The benefit board | 8 |
| 3 | `#s-whole` | The whole organism, every way it is bought | 9 |
| 4 | `#s-fleet` | Measured effect in full | 8 |
| 5 | `#p-evidence` | Evidence by stack, from the cloud down to the chip | 10 to 15 |
| 5a | `#s-cloud` | Cloud providers: Azure, Google Cloud, Amazon Web Services | 10 |
| 5b | `#s-orch` | Orchestrators and governors | 11 |
| 5c | `#s-ops` | Kubernetes: official run playback | 12 |
| 5d | `#s-runs` | Kubernetes: per-repetition run telemetry | 13 |
| 5e | `#s-live` | Kubernetes and cloud: the shipped controller's decision trace | 14 |
| 5f | `#s-stacks` | Hardware: the GPU card and the CPU host | 15 |
| 6 | `#p-organism` | The organism, live | 16, 17 |
| 6a | `#s-engines` | The organism, live | 16 |
| 6b | `#s-lab` | Telemetry analytics: the tensor, the modes, the service level | 17 |
| 7 | `#s-desk` | Control console | 18 |
| 8 | `#p-brain` | Control architecture: the brain | 19 to 22 |
| 8a | `#s-decision` | One control cycle, traced | 19 |
| 8b | `#s-plane` | Phase plane and scoreboard | 20 |
| 8c | `#s-brain` | The brain's internal state | 21 |
| 8d | `#s-verdict` | The verdict: change acceptance testing | 22 |
| 9 | `#s-fail` | Failure modes, controls and residual risk | 23 |
| 10 | `#s-math` | Component specification and mathematics | 24 |
| 11 | `#s-self` | Self-governed rendering | 25 |
| vi | `#s-disclose` | Disclosures, governing law and contact | 29, 30 |
| vii | `#notice-end` | Closing legal notice | Notice and Disclaimer |

## Appendix B - Every Control of the Console

| Control | Where | Acts on | Leaves alone |
|---|---|---|---|
| Kill switch | the top of the wall; the console | every lever of every governor on the page, to native at once; shades every time axis red | the records: nothing recorded is modified |
| Turn Omni-Compass OFF / ON | the console | the brain's outputs: OFF, read in shadow, nothing leaves; ON, outputs reach the muscles | the native side, which never stops |
| The max / Tune-down | the console | the dial of the live engine's governor | the records; the official runs' own dial, named in each |
| Demand × | the console | every muscle's demand, both sides, from this decision on | the seed |
| Noise σ | the console | each muscle's demand each decision, 1 + σ·z, one draw shared by both sides | the seed's day |
| Sensor delay (as it is, +8 ms, +16 ms) | the console | the decisions between a muscle's act and its controller's reading, both sides | the demand |
| Surge ×2 / Lose half its machines / A sense goes blind / Security hold | the console | one body part for 40 decisions, both sides | every other part |
| Pause / One decision / 1× 4× 16× 60× | the console | the console's clock | nothing else |
| The same day again / A new day | the console | the seed replayed or redrawn, with the knobs as set | the knobs |
| Every knob to its start | the console | demand, noise and delay, back to the day as written | the dial and the switch |
| A / B / C | the page's sections 5c, 5d, 5e, 5f | which run is played | the other runs |
| Benchmark, run, repetition | the page's sections 5c, 5d | which record is played | the record itself |
| Each muscle alone / One organism / Stress-test model | the page's section 8a | which body the organism monitor plays | the console's knobs, which act on whichever plays |
| Its own load / The climb / Work waiting in line | the page's section 4 | which load the realms table is read under | the table |
| On-site bare metal / Through the cloud / In the device / As a service | the page's section 3 | which way the stack is bought in the composition | the receipts |
| Every measured piece / The strict reading | the page's section 3 | which rule the synopsis counts by | the factors |
| Its one run beside the count / in the count | the page's section 3 | whether a governor that replaces a controller enters the whole | the governor's own table |
| ALERT / WARN / INFO; All / LOSS / The runs disagree / Live now / Guards and open items / GitHub | the page's sections 1d, 1h, 4 | which rows are shown | the rows |
| Copy the exposition | the page's section 1h | the clipboard | the page |
| This muscle: Omni-Compass ON / handed back to native; Every muscle back under Omni-Compass | the page's section 8a, on the muscle's card | one muscle of the stress-test model run by native's own controller alone, or in a replay shown by native's own record, while every other muscle stays governed | the body's recorded totals in a replay; the kill switch, which hands every muscle back at once |
| Run the Python's 500 runs here; a new set (base seed, count); print and download the receipts | the page's sections 1a (the control panel) and 1f (the proof monitor) | the page's own run of the Python's seeded runs, its digest against the Python's | the Python's record, `results/engine_runs/` |
| Speak aloud / Ask Omni-Compass / Stop | the page's section 6b | the viewer's browser voice; a question composed on the viewer's own account | the records |

## Appendix C - The Gauges on the Wall

| Gauge | Side | Aim | GAIN reads | Power given reads | Where it comes from |
|---|---|---|---|---|---|
| The work waiting | both | time waited: lower | the blue line under the amber | — | the live engine; on the official runs, pending pods and the queue |
| The work done | both | work done: higher | the blue line over the amber | — | requests served, jobs finished, work inside the line |
| The decisions past their line | both | missed: lower | fewer blue past the line | — | the compass positions over 1 |
| The capacity held | both | a resource held | a fall (a cut) | a rise | machines, replicas, clock in service |
| Response time, mean, 95th, 99th | both | time waited: lower | a fall | — | the runs' own samples, binned |
| Time over the response line | both | missed: lower | a fall | — | the share of samples over the line |
| Failed requests | both | failed: lower | a fall | — | the load generator's record |
| Alert minutes | both | time over the line: lower | a fall | — | whole minutes whose 95th percentile, failed requests counted over, was over the line |
| Machines billed, the compute bill | both | a resource spent | a fall | a rise | the cloud's own count of machines, priced at list |
| Energy (declared model, the meter, Kepler) | both | a resource spent | a fall | a rise | the declared model; the RAPL counters where a meter exists (P); Kepler shown, not judged |
| HPA replicas, pods started | both | a resource held | a fall | a rise | native's autoscaler's own record in both arms |
| Pod start wait, total and mean | both | time waited: lower | a fall | — | the pods' own start times; the test machine's limit never read as the governor's |
| The governor's commands, its additions inside the line, its own processor time | Omni-Compass | shown, not judged | — | — | the audit; native is 0 |
| Frame time, frames dropped, frames waited | both | time waited: lower | a fall | — | the viewer's browser (L, the viewer's machine) |

## Appendix D - The Colours and the Marks

| Mark | Meaning |
|---|---|
| Amber | native |
| Blue | Omni-Compass; on a reading, power given |
| Green | GAIN |
| Yellow | EVEN |
| Red | LOSS; the kill switch and its window; the master switch engaged |
| White, dashed edge | the runs disagree; the runs differ; not a reading |
| Grey | shown, not judged; a monitor with no record yet |
| Dashed blue on amber | Omni-Compass's side following native with the switch OFF |
| Accent border on a tile | the monitor it copies is on screen now |
| Red shading across a time axis | a kill-switch window |
| A bar on a ring | a room's heat debt (the immune system) |

## Appendix E - Troubleshooting the Page

| Symptom | Cause | What to do |
|---|---|---|
| The page is slow or stutters | the browser's own loop would draw every chart on every frame | the page's section 11 governs it: charts off screen wait; close other tabs; the kill switch on the console shows native's loop for comparison |
| A tile is grey and says "not yet run" | the record does not exist yet | nothing: an empty slot is a true reading; the board says where it stands |
| A monitor says "stopped before a result" | a cloud or chip run ended without a measurement | the alarms table carries it; the run's own log says why (a key cut short, a plan, a quota); fix at the cloud, never on the page |
| The age of the page is over three hours | the rebuild did not run or did not land | `.github/workflows/live-engine.yml` on GitHub; `python3 docs/engine/build_live_engine.py` locally |
| A number on the page differs from a table | the page was built before the table changed | the age tile; the table governs; the next build carries it |
| The two sides are identical on a monitor | the muscle is at its limit on native, or Omni-Compass left it native | EVEN, correct; chapter 26.4 |
| The first ticker is empty | the switch is OFF or the kill switch engaged | nothing decides on top of native while it is; turn it ON |
| Ask Omni-Compass does not answer | the page is open outside claude.ai or without permission | the rest of the page runs whole without it |
| The page refuses to build | the checkout's engine is not the one the page names | a new engine is written into the page's words by a person first; `python3 tools/omni_version.py` |

## Appendix F - The License

The license is bound here in full from the file `LICENSE` at the root of the repository, as the book is built.

## Appendix G - Licensing: Questions and Answers

Bound from `LICENSING_FAQ.md` as the book is built.

## Appendix H - Third-Party Notices

Bound from `THIRD_PARTY_NOTICES.md` as the book is built.

## Appendix I - The Enterprise License: Standard Terms

Bound from `ENTERPRISE_LICENSE.md` as the book is built.

## Appendix J - Patents and Trademarks

Bound from `PATENTS.md` and `TRADEMARKS.md` as the book is built.

## Appendix K - Security Policy

Bound from `SECURITY.md` as the book is built.

## Appendix L - The Page Word for Word: Every Section, Monitor and Knob

Bound from `docs/engine/PAGE_WORD_FOR_WORD.md` as the book is built: the page itself, written from
`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build by `docs/book/build_live_manual.py`, every section in the page's
order, every monitor under its number with its evidence class, state, feed and knobs, every knob and every LOSS row with its
cause and the knob that answers it.

## Contact

Licensing, pilots, evaluations and the Omni-Compass Enterprise License: **The Omni-Compass LLC**. Owner and developer: AJ Dubra.
Main office infrastructure: toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1. Landline, registered in
Florida: 321-746-4411. www.omni-compass.com. Repository: github.com/The-Omni-Compass-LLC/The-Omni-Compass. Any use beyond
evaluation and simulation requires a signed, paid Omni-Compass Enterprise License. Write to The Omni-Compass LLC before any
production use.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
