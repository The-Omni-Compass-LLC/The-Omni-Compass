# THE OMNI-COMPASS LIVE ENGINE MANUAL

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

October 2026

All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.

The printable book of this text, with its contents and appendices: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`. Built by `docs/book/build_book.py` --live.

## The Problem and the Answer


**What the whole industry faces.** Every computing system in service, from one server to a cloud region, from a GPU to a
building's chillers, a grid feeder or a robot cell, is run by a stack of native controllers: the Kubernetes autoscalers and
scheduler, the cloud's node pools, the GPU's power and clock firmware, the database's cache and connection pools, the
building's cooling loops, the battery's management system, the servo's loop. Each was designed and tuned alone, against its own
setpoint, with margins sized for the worst case it might meet. Three costs follow, on every stack:

1. **Capacity held idle.** Worst-case margins stay in place through the common case. Machines, power caps, caches and cooling
   run far inside their limits, and the room between the operating point and the limit is paid for and seldom used.
2. **Late reaction.** Reactive loops act on averaged, lagging signals and wait out deliberate cooldowns, so queues and
   response-time tails form before capacity arrives.
3. **Loops at cross purposes.** The loops share power, cooling, connections and memory. One loop's correction is another
   loop's disturbance, and no loop sees the whole.

Demand for computing, above all for AI and the cloud, is growing faster than the power, cooling and hardware that can be built
for it. The usual answer is to add: more machines, more power, more people watching thresholds. Replacing the native
controllers is not an answer most operators will take: they are proven, often certified, and the people on call know them.

**What Omni-Compass does about it.** Omni-Compass is a supervisory governor. It sits on top of those native controllers and
never replaces them. It plugs into each setting a native controller already exposes, through a two-way plug (one wire in, the
reading; one wire out, the setting), takes a snapshot of every setting before its first write, and governs the whole stack as
one body, the organism: every muscle driven as far as its own limit and never past it, and, on the engine that stands, never
below native; where it cannot bring a muscle a GAIN, that muscle stays native. It acts before a line is crossed instead of
after, reads back every write, puts every give-back to its own trial, records every decision with its reason, walks every
setting home if it stops (the lease) and stops at once on the kill switch. Its first rule is do no harm, judged at the
organism: never less work or health than native (`DISCLOSURES.md`, section 3). The aim is the one headline: more work,
faster, on fewer machines, with less energy, from the hardware and the controllers already in place; in a cloud, the same
work for a smaller bill.

**Where the page shows it.** The live engine page plays every benchmark back from its own SHA-256-checked files, native
beside Omni-Compass on top of native, lane by lane, and runs the engine's own runs in the page: the Python's seeded runs, and
the same runs through the engine's C++ twin, side by side (the page's section 10b). This book reads that page; the mechanism and every
result are in the Owner's Manual.

**What is not claimed.** No new physics, no new model of computation, and no promise for any system Omni-Compass was not
run on. It does not make a system immune to failure, delay or drift: it keeps each muscle inside its own limits and shows, row
by row, what it did against native. A result on another system is that system's own, from its own paired runs; where it
differs, the first presumption is the wiring (`DISCLOSURES.md`, section 4).

<!-- the key: GAIN, EVEN and LOSS (tools/readings.py) -->

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

## Preface

This is the Live Engine Manual, the third book: how to read the live engine page, the monitor of the engine and of
the benchmark runs GitHub ran. It is for the operator at the dashboard: which tile means what, which knob does what, where every
number comes from, and how the mechanism of action of Omni-Compass against native shows on the monitors. It explains neither how
the engine is built (the Owner's Manual) nor how it is wired onto a stack (the Operator's Manual).

The book is in eight parts, and it can be read in two ways.

| You are | Read |
|---|---|
| The operator on shift, at the wall | the Quick Reference card; Part Two (the wall and the switch); the chapter on a tile that reads LOSS in Part Seven; the troubleshooting appendix |
| CTO, architect, head of platform | the front matter; Part Three (the whole organism and the benefit board); Part Seven (the mechanism side by side; what the page does not tell you) |
| CEO, CFO, CIO, board member | the Problem and the Answer; the Foreword; the Disclosures; the bills and receipts in Part Three; the clouds in Part Four |
| Site reliability engineer, on call | the Quick Reference card; Part Two; the official run playback in Part Four (the heart and the two tickers); the gauges appendix |
| Control or plant engineer | Part Six (one cycle, the phase plane, the brain's state, the verdict, the specification); the console in Part Five |
| Auditor, diligence team | Part One (a monitor, not a drawing); the trace from a tile to its record and the verification chapter; the page's own appraisal |
| Procurement and counsel | the Disclosures and the papers bound into the back matter |

**Part One** says what the page is and how it is built. **Part Two** is the wall and the switch. **Part Three** is the whole
organism and the measured effect. **Part Four** is the evidence stack by stack, from the cloud down to the chip. **Part Five**
is the organism live and the console. **Part Six** is the brain. **Part Seven** reads a result off the page. **Part Eight** is
the license and how to verify a copy.

**Conventions.** `Code` is a command, file, anchor or switch exactly as typed. "Native" is the system by itself, amber;
"Omni-Compass" is Omni-Compass on top of native, blue; there is no third side. "A section" is a numbered part of the page, named
by its anchor; "a chapter" is a chapter of this book. A knob marked **LIVE** acts on the live engine; one marked **RECORDED**
chooses a record and modifies nothing. Every number carries its evidence class: P a physical meter, L live software, S our own
models (modelled); a model is never proof.

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
built on omni-v18; a later engine renames itself on the page's title block and this book is realigned in the same push.

**What this manual does not cover.** How the engine is built, its equations beyond the ones the page itself prints, the
wiring of Omni-Compass onto any stack, and the benchmark results themselves as a body of evidence: those are the Owner's and
the Operator's Manuals and `docs/STATE_OF_PLAY.md`.


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

**How to read a number beside a word.** The word comes first and settles the direction; the number is the size, and it wears
the word's sign so the two never pull apart: GAIN +29.6% on pods waiting means 29.6% fewer pods waited than under native (a fall
in waiting is the gain, so it is written with the plus of the word, never with the minus of the gauge); LOSS −2.3% on alert
minutes means 2.3% more minutes over the line; EVEN =0.9% means a 0.9% difference the noise covers; power given +3.1% means 3.1%
more of a resource put in to buy the work beside it. The gauge's own direction is never hidden: on the page, hover any word or any
coloured number and it says what the word means and why the number wears its sign, and where the page knows the gauge, what rose
or fell against native (the page's section iv, "How to read a number beside a word"; the founder's order of 23 October).


## What You Are Looking At: Omni-Compass, Hooked Up, and How to Read Its Report


**A live tuning engine, and one tuned engine.** The page is a live tuning engine: every knob, button and monitor on it turns in
real time, native alone, Omni-Compass on top, or both, and **any knob can move every metric, up or down**. Every benchmark is
one engine at one tune, the factory tune; any other setting shows the engine's range, never a benchmark result (the page's first
box, `#tuningBench`; section 1.1).

