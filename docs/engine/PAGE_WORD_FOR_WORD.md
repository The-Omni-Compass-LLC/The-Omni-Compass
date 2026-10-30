# The Live Benchmark Engine Page, Word for Word

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This appendix is the live engine page itself, written from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build of this book (`docs/book/build_live_manual.py`): every section in the page's own order with its number, title, summary and controls line; every monitor under the number its badge carries, with its evidence class, its state, the open-source feed that would carry it on a running system and its knobs; every knob; and every LOSS row with whose it is, its cause and the knob that answers it. Nothing here is typed twice: what the page says, this appendix says, so the book and the page read each other both ways. This edition was written from the page built 2026-10-27 02:22 UTC on omni-v21 (digest b658f05d43c1e602) from commit 36f9bd511269.


Each part below is one section of the page, in the page's order and under its number: what the page says it is, its controls, its panels, and every monitor in it under its own number, with what it shows, its evidence and state, the feed that would carry it live, its knobs, how to read it and what to do with it.

## ii Title page and build

**The page, in its own words.**

A live monitor of the Omni-Compass engine and of every benchmark GitHub has run on it: each run played back from its own SHA-256-checked files, each model run by the repository's own code, so the engine can be watched moving instead of only read. Two sides everywhere, and only two: Native, the whole system running by itself, and Omni-Compass and native, the same system with Omni-Compass on top of all of it. On this page Omni-Compass is never run by itself (the founder's order of 25 October): it always sits on top of a native controller. Beside this title stand the owner's two pictures, each with the engine's live marks over it. It reads from the top down, as its table of contents lists it: the bottom line and the contents; Part 1, the monitors and the main control panel; Part 2, what they say together; Part 3, every monitor spread out; Part 4, the organisms and everything else, the problem and the answer, the executive summary and the reading key, the glossary and the index among them; and the disclosures. The engine that stands is omni-v21 (`docs/OMNI_V21.md`); its road from omni-v11 is in the disclosures (section v). The engine that stands still carries the code omni-v18 and omni-v19 added to run Omni-Compass by itself (its own orchestrator and a pod muscle of its own); it is an opt-in start flag outside the factory tune, and this page shows none of it. Its only modelled record read LOSS: the record of 24 October carried that third arm, Omni-Compass by itself, and it read LOSS in all three of our runs on work and on muscles over the line in eight organisms, 32 rows (class S); the founder's order of 25 October took the arm off this page, and its record is kept whole in `docs/history/SCENARIOS_30_2026-10-24.md`.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 0 The answer first: is Omni-Compass a benefit against native?

**The page, in its own words.**

**The two bills**

**Its monitors.** This section draws no canvas: it is words and their sources, written in the page itself.

## iii The bottom line: is Omni-Compass a benefit? One light and one number for each way to run it, against native

**The page, in its own words.**

How to read it. Each row is one way to run a workload, against native alone on the same work. The light is the whole verdict: green THRIVING, Omni-Compass ahead of native; yellow STEADY, within 0.5% of native (EVEN by the key's floor); red REDLINING, behind native. The big number is how much: on the first row more work done for the same demand, on the bills and the index one number over their gauges, read by the key (GAIN, EVEN, LOSS by what the gauge is for, never by its sign; EVEN only under 0.5%, the mean of the three runs' changes). A slower service, less work or a failed request turns the light red whatever the number, on every row, the index's included. Each row names what it stands on: its test, its engine and its evidence class.

**The way to run it: a real test on Omni-Compass's own orchestrator, three runs on GitHub's machines (no Kubernetes)**

**The two bills a whole workload is bought by: on site, or through the cloud**

**Every real test together**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## Part 1 of the page: The monitors and the main control panel

## 1a The monitor wall: every monitor, numbered 1 upward in its order of appearance, read left to right

Every monitor of this page at once, numbered in the order it appears from the top, 1 first, and read left to right, then the next row, as any page is read; the last number is the last monitor on the page. Two monitors that sit side by side in their section, native beside Omni-Compass, stay side by side on the wall. Each tile carries at its top its number and its title, what the monitor shows, with its section and its state under them; the numbered list beside it (4l) says the rest.

**Controls.** Live: click a tile to go to its monitor; every tile is read again four times a second.

**The page, in its own words.**

**The monitor wall: every monitor of this page, numbered 1 upward in its order of appearance, read left to right, then the next row; click a tile to go to it**

The same canvases the sections draw, copied small four times a second; nothing is drawn twice from different data. The page's own governor (section 4i) leaves a monitor resting while it is off screen, so while this wall is in view the resting monitors are drawn in turn, one a frame, each through its own drawing code; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to. Two monitors that sit side by side in their section, native beside Omni-Compass, sit side by side on the wall too: a pair never splits across two rows. Each tile's head is its number and its title in capital letters, then its section and its state (live, replay, from the records, a model, or awaiting its run). A tile with the accent border is a monitor on screen now; the list of every monitor by its number follows in section 4l.

**The main control panel: every monitor switched from one box**

**How to use the control panel**

How to use it. The first row is the master switches: each acts on the whole page at once, through the same code as the console and the dock, both sides alike (the kill switch hands everything back to native; the dial, the body and the time). Under it, five tabs: Drive (the plant's conditions and faults, the heartbeat, the profile with its actuation, its contract and each route's bill), The mechanism's knobs (the engine's own constants, one group at a time), The twenty scenarios, The breakers (one per monitor: its light and word, green GAINING, yellow STEADY, red REDLINING; ON runs it live, REST stops its drawing; a way to it) and Everything (the whole panel at once). Every switch is logged with its decision; Back to the factory tune puts all of it back.

**The mechanism's own knobs (fold or unfold)**

**The mechanism's own knobs: the four pieces, the compass law, Omni-Compass's hand, native's controller, every muscle**

**What these knobs are, and how to read them**

What these are. Not the plant's conditions above: these turn the engine's own equations while it runs. Each knob is a constant of the brain (omnicompass/core.py), the compass law (omnicompass/compass_law.py), the governor's law (omnicompass/adapter.py, nervous_system.py), Omni-Compass's hand on each muscle, the model's native controller, or one muscle's body. Turned, the next decision of the live stress-test model is computed with it, on Omni-Compass's side; native's controller knobs move every native controller, the one under Omni-Compass on native too. The harness replays recorded positions, so turning a knob moves the live benchmark engine to the model. How to read it. A knob turned from the factory turns violet; ↺ puts that one back; the factory button above puts every one back. Watch the monitors (the strip, the rings, the phase plane, the brain's state, the health board): the mechanism of action changes in front of you. A tune other than the factory's is a variation of the mechanism (class S, our own model): the benchmarks prove the factory tune only, and a changed tune's results are its own. Where each piece acts. The compass law, Omni-Compass's hand, native's controller and every muscle's body move the muscles at once. The brain's four pieces move its own state (E, U, I[U], S, B on the brain's monitors) and its grants: at the max every organ may add capacity unless a security hold stands, so the brain's calm acts through the give-backs; set the dial to the tune-down to watch the four pieces move the muscles too.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 1b The control panel and the kill switch: one switch for the whole organism, the Python's runs, the three manuals

The first view after the front matter: the control panel that drives every monitor of this page. The kill switch stands at its head, ON in green while Omni-Compass governs on top of native, red when engaged, and Omni-Compass OFF in white; the Python's own runs can be run again here at a button, and one switch activates the Python's jump generator, set after set of 500 into the monitors, its OFF state the page's standing mode, said under it; the three manuals are a click away. The monitors it drives follow: the wall of every monitor (1a), the numbered list of them (4l), the status board (2a), the master switch's wiring (4f), the Python's runs in this page (3o), every LOSS row (2c), the golden signals (2b) and GitHub's pipeline (4e). No value here is typed in: each is computed at runtime from the live benchmark engine or from the repository's records embedded at build time.

**Controls.** Live: the kill switch acts at once on every governor of this page; the buttons run the Python's runs here and fetch the three manuals.

**The page, in its own words.**

**The control panel: one switch for the whole organism, the Python's runs in this page, the three manuals**

ON: the page draws set after set from the Python's jump generator, 500 runs a set unless another size is chosen, one base after another (run k of a set takes the seed base + k·0x9E3779B9 mod 2³², its stream mulberry32, the generator tools/engine_runs.py and tools/core_runs.py write bit for bit). Each set runs twice in this browser: through the engine's runs (288 decisions of the brain, 80 steps of the compass law and one give-back trial a run; the proof monitor, 1f) and through the core's Monte Carlo (the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps a run, native beside Omni-Compass; the Monte Carlo monitor, 1f). Each set's output is its 500 runs, their counts and one SHA-256 digest; where the Python has run the same base its record's digest stands beside this page's, and they must be equal. It runs until the switch is pressed again, and rests while the page is hidden. Class S: the engine's own mathematics on draws, never a measurement.