**What the live engine is.** The live engine is one web page, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, built by the
repository's own code (`docs/engine/build_live_engine.py`) from the engine that stands and from the repository's own
results. It is a monitor of the engine and of the benchmark runs GitHub ran: every number on it is read from a record the
repository holds (a three-run table, a run's raw files, the engine's own audit, the realms table, the models' own readings),
and every word on it (GAIN, EVEN, LOSS, power given) is that record's own reading under `tools/readings.py`. The page decides
nothing about any result and types nothing in. Where it plays the repository's own models (evidence class S) it says so, and
a model is never proof.

**What "native" and "Omni-Compass" mean on the page.** Two names today, a third ordered on 23 October (below). *Native* is the whole system
running by itself: every autoscaler, scheduler, firmware, thermostat, orchestrator and controller it ships with, every muscle
wired and moving by its own machinery. *Omni-Compass* always means Omni-Compass on top of native: the same whole system with
all of that still running underneath, and the governor on top of all of it, wired in through the two-way plug. No third side
exists anywhere on the page. Native is drawn in amber, Omni-Compass in blue, in every chart, table, tile and number.

**The third arm, Omni-Compass by itself** (the founder's order of 23 October, `docs/SOLO_PREREGISTRATION.md`). The same system with each muscle's own native controller switched off and Omni-Compass the only controller moving that knob: on Kubernetes no pod autoscaler and no cluster autoscaler, while Kubernetes' own scheduler and kubelet stay. Where native is a setting rather than a controller (a cache's memory ceiling, a pool's size) the two Omni-Compass arms are one and the same arm. On the page the arm that was called Omni-Compass is now called Omni-Compass and native wherever an arm is named (the chips, the table heads, the lanes), and the third arm's column appears in every table from its first run on GitHub's machines, once the engine that carries it lands; nothing is written for it before. Until then every two-arm reading on the page is native against Omni-Compass and native.

**What a monitor is.** The page is laid out as an operations monitor is: a wall of tiles at the top (the status board), each
tile a small copy of a monitor further down the page; then the monitors themselves, section by section, each with its own
knobs in a bar at its head ("Controls"). A knob marked *Live* acts on the live engine, the engine's own mathematics running in
the page; a knob marked *Recorded data* only chooses which record is shown and never modifies it. Every monitor shows native
beside Omni-Compass on the same demand, the same seconds, so the one difference left between the two sides is Omni-Compass.

**What a gauge is.** A gauge is one measured quantity of the system (the work waiting, the work done, a response time, the
machines in service, the energy drawn, a bill). On the page each gauge is drawn for both sides with its paired reading: the
change from native, its 95% interval, and its word. The word is decided by what the gauge is for (the key, above), never by the
sign of its number.

**How to read the page, in order.** First the switch and the engine (the master switch at the top of the wall, and the engine's
name, digest and commit in the title block). Then the four signals a service is watched by: the work waiting, the work done, the
decisions past their line and the capacity held, native beside Omni-Compass. Then every reading that went against native, worst
first (the alarms). Then the benefit board (the page's section 2), the whole organism, every way it is bought (the page's
Chapter 3), the measured effect in full (the page's section 4), the evidence stack by stack from the cloud down to the chip (the
page's Chapter 5), the organism live (the page's section 6), the console (the page's section 7) and the brain (the page's
Chapter 8). This manual follows that order, chapter by chapter.

**What this manual is, and is not.** It is the interpretation of the page: how to follow the dashboard, read each gauge, turn
each knob, and see the mechanism of action of Omni-Compass against native as the monitors show it. Nothing in it decides a
result: the records of authority are the repository's result files, the raw files GitHub archived with their SHA-256 lists, the
two other manuals and `DISCLOSURES.md`.


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



# Part One. The Page as a Monitor

*What the live engine page is: a monitor of the engine and of the runs GitHub ran, never a drawing; how it is built, its table of contents, and its two sides and three words.*


## 1. A Monitor, Not a Drawing


### 1.1 What the page is

The live engine is a monitor of the Omni-Compass engine and of the benchmark runs GitHub ran. A
monitor shows what its instrument reads; a drawing shows what its author believes. The page is the former by construction:
every record it replays is made again by the repository's own code on the checkout it is built from, and `--check` fails a
page whose engine is not the one `python3 tools/omni_version.py` reads. So the page never runs ahead of the repository: when
a new engine stands, the build stamps it on the page and rebuilds every record on it, and the page says in a banner that its
prose was written for the older engine until a person realigns the words.

It is also a live tuning engine, a tuning bench. Its buttons turn the engine's knobs in real time: the heartbeat from 5 to 120
s, the dial between the max and the tune-down, the pedal, each muscle driven or left native, up or down, in or out, minus or
plus. Turning them shows the mechanism of action and its variations with native alone, with Omni-Compass on top of native, or
both side by side. As on any engine, where the mixture, the intake, the exhaust, the firing or the pistons change what a car's
engine delivers, **turning any knob of Omni-Compass can change every metric, up or down, in any direction a tuner chooses**: one
engine for many vessels, tuned many ways, for many outputs. The records the page replays are something else: the main engine's
one tune, the factory tune, as the benchmarks ran it. That tune is chosen by a declared rule: of the tunes that harm no gauge
against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on
development seeds and read again on untouched ones (`docs/THE_TUNE.md`). What the page shows at any other setting demonstrates
the engine's range and is never a benchmark result; a tune other than the factory tune belongs to its tuner, and so do its
results. The first box at the top of the page says which is which (`#tuningBench`). The beat on the dial (the page's section 1j)
is one such knob: the factory tune runs it at 60 s, and every other beat is shown beside native with what it buys and what it
costs, as range, never as a result. Each muscle's own setting is part of the same factory tune: its card where one was found
under the same rule, the engine's setting for the rest (`realms/muscle_cards_v5.csv`).

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

The page opens with its legal notice (i), then the title page with the build (ii), the problem and the answer: what the whole industry faces and how
Omni-Compass addresses it (iii), the executive summary with the reading key (iv), and then its own table of contents (v, "Engine
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
to 1k, one letter for each of its panels, with no unnumbered entry in the contents.

### 2.2 The sections, as built on omni-v18

Appendix A lists every section with its anchor and the chapter of this book that
reads it. In the page's order: 1 the monitor wall and the control panel (1a the control panel and the kill switch, 1b the
monitor wall, 1c the monitor list, 1d the status board, 1e the master switch's wiring, 1f the Python's runs in the page, 1g
every LOSS row, 1h the golden signals, the event log and the live metrics, 1i the pipeline, 1j the heartbeat dial, 1k Omni direct: the three arms); 2 the benefit board; 3 the whole organism, every way it is bought; 4 the
measured effect in full (the organisms, every muscle, the register, the grid and every three-run table); 5 the evidence by
stack (5a the clouds, 5b the orchestrators and governors, 5c Kubernetes, the official run playback, 5d Kubernetes,
per-repetition telemetry, 5e the shipped controller's decision trace, 5f the chip and the host); 6 the organism live (6a
native and Omni-Compass, 6b the telemetry analytics and Omni-Compass in its own words); 7 the console; 8 the brain (8a one
cycle, 8b the phase plane, 8c the brain's state, 8d the verdict); 9 the failure modes; 10 the components, their mathematics and their C++ twin (10a the component
specification and mathematics, 10b the C++ twin, the Python's runs through the C++ engine); 11 the self-governed rendering.

### 2.3 Anchors

Every section has an anchor that does not move when the page is reordered: `#s-problem`, `#s-read`, `#p-health`, `#s-health`,
`#s-wall`, `#s-monlist`, `#s-status`, `#s-master`, `#s-proof`, `#s-loss`, `#s-feed`, `#s-github`, `#s-dial`, `#s-direct`, `#s-board`, `#s-whole`, `#s-fleet`, `#p-evidence`, `#s-cloud`, `#s-orch`, `#s-ops`, `#s-runs`, `#s-live`, `#s-stacks`,
`#p-organism`, `#s-engines`, `#s-lab`, `#s-desk`, `#p-brain`, `#s-decision`, `#s-plane`, `#s-brain`, `#s-verdict`, `#s-fail`,
`#s-math`, `#s-cpp`, `#s-self`, `#s-disclose`. A tile on the wall links to the anchor of the monitor it copies; a row of the table of
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

**The audit of 22 October** (`docs/engine/CONSENSUS_AUDIT_2026-10-22.md`). Five seats read the page again on omni-v16, each on
one dimension: the mathematics and the readings, the underwriting (evidence, provenance, claims), the editing (tone, terms,
consistency), the structure (hierarchy, order of comprehension, navigation) and the visual layout as rendered. That page carries
each seat's grade part by part, the consensus grade, every finding merged with what was closed in the same push, and the order of
the page the structure seat proposed, with its cost, for the founder's decision.

### 3.3 The sides are never a reading

Blue does not mean good and amber does not mean bad: they name who is being read.
Where the two sides look the same, they are the same, and that is EVEN. Where Omni-Compass's blue line sits closer to a
muscle's line than native's amber one, that is the max at work: every muscle to its own limit, never past it, and the
capacity it holds there is power given, shown beside the work and the speed it bought.

![Flowchart: how a gauge's number becomes a word. The gauge's declared aim is read first: time waited, missed or failed, where a fall is GAIN; work done, where a rise is GAIN; a resource spent or held, where a fall is a cut (GAIN) and a rise is power given. Then the paired change and its 95% interval: an interval that includes zero reads EVEN; clear of zero, the word follows the aim. Three runs A, B and C: GAIN or LOSS only when all three point the same way with every interval clear of zero; EVEN when any interval includes zero; the runs disagree when clear runs point different ways. The page draws exactly this rule, as tools/readings.py writes it.](figures/f_reading.svg)

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


# Part Two. The Wall and the Switch

*The status board, the master switch and its three states, the alarms, the golden-signal feed, the event log, the metrics exposition, and the pipeline that rebuilds the page.*


## 4. The Monitor Wall


### 4.1 The numbered monitors and the control panel

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

### 4.2 What the wall is

The wall (the page's section 1b, `#s-wall`) is every monitor of the page in one view: the same
canvases the sections draw, copied small four times a second, so nothing is drawn twice from different data. Every tile
carries at its top its number and its title in capital letters, what the monitor shows, and under them its section and its state (live, replay,
from the records, a model, or awaiting its run), so a tile says where its monitor is and what it represents before it is
opened. Click a tile and the page scrolls to the monitor it copies. The page's own governor (the page's section 11, chapter 25) leaves a monitor resting while it is
off screen; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to, and while the wall
is in view the resting monitors are drawn in turn, one a frame, each by its own drawing code; a tile with the accent border is
a monitor on screen now.

**The light on every monitor** (the founder's order of 23 October). Each tile carries a light in its top right corner, and each
monitor the same light beside its number on the page: green while the gauge the monitor draws is inside its lines; amber before
the line, when the gauge is within 3% of it or when its own slope over the last readings, carried three readings ahead, crosses it;
red when it is over; grey where the monitor has no line to watch (a bill, a count of runs), and the light says so.
The light reads the series the monitor draws and adds no number: on the live engine, the muscles against their lines; on a cluster
replay, the 95th percentile against the 200 ms line and the pods waiting for a place; on the heart, the decision's own time against
half its beat; on the CPU host, the busy share against the 75% line; on the card, the draw against its power limit; on the page's
own governor, the time between frames against 1.5 frames; on the proof, the page's runs against the Python's (green when the
digests match and every number is within 1e-9, red when they differ); on the governors and orchestrators, their own three-run
tables; on a record, the judged rows of the newest tables (a LOSS row lights red and stays). A light fed by our own models says
so (class S). Above the wall a line counts the lights and names the monitors heading for a line or over one, beside the engine's
own last entry on its side. The three-reading projection is the light's own: the brain's law acts on the position inside its
band and damps on the position's rate of change, with a fail-up at the band's 95% wall; it projects nothing ahead. Hover a light
for its reading.

### 4.3 The order of the board

The board is laid out the way an operations monitor is. The switch and the engine come first.
Next come the live organism's signals, native beside Omni-Compass, in the four a service is watched by (latency, traffic,
errors and saturation in site-reliability practice): here the work waiting, the work done, the decisions past their line and
the capacity held. Then every reading of the real and modelled runs that went against native, worst first. Last come GitHub
(the runs in progress and queued) and the age of this page. A tile's word is its reading against native by the key; a tile
with no reading says what it shows.

### 4.4 Reading a signal tile

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

### 4.5 Reading an alarm tile

An alarm tile is a judged row of a real or modelled run that read LOSS, or a run on the engine
that stands that terminated without a measurement. It names its gauge, its size with the word's sign, the table or run it
came from, and the repository's root-cause document where one exists (`docs/POD_START_WAIT.md`, `docs/TAIL_LATENCY.md`, and
the others). The alarms are ordered worst first by their size. Chapter 28 is what to do with one.

### 4.6 The age of the page

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

![State machine: the governor's modes. OFF is native alone; WATCHING reads and logs and writes nothing; AUTOPILOT pushes, lifts off and idles; CRUISE holds every machine in service while a known queue waits; RESET hands every setting back and reads it back. The kill switch leaves every mode for OFF at once; the lease walks a crashed governor's settings back to native. On the page the switch's three states are ON (green), the kill switch engaged (red) and OFF (white, the brain reading in shadow).](figures/g_modes.svg)

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

### 7.4 The heartbeat dial (the page's section 1j, `#s-dial`)

The governor's heartbeat, its full decision, is a dial from omni-v17 on: the main engine decides every 60 s, and the operator
may set any beat (`--interval`: 5, 15, 30, 60, 75, 90 or 120 s, or any value between), the fast checks every 5 s at every beat.
The section shows every beat beside native in two tables for each setting the models read (the cloud's: the tune-down, the
machines alone; the kind benchmark's: the max, every autoscaler sensed). The first table gives each beat's value and its word
against native: the reads of the cluster a day (what a beat buys: about 39,700 at 60 s and 86,400 at 5 s), the governor's own
processor, the pods waiting for a place, the 95th percentile, the minutes over the line, the autoscaler's shortfall, the machine
hours and the energy per core-hour; the main engine's row is set in bold. The second table gives each other beat's change
against the main engine's 60 s, with its word. Read a row across: a beat whose service words read GAIN or EVEN against native
and whose cost columns the operator accepts is a beat that can be set. A word of LOSS against native is the engine's at that
beat and is listed with every other LOSS row (the page's section 1g, chapter 6). The values are our own models (class S), each
beat's mean over seeded days on a plant that moves every 5 s; the real runs at every beat (`docs/PACE_PREREGISTRATION.md`,
amendment 3) take their place in the note above the tables when their three runs land. The governor's own screen in Grafana
shows the beat it runs at (`omni_heartbeat_seconds`, the median spacing of its last eleven decisions) and counts the time since
its last decision in beats of that setting; the staleness alert fires after three, at any setting. The dial is the tuning
bench's own example: the factory tune runs the main engine at 60 s, chosen and read again under the rule of `docs/THE_TUNE.md`;
any other beat is the engine's range on the page, never a benchmark result, until its own three runs land on that beat and are
read as that beat's. A beat set on a live system is the operator's own tune, and its results are its own.

### 7.5 Omni direct: the three arms (the page's section 1k, `#s-direct`)

From omni-v18 Omni-Compass's own orchestrator is part of the engine, and every organism it runs is shown three ways. **Native** is
Kubernetes' published autoscaling rule on the muscles (written by The Omni-Compass LLC from the published rule), every machine on and
the units spread. **Omni on native** is Omni-Compass on top of that rule: the rule's units and never fewer, with Omni-Compass's
reflex, conveyance, room rule, packing and parked machines above them. **Omni direct** is Omni-Compass alone on the muscles, no
Kubernetes beneath it. The section draws the three arms from the showing's own record (`results/orchestrator/`), class L.

The arm buttons (**All three**, **Native**, **Omni on native**, **Omni direct**) choose the arms drawn on the four monitors: the
work answered each step, the 95th percentile each step (with the service's line), the units serving each step (with the units'
top) and the machines on each step (with the machines there are). Native is amber, the two Omni-Compass arms blue, Omni on native
dashed and Omni direct solid. The step slider walks the run step by step, and every monitor's light reads the step it stands on.
The master switch shows native alone.

Under the monitors stand three tables. The first reads every pair (Omni on native against native, Omni direct against native, Omni
direct against Omni on native) on the four gauges by the one key, each word with its direction in words, from the one run of each
arm on one host (the quick form). The second gives each arm's totals in that run: requests answered, failed and wrong, the 95th
and 99th percentiles, machine-minutes, unit-minutes and the processor conveyed. The third is the full form's three runs on
GitHub's own machines, A, B and C from one commit (`results/orchestrator/V18_THREE_ARMS_ABC.md`): each pair and gauge with each
run's word and the one rule's reading of the three, GAIN, LOSS or power given in all three when every run's interval is clear of
zero on the same side, EVEN when any run's interval holds zero, the runs disagree when clear runs point different ways. Work aims
up; the 95th percentile aims down; units and machines are resources, so a fall is a cut, a GAIN, and a rise is power given.

On a real machine each arm is the control plane started with its brain (`python3 -m omni_orchestrator.control --brain yardstick`,
`omni_native` or `omni`), and its kill switch is the control plane's kill file: the brain off, the declared state held, every
conveyed wall handed back.

---


# Part Three. The Measured Effect and the Whole

*In the page's order (the founder's order of 20 October): the benefit board, the grid and the catalog, then the whole organism every way it is bought, its bills and receipts.*


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

### 8.3 The trading floor: the market map and the quote board

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

### 8.4 Aggregate: one figure for the whole board

The Omni index (`results/OMNI_INDEX.md`): the geometric mean of the
ratios of every measure that enters, where a measure enters only as its three-run reading allows (GAIN, LOSS or power given
in all three runs counts; EVEN counts as exactly 1, so nothing inside the noise is claimed either way). Each test is read
from its own newest three-run table, no table is pooled across engines, and every row names its table. The index is one
number for the board; its row of factors under it is the board's own audit.

![The three-run rule. A benchmark runs three times, A, B and C, on one engine version, each a paired run of native against Omni-Compass. A row reads GAIN or LOSS in all three of our runs only when the three agree in sign with every 95% interval clear of zero; EVEN, no difference beyond the noise, when an interval includes zero; the runs disagree when clear runs point different ways. The board and the index count by this rule and no other.](figures/readings.svg)

### 8.5 Third-party software still to be benchmarked

The register's slots, in order (`docs/REGISTER.md`): every muscle in
them already runs, modelled, in the 1,107-muscle catalog and the seven organisms, native and with Omni-Compass on top; a slot is
the same test on the outside world's own software, each queued until its three runs land. A slot shows its status in the
register's own words, what is measured (the lines of its preregistration) and the known limits said before the result.

### 8.6 The scale-out grid

Seven organisms × 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs: modelled (the misses)
and with the real cluster inside (the 95th percentile), both values shown in every square. The 1,000 tier runs on GitHub's free
runners only; paid machines stay at 100. Two buttons choose *the engine that stands: its runs as they land* or *the road: the
newest grid with its squares landed*. A square not yet landed says so; a square beyond a free runner's memory or time is listed
as pending runner capacity, never rented. The grid's monitor draws the engine that stands' own campaign as GitHub runs it: each
square filled by its runs started (pale) and measured (solid), as GitHub was read at the build, with the age of that reading in
its heading; the reading cursor walks every started square and names it under the grid. Once the grid's receipt is written, each
square takes its word. The road draws the newest grid with its squares landed, under its own engine's name, never read across.

### 8.7 Every three-run table

Every three-run table in the repository, native against Omni-Compass, every row as written,
each benchmark's newest engine's table; open a row to read every judged row that is not EVEN. The table's own rule is printed
with it; rows shown and not judged are left out of the counts; a tuning case is shown and never counted.

### 8.8 Every muscle and the seven organisms

From `results/realms_v5/REALMS_V5.json`, the realms runner at the max, its
engine and commit named above it (`tools/run_realms_v5.py`, catalog `realms/catalog_v5.csv`), ten paired seeds per muscle and
per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A
muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none
moving the other way; EVEN at its limit on native when its knob already sits at the top of its range; EVEN, the same as
native, when it wrote and nothing moved beyond the noise. Energy is power given where it rose. The seven organisms are listed
spine first, then the four realms, the four stacked and the whole tower, each under its own load, the climb and the work
waiting in line (the three buttons). Evidence class S: a model's energy is not a meter's.

### 8.9 Every family, by stack

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


# Part Four. Evidence by Stack

*From the cloud down to the chip: the clouds, the orchestrators, the official Kubernetes runs and their playback, the shipped controller's decision trace, the card and the host.*


## 10. The Clouds


### 10.1 One metric: the bill

In a cloud Omni-Compass shows one thing: the same work as native for a smaller bill, never a
bigger one. Every cloud set runs Omni-Compass at the tune-down on the machines alone (`OMNI_MACHINES_ONLY=1`,
`--give-back-only`): no pod autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's. It parks
only a machine the cloud already made, after its own trial, and wakes it on a breach. The bill and the machines aim lower;
work, speed and failures must read EVEN or GAIN. Azure runs first and is the measure of the other two (Google Cloud, Amazon
Web Services): the same tuning, mechanism and harness. Google's and Amazon's sets are not yet run: their queues are switched off
(24 October), kept ready as Azure's sets run, and the page reads each of their rows "not yet run" until the founder switches it on.

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
(`docs/AMAZON_SETUP.md`, section 1a); an Azure key stored in another form than the whole block from `{` to `}` (a client
secret's value alone, or a storage account's access key, for two) is stored again: one value to each of four boxes, or the
whole block under a new name, which leaves a running set's login untouched (`docs/AZURE_SETUP.md`, section 7; Azure joined the
check on 22 October). Nothing is built and nothing is billed until the check passes.


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

![Timing diagram: the lease. The governor renews its lease on every beat; the watchdog reads the lease on its own clock. When the governor dies without handing back, the lease ages past its limit (the larger of 120 s and five beats) and the watchdog walks every setting back to native, a step at a time, reading each back. On the page, the heart monitor shows the beat and how close the lease came to its limit; a stopped heart leaves the body exactly as native runs it.](figures/t_lease.svg)

### 12.3 A healthy heart, never pushed

The beat runs at a fixed, calm rate (on omni-v16 one decision every 15 s, the fast checks every 5 s between beats; the
runs replayed on the page ran before omni-v16, one decision a minute) and is never driven faster by the load it governs.
Every clock of the engine counts seconds, so the beat's pace sets how often the body is read, never what a rule means: a
give-back still waits its trial's minutes, the cushion still keeps its twenty minutes of memory, and a machine still goes
back at most one a minute. What it costs is counted inside the body's
own load (the row *Omni's own CPU*), so the organism never pays for its brain without knowing it. A decision that fails is
recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal
time. Two gauges read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page
calls a heart under strain when a decision takes more than half its beat, or a gap between beats runs past half the lease.

### 12.4 The heartbeat sweep: the beat as a knob

Under the heart stands the heartbeat sweep (the panel `#beatPanel`, monitor *The heartbeat sweep: every beat the governor can
run at*). The beat is a setting of the run, not a constant: the factory sets 15 s, and an operator may choose another for a
system's own reasons (a slower beat reads the cluster less often; a faster one answers sooner). The monitor shows what each
choice does. Its five rows of buttons pick the record to read:

- **Beat:** 5, 10, 15, 20, 30, 60, 75, 90 or 120 s.
- **Setting:** on-site, where the governor sizes the pool on top of the pod autoscaler, or in the cloud, the machines alone.
- **Engine:** omni-v16, every clock in seconds, or omni-v15, its rules counted in beats.
- **Against:** what each reading is set against: native, the same engine at 15 s (omni-v16's factory beat), or the same
  engine at 60 s (omni-v17's). The sweep's record is omni-v16's and omni-v15's; the dial's ladder (the page's section 1j, section 7.4) reads omni-v17.
  The monitor opens on 60 s, the factory's beat on the engine that stands.
- **Gauge:** pods waiting for a place, machine-hours, energy per used core-hour, the 95th and 99th percentile response, the
  minutes over the line, and the engine's own cost: its processor time, its reads of the cluster and its writes a day, and
  the fast check's rescues, the machines its 5-second check added only after a pod already waited.

The tiles give the chosen beat whole. They show what it is read against and every gauge's mean change with its 95% interval
and its word (GAIN, EVEN, LOSS or power given, by the one key); the number carries the word's sign (GAIN +, LOSS −, EVEN =),
never the gauge's raw direction. The last tiles give the engine's own cost a day; native,
which runs no governor, costs nothing there. The rescues tile says why a slow beat waits more: the full decision sizes the
pool ahead of the load, and read less often, the load outruns it between decisions, so the 5-second check adds the machine
only once a pod already waits.

The chart gives the chosen gauge at every beat. Each bar is the mean change over the seeds, coloured by its word, with its
whisker the 95% interval. A fall cannot pass −100%, so an interval reaching past it is cut there and marked ▼; the tiles
print it whole. The beat chosen is framed, and a cursor reads the beats in turn and names the row it holds.

Every number is our own model (evidence class S), never a benchmark result. The shipped controller of each engine runs on the
toy cluster's 5-second plant, eight seeds of a day each, paired by seed and read by the toy gate's own rule
(`tools/heartbeat_sweep.py`; the record, `results/toy_gate/HEARTBEAT_SWEEP.md`). Every beat on this monitor is read in
the model only: a real run reads the one beat it was started with, the governor's `--interval`, and the gauges
`omni_decisions_total` and `omni_own_cpu_cores` of `tools/omni_exporter.py` show the beat it runs at and what it costs.

### 12.5 The three charts

Response time, one candlestick per 30-second bin (open, high, low, close of the responses in the
bin), native beside Omni-Compass; the latency heatmap, every response binned by time and by duration, the darker the fuller;
throughput, requests served per 30-second bin. Read the three together: a GAIN in the 99th percentile shows as the candles'
upper wicks shortening on the blue side while the heatmap's upper band thins and the throughput bars stand level or higher.

### 12.6 The governor's ticker

From the repetition's own `audit.jsonl`: the minute and second of the decision, the compass
position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward
native). Then the machines it recommends, and the give-back verdict's state: *left native* means every setting stays
native's; *acting* means a trial on its own measurement. Every line of the ticker is a line of the governor's audit, and the
audit is the record of authority for what it did.

### 12.7 Native's own controllers' ticker

Native has no governor; its own controllers' moves are the second ticker, read
from the native arm's `capture.csv`: the replicas its pod autoscaler holds, the pods waiting for a place and the machines
ready, every change in the same repetition, newest first. With Omni-Compass OFF the first ticker is empty, for nothing
decides on top of native. The two tickers side by side are the mechanism of action in its plainest form (chapter 26).

![One pedal, no brake. Pushing the pedal adds capacity at once; lifting it eases capacity back toward native a step at a time, never below idle, the floor of two machines. Cruise holds every machine in service while a known queue waits. Watching reads and writes nothing. On the governor's ticker, push and lift are the force column, and the machines recommended are what the pedal bought or handed back.](figures/pedal.svg)

### 12.8 Every repetition side by side, and the run's receipt

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
hours each, a decision every 15 s, the controller's own default on omni-v16; class S). Three buttons choose the setting: *on top of the HPA, the max*; *the cloud: the
tune-down, machines only*; and the Linux host and the card (the page's section 5f).

![One decision of the governor. Read the body (the senses), place every reading in its band, let the brain's state evolve, grant or refuse through the nerves, apply the compass law to each muscle (push or lift), run the verdict's trial on a step past native, pass the release gate, write through the plug and read it back, renew the lease. On the decision-trace monitor each box is one column of the audit, and *open the same controller, decision by decision* steps through them.](figures/loop.svg)

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

### 15.3 The 8-card node, built and awaiting its run

Under the settings, a node of eight NVIDIA cards stands built before its run (`scripts/gpu_8card.sh`,
`docs/GPU_RUN_GUIDE.md`, section D): eight card slots, each native lane drawn from the repository's one-card model (class S, the
same model on every card until the run, never eight measurements), each Omni-Compass lane empty and marked awaiting its run.
Nothing on it is invented: on a running node the same panel reads the NVIDIA DCGM exporter's series card by card, and the
8-card run fills it when it lands.

### 15.4 Reading a row with nothing held off native

A row with no second held off native is Omni-Compass deciding to stay
native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native. That row is the
engine's own rule at work and is not a fault. The slots marked not yet run are written as the repository holds them and fill
in, played back from their raw files like every Kubernetes run, the moment their three runs land.

---


# Part Five. The Organism Live and the Console

*The organism rendered live, native beside Omni-Compass, its body scan and immune system; the telemetry analytics; and every knob of the console.*


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

![The seven organisms. The spine (267 muscles, every muscle that sits in all four realms), the four realms (Compute/AI/Cloud, Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized), the four stacked, and the whole tower of 1,107 muscles in 70 families. The organism monitor plays one organism of sixty muscles and each muscle alone; the benefit board (chapter 9) carries all seven.](figures/organisms.svg)

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

**Back to the factory tune.** One button, on the console under the kill switch, on the dock, above the wall and in every
monitor's own knobs, puts back two things at once: the engine's tune as it ships (`DISCLOSURES.md`, section 3: the dial at
the max, every muscle driven, Omni-Compass ON, the 60 s beat) and the page's plant at rest (the day as written, demand ×1, noise
σ 0, sense delay +0, no fault held, speed 1×, running, no frame load, and the heartbeat monitor on 60 s, on-site, pods waiting,
against native). It says what it put back. Turn anything, break it, watch it break; this
button brings all of it back (the founder's order of 23 October). Native alone is not a tune: it is the kill switch.

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


# Part Six. The Brain

*One control cycle traced, the phase plane and the scoreboard, the brain's state, the verdict, the failure modes, the component specification, and the page that governs its own drawing.*


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

![The compass band and the two forces. A reading is placed in its band, p = (r − lo)/(hi − lo), calm at 0, the center at ½, the line at 1, with 5% cushions at each end. Two antagonist forces act on the knob: the add force as the reading climbs toward the line, the hand-back force as it falls toward calm, combined as F = A·tanh((kₚ(p − ½) + k[d]·v)/A), smooth, never hammering. It fails up past 0.95 and never hands back while it climbs above the center. The phase plane's shading is this force at every point.](figures/band.svg)

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

![The engine's six states. E the stress, U the utility, I[U] the memory of need, S the stance, B the slow tide of physical load and Ḃ its rate, each drawn on its own scale (E, U and I[U] on [0, 1], S on [−1, 1], B on [−0.5, 1], Ḃ on [−0.5, 0.5]). The brain monitor draws each as a ball on its own landscape, live, every decision.](figures/engine.svg)

### 21.2 The three landscapes the page prints

The utility's well, V(U) = −μ(U²/2 − U⁴/4) + (Ė/Eₘₐₓ)·U: a rising stress E
tilts the well toward the basin of collapse, and the ball rolls toward it unless the body is relieved. The stance's well,
Φ(S) = αₛS²/2 + βₛS³/4 − δS: S rolls to its minimum S* and the senses pull it back each decision. The tide,
B̈ = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B: the slow tide of physical load, a damped oscillator driven by the stance.

![The double well. The utility U rests in one of two basins: the working basin, where the body does its work inside its lines, and the basin of collapse. The stress E tilts the landscape; the brain's push and the body's relief tilt it back. A ball near the ridge between them is a body under load; the compass law and the nerves exist to keep it on the working side.](figures/potential.svg)

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

![Block diagram: the verdict's paired trial around a slow knob, read GAIN, EVEN or LOSS. The reference is the cost of n pieces of work at the deepest step already allowed; the trial is the cost of n pieces at the step. Both on the log of the cost, with the 95% interval of their difference: an interval wholly above zero refuses the step; one inside the allowance keeps it; one wider than the allowance measures on, up to three times n each side. The verdict monitor runs this rule live at any true cost the viewer sets.](figures/c_verdict.svg)

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

![Flowchart: the give-back trial. A trial starts only with the organ's grant and a clean line; it runs to its full measurement and is never ended by the calm it causes; its reading against native decides, GAIN or EVEN keeps the step, LOSS refuses it and the setting stays; the release gate then passes or holds the write. The ticker's state column reads left native until a trial starts and acting while one runs.](figures/f_trial.svg)


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


### 24.1 Every part and its equation (the page's section 10a, `#s-math`)

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
| 8 | Verdict | the paired trial of chapter 22 | `verdict.py` (its C++ twin `cpp/src/verdict.cpp`, 24.3) |

### 24.2 What the specification is for

It lets the reader of the page check that what moves on the monitors is what the
code says: the six spokes at the center of the cycle (E, U, I[U], S, B, Ḃ) are item 3's state, the inner arc of nine segments
is item 1's senses, the force field of the phase plane is item 6's law. The Owner's Manual carries the derivations; this page
carries the statements.

### 24.3 The C++ twin (the page's section 10b, `#s-cpp`)

The engine is written twice, in Python and in C++, line for line where a twin exists. Every time the page is built, the
Python's own runs are fed into the C++ as its input and the C++ answer is set beside the Python's, number by number. Where
they are the same to the last digit, the two are one engine. The section holds five tables.

| Table | What it shows | How to read it |
|---|---|---|
| Every twin, on its own parity check | each Python file and its C++ twin, the inputs the check fed both, the largest difference, and the reading | "the same" on every row is a whole engine in two languages; "DIFFERS" names the row to look at |
| The Python's runs through the C++ harness, receipt by receipt | the record of the Python's seeded runs the page shows (the jump generator's 500), its draws (the Python's injection) fed to the C++ harness at the page's build (`cpp/tools/engine_runs.cpp`): the record, its runs and base seed, the Python's digest, the C++ engine's digest, how many receipts are identical to the last bit, the largest difference, the reading, and the GitHub run that made the record | the Python's runs are the input and the C++ engine's receipts the output; the two digests one string and every receipt identical is the same engine run twice, in two languages |
| The compass law of every run on this page | every compass law the page's own runs wired while the page was built, grouped by the file that wired it, each law's readings in the order they came, through the C++ law and through the Python again | the C++ against the Python, and the Python again against the run's own forces: 0 (identical) on both is the run's law reproduced exactly |
| The seven organisms at the tune-down | each organism, its muscles, the muscles that run the compass law at the tune-down, the readings fed through the C++, and any muscle that differs | at the max, the default brain, the edge and the bone decide each muscle, and they have no C++ twin yet; the tune-down is where every muscle's law is the compass law, so that is where it is fed through |
| What runs in Python only, for now | every part of the engine with no C++ twin yet, by file | the list is the work still to twin; nothing on it is hidden from the other tables |

A box under the organisms' table finds any muscle by its catalog id: it names each organism the muscle's law ran in, its
readings, and whether the C++ and the Python gave the same answer. A muscle with no lever at the tune-down stays native
there, and the box says so.


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


# Part Seven. Reading a Result off the Page

*The mechanism of action side by side, the trace from a tile to its record, what to do when a tile reads LOSS, and what the page does not tell you.*


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

![Block diagram: the compass control loop. The muscle's reading comes in on the sense terminal, is placed in its band, and the compass law computes a force; the force is a setting written out on the motor terminal, inside the knob's cover, through the plug, and read back; the native controller sits inside the loop, still reading its own gauge and still moving its own setting; the kill switch opens the motor terminal and the lease restores the snapshot. On the page the two tickers show the two loops, native's own and the governor's on top of it, at the same seconds.](figures/c_compass_loop.svg)

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
the page stands on (omni-v18). A table on an older engine stands only until its runs on the engine that stands land, and the
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

### 29.5 The page's Chapter 10 is measured on your machine

The self-governed rendering is class L on the viewer's own device; its
numbers are the viewer's browser's and prove nothing about any server.

### 29.6 Ask Omni-Compass is composed

Its answers are drawn from the page's records by a language model on the viewer's own
account, are not reviewed by any outside party, and are not a record. The records are the tables and the raw files.

---


# Part Eight. License and Your Copy

*The terms the page and this manual are licensed under, and how to verify a copy of the page.*


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


# Back Matter


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
- **Console.** The page's Chapter 6: every runtime control of the live engine, acting on both sides alike.
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


## Appendix A. The Page, Section by Section


| Page section | Anchor | Title | Chapter of this book |
|---|---|---|---|
| i | `#notice` | Legal notice | Notice and Disclaimer |
| ii | `#title-page` | Title page and build | 1, 27 |
| iii | `#s-problem` | The problem and the answer | The Problem and the Answer |
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
| 1j | `#s-dial` | The heartbeat dial: every beat beside native | 7 |
| 1k | `#s-direct` | Omni direct: the three arms, native, Omni on native and Omni direct | 7 |
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
| 10 | `#s-math` | The components: their mathematics and their C++ twin | 24 |
| 10a | `#s-math` | Component specification and mathematics | 24.1, 24.2 |
| 10b | `#s-cpp` | The C++ twin: the Python's runs through the C++ engine | 24.3 |
| 11 | `#s-self` | Self-governed rendering | 25 |
| vi | `#s-disclose` | Disclosures, governing law and contact | 29, 30 |
| vii | `#notice-end` | Closing legal notice | Notice and Disclaimer |


## Appendix B. Every Control of the Console


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


## Appendix C. The Gauges on the Wall


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


## Appendix D. The Colours and the Marks


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


## Appendix E. Troubleshooting the Page


| Symptom | Cause | What to do |
|---|---|---|
| The page is slow or stutters | the browser's own loop would draw every chart on every frame | the page's section 11 governs it: charts off screen wait; close other tabs; the kill switch on the console shows native's loop for comparison |
| A tile is grey and says "not yet run" | the record does not exist yet | nothing: an empty slot is a true reading; the board says where it stands |
| A monitor says "stopped before a result" | a cloud or chip run ended without a measurement | the alarms table carries it; the run's own log says why (a key cut short, a plan, a quota); fix at the cloud, never on the page |
| The age of the page is over three hours | the rebuild did not run or did not land | `.github/workflows/live-engine.yml` on GitHub; `python3 docs/engine/build_live_engine.py` locally |
| A number on the page differs from a table | the page was built before the table changed | the age tile; the table governs; the next build carries it |
| The two sides are identical on a monitor | the muscle is at its limit on native, or Omni-Compass left it native | EVEN, correct; chapter 26.4 |
| The first ticker is empty | the switch is OFF or the kill switch engaged | nothing decides on top of native while it is; turn it ON |
| The page refuses to build | the checkout's engine is not the one the page names | a new engine is written into the page's words by a person first; `python3 tools/omni_version.py` |


## Appendix F. The License

The license is the file `LICENSE`.

## Appendix G. Licensing: Questions and Answers



Plain answers to the questions buyers, engineers and their lawyers ask. The binding terms are in `LICENSE`; where
this page and `LICENSE` differ, `LICENSE` governs. Every declaration is in `DISCLOSURES.md`.

**Is Omni-Compass open source?** No. The source is published so that it can be evaluated, reproduced and audited. It is
licensed under the Omni-Compass Evaluation License 1.0 (`LicenseRef-OmniCompass-Evaluation-1.0`), which permits
evaluation and simulation only.

**What may I do without a commercial license?** Evaluation and simulation, free of charge (`LICENSE`, sections 1.4,
1.5 and 2): read the code; run `verify.py`, the simulations and the benchmarks; reproduce the published results and
publish your own, every row included (`LICENSE`, section 4); run Omni-Compass in watch, dry-run or shadow mode, or in a test
environment, on systems you own or control, where it writes to nothing that serves production traffic or real users and
to no physical process outside a test bench. A limited patent license comes with it, for evaluation only (`LICENSE`,
section 2.2).

**What needs the Omni-Compass Enterprise License?** Every commercialization or monetization of any kind; production
use; operating any system beyond evaluation; offering it, or its function, as a hosted, managed or software-as-a-service
offering; redistributing it; incorporating it, or any part or derivative of it, into a product, service, appliance or
firmware; using it or its results to build or train a competing product (`LICENSE`, sections 3 and 5). The Enterprise
License is a written agreement signed by The Omni-Compass LLC and paid for; its standard terms are summarized in
`ENTERPRISE_LICENSE.md` (production, hosted service, OEM and embedded, managed service provider, research).

**May I run it as a service for others?** Not without an Enterprise License with a hosted-service rider (`LICENSE`,
section 3(c); `ENTERPRISE_LICENSE.md`, section 1).

**May I connect it to a grid, a plant, a vehicle or a medical device?** Not under the evaluation license: such systems may
be studied only in simulation. A live connection to any physical system needs an Enterprise License and a written safety
case accepted by the system's owner (`LICENSE`, section 10).

**How is the Enterprise License priced?** Against the measured gain on the customer's own paired receipts (native
against Omni-Compass on the same system, the same load and the same clock). Terms are set in each signed agreement; no
price stated anywhere in this repository is an offer.

**Are patents involved?** All patents, copyrights and trademarks covering the
Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC
(`PATENTS.md`). The evaluation license grants no patent license beyond evaluation.

**May I use the name or the compass rose?** Only to refer to Omni-Compass accurately (`TRADEMARKS.md`).

**May I contribute?** Contributions require the contributor license agreement (`.github/CLA.md`): every contribution
is assigned to The Omni-Compass LLC, with a patent license from the contributor.

**Does Omni-Compass send data anywhere?** No. The software contains no telemetry and makes no network connection of
its own except to the systems an operator points it at (a Kubernetes API, `nvidia-smi`, a meter command).

**What do scanners report?** The license is declared in machine-readable form for Black Duck, FOSSA, Snyk and REUSE
(`pyproject.toml`, `REUSE.toml`, `.fossa.yml`, `.snyk`, `sbom/`); third-party components are listed in
`THIRD_PARTY_NOTICES.md`.

**Can the terms change?** Yes. The Omni-Compass LLC reserves the right to change the software, its documentation, its
results and these terms at any time, without notice; a changed version applies to copies obtained and uses made after it
is published (`LICENSE`, section 9). A signed Enterprise License governs its own term.

**Which law governs?** The laws of the State of Delaware and the federal laws of the United States, with exclusive
venue in the Delaware state courts and the United States District Court for the District of Delaware (`LICENSE`,
section 19). The Omni-Compass LLC is based in Florida.

**Who do I contact?** The Omni-Compass LLC, main office infrastructure, toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1, landline 321-746-4411 registered in Florida, www.omni-compass.com.

## Appendix H. Third-Party Notices



Omni-Compass uses the following third-party components. Each remains under its own license; nothing in the
Omni-Compass Evaluation License changes those terms. Installed versions are those resolved from `requirements.txt`.

| Component | Use | License |
|---|---|---|
| NumPy | numerical arrays | BSD-3-Clause |
| Matplotlib | charts in the reports | Matplotlib License (PSF-based, BSD-compatible) |
| ReportLab (open-source edition) | the printable book and reports | BSD-3-Clause |
| Numba | compiled inner loops of the motion-axis plant | BSD-2-Clause |
| PyTorch (on GPU machines only, not installed by `requirements.txt`) | the GPU workload of the benchmark | BSD-3-Clause |
| `tests/third_party/hpa_independent.py` | an independently written HPA reference used unmodified in tests | its own terms, stated in the file |
| Liberation Serif and Liberation Sans fonts (embedded in the PDF book) | typesetting | SIL Open Font License 1.1 |
| DejaVu Sans and DejaVu Sans Mono fonts (embedded in the PDF book) | typesetting | Bitstream Vera / DejaVu license (free) |
| PlanetLab / CoMon VM CPU traces, March 2011 (`fleet/traces/`, `k8s_controlplane/traces/`; source in their `PROVENANCE.json`) | held-out demand for the modelled fleet | their own terms (public research data); no Omni-Compass copyright is claimed in them |
| Google cluster-usage traces 2011 (`clusterdata-2011-2`), from which `results/traces/google2011/` is derived (`docs/TRACES_PREREGISTRATION.md`) | the public demand trace on the real cluster | Google's published terms for the traces; no Omni-Compass copyright is claimed in the trace itself |

Kubernetes, kind, `kubectl`, the NVIDIA driver and `nvidia-smi` are not distributed with Omni-Compass; it calls them
where an operator has installed them. Their names are the property of their owners (`DISCLOSURES.md`, section 1).

## Appendix I. The Enterprise License: Standard Terms



This page summarizes the standard terms of the Omni-Compass Enterprise License, the paid license that every production
use, commercial use, hosted service, distribution, OEM or embedded use, and every other commercialization or monetization
of Omni-Compass requires (`LICENSE`, section 5). It is a summary for evaluation and planning. It is not an offer, and it
binds no one: only an Enterprise License signed by The Omni-Compass LLC and the licensee, with its order form, grants any
right, and that signed agreement controls over this page in every respect.

### I.1 What can be licensed

| License | What it allows |
|---|---|
| **Production** | The licensee runs Omni-Compass on top of its own systems (clusters, fleets, cards, sites, plants), on premises or in its own cloud accounts, within the scope in the order form |
| **Hosted service** | The licensee offers Omni-Compass's function to its own customers as a hosted, managed or software-as-a-service offering, under a hosted-service rider (per customer, per managed unit or revenue share) |
| **OEM and embedded** | The licensee ships Omni-Compass inside its own product, appliance, firmware or platform, under an OEM rider (per unit or per installed base) |
| **Managed service provider** | The licensee operates Omni-Compass for named third parties under a managed-service rider |
| **Research** | A university or public laboratory uses Omni-Compass beyond evaluation for non-commercial research and publication, under a research rider |

**Scope** is set in each order form: the licensed systems and their size (machines, cores, cards, sites, muscles or
managed units), the fields of use, the territory, the named sites or accounts, and the engine versions covered.

### I.2 Fees

Fees are set in each order form: a subscription, a usage-based fee, a share of the measured value captured, or a
combination, with any minimum commitment. Where fees track value, the value is measured on the licensee's own paired
receipts (native against Omni-Compass on the same system, the same load and the same clock), by the method the order form
names. Payment terms, taxes and late charges are as the order form states. No price, rate or benchmark in this repository
is an offer.

### I.3 What the licensee receives

1. The licensed engine at a named, sealed version (its fingerprint, `tools/omni_version.py`), and each later version the
   subscription covers.
2. The wiring kits and the plug for the licensed systems, the manual and the book, and the receipts tooling.
3. Support and maintenance at the tier in the order form: response targets, named contacts, and corrections of defects
   that reproduce on the licensed version.
4. Installation through the manual's levels: read-only first, the wire check, a watch arm equal to native, then writing
   levels one at a time, each with its receipt.

### I.4 Warranties

1. **Conformance.** For the warranty period in the order form, the licensed version performs materially as its
   documentation describes. The remedy is correction or, failing that, a refund of the fees paid for the nonconforming
   version for the affected period.
2. **The safeguards.** The kill switch hands every setting back to the value read before Omni-Compass's first write; the
   shield keeps every write inside the cover the operator granted; Omni-Compass never fights another writer.
3. **No other warranty.** No outcome, saving or result on the licensee's systems is warranted. Published results are
   evidence about the systems they ran on (`DISCLOSURES.md`, section 2).

### I.5 Intellectual property

1. The Omni-Compass LLC keeps all right, title and interest in Omni-Compass, the Mechanism and the marks. The licensee
   receives the rights its order form lists, for its term, and no others.
2. **Patent license.** The Enterprise License includes a license under The Omni-Compass LLC's patent rights in the filed
   applications, and in any patent issuing from them, for the licensed scope.
3. **Infringement indemnity.** The Omni-Compass LLC defends the licensee against a third-party claim that the licensed
   version, used as licensed, infringes that party's intellectual property, and pays the damages finally awarded or the
   settlement it agrees, subject to prompt notice, control of the defense and the usual exclusions (modifications,
   combinations, unlicensed use, versions superseded by an offered fix). Remedies may include a license, a modification
   or a refund.
4. **Confidential filings.** The patent application number and other confidential information are disclosed to a
   licensee under the agreement's confidentiality terms.

### I.6 Limits of liability

Each party's liability is limited to the fees paid or payable in the twelve months before the claim, and neither party is
liable for indirect, incidental, special, consequential or punitive damages, except for the exclusions the signed
agreement states (for example, breach of confidentiality, the infringement indemnity, and the licensee's breach of the
license scope).

### I.7 Confidentiality, data and security

1. **Confidentiality.** Mutual, for the term and a period after it, covering non-public information either party gives
   the other.
2. **Data.** Omni-Compass contains no telemetry. The licensee's data, readings, settings and receipts stay on the
   licensee's systems and remain the licensee's. Where the licensee chooses to share data for support, a data-processing
   agreement applies.
3. **Security.** A software bill of materials ships with every version (`sbom/`); vulnerabilities are handled under
   `SECURITY.md`; the licensee may run the verifier (`python3 verify.py`) and the seal checks on every delivered version.

### I.8 Safety and operation

1. The licensee remains the operator of its systems. The machines' own controls and protections stay in place;
   Omni-Compass sets only values they already accept.
2. Any connection to a physical system (grid, plant, vehicle, robot, medical device, facility) requires a written safety
   case accepted by the system's owner and every review its regulator requires; safety-critical systems are licensed only
   on those terms.
3. The kill switch stays operable at all times.

### I.9 Compliance, audit and insurance

1. Each party complies with export-control, sanctions and anti-corruption law.
2. The licensee reports usage against the licensed scope as the order form provides, and The Omni-Compass LLC may verify
   it on reasonable notice, no more than once a year.
3. Insurance, where the order form requires it, is carried by each party at the limits stated there.

### I.10 Term, renewal and transition

1. Term and renewal are as the order form states.
2. On termination or expiry, the licensee stops use, every setting Omni-Compass changed is handed back to native (the
   hand-back is built into the engine), and every copy is returned or destroyed; transition assistance is available at
   the rates in the order form.
3. Source-code escrow for the licensed version is available under a three-party escrow agreement.

### I.11 Governing law and precedence

The signed agreement states its governing law and venue; the standard is the law of the State of Delaware, with venue in
the Delaware state courts and the United States District Court for the District of Delaware. Its order of precedence is: the order form, then any rider, then
the Enterprise License terms, then the documentation. This page and the evaluation license (`LICENSE`) are superseded by
the signed agreement for the licensee and its scope.

### I.12 How to obtain one

The Omni-Compass LLC, main office infrastructure, toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1, landline 321-746-4411 registered in Florida, www.omni-compass.com. A license starts with an evaluation on the licensee's own systems
(`LICENSE`, section 1.4): watch mode, the wire check, and paired receipts on its own load.

## Appendix J. Patents and Trademarks

### J.1 Patents



**All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.**

The filings cover, among other things, the Omni-Compass engine (the six-state closed law and its bounded control
command held through the integration step), the compass law (the service position pulled to the middle of its band by a
bounded push and pull, with fail-up at the wall), the antagonist up/down wiring of each muscle, the plug contract (one
restore point, read-back, the one-writer rule), the two-wire governance of a processor (clock ceiling and power limit),
the two-way nervous system that grants and withdraws authority per organ, and one governor over many machines and
realms on one clock.

#### J.1.1 What has been filed

| | |
|---|---|
| Application | a **nonprovisional utility patent application** under 35 U.S.C. 111(a), filed with the United States Patent and Trademark Office |
| Title of the invention | **The Omni-Compass** |
| Inventor | Alan John Dubra, Kissimmee, Florida, United States |
| Drawing sheets | 15 |
| Application data sheet signed | 20 September 2026 (form PTO/AIA/14, 37 CFR 1.76) |
| Publication | normal eighteen-month publication requested |
| Application number | withheld here on purpose; the filing is verifiable with the USPTO and is shown to a licensee under a signed Omni-Compass Enterprise License |

The application data sheet names no assignee; the application stands in the inventor's name. Any assignment to The
Omni-Compass LLC is recorded with the USPTO separately (37 CFR part 3).

No patent license is granted by publishing this repository, by the evaluation license, or by any act of The
Omni-Compass LLC other than a signed, paid Omni-Compass Enterprise License. Use outside the evaluation license is
infringement. Everyone who downloads, forks, scans or runs this software is on notice of these filings.
### J.2 Trademarks



**All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.**

#### J.2.1 The marks

"Omni-Compass", "OmniCompass", the Omni-Compass compass rose with its ring of Greek letters, and the related names, logos
and trade dress (the "Marks") are trademarks of The Omni-Compass LLC; trademark applications have been filed in the
United States. Neither the evaluation license (`LICENSE`) nor publication of this repository grants any license to the
Marks. A license to use them is granted only in a signed Omni-Compass Enterprise License, and only as it states.

#### J.2.2 What is allowed without a license

- Referring to Omni-Compass by name, accurately and in plain text, to say what it is, that you evaluated it, or that a
  result was produced with it, with the engine version and commit (`LICENSE`, section 4).
- Linking to the repository or to www.omni-compass.com.

#### J.2.3 What is not allowed

- Using any Mark, or anything confusingly similar, in the name of a product, service, company, domain, account, package,
  repository, fork or derivative.
- Using the logo or the compass rose, or altering any Mark.
- Suggesting endorsement, sponsorship, certification, partnership or affiliation by The Omni-Compass LLC.
- Using a Mark in advertising, comparative claims or sales material without a signed license.

#### J.2.4 Other companies' marks

Kubernetes is a trademark of The Linux Foundation; NVIDIA is a trademark of NVIDIA Corporation; KEDA and Karpenter are
projects of their maintainers; other names belong to their owners. Their mention describes compatibility or a system
Omni-Compass was tested with; it states no affiliation, endorsement or certification (`DISCLOSURES.md`, section 1).

#### J.2.5 Reporting misuse

The Omni-Compass LLC, main office infrastructure, toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1, landline 321-746-4411 registered in Florida, www.omni-compass.com.

## Appendix K. Security Policy



### K.1 Reporting a vulnerability

Report a suspected vulnerability privately to The Omni-Compass LLC by telephone at its main office infrastructure (toll-free direct 1-888-339-9551; system route asset 1-888-DEX-YLL-1, landline 321-746-4411 registered in Florida) or through www.omni-compass.com, never in a public issue,
pull request or discussion. Include the version and commit, what you saw, how to reproduce it, and its likely impact. We
acknowledge reports, keep the reporter informed, and coordinate disclosure: a fix or a mitigation is published before the
details are, and the reporter is credited if they wish. Please give us a reasonable time to fix before any disclosure, do
not access data that is not yours, and do not disrupt any system; good-faith research that follows this policy will not
be pursued by us.

### K.2 What is in scope

The engine, the controllers, the plugs and wiring, the harnesses, the workflows and the verifier in this repository.
Third-party software Omni-Compass runs on or connects to (Kubernetes, KEDA, Karpenter, NVIDIA drivers, databases) is
reported to its own maintainers.

### K.3 How Omni-Compass is built to fail safe

- The governor issues control actions only through the shield (`omnicompass/shield.py`, `cpp/src/shield.cpp`), inside the
  cover the operator granted, and never fights another writer.
- It snapshots every setting once, before its first write, and the kill switch (`python3 tools/omni_switch.py off`) hands
  every setting back; a dead-man lease hands them back if the governor stops.
- It runs under least privilege: on Kubernetes, a service account with `kubectl auth can-i` receipts for what it can and
  cannot do (`deploy/kind/rbac-omni.yaml`).
- The watchdog acts only on registry records its own user wrote that no other user can change, and never signals a
  process number the system gave to another process (`tools/omni_switch.py`). Put the switch and the registry in a
  directory only the governors' user can write (`OMNI_MASTER_OFF`, `OMNI_REGISTRY`); `status` warns when they are not.
- It contains no telemetry and makes no network connection of its own except to the systems an operator points it at.
- The threats of misuse, the guards against each and what is still open are set out in `docs/THREAT_MODEL.md`.
- Every release carries a software bill of materials (`sbom/`) and a seal of the engine and its twins (`results/SEAL.json`,
  `python3 verify.py`).
- The capture script (`fleet/capture/kube_capture.sh`) is read-only; no component writes to a live cluster unless the
  operator starts it in a writing mode.

## Appendix L. The Page Word for Word: Every Section, Monitor and Knob



This appendix is the live engine page itself, written from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build of this book (`docs/book/build_live_manual.py`): every section in the page's own order with its number, title, summary and controls line; every monitor under the number its badge carries, with its evidence class, its state, the open-source feed that would carry it on a running system and its knobs; every knob; and every LOSS row with whose it is, its cause and the knob that answers it. Nothing here is typed twice: what the page says, this appendix says, so the book and the page read each other both ways. This edition was written from the page built 2026-10-24 15:20 UTC on omni-v18 (digest 1cb92edb64c4391d) from commit 1aa4ebd3855c.


Each part below is one section of the page, in the page's order and under its number: what the page says it is, its controls, its panels, and every monitor in it under its own number, with what it shows, its evidence and state, the feed that would carry it live, its knobs, how to read it and what to do with it.

### L.1 ii Title page and build

**The page, in its own words.**

A live monitor of the Omni-Compass engine and of every benchmark GitHub has run on it: each run played back from its own SHA-256-checked files, each model run by the repository's own code, so the engine can be watched moving instead of only read. Two sides everywhere today: Native, the whole system running by itself, and Omni-Compass and native, the same system with Omni-Compass on top of all of it; the third, Omni-Compass by itself (each muscle's own native controller switched off, Omni-Compass the only controller on its knob), joins every table where native is a controller that can be switched off (on Kubernetes and in our models) once the engine that carries it lands and its runs are in; where native is a setting, or its own loop is the actuator, the two Omni-Compass arms are one, and the cloud waits for the founder's word (docs/SOLO_PREREGISTRATION.md). Beside this title stand the owner's two pictures, the stacks Omni-Compass sits on top of and the control authority, each with the engine's live marks over it. It is laid out as a book, read from the top down: this title page first, then the problem and the answer, what the whole industry faces and how Omni-Compass addresses it, then the executive summary and the reading key, then the table of contents, then the monitor wall with the control panel and the kill switch, every monitor at once with its number and its knobs, then the benefit board, then the whole organism composed every way it is bought, then every part from the whole down to the smallest: the measured effect in full, the evidence by stack from the cloud down to the chip, the organism and its muscles, the control console, the brain and its verdict, the failure modes, the component specification, and this page's own rendering. The disclosures close it. The engine that stands is omni-v18: omni-v17 with Omni direct taken into the engine, the seven files of Omni-Compass's own orchestrator that hold its rules fingerprinted like every other wire, and every organism the orchestrator runs shown three ways, native, Omni on native and Omni direct (section L.15, docs/OMNI_V18.md); omni-v17 was omni-v16 with its full decision, the heartbeat, every 60 s by default and a dial from 5 to 120 s, each beat shown beside native with what it buys and what it costs (section L.14), and the cruise wait never under two readings (docs/OMNI_V17.md); omni-v16 was omni-v15 with every clock of the Kubernetes governor in seconds, so its decision period changes only how often it looks (at 60 s every value is omni-v15's); omni-v15 was omni-v14 with the brain's request for the power cap trimming only while the response line has been clean for the governor's own clear time, and every wire that holds a governor's rules inside the fingerprint (docs/OMNI_V15.md). Before it, omni-v14 was omni-v13 with a knob that leaves any muscle native, never written, and the operator's own commands run without a shell (docs/OMNI_V14.md); and omni-v13 fixed one fault found on its own runs: on a shared host at its top, while another workload there has room of its own, the governor's conveyance hands every processor limit it gave back to the operator's, and it counts every other pod by what it may use (docs/OMNI_V13.md). Before that, omni-v12 fixed two faults found on omni-v11's runs. A processor-limit raise that the cluster's admission refuses is held until the pod's limit changes, the raise shrinks or a wait passes; omni-v11 wrote it again at every fast check. The swarm's proximity reflex hands back the planner's cruise in the tick it is triggered. omni-v11's guard stays in it: a reading that shows no machine in service is blind, and nothing is decided or written from it.

THIS PAGE IS A LIVE TUNING ENGINE. THE BENCHMARKS ARE ONE TUNED ENGINE. Every knob, button and monitor on this page can be turned in real time: the heartbeat from 5 to 120 s, the dial between the max and the tune-down, the pedal, each muscle driven or left native, up or down, in or out, minus or plus, to see and produce the variations of the mechanism of action with native alone, with Omni-Compass on top of native, or both side by side. Like any engine, where turning the mixture, the intake, the exhaust, the firing or the pistons changes what it delivers, turning any knob can change every metric, up or down, in any direction a tuner chooses: that range is the engine's versatility, one engine for many vessels, tuned many ways, for many outputs. What the page shows at any setting other than the factory tune demonstrates that range and is never a benchmark result. Every benchmark result is one engine at its one factory tune: the engine its table names, every benchmark run again on the engine that stands (section L.13). From omni-v17 the factory tune is chosen by a declared rule: of the tunes that harm no gauge against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on development seeds and read again on untouched ones (docs/THE_TUNE.md; DISCLOSURES.md, section L.17). A tune other than the factory tune is the tuner's own, and its results are its own.

DISCLOSURE: REAL RUNS, A REAL ENGINE, NOTHING HARDWIRED. Every run played back on this page (sections L.22 and L.23) is read from the raw files of benchmark runs executed on GitHub's own machines, each file checked against its run's SHA-256 list before a single number is drawn; every three-run table is read as the repository holds it, each naming its runs, and the raw branch holds their folders as they are archived (a table whose folders are not yet there says so in section L.13). Every model view runs the engine's own code (the compass law, the brain, the verdict) live in this page, linked through software to the repository's Python and C++ and checked against them on every build. GitHub rebuilds the page from the repository whenever the engine, a model or a result changes, and every three hours: no number on it is typed in by hand, and when the repository changes, the page changes with it.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.2 iii The problem and the answer: what the whole industry faces, and how Omni-Compass addresses it

**The page, in its own words.**

In one paragraph. What every stack faces: capacity built and left idle, controllers that react after the line is crossed and work at cross purposes, demand outrunning power and hardware. What Omni-Compass does about it: a supervisory governor on top of every native controller, never in its place, every muscle driven to its own limit and never past it, reactive and proactive like an immune system. Where the proof is (the three-run tables, the receipts, the runs played back on this page), what is not claimed, and what is protected.

**Read the whole section: what the industry faces, what Omni-Compass does, where the proof is, what is not claimed, what is protected (about three printed pages)**

**What the whole industry faces**

More demand than capacity. Demand for computing is growing faster than the power, the machines and the budgets built to carry it. The International Energy Agency puts the world's data centres at about 415 TWh of electricity in 2024, around 1.5% of all the electricity the world used, and expects that to more than double, to about 945 TWh, by 2030, with artificial intelligence the largest driver. In the United States, Lawrence Berkeley National Laboratory counts 176 TWh in 2023, 4.4% of the country's electricity, and between 6.7% and 12% by 2028. The usual answer is to build more: more machines, more megawatts, more cooling and a larger bill.

Much of what is built sits idle. Across the Kubernetes clusters Cast AI measured in 2025, the average processor was 8% busy and the average memory 20% used, read before its own automation was switched on. The organizations Flexera surveyed estimate that 29% of what they spend on cloud infrastructure and platforms is wasted.

Not short of control, short of coordination. In every realm (compute, AI and the cloud; physics, robotics and autonomy; energy, facilities and industry; distribution and specialized systems) each machine already runs under local feedback loops: horizontal autoscalers, firmware power and clock governors, building-management loops, battery-management systems, connection pools, servo controllers. Each loop is tuned on its own, against its own setpoint, with margins sized for a worst case. Four costs follow, and every operator pays them:

Reaction latency. Reactive loops act on lagging, averaged signals. A Kubernetes Horizontal Pod Autoscaler recomputes its replicas every 15 seconds by default and damps its scale-downs over a 5-minute stabilization window; new pods then need time to schedule and start. Queues form before capacity arrives.

Static over-provisioning. Worst-case margins persist through the far more common nominal regime. The operating point sits well inside the safe region, and the headroom between it and the constraint boundary is paid for and rarely used.

Uncoordinated coupling. Loops share resources: power, cooling, connections, memory, network. One loop's correction is another loop's disturbance: more web replicas saturate the database's connections; more cooling pushes a power feed toward its limit.

The gaps closed by hand. Operators close them with fixed settings, runbooks, alerts and on-call rotations, and the settings go stale as the load moves. That is safe, and it leaves the region between the operating point and the safe boundary unused nearly all of the time.

**Omni-Compass's solution: govern what is built before building more**

Omni-Compass is a supervisory governor. It sits on top of every native controller and never in place of one; native keeps running underneath, always. It treats each setting a native controller already exposes (a replica floor, a power cap, a clock ceiling, a temperature setpoint, a pool size) as a muscle, and the whole stack as one body, the organism. Through a two-way plug, one wire in (the readings native already reports) and one wire out (the settings native already exposes), it reads every muscle, places each reading in the muscle's own band, from calm to its line (the limit it must not cross: a response time, a temperature, a feed's rating), and moves each setting one bounded, smooth step at a time. By default every muscle is driven up to its own limit, never past it and never below native; every write is read back; every give-back is tried in its own paired trial (the muscle with and without it, under the same load) and undone if the muscle loses by it; a raise is held inside the muscle's own bounds and judged afterwards by the three-run tables; and wherever no gain can be brought, the muscle stays native. One brain governs the whole body, so a step on one muscle stands only while every muscle it couples to stays inside its own cushion. The aim, in one line: more work, faster, on fewer machines, with less energy. Where Omni-Compass takes more energy to buy more work or speed, that energy is shown beside what it bought, as power given, and never called a loss.

**How it addresses each cost**

| What the industry faces, and what it costs | How Omni-Compass addresses it | How it is judged |
|---|---|---|
| Reaction latency: waiting, queues and time over the line before capacity arrives | it reads every muscle on its own clock (on Kubernetes its full read of the state every 15 seconds, the autoscaler's own pace, and its fast checks every 5 seconds) and moves as a reading nears its line, not after the line is crossed: proactive as well as reactive, like an immune system | time waited, missed or failed: a fall is GAIN, a rise is LOSS |
| Static over-provisioning: machines, energy and a bill paid for headroom rarely used | every muscle driven up to its own limit and never past it, so the machines already paid for carry more work; in a public cloud it parks only a machine the cloud already made, after its own trial, and wakes it on a breach, so the bill can only fall or stay | work done: a rise is GAIN; machines, energy and the bill: a fall is a cut, a GAIN, and a rise is power given |
| Uncoordinated coupling: one loop's correction is another loop's disturbance | one brain for one body: a step on one muscle stands only while every muscle it couples to stays inside its own cushion | every muscle judged on itself, and the organism judged whole |
| The gaps closed by hand: settings retuned by hand, alert minutes, on-call | an autopilot: every write read back, every give-back on its own trial, every reason written to its audit; an alert minute on Omni-Compass's side is found and fixed, never accepted | the alert minutes, judged; the settings commands it wrote on its own, shown |

Where this page shows each answer. Reaction latency: the organism live, every muscle's place in its band and the decisions past the line, native beside Omni-Compass (6a), and the shipped controller's decision trace (5e). Static over-provisioning: the benefit board (2) and the clouds' bills (5a). Uncoordinated coupling: the whole organism (3) and the organism's immune system (6a). The gaps closed by hand: the status board's alarms (1d) and the golden signals, the event log and the live metrics (1h).

What it does not do. It replaces no controller, and it creates no capacity a machine does not have: it uses the capacity already there, each muscle to its own limit. It promises no number on a system it has not run on: the only number that applies to a system is the one that system's own paired runs produce. The outside figures above are their authors' own, quoted for scale; none was measured, checked or endorsed by The Omni-Compass LLC, and none is a result of Omni-Compass.

How it is held to account. Every benchmark has two arms, native and Omni-Compass on top of native, on the same machines with the same work, run three separate times. Every reading is one word, GAIN, EVEN or LOSS, decided by what the gauge is for (the key, in the next section); every result carries its evidence class (P a physical meter, L live software, S our own models, never shown as proof of hardware); and every row is shown, LOSS included. The governing rule is do no harm, in its one meaning (DISCLOSURES.md, section L.17): the aim is an organism never left turning out less than native, nor less healthy; where a row reads LOSS against native (section L.11 lists each, 7 today), the row stays, its cause is found and fixed, and the test runs again. The executive summary under this section reads where the record stands, from the records on this page.

The outside sources. International Energy Agency, Energy and AI (April 2025), its executive summary. Lawrence Berkeley National Laboratory, 2024 United States Data Center Energy Usage Report (December 2024), prepared for the U.S. Department of Energy. Cast AI, 2026 State of Kubernetes Optimization Report: a seller of Kubernetes optimization, reporting its own customers' clusters as they ran before its automation. Flexera, 2026 State of the Cloud Report (March 2026): a survey of 753 cloud decision-makers and users, the figure their own estimate. The Kubernetes documentation, Horizontal Pod Autoscaling: the controller's defaults.

**Its monitors.** This section draws no canvas: it is words and their sources, written in the page itself.

### L.3 iv Executive summary and reading key

The Omni index, every real test weighed together: the record loads below.

**Controls.** Live: the buttons act on the live engine; every number below is read from the records on this page.

**The page, in its own words.**

In one paragraph. Two sides everywhere today: native, the whole system by itself, and Omni-Compass and native, the same system with Omni-Compass on top of all of it; a third, Omni-Compass by itself, joins when the engine that carries it lands and its runs are in. Three words, by the one key: GAIN, EVEN and LOSS, with power given for a resource that rose, each number beside a word carrying the word's sign. Three classes of evidence: P a physical meter, L live software, S our own models, never proof. The figure of record is the Omni index, every real test weighed together.

**Read the whole section: the executive summary, the key, the terms, the examples (about two printed pages)**

**Executive summary**

Every number in this list is read from the records on this page when it opens (the three-run tables, the Omni index, the cloud ledger, the card run, the models' own readings, the realms table and the harness); none is typed in. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**The key: GAIN, EVEN and LOSS**

**The terms this page uses, each defined once (the first time a term appears on the page it carries the same definition, shown when pointed at)**

The size is how far the gauge moved from native; the word says whether that move helped the work. Examples, read from the three-run tables on this page, appear here when they load. A miss is a decision where the work went over its line. The key is written once in tools/readings.py and stands at the top of the README, the reading guide and both manuals. GAIN, EVEN and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results; the underwriting senses explain the words and are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.4 Part 1 of the page: The monitor wall and the control panel

### L.5 The control panel and the kill switch: one switch for the whole organism, the Python's runs, the three manuals

The first view after the front matter: the control panel that drives every monitor of this page. The kill switch stands at its head, ON in green while Omni-Compass governs on top of native, red when engaged, and Omni-Compass OFF in white; the Python's own runs can be run again here at a button; the three manuals are a click away. The monitors it drives follow: the wall of every monitor (1b), the numbered list of them (1c), the status board (1d), the master switch's wiring (1e), the Python's runs in this page (1f), every LOSS row (1g), the golden signals (1h) and GitHub's pipeline (1i). No value here is typed in: each is computed at runtime from the live engine or from the repository's records embedded at build time.

**Controls.** Live: the kill switch acts at once on every governor of this page; the buttons run the Python's runs here and fetch the three manuals.

**The page, in its own words.**

**The control panel: one switch for the whole organism, the Python's runs in this page, the three manuals**

The kill switch. While Omni-Compass governs on top of native the switch reads ON in green. Pressed, it turns red: at the next decision every governor puts every setting it wrote back, reads each one back and stops (omnicompass/master.py, tools/omni_switch.py); the word OFF stands white, and every Omni-Compass side of every monitor follows native, drawn in native's colour. Native's own controllers under every muscle never stop and never see the switch. A recorded result never changes with it: its colour does, never a value, a word or a row. The same switch stands at the head of every section and in every monitor's own knobs; one press anywhere is one press everywhere. It is for security and is instant; the walk back after a crash is the lease, separate.

The three manuals. The Live Engine Manual reads this page top to bottom: how to read, operate, tune and watch it, native beside Omni-Compass, chapter by chapter in the page's own order, and, in its last appendix, the page word for word, every section, every monitor under its number and every knob, written from this page at every build. The Operator's Manual wires and runs Omni-Compass on a stack; the Owner's Manual holds the whole mechanism, its mathematics, its source and every result. Each carries the notice, the LICENSE, the NOTICE and DISCLOSURES.md.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.6 The monitor wall: every monitor, numbered 1 upward in its order of appearance, read left to right

Every monitor of this page at once, numbered in the order it appears from the top, 1 first, and read left to right, then the next row, as any page is read; the last number is the last monitor on the page. Two monitors that sit side by side in their section, native beside Omni-Compass, stay side by side on the wall. Each tile carries at its top its number and its title, what the monitor shows, with its section and its state under them; the numbered list beside it (1c) says the rest.

**Controls.** Live: click a tile to go to its monitor; every tile is read again four times a second.

**The page, in its own words.**

**The monitor wall: every monitor of this page, numbered 1 upward in its order of appearance, read left to right, then the next row; click a tile to go to it**

The same canvases the sections draw, copied small four times a second; nothing is drawn twice from different data. The page's own governor (section L.39) leaves a monitor resting while it is off screen, so while this wall is in view the resting monitors are drawn in turn, one a frame, each through its own drawing code; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to. Two monitors that sit side by side in their section, native beside Omni-Compass, sit side by side on the wall too: a pair never splits across two rows. Each tile's head is its number and its title in capital letters, then its section and its state (live, replay, from the records, a model, or awaiting its run). A tile with the accent border is a monitor on screen now; the list of every monitor by its number follows in section L.7.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.7 The monitor list: every monitor by its number, what it shows, its section and its feed

The list that goes with the wall: every monitor by its number, in the same order, with what it shows, the section it lives in, its evidence class and state, the open-source feed that would carry it live and its knobs. Read the wall, find a number, read its line here.

**Controls.** Recorded data: the list is the page's own registry of its monitors, read when the page opens; click a number to go to its monitor, a section to go to its section.

**The page, in its own words.**

**Every monitor by its number: what it shows, its section, where its numbers come from, the open-source feed that would carry it live, its knobs, and what is still awaiting its run**

The motion meter: every monitor in view is photographed small once a second, as you see it, and its badge says whether it moved.

Every monitor is one canvas on this page; its number is its order of appearance from the top, and the wall (section L.6) reads them left to right, then the next row. The feeds name the open-source exporters an operator's Prometheus and Grafana already run (node_exporter, kube-state-metrics, the NVIDIA DCGM exporter, Kepler, OpenCost, the governor's own tools/omni_exporter.py); the button in the control panel downloads the whole wall as a Grafana dashboard on those series (deploy/grafana/omni-compass-wall.json, written from docs/engine/monitors.json), beside the governor's own screen (deploy/grafana/omni-compass.json). A monitor the page draws from the repository's tables, or from its own clock, says so: no series carries it.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.8 The status board: the tiles, the alarms and the watch items

Whether Omni-Compass is engaged, which signals are out of tolerance and where, and every LOSS row raised as an alarm with its source record. Each tile and each alarm is computed at runtime from the live engine or from the repository's records.

**Controls.** Live: the filters act at once, and every tile is read again four times a second.

**The page, in its own words.**

**Alarms and watch items, by severity**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.9 The master switch's wiring: the switch above the brain, the brain above the organism, every muscle under it

One switch for the whole organism, drawn as the repository wires it: the master switch holds the brain's outputs; the brain sits above the organism; every muscle hangs under it with native's own controller under every muscle, never switched. Every governor of this page is listed with its state at the switch.

**Controls.** Live: the switch on this monitor is the kill switch of section L.5.

**The page, in its own words.**

**The master switch, wired at the top of the organism: switch, brain, organism, every muscle**

One switch for the whole organism, as the repository builds it (omnicompass/master.py, tools/omni_switch.py). It sits at the top and holds the brain's outputs. With it OFF, nothing the brain computes is pushed or pulled into any muscle, and every muscle runs on native's own controllers, which never stop. On a real machine every governor exits at the switch; on this page the brain keeps reading the native body in shadow, so its monitors keep moving, and nothing it computes leaves it. No monitor is switched off: every Omni-Compass side follows native, drawn in native's colour. Every governor on this page is registered with it and obeys it at once. The live organism hands every setting it held back to native's own controller and reads each one back. Every record's Omni-Compass side, and every playback, trace, table, board and grid, reads native's own. Native's own controllers sit under every muscle and are never switched, so native's side never moves with it. Every section carries the same switch in its controls bar; pressing any one of them throws this one.

**Its monitors.**

#### L.9.1 Monitor 1: The master switch and the kill switch

The switch above the brain: ON, Omni-Compass governs every wired muscle; engaged, every setting is handed back to native's own controller at once and every Omni-Compass side on the page follows native.

- **Evidence and state.** Class S (the page's port of the master switch; the real one is omnicompass/master.py); live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_master_switch`; on a running system: `omni_master_switch`.
- **Wired.** This page's `drawMaster, masterSet` → the Python `omnicompass/master.py`, `tools/omni_switch.py`, `omnicompass/nervous_system.py` → the C++ `cpp/src/nervous_system.cpp`; held equal by `tests/test_master_switch.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** Every decision: the brain's pulse and the work flowing down to every muscle; the switch acts at once.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The wiring from the top down: the master switch above the brain, the brain above the organism, the organism above every muscle, and native's own controllers under every muscle, never switched. The switch's state is the word on it: ON in green while Omni-Compass governs; engaged, the switch red and OFF in white.
- **What to do with it.** Press the kill switch only for security: it is instant, every setting goes back to native and is read back. Watch the governors' table beside it: every governor on the page says OFF and what it handed back.

### L.10 The Python's runs, in this page: the jump generator's runs recomputed here, the 500 scenarios replayed

The Python's runs, the C++ harness's and this page's, run by run: the jump generator's set GitHub ran in the Python (its run linked), the same draws run through the C++ harness on the engine's C++ twins, and the same set recomputed here by this page's own port of the engine as the page opens; every receipt compared three ways, one SHA-256 digest each, and the digest of the draws themselves; and the Python's 500 scenarios a seed replayed from its own record with every trace hash.

**Controls.** Live: the runs start on their own when the page opens; the buttons run them again, run a new set from any base, print them and save the receipts.

**The page, in its own words.**

**The Python's runs, in this page: the engine's seeded runs recomputed here, and the 500 scenarios replayed**

How the three prove each other. tools/engine_runs.py runs N runs from a base seed: run k's seed is base + k·0x9E3779B9 mod 2³² (the jump generator), its stream mulberry32 (this page's own generator, written in the Python bit for bit), through the engine that stands: 288 decisions of the brain's state equations integrated by the fourth-order Runge–Kutta step, 80 steps of the compass law and one give-back trial judged by the verdict. Each run's receipt is its final state, its pushes and grants, the law's mean and last force and the trial's answer; the digest is the SHA-256 of every receipt at six decimals. The Python writes every draw of every run, the injection, and the C++ harness (cpp/tools/engine_runs.cpp) reads it as its input, puts the mechanism on through the engine's C++ twins and writes every receipt: its digest must be the Python's. This page runs the same N with its own port of the engine (proven equal to the Python and the C++ to 1e-12 on every build by docs/engine/check_live_engine.py) as it opens and compares every receipt and the digest. GitHub does all three on every set it runs (.github/workflows/engine-runs.yml) and on every push (verify.py); run the Python again with another base and it writes another set, and the three digests must be one.

**Its monitors.**

#### L.10.1 Monitor 2: The Python's runs, reproduced here

The engine's seeded runs: the Python's receipts (results/engine_runs) beside the same runs computed by this page's own engine, run by run, with one digest each.

- **Evidence and state.** Class S (the engine itself); live.
- **Feed.** tools/engine_runs.py (the Python) and this page.
- **Wired.** This page's `drawProof, engineRuns, proofRecheck` → the Python `tools/engine_runs.py` → the C++ `cpp/tools/engine_runs.cpp`, `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `verify.py`, `tests/test_engine_runs.py`, `.github/workflows/engine-runs.yml`.
- **Moves.** The page recomputes one run of the Python's set from its own seed about twice a second, round after round, and holds its receipt against the Python's.
- **Knobs.** Runs: how many of the Python's runs this page computes again; Print: the receipts of the runs, printable, with the digests and the notice.
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

#### L.10.2 Monitor 3: The Python's 500 scenarios, replayed

benchmarks/stack_benchmark.py's 500 scenarios a seed base (the two held-out seeds), each through every arm, replayed from its record scenario by scenario with every trace hash and the file's SHA-256; verify.py replays them on every push.

- **Evidence and state.** Class S; replay.
- **Feed.** benchmarks/stack_benchmark.py (results/heldout_seed_*/RUNS.csv).
- **Wired.** This page's `drawHeld` → the Python `benchmarks/stack_benchmark.py`, `omnicompass/adapter.py`, `omnicompass/shield.py`, `omnicompass/stack_sim.py`, `docs/engine/export_heldout.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`; held equal by `verify.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`.
- **Moves.** The 500 scenarios replayed one after another from the record, every scenario's trace hash with it.
- **Knobs.** Seed base: which held-out seed base's 500 scenarios are replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Gauge: which gauge of the run is shown; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

### L.11 Every LOSS row: its cause and the knob that answers it

Every LOSS row of every three-run table on this page, Omni-Compass's own first and then the orchestrators' own, each with the cause the repository records and, where that cause is the governor's, the knob that brings it EVEN or leaves the muscle native; where the cause is the test machine, or not yet established, the row says so and asserts no knob. No row is cut and no number is tuned.

**Controls.** Recorded data: every row is read from the three-run tables on this page.

**The page, in its own words.**

**Every LOSS row: its cause and the knob that answers it (Omni-Compass's own rows first, then the orchestrators' own cost)**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.12 The golden signals, the event log and the live metrics

The live organism's four golden signals, native beside Omni-Compass, one point a decision: errors (muscles over the line), throughput (work served), latency and saturation; the engine's own event log, newest first; and the same metrics in the OpenMetrics format Prometheus scrapes and Grafana charts.

**Controls.** Live: one point a decision from the live engine; the event log's filters act at once; the metrics refresh every two seconds.

**The page, in its own words.**

**Golden-signal feed, live: the last 240 decisions, native beside Omni-Compass**

One point per decision streamed from the live engine, gapless, each signal on its own axis, with each arm's last, mean and maximum as a time-series dashboard reports them; a kill-switch window is shaded red. Native in amber, Omni-Compass in blue, the same demand on both.

**Engine event log, newest first**

The live engine's own events as it emits them, with the wall-clock time and the decision. They are a threshold breach and its clearing on either arm, every injected fault and its end, the kill switch, the dial, a new day, and the brain's calm crossing the grant threshold. ALERT, WARN and INFO as an operations log grades them.

**OpenMetrics exposition: the live metrics, ready for Prometheus and Grafana**

The live engine's metrics in the OpenMetrics text format, the CNCF exposition format Prometheus scrapes and Grafana charts, refreshed every two seconds. They are engagement, the decision index, breaches, work, band time, actuator moves and reversals per arm, and frame time. Then the verdict's keep ratio at each true cost, the three-run tables' rows by class and reading, and the build's engine, digest and commit.

The board is laid out the way an operations monitor is. The switch and the engine come first. Next come the live organism's signals, native beside Omni-Compass, in the four a service is watched by (site reliability practice: latency, traffic, errors and saturation): here the work waiting, the work done, the decisions past their line and the capacity held. Then every reading of the real and modelled runs that went against native, worst first. Last come GitHub and the age of this page. A tile's word is its reading against native by the key (front matter, iv). A tile with no reading says what it shows.

**Its monitors.**

#### L.12.1 Monitor 4: Golden signal: errors

Errors a decision on the live organism, native beside Omni-Compass (site reliability's first of four).

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client), kube-state-metrics for pod restarts; series `http_requests_total{code=~"5.."}`, `kube_pod_container_status_restarts_total`; on a running system: `sum(rate(http_requests_total{code=~"5.."}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live engine: native in amber, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

#### L.12.2 Monitor 5: Golden signal: throughput

Work done a decision (traffic), native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client); series `http_requests_total`; on a running system: `sum(rate(http_requests_total[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live engine: native in amber, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

#### L.12.3 Monitor 6: Golden signal: latency

Response time a decision, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own duration histogram; series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live engine: native in amber, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

#### L.12.4 Monitor 7: Golden signal: saturation

Capacity held against capacity used, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** node_exporter; series `node_cpu_seconds_total`; on a running system: `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live engine: native in amber, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### L.13 CI pipeline: GitHub Actions runs in progress and queued

Every GitHub Actions workflow run in progress or queued at build time. The hardware and cloud runs, with their terminal status, are in sections L.20 and L.25; every run on the engine that stands that terminated without a measurement is raised on the status board (section L.8).

**Controls.** Recorded data: GitHub's runs as read when the page was built.

**The page, in its own words.**

**GitHub Actions, as a monitor: the runs in flight, the Azure set's repetitions, the clouds' gates, the chips**

Read at the build from GitHub's own API: a workflow's running runs in solid blue, its waiting ones pale; the Azure set to the paid cap with its repetitions measured so far (the table is written when the set ends); each cloud's hourly gate with the reason its own job wrote. Live, the same lives in the open-source github-actions-exporter for Prometheus.

**Workflow runs in progress and queued**

The page is rebuilt by GitHub itself (.github/workflows/live-engine.yml, docs/engine/build_live_engine.py) whenever the engine, a model or a result changes, and every three hours. Every record is made again by the repository's own code on the engine that stands, checked against the Python and the C++, and committed. This table is GitHub's own list at that moment.

**Its monitors.**

#### L.13.1 Monitor 8: GitHub Actions: the runs in flight

Every workflow run in progress or queued when the page was built, the Azure set's repetitions done of its cap, and the clouds' gates.

- **Evidence and state.** Class L (GitHub's own API, read at the build); record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter; series `github_workflow_run_status`, `github_job_duration_seconds`; on a running system: `sum by (workflow) (github_workflow_run_status == 1)`.
- **Wired.** This page's `drawCi` → the Python `docs/engine/build_live_engine.py` → the C++ none: GitHub's own record of its runs, read from its API at the build; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the workflows, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** GitHub's runs in flight at the build by workflow, the Azure set's repetitions measured, each cloud's gate with its reason, the chips' runs.
- **What to do with it.** A gate that holds names its fix in its own words; nothing is billed while it holds.

### L.14 The heartbeat dial: every beat beside native, what it buys and what it costs

The governor's heartbeat, its full decision, is a dial from omni-v17 on: the main engine decides every 60 s, and any beat can be set, 5, 15, 30, 60, 75, 90 or 120 s or any value between, with the fast checks (the scheduling floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat. Every clock of the governor counts seconds (omni-v16), so turning the dial changes only how often it looks. Each beat stands beside native with what it buys (the reads of the cluster a day) and what it costs (the governor's own processor, and every service row read against native and against the main engine's 60 s), because an operator may want a fast beat for its reads and accept what it costs, or a slow one. At each beat the other knobs may want their own combination; that tuning is the next study, in the toy first. The governor's own screen counts the time since its last decision in beats of the setting it runs at and alerts after three (omni_heartbeat_seconds, deploy/grafana/omni-compass.json, deploy/prometheus/omni-compass-rules.yaml).

**Controls.** Recorded data: every beat of the Kubernetes governor read in our own models (class S, results/toy_gate/V17_LADDER.json, tools/beat_ladder.py); the real runs at every beat (docs/PACE_PREREGISTRATION.md, amendment 3) join their place when their three runs land. The beat itself is set on the governor's command line (--interval) or with the control panel's heartbeat button (POST /v1/beat, tools/omni_control.py: one button for each stop of the dial), which hands every setting back and starts the governor again at the new beat.

**The page, in its own words.**

**Every beat, in our own models**

How to read it: each value is the beat's mean over seeded days on a plant that moves every 5 s, the same seeds and plant at every beat; the word beside it is its reading against native, paired by seed (GAIN, EVEN, LOSS, power given: the key at the top of the page). The second table reads each beat against the main engine's 60 s. Native has no governor, so its reads and processor are blank. The reads are what a beat spends to look more often, shown as the key reads a resource spent: power given. A LOSS here is the engine's at that beat and stands with every other LOSS row (1g).

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.15 Omni direct: the three arms, native, Omni on native and Omni direct

From omni-v18 Omni direct is part of the engine: Omni-Compass's own orchestrator runs the organism with no Kubernetes beneath it, and every organism is shown three ways. Native is Kubernetes' published autoscaling rule on the muscles, written by us, every machine on and the units spread. Omni on native is Omni-Compass on top of that rule: the rule's units and never fewer, Omni's reflex and fail-up above them, its conveyance (each unit's processor wall raised into the room its machine can spare under 75% busy), the busy room rule, packing and the machines parked and woken on top. Omni direct is Omni-Compass alone on the muscles: all of that, and a unit fewer than the rule's count tried under the verdict on the service's own response times and kept only where it reads no LOSS within 2%; a trial the traffic keeps abandoning holds the next one off, and work waiting in line hands a step back at once. Every pair is read by the one key, paired by step.

**Controls.** Recorded data: the showing's own record (results/orchestrator/, gathered by tools/orchestrator_record.py from the files tools/orchestrator_show.py wrote), one run of each arm, class L. The arm buttons choose the arms drawn; the step slider walks the run step by step, and every monitor's light reads the step it stands on. The master switch shows native alone. On a real machine each arm is the control plane started with its brain (python3 -m omni_orchestrator.control --brain yardstick, omni_native or omni), and its kill switch is the control plane's kill file: the brain off, the declared state held, every conveyed wall handed back.

**The page, in its own words.**

**Work: requests answered each step**

**The 95th percentile response each step**

**Units serving each step**

**Machines on each step**

**Every pair, read by the one key**

**Three runs on GitHub's machines (A, B and C from one commit)**

How to read it: each word is the pair's reading by the gauge's aim (the key at the top of the page), from the mean of the step-by-step differences and its 95% interval on Student's t; the direction follows the word in words. Work aims up; the 95th percentile aims down; units and machines are resources, so a fall is a cut, a GAIN, and a rise is power given. The amber line on native is the native arm drawn; Omni-Compass's arms are blue, Omni on native dashed and Omni direct solid. The tables above are one run of each arm on one host (the quick form); the three-run table under them is the full form on GitHub's own machines, A, B and C from one commit, combined by the one rule: GAIN, LOSS or power given in all three when every run's interval is clear of zero on the same side, EVEN when any run's interval holds zero, the runs disagree when clear runs point different ways.

**Its monitors.**

#### L.15.1 Monitor 9: Omni direct: work each step

Requests answered each step by native, Omni on native and Omni direct, the same clients (1 2 3 2 3 4).

- **Evidence and state.** Class L; record.
- **Feed.** the showing's record (results/orchestrator/), from the control plane's timeline and the front's own answers.
- **Wired.** This page's `drawDirect, lampDirect` → the Python `omni_orchestrator/control.py`, `omni_orchestrator/brain.py`, `tools/orchestrator_show.py`, `tools/orchestrator_record.py` → the C++ Omni direct's brain is Python (omni_orchestrator/); it has no C++ twin yet; held equal by `tests/test_orchestrator.py`.
- **Moves.** The showing's record, replayed step by step with the step slider; the arm buttons choose the arms drawn; the master switch shows native alone.
- **Knobs.** Arm: which arm stands on the right: Omni-Compass governing, or watching only; One decision: step the engine one decision while paused; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).

#### L.15.2 Monitor 10: Omni direct: the 95th percentile each step

The 95th percentile response each step, the three arms, against the service's line.

- **Evidence and state.** Class L; record.
- **Feed.** the showing's record (results/orchestrator/), from the control plane's timeline and the front's own answers.
- **Wired.** This page's `drawDirect, lampDirect` → the Python `omni_orchestrator/control.py`, `omni_orchestrator/brain.py`, `tools/orchestrator_show.py`, `tools/orchestrator_record.py` → the C++ Omni direct's brain is Python (omni_orchestrator/); it has no C++ twin yet; held equal by `tests/test_orchestrator.py`.
- **Moves.** The showing's record, replayed step by step with the step slider; the arm buttons choose the arms drawn; the master switch shows native alone.
- **Knobs.** Arm: which arm stands on the right: Omni-Compass governing, or watching only; One decision: step the engine one decision while paused; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).

#### L.15.3 Monitor 11: Omni direct: units each step

Units serving each step, the three arms, against the service's most.

- **Evidence and state.** Class L; record.
- **Feed.** the showing's record (results/orchestrator/), from the control plane's timeline and the front's own answers.
- **Wired.** This page's `drawDirect, lampDirect` → the Python `omni_orchestrator/control.py`, `omni_orchestrator/brain.py`, `tools/orchestrator_show.py`, `tools/orchestrator_record.py` → the C++ Omni direct's brain is Python (omni_orchestrator/); it has no C++ twin yet; held equal by `tests/test_orchestrator.py`.
- **Moves.** The showing's record, replayed step by step with the step slider; the arm buttons choose the arms drawn; the master switch shows native alone.
- **Knobs.** Arm: which arm stands on the right: Omni-Compass governing, or watching only; One decision: step the engine one decision while paused; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).

#### L.15.4 Monitor 12: Omni direct: machines each step

Machines on each step, the three arms, against the fleet.

- **Evidence and state.** Class L; record.
- **Feed.** the showing's record (results/orchestrator/), from the control plane's timeline and the front's own answers.
- **Wired.** This page's `drawDirect, lampDirect` → the Python `omni_orchestrator/control.py`, `omni_orchestrator/brain.py`, `tools/orchestrator_show.py`, `tools/orchestrator_record.py` → the C++ Omni direct's brain is Python (omni_orchestrator/); it has no C++ twin yet; held equal by `tests/test_orchestrator.py`.
- **Moves.** The showing's record, replayed step by step with the step slider; the arm buttons choose the arms drawn; the master switch shows native alone.
- **Knobs.** Arm: which arm stands on the right: Omni-Compass governing, or watching only; One decision: step the engine one decision while paused; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).

### L.16 The benefit board: every domain, native against Omni-Compass

The first thing after the wall: every benchmark's measured effect in one board, native against Omni-Compass on top of native, by domain and by gauge family, and the Omni index that weighs them together. Every bar is its table's own word (GAIN green, EVEN yellow, LOSS red, power given blue) beside its size; every LOSS row stands on it and is raised on the status board (section L.8) and answered, with its cause and its knob, in section L.11. The whole organism composed from these same tables follows in section L.17; every table, every muscle and the grid in full in section L.18.

**Controls.** Recorded data: every receipt as the repository holds it. The kill switch recolours a recorded result and never rewrites it; console controls never modify it.

**The page, in its own words.**

**The benefit board: every domain, native against Omni-Compass**

**Where the benefit lives, gauge by gauge**

Every judged row of every newest three-run table (the tables below), sorted into the family of gauge it measures. A CTO reads speed, the service level, failures and work. A CFO reads machines, energy and the bill. A plant engineer reads peaks and swings, wear and accuracy, and misses. Each bar counts the rows that read GAIN in all three runs; the size beside it is the median of those rows' own sizes (the middle of runs A, B and C). Power given and LOSS rows are counted beside them.

**The trading floor: every three-run table on one screen, the market map and the quote board**

Every three-run table on this page (the tables of section L.18, as GitHub's runs wrote them) read the way a trading floor reads its market. The map: one tile a table, grouped by stack, its area the gauges it judged and its colour its reading: green GAIN, the deeper the more of its rows; red where any row reads LOSS; yellow EVEN; blue where it gave power; grey with a dashed edge an orchestrator's own cost, with no Omni-Compass in either arm. The board: one quote a table, its ticker and engine, the gauge that moved most with its mean change, and that gauge in each of the three runs (A, B and C) as a candle, the bar its 95% interval and the tick its value against the zero line; the strip under it counts the table's rows by word, and the tape runs every headline across the top. Point at a tile or a quote for its record. Nothing here is typed in: every figure is the table's own.

**Aggregate: one figure for the whole board**

**Its monitors.**

#### L.16.1 Monitor 13: The benefit board

Every domain's three-run table as one bar: GAIN, EVEN, LOSS and power given, native against Omni-Compass.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawBenefit, fxCursor` → the Python `tools/benefit_sheet.py`, `tools/omni_index.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the bars, one benchmark at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

#### L.16.2 Monitor 14: Where the benefit lives, gauge by gauge

The same tables by gauge family: work, speed, misses, resources.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawFam` → the Python `tools/benefit_sheet.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the families, one at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

#### L.16.3 Monitor 15: The market map: every three-run table a tile

Every three-run table on the page as a tile of a squarified treemap, grouped by stack: its area the gauges it judged, its colour its reading (GAIN green, LOSS red, EVEN yellow, power given the accent, an orchestrator's own cost grey and dashed).

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawTradeMap` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The scan cursor walks every tile, one every 1.5 s.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

#### L.16.4 Monitor 16: The quote board: every three-run table a quote

Every three-run table as a quote: its ticker and engine, the gauge that moved most with its mean change, that gauge in runs A, B and C as a candle (the 95% interval and the value), its rows counted by word, and a tape of every headline.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawQuotes` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The tape of the headlines runs across the top at 55 px a second.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### L.17 The whole organism, every way it is bought: on-site bare metal, through the cloud, in the device, as a service

Omni-Compass is wired into every piece of a stack through its own two-way plug: the software (the cluster: Kubernetes, its add-ons, its governors and orchestrators; and the services on it: the pools, the consumers, the caches), the bare metal under it (the chip's power limit and clock; the machine's kernel and its own meter) and, where the stack is rented, the cloud that bills the machines. A stack is bought one of two ways: on-site bare metal, the software on the owner's own bare metal (software × bare metal, no cloud); through the cloud, the cloud's build, its bare metal at the back end and the software (cloud × bare metal × software), with the cloud as two pieces beside it (cloud × software, the back-end bare metal left to the provider). The composition is read four ways (the Scenario knob): the two ways a stack is bought, and two more that take its pieces alone, in the device (the bare metal by itself) and as a service (the software by itself). Every piece's benefit is added into one collective reading, gauge by gauge (work, the 95th percentile response, machines, energy, the bill), with the receipts under it: what native spent, what Omni-Compass spent, and the benefit, in the units each table measured. The repository composes the layers in one place, tools/whole_system.py, which writes results/WHOLE_SYSTEM.md from the tables that stand: each layer measured against its own native with the layer under it as native runs it; a gauge's ratio oriented so that above 1 is a GAIN at every layer alike; the layers composed by the product law, R(g) = ∏ℓ Rℓ(g), log R = Σℓ log Rℓ (for small benefits the product is their sum), every interval carried (the exact Student t per run; A, B and C pooled by inverse variance; the layers' variances added); two readings of the same numbers (every measured piece: everything measured enters with its interval; the strict reading, the index's rule: only what held the same way in all three of our runs, everything else exactly 1); and the separability assumption tested on the governors' four ways. This section recomputes nothing from the tables: it regroups that file's layers into the two ways (docs/engine/export_whole.py), summing the logarithms of the layers a scenario stacks and adding their variances, as the file's rule composes any set of layers; the one number is the mean of the gauge logarithms, its 95% interval under the file's two bounds. The composition is a model (evidence class S) of class P and class L measurements under the separability assumption, and says so; no run has yet stacked every layer at once, and that stacked run is the measurement that would replace it. The chip's one measured run (2 October, on the card controller since replaced) stands beside the count by default, every row of it shown, as the repository's own headline has it; one click puts it in, until its run on Lambda on the engine that stands replaces it. The machine (the kernel, bare metal, Kepler) is not yet run and enters as exactly 1, named. GAIN is green, LOSS red, EVEN yellow, power given blue, on every word, cell and tile.

**The page, in its own words.**

The third arm, Omni-Compass by itself. Every composition on this page is bought two ways today, native and Omni-Compass and native. The founder's order of 23 October adds a third wherever native is a controller that can be switched off: Omni-Compass by itself, the muscle's own native controller switched off and Omni-Compass alone on its knob (docs/SOLO_PREREGISTRATION.md). Its column appears here from its first run on GitHub's machines, read from the raw files like every other; nothing is written for it before then.

DISCLOSURE: THE CLOUD'S BACK END IS NOT OURS TO METER. Through the cloud, the bare metal at the back end belongs to the provider: no tenant can read its power meter or write its chips' limits, so no run here reaches it. What a tenant can measure is what the cloud meters and bills: the machines it counts every fifteen seconds and the bill at list price (section L.20); that difference, native against Omni-Compass on top of the cloud's own autoscaler, is the cloud piece's benefit, and it is the provider's own health on its own hardware too, fewer machines held for the same work. The bare-metal piece is gauged on hardware we can meter (the card's own meter, the CPU host's energy counter, section L.25) and claimed for the provider's bare metal only as the same mechanism on the same kind of part: the composition multiplies it in as a modelled factor (class S of class P), never as a measurement of the provider's machines. Four ways are composed: on-site bare metal (the owner's own racks and chips: software × bare metal); through the cloud (the cloud's build, its bare metal at the back end and the software; and the cloud as two pieces, the back end left to the provider); in the device (Omni-Compass built into the bare metal alone, the card and the machine, nothing else wired: for an owner who ships hardware); as a service (the software alone, run for an owner with neither bare metal of their own nor a cloud account: the transport of the software only). This whole stack is a composition with two arms, native and with Omni-Compass on top of every piece; it is not counted among the organisms (the seven, and the orchestra the eighth). Each piece is its own newest measurement, on the engine its record names (the cloud piece Azure's runs on omni-v1, the chip piece the card run of 2 October under a controller since replaced, the software pieces their newest three-run tables): the composition is across those engines, names each, and is remade as each piece's run on the engine that stands lands.

**The stack, native beside Omni-Compass: work flowing down through the pieces**

**The collective synopsis: the benefits, gauge by gauge, added together**

**The composition, piece by piece and layer by layer: each factor with its 95% interval, the whole their product**

**Bills and receipts: what native spent (the cost), what Omni-Compass spent (the expense), and the benefit, in the units each table measured**

**Beyond the count: the governors' tables on this page, the models beside, the separability test, and where the missing pieces land**

**Its monitors.**

#### L.17.1 Monitor 17: The whole organism, composed

The pieces of a stack, native beside Omni-Compass, each piece's composed factors and the whole, their product, in every way a stack is bought.

- **Evidence and state.** Class S (of P and L); composed.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawWhole` → the Python `tools/whole_system.py`, `docs/engine/export_whole.py` → the C++ none: a composition of measured tables by the product law, read as tools/whole_system.py writes it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Work flows down both columns; the reading cursor walks the pieces, one a decision.
- **Knobs.** Scenario: on-site bare metal, through the cloud, in the device, as a service; Reading: every measured piece carried, or the index's strict rule; The chip's run: the chip's one run beside the count or in it; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, EVEN yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is EVEN whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### L.18 Measured effect in full: the organisms, every muscle, the register, the grid and every three-run table

Everything the board in section L.16 stands on, from the organisms down to the single muscle: the seven organisms under their three loads, all 1,107 muscles of the catalog one cell each, every registered benchmark still to run, the scale-out grid of copies and runs, and every three-run table in the repository with every row as it is written.

**Controls.** Recorded data: every receipt as the repository holds it. Console controls never modify it.

**The page, in its own words.**

Every benchmark's benefit in one place, as the repository's benefit sheet holds it (results/BENEFIT_SHEET.json), with the Omni index that weighs them together (results/OMNI_INDEX.md). Then the grid: every organism at 1, 10, 100 and 1,000 copies, each at 1, 10, 100 and 1,000 runs, modelled and with the real cluster inside. The 1,000 tier runs on GitHub's free runners only; paid machines stay at 100. Each bar and square carries its own word, and the size beside the word carries the word's sign: GAIN +, LOSS −, EVEN =, power given +.

**The seven organisms of the catalog under three loads, then the whole stack's two arms, native and with Omni-Compass**

The founder's count of 20 October: the seven organisms of the catalog (the spine first, the base every stack runs on; the four realms; the four stacked; the whole tower), each run native and with Omni-Compass on top of native, under its own load, the climb (1 2 3 2 3 4 …) and work waiting in line; and the whole organism, the software, the cloud and the hardware stacked into one body (section L.17), composed from the pieces' own readings, native and with Omni-Compass on top of every piece: a composition with two arms, not an organism of the catalog. The orchestra, every governor's muscles as one body, is the eighth organism (section L.21). The monitor below draws the seven from the realms table; the whole stack's two arms are section L.17's composition until the stacked run, preregistered in docs/WHOLE_SYSTEM_PREREGISTRATION.md, measures them in one run.

**Every muscle of the catalog, one cell each, its word against native**

Click a cell to read the muscle: its name, family, realm, template, knob and its word under each load.

**Third-party software still to be benchmarked: the register's slots, in order**

What these slots are. Every muscle in them (a legged robot's gait, locomotion_speed; a wind turbine's blade pitch, pitch_angle_limit; a mobile robot's travel speed, agv_speed and trajectory_speed) already runs, modelled, in the 1,107-muscle catalog and the seven organisms below, native and with OMNI-COMPASS on top. A slot here is the next step for that kind of muscle: the same test on the outside world's own software (MuJoCo's Unitree Go2, NREL's OpenFAST, ROS 2 Nav2), each queued until its three runs land.

**The scale-out grid: seven organisms × 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs (the 1,000 tier on GitHub's free runners only)**

**Modelled (class S): the misses**

**With the real cluster inside (class L inside the model): the 95th percentile**

**Every three-run table in the repository, native against Omni-Compass, every row as written (each benchmark's newest engine's table; class L real software, class S outside simulators)**

From each benchmark's newest engine's table (results/live/V10_*.md today), read row by row by docs/engine/export_scenarios.py; open a row to read every judged row that is not EVEN. Class L: the real software (Kubernetes on kind, the real databases and broker). Class S: the outside simulators run by our own runner (CityLearn, pandapower on SimBench, MuJoCo Menagerie, gym-pybullet-drones). Rows shown and not judged are left out of the counts; the counts take every table of a receipt, its tuning case included where it has one (a receipt's own summary line counts its untouched cases). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Every muscle of the catalog and the seven organisms, native against Omni-Compass (the realms table)**

The eighth organism, the orchestra (every governor's catalog muscles, each governor's a body of its own and all of them one body), has its own runner and its own table: section L.21, under the governors.

**Every family, by stack: each muscle alone, native and then with Omni-Compass**

From results/realms_v5/REALMS_V5.json, the realms runner at the max, its engine and commit named above (tools/run_realms_v5.py, catalog realms/catalog_v5.csv), ten paired seeds per muscle and per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none moving the other way; EVEN at its limit on native when its knob already sits at the top of its range. Energy is power given where it rose. Evidence class S, our own models: a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

#### L.18.1 Monitor 18: The seven organisms, three loads

Each organism's misses against native under its own load, the climb and the line (the realms table).

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawOrgCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks every organism under every load, one a decision.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow EVEN, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

#### L.18.2 Monitor 19: Every muscle of the catalog

The 1,107 muscles as one matrix, each cell its word against native, by family and realm; a click names the muscle.

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawMuscleCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks the 1,107 muscles, one a decision; a click holds one.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Every muscle of the catalog one cell, its word against native on its own load: green GAIN, yellow EVEN (pale: at its limit on native), red LOSS.
- **What to do with it.** Click a cell to read the muscle: its family, realm, template, knob and its word under each load.

#### L.18.3 Monitor 20: The scale-out grid

Seven organisms × copies × runs: every square's word, modelled and with the real cluster inside.

- **Evidence and state.** Class S/L; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawGridCv` → the Python `tools/grid_v5.py`, `scripts/dispatch_grid.py`, `docs/engine/build_live_engine.py` → the C++ none: the grid's squares as its runs on GitHub write them; held equal by `tests/test_grid_v5.py`.
- **Moves.** The reading cursor walks every square with runs started, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow EVEN, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

### L.19 Part 5 of the page: Evidence by stack, from the cloud down to the chip

### L.20 Cloud providers: Azure, Google Cloud, Amazon Web Services

In a cloud the one metric is the bill: whether the same workload costs less with Omni-Compass on top. Each provider's four test sets and their status.

**Controls.** Recorded data: GitHub's own cloud runs as read at the build. The controller below plays live; its run and speed follow the console's clock.

**The page, in its own words.**

In a cloud, Omni-Compass shows one thing: the same work as native for a smaller bill, never a bigger one. Every cloud set runs Omni-Compass at the tune-down on the machines alone: no pod autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's. It parks only a machine the cloud already made, after its own trial, and wakes it on a breach. The bill and the machines aim lower; work, speed and failures must read EVEN or GAIN. Azure runs first and is the measure of the other two: the same tuning, mechanism and harness.

**Every cloud run GitHub has started, set by set**

**The bill monitors: Azure, Google Cloud and Amazon Web Services, native against Omni-Compass**

One monitor a provider, the same harness, mechanism and tuning in all three (Azure is the measure of the other two). Each bar pair is a finished set: native's machine-hours (amber) beside Omni-Compass's (blue), the word by the one key (the bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given), the bill at list price under it. A provider with no finished set shows its empty frame and the reason its hourly gate holds, in its own job's words; nothing is drawn for a run that has not run.

**The bill on Azure, run by run, each with the engine it ran on**

From 19 October: every Azure set runs up to 100 paired repetitions a run, the paid cap, under the preregistered stopping rule (tools/stop_rule.py). After 10, 20, 40 and 70 repetitions the bill's change is read with its 99% interval. The run stops once the bill is read (GAIN, power given, or EVEN within ±2% of native's bill), and never while the speed or the failed requests read a LOSS. Those runs carry "to the cap, stopping rule" in their title and count as their own A, B and C; the 5-repetition runs below stay as their own engines' record.

**The shipped controller in the cloud setting, live: native's machines against Omni-Compass's**

The controller every cloud set runs (omni_controller/controller.py --give-back-only, the tune-down, the machines alone), decision by decision on the repository's toy cluster (class S). The cloud's own autoscaler runs in both arms. Omni-Compass only parks a machine the cloud already made, after its trial, and wakes it on a breach. The bill is the machine-minutes in service, counted from the record.

**Native**

**Omni-Compass**

**Its monitors.**

#### L.20.1 Monitor 21: Azure: the bill, run by run

Machine-hours billed and the bill at list price, native against Omni-Compass, every finished Azure set with its 95% interval, and the running set's repetitions done.

- **Evidence and state.** Class L (metered by Azure); record.
- **Feed.** OpenCost; Azure's own billing export; series `node_total_hourly_cost`, `kube_node_info`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/live_reps.py`, `tools/stop_rule.py`, `docs/engine/build_live_engine.py` → the C++ none: the bill as Azure meters it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the finished sets; the age of GitHub's reading counts up every second.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

#### L.20.2 Monitor 22: Google Cloud: the gate and the bill

The same monitor for Google Cloud: the hourly gate's reading (the key, the login, the quota) and, once a set runs, its bill native against Omni-Compass.; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: not yet run: the queue is switched off (the key has not been stored whole); on the founder's word, wired as Azure's sets are (100 paired repetitions under the stopping rule, the 60 s beat, the $0 check first).
- **Feed.** OpenCost; Google Cloud Billing export; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

#### L.20.3 Monitor 23: Amazon: the gate and the bill

The same monitor for Amazon Web Services: the hourly gate's reading and, once a set runs, its bill native against Omni-Compass.; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: not yet run: the queue is switched off (the account cannot leave Amazon's Free plan yet); on the founder's word, wired as Azure's sets are (100 paired repetitions under the stopping rule, the 60 s beat, the $0 check first).
- **Feed.** OpenCost; AWS Cost and Usage Report; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

#### L.20.4 Monitor 24: The cloud setting, live: native's machines

The shipped controller's cloud mode on the toy cluster: the cloud's own autoscaler alone.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`; on a running system: `count(kube_node_info)`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

#### L.20.5 Monitor 25: The cloud setting, live: Omni-Compass's machines

The same autoscaler with Omni-Compass parking a machine only after its trial, waking it on a breach.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`, `omni_writes_total`; on a running system: `count(kube_node_info)`; `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise EVEN, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### L.21 Orchestrators and governors: every scheduler, queue and multi-cluster governor, native and with Omni-Compass on top

These are the governors and orchestrators that sit between the work and the cluster: batch schedulers and job queues, multi-cluster governors, the default Kubernetes scheduler, GPU and edge orchestrators, and the rightsizing controllers. Each runs four ways in every repetition: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, and Omni-Compass on top of the orchestrator; only the last two, each against its own native, are readings of Omni-Compass, and the other comparisons are the orchestrator's own cost. Each has three runs, and every row is shown. Every place below is laid out now and fills itself from the repository as each one lands. Until then it says what the repository holds, and nothing more.

**Controls.** Recorded data: each governor's place as the repository holds it, its runs read from GitHub at the build and played here the moment they land; click a governor (a tile, a row of the road or of the catalog) to hold it.

**The page, in its own words.**

**The road to a result, every governor at once: its register row, its preregistration, its rig on GitHub, runs A, B and C, its three-run table**

**The orchestration stack, live: Omni-Compass on top, the governor native as shipped, Kubernetes and its nodes beneath**

Where each governor sits in the stack. Omni-Compass reads and writes on top of it once its wire is in the repository. The governor runs native as shipped beneath it, and Kubernetes places the work on the nodes. The work dots move at the live engine's demand (section L.29): a picture of the flow, not a measurement. Each governor's readings replace this picture the moment its three runs land.

**The catalog of governors and orchestrators: what each governs, native as shipped, Omni-Compass on top, and what the repository holds now**

**The four ways: the organism alone, the governor as shipped, Omni-Compass on the organism alone, Omni-Compass on top of the governor, all four in every repetition**

**The orchestra, the eighth organism: every governor's catalog muscles, native and with Omni-Compass on top (modelled, class S)**

**Its monitors.**

#### L.21.1 Monitor 26: The orchestrators' road

Every scheduler, queue and multi-cluster governor on its way through trial, A, B and C, on the engine that stands.

- **Evidence and state.** Class L; record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawOrchRoad` → the Python `tools/governors_page.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`.
- **Moves.** A dot travels each governor's road, a running run pulses, and the reading cursor walks the governors, one a decision.
- **Knobs.** Governor: which orchestrator or governor is shown.
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

#### L.21.2 Monitor 27: An orchestrator, four ways

The organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator: the four arms of the chosen governor.

- **Evidence and state.** Class L; record.
- **Feed.** kube-state-metrics; each orchestrator's own metrics endpoint (Kueue, Volcano, KAI, Koordinator, Crane, KubeRay); series `kube_pod_status_phase{phase="Pending"}`, `kueue_pending_workloads`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`.
- **Wired.** This page's `drawOrch` → the Python `tools/governors_page.py`, `tools/run_orchestra.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`, `tests/test_orchestra.py`.
- **Moves.** Work flows down the stack at the live engine's demand.
- **Knobs.** Governor: which orchestrator or governor is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

### L.22 Kubernetes: official run playback

Playback of the official benchmark runs from their archived raw files: the native cluster and the Omni-Compass cluster under identical load, in 30-second bins, every file verified against its run's SHA-256 manifest.

**The page, in its own words.**

A real-time operations dashboard over the benchmark runs themselves (class L), not a model. Every series below streams half minute by half minute out of the raw files GitHub archived, each file's SHA-256 matched before a byte is drawn: native (the whole cluster with everything it ships with, everything but Omni-Compass) against Omni-Compass, the same load, the same second. The tiles, the candles, the heatmap, the bars and the governor's ticker all move together with section L.23 (pick a benchmark, a run or a repetition in either place). Every word is the run's own reading, never one drawn from the stream.

**Data pipeline: from the GitHub Actions run to this page**

**The heart: the governor's beat from this repetition's own audit, beside native's own clock**

Why a heart. A supervisory governor is only alive while its loop turns: once every decision it reads the whole body, decides, writes, and proves it is still there. That turn is the heart. Each beat pumps every reading in through the plug and the decision out (omni_controller/controller.py, its main loop), and renews the governor's lease (master.heartbeat(), omnicompass/master.py). If the heart stops, its process gone or its lease older than its limit (the larger of 120 s and five beats), the watchdog (tools/omni_switch.py watchdog) walks every setting back to native: a stopped heart leaves the body exactly as native runs it. Native has no heart of its own: each of its controllers keeps its own clock (the pod autoscaler every 15 s, the firmware, the thermostats) and no beat joins them. On omni-v16 the governor's heart beats at the pod autoscaler's own pace, a full read of the state every 15 s (the founder's order of 22 October; docs/OMNI_V16.md).

A healthy heart, never pushed. The beat runs at a fixed, calm rate (on omni-v16 one decision every 15 s, the fast checks every 5 s between beats; the runs replayed here ran before omni-v16, one decision a minute) and is never driven faster by the load it governs. Every clock of the engine counts seconds, so the beat's pace sets how often the body is read, never what a rule means: a give-back still waits its trial's minutes, the cushion still keeps its twenty minutes of memory, and a machine still goes back at most one a minute. What it costs is counted inside the body's own load, so the organism never pays for its own brain without knowing it. A decision that fails is recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal time (safe_step). Two gauges below read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page calls a heart under strain when a decision takes more than half its beat, or a gap between beats reaches 80% of the lease. Past half its beat, the governor would have less than half its period left to act before the next reading. Both lines are this page's reading, not rules of the engine; the engine's own guard is the lease and the watchdog.

**The heartbeat sweep: every beat the governor can run at, what it does against native and what it costs**

A knob, not a fixed number. The governor's full read of the state, its heartbeat, is a setting of the run: every clock of the engine counts seconds, so the beat sets only how often the body is read, never what a rule means (omni-v16, docs/OMNI_V16.md). The factory sets 60 s since omni-v17, the main engine (omni-v16 set 15 s, the pod autoscaler's own pace; this sweep reads omni-v16 and omni-v15, and the dial's own ladder reads omni-v17 at every beat in section L.14); an operator may choose another for a system's own reasons, a slower beat to read the cluster less, a faster one to answer sooner, and this monitor shows what each choice does. Each bar is our own model (evidence class S, never a benchmark result): the shipped controller on the toy cluster's 5-second plant, eight seeds of a day each, paired by seed with native and read by the one key (tools/heartbeat_sweep.py, results/toy_gate/HEARTBEAT_SWEEP.md). Every beat here is read in the model only: a real run reads the one beat it was started with, the governor's --interval.

**Response time: one candlestick per 30-second bin**

**Latency heatmap: every response, binned**

**Throughput: requests served per 30-second bin**

**Every repetition of this run, side by side**

**The governor's ticker: every decision of Omni-Compass in this repetition, newest first**

**Native's own controllers' ticker: every change its pod autoscaler and the cluster made in the same repetition, newest first**

From the repetition's own audit.jsonl: the minute and second of the decision, the compass position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward native). Then the machines it recommends, and the give-back verdict's state: "left native" means every setting stays native's; "acting" means a trial on its own measurement. Native has no governor; its own controllers' moves are the second ticker, read from the native arm's capture.csv: the replicas its pod autoscaler holds, the pods waiting for a place and the machines ready. With Omni-Compass OFF the first ticker is empty, for nothing decides on top of native.

**Benchmark status, by block**

**Its monitors.**

#### L.22.1 Monitor 28: The data pipeline, live: every stage from the GitHub Actions run to this page

Every stage from the GitHub Actions run to this page: the run, the raw files archived, the SHA-256 check, the official scorer, the three-run tables, the build and the page, the stage being read lit.

- **Evidence and state.** Class L; replay.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawPipe` → the Python `scripts/raw_archive.sh`, `tools/live_reps.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the stages are GitHub's runs and the repository's own tools; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The stage being read lights in turn and the data moves between the stages.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown.
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.2 Monitor 29: The official run's heartbeat

The official run's heartbeat: native's own 15 s clock above, every beat of the governor's decision loop in the repetition below, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; the load generator's own histogram (the rig's loadgen); series `kube_horizontalpodautoscaler_status_current_replicas`, `kube_node_status_allocatable`; on a running system: `sum(kube_horizontalpodautoscaler_status_current_replicas)`.
- **Wired.** This page's `drawHeart` → the Python `docs/engine/export_runs.py`, `omni_controller/controller.py` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen repetition replayed decision by decision; native's own 15 s clock beats above.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.3 Monitor 30: The heartbeat sweep: every beat the governor can run at

The governor's beat as a knob: what a decision every 5 to 120 s does against native, or against the same engine at 15 s or 60 s, on-site and in the cloud, gauge by gauge with its 95% interval, and what each beat costs the engine; our own model.

- **Evidence and state.** Class S; model.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_decisions_total`, `omni_decision_seconds`, `omni_last_decision_timestamp_seconds`, `omni_own_cpu_cores`; on a running system: `60 * rate(omni_decisions_total[5m])`; `omni_own_cpu_cores`; `time() - omni_last_decision_timestamp_seconds`.
- **Wired.** This page's `drawBeat, beatSetup` → the Python `tools/heartbeat_sweep.py`, `tools/toy_gate.py`, `omni_controller/controller.py` → the C++ none here: the sweep runs the shipped Python controller on the toy cluster; the C++ governor twin is held to the Python's at 60 s and at 15, 10 and 5 s (tests/test_cpp_governor_parity.py); held equal by `results/toy_gate/HEARTBEAT_SWEEP.md`, `docs/engine/build_live_engine.py`.
- **Moves.** A cursor reads the beats in turn and names the row it holds; every button redraws the chart from the record.
- **Knobs.** Beat: the governor's full read of the state and its decision: every 5, 10, 15, 20, 30, 60, 75, 90 or 120 s in the heartbeat sweep's record; on a real governor its --interval (60 s at the factory since omni-v17, 15 s on omni-v16); Scenario: on-site bare metal, through the cloud, in the device, as a service; Engine: which engine's record the monitor reads: the engine that stands or the one before it; Against: what each reading is set against: native, or the same engine at another setting; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.4 Monitor 31: The official run: response time candles

The response time of the chosen run as candles, one a half minute, native above and Omni-Compass below, on one logarithmic scale.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen); series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[1m])))`.
- **Wired.** This page's `drawCandle` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.5 Monitor 32: The official run: the heat map

The responses of each half minute counted in eight response-time buckets, native above and Omni-Compass below.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawHeat` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.6 Monitor 33: The official run: paired bars

The requests answered each half minute, native and Omni-Compass side by side, the failed requests marked.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawBars` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.22.7 Monitor 34: The official run: the repetitions

Each repetition's reading in the chosen gauge with its interval.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawReps` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each repetition's reading filled in as the run replays.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

### L.23 Kubernetes: per-repetition run telemetry

Per-run telemetry at one-second resolution, with the run's receipt and each repetition's score from the repository's own scorer.

**The page, in its own words.**

These are the benchmark runs themselves, not a model: each three-run table's runs A, B and C, read back from the raw files GitHub archived (results/live/raw), native and Omni-Compass, repetition by repetition, played second by second. Every file the page reads has its SHA-256 computed and matched against the run's own SHA256SUMS_ALL.txt, and every Kubernetes repetition is scored by the repository's own scorer (tools/live_reps.py); where a run holds its own scored summary, the scorer's mean over its repetitions equals it (the count is below). Class L: real Kubernetes on kind, real databases and a real broker.

**Native**

**Omni-Compass**

**The receipt of this run**

**This repetition, scored by the repository's own scorer**

**Benchmark status: landed, running, queued, or not yet run**

**Its monitors.**

#### L.23.1 Monitor 35: Per-repetition run telemetry

One repetition half minute by half minute from its archived capture: the 95th percentile of the response time, the replicas, the host's processor and the governor's heartbeat, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; metrics-server; Kepler; series `kube_node_status_condition`, `kube_pod_status_phase`, `kepler_node_package_joules_total`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`; `rate(kepler_node_package_joules_total[1m])`.
- **Wired.** This page's `drawRuStrip` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The archived capture replayed half minute by half minute; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

### L.24 Kubernetes and cloud: the shipped controller's decision trace

The shipped controller's decision trace, replayed from its own audit log one decision at a time: its inputs, its choice and its writes.

**Controls.** Recorded data: the shipped controller replayed decision by decision from its own audit (class S).

**The page, in its own words.**

This is the one place in the repository where the brain drives the muscles decision by decision: the shipped controller, omni_controller/controller.py, on the toy cluster of pilot/selfpilot.py, wired as the repository wires it. Each decision runs the chain left to right: the senses, the six-state brain, the nerves and the machine organ’s grant, the compass law on the service (cloud setting), the verdict’s trial, the release gate, the plug. Every value below is the controller’s own audit record of that decision, recorded by docs/engine/export_controller_trace.py on runs A, B and C (six hours each, a decision every 60 s, class S).

**Native**

**Omni-Compass**

**This decision, brain to muscle, as the controller audited it**

**Three runs, A B C (the whole six hours of each)**

The paired change per 15 s tick, averaged over ten-minute blocks, with its 95% interval (Student’s t) in each run; GAIN or LOSS only when all three runs point the same way with every interval clear of zero (tools/readings.py). Machines and power: a fall is a cut, a GAIN; a rise is power given. Our own models (class S): a model’s small numbers are the model’s.

**What the real thing reads (class L: real Kubernetes, three runs each; every Kubernetes three-run table on this page, each on its newest engine)**

**How steadily the governor steered on real Kubernetes: its own moves on every table results/STEERING.json holds, each on its own engine, beside native's own controllers**

**Its monitors.**

#### L.24.1 Monitor 36: The shipped controller's trace: native

The controller every Kubernetes and cloud set runs, replayed decision by decision from its own audit: native's cluster.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_nodes_observed`; on a running system: `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.24.2 Monitor 37: The shipped controller's trace: Omni-Compass

The same, Omni-Compass's cluster: every write, every trial, every hold.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_writes_total`, `omni_verdict_state`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

#### L.24.3 Monitor 38: The shipped controller's trace: the strip

The shipped controller's machines (in service, booting and parked) and the response time over the run, native beside Omni-Compass, replayed from its own audit.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawCStrip` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/toy_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v19; an older engine's run is its own record.

### L.25 Hardware: the GPU card and the CPU host

The chip is the far end of every stack: there the max would ride each card's own limit, and every watt it takes is power given, shown beside the work it buys. No GPU card and no CPU package has been measured on the engine that stands; what the chip receipts will measure is listed below, no result before its record. Below: the slots for the metered GPU and CPU runs, every hardware run GitHub has started, then the models of one GPU card and one Linux host, native beside Omni-Compass.

**Controls.** Recorded data: GitHub's chip runs, then the chip models replayed from the repository's own run (class S); pick a setting in the table below.

**The page, in its own words.**

Each stack is run twice on the same load and the same seed: native first, then Omni-Compass. Left is native, right is Omni-Compass, and every table gives both columns and the difference. Each stack is its own model in the repository, run exactly as the repository runs it and recorded second by second by docs/engine/export_scenarios.py (class S, our own models). The clouds are section L.20 and Kubernetes sections L.22 to L.24, above this one; every muscle of the catalog, the seven organisms and the three-run tables are in section L.18.

**Hardware runs: the slots for the metered GPU and CPU runs**

The GPU runs on Lambda (class P: the card's own meter) and the CPU on its own machine (class P: the package's own energy counter, tools/run_cpu_power.py) are the receipts this engine still has to earn: whether the same work is done for less power on the chip itself is what those runs will read, and nothing here reads it before they land. Their runs on the engine that stands are not hooked up yet: each place is written here as the repository holds it and fills in, played back from its raw files like every Kubernetes run, the moment its three runs land. Until then the views below are the repository's own models of one GPU card and one Linux host (class S), run native and then with Omni-Compass on the same load and seed.

**The GPU card, metered: the one real run, replayed second by second (class P, the card's own meter)**

The only run in the repository where a real card's own meter recorded native beside Omni-Compass: an NVIDIA A10 on 2 October, ten paired repetitions of 600 s an arm, native (the card as shipped), Omni-Compass watching only (the switch OFF: it reads and writes nothing) and Omni-Compass governing the power limit, every sample of nvidia-smi (200 ms) and every write of the governor's own audit (results/gpu/run-20261002T082232Z, docs/engine/export_gpu_run.py). It ran the card controller of commit c908054, replaced since: its rows stand as that controller's record, every one shown, until the run on Lambda on the engine that stands replaces it (one exact commit, the founder's order). Its own table, re-read by the one key:

**The CPU host: built and waiting for its machine (a model of a machine until then, class S)**

The CPU power harness (tools/run_cpu_power.py) puts Omni-Compass on top of the Linux kernel's own frequency governor and meters the processor's package energy (RAPL). No GitHub runner exposes that counter or a writable ceiling, so its real run waits for a Linux machine that does (the register's row 79, cpu-power.yml). Until then this monitor plays the harness on its own modelled machine (--plant sim, written for its tests; results/sim/cpu_power_model, three repetitions): the mechanism moving, every decision and write of its own audit, never a measurement. The machine layer enters the whole organism as exactly 1 until the real run lands.

**An 8-card node: built and awaiting its run (scripts/gpu_8card.sh)**

The 8-card result is one command on a rented machine with eight NVIDIA cards (scripts/gpu_8card.sh, docs/GPU_RUN_GUIDE.md section D): every card runs the whole card test at once, its firmware alone against its firmware with Omni-Compass on top, 24 paired repetitions a test pooled across the cards. It has not run. The monitor is built for it: eight card slots, each native lane drawn from the repository's one-card model (class S: AI token generation at the card's shipped 150 W, the same model on every card until the run, never eight measurements), each Omni-Compass lane empty until the run lands. On a running node the same panel reads the NVIDIA DCGM exporter's series card by card.

**Every chip run GitHub has started, newest first**

**Where the mechanism moves on the chip models: every setting, three runs each**

Read from the replayed record itself, second by second, in each of the three runs (seeds as below). A row with no second held off native is Omni-Compass deciding to stay native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native.

**Native**

**Omni-Compass**

**What Omni-Compass did, as its own audit records it**

**Three runs, A B C (the whole run of each)**

**Its monitors.**

#### L.25.1 Monitor 39: The GPU card, metered: the one real run

The NVIDIA A10 run of 2 October replayed from the card's own meter: draw, limit, clock and temperature, requests served and the 95th percentile, native beside Omni-Compass governing (or watching only), every write of the governor marked.

- **Evidence and state.** Class P; awaiting its run: its omni-v13 run on Lambda (lambda-gpu.yml, one exact commit): the replaced controller's run stands until then, shown as such.
- **Feed.** NVIDIA DCGM exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`, `DCGM_FI_DEV_GPU_TEMP`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_POWER_MGMT_LIMIT`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawGpuRun` → the Python `docs/engine/export_gpu_run.py` → the C++ none: the 2 October run of an earlier controller, replayed from the card's own meter; today's GPU rules have their twin, cpp/src/gpu_rules.cpp, for the run on Lambda; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The card's own meter replayed at ten times the run's seconds.
- **Knobs.** Repetition: which repetition of the run is replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v19 run lands.

#### L.25.2 Monitor 40: The CPU host, metered: awaiting its machine

The CPU power harness on the host: the frequency ceiling, the clock run at, the package power and the response line, native beside Omni-Compass; today its own modelled machine (class S), the real run the day a machine with its meter runs it.

- **Evidence and state.** Class S (model) until the run; awaiting its run: a Linux machine whose processor exposes its energy counter (RAPL) and a writable frequency ceiling (register row 79, cpu-power.yml).
- **Feed.** node_exporter (rapl, cpufreq collectors); Kepler; series `node_rapl_package_joules_total`, `node_cpu_scaling_frequency_hertz`, `node_cpu_scaling_frequency_max_hertz`, `kepler_node_package_joules_total`; on a running system: `rate(node_rapl_package_joules_total[1m])`; `avg(node_cpu_scaling_frequency_hertz)`.
- **Wired.** This page's `drawCpuHost` → the Python `docs/engine/export_cpu_model.py`, `tools/run_cpu_power.py` → the C++ none: the host's model until its run lands on a machine with its meter; held equal by `tests/test_run_cpu_power.py`.
- **Moves.** The host's model replayed second by second until its run lands.
- **Knobs.** Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The processor's frequency ceiling (the knob), the clock the kernel's own governor ran at under it, the package power and the busy share, native beside Omni-Compass.
- **What to do with it.** Until a machine with its energy counter runs it, the monitor plays the harness's own modelled machine: read the mechanism, never the numbers.

#### L.25.3 Monitor 41: An 8-card node: built and awaiting its run

Eight card slots for scripts/gpu_8card.sh: each native lane the repository's one-card model (class S), each Omni-Compass lane empty until the 8-card run lands, 24 paired repetitions a test pooled across the cards.

- **Evidence and state.** Class S (native model) until the run; awaiting its run: scripts/gpu_8card.sh on a rented machine with eight NVIDIA cards (docs/GPU_RUN_GUIDE.md, section D).
- **Feed.** NVIDIA DCGM exporter, card by card; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`; on a running system: `sum by (gpu) (DCGM_FI_DEV_POWER_USAGE)`.
- **Wired.** This page's `drawGpu8` → the Python `realms/gpu_card.py`, `omni_controller/gpu_governor.py`, `scripts/gpu_8card.sh` → the C++ `cpp/src/gpu_rules.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** The one-card model's native lanes replayed second by second; the Omni-Compass lanes wait for the 8-card run.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v19 run lands.

#### L.25.4 Monitor 42: The chip and the host, modelled

The repository's own models of one GPU card and one Linux host, native beside Omni-Compass, second by second (class S).

- **Evidence and state.** Class S; model.
- **Feed.** NVIDIA DCGM exporter; node_exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_SM_CLOCK`, `node_cpu_scaling_frequency_hertz`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawSStrip` → the Python `realms/gpu_card.py`, `omnicompass/compass_law.py`, `tools/toy_gate.py`, `omni_controller/muscles.py`, `omnicompass/conveyance.py`, `docs/engine/export_scenarios.py` → the C++ `cpp/src/conveyance.cpp`, `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_conveyance_parity.py`, `verify.py`.
- **Moves.** The chip's and the host's models replayed second by second; a ring opens at each head with its newest value.
- **Knobs.** Stack: the GPU card, the Linux host, Kubernetes or the cloud; Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v19 run lands.

### L.26 Part 6 of the page: The organism, live: native and Omni-Compass

### L.27 The organism, live: native and Omni-Compass

The system rendered as an organism: each node is a muscle (one controlled actuator) and each ring its operating range. The left instance runs under its native controllers alone; the right runs the same controllers with Omni-Compass's brain, nerves, heart and immune system supervising them. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: the rings, the immune system and the anatomy respond to the console.

**The page, in its own words.**

Every view is run twice on the same body, the same load and the same seed: native (left), then Omni-Compass (right). "One organism" is the sixty muscles in one body: the whole native organism on the left, the same organism with Omni-Compass on the right; "each muscle alone" runs each muscle native and then with Omni-Compass, one at a time. The counters under each ring and the scoreboard (section L.32) give both arms and the difference. Where the two sides look the same, they are the same. Under the max a muscle is moved only where it has room above native. A muscle already at its limit on native (— of these sixty) is left native by design. Inside one organism the bone, the power and cooling the whole body shares, holds most moves back. A dashed white ring marks every muscle that differs between the two sides at that moment; the counter under each ring counts them. In these harness views the max acts muscle by muscle and the brain at the center reads the body without steering it, as in the realms harness itself; section L.24 shows the live controller, where the brain's rules run every decision.

**Reading the rings: a quick-start guide**

**Native**

**Omni-Compass**

**The body scan: every organ, native and Omni-Compass, live from the official run playing**

As a scan reads a living body organ by organ, this reads the system playing in section L.22 (the benchmark, run and repetition chosen there), organ by organ, half minute by half minute, from its own SHA-256-checked files: native beside Omni-Compass. Where native has no such organ the cell says so.

**The immune system, live: native beside Omni-Compass (the immune system is Omni-Compass's; native runs on its own controllers)**

The body keeps itself healthy the way a human body does. Every room and every machine pool has a native twin: the same muscle under its own controller, on native's heat and load, the body's memory of healthy. A room that stands warmer than its twin is inflamed. Where its own knob can cool it, it is cured on the spot. Where it cannot, it sends the whole body a signal, its heat debt, like a cytokine calling for help. The other muscles answer: the machine pools give back what Omni-Compass added until the room stands no warmer than native's. The skeleton (the bone: the power and cooling lines the whole body shares) grants nothing it cannot carry. A cooling setting is walked back, never snapped. A pool never loses a machine its queue needs, a battery is timed for its line, and no sense is locked. On the ring a pulsing red circle marks the inflamed muscle, and red signals run from it to every machine pool that answers it.

**The anatomy, part by part, in the order of control: the brain first, the whole organism last**

**Its monitors.**

#### L.27.1 Monitor 43: The organism, live: native

Sixty muscles of the stress model, each on its own native controller, at their positions in the band.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); kube-state-metrics; series `omni_recommended`, `kube_horizontalpodautoscaler_status_current_replicas`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position in the band.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; The muscle's own switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

#### L.27.2 Monitor 44: The organism, live: Omni-Compass

The same sixty muscles with Omni-Compass on top of their native controllers, the brain's grants and pushes.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_recommended_moves_total`, `omni_writes_total`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position, the brain's grants and pushes pulse.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; The muscle's own switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

#### L.27.3 Monitor 45: The immune system

Where the two sides differ, and the body's heat debt: a room warmer than its native twin, inflamed, given back.

- **Evidence and state.** Class S; live.
- **Feed.** Prometheus Alertmanager; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `ALERTS`, `omni_compass_decisions_total{zone="wall"}`; on a running system: `sum(ALERTS{alertstate="firing"})`; `increase(omni_compass_decisions_total{zone="wall"}[1h])`.
- **Wired.** This page's `drawImm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py`, `realms/compass_arm_v5.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each side's pools, warmest room and muscles past the line take a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

#### L.27.4 Monitor 46: The body parts on the band

Each body part's muscles (the spine and the four realms) at their positions in the band, native above and Omni-Compass below, every decision.

- **Evidence and state.** Class S; live.
- **Feed.** the realms harness's own record (realms/harness.py, each body part's muscles at their positions in the band, recorded by docs/engine/export_harness_trace.py); no Prometheus feed.
- **Wired.** This page's `drawSwarm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's dot moves to its position in the band.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### L.28 Telemetry analytics and Omni-Compass in its own words

The same telemetry analysed four ways: a three-dimensional tensor view, a difference matrix, a principal-component decomposition and Omni-Compass's own account of its run; the service level and error budget in SRE terms; and Omni-Compass answering the viewer's questions about itself from the page's own records.

**Controls.** Recorded data: the engine's harness record (class S), played on the live engine's clock, and the official run chosen in section L.22 (class L). Console controls never modify either.

**The page, in its own words.**

The engine's own record is a tensor: two arms × every decision × sixty muscles, each entry a muscle's compass position (0 calm, 0.5 the center of its band, 1 its line), recorded from realms/harness.py by docs/engine/export_harness_trace.py (class S, our own models). It fills in below decision by decision as section L.27 plays, and the same numbers are read three more ways: the difference between the arms, the body's principal motions, and Omni-Compass's own account of what it is doing. Then the official runs (class L) are read as an SRE reads a service: the service level, the error budget burned and every gauge against native; and Omni-Compass answers questions about itself, reading the page's own records through tools and turning the dashboard to a run. No word on this panel is drawn from a picture: every GAIN, EVEN, LOSS and power given is a run's own reading.

**Omni-Compass, in its own words**

Omni-Compass speaks for itself here: every line is read from its own records at the moment on screen (the official run playing in section L.22, its governor's own audit, and the engine's harness on the console's clock), and says what it is doing, beside what native does. Speak aloud reads it out on the viewer's own browser voice as the run plays, and reads its answers below too.

**The telemetry tensor, in three dimensions**

**The difference matrix: Omni-Compass against native**

**The body's principal motions (the tensor's eigen-decomposition)**

**The service level and the error budget, this repetition**

**Every gauge of this repetition against native**

**Ask Omni-Compass: it answers for itself, from its own records on this page**


Connecting…

Omni-Compass's answers are drawn from this page's records and are not reviewed by any outside party. © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with LICENSE, NOTICE and DISCLOSURES.md. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Its monitors.**

#### L.28.1 Monitor 47: Telemetry tensor: the cube

The engine's harness record as a tensor (decisions × sixty muscles × two arms), native and Omni-Compass as two slabs, filling in on the live engine's clock.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** kube-state-metrics; the service's own metrics.
- **Wired.** This page's `drawCube` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Fills in decision by decision on the live engine's clock, and turns.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

#### L.28.2 Monitor 48: Telemetry tensor: the difference

The difference of the two sides' tensors, cell by cell.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawDelta` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** One column a decision on the live engine's clock.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

#### L.28.3 Monitor 49: Telemetry tensor: the modes

The principal modes of the telemetry (its matrix decomposed).

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawModes, tEig` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision: the line across each bar is that decision's own motion in the mode; the first mode's line takes a point, a ring at its head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

#### L.28.4 Monitor 50: Service level: the objective

The share of each half minute's requests answered inside the 500 ms line, native beside Omni-Compass, through the official run chosen in section L.22.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra) over the service's histogram; series `slo:sli_error:ratio_rate5m`; on a running system: `1 - slo:sli_error:ratio_rate5m`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

#### L.28.5 Monitor 51: Service level: the error budget burn

The requests over the 500 ms line counted up since the repetition began, native beside Omni-Compass: each side's error budget burned.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra); series `slo:error_budget:remaining`; on a running system: `slo:error_budget:remaining`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

#### L.28.6 Monitor 52: Telemetry radar

Every gauge of the repetition replaying in section L.22 against native's 0 line: GAIN to the right in green, LOSS to the left in red, its side the run's own reading.

- **Evidence and state.** Class L (the official run's own gauges); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawRadar` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each gauge of the repetition replaying in section L.22.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### L.29 Control console: every runtime control of the live engine

The engine these knobs turn is the engine's own mathematics running in this page: the brain (omnicompass/core.py, integrated by RK4), the compass law (omnicompass/compass_law.py) and the verdict (omnicompass/verdict.py). docs/engine/check_live_engine.py proves the port equal to the Python and the C++ on every build. It governs the stress-test model's sixty muscles (class S), each on top of its own native controller. Every knob acts on both sides at once, the same demand, the same draw of noise, the same lost pool, so the one difference left between them is Omni-Compass. The knobs move the live engine in sections L.27 and L.31 to L.33, and the kill switch and the frame load also move this page's own renderer (section L.39). A recorded run (the benefit board, the chips' and Kubernetes' replays, the official runs) is a record: no knob rewrites it.

**The page, in its own words.**

Do no harm. Every control here acts on both arms alike; what Omni-Compass does with them is held by its guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another, a give-back tried against native first and refused on a LOSS. Its one meaning is written once, in the back matter (vi) as DISCLOSURES.md section L.17 writes it.

What these controls do. Runtime parameter control and fault injection on the live engine: load scaling, noise injection, sensor latency, capacity loss, a demand surge, a sensor blackout, a security hold, the dial, and the kill switch. Every control is applied to both arms identically; the response is plotted per decision, native beside Omni-Compass.

**System response, per decision**

**Frame timing: the inter-frame interval against the 60 Hz budget**

**Control event log, newest first**

**Control-loop performance assessment, this day (live)**

**Its monitors.**

#### L.29.1 Monitor 53: The console's response

The last 120 decisions of the live engine: the muscles past their line and the work, native beside Omni-Compass, every knob of the console turned marked.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawDeskCv` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: both lanes slide one decision, a ring opens at each head with its newest value; every knob turned is marked.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Pause: hold the engine's clock; Frame load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

#### L.29.2 Monitor 54: The frame budget

The time between frames of this page against its line under the frame load knob.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawFrameCv` → the Python none: the page's own frame clock, measured in the browser; there is nothing to port → the C++ none: the page's own frame clock, measured in the browser; there is nothing to port.
- **Moves.** Every frame of this page.
- **Knobs.** Frame load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

### L.30 Part 8 of the page: Control architecture: the brain

### L.31 One control cycle, traced step by step

One control cycle traced end to end at reduced speed: the sensed inputs, the brain's decision, and the actuator (muscle) it wrote. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: the cycle and the controls below share the console's state.

**The page, in its own words.**

**One decision, in the order the code runs it**

**Controls**

The max: every muscle to its own limit, never below native; the capacity it holds is power given. Tune-down: never more than native, and a step back only with the organ’s grant and the release gate. In this model native already sits near its band, so the tune-down finds little to hand back; the scoreboard (section L.32) reads its runs A, B and C live when the dial is on the tune-down. The spread of positions can widen a little, because the calm muscles it hands back move toward their line while the busy ones stay.

Each stress lasts 40 decisions from the moment you press it. Both arms meet the same demand.

**Its monitors.**

#### L.31.1 Monitor 55: One control cycle, traced

The compass band with its cushions, the two forces and one decision, step by step.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawBand` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** One control cycle traced step by step on the followed muscle, every decision.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### L.32 Phase plane and scoreboard

The phase-plane state of every muscle (its position and velocity in its band) for both arms at the same instant, with the running scoreboard. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: every plane, strip and well responds to the console.

**The page, in its own words.**

How to read the plane. It is a phase portrait, the picture control engineers use for a system's state. Across is where each muscle sits in its band: p is 0 when calm, 0.5 at the center and 1 at its line. Up and down is how fast it moves there (v, per decision). A muscle at rest sits on the middle line. One climbing toward its line moves up and right, and past the right edge it is past its line. Native is on the left and Omni-Compass on the right: the same muscles at the same instant, one dot each. In the realms harness each muscle answers to its own rule, so no single field is drawn. In the stress-test model the shading on the right is the force the compass law would apply there: the add force gives capacity and the hand-back force returns it. Past the 0.95 wall the law fails up at once. Under each plane, the same instant in words.

**Native**

**Omni-Compass**

**Live stat panels: native beside Omni-Compass, now and over the last 120 decisions**

Each panel is one gauge of the live organism, read every decision on both sides, as an operations dashboard shows it. It gives native's value now and Omni-Compass's, the last 120 decisions of both (native solid amber, Omni-Compass blue), and the running paired reading in the tables' words. With the master switch OFF the decisions are shaded red and Omni-Compass's side follows native: its value equals native's and its line is drawn in native's colour, dashed on top of native's, so both stay in view.

**Native against Omni-Compass**

How each row is read: the paired change, native against Omni-Compass at the same decision, averaged over blocks of ten decisions so neighbouring decisions do not count twice, with its 95% interval (Student’s t over the blocks). This run: an interval that includes zero reads EVEN; clear of zero, the word follows the gauge’s aim (work: a rise is GAIN; misses, failed work, waiting: a fall is GAIN; energy or capacity held: a rise is power given, a fall a cut). Three runs (tools/readings.py): GAIN or LOSS only when all three runs point the same way with every interval clear of zero; EVEN when an interval includes zero; “the runs disagree” when clear runs point different ways. The spread of positions and the settings are shown, never judged: no rule of the engine aims at them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

#### L.32.1 Monitor 56: Phase plane: native

Native's muscles in position and velocity.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

#### L.32.2 Monitor 57: Phase plane: Omni-Compass

Omni-Compass's muscles in position and velocity, the band's walls drawn.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

#### L.32.3 Monitor 58: The scoreboard strip

The body's capacity in service and its demand (in the harness, its electrical power), the muscles past their line and the spread of positions over the day, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_decisions_total`, `omni_writes_total`; on a running system: `increase(omni_compass_decisions_total{zone="wall"}[1h])`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawStrip` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine (900 ms at 1×): the line takes a point, a ring opens at its head and its newest value is printed beside it.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### L.33 The brain's internal state

The brain's six state variables rendered on their potential-energy landscapes: a state resting at a minimum is stable; a state driven toward a maximum is under load. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: every plane, strip and well responds to the console.

**The page, in its own words.**

The same state the cycle panel prints, drawn as the physics it is. Each ball is a live value of the engine's brain, integrated by RK4 every decision. In the stress-test model its push and target feed the body's levers. In the harness views the harness arm (realms/compass_arm_v5.py) acts muscle by muscle with no brain, so the brain drawn here is the page's own, fed the harness's readings. With each muscle alone there is no body, and its power and thermal readings are held at 0.3. Native has none of this: no state, no memory of need, no stress, no tide; each controller sees only its own reading, one to three decisions late.

**U on the double well · eq. (2)**

V(U) = −μ(U²/2 − U⁴/4) + (Ė/E_max)·U. A rising E tilts the well toward the basin of collapse.

**S in its potential Φ · eqs. (5)–(6)**

Φ(S) = αₛ S²/2 + βₛ S³/4 − δS. S rolls to S*; the senses pull it back each decision.

**The bath B · eq. (7)**

B̈ = γ[c] δ S − (ω[B]/Q[B]) Ḃ − ω[B]² B. The slow tide of physical load.

**Native, the same decisions: what its own controllers read and do**

Native has no brain to draw: each of its controllers reads one reading, its own muscle's, and moves. Drawn live from the same decisions as the wells above: the mean position its muscles' readings put them at (0 calm, 1 at the line), the share of its muscles past their line, and how many of its own controllers moved their setting this decision. Class S, our own models.

**The nerves: four scalars multiply into calm**

Native has no nerves: nothing grants or refuses a controller, and a blind sense or a security hold changes nothing it does.

calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)). An organ may hand capacity back only when calm ≥ its θ, the line is clean and every sense is live; expanding stays allowed except under a security hold. Under the max, lifting off toward native never needs this grant; going below native does.

**Its monitors.**

#### L.33.1 Monitor 59: The brain's state: the well

The brain's double-well potential and where its state sits.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

#### L.33.2 Monitor 60: The brain's state: stress S in its potential

Stress S on its cubic potential Φ(S) = αₛS²/2 + βₛS³/4 − δS, rolling toward S*; the senses pull it back each decision (eqs. (5)–(6)).

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

#### L.33.3 Monitor 61: The brain's state: the bath B

The bath oscillator B, the slow tide of physical load, over the last 120 decisions (eq. (7)), its spring at the latest B.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`.
- **Wired.** This page's `drawBrain` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the bath's line takes a point and a ring opens at its head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

#### L.33.4 Monitor 62: Native's own controller beside the brain

What native's controller would do at the same decision, beside the brain's grant.

- **Evidence and state.** Class S; live.
- **Feed.** kube-state-metrics; series `kube_horizontalpodautoscaler_status_desired_replicas`.
- **Wired.** This page's `drawNat6c` → the Python `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ none: native's own controllers, as the harness's record or the page's own model holds them; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision of the live engine.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### L.34 The verdict: change acceptance testing

The change-acceptance test. Each step is trialled against native and kept unless the measurement reads LOSS or its estimated cost exceeds the 2% allowance. An EVEN result (no difference resolvable from the noise) is also accepted, so on high-variance workloads a step with a small true cost can pass; the lab below measures that false-acceptance rate.

**The page, in its own words.**

Before a knob moves one step past native, the step runs as a trial: costs at native first, then at the step. The engine that stands reads the change exactly as a report reads a row, on the log of each cost, with its 95% interval. Set what the step truly costs and watch the rule decide. It opens wired as the shipped Kubernetes controller is wired, on the noise the real runs measured.

**This trial**

**Over many trials at this cost**

Native: its knob never moves past its own setting, so there is no trial and nothing to judge; every step Omni-Compass takes past native has to pass this test first. The medians alone allow a step when the trial's median is within the allowance of the reference's. The engine's rule (omni-v12's, unchanged) also refuses any step whose interval sits wholly above zero. It measures on while the interval is wider than the allowance, up to three times the pieces measured each side. It keeps a step only if both estimates are inside the allowance. Ported from omnicompass/verdict.py; the costs are modelled (class S).

How each muscle wires it. The Kubernetes controller measures 200 requests each side against a 2% allowance (omni_controller/controller.py --verdict-samples 200 --allow 0.02), the cost being each request's response time. The noise is measured at every build on each request of the newest tables' own runs. The σ 0.05 and 0.25 this page carried before 19 October did not come from these files and are withdrawn. The GPU card measures 30 requests (gpu_compass.py --verdict-samples 30); in its model the card's own time per request carries no noise. The toy gate measures 60 (tools/toy_gate.py, σ 0.25). What the rule does there is computed live in this page as you read: trials at each cost with this lab's own rule, 200 requests a side to start (the trial side measured on to 600 while its interval is wider than the allowance), a 2% allowance and the measured σ (modelled, class S). With noise this wide, 200 requests a side do not refuse a small LOSS on their own; with no noise any LOSS it can read is refused, even 0.1%. A larger sample would refuse more, and any change to the rule or its sample is the next engine version, landed through the toy gate and told to the founder (his order of 19 October). Above the verdict the max never goes below native at all, so in the default it never runs (section L.24: no trial on top of the HPA).

**Its monitors.**

#### L.34.1 Monitor 63: The verdict: one trial

A give-back trial judged against native: its reference, its step, its interval and the word.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`; on a running system: `omni_verdict_state`.
- **Wired.** This page's `drawVerdict, vTick, judge` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** A cost measured every 28 ms until the verdict reads; a new trial starts 2.6 s after.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

#### L.34.2 Monitor 64: The verdict: every true cost

The keep ratio of the verdict at each true cost, from trials run in this page's idle time.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawVerdict2, runTrialSync` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** Trials run in the browser's idle time; the shares fill as they run.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native).
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

### L.35 Failure modes, controls and residual risk

The failure-mode register: every known way Omni-Compass can fall short, the control that mitigates it, that control's coverage, and the residual risk where it does not reach. Every failure mode the live engine can be put through has a fault-injection control; trigger it and observe both arms on the console. Below: the resource costs the three-run tables report but do not judge.

**Controls.** Live: every way below that the live engine can be put through has its own button, and the response plays on the console (section L.29), native beside Omni-Compass.

**The page, in its own words.**

**Failure-mode register: control, coverage and residual risk**

**Reported, unjudged metrics: the resource cost of the work**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.36 Part 10 of the page: The components: their mathematics and their C++ twin

### L.37 Component specification and mathematics

The component specification: every part, its equations and the source module that implements it, in Unicode as the repository writes them.

**Controls.** Live: the brain's six state variables below are read from the live engine every decision, beside the equations that evolve them.

**The page, in its own words.**

Items 1 to 5 and 8 are the engine’s code and run in every live view (the official-run playback of 5c and 5d replays records and runs none of it). Items 6 and 7 as written (the compass law on each muscle, the plug’s lever) drive the stress-test model. In the harness views the max and the plants’ own overrides take their place. The live controller runs the compass law on the service, as section L.24 shows.

**The stress-test model, written out (class S, drawn for this page)**

**Who drives what**

**What is the engine's code**

The six-state engine, its constants and RK4 integrator, the assimilation, push and ρ*, the four nerve scalars and the organ thresholds, the compass law and the verdict in words are ported from omnicompass/core.py, adapter.py, nervous_system.py, compass_law.py and verdict.py at commit c8ba7775d. All are inside the omni-v18 fingerprint, unchanged since omni-v17 (omni-v18 added only Omni direct's seven files, and omni-v17 moved only the Kubernetes governor's default beat to 60 s and its cruise wait to two readings at least, neither of which the port computes); adapter.py carries omni-v16's clocks in seconds (at the page's 60 s step every value is omni-v15's) and omni-v15's clear-time gate on the power-cap request, which the port does not compute (it ports the states, the push and the headroom), and the others are omni-v12's bytes. omni-v9 added omnicompass/student_t.py, and the page carries its Student t too, computed by bisection on its own distribution and rounded to three decimals as the printed tables are. omni-v10 changed only the CityLearn wire's glide, omni-v11 only the Kubernetes governor's blind-reading guard, omni-v12 only that governor's hold on a refused raise, and omni-v13 only the governor's conveyance on a shared host at its top, omni-v14 only the governor and its muscles: a muscle left native, the operator's commands without a shell, and omni-v15 the brain's power-cap request through the line's own clear time, with the card governor handing the brain its clear flag. Checked against the Python on seeded inputs (docs/engine/check_live_engine.py): 8,000 decisions of the governor (state, push, ρ*, κ, h, σ, ν, calm), 48,000 organ grants, 4,800 compass forces, 300 verdict intervals and 400 full verdict trials. A build passes only when the largest difference is under 10⁻¹², no grant and no verdict differs, and the Student t is equal on all 500 degrees of freedom checked. And against the C++ twin of the core (cpp/src/core.cpp, compiled by the check with docs/engine/cpp_core_probe.cpp): 2,000 seeded states, the derivative and the RK4 step within 10⁻¹² of each other. The check prints its own measured differences in each build's report on GitHub. The page's engine, the Python and the C++ are one engine. The harness views are not ported: they are the harness’s own record, made by its code.

**The two bodies**

The realms harness (the default). The sixty muscles are one organism of realms/harness.py. Each is a plant of realms/plants.py: machine pools under their autoscalers, cooled zones, batteries on their lines, motion axes and process loops. They are coupled through their heat and their power, under the climb (1 2 3 2 3 4 …), for 240 decisions of 15 s. Omni-Compass is the max of realms/compass_arm_v5.py with the body’s bone, its twins and the muscles’ cards; at 80% the brain goes silent and the lease walks every setting back to native over 24 decisions. Recorded on seeds 3000, 3001 and 3002 (runs A, B and C) by docs/engine/export_harness_trace.py; the page replays the record. Each muscle alone is the same harness one muscle at a time, as run_muscle_arm runs the preregistered muscle table: under the line (work waiting at the start), the max with the muscle's own twin, and the lease after 80%. Each muscle's decisions are laid on 240 frames. A frame shows the last decision it covers, and reads over the line if any of them was. In that harness the brain’s state is computed from the body’s aggregate, as a governor reads it, and shown; the max itself acts muscle by muscle. The stress-test model. A model drawn for this page so the body can be stressed by hand (a surge, a blind sense, a security hold, the kill switch), evidence class S; like every view it runs native and Omni-Compass, side by side, on the same demand. Sixty muscles named from the 1,107-muscle catalog (twelve each from the spine and the four realms), each a capacity lever with its own response time τ and sensing delay, under an HPA-style native controller (target 0.70, 10% tolerance, five-decision scale-down window). Demand climbs 1 2 3 2 3 4, surges, eases and idles over six hours, the same for both arms. The lever rules that turn F into a write are this page's, written out above and kept inside the doctrine. Under the max: never below native, and lifting off hands back toward native. On the tune-down: never above native, and below it only with the organ's grant and the release gate.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.38 The C++ twin: the Python's runs through the C++ engine

**The page, in its own words.**

In plain words. The engine is written twice, in Python and in C++, line for line. Every time this page is built, the Python's own runs are fed into the C++ as its input, and the C++ answer is set beside the Python's, number by number. Where they are the same to the last digit, the two are one engine. Where a part runs in Python only, the last table names it.

**Every twin, on its own parity check**

**The Python's runs through the C++ engine, receipt by receipt**

The Python's seeded runs (tools/engine_runs.py: the jump generator's seeds, 288 decisions of the brain, 80 steps of the compass law and one give-back trial a run) are the input: the Python writes every run's draws as the injection, the C++ harness (cpp/tools/engine_runs.cpp) reads it, puts the mechanism on through the C++ twins (the governor, the nervous system, the compass law, the verdict) and writes its own receipts and digest, the output. The proof monitor (section L.10, the Python's runs, in this page) shows the same column run by run.

**The compass law of every run on this page, reading by reading**

**The seven organisms at the tune-down, every muscle's law**

**What runs in Python only, for now**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

### L.39 Self-governed rendering: Omni-Compass inside this page

The page's own render loop is governed by the same compass law, measured on the client device, native beside Omni-Compass.

**The page, in its own words.**

The engine that runs this page has Omni-Compass in it. Native is the browser's own loop: every chart on screen drawn on every frame, and when the frame overruns, whole frames dropped. Omni-Compass is the same loop with the engine's own compass law governing it (omnicompass/compass_law.py, ported here and checked against the Python). Each chart is a muscle whose knob is how many frames it waits between draws, and the reading is the time between frames. Below the band's center the pedal lifts and every chart is handed back to native, drawn every frame. Toward the line it pushes: the charts farthest from where you are looking wait a frame or more, so the frame itself stays inside its line. Every step is a trial run to its full measurement and kept only when the frame shortens; a step that buys nothing is refused and every chart handed back to native (the reflex rule: where a knob cannot bring a GAIN, it stays native). The reading is the time between frames, the band two frames wide with its center one frame at 60 Hz. The two arms take turns in paired windows of three seconds on this same page, on your own machine, and are read by the three-run rule's interval (class L: this browser, live; a reading of this page, never a benchmark of record).

**Native**

**Omni-Compass**

**Frame timing: the inter-frame interval against the 60 Hz budget**

**Paired measurement of this page, per window**

**Its monitors.**

#### L.39.1 Monitor 65: Self-governed rendering

This page's own render loop governed by the compass law: the frame time against its line, native (no governor) beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawSelf` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`.
- **Moves.** Every frame: this page's own frame time under the compass law.
- **Knobs.** Frame load: +0, +8 or +16 ms burned inside every frame of this page; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** This page's own render loop governed by the compass law: the time between frames against its line, native (no governor) beside Omni-Compass.
- **What to do with it.** Load the page with the frame-load knob and watch the governor shed chart frames to keep every frame inside its line.

### L.40 vi Disclosures, governing law and contact

**The page, in its own words.**

**What this page is**

**Disclosures**

**Contact**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.


### L.41 Every monitor

| No. | Monitor | Section | Class | State |
|---|---|---|---|---|
| 1 | The master switch and the kill switch | 1e The master switch's wiring | S (the page's port of the master switch; the real one is omnicompass/master.py) | live |
| 2 | The Python's runs, reproduced here | 1f The Python's runs, in this page | S (the engine itself) | live |
| 3 | The Python's 500 scenarios, replayed | 1f The Python's runs, in this page | S | replay |
| 4 | Golden signal: errors | 1h The golden signals, the event log and the live metrics | S | live |
| 5 | Golden signal: throughput | 1h The golden signals, the event log and the live metrics | S | live |
| 6 | Golden signal: latency | 1h The golden signals, the event log and the live metrics | S | live |
| 7 | Golden signal: saturation | 1h The golden signals, the event log and the live metrics | S | live |
| 8 | GitHub Actions: the runs in flight | 1i CI pipeline | L (GitHub's own API, read at the build) | record |
| 9 | Omni direct: work each step | 1k Omni direct | L | record |
| 10 | Omni direct: the 95th percentile each step | 1k Omni direct | L | record |
| 11 | Omni direct: units each step | 1k Omni direct | L | record |
| 12 | Omni direct: machines each step | 1k Omni direct | L | record |
| 13 | The benefit board | 2 The benefit board | L/S | record |
| 14 | Where the benefit lives, gauge by gauge | 2 The benefit board | L/S | record |
| 15 | The market map: every three-run table a tile | 2 The benefit board | L/S | record |
| 16 | The quote board: every three-run table a quote | 2 The benefit board | L/S | record |
| 17 | The whole organism, composed | 3 The whole organism, every way it is bought | S (of P and L) | composed |
| 18 | The seven organisms, three loads | 4 Measured effect in full | S | record |
| 19 | Every muscle of the catalog | 4 Measured effect in full | S | record |
| 20 | The scale-out grid | 4 Measured effect in full | S/L | record |
| 21 | Azure: the bill, run by run | 5a Cloud providers | L (metered by Azure) | record |
| 22 | Google Cloud: the gate and the bill | 5a Cloud providers | L | awaiting its run |
| 23 | Amazon: the gate and the bill | 5a Cloud providers | L | awaiting its run |
| 24 | The cloud setting, live: native's machines | 5a Cloud providers | S | replay |
| 25 | The cloud setting, live: Omni-Compass's machines | 5a Cloud providers | S | replay |
| 26 | The orchestrators' road | 5b Orchestrators and governors | L | record |
| 27 | An orchestrator, four ways | 5b Orchestrators and governors | L | record |
| 28 | The data pipeline, live: every stage from the GitHub Actions run to this page | 5c Kubernetes | L | replay |
| 29 | The official run's heartbeat | 5c Kubernetes | L | replay |
| 30 | The heartbeat sweep: every beat the governor can run at | 5c Kubernetes | S | model |
| 31 | The official run: response time candles | 5c Kubernetes | L | replay |
| 32 | The official run: the heat map | 5c Kubernetes | L | replay |
| 33 | The official run: paired bars | 5c Kubernetes | L | replay |
| 34 | The official run: the repetitions | 5c Kubernetes | L | replay |
| 35 | Per-repetition run telemetry | 5d Kubernetes | L | replay |
| 36 | The shipped controller's trace: native | 5e Kubernetes and cloud | S | replay |
| 37 | The shipped controller's trace: Omni-Compass | 5e Kubernetes and cloud | S | replay |
| 38 | The shipped controller's trace: the strip | 5e Kubernetes and cloud | S | replay |
| 39 | The GPU card, metered: the one real run | 5f Hardware | P | awaiting its run |
| 40 | The CPU host, metered: awaiting its machine | 5f Hardware | S (model) until the run | awaiting its run |
| 41 | An 8-card node: built and awaiting its run | 5f Hardware | S (native model) until the run | awaiting its run |
| 42 | The chip and the host, modelled | 5f Hardware | S | model |
| 43 | The organism, live: native | 6a The organism, live | S | live |
| 44 | The organism, live: Omni-Compass | 6a The organism, live | S | live |
| 45 | The immune system | 6a The organism, live | S | live |
| 46 | The body parts on the band | 6a The organism, live | S | live |
| 47 | Telemetry tensor: the cube | 6b Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 48 | Telemetry tensor: the difference | 6b Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 49 | Telemetry tensor: the modes | 6b Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 50 | Service level: the objective | 6b Telemetry analytics and Omni-Compass in its own words | L (the official run's request log, SHA-256-checked) | replay |
| 51 | Service level: the error budget burn | 6b Telemetry analytics and Omni-Compass in its own words | L (the official run's request log, SHA-256-checked) | replay |
| 52 | Telemetry radar | 6b Telemetry analytics and Omni-Compass in its own words | L (the official run's own gauges) | replay |
| 53 | The console's response | 7 Control console | S | live |
| 54 | The frame budget | 7 Control console | S | live |
| 55 | One control cycle, traced | 8a One control cycle, traced step by step | S | live |
| 56 | Phase plane: native | 8b Phase plane and scoreboard | S | live |
| 57 | Phase plane: Omni-Compass | 8b Phase plane and scoreboard | S | live |
| 58 | The scoreboard strip | 8b Phase plane and scoreboard | S | live |
| 59 | The brain's state: the well | 8c The brain's internal state | S | live |
| 60 | The brain's state: stress S in its potential | 8c The brain's internal state | S | live |
| 61 | The brain's state: the bath B | 8c The brain's internal state | S | live |
| 62 | Native's own controller beside the brain | 8c The brain's internal state | S | live |
| 63 | The verdict: one trial | 8d The verdict | S | live |
| 64 | The verdict: every true cost | 8d The verdict | S | live |
| 65 | Self-governed rendering | 11 Self-governed rendering | S | live |

### L.42 Every knob

| Knob | What it does | Where it is |
|---|---|---|
| Kill switch | Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white) | the kill switch (section L.5; its wiring, section L.9) |
| The dial | the max (every muscle to its own limit) or the tune-down (never more than native) | the console's dial |
| Demand | ×0.25 to ×2 of the day's own demand, both arms alike | the console's demand slider |
| Noise | σ of the demand's noise, one draw a muscle a decision, both arms alike | the console's noise slider |
| Sense delay | decisions added between what a muscle does and what its controller reads, both arms alike | the console's delay slider |
| Faults | a surge, half the machines lost, a sense blind, a security hold, on the chosen body part | the console's fault buttons |
| Speed | 1×, 4×, 16× or 60× of the engine's clock | the console's time knob |
| One decision | step the engine one decision while paused | the console's time knob |
| Pause | hold the engine's clock | the console's time knob |
| Frame load | +0, +8 or +16 ms burned inside every frame of this page | the console's frame-load knob |
| Run | A, B or C (or the archived run) the monitor plays | the monitor's own buttons |
| Repetition | which repetition of the run is replayed | the monitor's own buttons |
| Arm | which arm stands on the right: Omni-Compass governing, or watching only | the monitor's own buttons |
| Stack | the GPU card, the Linux host, Kubernetes or the cloud | the monitor's own buttons |
| Governor | which orchestrator or governor is shown | the monitor's own table |
| Scenario | on-site bare metal, through the cloud, in the device, as a service | the monitor's own buttons |
| Reading | every measured piece carried, or the index's strict rule | the monitor's own buttons |
| The chip's run | the chip's one run beside the count or in it | the monitor's own buttons |
| Beat | the governor's full read of the state and its decision: every 5, 10, 15, 20, 30, 60, 75, 90 or 120 s in the heartbeat sweep's record; on a real governor its --interval (60 s at the factory since omni-v17, 15 s on omni-v16) | the monitor's own buttons |
| Engine | which engine's record the monitor reads: the engine that stands or the one before it | the monitor's own buttons |
| Against | what each reading is set against: native, or the same engine at another setting | the monitor's own buttons |
| Gauge | which gauge of the run is shown | the monitor's own buttons |
| Filter | which rows, words, families or organisms are shown | the monitor's own buttons |
| Body | which body the organism runs: the harness, the organism, every muscle alone | the organism's own buttons |
| The muscle's own switch | pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once | the organism's monitors and the muscle's card (section L.27) |
| Runs | how many of the Python's runs this page computes again | the monitor's own buttons |
| Print | the receipts of the runs, printable, with the digests and the notice | the monitor's own button |
| Seed base | which held-out seed base's 500 scenarios are replayed | the monitor's own buttons |

### L.43 Every LOSS row, whose it is, its cause and the knob that answers it

7 LOSS rows are Omni-Compass against its native; 103 are an orchestrator's own cost against the organism alone, with no Omni-Compass in either arm. Every one is shown as its table writes it.

- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C +5.1% (+1.9 to +8.3) · +8.9% (+4.9 to +12.9) · +9.1% (+0.9 to +17.3). Cause: Job turnaround under Armada, Omni-Compass on the organism alone (V12_ARMADA_4W_BARE.md): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the toy gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): queue: job turnaround, submitted to done, mean (s), A B C +1.4% (+0.8 to +1.9) · +1.0% (+0.4 to +1.7) · +1.2% (+0.7 to +1.6). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the toy gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_TOP.md`): pod start wait, total (s), A B C +80.9% (+37.3 to +124.5) · +104.5% (+46.9 to +162.2) · +54.4% (+20.0 to +88.9). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): response time (ms), 99th percentile, A B C +9.8% (+1.5 to +18.0) · +4.4% (+0.1 to +8.7) · +13.0% (+4.7 to +21.2). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the toy gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): batch: queue finished (s), A B C +0.8% (+0.1 to +1.5) · +0.7% (+0.2 to +1.2) · +0.6% (+0.2 to +1.1). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the toy gate is refused and the muscle stays native.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +5.7% (+1.4 to +10.0) · +6.1% (+0.8 to +11.4) · +45.5% (+5.7 to +85.2). Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (V12_OCM_4W_TOP.md): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): queue: job turnaround, submitted to done, mean (s), A B C +0.9% (+0.2 to +1.7) · +0.9% (+0.1 to +1.6) · +1.2% (+0.6 to +1.8). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the toy gate, the muscle stays native on this stack.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): batch: queue finished (s), A B C +72.4% (+61.8 to +82.9) · +68.6% (+58.6 to +78.6) · +86.7% (+75.6 to +97.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1190995.2% (+1185985.7 to +1196004.8) · +1634917.6% (+1630334.8 to +1639500.5) · +1324419.0% (+1319896.0 to +1328942.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +221050.0% (+220287.4 to +221812.6) · +245633.3% (+245069.1 to +246197.6) · +245750.0% (+245056.6 to +246443.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +528.0% (+478.0 to +578.0) · +469.9% (+426.8 to +513.0) · +904.9% (+825.1 to +984.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C +24 (+24 to +24) · +24 (+24 to +24) · +24 (+24 to +24). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): batch: queue finished (s), A B C +72.6% (+62.2 to +83.1) · +68.4% (+58.3 to +78.6) · +86.7% (+75.4 to +98.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1193142.9% (+1189052.7 to +1197233.0) · +1632935.3% (+1629797.0 to +1636073.6) · +1323895.2% (+1320577.4 to +1327213.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +221366.7% (+220793.7 to +221939.6) · +245383.3% (+244977.9 to +245788.8) · +245666.7% (+245189.8 to +246143.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +529.1% (+479.5 to +578.7) · +469.3% (+425.4 to +513.1) · +904.5% (+823.7 to +985.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C +24 (+24 to +24) · +24 (+24 to +24) · +24 (+24 to +24). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), mean, A B C +365.9% (+157.4 to +574.3) · +387.2% (+211.6 to +562.8) · +271.6% (+1.7 to +541.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 95th percentile, A B C +1362.7% (+633.9 to +2091.4) · +1439.3% (+847.3 to +2031.3) · +986.8% (+75.2 to +1898.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 99th percentile, A B C +1691.7% (+817.5 to +2565.8) · +1837.8% (+1123.2 to +2552.5) · +1233.4% (+145.9 to +2320.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): time over the response line (% of samples), A B C +583748.7% (+317248.1 to +850249.4) · +27.76 (+17.87 to +37.65) · +13.96 (+2.291 to +25.63). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +12.33 (+7.036 to +17.63) · +14 (+10.07 to +17.93) · +8.2 (+2.509 to +13.89). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): time over the response line (% of samples), A B C +21.1% (+5.3 to +36.8) · +37.2% (+12.4 to +61.9) · +29.8% (+1.0 to +58.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BOTH.md`): pod start wait, total (s), A B C +80.9% (+32.7 to +129.0) · +68.8% (+12.8 to +124.7) · +71.8% (+31.7 to +112.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_ORCH.md`): response time (ms), mean, A B C +2.6% (+0.7 to +4.4) · +3.2% (+0.5 to +5.9) · +2.9% (+0.9 to +5.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_VS.md`): pod start wait, total (s), A B C +60.3% (+28.4 to +92.2) · +56.1% (+0.6 to +111.6) · +51.9% (+20.4 to +83.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 95th percentile, A B C +41.9% (+11.7 to +72.1) · +45.9% (+20.6 to +71.1) · +57.5% (+32.2 to +82.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 99th percentile, A B C +45.2% (+12.1 to +78.2) · +48.9% (+22.4 to +75.5) · +62.1% (+33.1 to +91.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): batch: queue finished (s), A B C +5.1% (+1.7 to +8.5) · +6.9% (+3.4 to +10.3) · +5.1% (+3.0 to +7.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1753.8% (+1040.8 to +2466.9) · +1626.7% (+910.1 to +2343.3) · +915.8% (+807.5 to +1024.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +550.0% (+38.6 to +1061.4) · +650.0% (+129.0 to +1171.0) · +128.6% (+70.6 to +186.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +48.0% (+17.8 to +78.1) · +51.3% (+28.0 to +74.7) · +52.5% (+31.0 to +73.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), mean, A B C +13.2% (+1.6 to +24.8) · +15.8% (+8.1 to +23.5) · +18.3% (+7.5 to +29.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 95th percentile, A B C +38.1% (+7.2 to +69.0) · +41.1% (+19.5 to +62.6) · +50.8% (+22.6 to +79.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 99th percentile, A B C +39.9% (+7.8 to +72.1) · +44.0% (+23.2 to +64.9) · +61.3% (+30.8 to +91.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): batch: queue finished (s), A B C +4.2% (+1.6 to +6.9) · +5.7% (+2.8 to +8.6) · +4.6% (+2.7 to +6.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1461.5% (+1162.4 to +1760.7) · +1613.3% (+1157.7 to +2069.0) · +968.4% (+828.5 to +1108.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +300.0% (+115.3 to +484.7) · +550.0% (+225.7 to +874.3) · +100.0% (+31.0 to +169.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +40.1% (+16.1 to +64.0) · +42.1% (+24.1 to +60.0) · +45.2% (+26.8 to +63.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), mean, A B C +45.7% (+15.8 to +75.5) · +33.1% (+14.0 to +52.3) · +25.0% (+7.6 to +42.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 95th percentile, A B C +81.3% (+33.4 to +129.1) · +62.1% (+27.0 to +97.3) · +38.8% (+13.8 to +63.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 99th percentile, A B C +73.4% (+34.4 to +112.5) · +64.1% (+30.5 to +97.7) · +36.5% (+13.7 to +59.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): time over the response line (% of samples), A B C +17.9% (+8.8 to +27.1) · +12.6% (+0.3 to +25.0) · +22.4% (+7.1 to +37.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +45.1% (+21.3 to +68.9) · +34.5% (+21.0 to +48.0) · +30.8% (+18.3 to +43.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): batch: queue finished (s), A B C +16.5% (+7.4 to +25.6) · +15.7% (+8.5 to +23.0) · +14.3% (+5.7 to +22.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +180.0% (+82.2 to +277.8) · +183.3% (+52.1 to +314.5) · +24360.0% (+1893.1 to +46826.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +83.0% (+40.0 to +126.1) · +78.2% (+42.6 to +113.8) · +57.9% (+24.1 to +91.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), mean, A B C +27.9% (+13.5 to +42.3) · +20.4% (+10.8 to +30.0) · +21.6% (+7.9 to +35.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 95th percentile, A B C +51.1% (+21.9 to +80.2) · +38.9% (+18.4 to +59.5) · +35.4% (+13.9 to +56.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 99th percentile, A B C +54.9% (+23.6 to +86.2) · +47.7% (+25.1 to +70.2) · +31.3% (+13.1 to +49.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +34.3% (+13.3 to +55.3) · +22.1% (+12.1 to +32.1) · +31.7% (+8.1 to +55.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): batch: queue finished (s), A B C +11.7% (+5.1 to +18.3) · +11.2% (+6.1 to +16.2) · +11.0% (+5.0 to +16.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +58.2% (+28.9 to +87.5) · +56.1% (+30.6 to +81.6) · +44.2% (+20.7 to +67.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): batch: queue finished (s), A B C +79.6% (+57.4 to +101.8) · +82.5% (+72.2 to +92.7) · +90.2% (+71.9 to +108.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +332575.0% (+204178.2 to +460971.8) · +701433.3% (+502619.2 to +900247.5) · +227980.0% (+149811.1 to +306148.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +172733.3% (+104746.8 to +240719.9) · +763800.0% (+530043.0 to +997557.0) · +136780.0% (+86044.3 to +187515.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +1607.8% (+1081.3 to +2134.4) · +849.4% (+675.6 to +1023.2) · +1322.9% (+1027.8 to +1618.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): batch: queue finished (s), A B C +76.5% (+54.1 to +98.9) · +82.5% (+72.8 to +92.1) · +86.9% (+68.4 to +105.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +310637.5% (+166814.0 to +454461.0) · +686083.3% (+439006.5 to +933160.2) · +233933.3% (+162122.7 to +305743.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +171200.0% (+91149.9 to +251250.1) · +797900.0% (+545467.5 to +1050332.5) · +139600.0% (+101748.5 to +177451.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +1512.7% (+1011.0 to +2014.4) · +831.8% (+691.5 to +972.0) · +1276.6% (+979.1 to +1574.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 95th percentile, A B C +191.2% (+63.6 to +318.8) · +485.5% (+212.9 to +758.0) · +285.6% (+106.4 to +464.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 99th percentile, A B C +181.3% (+56.9 to +305.8) · +481.6% (+212.0 to +751.1) · +285.0% (+116.9 to +453.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +4.9 (+0.7503 to +9.05) · +8900.0% (+4446.3 to +13353.7) · +9500.0% (+6140.7 to +12859.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): response time (ms), mean, A B C +85.7% (+68.2 to +103.3) · +85.1% (+68.5 to +101.7) · +67.0% (+49.1 to +84.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): time over the response line (% of samples), A B C +212.8% (+175.6 to +250.1) · +223.2% (+172.9 to +273.6) · +207.9% (+172.9 to +243.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +202.8% (+146.0 to +259.6) · +216.4% (+168.3 to +264.6) · +157.0% (+115.5 to +198.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): batch: queue finished (s), A B C +89.3% (+79.7 to +98.9) · +80.1% (+69.7 to +90.5) · +80.8% (+71.6 to +90.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1967119.6% (+1111934.3 to +2822304.9) · +1287745.8% (+521467.2 to +2054024.4) · +1250833.4% (+747221.5 to +1754445.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +1001696.3% (+623421.0 to +1379971.7) · +230987.0% (+116467.0 to +345506.9) · +285052.5% (+193399.9 to +376705.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +1067.6% (+891.6 to +1243.7) · +910.0% (+690.2 to +1129.8) · +774.9% (+649.7 to +900.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C +13.44 (+7.163 to +19.73) · +11.3 (+3.858 to +18.74) · +14.5 (+8.326 to +20.67). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): response time (ms), mean, A B C +87.9% (+61.0 to +114.8) · +86.6% (+61.9 to +111.4) · +70.6% (+49.8 to +91.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): time over the response line (% of samples), A B C +221.2% (+183.5 to +258.9) · +234.2% (+179.7 to +288.8) · +217.5% (+182.6 to +252.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +204.2% (+145.9 to +262.4) · +219.2% (+169.2 to +269.1) · +159.1% (+116.0 to +202.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): batch: queue finished (s), A B C +90.4% (+80.4 to +100.4) · +80.6% (+70.9 to +90.3) · +81.4% (+72.4 to +90.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1959438.6% (+1137492.1 to +2781385.0) · +1280430.0% (+511805.8 to +2049054.2) · +1238207.0% (+751232.1 to +1725181.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +1015791.5% (+684899.6 to +1346683.4) · +228574.2% (+114225.9 to +342922.5) · +286211.2% (+190609.6 to +381812.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +1067.4% (+882.4 to +1252.3) · +927.0% (+727.3 to +1126.7) · +779.3% (+655.6 to +902.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C +14.33 (+8.22 to +20.45) · +11.1 (+3.755 to +18.44) · +14.6 (+8.613 to +20.59). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): response time (ms), 95th percentile, A B C +9.5% (+1.9 to +17.1) · +13.4% (+3.4 to +23.4) · +15.4% (+7.8 to +22.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): batch: queue finished (s), A B C +1.0% (+0.3 to +1.7) · +1.6% (+0.8 to +2.5) · +1.9% (+1.1 to +2.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +12.5% (+3.2 to +21.8) · +13.8% (+6.4 to +21.3) · +16.6% (+8.6 to +24.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), mean, A B C +7.3% (+0.0 to +14.5) · +6.4% (+1.8 to +11.0) · +8.9% (+3.7 to +14.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), 95th percentile, A B C +12.8% (+0.3 to +25.2) · +10.0% (+1.4 to +18.7) · +10.2% (+2.9 to +17.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +178.6% (+75.7 to +281.5) · +118.2% (+22.2 to +214.1) · +537.5% (+313.8 to +761.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +11.5% (+0.3 to +22.7) · +9.3% (+2.0 to +16.5) · +12.7% (+5.4 to +19.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), mean, A B C +59.9% (+38.6 to +81.3) · +51.7% (+23.3 to +80.0) · +58.7% (+37.1 to +80.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 95th percentile, A B C +51.5% (+36.6 to +66.4) · +55.2% (+22.4 to +88.0) · +55.0% (+29.0 to +81.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 99th percentile, A B C +49.4% (+31.0 to +67.8) · +58.4% (+25.9 to +90.9) · +52.9% (+30.2 to +75.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): time over the response line (% of samples), A B C +55.9% (+30.2 to +81.5) · +23.9% (+11.2 to +36.5) · +75.5% (+53.5 to +97.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C +24.8% (+18.0 to +31.6) · +26.6% (+20.5 to +32.7) · +74.3% (+40.2 to +108.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): batch: queue finished (s), A B C +21.4% (+16.0 to +26.8) · +19.4% (+11.5 to +27.4) · +19.1% (+13.1 to +25.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +14475.7% (+1985.4 to +26966.0) · +15860.7% (+1447.0 to +30274.5) · +17305.6% (+349.2 to +34262.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +22685.7% (+4894.5 to +40476.9) · +13100.0% (+1240.5 to +24959.5) · +16980.0% (+170.1 to +33789.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +70.9% (+54.6 to +87.2) · +67.7% (+38.0 to +97.5) · +76.8% (+55.5 to +98.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): batch: queue finished (s), A B C +15.0% (+9.3 to +20.7) · +15.9% (+9.3 to +22.6) · +16.1% (+4.7 to +27.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +47.9% (+27.4 to +68.3) · +57.0% (+30.7 to +83.2) · +46.0% (+18.7 to +73.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, total (s), A B C +466.7% (+186.8 to +746.5) · +2.4 (+0.9225 to +3.878) · +1.3 (+0.4047 to +2.195). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, mean (s), A B C +266.7% (+26.9 to +506.4) · +1.25 (+0.6136 to +1.886) · +0.8 (+0.2615 to +1.338). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): batch: queue finished (s), A B C +1.8% (+0.8 to +2.8) · +1.7% (+0.4 to +2.9) · +1.8% (+0.4 to +3.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1126.7% (+1020.2 to +1233.2) · +1088.9% (+690.1 to +1487.7) · +1416.7% (+986.8 to +1846.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +333.3% (+174.4 to +492.3) · +450.0% (+38.7 to +861.3) · +550.0% (+436.9 to +663.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C +32.1% (+13.4 to +50.8) · +19.7% (+5.5 to +33.9) · +26.0% (+8.1 to +43.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): batch: queue finished (s), A B C +1.2% (+0.6 to +1.8) · +1.4% (+0.4 to +2.5) · +1.4% (+0.3 to +2.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C +1053.3% (+883.9 to +1222.8) · +866.7% (+664.7 to +1068.6) · +1491.7% (+1085.0 to +1898.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C +366.7% (+231.3 to +502.0) · +275.0% (+78.2 to +471.8) · +500.0% (+331.4 to +668.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C +24.2% (+10.9 to +37.5) · +17.6% (+5.6 to +29.5) · +23.2% (+6.9 to +39.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), 95th percentile, A B C +92.6% (+46.7 to +138.5) · +31.9% (+10.8 to +53.0) · +50.9% (+23.2 to +78.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): time over the response line (% of samples), A B C +124.1% (+51.4 to +196.7) · +50.2% (+5.7 to +94.8) · +54.8% (+19.1 to +90.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.

## Index

Every glossary term where the book defines or discusses it, every muscle family, every file of the repository and every setting the book names, with the pages they stand on in the printed book (this one-file text has no pages).

## Contact

The Omni-Compass LLC. Owner and developer: AJ Dubra. Main office infrastructure: toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1; landline, registered in Florida, 321-746-4411. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