OFF (the page's standing mode, as it opens): nothing new is drawn from the generator. The page plays its records: the Monte Carlo monitor plays the Python's own 500 (benchmarks/core_evidence.py, numpy's generator from seed 223387268, the record results/core_evidence.json); the proof monitor recomputes, once as the page opens, the newest set GitHub ran in the Python and checks it digest for digest, then re-checks it one run at a time; the 500 scenarios a seed replay from their record with every trace hash; GitHub's runs play back from their own raw files; the organism's model day (sections 3a, 3b and 3d to 3g) runs on its own seeded stream, the same at every opening. A button above or in section 3o still runs one set at a time.

Each knob sets every monitor that carries its variation and names them here; a monitor that does not carry it is left as it is.

The kill switch. While Omni-Compass governs on top of native the switch reads ON in green. Pressed, it turns red: at the next decision every governor puts every setting it wrote back, reads each one back and stops (omnicompass/master.py, tools/omni_switch.py); the word OFF stands white, and every Omni-Compass side of every monitor follows native, drawn in native's colour. Native's own controllers under every muscle never stop and never see the switch. A recorded result never changes with it: its colour does, never a value, a word or a row. The same switch stands at the head of every section and in every monitor's own knobs; one press anywhere is one press everywhere. It is for security and is instant; the walk back after a crash is the lease, separate.

The three manuals. The Live Benchmark Engine Manual reads this page top to bottom: how to read, operate, tune and watch it, native beside Omni-Compass, chapter by chapter in the page's own order, and, in its last appendix, the page word for word, every section, every monitor under its number and every knob, written from this page at every build. The Operator's Manual wires and runs Omni-Compass on a stack; the Owner's Manual holds the whole mechanism, its mathematics, its source and every result. Each carries the notice, the LICENSE, the NOTICE and `DISCLOSURES.md`.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 1c The dashboards: the live benchmark engine in every form an operations team reads a system

**The page, in its own words.**

The same live benchmark engine, drawn the ways the industry draws a system: a board of panels, a host map, a graph of one series, an event stream, a cluster console with a button on every workload, a one-line diagram with its breakers, a wall of numbers, the cost of each body part, and Omni-Compass's own form, the two-way pipeline that reads, decides, writes and reads back. Each is fed by this page's own model as it runs (class S), native in orange beside Omni-Compass in blue, each change with its word by the key; the forms are the industry's, the numbers are this engine's, and no vendor's product is drawn or implied. The level sets how much each form gathers: each muscle, each body part, or the whole organism.

**Who does what: the words for every tool a reader may know, and where Omni-Compass sits**

**The ones that compete: the first five benchmarks to run**

Each takes its own preregistration (the knobs it owns, the muscles left native, its learning window), a trial run that is never counted, and its three runs; a vendor's licence is read for evaluation and publication first. Every other product, the observers, the consoles and the native controllers, with its sources: `docs/THE_FIELD.md`. A vendor's savings figure is that vendor's own claim.

Plain words for the rest: a muscle is any machine, service or controller Omni-Compass can read and set; native is the system as it runs without Omni-Compass; a write is one setting Omni-Compass changed; read back means it checks the setting landed; the lease walks every setting back to native after a crash; the kill switch stops Omni-Compass at once, for security. Every benchmark puts Omni-Compass on top of a native setup and reads both sides by the same key.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## Part 2 of the page: What the monitors say: the synopses

## 2a The status board: the tiles, the alarms and the watch items

Whether Omni-Compass is engaged, which signals are out of tolerance and where, and every LOSS row raised as an alarm with its source record. Each tile and each alarm is computed at runtime from the live benchmark engine or from the repository's records.

**Controls.** Live: the filters act at once, and every tile is read again four times a second.

**The page, in its own words.**

**Alarms and watch items, by severity**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 2b The golden signals, the event log and the live metrics

The live organism's four golden signals, native beside Omni-Compass, one point a decision: errors (muscles over the line), throughput (work served), latency and saturation; the engine's own event log, newest first; and the same metrics in the OpenMetrics format Prometheus scrapes and Grafana charts.

**Controls.** Live: one point a decision from the live benchmark engine; the event log's filters act at once; the metrics refresh every two seconds.

**The page, in its own words.**

**Golden-signal feed, live: the last 240 decisions, native beside Omni-Compass**

One point per decision streamed from the live benchmark engine, gapless, each signal on its own axis, with each arm's last, mean and maximum as a time-series dashboard reports them; a kill-switch window is shaded red. Native in orange, Omni-Compass in blue, the same demand on both.

**Engine event log, newest first**

The live benchmark engine's own events as it emits them, with the wall-clock time and the decision. They are a threshold breach and its clearing on either arm, every injected fault and its end, the kill switch, the dial, a new day, and the brain's calm crossing the grant threshold. ALERT, WARN and INFO as an operations log grades them.

**OpenMetrics exposition: the live metrics, ready for Prometheus and Grafana**

The live benchmark engine's metrics in the OpenMetrics text format, the CNCF exposition format Prometheus scrapes and Grafana charts, refreshed every two seconds. They are engagement, the decision index, breaches, work, band time, actuator moves and reversals per arm, and frame time. Then the verdict's keep ratio at each true cost, the three-run tables' rows by class and reading, and the build's engine, digest and commit.

The board is laid out the way an operations monitor is. The switch and the engine come first. Next come the live organism's signals, native beside Omni-Compass, in the four a service is watched by (site reliability practice: latency, traffic, errors and saturation): here the work waiting, the work done, the decisions past their line and the capacity held. Then every reading of the real and modelled runs that went against native, worst first. Last come GitHub and the age of this page. A tile's word is its reading against native by the key (front matter, iv). A tile with no reading says what it shows.

**Its monitors.**

### Monitor 1: Golden signal: errors

Errors a decision on the live organism, native beside Omni-Compass (site reliability's first of four).

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client), kube-state-metrics for pod restarts; series `http_requests_total{code=~"5.."}`, `kube_pod_container_status_restarts_total`; on a running system: `sum(rate(http_requests_total{code=~"5.."}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 2: Golden signal: throughput

Work done a decision (traffic), native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client); series `http_requests_total`; on a running system: `sum(rate(http_requests_total[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 3: Golden signal: latency

Response time a decision, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own duration histogram; series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 4: Golden signal: saturation

Capacity held against capacity used, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** node_exporter; series `node_cpu_seconds_total`; on a running system: `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

## 2c Every LOSS row: its cause and the knob that answers it

Every LOSS row of every three-run table on this page, Omni-Compass's own first and then the orchestrators' own, each with the cause the repository records and, where that cause is the governor's, the knob that brings it STEADY or leaves the muscle native; where the cause is the test machine, or not yet established, the row says so and asserts no knob. No row is cut and no number is tuned.

**Controls.** Recorded data: every row is read from the three-run tables on this page.

**The page, in its own words.**

**Every LOSS row: its cause and the knob that answers it (Omni-Compass's own rows first, then the orchestrators' own cost)**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 2d The benefit board: every domain, native against Omni-Compass

This section gathers every benchmark's measured effect in one board, native against Omni-Compass on top of native, by domain and by gauge family, and the Omni index that weighs them together. Every bar is its table's own word (GAIN green, EVEN yellow, LOSS red, power given blue) beside its size; every LOSS row of the benchmarks on this board stands on it, and every LOSS row of every three-run table, the governors' four-ways tables and the service variants included, is raised on the status board (section 2a) and answered, with its cause and its knob, in section 2c. The whole organism composed from these same tables follows in section 4a; every table, every muscle and the grid in full in section 4c.

**Controls.** Recorded data: every receipt as the repository holds it. The kill switch recolours a recorded result and never rewrites it; console controls never modify it.

**The page, in its own words.**

**The benefit board: every domain, native against Omni-Compass**

**Where the benefit lives, gauge by gauge**

Every judged row of every newest three-run table (the tables below), sorted into the family of gauge it measures. A CTO reads speed, the service level, failures and work. A CFO reads machines, energy and the bill. A plant engineer reads peaks and swings, wear and accuracy, and misses. Each bar counts the rows that read GAIN in all three runs; the size beside it is the median of those rows' own sizes (the middle of runs A, B and C). Power given and LOSS rows are counted beside them.

**The trading floor: every three-run table on one screen, the market map and the quote board**

Every three-run table on this page (the tables of section 4c, as GitHub's runs wrote them) read the way a trading floor reads its market. The map: one tile a table, grouped by stack, its area the gauges it judged and its colour its reading: green GAIN, the deeper the more of its rows; red where any row reads LOSS; yellow STEADY; blue where it gave power; grey with a dashed edge an orchestrator's own cost, with no Omni-Compass in either arm. The board: one quote a table, its ticker and engine, the gauge that moved most with its mean change, and that gauge in each of the three runs (A, B and C) as a candle, the bar its 95% interval and the tick its value against the zero line; the strip under it counts the table's rows by word, and the tape runs every headline across the top. Point at a tile or a quote for its record. Nothing here is typed in: every figure is the table's own.

**Aggregate: one figure for the whole board**

**Its monitors.**

### Monitor 5: The benefit board

Every domain's three-run table as one bar: GAIN, STEADY, LOSS and power given, native against Omni-Compass.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawBenefit, fxCursor` → the Python `tools/benefit_sheet.py`, `tools/omni_index.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the bars, one benchmark at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 6: Where the benefit lives, gauge by gauge

The same tables by gauge family: work, speed, misses, resources.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawFam` → the Python `tools/benefit_sheet.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the families, one at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 7: The market map: every three-run table a tile

Every three-run table on the page as a tile of a squarified treemap, grouped by stack: its area the gauges it judged, its colour its reading (GAIN green, LOSS red, STEADY yellow, power given the accent, an orchestrator's own cost grey and dashed).

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawTradeMap` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The scan cursor walks every tile, one every 1.5 s.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 8: The quote board: every three-run table a quote

Every three-run table as a quote: its ticker and engine, the gauge that moved most with its mean change, that gauge in runs A, B and C as a candle (the 95% interval and the value), its rows counted by word, and a tape of every headline.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawQuotes` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The tape of the headlines runs across the top at 55 px a second.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

## Part 3 of the page: Every monitor, spread out

## 3a The organism, live: native and Omni-Compass

The system rendered as an organism: each node is a muscle (one controlled actuator) and each ring its operating range. The left instance runs under its native controllers alone; the right runs the same controllers with Omni-Compass's brain, nerves, heart and immune system supervising them. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: the rings, the immune system and the anatomy respond to the console.

**The page, in its own words.**

Every view is run twice on the same body, the same load and the same seed: native (left), then Omni-Compass (right). "One organism" is the sixty muscles in one body: the whole native organism on the left, the same organism with Omni-Compass on the right; "each muscle alone" runs each muscle native and then with Omni-Compass, one at a time. The counters under each ring and the scoreboard (section 3e) give both arms and the difference. Where the two sides look the same, they are the same. Under the max a muscle is moved only where it has room above native. A muscle already at its limit on native (— of these sixty) is left native by design. Inside one organism the bone, the power and cooling the whole body shares, holds most moves back. A dashed white ring marks every muscle that differs between the two sides at that moment; the counter under each ring counts them. In these harness views the max acts muscle by muscle and the brain at the center reads the body without steering it, as in the realms harness itself; section 3l shows the live controller, where the brain's rules run every decision.

**Reading the rings: a quick-start guide**

**Native**

**Omni-Compass**

**The body scan: every organ, native and Omni-Compass, live from the official run playing**

As a scan reads a living body organ by organ, this reads the system playing in section 3j (the benchmark, run and repetition chosen there), organ by organ, half minute by half minute, from its own SHA-256-checked files: native beside Omni-Compass. Where native has no such organ the cell says so.

**The immune system, live: native beside Omni-Compass (the immune system is Omni-Compass's; native runs on its own controllers)**

The body keeps itself healthy the way a human body does. Every room and every machine pool has a native twin: the same muscle under its own controller, on native's heat and load, the body's memory of healthy. A room that stands warmer than its twin is inflamed. Where its own knob can cool it, it is cured on the spot. Where it cannot, it sends the whole body a signal, its heat debt, like a cytokine calling for help. The other muscles answer: the machine pools give back what Omni-Compass added until the room stands no warmer than native's. The skeleton (the bone: the power and cooling lines the whole body shares) grants nothing it cannot carry. A cooling setting is walked back, never snapped. A pool never loses a machine its queue needs, a battery is timed for its line, and no sense is locked. On the ring a pulsing red circle marks the inflamed muscle, and red signals run from it to every machine pool that answers it.

**The anatomy, part by part, in the order of control: the brain first, the whole organism last**

**Its monitors.**

### Monitor 9: The organism, live: native

Sixty muscles of the stress model, each on its own native controller, at their positions in the band.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); kube-state-metrics; series `omni_recommended`, `kube_horizontalpodautoscaler_status_current_replicas`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position in the band.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; The muscle's own switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 10: The organism, live: Omni-Compass

The same sixty muscles with Omni-Compass on top of their native controllers, the brain's grants and pushes.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_recommended_moves_total`, `omni_writes_total`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position, the brain's grants and pushes pulse.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; The muscle's own switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 11: The immune system

Where the two sides differ, and the body's heat debt: a room warmer than its native twin, inflamed, given back.

- **Evidence and state.** Class S; live.
- **Feed.** Prometheus Alertmanager; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `ALERTS`, `omni_compass_decisions_total{zone="wall"}`; on a running system: `sum(ALERTS{alertstate="firing"})`; `increase(omni_compass_decisions_total{zone="wall"}[1h])`.
- **Wired.** This page's `drawImm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py`, `realms/compass_arm_v5.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each side's pools, warmest room and muscles past the line take a point.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 12: The body parts on the band

Each body part's muscles (the spine and the four realms) at their positions in the band, native above and Omni-Compass below, every decision.

- **Evidence and state.** Class S; live.
- **Feed.** the realms harness's own record (realms/harness.py, each body part's muscles at their positions in the band, recorded by docs/engine/export_harness_trace.py); no Prometheus feed.
- **Wired.** This page's `drawSwarm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's dot moves to its position in the band.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

## 3b Control console: every runtime control of the live benchmark engine

The engine these knobs turn is the engine's own mathematics running in this page: the brain (omnicompass/core.py, integrated by RK4), the compass law (omnicompass/compass_law.py) and the verdict (omnicompass/verdict.py). docs/engine/check_live_engine.py proves the port equal to the Python and the C++ on every build. It governs the stress-test model's sixty muscles (class S), each on top of its own native controller. Every knob acts on both sides at once, the same demand, the same draw of noise, the same lost pool, so the one difference left between them is Omni-Compass. The knobs move the live benchmark engine in sections 3a and 3d to 3f, and the kill switch and the frame load also move this page's own renderer (section 4i). A recorded run (the benefit board, the chips' and Kubernetes' replays, the official runs) is a record: no knob rewrites it.

**The page, in its own words.**

Do no harm. Every control here acts on both arms alike; what Omni-Compass does with them is held by its guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another, a give-back tried against native first and refused on a LOSS. Its one meaning is written once, in the back matter (v) as `DISCLOSURES.md` section 3 writes it.

What these controls do. Runtime parameter control and fault injection on the live benchmark engine: load scaling, noise injection, sensor latency, capacity loss, a demand surge, a sensor blackout, a security hold, the dial, and the kill switch. Every control is applied to both arms identically; the response is plotted per decision, native beside Omni-Compass.

**System response, per decision**

**Frame timing: the inter-frame interval against the 60 Hz budget**

**Control event log, newest first**

**Control-loop performance assessment, this day (live)**

**Its monitors.**

### Monitor 13: The console's response

The last 120 decisions of the live benchmark engine: the muscles past their line and the work, native beside Omni-Compass, every knob of the console turned marked.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawDeskCv` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: both lanes slide one decision, a ring opens at each head with its newest value; every knob turned is marked.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused; Pause: hold the engine's clock; Frame load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live benchmark engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

### Monitor 14: The frame budget

The time between frames of this page against its line under the frame load knob.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawFrameCv` → the Python none: the page's own frame clock, measured in the browser; there is nothing to port → the C++ none: the page's own frame clock, measured in the browser; there is nothing to port.
- **Moves.** Every frame of this page.
- **Knobs.** Frame load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live benchmark engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

## 3c The heartbeat dial: every beat beside native, what it buys and what it costs

The governor's heartbeat, its full decision, is a dial from omni-v17 on: the main engine decides every 60 s, and any of six beats can be set on this page, 10, 15, 30, 60, 90 or 120 s, with the fast checks (the scheduling floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat. Every clock of the governor counts seconds (omni-v16), so turning the dial changes only how often it looks. Each beat stands beside native with what it buys (the reads of the cluster a day) and what it costs (the governor's own processor, and every service row read against native and against the main engine's 60 s), because an operator may want a fast beat for its reads and accept what it costs, or a slow one. At each beat the other knobs may want their own combination; that tuning is the next study, in our own models first. The governor's own screen counts the time since its last decision in beats of the setting it runs at and alerts after three (omni_heartbeat_seconds, deploy/grafana/omni-compass.json, deploy/prometheus/omni-compass-rules.yaml).

**Controls.** Recorded data: every beat of the Kubernetes governor read in our own models (class S, results/model_gate/V17_LADDER.json, tools/beat_ladder.py); the real runs at every beat (`docs/PACE_PREREGISTRATION.md`, amendment 3) join their place when their three runs land. The beat itself is set on the governor's command line (--interval) or with the control panel's heartbeat button (POST /v1/beat, tools/omni_control.py: one button for each stop of the dial), which hands every setting back and starts the governor again at the new beat.

**The page, in its own words.**

**Every beat, in our own models**

How to read it: each value is the beat's mean over seeded days on a plant that moves every 5 s, the same seeds and plant at every beat; the word beside it is its reading against native, paired by seed (GAIN, EVEN, LOSS, power given: the key, section 4k). The second table reads each beat against the main engine's 60 s. Native has no governor, so its reads and processor are blank. The reads are what a beat spends to look more often, shown as the key reads a resource spent: power given. A LOSS here is the engine's at that beat, a model's reading (class S): it stands in this table and on the next version's list; section 2c lists the LOSS rows of the three-run tables of real software, never these.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 3d One control cycle, traced step by step

One control cycle traced end to end at reduced speed: the sensed inputs, the brain's decision, and the actuator (muscle) it wrote. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: the cycle and the controls below share the console's state.

**The page, in its own words.**

**One decision, in the order the code runs it**

**Controls**

The max: every muscle to its own limit, never below native; the capacity it holds is power given. Tune-down: never more than native, and a step back only with the organ’s grant and the release gate. In this model native already sits near its band, so the tune-down finds little to hand back; the scoreboard (section 3e) reads its runs A, B and C live when the dial is on the tune-down. The spread of positions can widen a little, because the calm muscles it hands back move toward their line while the busy ones stay.

Each stress lasts 40 decisions from the moment you press it. Both arms meet the same demand.

**Its monitors.**

### Monitor 15: One control cycle, traced

The compass band with its cushions, the two forces and one decision, step by step.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawBand` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** One control cycle traced step by step on the followed muscle, every decision.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3e Phase plane and scoreboard

The phase-plane state of every muscle (its position and velocity in its band) for both arms at the same instant, with the running scoreboard. Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Controls.** Live: every plane, strip and well responds to the console.

**The page, in its own words.**

How to read the plane. It is a phase portrait, the picture control engineers use for a system's state. Across is where each muscle sits in its band: p is 0 when calm, 0.5 at the center and 1 at its line. Up and down is how fast it moves there (v, per decision). A muscle at rest sits on the middle line. One climbing toward its line moves up and right, and past the right edge it is past its line. Native is on the left and Omni-Compass on the right: the same muscles at the same instant, one dot each. In the realms harness each muscle answers to its own rule, so no single field is drawn. In the stress-test model the shading on the right is the force the compass law would apply there: the add force gives capacity and the hand-back force returns it. Past the 0.95 wall the law fails up at once. Under each plane, the same instant in words.

**Native**

**Omni-Compass**

**Live stat panels: native beside Omni-Compass, now and over the last 120 decisions**

Each panel is one gauge of the live organism, read every decision on both sides, as an operations dashboard shows it. It gives native's value now and Omni-Compass's, the last 120 decisions of both (native solid orange, Omni-Compass blue), and the running paired reading in the tables' words. With the master switch OFF the decisions are shaded red and Omni-Compass's side follows native: its value equals native's and its line is drawn in native's colour, dashed on top of native's, so both stay in view.

**Native against Omni-Compass**

How each row is read: the paired change, native against Omni-Compass at the same decision, averaged over blocks of ten decisions so neighbouring decisions do not count twice, with its 95% interval (Student’s t over the blocks). This run (tools/readings.py, run_word): a change under 0.5% of native reads STEADY; 0.5% or more, the word follows the gauge’s aim (work: a rise is GAIN; misses, failed work, waiting: a fall is GAIN; energy or capacity held: a rise is power given, a fall a cut), its 95% interval printed beside it. Three runs (tools/readings.py, three_run_reading): the change is the mean of the three runs' changes; under 0.5% it reads STEADY, under the floor; 0.5% or more reads GAIN, LOSS or power given by the gauge's aim, “in all three of our runs” when every run went the same way clear of zero, otherwise “by the mean of our three runs” with the count of runs beyond the noise; runs that moved 0.5% or more in opposite directions disagree. The spread of positions and the settings are shown, never judged: no rule of the engine aims at them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

### Monitor 16: Phase plane: native

Native's muscles in position and velocity.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 17: Phase plane: Omni-Compass

Omni-Compass's muscles in position and velocity, the band's walls drawn.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 18: The scoreboard strip

The body's capacity in service and its demand (in the harness, its electrical power), the muscles past their line and the spread of positions over the day, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_decisions_total`, `omni_writes_total`; on a running system: `increase(omni_compass_decisions_total{zone="wall"}[1h])`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawStrip` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine (900 ms at 1×): the line takes a point, a ring opens at its head and its newest value is printed beside it.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3f The brain's internal state

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

### Monitor 19: The brain's state: the well

The brain's double-well potential and where its state sits.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 20: The brain's state: stress S in its potential

Stress S on its cubic potential Φ(S) = αₛS²/2 + βₛS³/4 − δS, rolling toward S*; the senses pull it back each decision (eqs. (5)–(6)).

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 21: The brain's state: the bath B

The bath oscillator B, the slow tide of physical load, over the last 120 decisions (eq. (7)), its spring at the latest B.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`.
- **Wired.** This page's `drawBrain` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the bath's line takes a point and a ring opens at its head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 22: Native's own controller beside the brain

What native's controller would do at the same decision, beside the brain's grant.

- **Evidence and state.** Class S; live.
- **Feed.** kube-state-metrics; series `kube_horizontalpodautoscaler_status_desired_replicas`.
- **Wired.** This page's `drawNat6c` → the Python `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ none: native's own controllers, as the harness's record or the page's own model holds them; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3g The verdict: change acceptance testing

The change-acceptance test. Each step is trialled against native and kept unless the measurement reads LOSS or its estimated cost exceeds the 2% allowance. An STEADY result (no difference resolvable from the noise) is also accepted, so on high-variance workloads a step with a small true cost can pass; the lab below measures that false-acceptance rate.

**The page, in its own words.**

Before a knob moves one step past native, the step runs as a trial: costs at native first, then at the step. The engine that stands reads the change exactly as a report reads a row, on the log of each cost, with its 95% interval. Set what the step truly costs and watch the rule decide. It opens wired as the shipped Kubernetes controller is wired, on the noise the real runs measured.

**This trial**

**Over many trials at this cost**

Native: its knob never moves past its own setting, so there is no trial and nothing to judge; every step Omni-Compass takes past native has to pass this test first. The medians alone allow a step when the trial's median is within the allowance of the reference's. The engine's rule (omni-v12's, unchanged) also refuses any step whose interval sits wholly above zero. It measures on while the interval is wider than the allowance, up to three times the pieces measured each side. It keeps a step only if both estimates are inside the allowance. Ported from omnicompass/verdict.py; the costs are modelled (class S).

How each muscle wires it. The Kubernetes controller measures 200 requests each side against a 2% allowance (omni_controller/controller.py --verdict-samples 200 --allow 0.02), the cost being each request's response time. The noise is measured at every build on each request of the newest tables' own runs. The σ 0.05 and 0.25 this page carried before 19 October did not come from these files and are withdrawn. The GPU card measures 30 requests (gpu_compass.py --verdict-samples 30); in its model the card's own time per request carries no noise. The model gate measures 60 (tools/model_gate.py, σ 0.25). What the rule does there is computed live in this page as you read: trials at each cost with this lab's own rule, 200 requests a side to start (the trial side measured on to 600 while its interval is wider than the allowance), a 2% allowance and the measured σ (modelled, class S). With noise this wide, 200 requests a side do not refuse a small LOSS on their own; with no noise any LOSS it can read is refused, even 0.1%. A larger sample would refuse more, and any change to the rule or its sample is the next engine version, landed through the model gate and told to the founder (his order of 19 October). Above the verdict the max never goes below native at all, so in the default it never runs (section 3l: no trial on top of the HPA).

**Its monitors.**

### Monitor 23: The verdict: one trial

A give-back trial judged against native: its reference, its step, its interval and the word.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`; on a running system: `omni_verdict_state`.
- **Wired.** This page's `drawVerdict, vTick, judge` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** A cost measured every 28 ms until the verdict reads; a new trial starts 2.6 s after.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

### Monitor 24: The verdict: every true cost

The keep ratio of the verdict at each true cost, from trials run in this page's idle time.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawVerdict2, runTrialSync` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** Trials run in the browser's idle time; the shares fill as they run.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native).
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

## 3h Cloud providers: Azure, Google Cloud, Amazon Web Services

In a cloud the one metric is the bill: whether the same workload costs less with Omni-Compass on top. Each provider's four test sets and their status.

**Controls.** Recorded data: GitHub's own cloud runs as read at the build. The controller below plays live; its run and speed follow the console's clock.

**The page, in its own words.**

In a cloud, Omni-Compass shows one thing: the same work as native for a smaller bill, never a bigger one. Every cloud set runs Omni-Compass at the tune-down on the machines alone: no pod autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's. It parks only a machine the cloud already made, after its own trial, and wakes it on a breach. The bill and the machines aim lower; work, speed and failures must read STEADY or GAIN. Azure runs first and is the measure of the other two: the same tuning, mechanism and harness.

**Every cloud run GitHub has started, set by set**

**The bill monitors: Azure, Google Cloud and Amazon Web Services, native against Omni-Compass**

One monitor a provider, the same harness, mechanism and tuning in all three (Azure is the measure of the other two). Each bar pair is a finished set: native's machine-hours (orange) beside Omni-Compass's (blue), the word by the one key (the bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given), the bill at list price under it. A provider with no finished set shows its empty frame and the reason its hourly gate holds, in its own job's words; nothing is drawn for a run that has not run.

**The bill on Azure, run by run, each with the engine it ran on**

From 19 October: every Azure set runs up to 100 paired repetitions a run, the paid cap, under the preregistered stopping rule (tools/stop_rule.py). After 10, 20, 40 and 70 repetitions the bill's change is read with its 99% interval. The run stops once the bill is read (GAIN, power given, or STEADY within ±2% of native's bill), and never while the speed or the failed requests read a LOSS. Those runs carry "to the cap, stopping rule" in their title and count as their own A, B and C; the 5-repetition runs below stay as their own engines' record.

**The shipped controller in the cloud setting, live: native's machines against Omni-Compass's**

The controller every cloud set runs (omni_controller/controller.py --give-back-only, the tune-down, the machines alone), decision by decision on the repository's modelled cluster (class S). The cloud's own autoscaler runs in both arms. Omni-Compass only parks a machine the cloud already made, after its trial, and wakes it on a breach. The bill is the machine-minutes in service, counted from the record.

**Native**

**Omni-Compass**

**Its monitors.**

### Monitor 25: Azure: the bill, run by run

Machine-hours billed and the bill at list price, native against Omni-Compass, every finished Azure set with its 95% interval, and the running set's repetitions done.

- **Evidence and state.** Class L (metered by Azure); record.
- **Feed.** OpenCost; Azure's own billing export; series `node_total_hourly_cost`, `kube_node_info`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/live_reps.py`, `tools/stop_rule.py`, `docs/engine/build_live_engine.py` → the C++ none: the bill as Azure meters it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the finished sets; the age of GitHub's reading counts up every second.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 26: Google Cloud: the gate and the bill

The same monitor for Google Cloud: the hourly gate's reading (the key, the login, the quota) and, once a set runs, its bill native against Omni-Compass.; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: the first set starts within the hour after the gate passes: the key stored whole (`docs/GOOGLE_SETUP.md`, section 4).
- **Feed.** OpenCost; Google Cloud Billing export; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 27: Amazon: the gate and the bill

The same monitor for Amazon Web Services: the hourly gate's reading and, once a set runs, its bill native against Omni-Compass.; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: the first set starts within the hour after the gate passes: the account on the Paid plan (`docs/AMAZON_SETUP.md`, section 1a).
- **Feed.** OpenCost; AWS Cost and Usage Report; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 28: The cloud setting, live: native's machines

The shipped controller's cloud mode on the model cluster: the cloud's own autoscaler alone.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`; on a running system: `count(kube_node_info)`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 29: The cloud setting, live: Omni-Compass's machines

The same autoscaler with Omni-Compass parking a machine only after its trial, waking it on a breach.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`, `omni_writes_total`; on a running system: `count(kube_node_info)`; `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

## 3i Orchestrators and governors: every scheduler, queue and multi-cluster governor, native and with Omni-Compass on top

These are the governors and orchestrators that sit between the work and the cluster: batch schedulers and job queues, multi-cluster governors, the default Kubernetes scheduler, GPU and edge orchestrators, and the rightsizing controllers. Each runs four ways in every repetition: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, and Omni-Compass on top of the orchestrator; only the last two, each against its own native, are readings of Omni-Compass, and the other comparisons are the orchestrator's own cost. Each has three runs, and every row is shown. Every place below is laid out now and fills itself from the repository as each one lands. Until then it says what the repository holds, and nothing more.

**Controls.** Recorded data: each governor's place as the repository holds it, its runs read from GitHub at the build and played here the moment they land; click a governor (a tile, a row of the road or of the catalog) to hold it.

**The page, in its own words.**

**The road to a result, every governor at once: its register row, its preregistration, its rig on GitHub, runs A, B and C, its three-run table**

**The orchestration stack, live: Omni-Compass on top, the governor native as shipped, Kubernetes and its nodes beneath**

Where each governor sits in the stack. Omni-Compass reads and writes on top of it once its wire is in the repository. The governor runs native as shipped beneath it, and Kubernetes places the work on the nodes. The work dots move at the live benchmark engine's demand (section 3b): a picture of the flow, not a measurement. Each governor's readings replace this picture the moment its three runs land.

**The catalog of governors and orchestrators: what each governs, native as shipped, Omni-Compass on top, and what the repository holds now**

**The four ways: the organism alone, the governor as shipped, Omni-Compass on the organism alone, Omni-Compass on top of the governor, all four in every repetition**

**The orchestra, the eighth organism: every governor's catalog muscles, native and with Omni-Compass on top (modelled, class S)**

**Its monitors.**

### Monitor 30: The orchestrators' road

Every scheduler, queue and multi-cluster governor on its way through trial, A, B and C, on the engine that stands.

- **Evidence and state.** Class L; record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawOrchRoad` → the Python `tools/governors_page.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`.
- **Moves.** A dot travels each governor's road, a running run pulses, and the reading cursor walks the governors, one a decision.
- **Knobs.** Governor: which orchestrator or governor is shown.
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

### Monitor 31: An orchestrator, four ways

The organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator: the four arms of the chosen governor.

- **Evidence and state.** Class L; record.
- **Feed.** kube-state-metrics; each orchestrator's own metrics endpoint (Kueue, Volcano, KAI, Koordinator, Crane, KubeRay); series `kube_pod_status_phase{phase="Pending"}`, `kueue_pending_workloads`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`.
- **Wired.** This page's `drawOrch` → the Python `tools/governors_page.py`, `tools/run_orchestra.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`, `tests/test_orchestra.py`.
- **Moves.** Work flows down the stack at the live benchmark engine's demand.
- **Knobs.** Governor: which orchestrator or governor is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

## 3j Kubernetes: official run playback

Playback of the official benchmark runs from their archived raw files: the native cluster and the Omni-Compass cluster under identical load, in 30-second bins, every file verified against its run's SHA-256 manifest.

**The page, in its own words.**

A real-time operations dashboard over the benchmark runs themselves (class L), not a model. Every series below streams half minute by half minute out of the raw files GitHub archived, each file's SHA-256 matched before a byte is drawn: native (the whole cluster with everything it ships with, everything but Omni-Compass) against Omni-Compass, the same load, the same second. The tiles, the candles, the heatmap, the bars and the governor's ticker all move together with section 3k (pick a benchmark, a run or a repetition in either place). Every word is the run's own reading, never one drawn from the stream.

**Data pipeline: from the GitHub Actions run to this page**

**The heart: the governor's beat from this repetition's own audit, beside native's own clock**

Why a heart. A supervisory governor is only alive while its loop turns: once every decision it reads the whole body, decides, writes, and proves it is still there. That turn is the heart. Each beat pumps every reading in through the plug and the decision out (omni_controller/controller.py, its main loop), and renews the governor's lease (master.heartbeat(), omnicompass/master.py). If the heart stops, its process gone or its lease older than its limit (the larger of 120 s and five beats), the watchdog (tools/omni_switch.py watchdog) walks every setting back to native: a stopped heart leaves the body exactly as native runs it. Native has no heart of its own: each of its controllers keeps its own clock (the pod autoscaler every 15 s, the firmware, the thermostats) and no beat joins them. On the engine that stands the governor's heart beats every 60 s at the factory, a full read of the state once a minute (from omni-v17; the founder's order of 22 October, afternoon); 15 s, the pod autoscaler's own pace, is a beat a person may pick on the dial (3c), as are 10, 30, 90 and 120 s. omni-v16 beat every 15 s (`docs/OMNI_V16.md`).

A healthy heart, never pushed. The beat runs at a fixed, calm rate (on the engine that stands one decision every 60 s at the factory, or the beat a person picks on the dial, the fast checks every 5 s between beats; the runs replayed here ran on the engine each table names, omni-v10 to omni-v12 at one decision a minute and omni-v16 and omni-v17 at their own beats) and is never driven faster by the load it governs. Every clock of the engine counts seconds, so the beat's pace sets how often the body is read, never what a rule means: a give-back still waits its trial's minutes, the cushion still keeps its twenty minutes of memory, and a machine still goes back at most one a minute. What it costs is counted inside the body's own load, so the organism never pays for its own brain without knowing it. A decision that fails is recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal time (safe_step). Two gauges below read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page calls a heart under strain when a decision takes more than half its beat, or a gap between beats reaches 80% of the lease. Past half its beat, the governor would have less than half its period left to act before the next reading. Both lines are this page's reading, not rules of the engine; the engine's own guard is the lease and the watchdog.

**The heartbeat sweep: every beat the governor can run at, what it does against native and what it costs**

A knob, not a fixed number. The governor's full read of the state, its heartbeat, is a setting of the run: every clock of the engine counts seconds, so the beat sets only how often the body is read, never what a rule means (omni-v16, `docs/OMNI_V16.md`). The factory sets 60 s since omni-v17, the main engine (omni-v16 set 15 s, the pod autoscaler's own pace; this sweep reads omni-v16 and omni-v15, and the dial's own ladder reads omni-v17 at every beat in section 3c); an operator may choose another for a system's own reasons, a slower beat to read the cluster less, a faster one to answer sooner, and this monitor shows what each choice does. Each bar is our own model (evidence class S, never a benchmark result): the shipped controller on the modelled cluster's 5-second plant, eight seeds of a day each, paired by seed with native and read by the one key (tools/heartbeat_sweep.py, `results/model_gate/HEARTBEAT_SWEEP.md`). Every beat here is read in the model only: a real run reads the one beat it was started with, the governor's --interval.

**Response time: one candlestick per 30-second bin**

**Latency heatmap: every response, binned**

**Throughput: requests served per 30-second bin**

**Every repetition of this run, side by side**

**The governor's ticker: every decision of Omni-Compass in this repetition, newest first**

**Native's own controllers' ticker: every change its pod autoscaler and the cluster made in the same repetition, newest first**

From the repetition's own audit.jsonl: the minute and second of the decision, the compass position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward native). Then the machines it recommends, and the give-back verdict's state: "left native" means every setting stays native's; "acting" means a trial on its own measurement. Native has no governor; its own controllers' moves are the second ticker, read from the native arm's capture.csv: the replicas its pod autoscaler holds, the pods waiting for a place and the machines ready. With Omni-Compass OFF the first ticker is empty, for nothing decides on top of native.

**Benchmark status, by block**

**Its monitors.**

### Monitor 32: The data pipeline, live: every stage from the GitHub Actions run to this page

Every stage from the GitHub Actions run to this page: the run, the raw files archived, the SHA-256 check, the official scorer, the three-run tables, the build and the page, the stage being read lit.

- **Evidence and state.** Class L; replay.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawPipe` → the Python `scripts/raw_archive.sh`, `tools/live_reps.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the stages are GitHub's runs and the repository's own tools; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The stage being read lights in turn and the data moves between the stages.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown.
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 33: The official run's heartbeat

The official run's heartbeat: native's own 15 s clock above, every beat of the governor's decision loop in the repetition below, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; the load generator's own histogram (the rig's loadgen); series `kube_horizontalpodautoscaler_status_current_replicas`, `kube_node_status_allocatable`; on a running system: `sum(kube_horizontalpodautoscaler_status_current_replicas)`.
- **Wired.** This page's `drawHeart` → the Python `docs/engine/export_runs.py`, `omni_controller/controller.py` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen repetition replayed decision by decision; native's own 15 s clock beats above.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 34: The heartbeat sweep: every beat the governor can run at

The governor's beat as a knob: what a decision every 5 to 120 s does against native, or against the same engine at 15 s or 60 s, on-site and in the cloud, gauge by gauge with its 95% interval, and what each beat costs the engine; our own model.

- **Evidence and state.** Class S; model.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_decisions_total`, `omni_decision_seconds`, `omni_last_decision_timestamp_seconds`, `omni_own_cpu_cores`; on a running system: `60 * rate(omni_decisions_total[5m])`; `omni_own_cpu_cores`; `time() - omni_last_decision_timestamp_seconds`.
- **Wired.** This page's `drawBeat, beatSetup` → the Python `tools/heartbeat_sweep.py`, `tools/model_gate.py`, `omni_controller/controller.py` → the C++ none here: the sweep runs the shipped Python controller on the model cluster; the C++ governor twin is held to the Python's at 60 s and at 15, 10 and 5 s (tests/test_cpp_governor_parity.py); held equal by `results/model_gate/HEARTBEAT_SWEEP.md`, `docs/engine/build_live_engine.py`.
- **Moves.** A cursor reads the beats in turn and names the row it holds; every button redraws the chart from the record.
- **Knobs.** Beat: the governor's full read of the state and its decision: every 5, 10, 15, 20, 30, 60, 75, 90 or 120 s in the heartbeat sweep's record; on a real governor its --interval (60 s at the factory since omni-v17, 15 s on omni-v16); Scenario: on-site bare metal, through the cloud, in the device, as a service; Engine: which engine's record the monitor reads: the engine that stands or the one before it; Against: what each reading is set against: native, or the same engine at another setting; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 35: The official run: response time candles

The response time of the chosen run as candles, one a half minute, native above and Omni-Compass below, on one logarithmic scale.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen); series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[1m])))`.
- **Wired.** This page's `drawCandle` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 36: The official run: the heat map

The responses of each half minute counted in eight response-time buckets, native above and Omni-Compass below.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawHeat` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 37: The official run: paired bars

The requests answered each half minute, native and Omni-Compass side by side, the failed requests marked.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawBars` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 38: The official run: the repetitions

Each repetition's reading in the chosen gauge with its interval.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawReps` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each repetition's reading filled in as the run replays.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

## 3k Kubernetes: per-repetition run telemetry

Per-run telemetry at one-second resolution, with the run's receipt and each repetition's score from the repository's own scorer.

**The page, in its own words.**

These are the benchmark runs themselves, not a model: each three-run table's runs A, B and C, read back from the raw files GitHub archived (results/live/raw), native and Omni-Compass, repetition by repetition, played second by second. Every file the page reads has its SHA-256 computed and matched against the run's own SHA256SUMS_ALL.txt, and every Kubernetes repetition is scored by the repository's own scorer (tools/live_reps.py); where a run holds its own scored summary, the scorer's mean over its repetitions equals it (the count is below). Class L: real Kubernetes on kind, real databases and a real broker.

**Native**

**Omni-Compass**

**The receipt of this run**

**This repetition, scored by the repository's own scorer**

**Benchmark status: landed, running, queued, or not yet run**

**Its monitors.**

### Monitor 39: Per-repetition run telemetry

One repetition half minute by half minute from its archived capture: the 95th percentile of the response time, the replicas, the host's processor and the governor's heartbeat, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; metrics-server; Kepler; series `kube_node_status_condition`, `kube_pod_status_phase`, `kepler_node_package_joules_total`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`; `rate(kepler_node_package_joules_total[1m])`.
- **Wired.** This page's `drawRuStrip` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The archived capture replayed half minute by half minute; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

## 3l Kubernetes and cloud: the shipped controller's decision trace

The shipped controller's decision trace, replayed from its own audit log one decision at a time: its inputs, its choice and its writes.

**Controls.** Recorded data: the shipped controller replayed decision by decision from its own audit (class S).

**The page, in its own words.**

This is the one place in the repository where the brain drives the muscles decision by decision: the shipped controller, omni_controller/controller.py, on the modelled cluster of pilot/selfpilot.py, wired as the repository wires it. Each decision runs the chain left to right: the senses, the six-state brain, the nerves and the machine organ’s grant, the compass law on the service (cloud setting), the verdict’s trial, the release gate, the plug. Every value below is the controller’s own audit record of that decision, recorded by docs/engine/export_controller_trace.py on runs A, B and C (six hours each, a decision every 60 s, class S).

**Native**

**Omni-Compass**

**This decision, brain to muscle, as the controller audited it**

**Three runs, A B C (the whole six hours of each)**

The paired change per 15 s tick, averaged over ten-minute blocks, with its 95% interval (Student’s t) in each run. Three runs (tools/readings.py, three_run_reading): the change is the mean of the three runs' changes; under 0.5% it reads STEADY, under the floor; 0.5% or more reads GAIN, LOSS or power given by the gauge's aim, “in all three of our runs” when every run went the same way clear of zero, otherwise “by the mean of our three runs” with the count of runs beyond the noise; runs that moved 0.5% or more in opposite directions disagree. Machines and power: a fall is a cut, a GAIN; a rise is power given. Our own models (class S): a model’s small numbers are the model’s.

**What the real thing reads (class L: real Kubernetes, three runs each; every Kubernetes three-run table on this page, each on its newest engine)**

**How steadily the governor steered on real Kubernetes: its own moves on every table results/STEERING.json holds, each on its own engine, beside native's own controllers**

**Its monitors.**

### Monitor 40: The shipped controller's trace: native

The controller every Kubernetes and cloud set runs, replayed decision by decision from its own audit: native's cluster.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_nodes_observed`; on a running system: `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 41: The shipped controller's trace: Omni-Compass

The same, Omni-Compass's cluster: every write, every trial, every hold.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_writes_total`, `omni_verdict_state`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

### Monitor 42: The shipped controller's trace: the strip

The shipped controller's machines (in service, booting and parked) and the response time over the run, native beside Omni-Compass, replayed from its own audit.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawCStrip` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v21; an older engine's run is its own record.

## 3m Hardware: the GPU card and the CPU host

The chip is the far end of every stack: there the max would ride each card's own limit, and every watt it takes is power given, shown beside the work it buys. No GPU card and no CPU package has been measured on the engine that stands; what the chip receipts will measure is listed below, no result before its record. Below: the slots for the metered GPU and CPU runs, every hardware run GitHub has started, then the models of one GPU card and one Linux host, native beside Omni-Compass.

**Controls.** Recorded data: GitHub's chip runs, then the chip models replayed from the repository's own run (class S); pick a setting in the table below.

**The page, in its own words.**

Each stack is run twice on the same load and the same seed: native first, then Omni-Compass. Left is native, right is Omni-Compass, and every table gives both columns and the difference. Each stack is its own model in the repository, run exactly as the repository runs it and recorded second by second by docs/engine/export_scenarios.py (class S, our own models). The clouds are section 3h and Kubernetes sections 3j to 3l, above this one; every muscle of the catalog, the seven organisms and the three-run tables are in section 4c.

**Hardware runs: the slots for the metered GPU and CPU runs**

The GPU runs on Lambda (class P: the card's own meter) and the CPU on its own machine (class P: the package's own energy counter, tools/run_cpu_power.py) are the receipts this engine still has to earn: whether the same work is done for less power on the chip itself is what those runs will read, and nothing here reads it before they land. Their runs on the engine that stands are not hooked up yet: each place is written here as the repository holds it and fills in, played back from its raw files like every Kubernetes run, the moment its three runs land. Until then the views below are the repository's own models of one GPU card and one Linux host (class S), run native and then with Omni-Compass on the same load and seed.

**The GPU card, metered: the one real run, replayed second by second (class P, the card's own meter)**

The engine that stands on a real card, its own meter recording native beside Omni-Compass: an NVIDIA A100 (SXM4, 40 GB) on Lambda on 24 October (workflow run 40079645681, omni-v18's card governor at commit e3b05dc), ten paired repetitions of 600 s an arm, native (the card as shipped), Omni-Compass watching only (the switch OFF: it reads and writes nothing) and Omni-Compass governing the power limit and the clock ceiling, every sample of nvidia-smi (200 ms) and every decision of the governor's own audit (results/gpu/run-20261024T091235Z, docs/engine/export_gpu_run.py). On this card native already runs both knobs at their top (the power limit 400 W of 400 W, the clock unlocked to 1,410 MHz), so the factory tune's governor asked for exactly that in its 3,050 decisions and wrote nothing: at its limit on native. One run; B and C and the 8-card run are not yet run. The A10 run of 2 October (the card controller of commit c908054, replaced since) stays as its own record in results/gpu/run-20261002T082232Z. Its own table, re-read by the one key:

**The CPU host: built and waiting for its machine (a model of a machine until then, class S)**

The CPU power harness (tools/run_cpu_power.py) puts Omni-Compass on top of the Linux kernel's own frequency governor and meters the processor's package energy (RAPL). No GitHub runner exposes that counter or a writable ceiling, so its real run waits for a Linux machine that does (the register's row 79, cpu-power.yml). Until then this monitor plays the harness on its own modelled machine (--plant sim, written for its tests; results/sim/cpu_power_model, three repetitions): the mechanism moving, every decision and write of its own audit, never a measurement. The machine layer enters the whole organism as exactly 1 until the real run lands.

**An 8-card node: built and awaiting its run (scripts/gpu_8card.sh)**

The 8-card result is one command on a rented machine with eight NVIDIA cards (scripts/gpu_8card.sh, `docs/GPU_RUN_GUIDE.md` section D): every card runs the whole card test at once, its firmware alone against its firmware with Omni-Compass on top, 24 paired repetitions a test pooled across the cards. It has not run. The monitor is built for it: eight card slots, each native lane drawn from the repository's one-card model (class S: AI token generation at the card's shipped 150 W, the same model on every card until the run, never eight measurements), each Omni-Compass lane empty until the run lands. On a running node the same panel reads the NVIDIA DCGM exporter's series card by card.

**Every chip run GitHub has started, newest first**

**Where the mechanism moves on the chip models: every setting, three runs each**

Read from the replayed record itself, second by second, in each of the three runs (seeds as below). A row with no second held off native is Omni-Compass deciding to stay native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native.

**Native**

**Omni-Compass**

**What Omni-Compass did, as its own audit records it**

**Three runs, A B C (the whole run of each)**

**Its monitors.**

### Monitor 43: The GPU card, metered: the one real run

The NVIDIA A10 run of 2 October replayed from the card's own meter: draw, limit, clock and temperature, requests served and the 95th percentile, native beside Omni-Compass governing (or watching only), every write of the governor marked.

- **Evidence and state.** Class P; awaiting its run: its omni-v13 run on Lambda (lambda-gpu.yml, one exact commit): the replaced controller's run stands until then, shown as such.
- **Feed.** NVIDIA DCGM exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`, `DCGM_FI_DEV_GPU_TEMP`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_POWER_MGMT_LIMIT`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawGpuRun` → the Python `docs/engine/export_gpu_run.py` → the C++ none: the 2 October run of an earlier controller, replayed from the card's own meter; today's GPU rules have their twin, cpp/src/gpu_rules.cpp, for the run on Lambda; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The card's own meter replayed at ten times the run's seconds.
- **Knobs.** Repetition: which repetition of the run is replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v21 run lands.

### Monitor 44: The CPU host, metered: awaiting its machine

The CPU power harness on the host: the frequency ceiling, the clock run at, the package power and the response line, native beside Omni-Compass; today its own modelled machine (class S), the real run the day a machine with its meter runs it.

- **Evidence and state.** Class S (model) until the run; awaiting its run: a Linux machine whose processor exposes its energy counter (RAPL) and a writable frequency ceiling (register row 79, cpu-power.yml).
- **Feed.** node_exporter (rapl, cpufreq collectors); Kepler; series `node_rapl_package_joules_total`, `node_cpu_scaling_frequency_hertz`, `node_cpu_scaling_frequency_max_hertz`, `kepler_node_package_joules_total`; on a running system: `rate(node_rapl_package_joules_total[1m])`; `avg(node_cpu_scaling_frequency_hertz)`.
- **Wired.** This page's `drawCpuHost` → the Python `docs/engine/export_cpu_model.py`, `tools/run_cpu_power.py` → the C++ none: the host's model until its run lands on a machine with its meter; held equal by `tests/test_run_cpu_power.py`.
- **Moves.** The host's model replayed second by second until its run lands.
- **Knobs.** Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The processor's frequency ceiling (the knob), the clock the kernel's own governor ran at under it, the package power and the busy share, native beside Omni-Compass.
- **What to do with it.** Until a machine with its energy counter runs it, the monitor plays the harness's own modelled machine: read the mechanism, never the numbers.

### Monitor 45: An 8-card node: built and awaiting its run

Eight card slots for scripts/gpu_8card.sh: each native lane the repository's one-card model (class S), each Omni-Compass lane empty until the 8-card run lands, 24 paired repetitions a test pooled across the cards.

- **Evidence and state.** Class S (native model) until the run; awaiting its run: scripts/gpu_8card.sh on a rented machine with eight NVIDIA cards (`docs/GPU_RUN_GUIDE.md`, section D).
- **Feed.** NVIDIA DCGM exporter, card by card; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`; on a running system: `sum by (gpu) (DCGM_FI_DEV_POWER_USAGE)`.
- **Wired.** This page's `drawGpu8` → the Python `realms/gpu_card.py`, `omni_controller/gpu_governor.py`, `scripts/gpu_8card.sh` → the C++ `cpp/src/gpu_rules.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** The one-card model's native lanes replayed second by second; the Omni-Compass lanes wait for the 8-card run.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v21 run lands.

### Monitor 46: The chip and the host, modelled

The repository's own models of one GPU card and one Linux host, native beside Omni-Compass, second by second (class S).

- **Evidence and state.** Class S; model.
- **Feed.** NVIDIA DCGM exporter; node_exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_SM_CLOCK`, `node_cpu_scaling_frequency_hertz`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawSStrip` → the Python `realms/gpu_card.py`, `omnicompass/compass_law.py`, `tools/model_gate.py`, `omni_controller/muscles.py`, `omnicompass/conveyance.py`, `docs/engine/export_scenarios.py` → the C++ `cpp/src/conveyance.cpp`, `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_conveyance_parity.py`, `verify.py`.
- **Moves.** The chip's and the host's models replayed second by second; a ring opens at each head with its newest value.
- **Knobs.** Stack: the GPU card, the Linux host, Kubernetes or the cloud; Run: A, B or C (or the archived run) the monitor plays; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v21 run lands.

## 3n Telemetry analytics and Omni-Compass in its own words

The same telemetry analysed four ways: a three-dimensional tensor view, a difference matrix, a principal-component decomposition and Omni-Compass's own account of its run; the service level and error budget in SRE terms; and Omni-Compass answering the viewer's questions about itself from the page's own records.

**Controls.** Recorded data: the engine's harness record (class S), played on the live benchmark engine's clock, and the official run chosen in section 3j (class L). Console controls never modify either.

**The page, in its own words.**

The engine's own record is a tensor: two arms × every decision × sixty muscles, each entry a muscle's compass position (0 calm, 0.5 the center of its band, 1 its line), recorded from realms/harness.py by docs/engine/export_harness_trace.py (class S, our own models). It fills in below decision by decision as section 3a plays, and the same numbers are read three more ways: the difference between the arms, the body's principal motions, and Omni-Compass's own account of what it is doing. Then the official runs (class L) are read as an SRE reads a service: the service level, the error budget burned and every gauge against native; and Omni-Compass answers questions about itself, reading the page's own records through tools and turning the dashboard to a run. No word on this panel is drawn from a picture: every GAIN, STEADY, LOSS and power given is a run's own reading.

**Omni-Compass, in its own words**

Omni-Compass speaks for itself here: every line is read from its own records at the moment on screen (the official run playing in section 3j, its governor's own audit, and the engine's harness on the console's clock), and says what it is doing, beside what native does. Speak aloud reads it out on the viewer's own browser voice as the run plays, and reads its answers below too.

**The telemetry tensor, in three dimensions**

**The difference matrix: Omni-Compass against native**

**The body's principal motions (the tensor's eigen-decomposition)**

**The service level and the error budget, this repetition**

**Every gauge of this repetition against native**

**Ask Omni-Compass: it answers for itself, from its own records on this page**

Ask in your own words, or pick a question. Omni-Compass answers in the first person, for its own mechanism and its own runs, reading only this page's records through six tools. The words are composed for it by Claude on claude.ai, on the viewer's own account and with the viewer's permission; opened anywhere else, the rest of the page runs whole without it.

Connecting…

Omni-Compass's answers are drawn from this page's records and are not reviewed by any outside party. © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with LICENSE, NOTICE and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Its monitors.**

### Monitor 47: Telemetry tensor: the cube

The engine's harness record as a tensor (decisions × sixty muscles × two arms), native and Omni-Compass as two slabs, filling in on the live benchmark engine's clock.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** kube-state-metrics; the service's own metrics.
- **Wired.** This page's `drawCube` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Fills in decision by decision on the live benchmark engine's clock, and turns.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 48: Telemetry tensor: the difference

The difference of the two sides' tensors, cell by cell.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawDelta` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** One column a decision on the live benchmark engine's clock.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 49: Telemetry tensor: the modes

The principal modes of the telemetry (its matrix decomposed).

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawModes, tEig` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision: the line across each bar is that decision's own motion in the mode; the first mode's line takes a point, a ring at its head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 50: Service level: the objective

The share of each half minute's requests answered inside the 500 ms line, native beside Omni-Compass, through the official run chosen in section 3j.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra) over the service's histogram; series `slo:sli_error:ratio_rate5m`; on a running system: `1 - slo:sli_error:ratio_rate5m`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 51: Service level: the error budget burn

The requests over the 500 ms line counted up since the repetition began, native beside Omni-Compass: each side's error budget burned.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra); series `slo:error_budget:remaining`; on a running system: `slo:error_budget:remaining`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 52: Telemetry radar

Every gauge of the repetition replaying in section 3j against native's 0 line: GAIN to the right in green, LOSS to the left in red, its side the run's own reading.

- **Evidence and state.** Class L (the official run's own gauges); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawRadar` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each gauge of the repetition replaying in section 3j.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); The dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

## 3o The Python's runs, in this page: the jump generator's runs recomputed here, the 500 scenarios replayed, the core's Monte Carlo

The Python's runs, the C++ harness's and this page's, run by run: the jump generator's set GitHub ran in the Python (its run linked), the same draws run through the C++ harness on the engine's C++ twins, and the same set recomputed here by this page's own port of the engine as the page opens; every receipt compared three ways, one SHA-256 digest each, and the digest of the draws themselves; and the Python's 500 scenarios a seed replayed from its own record with every trace hash; and the Python's Monte Carlo of the engine's core, 500 runs each from step 0 through the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps, native beside Omni-Compass, into the basin, held and certified, with every set the jump generator draws here held to the Python's digest.

**Controls.** Live: the runs start on their own when the page opens; the buttons run them again, run a new set from any base, print them and save the receipts.

**The page, in its own words.**

**The Python's runs, in this page: the engine's seeded runs recomputed here, and the 500 scenarios replayed**

How the three prove each other. tools/engine_runs.py runs N runs from a base seed: run k's seed is base + k·0x9E3779B9 mod 2³² (the jump generator), its stream mulberry32 (this page's own generator, written in the Python bit for bit), through the engine that stands: 288 decisions of the brain's state equations integrated by the fourth-order Runge–Kutta step, 80 steps of the compass law and one give-back trial judged by the verdict. Each run's receipt is its final state, its pushes and grants, the law's mean and last force and the trial's answer; the digest is the SHA-256 of every receipt at six decimals. The Python writes every draw of every run, the injection, and the C++ harness (cpp/tools/engine_runs.cpp) reads it as its input, puts the mechanism on through the engine's C++ twins and writes every receipt: its digest must be the Python's. This page runs the same N with its own port of the engine (proven equal to the Python and the C++ to 1e-12 on every build by docs/engine/check_live_engine.py) as it opens and compares every receipt and the digest. GitHub does all three on every set it runs (.github/workflows/engine-runs.yml) and on every push (verify.py); run the Python again with another base and it writes another set, and the three digests must be one.

**The Python's Monte Carlo: 500 runs of the engine's core, each from step 0, the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps, into the basin, held and certified**

**Your own system through it: write your stack as the core's ranges, run it here, or run it on GitHub through the Python and the C++**

A system is your own stack written as ranges of the engine's core: a name, and for any of the six starting states (E, energy debt; U, the order parameter, its basins at −1 and +1; I[U], the integral of need; S, stress; B, the bath; Ḃ, its rate; the block below names each by its key) and any of the 22 parameters of omnicompass/core.py a range [low, high] or one number; the rest keep the engine's own. Among the parameters: beta_int and beta_ext, the demand into E from inside and outside; E[max], the headroom; c, ω[B], Q[B] and λ₀ to λ₂, the bath's swing; mu, the depth of the double well. The draws keep their one order, so the jump generator's streams are the same; only the ranges they spread over change. The block is read as numbers only, never run as code (`systems/README.md`).

On GitHub (the simulation done within GitHub, on its own machines, at no cost): the button checks the block, copies it and opens the monte-carlo workflow. There, press Run workflow, paste the block into system, set runs (500) and base (empty for a new one) and press Run workflow again. The Python (tools/core_runs.py) draws the runs, the C++ twin of the core (cpp/tools/core_runs.cpp on cpp/src/core.cpp) runs the same draws, this page's own port is run on them in node, and the three digests must be one; the record, with the run's link, is committed to results/core_runs/ and joins this monitor's table at the page's next build. A system file committed under systems/ runs there on every push that changes it. GitHub offers Run workflow for a workflow on the repository's main branch: this one reaches main with omni-v18.

Class S: the engine's own mathematics on your ranges, never a measurement of your stack. Wiring Omni-Compass onto the stack itself is the plug of the Operator's Manual.

How to read it. Every line is one run of omnicompass/core.py: six states (E, U, I[U], S, B, Ḃ), the fourth-order Runge–Kutta step 10 times a macro step (Δt 0.01 s), 20 macro steps, from the starting state and parameters the run drew; the line is its U at step 0 and at the end of every macro step. The left lane is native: the same plant with no command (u = 0), left to its own double well, μU(1 − U²). The right lane is Omni-Compass on top: the bounded feedforward-plus-proportional command (u = −f[U] + 12(σ − U), clipped to ±25 and held across the four stages) toward the nearest basin, or, by the knob, toward the far one, or with the double well switched off (μ = 0). The green bands are the basins, |U ∓ 1| ≤ 0.10. A run is conveyed when it has stayed in one basin for 5 macro steps in a row, certified at 10; the bars under each lane count the macro step each run was conveyed (its colour) and certified (green), and the counters read at the sweeping cursor. The set the page opens on is the Python's own 500 (benchmarks/core_evidence.py, numpy's generator from seed 223387268), whose counts must be its record's (results/core_evidence.json); a set run here from the jump generator is computed by this page's own port of the core, line for line, and its digest must be the one tools/core_runs.py writes for the same base. Class S: the engine's own mathematics, never a measurement.

**Its monitors.**

### Monitor 53: The Python's runs, reproduced here

The engine's seeded runs: the Python's receipts (results/engine_runs) beside the same runs computed by this page's own engine, run by run, with one digest each.

- **Evidence and state.** Class S (the engine itself); live.
- **Feed.** tools/engine_runs.py (the Python) and this page.
- **Wired.** This page's `drawProof, engineRuns, proofRecheck` → the Python `tools/engine_runs.py` → the C++ `cpp/tools/engine_runs.cpp`, `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `verify.py`, `tests/test_engine_runs.py`, `.github/workflows/engine-runs.yml`.
- **Moves.** The page recomputes one run of the Python's set from its own seed about twice a second, round after round, and holds its receipt against the Python's.
- **Knobs.** Runs: how many of the Python's runs this page computes again; Print: the receipts of the runs, printable, with the digests and the notice.
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

### Monitor 54: The Python's 500 scenarios, replayed

benchmarks/stack_benchmark.py's 500 scenarios a seed base (the two held-out seeds), each through every arm, replayed from its record scenario by scenario with every trace hash and the file's SHA-256; verify.py replays them on every push.

- **Evidence and state.** Class S; replay.
- **Feed.** benchmarks/stack_benchmark.py (results/heldout_seed_*/RUNS.csv).
- **Wired.** This page's `drawHeld` → the Python `benchmarks/stack_benchmark.py`, `omnicompass/adapter.py`, `omnicompass/shield.py`, `omnicompass/stack_sim.py`, `docs/engine/export_heldout.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`; held equal by `verify.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`.
- **Moves.** The 500 scenarios replayed one after another from the record, every scenario's trace hash with it.
- **Knobs.** Seed base: which held-out seed base's 500 scenarios are replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Gauge: which gauge of the run is shown; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

### Monitor 55: The Python's Monte Carlo: 500 runs into the basin

The engine's core (omnicompass/core.py) over 500 runs, each from step 0: the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps, native (the plant alone, u = 0) beside Omni-Compass on top (the bounded command toward the nearest basin, the far basin, or with the double well off), every run's U, the basins at ±1, and the macro step each run was conveyed (5 in a row) and certified (10 in a row); the Python's own 500 (benchmarks/core_evidence.py, seed 223387268) and every set the jump generator draws here, each held to tools/core_runs.py's digest; the linked run holds the Python's digest, the C++ twin's on the same draws and this page's beside each other, and a system of your own runs here or on GitHub.

- **Evidence and state.** Class S (the engine itself); live.
- **Feed.** benchmarks/core_evidence.py and tools/core_runs.py (the Python) and this page's port of the core.
- **Wired.** This page's `drawMC, mcRun, mcLinkedRun, mcSysParse, coreSim, coreRk4, jgTick` → the Python `omnicompass/core.py`, `benchmarks/core_evidence.py`, `tools/core_runs.py`, `systems/README.md`, `docs/engine/build_live_engine.py` → the C++ `cpp/tools/core_runs.cpp`, `cpp/src/core.cpp`; held equal by `tests/test_core_runs.py`, `tests/test_cpp_core_runs_parity.py`, `verify.py`, `.github/workflows/monte-carlo.yml`, `.github/workflows/engine-runs.yml`.
- **Moves.** The cursor sweeps macro step 0 to 20 in 10 s, every run's line drawn up to it, the counters and the bars read at it; with the jump generator ON a new set of 500 arrives set after set.
- **Knobs.** Set: the Python's own 500 (numpy, seed 223387268) or a set the jump generator drew on this page; Omni-Compass side: the bounded command toward the nearest basin, toward the far basin, or with the double well off (μ = 0); native is the plant alone (u = 0); Your own system: your stack written as ranges of the core's six states and 22 parameters, run in the page or on GitHub through the Python and the C++ (`systems/README.md`); Play / pause: the cursor's sweep of the 20 macro steps, held or running; Runs: how many of the Python's runs this page computes again; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

## Part 4 of the page: The organisms and everything else

## 4a The whole organism, every way it is bought: on-site bare metal, through the cloud, in the device, as a service

Omni-Compass is wired into every piece of a stack through its own two-way plug: the software (the cluster: Kubernetes, its add-ons, its governors and orchestrators; and the services on it: the pools, the consumers, the caches), the bare metal under it (the chip's power limit and clock; the machine's kernel and its own meter) and, where the stack is rented, the cloud that bills the machines. A stack is bought one of two ways: on-site bare metal, the software on the owner's own bare metal (software × bare metal, no cloud); through the cloud, the cloud's build, its bare metal at the back end and the software (cloud × bare metal × software), with the cloud as two pieces beside it (cloud × software, the back-end bare metal left to the provider). The composition is read four ways (the Scenario knob): the two ways a stack is bought, and two more that take its pieces alone, in the device (the bare metal by itself) and as a service (the software by itself). Every piece's benefit is added into one collective reading, gauge by gauge (work, the 95th percentile response, machines, energy, the bill), with the receipts under it: what native spent, what Omni-Compass spent, and the benefit, in the units each table measured. The repository composes the layers in one place, tools/whole_system.py, which writes `results/WHOLE_SYSTEM.md` from the tables that stand: each layer measured against its own native with the layer under it as native runs it; a gauge's ratio oriented so that above 1 is a GAIN at every layer alike; the layers composed by the product law, R(g) = ∏ℓ Rℓ(g), log R = Σℓ log Rℓ (for small benefits the product is their sum), every interval carried (the exact Student t per run; A, B and C pooled by inverse variance; the layers' variances added); two readings of the same numbers (every measured piece: everything measured enters with its interval; the strict reading, the index's rule: only what held the same way in all three of our runs, everything else exactly 1); and the separability assumption tested on the governors' four ways. This section recomputes nothing from the tables: it regroups that file's layers into the two ways (docs/engine/export_whole.py), summing the logarithms of the layers a scenario stacks and adding their variances, as the file's rule composes any set of layers; the one number is the mean of the gauge logarithms, its 95% interval under the file's two bounds. The composition is a model (evidence class S) of class P and class L measurements under the separability assumption, and says so; no run has yet stacked every layer at once, and that stacked run is the measurement that would replace it. The chip's one measured run (2 October, on the card controller since replaced) stands beside the count by default, every row of it shown, as the repository's own headline has it; one click puts it in, until its run on Lambda on the engine that stands replaces it. The machine (the kernel, bare metal, Kepler) is not yet run and enters as exactly 1, named. GAIN is green, LOSS red, STEADY yellow, power given blue, on every word, cell and tile.

**The page, in its own words.**

DISCLOSURE: THE CLOUD'S BACK END IS NOT OURS TO METER. Through the cloud, the bare metal at the back end belongs to the provider: no tenant can read its power meter or write its chips' limits, so no run here reaches it. What a tenant can measure is what the cloud meters and bills: the machines it counts every fifteen seconds and the bill at list price (section 3h); that difference, native against Omni-Compass on top of the cloud's own autoscaler, is the cloud piece's benefit, and it is the provider's own health on its own hardware too, fewer machines held for the same work. The bare-metal piece is gauged on hardware we can meter (the card's own meter, the CPU host's energy counter, section 3m) and claimed for the provider's bare metal only as the same mechanism on the same kind of part: the composition multiplies it in as a modelled factor (class S of class P), never as a measurement of the provider's machines. Four ways are composed: on-site bare metal (the owner's own racks and chips: software × bare metal); through the cloud (the cloud's build, its bare metal at the back end and the software; and the cloud as two pieces, the back end left to the provider); in the device (Omni-Compass built into the bare metal alone, the card and the machine, nothing else wired: for an owner who ships hardware); as a service (the software alone, run for an owner with neither bare metal of their own nor a cloud account: the transport of the software only). This whole stack is a composition with two arms, native and with Omni-Compass on top of every piece; it is not counted among the organisms (the seven, and the orchestra the eighth). Each piece is its own newest measurement, on the engine its record names (the cloud piece Azure's runs on omni-v1, the chip piece the card run of 2 October under a controller since replaced, the software pieces their newest three-run tables): the composition is across those engines, names each, and is remade as each piece's run on the engine that stands lands.

**The stack, native beside Omni-Compass: work flowing down through the pieces**

**The collective synopsis: the benefits, gauge by gauge, added together**

**The composition, piece by piece and layer by layer: each factor with its 95% interval, the whole their product**

**Bills and receipts: what native spent (the cost), what Omni-Compass spent (the expense), and the benefit, in the units each table measured**

**Beyond the count: the governors' tables on this page, the models beside, the separability test, and where the missing pieces land**

**Its monitors.**

### Monitor 56: The whole organism, composed

The pieces of a stack, native beside Omni-Compass, each piece's composed factors and the whole, their product, in every way a stack is bought.

- **Evidence and state.** Class S (of P and L); composed.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawWhole` → the Python `tools/whole_system.py`, `docs/engine/export_whole.py` → the C++ none: a composition of measured tables by the product law, read as tools/whole_system.py writes it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Work flows down both columns; the reading cursor walks the pieces, one a decision.
- **Knobs.** Scenario: on-site bare metal, through the cloud, in the device, as a service; Reading: every measured piece carried, or the index's strict rule; The chip's run: the chip's one run beside the count or in it; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

## 4b The twenty scenarios and the injection grid: ten organisms native and with Omni-Compass on native, every governor, on the Python's 500 injections

The ten organisms (the spine; the four realms; the four stacked; the whole tower; the orchestra; this page's own sixty-muscle organism; and the whole organism in its three places), each run two ways: native alone, and Omni-Compass on top of native (the factory tune); Omni-Compass is never by itself (the founder's order of 25 October). Twenty cells, each read by the key against native, from the record results/scenarios/SCENARIOS_20.json (class S, our own models, three runs A, B and C). A cell with no run reads "not yet run", never a number.

**Controls.** Recorded data: click an organism and an arm, or hover a cell, for its gauges and its readings. In the injection grid: the organism, the way (Omni-Compass on native, a governor on the organism, Omni-Compass on top of a governor), what it is read against, the runs (1, 10, 100, 500), the organisms stacked (1, 10, 100, 500), the gauge and the injection; exports, an import and a reference to any cell. Both grids stand in the main control panel beside the wall, and the switchboard's runs, copies and organism drive the injection grid.

**The page, in its own words.**

**The injection grid: one batch of the Python's 500 injections through every organism and every governor, 1, 10, 100 and 500 runs × 1, 10, 100 and 500 organisms stacked**

What a governor is here. In our models each governor is the body of the catalog muscles that stand for its knobs (tools/run_orchestra.py, the mapping of tools/governors_page.py), run on the organism's clock on the same injections, each under its own native controllers; Omni-Compass on top of the governor governs both bodies. The governor's body does not reach the organism's own muscles, so its way reads its own muscles beside the organism's. The governors themselves, as their projects ship them, run on real Kubernetes in section 3i (class L): fourteen named, twelve with a rig built, eleven run the four ways (KubeEdge and Nephio are modelled only). A LOSS counts against Omni-Compass only on a way with Omni-Compass on top (on native, or on top of a governor); a governor on the organism read against native is the governor's own reading, shown as the governor's. One batch is one run in the key's sense; three batches make a three-run reading.

The injection grid draws as the page opens.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4c Measured effect in full: the organisms, every muscle, the register, the grid and every three-run table

Everything the board in section 2d stands on, from the organisms down to the single muscle: the seven organisms under their three loads, all 1,107 muscles of the catalog one cell each, every registered benchmark still to run, the scale-out grid of copies and runs, and every three-run table in the repository with every row as it is written.

**Controls.** Recorded data: every receipt as the repository holds it. Console controls never modify it.

**The page, in its own words.**

Every benchmark's benefit in one place, as the repository's benefit sheet holds it (results/BENEFIT_SHEET.json), with the Omni index that weighs them together (`results/OMNI_INDEX.md`). Then the grid: every organism at 1, 10, 100 and 1,000 copies, each at 1, 10, 100 and 1,000 runs, modelled and with the real cluster inside. The 1,000 tier runs on GitHub's free runners only; paid machines stay at 100. Each bar and square carries its own word, and the size beside the word carries the word's sign: GAIN +, LOSS −, STEADY =, power given +.

**The seven organisms of the catalog under three loads, then the whole stack's two arms, native and with Omni-Compass**

The founder's count of 20 October: the seven organisms of the catalog (the spine first, the base every stack runs on; the four realms; the four stacked; the whole tower), each run native and with Omni-Compass on top of native, under its own load, the climb (1 2 3 2 3 4 …) and work waiting in line; and the whole organism, the software, the cloud and the hardware stacked into one body (section 4a), composed from the pieces' own readings, native and with Omni-Compass on top of every piece: a composition with two arms, not an organism of the catalog. The orchestra, every governor's muscles as one body, is the eighth organism (section 3i). The monitor below draws the seven from the realms table; the whole stack's two arms are section 4a's composition until the stacked run, preregistered in `docs/WHOLE_SYSTEM_PREREGISTRATION.md`, measures them in one run.

**Every muscle of the catalog, one cell each, its word against native**

Click a cell to read the muscle: its name, family, realm, template, knob and its word under each load.

**Third-party software still to be benchmarked: the register's slots, in order**

What these slots are. Every muscle in them (a legged robot's gait, locomotion_speed; a wind turbine's blade pitch, pitch_angle_limit; a mobile robot's travel speed, agv_speed and trajectory_speed) already runs, modelled, in the 1,107-muscle catalog and the seven organisms below, native and with OMNI-COMPASS on top. A slot here is the next step for that kind of muscle: the same test on the outside world's own software (MuJoCo's Unitree Go2, NREL's OpenFAST, ROS 2 Nav2), each queued until its three runs land.

**The scale-out grid: seven organisms × 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs (the 1,000 tier on GitHub's free runners only)**

**Modelled (class S): the misses**

**With the real cluster inside (class L inside the model): the 95th percentile**

**Every three-run table in the repository, native against Omni-Compass, every row as written (each benchmark's newest engine's table; class L real software, class S outside simulators)**

From each benchmark's newest engine's table (results/live/V10_*.md today), read row by row by docs/engine/export_scenarios.py; open a row to read every judged row that is not STEADY. Class L: the real software (Kubernetes on kind, the real databases and broker). Class S: the outside simulators run by our own runner (CityLearn, pandapower on SimBench, MuJoCo Menagerie, gym-pybullet-drones). Rows shown and not judged are left out of the counts; the counts take every table of a receipt, its tuning case included where it has one (a receipt's own summary line counts its untouched cases). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Every muscle of the catalog and the seven organisms, native against Omni-Compass (the realms table)**

The eighth organism, the orchestra (every governor's catalog muscles, each governor's a body of its own and all of them one body), has its own runner and its own table: section 3i, under the governors.

**Every family, by stack: each muscle alone, native and then with Omni-Compass**

From results/realms_v5/REALMS_V5.json, the realms runner at the max, its engine and commit named above (tools/run_realms_v5.py, catalog realms/catalog_v5.csv), ten paired seeds per muscle and per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none moving the other way; STEADY at its limit on native when its knob already sits at the top of its range. Energy is power given where it rose. Evidence class S, our own models: a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

### Monitor 57: The seven organisms, three loads

Each organism's misses against native under its own load, the climb and the line (the realms table).

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawOrgCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks every organism under every load, one a decision.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow STEADY, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

### Monitor 58: Every muscle of the catalog

The 1,107 muscles as one matrix, each cell its word against native, by family and realm; a click names the muscle.

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawMuscleCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks the 1,107 muscles, one a decision; a click holds one.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Every muscle of the catalog one cell, its word against native on its own load: green GAIN, yellow STEADY (pale: at its limit on native), red LOSS.
- **What to do with it.** Click a cell to read the muscle: its family, realm, template, knob and its word under each load.

### Monitor 59: The scale-out grid

Seven organisms × copies × runs: every square's word, modelled and with the real cluster inside.

- **Evidence and state.** Class S/L; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawGridCv` → the Python `tools/grid_v5.py`, `scripts/dispatch_grid.py`, `docs/engine/build_live_engine.py` → the C++ none: the grid's squares as its runs on GitHub write them; held equal by `tests/test_grid_v5.py`.
- **Moves.** The reading cursor walks every square with runs started, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow STEADY, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

## 4d The C++ twin: the Python's runs through the C++ engine

**The page, in its own words.**

In plain words. The engine is written twice, in Python and in C++, line for line. Every time this page is built, the Python's own runs are fed into the C++ as its input, and the C++ answer is set beside the Python's, number by number. Where they are the same to the last digit, the two are one engine. Where a part runs in Python only, the last table names it.

**Every twin, on its own parity check**

**The Python's runs through the C++ engine, receipt by receipt**

The Python's seeded runs (tools/engine_runs.py: the jump generator's seeds, 288 decisions of the brain, 80 steps of the compass law and one give-back trial a run) are the input: the Python writes every run's draws as the injection, the C++ harness (cpp/tools/engine_runs.cpp) reads it, puts the mechanism on through the C++ twins (the governor, the nervous system, the compass law, the verdict) and writes its own receipts and digest, the output. The proof monitor (section 3o, the Python's runs, in this page) shows the same column run by run.

**The compass law of every run on this page, reading by reading**

**The seven organisms at the tune-down, every muscle's law**

**What runs in Python only, for now**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4e CI pipeline: GitHub Actions runs in progress and queued

Every GitHub Actions workflow run in progress or queued at build time. The hardware and cloud runs, with their terminal status, are in sections 3h and 3m; every run on the engine that stands that terminated without a measurement is raised on the status board (section 2a).

**Controls.** Recorded data: GitHub's runs as read when the page was built.

**The page, in its own words.**

**GitHub Actions, as a monitor: the runs in flight, the Azure set's repetitions, the clouds' gates, the chips**

Read at the build from GitHub's own API: a workflow's running runs in solid blue, its waiting ones pale; the Azure set to the paid cap with its repetitions measured so far (the table is written when the set ends); each cloud's hourly gate with the reason its own job wrote. Live, the same lives in the open-source github-actions-exporter for Prometheus.

**Workflow runs in progress and queued**

The page is rebuilt by GitHub itself (.github/workflows/live-engine.yml, docs/engine/build_live_engine.py) whenever the engine, a model or a result changes, and every three hours. Every record is made again by the repository's own code on the engine that stands, checked against the Python and the C++, and committed. This table is GitHub's own list at that moment.

**Its monitors.**

### Monitor 60: GitHub Actions: the runs in flight

Every workflow run in progress or queued when the page was built, the Azure set's repetitions done of its cap, and the clouds' gates.

- **Evidence and state.** Class L (GitHub's own API, read at the build); record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter; series `github_workflow_run_status`, `github_job_duration_seconds`; on a running system: `sum by (workflow) (github_workflow_run_status == 1)`.
- **Wired.** This page's `drawCi` → the Python `docs/engine/build_live_engine.py` → the C++ none: GitHub's own record of its runs, read from its API at the build; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the workflows, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** GitHub's runs in flight at the build by workflow, the Azure set's repetitions measured, each cloud's gate with its reason, the chips' runs.
- **What to do with it.** A gate that holds names its fix in its own words; nothing is billed while it holds.

## 4f The master switch's wiring: the switch above the brain, the brain above the organism, every muscle under it

One switch for the whole organism, drawn as the repository wires it: the master switch holds the brain's outputs; the brain sits above the organism; every muscle hangs under it with native's own controller under every muscle, never switched. Every governor of this page is listed with its state at the switch.

**Controls.** Live: the switch on this monitor is the kill switch of section 1b.

**The page, in its own words.**

**The master switch, wired at the top of the organism: switch, brain, organism, every muscle**

One switch for the whole organism, as the repository builds it (omnicompass/master.py, tools/omni_switch.py). It sits at the top and holds the brain's outputs. With it OFF, nothing the brain computes is pushed or pulled into any muscle, and every muscle runs on native's own controllers, which never stop. On a real machine every governor exits at the switch; on this page the brain keeps reading the native body in shadow, so its monitors keep moving, and nothing it computes leaves it. No monitor is switched off: every Omni-Compass side follows native, drawn in native's colour. Every governor on this page is registered with it and obeys it at once. The live organism hands every setting it held back to native's own controller and reads each one back. Every record's Omni-Compass side, and every playback, trace, table, board and grid, reads native's own. Native's own controllers sit under every muscle and are never switched, so native's side never moves with it. Every section carries the same switch in its controls bar; pressing any one of them throws this one.

**Its monitors.**

### Monitor 61: The master switch and the kill switch

The switch above the brain: ON, Omni-Compass governs every wired muscle; engaged, every setting is handed back to native's own controller at once and every Omni-Compass side on the page follows native.

- **Evidence and state.** Class S (the page's port of the master switch; the real one is omnicompass/master.py); live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_master_switch`; on a running system: `omni_master_switch`.
- **Wired.** This page's `drawMaster, masterSet` → the Python `omnicompass/master.py`, `tools/omni_switch.py`, `omnicompass/nervous_system.py` → the C++ `cpp/src/nervous_system.cpp`; held equal by `tests/test_master_switch.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** Every decision: the brain's pulse and the work flowing down to every muscle; the switch acts at once.
- **Knobs.** Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The wiring from the top down: the master switch above the brain, the brain above the organism, the organism above every muscle, and native's own controllers under every muscle, never switched. The switch's state is the word on it: ON in green while Omni-Compass governs; engaged, the switch red and OFF in white.
- **What to do with it.** Press the kill switch only for security: it is instant, every setting goes back to native and is read back. Watch the governors' table beside it: every governor on the page says OFF and what it handed back.

## 4g Component specification and mathematics

The component specification: every part, its equations and the source module that implements it, in Unicode as the repository writes them.

**Controls.** Live: the brain's six state variables below are read from the live benchmark engine every decision, beside the equations that evolve them.

**The page, in its own words.**

Items 1 to 5 and 8 are the engine’s code and run in every live view (the official-run playback of 5c and 5d replays records and runs none of it). Items 6 and 7 as written (the compass law on each muscle, the plug’s lever) drive the stress-test model. In the harness views the max and the plants’ own overrides take their place. The live controller runs the compass law on the service, as section 3l shows.

**The stress-test model, written out (class S, drawn for this page)**

**Who drives what**

**What is the engine's code**

The six-state engine, its constants and RK4 integrator, the assimilation, push and ρ*, the four nerve scalars and the organ thresholds, the compass law and the verdict in words are ported from omnicompass/core.py, adapter.py, nervous_system.py, compass_law.py and verdict.py at commit c8ba7775d. All are inside the omni-v17 fingerprint (omni-v17 moved only the Kubernetes governor's default beat to 60 s and its cruise wait to two readings at least, neither of which the port computes); adapter.py carries omni-v16's clocks in seconds (at the page's 60 s step every value is omni-v15's) and omni-v15's clear-time gate on the power-cap request, which the port does not compute (it ports the states, the push and the headroom), and the others are omni-v12's bytes. omni-v9 added omnicompass/student_t.py, and the page carries its Student t too, computed by bisection on its own distribution and rounded to three decimals as the printed tables are. omni-v10 changed only the CityLearn wire's glide, omni-v11 only the Kubernetes governor's blind-reading guard, omni-v12 only that governor's hold on a refused raise, and omni-v13 only the governor's conveyance on a shared host at its top, omni-v14 only the governor and its muscles: a muscle left native, the operator's commands without a shell, and omni-v15 the brain's power-cap request through the line's own clear time, with the card governor handing the brain its clear flag. Checked against the Python on seeded inputs (docs/engine/check_live_engine.py): 8,000 decisions of the governor (state, push, ρ*, κ, h, σ, ν, calm), 48,000 organ grants, 4,800 compass forces, 300 verdict intervals and 400 full verdict trials. A build passes only when the largest difference is under 10⁻¹², no grant and no verdict differs, and the Student t is equal on all 500 degrees of freedom checked. And against the C++ twin of the core (cpp/src/core.cpp, compiled by the check with docs/engine/cpp_core_probe.cpp): 2,000 seeded states, the derivative and the RK4 step within 10⁻¹² of each other. The check prints its own measured differences in each build's report on GitHub. The page's engine, the Python and the C++ are one engine. The harness views are not ported: they are the harness’s own record, made by its code.

**The two bodies**

The realms harness (the default). The sixty muscles are one organism of realms/harness.py. Each is a plant of realms/plants.py: machine pools under their autoscalers, cooled zones, batteries on their lines, motion axes and process loops. They are coupled through their heat and their power, under the climb (1 2 3 2 3 4 …), for 240 decisions of 15 s. Omni-Compass is the max of realms/compass_arm_v5.py with the body’s bone, its twins and the muscles’ cards; at 80% the brain goes silent and the lease walks every setting back to native over 24 decisions. Recorded on seeds 3000, 3001 and 3002 (runs A, B and C) by docs/engine/export_harness_trace.py; the page replays the record. Each muscle alone is the same harness one muscle at a time, as run_muscle_arm runs the preregistered muscle table: under the line (work waiting at the start), the max with the muscle's own twin, and the lease after 80%. Each muscle's decisions are laid on 240 frames. A frame shows the last decision it covers, and reads over the line if any of them was. In that harness the brain’s state is computed from the body’s aggregate, as a governor reads it, and shown; the max itself acts muscle by muscle. The stress-test model. A model drawn for this page so the body can be stressed by hand (a surge, a blind sense, a security hold, the kill switch), evidence class S; like every view it runs native and Omni-Compass, side by side, on the same demand. Sixty muscles named from the 1,107-muscle catalog (twelve each from the spine and the four realms), each a capacity lever with its own response time τ and sensing delay, under an HPA-style native controller (target 0.70, 10% tolerance, five-decision scale-down window). Demand climbs 1 2 3 2 3 4, surges, eases and idles over six hours, the same for both arms. The lever rules that turn F into a write are this page's, written out above and kept inside the doctrine. Under the max: never below native, and lifting off hands back toward native. On the tune-down: never above native, and below it only with the organ's grant and the release gate.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4h Failure modes, controls and residual risk

The failure-mode register: every known way Omni-Compass can fall short, the control that mitigates it, that control's coverage, and the residual risk where it does not reach. Every failure mode the live benchmark engine can be put through has a fault-injection control; trigger it and observe both arms on the console. Below: the resource costs the three-run tables report but do not judge.

**Controls.** Live: every way below that the live benchmark engine can be put through has its own button, and the response plays on the console (section 3b), native beside Omni-Compass.

**The page, in its own words.**

**Failure-mode register: control, coverage and residual risk**

**Reported, unjudged metrics: the resource cost of the work**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4i Self-governed rendering: Omni-Compass inside this page

The page's own render loop is governed by the same compass law, measured on the client device, native beside Omni-Compass.

**The page, in its own words.**

The engine that runs this page has Omni-Compass in it. Native is the browser's own loop: every chart on screen drawn on every frame, and when the frame overruns, whole frames dropped. Omni-Compass is the same loop with the engine's own compass law governing it (omnicompass/compass_law.py, ported here and checked against the Python). Each chart is a muscle whose knob is how many frames it waits between draws, and the reading is the time between frames. Below the band's center the pedal lifts and every chart is handed back to native, drawn every frame. Toward the line it pushes: the charts farthest from where you are looking wait a frame or more, so the frame itself stays inside its line. Every step is a trial run to its full measurement and kept only when the frame shortens; a step that buys nothing is refused and every chart handed back to native (the reflex rule: where a knob cannot bring a GAIN, it stays native). The reading is the time between frames, the band two frames wide with its center one frame at 60 Hz. The two arms take turns in paired windows of three seconds on this same page, on your own machine, and are read by the three-run rule's interval (class L: this browser, live; a reading of this page, never a benchmark of record).

**Native**

**Omni-Compass**

**Frame timing: the inter-frame interval against the 60 Hz budget**

**Paired measurement of this page, per window**

**Its monitors.**

### Monitor 62: Self-governed rendering

This page's own render loop governed by the compass law: the frame time against its line, native (no governor) beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawSelf` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`.
- **Moves.** Every frame: this page's own frame time under the compass law.
- **Knobs.** Frame load: +0, +8 or +16 ms burned inside every frame of this page; Kill switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** This page's own render loop governed by the compass law: the time between frames against its line, native (no governor) beside Omni-Compass.
- **What to do with it.** Load the page with the frame-load knob and watch the governor shed chart frames to keep every frame inside its line.

## 4j The problem and the answer: what the whole industry faces, and how Omni-Compass addresses it

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
| Reaction latency: waiting, queues and time over the line before capacity arrives | it reads every muscle on its own clock (on Kubernetes its full read of the state every 60 seconds at the factory, 15 seconds or faster where a person picks it on the dial, and its fast checks every 5 seconds) and moves as a reading nears its line, not after the line is crossed: proactive as well as reactive, like an immune system | time waited, missed or failed: a fall is GAIN, a rise is LOSS |
| Static over-provisioning: machines, energy and a bill paid for headroom rarely used | every muscle driven up to its own limit and never past it, so the machines already paid for carry more work; in a public cloud it parks only a machine the cloud already made, after its own trial, and wakes it on a breach, so the bill can only fall or stay | work done: a rise is GAIN; machines, energy and the bill: a fall is a cut, a GAIN, and a rise is power given |
| Uncoordinated coupling: one loop's correction is another loop's disturbance | one brain for one body: a step on one muscle stands only while every muscle it couples to stays inside its own cushion | every muscle judged on itself, and the organism judged whole |
| The gaps closed by hand: settings retuned by hand, alert minutes, on-call | an autopilot: every write read back, every give-back on its own trial, every reason written to its audit; an alert minute on Omni-Compass's side is found and fixed, never accepted | the alert minutes, judged; the settings commands it wrote on its own, shown |

Where this page shows each answer. Reaction latency: the organism live, every muscle's place in its band and the decisions past the line, native beside Omni-Compass (3a), and the shipped controller's decision trace (3l). Static over-provisioning: the benefit board (2d) and the clouds' bills (3h). Uncoordinated coupling: the whole organism (4a) and the organism's immune system (3a). The gaps closed by hand: the status board's alarms (2a) and the golden signals, the event log and the live metrics (2b).

What it does not do. It replaces no controller, and it creates no capacity a machine does not have: it uses the capacity already there, each muscle to its own limit. It promises no number on a system it has not run on: the only number that applies to a system is the one that system's own paired runs produce. The outside figures above are their authors' own, quoted for scale; none was measured, checked or endorsed by The Omni-Compass LLC, and none is a result of Omni-Compass.

How it is held to account. Every benchmark has two arms, native and Omni-Compass on top of native, on the same machines with the same work, run three separate times. Every reading is one word, GAIN, EVEN or LOSS, decided by what the gauge is for (the key, in the next section); every result carries its evidence class (P a physical meter, L live software, S our own models, never shown as proof of hardware); and every row is shown, LOSS included. The governing rule is do no harm, in its one meaning (`DISCLOSURES.md`, section 3): the aim is an organism never left turning out less than native, nor less healthy; where a row of a three-run table reads LOSS against native (section 2c lists each, every one; a model's own LOSS rows, class S, stand in their own sections, the heartbeat dial's in 3c), the row stays, its cause is found and fixed, and the test runs again. The executive summary under this section reads where the record stands, from the records on this page.

The outside sources. International Energy Agency, Energy and AI (April 2025), its executive summary. Lawrence Berkeley National Laboratory, 2024 United States Data Center Energy Usage Report (December 2024), prepared for the U.S. Department of Energy. Cast AI, 2026 State of Kubernetes Optimization Report: a seller of Kubernetes optimization, reporting its own customers' clusters as they ran before its automation. Flexera, 2026 State of the Cloud Report (March 2026): a survey of 753 cloud decision-makers and users, the figure their own estimate. The Kubernetes documentation, Horizontal Pod Autoscaling: the controller's defaults.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4k Executive summary and reading key

The Omni index, every real test weighed together: the record loads below.

**Controls.** Live: the buttons act on the live benchmark engine; every number below is read from the records on this page.

**The page, in its own words.**

In one paragraph. Two sides everywhere, and only two: native, the whole system by itself, and Omni-Compass and native, the same system with Omni-Compass on top of all of it; Omni-Compass is never by itself. Three words, by the one key: GAIN, STEADY and LOSS, with power given for a resource that rose, each number beside a word carrying the word's sign. Three classes of evidence: P a physical meter, L live software, S our own models, never proof. The figure of record is the Omni index, every real test weighed together.

**Read the whole section: the executive summary, the key, the terms, the examples (about two printed pages)**

**Executive summary**

Every number in this list is read from the records on this page when it opens (the three-run tables, the Omni index, the cloud ledger, the card run, the models' own readings, the realms table and the harness); none is typed in. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**The key: GAIN, STEADY and LOSS**

**The terms this page uses, each defined once (the first time a term appears on the page it carries the same definition, shown when pointed at)**

The size is how far the gauge moved from native; the word says whether that move helped the work. Examples, read from the three-run tables on this page, appear here when they load. A miss is a decision where the work went over its line. The key is written once in tools/readings.py and stands at the top of the README, the reading guide and the manuals. GAIN, EVEN and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results; the underwriting senses explain the words and are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4l The monitor list: every monitor by its number, what it shows, its section and its feed

The list that goes with the wall: every monitor by its number, in the same order, with what it shows, the section it lives in, its evidence class and state, the open-source feed that would carry it live and its knobs. Read the wall, find a number, read its line here.

**Controls.** Recorded data: the list is the page's own registry of its monitors, read when the page opens; click a number to go to its monitor, a section to go to its section.

**The page, in its own words.**

**Every monitor by its number: what it shows, its section, where its numbers come from, the open-source feed that would carry it live, its knobs, and what is still awaiting its run**

The motion meter: every monitor in view is photographed small once a second, as you see it, and its badge says whether it moved.

Every monitor is one canvas on this page; its number is its order of appearance from the top, and the wall (section 1a) reads them left to right, then the next row. The feeds name the open-source exporters an operator's Prometheus and Grafana already run (node_exporter, kube-state-metrics, the NVIDIA DCGM exporter, Kepler, OpenCost, the governor's own tools/omni_exporter.py); the button in the control panel downloads the whole wall as a Grafana dashboard on those series (deploy/grafana/omni-compass-wall.json, written from docs/engine/monitors.json), beside the governor's own screen (deploy/grafana/omni-compass.json). A monitor the page draws from the repository's tables, or from its own clock, says so: no series carries it.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 4m Glossary and index: every term, the ten organisms, the twenty scenarios and every muscle of the catalog

What every word on this page means, written from the repository's own pages (each definition names its source file), the organisms by their realms and families, and every muscle of the catalog (realms/catalog_v5.csv) with the organisms it sits in; the index sends each term to the sections where it is used. Built by tools/live_glossary.py into docs/engine/glossary.json.

**Controls.** Type to find a term, an organism or a muscle; click a letter to jump; each muscle opens to its family, its realms, its template, its knob and its wiring.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## v Disclosures, governing law and contact

**The page, in its own words.**

THIS PAGE IS A LIVE TUNING ENGINE. THE BENCHMARKS ARE ONE TUNED ENGINE. Every knob, button and monitor on this page can be turned in real time: the heartbeat at 10, 15, 30, 60, 90 or 120 s, the dial between the max and the tune-down, the pedal, each muscle driven or left native, up or down, in or out, minus or plus, to see and produce the variations of the mechanism of action with native alone, with Omni-Compass on top of native, or both side by side. Like any engine, where turning the mixture, the intake, the exhaust, the firing or the pistons changes what it delivers, turning any knob can change every metric, either way, in any direction a tuner chooses: that range is the engine's versatility, one engine for many vessels, tuned many ways, for many outputs. What the page shows at any setting other than the factory tune demonstrates that range and is never a benchmark result. Every benchmark result is one engine at its one factory tune: the engine its table names, every benchmark run again on the engine that stands (section 4e). From omni-v17 the factory tune is chosen by a declared rule: of the tunes that harm no gauge against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on development seeds and read again on untouched ones (`docs/THE_TUNE.md`; `DISCLOSURES.md`, section 3). A tune other than the factory tune is the tuner's own, and its results are its own. No profile on this page is locked as the baseline: the factory profile is the one released with the engine, and reading every knob against it, one at a time, is the standing work of the sweeps (`docs/FACTORY_PROFILE.md`).

DISCLOSURE: REAL RUNS, A REAL ENGINE, NOTHING HARDWIRED. Every run played back on this page (sections 3j and 3k) is read from the raw files of benchmark runs executed on GitHub's own machines, each file checked against its run's SHA-256 list before a single number is drawn; every three-run table is read as the repository holds it, each naming its runs, and the raw branch holds their folders as they are archived (the status board, section 2a, marks each run whose raw files are archived). Every model view runs the engine's own code (the compass law, the brain, the verdict) live in this page, linked through software to the repository's Python and C++ and checked against them on every build. GitHub rebuilds the page from the repository whenever the engine, a model or a result changes, and every three hours: no number on it is typed in by hand, and when the repository changes, the page changes with it.

**The road to the engine that stands**

**What this page is**

**Disclosures**

**Contact**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.


## Every monitor

| No. | Monitor | Section | Class | State |
|---|---|---|---|---|
| 1 | Golden signal: errors | 2b The golden signals, the event log and the live metrics | S | live |
| 2 | Golden signal: throughput | 2b The golden signals, the event log and the live metrics | S | live |
| 3 | Golden signal: latency | 2b The golden signals, the event log and the live metrics | S | live |
| 4 | Golden signal: saturation | 2b The golden signals, the event log and the live metrics | S | live |
| 5 | The benefit board | 2d The benefit board | L/S | record |
| 6 | Where the benefit lives, gauge by gauge | 2d The benefit board | L/S | record |
| 7 | The market map: every three-run table a tile | 2d The benefit board | L/S | record |
| 8 | The quote board: every three-run table a quote | 2d The benefit board | L/S | record |
| 9 | The organism, live: native | 3a The organism, live | S | live |
| 10 | The organism, live: Omni-Compass | 3a The organism, live | S | live |
| 11 | The immune system | 3a The organism, live | S | live |
| 12 | The body parts on the band | 3a The organism, live | S | live |
| 13 | The console's response | 3b Control console | S | live |
| 14 | The frame budget | 3b Control console | S | live |
| 15 | One control cycle, traced | 3d One control cycle, traced step by step | S | live |
| 16 | Phase plane: native | 3e Phase plane and scoreboard | S | live |
| 17 | Phase plane: Omni-Compass | 3e Phase plane and scoreboard | S | live |
| 18 | The scoreboard strip | 3e Phase plane and scoreboard | S | live |
| 19 | The brain's state: the well | 3f The brain's internal state | S | live |
| 20 | The brain's state: stress S in its potential | 3f The brain's internal state | S | live |
| 21 | The brain's state: the bath B | 3f The brain's internal state | S | live |
| 22 | Native's own controller beside the brain | 3f The brain's internal state | S | live |
| 23 | The verdict: one trial | 3g The verdict | S | live |
| 24 | The verdict: every true cost | 3g The verdict | S | live |
| 25 | Azure: the bill, run by run | 3h Cloud providers | L (metered by Azure) | record |
| 26 | Google Cloud: the gate and the bill | 3h Cloud providers | L | awaiting its run |
| 27 | Amazon: the gate and the bill | 3h Cloud providers | L | awaiting its run |
| 28 | The cloud setting, live: native's machines | 3h Cloud providers | S | replay |
| 29 | The cloud setting, live: Omni-Compass's machines | 3h Cloud providers | S | replay |
| 30 | The orchestrators' road | 3i Orchestrators and governors | L | record |
| 31 | An orchestrator, four ways | 3i Orchestrators and governors | L | record |
| 32 | The data pipeline, live: every stage from the GitHub Actions run to this page | 3j Kubernetes | L | replay |
| 33 | The official run's heartbeat | 3j Kubernetes | L | replay |
| 34 | The heartbeat sweep: every beat the governor can run at | 3j Kubernetes | S | model |
| 35 | The official run: response time candles | 3j Kubernetes | L | replay |
| 36 | The official run: the heat map | 3j Kubernetes | L | replay |
| 37 | The official run: paired bars | 3j Kubernetes | L | replay |
| 38 | The official run: the repetitions | 3j Kubernetes | L | replay |
| 39 | Per-repetition run telemetry | 3k Kubernetes | L | replay |
| 40 | The shipped controller's trace: native | 3l Kubernetes and cloud | S | replay |
| 41 | The shipped controller's trace: Omni-Compass | 3l Kubernetes and cloud | S | replay |
| 42 | The shipped controller's trace: the strip | 3l Kubernetes and cloud | S | replay |
| 43 | The GPU card, metered: the one real run | 3m Hardware | P | awaiting its run |
| 44 | The CPU host, metered: awaiting its machine | 3m Hardware | S (model) until the run | awaiting its run |
| 45 | An 8-card node: built and awaiting its run | 3m Hardware | S (native model) until the run | awaiting its run |
| 46 | The chip and the host, modelled | 3m Hardware | S | model |
| 47 | Telemetry tensor: the cube | 3n Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 48 | Telemetry tensor: the difference | 3n Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 49 | Telemetry tensor: the modes | 3n Telemetry analytics and Omni-Compass in its own words | S (the harness's record, realms/harness.py) | replay |
| 50 | Service level: the objective | 3n Telemetry analytics and Omni-Compass in its own words | L (the official run's request log, SHA-256-checked) | replay |
| 51 | Service level: the error budget burn | 3n Telemetry analytics and Omni-Compass in its own words | L (the official run's request log, SHA-256-checked) | replay |
| 52 | Telemetry radar | 3n Telemetry analytics and Omni-Compass in its own words | L (the official run's own gauges) | replay |
| 53 | The Python's runs, reproduced here | 3o The Python's runs, in this page | S (the engine itself) | live |
| 54 | The Python's 500 scenarios, replayed | 3o The Python's runs, in this page | S | replay |
| 55 | The Python's Monte Carlo: 500 runs into the basin | 3o The Python's runs, in this page | S (the engine itself) | live |
| 56 | The whole organism, composed | 4a The whole organism, every way it is bought | S (of P and L) | composed |
| 57 | The seven organisms, three loads | 4c Measured effect in full | S | record |
| 58 | Every muscle of the catalog | 4c Measured effect in full | S | record |
| 59 | The scale-out grid | 4c Measured effect in full | S/L | record |
| 60 | GitHub Actions: the runs in flight | 4e CI pipeline | L (GitHub's own API, read at the build) | record |
| 61 | The master switch and the kill switch | 4f The master switch's wiring | S (the page's port of the master switch; the real one is omnicompass/master.py) | live |
| 62 | Self-governed rendering | 4i Self-governed rendering | S | live |

## Every knob

| Knob | What it does | Where it is |
|---|---|---|
| Kill switch | Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white) | the kill switch (section 1a; its wiring, section 4f) |
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
| The muscle's own switch | pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once | the organism's monitors and the muscle's card (section 3a) |
| Runs | how many of the Python's runs this page computes again | the monitor's own buttons |
| Print | the receipts of the runs, printable, with the digests and the notice | the monitor's own button |
| Seed base | which held-out seed base's 500 scenarios are replayed | the monitor's own buttons |
| Set | the Python's own 500 (numpy, seed 223387268) or a set the jump generator drew on this page | the Monte Carlo monitor's set knob (section 3o) |
| Omni-Compass side | the bounded command toward the nearest basin, toward the far basin, or with the double well off (μ = 0); native is the plant alone (u = 0) | the Monte Carlo monitor's way knob (section 3o) |
| Play / pause | the cursor's sweep of the 20 macro steps, held or running | the Monte Carlo monitor (section 3o) |
| Your own system | your stack written as ranges of the core's six states and 22 parameters, run in the page or on GitHub through the Python and the C++ (`systems/README.md`) | the Monte Carlo monitor's own-system panel (section 3o) |

## Every LOSS row, whose it is, its cause and the knob that answers it

156 LOSS rows are Omni-Compass against its native; 171 are an orchestrator's own cost against the organism alone, with no Omni-Compass in either arm. Every one is shown as its table writes it.

- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): response time (ms), 95th percentile, A B C −2.4% (−6.9 to +2.1) · −6.5% (−16.7 to +3.8) · −7.7% (−1.4 to −14.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): response time (ms), 99th percentile, A B C −3.2% (−8.3 to +1.9) · −6.3% (−18.3 to +5.8) · −9.7% (−3.3 to −16.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): failed requests (%), A B C −12.0% (−379.2 to +355.1) · =0.0000 (±0.0000 to ±0.0000) · =0.0000 (±0.0000 to ±0.0000). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −2.8% (−6.0 to +0.4) · −7.7% (−17.7 to +2.4) · −20.6% (−0.0 to −41.2). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): pod start wait, total (s), A B C −125.0% (−300.3 to +50.3) · −666.7% (−151.6 to −1181.7) · −233.3% (−723.9 to +257.2). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): pod start wait, mean (s), A B C −275.0% (−596.0 to +46.0) · −261.1% (−52.5 to −469.8) · −333.3% (−884.0 to +217.3). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): batch: queue finished (s), A B C −1.4% (−0.4 to −2.4) · −2.3% (−1.0 to −3.5) · −1.6% (−3.2 to +0.1). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −5.1% (−1.9 to −8.3) · −8.9% (−4.9 to −12.9) · −9.1% (−0.9 to −17.3). Cause: Job turnaround under Armada, Omni-Compass on the organism alone (`V12_ARMADA_4W_BARE.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_TOP.md`): pod start wait, total (s), A B C −400.0% (−879.7 to +79.7) · −2.3000 (−1.0361 to −3.5639) · −6.7% (−181.4 to +168.1). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Batch queue (omni-v10, `results/live/V10_BATCH.md`): pod start wait, total (s), A B C −142.4% (−731.5 to +446.7) · −18.0000 (−1.9839 to −34.0161) · =0.0% (−337.2 to +337.2). Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Batch queue (omni-v10, `results/live/V10_BATCH.md`): pod start wait, mean (s), A B C −27.3% (−390.6 to +336.1) · −13.1000 (−1.3938 to −24.8062) · =0.0% (−337.2 to +337.2). Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Batch queue (omni-v10, `results/live/V10_BATCH.md`): batch: queue finished (s), A B C −0.5% (−1.2 to +0.1) · −0.9% (−0.2 to −1.6) · −0.8% (−0.2 to −1.4). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): response time (ms), 99th percentile, A B C −2.9% (−7.0 to +1.2) · −2.4% (−8.3 to +3.4) · −2.7% (−5.7 to +0.4). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): time over the response line (% of samples), A B C −40.0% (−89.3 to +9.4) · −27.7% (−118.3 to +62.9) · −14.8% (−52.8 to +23.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −75.0% (−161.4 to +11.4) · −44.4% (−212.8 to +123.9) · =0.0% (−44.4 to +44.4). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): pod start wait, total (s), A B C −500.0% (−1272.6 to +272.6) · −400.0% (−979.2 to +179.2) · =0.0% (−337.2 to +337.2). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): pod start wait, mean (s), A B C −400.0% (−1091.1 to +291.1) · −275.0% (−708.5 to +158.6) · =0.0% (−337.2 to +337.2). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C =0.0% (−337.2 to +337.2) · =0.0% (±0.0 to ±0.0) · −0.1000 (−0.3262 to +0.1262). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): queue: job turnaround, submitted to done, mean (s), A B C −1.4% (−0.8 to −1.9) · −1.0% (−0.4 to −1.7) · −1.2% (−0.7 to −1.6). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): response time (ms), 95th percentile, A B C −4.7% (−11.2 to +1.7) · −6.7% (−15.0 to +1.7) · −5.4% (−12.4 to +1.5). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): response time (ms), 99th percentile, A B C −2.3% (−10.6 to +6.1) · −3.5% (−9.6 to +2.6) · =0.3% (−11.9 to +11.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −0.9% (−4.7 to +2.8) · −11.6% (−25.2 to +2.1) · −3.6% (−11.8 to +4.6). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −4.4% (−10.5 to +1.7) · −3.6% (−10.3 to +3.2) · −4.3% (−10.9 to +2.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): pod start wait, total (s), A B C −80.0% (−284.6 to +124.6) · −100.0% (−494.7 to +294.7) · −0.6000 (−1.2032 to +0.0032). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): pod start wait, mean (s), A B C −260.0% (−7.2 to −512.8) · −62.5% (−392.4 to +267.4) · −0.6000 (−1.2032 to +0.0032). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −2.2% (−6.7 to +2.3) · −2.4% (−6.0 to +1.2) · −5.2% (−0.9 to −9.5). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BARE.md`): pod start wait, total (s), A B C −60.3% (−15.0 to −105.6) · −28.7% (−80.0 to +22.5) · −69.0% (−30.9 to −107.1). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_TOP.md`): pod start wait, total (s), A B C −80.9% (−37.3 to −124.5) · −104.5% (−46.9 to −162.2) · −54.4% (−20.0 to −88.9). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_TOP.md`): pod start wait, mean (s), A B C −8.6% (−26.8 to +9.5) · −21.3% (−1.4 to −41.2) · −0.9% (−16.8 to +15.0). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** CruiseKube (omni-v10, `results/live/V10_CRUISEKUBE.md`): response time (ms), mean, A B C −1.4% (−3.6 to +0.8) · −0.9% (−2.7 to +0.9) · −1.4% (−0.3 to −2.5). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** CruiseKube (omni-v10, `results/live/V10_CRUISEKUBE.md`): response time (ms), 95th percentile, A B C −1.5% (−3.9 to +0.8) · −3.0% (−7.8 to +1.7) · −0.5% (−2.2 to +1.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** CruiseKube (omni-v10, `results/live/V10_CRUISEKUBE.md`): response time (ms), 99th percentile, A B C −1.3% (−7.9 to +5.2) · −3.1% (−11.2 to +5.1) · −2.7% (−0.0 to −5.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): response time (ms), 99th percentile, A B C −0.7% (−4.7 to +3.4) · −9.7% (−21.7 to +2.4) · −5.7% (−23.3 to +11.8). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): time over the response line (% of samples), A B C −8.8% (−42.4 to +24.7) · −42.3% (−93.8 to +9.2) · −6.5% (−60.1 to +47.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −28.6% (−131.3 to +74.2) · −61.1% (−143.7 to +21.5) · =0.0% (−46.2 to +46.2). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C =0.0% (±0.0 to ±0.0) · =0.0% (±0.0 to ±0.0) · −20.0% (−50.2 to +10.2). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): queue: job turnaround, submitted to done, mean (s), A B C −1.5% (−0.4 to −2.5) · −5.3% (−13.1 to +2.4) · −2.2% (−9.9 to +5.4). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): response time (ms), 95th percentile, A B C −2.3% (−9.1 to +4.4) · −6.2% (−16.5 to +4.2) · −1.3% (−11.2 to +8.6). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): batch: queue finished (s), A B C −0.5% (−0.1 to −0.9) · −1.0% (−0.2 to −1.8) · =0.1% (−0.9 to +1.0). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −3.9% (−0.6 to −7.2) · −8.2% (−2.6 to −13.8) · =0.0% (−11.1 to +11.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): response time (ms), 95th percentile, A B C −2.8% (−14.1 to +8.6) · −3.4% (−9.1 to +2.4) · −4.4% (−16.0 to +7.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): response time (ms), 99th percentile, A B C −3.7% (−12.0 to +4.5) · −3.4% (−10.3 to +3.5) · =0.5% (−9.2 to +10.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): pod start wait, mean (s), A B C −433.3% (−984.6 to +117.9) · −166.7% (−369.3 to +36.0) · −25.0% (−221.8 to +171.8). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): batch: queue finished (s), A B C −0.8% (−0.1 to −1.6) · −1.1% (−0.3 to −1.9) · −0.6% (−1.4 to +0.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −62.5% (−146.8 to +21.8) · −15.4% (−91.2 to +60.5) · −14.3% (−46.6 to +18.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −5.6% (−11.7 to +0.4) · −6.5% (−0.8 to −12.2) · −5.0% (−0.2 to −9.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): response time (ms), 95th percentile, A B C −12.7% (−5.9 to −19.5) · −4.6% (−12.9 to +3.6) · −4.0% (−10.0 to +2.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): response time (ms), 99th percentile, A B C −15.0% (−3.5 to −26.5) · −7.4% (−15.3 to +0.4) · −5.7% (−16.8 to +5.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −14.7% (−32.0 to +2.6) · −8.8% (−20.4 to +2.7) · −4.8% (−1.2 to −8.4). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): pod start wait, total (s), A B C −300.0% (−672.5 to +72.5) · −1.2000 (−0.3879 to −2.0121) · −1.9000 (−3.9077 to +0.1077). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): pod start wait, mean (s), A B C −150.0% (−399.4 to +99.4) · −0.9500 (−0.3091 to −1.5909) · −1.2500 (−0.2210 to −2.2790). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): batch: queue finished (s), A B C −2.7% (−1.0 to −4.5) · −1.2% (−2.6 to +0.1) · −2.0% (−0.7 to −3.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −37.5% (−105.9 to +30.9) · −4.0% (−66.5 to +58.5) · −14.3% (−72.3 to +43.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −20.0% (−103.1 to +63.1) · −33.3% (−83.6 to +16.9) · =0.0% (±0.0 to ±0.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −11.6% (−4.9 to −18.2) · −2.2% (−6.0 to +1.7) · −5.8% (−1.3 to −10.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), mean, A B C −13.9% (−28.2 to +0.4) · −10.5% (−21.6 to +0.5) · −2.7% (−13.9 to +8.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), 95th percentile, A B C −20.0% (−4.1 to −35.9) · −16.7% (−1.6 to −31.8) · −2.5% (−11.3 to +6.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), 99th percentile, A B C −12.0% (−1.8 to −22.1) · −11.1% (−1.2 to −21.0) · −4.0% (−12.2 to +4.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): time over the response line (% of samples), A B C −4.9% (−10.0 to +0.1) · −5.4% (−1.7 to −9.1) · −8.3% (−24.3 to +7.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): failed requests (%), A B C −93.2% (−189.8 to +3.5) · −177.2% (−413.2 to +58.9) · −187.3% (−444.8 to +70.3). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): pod start wait, total (s), A B C −250.0% (−712.5 to +212.5) · −72.7% (−291.2 to +145.8) · −100.0% (−364.5 to +164.5). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): pod start wait, mean (s), A B C −32.1% (−211.2 to +147.0) · −59.0% (−238.9 to +121.0) · −44.1% (−219.6 to +131.4). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): batch: queue finished (s), A B C −4.3% (−1.8 to −6.8) · −4.1% (−1.8 to −6.3) · −3.0% (−6.4 to +0.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −15.7% (−5.9 to −25.6) · −14.2% (−6.1 to −22.2) · −9.6% (−20.8 to +1.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kubernetes with KEDA's HTTP add-on on the live requests in flight (omni-v11, `results/live/V11_KEDA_REQUESTS.md`): failed requests (%), A B C −0.0120 (−0.0391 to +0.0151) · =0.0000 (±0.0000 to ±0.0000) · =0.0000 (±0.0000 to ±0.0000). Cause: 1. No tail reads LOSS (`docs/TAIL_LATENCY.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Koordinator under the batch stream (omni-v12, `results/live/V12_KOORDINATOR.md`): pod start wait, total (s), A B C −300.0% (−864.2 to +264.2) · −300.0% (−645.5 to +45.5) · −350.0% (−1004.1 to +304.1). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Koordinator under the batch stream (omni-v12, `results/live/V12_KOORDINATOR.md`): pod start wait, mean (s), A B C −200.0% (−619.8 to +219.8) · −300.0% (−645.5 to +45.5) · −225.0% (−674.6 to +224.6). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): response time (ms), 95th percentile, A B C −5.8% (−1.6 to −9.9) · −6.9% (−15.1 to +1.2) · −5.8% (−12.8 to +1.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): response time (ms), 99th percentile, A B C −6.6% (−17.9 to +4.7) · −7.3% (−16.1 to +1.6) · −3.6% (−8.4 to +1.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −5.3% (−15.3 to +4.7) · −3.9% (−7.9 to +0.1) · −7.2% (−0.2 to −14.2). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C =0.0000 (±0.0000 to ±0.0000) · −100.0% (−506.0 to +306.0) · =0.0% (−337.2 to +337.2). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): batch: queue finished (s), A B C −1.8% (−7.2 to +3.7) · =0.0% (−0.8 to +0.8) · −1.8% (−4.8 to +1.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −5.9% (−14.1 to +2.3) · −1.9% (−8.5 to +4.7) · −3.4% (−7.8 to +1.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): response time (ms), 95th percentile, A B C −6.3% (−13.4 to +0.8) · −7.0% (−2.5 to −11.4) · −3.4% (−7.4 to +0.7). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): response time (ms), 99th percentile, A B C −9.8% (−1.5 to −18.0) · −4.4% (−0.1 to −8.7) · −13.0% (−4.7 to −21.2). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): pod start wait, total (s), A B C −0.5556 (−1.4244 to +0.3133) · −0.5000 (−1.1952 to +0.1952) · −0.6000 (−1.3689 to +0.1689). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): pod start wait, mean (s), A B C −0.5556 (−1.4244 to +0.3133) · −0.3500 (−0.7647 to +0.0647) · −0.6000 (−1.3689 to +0.1689). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): batch: queue finished (s), A B C −0.8% (−0.1 to −1.5) · −0.7% (−0.2 to −1.2) · −0.6% (−0.2 to −1.1). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −57.1% (−168.9 to +54.6) · −120.0% (−301.0 to +61.0) · −76.9% (−219.0 to +65.1). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −200.0% (−505.1 to +105.1) · =0.0% (−119.2 to +119.2) · −50.0% (−125.4 to +25.4). Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −6.8% (−14.2 to +0.6) · −5.0% (−10.2 to +0.2) · −6.1% (−1.9 to −10.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_TOP.md`): response time (ms), 95th percentile, A B C −3.9% (−14.7 to +6.9) · −5.6% (−15.5 to +4.2) · −0.5% (−7.0 to +5.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C =0.4% (−8.5 to +9.2) · −0.6% (−9.1 to +7.9) · −1.0% (−5.7 to +3.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): response time (ms), 95th percentile, A B C −3.8% (−9.8 to +2.2) · −1.6% (−8.2 to +5.0) · −4.4% (−13.8 to +5.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): pod start wait, total (s), A B C =0.0000 (±0.0000 to ±0.0000) · −0.3000 (−0.9786 to +0.3786) · =0.0000 (±0.0000 to ±0.0000). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): pod start wait, mean (s), A B C =0.0000 (±0.0000 to ±0.0000) · −0.3000 (−0.9786 to +0.3786) · =0.0000 (±0.0000 to ±0.0000). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −8.2% (−0.2 to −16.1) · −3.3% (−7.8 to +1.2) · −5.3% (−12.8 to +2.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): failed requests (%), A B C =0.0000 (±0.0000 to ±0.0000) · −0.0093 (−0.0303 to +0.0117) · =0.0000 (±0.0000 to ±0.0000). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −2.6% (−13.8 to +8.7) · −2.9% (−7.6 to +1.8) · −2.0% (−5.1 to +1.1). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −2.6% (−80.1 to +75.0) · =0.0% (−63.2 to +63.2) · =0.0% (−17.9 to +17.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −0.9% (−7.3 to +5.4) · −4.2% (−10.6 to +2.2) · −3.5% (−9.6 to +2.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): response time (ms), 95th percentile, A B C −4.3% (−9.4 to +0.7) · −3.8% (−11.8 to +4.2) · −1.8% (−11.6 to +8.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): response time (ms), 99th percentile, A B C −5.1% (−16.3 to +6.1) · −5.1% (−13.1 to +3.0) · −3.0% (−10.7 to +4.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −2.7% (−0.2 to −5.2) · −2.4% (−5.2 to +0.4) · −10.9% (−22.7 to +0.9). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): pod start wait, total (s), A B C −112.5% (−333.3 to +108.3) · −1100.0% (−243.6 to −1956.4) · −116.7% (−303.5 to +70.2). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): pod start wait, mean (s), A B C −100.0% (−302.1 to +102.1) · −525.0% (−52.2 to −997.8) · −100.0% (−244.8 to +44.8). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): batch: queue finished (s), A B C −2.3% (−0.9 to −3.7) · −1.4% (−0.3 to −2.6) · −1.0% (−2.4 to +0.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −6.5% (−3.2 to −9.9) · −4.9% (−9.9 to +0.2) · −2.3% (−7.5 to +2.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): response time (ms), 95th percentile, A B C −9.2% (−20.0 to +1.6) · −1.6% (−15.2 to +12.0) · −41.2% (−1.6 to −80.7). Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): response time (ms), 99th percentile, A B C −11.2% (−24.3 to +2.0) · −6.9% (−21.4 to +7.7) · −38.0% (−0.1 to −76.0). Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): failed requests (%), A B C −39.5% (−125.8 to +46.7) · −123.7% (−450.7 to +203.3) · −207.5% (−675.6 to +260.7). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −5.7% (−1.4 to −10.0) · −6.1% (−0.8 to −11.4) · −45.5% (−5.7 to −85.2). Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): pod start wait, total (s), A B C −866.7% (−127.9 to −1605.4) · −2.9000 (−1.1014 to −4.6986) · −5.0000 (−10.4892 to +0.4892). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): pod start wait, mean (s), A B C −416.7% (−69.1 to −764.2) · −1.6167 (−0.8358 to −2.3975) · −2.4667 (−5.2106 to +0.2772). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): batch: queue finished (s), A B C −5.5% (−2.2 to −8.9) · −3.0% (−1.0 to −5.0) · −2.6% (−9.5 to +4.4). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −210.8% (−435.5 to +13.9) · −168.7% (−386.7 to +49.3) · −358.1% (−736.6 to +20.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −304.8% (−617.8 to +8.1) · −88.9% (−210.0 to +32.2) · −1389.5% (−2898.4 to +119.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −15.6% (−2.8 to −28.4) · −6.9% (−18.7 to +5.0) · −19.6% (−8.1 to −31.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Robustness (omni-v11, `results/live/V11_ROBUST_LONG.md`): pod start wait, total (s), A B C −268.2% (−723.1 to +186.8) · −135.7% (−466.4 to +195.0) · −138.1% (−64.2 to −212.0). Cause: On omni-v11 (19 October): both scenarios, three runs each, on the rules above unchanged (`docs/ROBUSTNESS_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** A public day of demand (omni-v10, `results/live/V10_TRACE_GOOGLE2011.md`): pod start wait, total (s), A B C −76.1% (−43.5 to −108.6) · −116.3% (−31.1 to −201.4) · −45.1% (−115.0 to +24.8). Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): response time (ms), 95th percentile, A B C =0.2% (−5.3 to +4.9) · −9.1% (−3.9 to −14.2) · −5.3% (−11.9 to +1.2). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): response time (ms), 99th percentile, A B C −1.0% (−4.6 to +2.6) · −5.7% (−1.0 to −10.4) · −4.5% (−1.1 to −8.0). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C =0.0% (−4.9 to +4.9) · −28.9% (−61.6 to +3.8) · −22.1% (−49.8 to +5.7). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): queue: job turnaround, submitted to done, mean (s), A B C −0.9% (−0.2 to −1.7) · −0.9% (−0.1 to −1.6) · −1.2% (−0.6 to −1.8). Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): response time (ms), 95th percentile, A B C −7.6% (−0.8 to −14.5) · −2.9% (−8.8 to +2.9) · −7.5% (−15.1 to +0.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): response time (ms), 99th percentile, A B C −9.7% (−1.9 to −17.5) · =0.4% (−10.6 to +9.7) · −10.4% (−21.7 to +0.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C =0.0% (−159.0 to +159.0) · −25.0% (−126.5 to +76.5) · −150.0% (−391.4 to +91.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C −7.3% (−1.1 to −13.4) · −1.5% (−4.8 to +1.8) · −9.0% (−1.5 to −16.5). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): response time (ms), 95th percentile, A B C =0.3% (−21.7 to +22.3) · −13.4% (−35.1 to +8.4) · −10.6% (−28.2 to +7.0). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): pod start wait, total (s), A B C −100.0% (−506.0 to +306.0) · −1300.0% (−3685.5 to +1085.5) · −1.2000 (−2.7004 to +0.3004). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): pod start wait, mean (s), A B C −100.0% (−506.0 to +306.0) · −600.0% (−1825.1 to +625.1) · −1.2000 (−2.7004 to +0.3004). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C −6.4% (−0.7 to −12.1) · −1.8% (−8.1 to +4.5) · −2.3% (−6.8 to +2.1). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Wandering demand (omni-v10, `results/live/V10_WANDERING.md`): pod start wait, total (s), A B C −32.8% (−89.4 to +23.9) · −4.5% (−91.1 to +82.1) · −14.7% (−57.0 to +27.6). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, mean (ms), A B C -0.4% (-8.4 to +7.6) · +3.0% (-6.0 to +12.0) · +2.9% (-20.8 to +26.7). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA.md`): consumer lag, mean messages waiting, A B C -0.1% (-6.1 to +5.9) · +3.1% (-5.2 to +11.5) · +3.9% (-23.7 to +31.5). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, 99th percentile (ms), A B C +0.6% (-4.3 to +5.5) · +0.8% (-3.8 to +5.4) · +9.1% (-14.1 to +32.2). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, mean (ms), A B C +1.5% (-3.7 to +6.6) · +0.1% (-10.7 to +10.8) · +11.8% (-13.9 to +37.4). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA.md`): consumer lag, mean messages waiting, A B C +1.3% (-4.4 to +7.1) · +0.1% (-10.3 to +10.5) · +11.2% (-13.1 to +35.6). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C +2.5% (-4.5 to +9.6) · -0.3% (-3.4 to +2.8) · +3.3% (-3.3 to +9.8). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, most messages waiting at once, A B C +0.5% (-6.5 to +7.5) · +1.3% (-4.8 to +7.4) · +2.9% (+1.9 to +3.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C +2.9% (-4.1 to +9.9) · -0.2% (-5.9 to +5.4) · +2.4% (-4.4 to +9.3). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C -0.4% (-2.4 to +1.5) · +1.9% (-9.9 to +13.8) · +2.7% (-4.3 to +9.8). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, most messages waiting at once, A B C +1.2% (-14.0 to +16.4) · +1.3% (-4.3 to +6.9) · +1.5% (-7.4 to +10.4). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C -0.5% (-8.2 to +7.2) · +1.9% (-10.3 to +14.0) · +1.7% (-2.4 to +5.9). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): work inside the response line (messages a second handled within the line), A B C -1.3% (-3.1 to +0.5) · -0.6% (-2.8 to +1.5) · -0.4% (-2.2 to +1.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, 95th percentile (ms), A B C +0.9% (-6.0 to +7.9) · +2.6% (-0.7 to +5.9) · -0.1% (-2.6 to +2.4). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C +5.4% (-9.7 to +20.5) · +3.9% (-3.9 to +11.7) · +1.8% (-7.6 to +11.2). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size (the verdict's objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C +4.0% (-11.0 to +19.1) · +3.7% (-4.4 to +11.7) · +1.7% (-7.3 to +10.7). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row EVEN in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Redis, a cache's operator-set memory ceiling (the verdict's objective (omni-v21, `results/live/V21_REDIS.md`): latency, 99th percentile (ms), A B C +0.2% (-0.3 to +0.6) · +0.2% (+0.1 to +0.3) · +1.7% (+0.4 to +3.1). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Redis, a cache's operator-set memory ceiling (the verdict's objective (omni-v21, `results/live/V21_REDIS_SERVICE.md`): latency, 99th percentile (ms), A B C +0.4% (-0.7 to +1.5) · +1.0% (-2.2 to +4.2) · +0.2% (-0.0 to +0.5). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped (the verdict's objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, 95th percentile (ms), A B C +0.0% (+0.0 to +0.0) · +255.1% (-554.4 to +1064.6) · +0.6% (-2.0 to +3.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped (the verdict's objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, mean (ms), A B C -0.4% (-4.6 to +3.9) · +8.7% (-40.0 to +57.4) · -0.1% (-1.7 to +1.5). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped (the verdict's objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, mean (ms), A B C +1.6% (-17.8 to +21.1) · +2.8% (-22.6 to +28.2) · +2.2% (-4.1 to +8.4). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (the verdict's objective (omni-v21, `results/live/V21_YCSB.md`): latency, 95th percentile (ms), A B C +0.2% (-2.9 to +3.2) · +5.4% (-7.8 to +18.6) · +0.7% (-1.1 to +2.6). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (the verdict's objective (omni-v21, `results/live/V21_YCSB.md`): latency, 99th percentile (ms), A B C +0.4% (-4.4 to +5.2) · +2.5% (-0.4 to +5.5) · +1.7% (-2.5 to +5.9). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (the verdict's objective (omni-v21, `results/live/V21_YCSB_SERVICE.md`): latency, 95th percentile (ms), A B C +0.2% (-7.1 to +7.5) · +1.0% (-1.2 to +3.3) · +0.6% (-11.7 to +12.8). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (the verdict's objective (omni-v21, `results/live/V21_YCSB_SERVICE.md`): latency, mean (ms), A B C +0.4% (-6.9 to +7.8) · +1.7% (-1.8 to +5.1) · -0.0% (-9.7 to +9.7). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C +5.8% (-8.1 to +19.7) · +22.6% (-26.5 to +71.7) · +1.9% (-9.9 to +13.7). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 99th percentile (ms), A B C +2.0% (-5.1 to +9.2) · +5.2% (-2.2 to +12.6) · +2.2% (-10.4 to +14.9). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C +1.6% (-2.4 to +5.5) · +4.2% (-17.6 to +26.0) · +6.5% (-8.3 to +21.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C +1.9% (-2.7 to +6.5) · +0.1% (-17.5 to +17.7) · +4.3% (-6.4 to +15.0). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 99th percentile (ms), A B C +4.6% (-6.6 to +15.7) · +0.6% (-49.8 to +50.9) · +4.8% (-2.5 to +12.1). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C +2.5% (-1.5 to +6.5) · +0.6% (-16.5 to +17.7) · +4.7% (-3.9 to +13.3). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C +0.7% (-2.2 to +3.7) · +0.2% (-2.2 to +2.7) · +2.7% (-8.8 to +14.1). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C +0.3% (-2.5 to +3.1) · +1.2% (-3.7 to +6.0) · +1.2% (-2.3 to +4.8). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size (native exactly as the vendor ships it) (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C +0.6% (-2.2 to +3.3) · +2.3% (-1.6 to +6.1) · +0.3% (-1.0 to +1.5). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): pod start wait, total (s), A B C −400.0% (−25.3 to −774.7) · −666.7% (−176.7 to −1156.6) · −433.3% (−1007.0 to +140.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): pod start wait, mean (s), A B C −425.0% (−53.6 to −796.4) · −366.7% (−136.3 to −597.0) · −494.4% (−1023.8 to +34.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): batch: queue finished (s), A B C −72.4% (−61.8 to −82.9) · −68.6% (−58.6 to −78.6) · −86.7% (−75.6 to −97.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1190995.2% (−1185985.7 to −1196004.8) · −1634917.6% (−1630334.8 to −1639500.5) · −1324419.0% (−1319896.0 to −1328942.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −221050.0% (−220287.4 to −221812.6) · −245633.3% (−245069.1 to −246197.6) · −245750.0% (−245056.6 to −246443.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −528.0% (−478.0 to −578.0) · −469.9% (−426.8 to −513.0) · −904.9% (−825.1 to −984.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C −24.0000 (−24.0000 to −24.0000) · −24.0000 (−24.0000 to −24.0000) · −24.0000 (−24.0000 to −24.0000). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): batch: queue finished (s), A B C −72.6% (−62.2 to −83.1) · −68.4% (−58.3 to −78.6) · −86.7% (−75.4 to −98.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1193142.9% (−1189052.7 to −1197233.0) · −1632935.3% (−1629797.0 to −1636073.6) · −1323895.2% (−1320577.4 to −1327213.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −221366.7% (−220793.7 to −221939.6) · −245383.3% (−244977.9 to −245788.8) · −245666.7% (−245189.8 to −246143.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −529.1% (−479.5 to −578.7) · −469.3% (−425.4 to −513.1) · −904.5% (−823.7 to −985.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C −24.0000 (−24.0000 to −24.0000) · −24.0000 (−24.0000 to −24.0000) · −24.0000 (−24.0000 to −24.0000). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), mean, A B C −365.9% (−157.4 to −574.3) · −387.2% (−211.6 to −562.8) · −271.6% (−1.7 to −541.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 95th percentile, A B C −1362.7% (−633.9 to −2091.4) · −1439.3% (−847.3 to −2031.3) · −986.8% (−75.2 to −1898.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 99th percentile, A B C −1691.7% (−817.5 to −2565.8) · −1837.8% (−1123.2 to −2552.5) · −1233.4% (−145.9 to −2320.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): time over the response line (% of samples), A B C −583748.7% (−317248.1 to −850249.4) · −27.7590 (−17.8729 to −37.6451) · −13.9600 (−2.2913 to −25.6287). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): failed requests (%), A B C −0.0076 (−0.0252 to +0.0100) · =0.0000 (±0.0000 to ±0.0000) · =0.0000 (±0.0000 to ±0.0000). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −12.3333 (−7.0357 to −17.6310) · −14.0000 (−10.0676 to −17.9324) · −8.2000 (−2.5094 to −13.8906). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): response time (ms), 95th percentile, A B C −10.5% (−21.8 to +0.8) · −1.0% (−12.1 to +10.2) · −7.2% (−17.7 to +3.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): response time (ms), 99th percentile, A B C −14.2% (−31.2 to +2.7) · −7.9% (−19.0 to +3.3) · −12.7% (−29.1 to +3.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −5.9% (−12.0 to +0.1) · −2.7% (−5.8 to +0.5) · −4.4% (−10.0 to +1.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_ORCH.md`): response time (ms), 99th percentile, A B C −13.8% (−28.2 to +0.5) · −14.7% (−32.7 to +3.2) · −9.9% (−27.3 to +7.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): time over the response line (% of samples), A B C −21.1% (−5.3 to −36.8) · −37.2% (−12.4 to −61.9) · −29.8% (−1.0 to −58.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −1.9% (−6.1 to +2.4) · −28.3% (−59.6 to +3.0) · −8.9% (−22.4 to +4.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): batch: queue finished (s), A B C =0.4% (−0.7 to +1.4) · −0.6% (−1.4 to +0.2) · −0.8% (−1.7 to +0.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): queue: job turnaround, submitted to done, mean (s), A B C −0.7% (−7.7 to +6.2) · −3.3% (−9.3 to +2.8) · −5.0% (−15.0 to +4.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BOTH.md`): response time (ms), mean, A B C −2.2% (−4.4 to +0.1) · −2.4% (−5.1 to +0.2) · −1.7% (−4.4 to +1.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BOTH.md`): pod start wait, total (s), A B C −80.9% (−32.7 to −129.0) · −68.8% (−12.8 to −124.7) · −71.8% (−31.7 to −112.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_ORCH.md`): response time (ms), mean, A B C −2.6% (−0.7 to −4.4) · −3.2% (−0.5 to −5.9) · −2.9% (−0.9 to −5.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_VS.md`): pod start wait, total (s), A B C −60.3% (−28.4 to −92.2) · −56.1% (−0.6 to −111.6) · −51.9% (−20.4 to −83.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_VS.md`): pod start wait, mean (s), A B C −1.6% (−25.0 to +21.9) · −16.8% (−44.7 to +11.2) · −7.8% (−24.3 to +8.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), mean, A B C −0.6% (−10.0 to +8.8) · −7.1% (−17.1 to +2.9) · −6.9% (−16.0 to +2.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 95th percentile, A B C −41.9% (−11.7 to −72.1) · −45.9% (−20.6 to −71.1) · −57.5% (−32.2 to −82.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 99th percentile, A B C −45.2% (−12.1 to −78.2) · −48.9% (−22.4 to −75.5) · −62.1% (−33.1 to −91.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −2.3% (−18.4 to +13.7) · −4.3% (−11.6 to +3.0) · −5.5% (−0.9 to −10.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): pod start wait, total (s), A B C −100.0% (−369.2 to +169.2) · −0.4000 (−0.9001 to +0.1001) · −0.5000 (−1.0058 to +0.0058). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): pod start wait, mean (s), A B C −300.0% (−684.5 to +84.5) · −0.4000 (−0.9001 to +0.1001) · −0.5000 (−1.0058 to +0.0058). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): batch: queue finished (s), A B C −5.1% (−1.7 to −8.5) · −6.9% (−3.4 to −10.3) · −5.1% (−3.0 to −7.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1753.8% (−1040.8 to −2466.9) · −1626.7% (−910.1 to −2343.3) · −915.8% (−807.5 to −1024.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −550.0% (−38.6 to −1061.4) · −650.0% (−129.0 to −1171.0) · −128.6% (−70.6 to −186.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −48.0% (−17.8 to −78.1) · −51.3% (−28.0 to −74.7) · −52.5% (−31.0 to −73.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), mean, A B C −13.2% (−1.6 to −24.8) · −15.8% (−8.1 to −23.5) · −18.3% (−7.5 to −29.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 95th percentile, A B C −38.1% (−7.2 to −69.0) · −41.1% (−19.5 to −62.6) · −50.8% (−22.6 to −79.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 99th percentile, A B C −39.9% (−7.8 to −72.1) · −44.0% (−23.2 to −64.9) · −61.3% (−30.8 to −91.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −1.2% (−13.8 to +11.5) · −6.9% (−4.3 to −9.5) · −6.4% (−2.0 to −10.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): batch: queue finished (s), A B C −4.2% (−1.6 to −6.9) · −5.7% (−2.8 to −8.6) · −4.6% (−2.7 to −6.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1461.5% (−1162.4 to −1760.7) · −1613.3% (−1157.7 to −2069.0) · −968.4% (−828.5 to −1108.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −300.0% (−115.3 to −484.7) · −550.0% (−225.7 to −874.3) · −100.0% (−31.0 to −169.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −40.1% (−16.1 to −64.0) · −42.1% (−24.1 to −60.0) · −45.2% (−26.8 to −63.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_VS.md`): time over the response line (% of samples), A B C −16.2% (−5.8 to −26.6) · −5.0% (−22.3 to +12.2) · −8.2% (−18.5 to +2.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), mean, A B C −45.7% (−15.8 to −75.5) · −33.1% (−14.0 to −52.3) · −25.0% (−7.6 to −42.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 95th percentile, A B C −81.3% (−33.4 to −129.1) · −62.1% (−27.0 to −97.3) · −38.8% (−13.8 to −63.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 99th percentile, A B C −73.4% (−34.4 to −112.5) · −64.1% (−30.5 to −97.7) · −36.5% (−13.7 to −59.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): time over the response line (% of samples), A B C −17.9% (−8.8 to −27.1) · −12.6% (−0.3 to −25.0) · −22.4% (−7.1 to −37.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): failed requests (%), A B C −912.6% (−76.0 to −1749.3) · −0.1452 (−0.2990 to +0.0085) · −1119.8% (−2446.7 to +207.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −45.1% (−21.3 to −68.9) · −34.5% (−21.0 to −48.0) · −30.8% (−18.3 to −43.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): pod start wait, total (s), A B C −600.0% (−1458.5 to +258.5) · −1.9000 (−0.4914 to −3.3086) · −2.2000 (−4.4820 to +0.0820). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): pod start wait, mean (s), A B C −98.1% (−342.1 to +145.9) · −1.0333 (−0.3341 to −1.7326) · −1.2250 (−0.2048 to −2.2452). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): batch: queue finished (s), A B C −16.5% (−7.4 to −25.6) · −15.7% (−8.5 to −23.0) · −14.3% (−5.7 to −22.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −2550.0% (−7297.6 to +2197.6) · −3040.0% (−7128.9 to +1048.9) · −18419.0% (−3305.6 to −33532.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −180.0% (−82.2 to −277.8) · −183.3% (−52.1 to −314.5) · −24360.0% (−1893.1 to −46826.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −83.0% (−40.0 to −126.1) · −78.2% (−42.6 to −113.8) · −57.9% (−24.1 to −91.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), mean, A B C −27.9% (−13.5 to −42.3) · −20.4% (−10.8 to −30.0) · −21.6% (−7.9 to −35.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 95th percentile, A B C −51.1% (−21.9 to −80.2) · −38.9% (−18.4 to −59.5) · −35.4% (−13.9 to −56.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 99th percentile, A B C −54.9% (−23.6 to −86.2) · −47.7% (−25.1 to −70.2) · −31.3% (−13.1 to −49.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): time over the response line (% of samples), A B C −12.4% (−0.5 to −24.3) · −6.9% (−19.9 to +6.2) · −13.0% (−4.3 to −21.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): failed requests (%), A B C −424.2% (−953.0 to +104.6) · −0.0524 (−0.1403 to +0.0355) · −324.7% (−930.4 to +281.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −34.3% (−13.3 to −55.3) · −22.1% (−12.1 to −32.1) · −31.7% (−8.1 to −55.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): pod start wait, total (s), A B C −100.0% (−439.7 to +239.7) · −1.1000 (−2.4676 to +0.2676) · −1.1000 (−2.4254 to +0.2254). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): pod start wait, mean (s), A B C −50.0% (−324.8 to +224.8) · −0.6500 (−1.4049 to +0.1049) · −0.8500 (−1.8338 to +0.1338). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): batch: queue finished (s), A B C −11.7% (−5.1 to −18.3) · −11.2% (−6.1 to −16.2) · −11.0% (−5.0 to −16.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −4531.3% (−13992.7 to +4930.2) · −1692.0% (−4647.7 to +1263.7) · −11114.3% (−22602.3 to +373.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −6540.0% (−21413.9 to +8333.9) · −150.0% (−31.4 to −268.6) · −12780.0% (−31619.7 to +6059.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −58.2% (−28.9 to −87.5) · −56.1% (−30.6 to −81.6) · −44.2% (−20.7 to −67.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_VS.md`): pod start wait, total (s), A B C −100.0% (−248.6 to +48.6) · −9.1% (−181.0 to +162.8) · −72.7% (−250.9 to +105.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_VS.md`): pod start wait, mean (s), A B C −66.7% (−168.4 to +35.0) · −46.2% (−216.6 to +124.3) · −47.1% (−147.8 to +53.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): pod start wait, total (s), A B C −50.0% (−163.1 to +63.1) · −0.7000 (−1.5294 to +0.1294) · =0.0% (−337.2 to +337.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): batch: queue finished (s), A B C −79.6% (−57.4 to −101.8) · −82.5% (−72.2 to −92.7) · −90.2% (−71.9 to −108.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −332575.0% (−204178.2 to −460971.8) · −701433.3% (−502619.2 to −900247.5) · −227980.0% (−149811.1 to −306148.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −172733.3% (−104746.8 to −240719.9) · −763800.0% (−530043.0 to −997557.0) · −136780.0% (−86044.3 to −187515.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −1607.8% (−1081.3 to −2134.4) · −849.4% (−675.6 to −1023.2) · −1322.9% (−1027.8 to −1618.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C −5.3000 (−11.4906 to +0.8906) · −10.7000 (−4.0490 to −17.3510) · −8.8000 (−3.2613 to −14.3387). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): batch: queue finished (s), A B C −76.5% (−54.1 to −98.9) · −82.5% (−72.8 to −92.1) · −86.9% (−68.4 to −105.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −310637.5% (−166814.0 to −454461.0) · −686083.3% (−439006.5 to −933160.2) · −233933.3% (−162122.7 to −305743.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −171200.0% (−91149.9 to −251250.1) · −797900.0% (−545467.5 to −1050332.5) · −139600.0% (−101748.5 to −177451.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −1512.7% (−1011.0 to −2014.4) · −831.8% (−691.5 to −972.0) · −1276.6% (−979.1 to −1574.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C −4.9000 (−10.5971 to +0.7971) · −9.4000 (−3.5091 to −15.2909) · −9.6000 (−3.5005 to −15.6995). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), mean, A B C −40.4% (−83.9 to +3.0) · −148.2% (−55.6 to −240.8) · −71.4% (−13.0 to −129.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 95th percentile, A B C −191.2% (−63.6 to −318.8) · −485.5% (−212.9 to −758.0) · −285.6% (−106.4 to −464.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 99th percentile, A B C −181.3% (−56.9 to −305.8) · −481.6% (−212.0 to −751.1) · −285.0% (−116.9 to −453.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): time over the response line (% of samples), A B C −4381.5% (−8894.3 to +131.3) · −7419.5% (−3065.0 to −11774.0) · −8073.6% (−3500.6 to −12646.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −4.9000 (−0.7503 to −9.0497) · −8900.0% (−4446.3 to −13353.7) · −9500.0% (−6140.7 to −12859.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): response time (ms), mean, A B C −85.7% (−68.2 to −103.3) · −85.1% (−68.5 to −101.7) · −67.0% (−49.1 to −84.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): time over the response line (% of samples), A B C −212.8% (−175.6 to −250.1) · −223.2% (−172.9 to −273.6) · −207.9% (−172.9 to −243.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −202.8% (−146.0 to −259.6) · −216.4% (−168.3 to −264.6) · −157.0% (−115.5 to −198.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): pod start wait, total (s), A B C −1.1111 (−2.5203 to +0.2981) · −0.2000 (−0.6524 to +0.2524) · −0.8000 (−1.6121 to +0.0121). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): pod start wait, mean (s), A B C −0.7407 (−1.6355 to +0.1540) · −0.2000 (−0.6524 to +0.2524) · −0.8000 (−1.6121 to +0.0121). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): batch: queue finished (s), A B C −89.3% (−79.7 to −98.9) · −80.1% (−69.7 to −90.5) · −80.8% (−71.6 to −90.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1967119.6% (−1111934.3 to −2822304.9) · −1287745.8% (−521467.2 to −2054024.4) · −1250833.4% (−747221.5 to −1754445.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −1001696.3% (−623421.0 to −1379971.7) · −230987.0% (−116467.0 to −345506.9) · −285052.5% (−193399.9 to −376705.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −1067.6% (−891.6 to −1243.7) · −910.0% (−690.2 to −1129.8) · −774.9% (−649.7 to −900.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C −13.4444 (−7.1631 to −19.7258) · −11.3000 (−3.8583 to −18.7417) · −14.5000 (−8.3259 to −20.6741). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): response time (ms), mean, A B C −87.9% (−61.0 to −114.8) · −86.6% (−61.9 to −111.4) · −70.6% (−49.8 to −91.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): time over the response line (% of samples), A B C −221.2% (−183.5 to −258.9) · −234.2% (−179.7 to −288.8) · −217.5% (−182.6 to −252.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −204.2% (−145.9 to −262.4) · −219.2% (−169.2 to −269.1) · −159.1% (−116.0 to −202.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): pod start wait, total (s), A B C −0.2222 (−0.7347 to +0.2902) · −0.8000 (−2.0526 to +0.4526) · −0.3000 (−0.7828 to +0.1828). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): pod start wait, mean (s), A B C −0.2222 (−0.7347 to +0.2902) · −0.5500 (−1.3837 to +0.2837) · −0.3000 (−0.7828 to +0.1828). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): batch: queue finished (s), A B C −90.4% (−80.4 to −100.4) · −80.6% (−70.9 to −90.3) · −81.4% (−72.4 to −90.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1959438.6% (−1137492.1 to −2781385.0) · −1280430.0% (−511805.8 to −2049054.2) · −1238207.0% (−751232.1 to −1725181.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −1015791.5% (−684899.6 to −1346683.4) · −228574.2% (−114225.9 to −342922.5) · −286211.2% (−190609.6 to −381812.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −1067.4% (−882.4 to −1252.3) · −927.0% (−727.3 to −1126.7) · −779.3% (−655.6 to −902.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C −14.3333 (−8.2201 to −20.4465) · −11.1000 (−3.7552 to −18.4448) · −14.6000 (−8.6134 to −20.5866). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): response time (ms), 95th percentile, A B C −9.5% (−1.9 to −17.1) · −13.4% (−3.4 to −23.4) · −15.4% (−7.8 to −22.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): response time (ms), 99th percentile, A B C −10.6% (−22.0 to +0.7) · −13.1% (−4.1 to −22.1) · −11.8% (−3.7 to −19.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): failed requests (%), A B C =0.0000 (±0.0000 to ±0.0000) · −0.0093 (−0.0303 to +0.0117) · =0.0000 (±0.0000 to ±0.0000). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −2.6% (−11.0 to +5.9) · −3.9% (−8.8 to +1.0) · −3.0% (−6.5 to +0.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): pod start wait, total (s), A B C −0.1000 (−0.3262 to +0.1262) · −0.3000 (−0.7828 to +0.1828) · −1.2222 (−2.8427 to +0.3983). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): pod start wait, mean (s), A B C −0.1000 (−0.3262 to +0.1262) · −0.3000 (−0.7828 to +0.1828) · −0.7222 (−1.6052 to +0.1607). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): batch: queue finished (s), A B C −1.0% (−0.3 to −1.7) · −1.6% (−0.8 to −2.5) · −1.9% (−1.1 to −2.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −185.7% (−419.5 to +48.1) · −118.2% (−27.2 to −209.1) · −537.5% (−360.4 to −714.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −100.0% (−215.2 to +15.2) · =0.0% (−42.1 to +42.1) · −800.0% (−569.4 to −1030.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −12.5% (−3.2 to −21.8) · −13.8% (−6.4 to −21.3) · −16.6% (−8.6 to −24.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), mean, A B C −7.3% (−0.0 to −14.5) · −6.4% (−1.8 to −11.0) · −8.9% (−3.7 to −14.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), 95th percentile, A B C −12.8% (−0.3 to −25.2) · −10.0% (−1.4 to −18.7) · −10.2% (−2.9 to −17.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), 99th percentile, A B C −13.2% (−27.7 to +1.3) · −7.0% (−0.4 to −13.6) · −11.1% (−5.0 to −17.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): time over the response line (% of samples), A B C −5.2% (−10.5 to +0.2) · −3.9% (−8.5 to +0.7) · −7.2% (−2.9 to −11.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C =0.0% (−6.1 to +6.1) · −1.0% (−8.0 to +6.0) · −1.0% (−3.3 to +1.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): pod start wait, total (s), A B C −0.4000 (−1.3048 to +0.5048) · −0.4000 (−1.3048 to +0.5048) · −0.3333 (−1.1020 to +0.4353). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): pod start wait, mean (s), A B C −0.4000 (−1.3048 to +0.5048) · −0.4000 (−1.3048 to +0.5048) · −0.3333 (−1.1020 to +0.4353). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): batch: queue finished (s), A B C −0.9% (−1.9 to +0.1) · −1.1% (−0.3 to −1.8) · −1.4% (−0.6 to −2.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −178.6% (−75.7 to −281.5) · −118.2% (−22.2 to −214.1) · −537.5% (−313.8 to −761.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −233.3% (−118.2 to −348.5) · −25.0% (−62.7 to +12.7) · −700.0% (−394.9 to −1005.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −11.5% (−0.3 to −22.7) · −9.3% (−2.0 to −16.5) · −12.7% (−5.4 to −19.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), mean, A B C −59.9% (−38.6 to −81.3) · −51.7% (−23.3 to −80.0) · −58.7% (−37.1 to −80.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 95th percentile, A B C −51.5% (−36.6 to −66.4) · −55.2% (−22.4 to −88.0) · −55.0% (−29.0 to −81.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 99th percentile, A B C −49.4% (−31.0 to −67.8) · −58.4% (−25.9 to −90.9) · −52.9% (−30.2 to −75.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): time over the response line (% of samples), A B C −55.9% (−30.2 to −81.5) · −23.9% (−11.2 to −36.5) · −75.5% (−53.5 to −97.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): failed requests (%), A B C −1075.1% (−3104.7 to +954.5) · −1410.9% (−3307.7 to +485.9) · −41.3% (−301.7 to +219.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −24.8% (−18.0 to −31.6) · −26.6% (−20.5 to −32.7) · −74.3% (−40.2 to −108.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): pod start wait, total (s), A B C −262.5% (−638.2 to +113.2) · −1350.0% (−337.7 to −2362.3) · −733.3% (−1506.4 to +39.7). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): pod start wait, mean (s), A B C −181.8% (−456.0 to +92.4) · −708.3% (−164.7 to −1251.9) · −516.7% (−1102.4 to +69.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): batch: queue finished (s), A B C −21.4% (−16.0 to −26.8) · −19.4% (−11.5 to −27.4) · −19.1% (−13.1 to −25.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −14475.7% (−1985.4 to −26966.0) · −15860.7% (−1447.0 to −30274.5) · −17305.6% (−349.2 to −34262.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −22685.7% (−4894.5 to −40476.9) · −13100.0% (−1240.5 to −24959.5) · −16980.0% (−170.1 to −33789.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −70.9% (−54.6 to −87.2) · −67.7% (−38.0 to −97.5) · −76.8% (−55.5 to −98.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), mean, A B C −43.6% (−24.2 to −62.9) · −56.4% (−31.6 to −81.2) · −15.7% (−63.5 to +32.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), 95th percentile, A B C −38.7% (−19.4 to −58.1) · −52.7% (−28.2 to −77.2) · −9.8% (−62.5 to +42.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), 99th percentile, A B C −34.4% (−13.7 to −55.0) · −48.2% (−27.5 to −69.0) · −10.8% (−62.1 to +40.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): time over the response line (% of samples), A B C −38.4% (−26.1 to −50.6) · −26.6% (−12.2 to −41.0) · −17.6% (−69.8 to +34.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −18.1% (−12.6 to −23.7) · −19.4% (−10.7 to −28.0) · −19.8% (−73.8 to +34.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): batch: queue finished (s), A B C −15.0% (−9.3 to −20.7) · −15.9% (−9.3 to −22.6) · −16.1% (−4.7 to −27.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −4589.2% (−12556.0 to +3377.6) · −5839.3% (−343.3 to −11335.2) · −4080.2% (−10503.3 to +2342.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −5528.6% (−14699.6 to +3642.5) · −6887.5% (−13992.2 to +217.2) · −1177.8% (−3216.5 to +860.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −47.9% (−27.4 to −68.3) · −57.0% (−30.7 to −83.2) · −46.0% (−18.7 to −73.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, total (s), A B C −466.7% (−186.8 to −746.5) · −2.4000 (−0.9225 to −3.8775) · −1.3000 (−0.4047 to −2.1953). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, mean (s), A B C −266.7% (−26.9 to −506.4) · −1.2500 (−0.6136 to −1.8864) · −0.8000 (−0.2615 to −1.3385). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): pod start wait, total (s), A B C =0.0% (−168.6 to +168.6) · −366.7% (−1211.2 to +477.8) · −500.0% (−1326.0 to +326.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): pod start wait, mean (s), A B C −100.0% (−326.2 to +126.2) · −366.7% (−1211.2 to +477.8) · −500.0% (−1326.0 to +326.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): batch: queue finished (s), A B C −1.8% (−0.8 to −2.8) · −1.7% (−0.4 to −2.9) · −1.8% (−0.4 to −3.2). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1126.7% (−1020.2 to −1233.2) · −1088.9% (−690.1 to −1487.7) · −1416.7% (−986.8 to −1846.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −333.3% (−174.4 to −492.3) · −450.0% (−38.7 to −861.3) · −550.0% (−436.9 to −663.1). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C −32.1% (−13.4 to −50.8) · −19.7% (−5.5 to −33.9) · −26.0% (−8.1 to −43.9). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): batch: queue finished (s), A B C −1.2% (−0.6 to −1.8) · −1.4% (−0.4 to −2.5) · −1.4% (−0.3 to −2.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C −1053.3% (−883.9 to −1222.8) · −866.7% (−664.7 to −1068.6) · −1491.7% (−1085.0 to −1898.3). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C −366.7% (−231.3 to −502.0) · −275.0% (−78.2 to −471.8) · −500.0% (−331.4 to −668.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C −24.2% (−10.9 to −37.5) · −17.6% (−5.6 to −29.5) · −23.2% (−6.9 to −39.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), mean, A B C −20.0% (−0.7 to −39.3) · −11.4% (−29.2 to +6.3) · −13.1% (−27.6 to +1.5). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), 95th percentile, A B C −92.6% (−46.7 to −138.5) · −31.9% (−10.8 to −53.0) · −50.9% (−23.2 to −78.6). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), 99th percentile, A B C −73.3% (−31.5 to −115.1) · −9.6% (−27.4 to +8.3) · −23.6% (−1.1 to −46.0). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): time over the response line (% of samples), A B C −124.1% (−51.4 to −196.7) · −50.2% (−5.7 to −94.8) · −54.8% (−19.1 to −90.4). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C −30.3% (−6.8 to −53.8) · −11.3% (−26.1 to +3.6) · −23.2% (−48.2 to +1.8). The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
