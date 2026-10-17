# CLAUDE.md: standing orders for any session working on this repository

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

These are the founder's orders, gathered from the full working record. They load every session. Follow them unless
the founder overrides one in the conversation.

## What Omni is

- Omni-Compass is a **supervisory governor**. It always sits **on top of a native controller**: the Kubernetes HPA,
  GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo, and so on. It is never standalone and never a
  competitor to native.
- Every benchmark has exactly two arms, **native** and **omni** (omni means Omni on top of native). There is no other
  arm and no other name.
- **Do no harm.** Omni must never cause a LOSS against native. Where it can't bring a knob a GAIN,
  that knob stays native. The 2%
  verdict (`omnicompass/verdict.py`) is the engine's trigger, not a stamp on a report. Gains are uncapped.
- Headline: more work, faster, on fewer machines, with less energy. One combined number: the Omni index.
- **The max is the default brain** (12 October): every muscle runs at its own limit, never past it and never below
  native; it rides the edge, not the middle. "We're never looking to shave energy": the energy it takes is **power
  given**, shown beside the work, the speed and the wear it bought, never called a loss; the max never takes from one
  muscle to give to another. Results are judged on work, speed, misses and failures. Anyone can tune it down from the
  max (the dial: the tune-down, `V5SAVE`). A knob native already runs at the top of its range is "at its limit on native".
- The word is **compass**, never "bowl". The law is `omnicompass/compass_law.py` (`CompassLaw`): a band with 5%
  cushions, two antagonist forces, smooth (tanh), not hammering.
- Wiring is a two-way plug, one wire in and one wire out. The brain does the math. The knob is restored to the snapshot
  taken once, at the start.
- **One pedal, no brake** (12 October), like an electric car: push for more, lift off for less; lifting hands the
  setting back toward native; idle is the pedal lifted all the way; reset hands everything back to native; cruise (a
  known queue waiting), autopilot / watching / off. After a crash the plug walks every setting back to native gradually
  (the lease); the **kill switch** is separate, for security only, and instant (`omnicompass/master.py`,
  `tools/omni_switch.py`). The word "brake" is not used.
- Scaling: floor of 2 machines, no ceiling, every machine usable. Traffic tests step by one (1 2 3 2 3 4 …).
- Nothing is hardwired. Anything that doesn't work is removed, not just switched off.

## The engine: Omni v9 stands (v8, v7, v6, v5, v3, v2 and v1 kept for their results)

- **Omni v9** (`OMNI_V9.json`, digest `7379f3a79ff2c475`, 47 files; `docs/OMNI_V9.md`) stands on main since 17 October,
  the founder's order ("we're going into another version of Engine ... Apply the fix, run it, and see in the toy sim that
  it works"; then "go go go"): omni-v8 with the CityLearn battery wire reading the coming hour (the mean of the same hour
  over the past seven days, only hours already seen) and gliding at up to 0.0625 an hour (0.05 before; the fastest glide that read no LOSS on any score
  in any district: 0.075 and faster raised the ramping in one district), because the reading of
  the hour gone ran about five hours behind the day and left the batteries empty at each month's top hour (the 2022
  robustness district's monthly unevenness +0.11%, power given: a peak, a swing and an unevenness are power held, the
  founder's correction of 17 October); and every 95% interval on the exact Student t quantile
  (`omnicompass/student_t.py`; every tabled value unchanged, no published reading moves). Proven locally on CityLearn
  3.0.2 and in the toy gate (`results/toy_gate/V9_VS_V8.md`, identical to v8 on every toy) before it was pushed. 44 of its
  47 files are omni-v8's bytes. Every benchmark runs again on it; the omni-v8 and omni-v7 tables stand as their own until
  each benchmark's three runs on v9 land.
- **Omni v8** (`OMNI_V8.json`, digest `f93d233136a1f902`, 46 files; `docs/OMNI_V8.md`) stood on main on 17 October,
  the founder's order ("there's a new version 8 ... push in all and update all"): omni-v7 with one wire changed, the
  CityLearn runner (`tools/run_citylearn.py`): a battery whose building simulates power outages stays native, because its
  charge is also its building's reserve (omni-v7's CityLearn table read LOSS in all three runs in the seven 2023 districts,
  the only ones with outages; every other district's commands are omni-v7's bytes). The other 45 engine files are omni-v7's.
  Every benchmark runs again on it (`scripts/reruns.txt`; the conductor's reruns, grid and Azure queues restarted on 17
  October); one row the table printed LOSS stayed, the 2022 robustness district's monthly unevenness (+0.11%), power given by the
  key, and cut in omni-v9.
- **Omni v7** (`OMNI_V7.json`, digest `d6d467b824c585f1`, 46 files; `docs/OMNI_V7.md`) stood on main 16 to 17 October,
  the founder's order ("Where is version 7? That's what you gotta push everything to"): v6's law, catalog and shared-host
  capacity repair (on kind every node is a container on one runner: its processor is counted once and no replica is
  added while that runner is 75% busy or unread, `omni_controller/capacity.py`), plus conveyance bounded by each
  namespace's CPU quota (`omni_controller/quota.py`; an unreadable quota is no budget known, Kubernetes admission is the
  authority), on a shared host no limit raised while the machine is 75% busy or unread, the verdict reading a trial in
  the reports' words (GAIN, EVEN, LOSS: a clear rise refused), every rule in seconds, the cloud's one flag
  `--give-back-only`. Two repairs first written for the KEDA pod start wait were refused by the toy gate and are not in
  it. Its seventeen three-run tables of 17 October (`results/live/V7_*.md`) and its twelve trial runs of 16 October
  (Goldilocks, KEDA's add-ons, fixed capacity, CruiseKube; A, B and C) are its own. **Omni v6** (`OMNI_V6.json`, `docs/OMNI_V6.md`) stood one day, 15 to 16 October; its four
  three-run tables are its own.
- `OMNI_V5.json` and `docs/OMNI_V5.md`: the max (`realms/compass_arm_v5.py`, `V5CFG`) on the 1,107-muscle catalog, the
  bone inside every organism with the living body's immune system (V6-V13, `docs/FORMAL_V5.md` section 4: native twins
  of every room, the heat debt, batteries timed for their lines, nothing locked), every muscle its own card
  (`realms/muscle_cards_v5.csv`, 364 muscles, found by `tools/tune_cards.py` on development seeds only and kept only when
  it wins twice and never falls behind native on any seed; inside a body a battery wired by its power keeps the body's
  margins, V14; `docs/FORMAL_V5.md` section 5), the lease's walk back, the tune-down on the dial. v5 is re-declared on
  every engine change while in development. `OMNI_V3.json` (`docs/OMNI_V3.md`), `OMNI_V2.json` and `OMNI_V1.json` stay for their results,
  never up front. Check with `python3 tools/omni_version.py [--commit <sha>]`: it prints omni-v9, omni-v8, omni-v7, omni-v6,
  omni-v5, omni-v3, omni-v2, omni-v1, or what differs.
- The version numbers are bookkeeping so no result is read across engines. When the founder says the engine is final, the
  engine that stands then is published as **Omni-Compass 1.0**; the older fingerprints go to `docs/history` as the road to
  1.0, never as a second product.
- Any change to a rule, gain, guard, preset or muscle makes **the next version**, and every result is run again on it. Never read a result across
  versions. Never change the engine without telling the founder first.
- Three runs: each benchmark runs as A, B and C (`tools/confirm_abc.py`). Every judged row gets one of three
  readings: GAIN or LOSS in all three of our runs (the same sign in all three, every 95% interval clear of zero, the word
  set by the gauge's aim; a resource spent that rose is power given); EVEN, no difference beyond the noise (an interval includes zero: that is the result, say so); the runs disagree (clear runs
  pointing different ways: the test is unstable there, look into it). Never write "confirmed" or "not confirmed"
  (the founder's order of 11 October: nobody outside approved these results); every three-run table says "Run and
  scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
  (`tools/readings.py`).
- Evidence classes: P (physical meter), L (live software), S (our own models). Never present S as proof.

## The seven organisms and the grid

- **Seven organisms** (the founder's order of 16 October): the **spine** (267 muscles, every muscle that sits in all four
  realms, the base every stack runs on as an operating system is the base of every program; `docs/THE_SPINE.md`), the four
  realms (Compute/AI/Cloud 540, Physics/Robotics/Autonomous 404, Energy/Facility/Industrial 480, Distribution/Specialized
  484, each its own families on the spine), the four stacked (1,908, the spine once in each realm's body) and the whole tower
  (1,107 distinct muscles in 70 families, the founder's nine open-source pieces among them: Kepler, Climatik, EAR, CruiseKube,
  Goldilocks, the Kubernetes Power Manager, PEAKS, Adaptive GPU Power Capping, NVIDIA's platform power manager). Every one
  runs native and with Omni-Compass on top of native. The organisms are groupings of catalog rows made in the runners
  (`tools/run_realms_v5.py`, `run_scale.py`, `run_hil.py`, `run_kil.py`), never in a fingerprinted engine file; the spine is
  `spine`, organism 7 in the numbered runners, and listed first on every page. Earlier catalogs' counts stay with their
  results in `docs/history`.
- The organisms are named `tower`, `stack` and `spine` in code and workflows (never by a count); the old names `organism_656`
  and `stack_1226` are read as aliases.
- The grid: each organism runs native and omni at clustered copies × runs: 63 squares (seven organisms) at 1, 10 and 100 copies × 1, 10
  and 100 runs, modelled and with the real cluster inside, with both values shown in every square. **On GitHub's own
  machines only, the 1,000 tier stands again** (the founder's distinction of 15 October, `scripts/dispatch_grid.py`,
  `docs/OMNI_V6.md`): the seven organisms and their modelled, Kubernetes, Linux and swarm workloads run at 1, 10, 100 and
  1,000 copies and nested 1, 10, 100 and 1,000 runs on free runners, and a cell beyond a free runner's memory or time is
  listed as pending runner capacity, never rented; **paid cloud and GPU runs stay at 1, 10 and 100 copies with at most
  100 repetitions** (the founder's order of 12 October, kept for everything that costs money). Nothing is rented for the
  grid. Every grid button starts all its sizes × all its run counts and uses every runner GitHub gives. The conductor
  (`scripts/dispatch_grid.py`, `grid.yml` every 15 minutes; the six and six-kube buttons with their defaults) starts every
  run not yet started, reads started runs back from their names, never starts one twice, and keeps the queue at what
  GitHub runs plus a margin; it starts nothing while an Azure run, a grid report or a verify waits for a runner (Azure
  first). It also releases the reruns of every benchmark on the engine that stands (`scripts/reruns.txt`; A of
  every benchmark, then B, then C; a few a tick; read back by count, never started twice). It starts every Azure set from `scripts/azure_queue.txt` (A of every set, then B, then C; one at a time in each
  machine family's queue; read back by its run's title, never started twice): the steady set, the bursts `1 4 1 6 1 9`
  and `1 6 1 8 1 6`, and the real day (Google 2011) on 1 to 9, every one at the tune-down with native's cap (the founder's words of 14 October; the load generator alone
  reads a schedule, never the governor). Google Cloud and Amazon carry the same four sets from `scripts/google_queue.txt` and
  `scripts/amazon_queue.txt`, each behind its own `switch=` line, off until that cloud's secrets are in the repository and the
  founder turns it on (16 October: the Azure run is the measure of the other two clouds, the same tuning, mechanism and harness). Each tick runs the conductor's newest
  code (fetched from the branch). `peek` (`.github/workflows/peek.yml`) prints a running run's finished repetitions,
  paired, so a benchmark is looked at while it runs and a problem fixed before it ends. Shards are cut from measured run times; each stops at its deadline and hands in every run it finished. With
  the cluster inside only runs of protocol 3 count (12 Oct: the governor never below the organism's CPU priority, its
  decisions counted inside the window; 13 Oct: the model of the organism on the runner's last core and the kind nodes on
  the others, the same in both arms); a repetition whose job fails runs again, up to three times, paired within one run,
  and one that fails three times is listed. With the cluster inside, the window is set from the heavier arm's step,
  timed before either arm, so the max keeps the organism's clock.
- Three loads: each organism's own load, the climb (the load stepping by one, 1 2 3 2 3 4 …) and work waiting in line
  (`LINE`, `realms/harness.py`); every muscle alone runs its own load and the line.
- Benchmark breadth: every domain that can be benchmarked defensibly (`docs/REGISTER.md`), with Omni on top of that
  domain's own native controller, one or two at a time.
- GPU: all old GPU results are obsolete. The founder reruns them on Lambda. Never spend GPU money before the CPU side
  is done, and give the founder one exact commit.

## Honesty

- Report every row, losses included. Never drop a row because it went against Omni. If Omni loses, first suspect our
  own wiring, native setup or scoring; fix that, then rerun. The founder may choose not to publish a benchmark; it is
  never published with rows cut out.
- Preregister before running, freeze the rules on one tuning case, and test on untouched cases.
- "Flake" is not a root cause.

## Legal, on every output

- At the top and end of every output: © 2026 The Omni-Compass LLC; all rights reserved; evaluation and simulation use
  only; any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License; then **all**
  patents, copyrights and trademarks filed in the USA (say "filed", never give numbers), followed by www.omni-compass.com
  and nothing after it (the founder's wording of 10 October: the word "all" before patents and "all rights reserved"
  everywhere; that night he struck two earlier sentences from the notice, and they stand nowhere: no page, header, report,
  license paper or program output carries them, and `tools/legal.py --check` fails any file that does).
- Every export of any part of Omni-Compass (a zip, a report, a table, a PDF, a chat answer) carries the README's notice,
  the LICENSE, the NOTICE and DISCLOSURES.md the same way, written as a multi-billion-dollar company would protect a
  released asset.
- Keep the SPDX headers so Black Duck, FOSSA and Snyk detect the license.
- The notice is written once, in `tools/legal.py`; `python3 tools/legal.py --fix` puts it on every page, header, workflow
  report and export, and `--check` (run by `verify.py`) fails any push where a file lacks it. Engine files locked by a
  fingerprint take the new header only with the next engine version.

## Orders of 15 October

- **The toy gate first** (the founder's order of 15 October, night: every fix, knob and rule is tried in a toy model
  before it is pushed, and goes to a real run only where it shows promise there). Every change to the engine or to a
  live controller runs in our own models (`tools/toy_gate.py`: the shipped controller on the toy cluster in the cloud
  setting at 60 and 15 s, conveyance on one kind host set to the v6 KEDA run's own regime, the verdict on noisy work)
  against the engine that stands, on the same seeds, paired, read GAIN, EVEN or LOSS by the gauge's aim. A LOSS there
  is root-caused and fixed in the model, never carried into a real run; a change that reads no LOSS and shows promise
  goes to its GitHub trials; nothing is dispatched before. The gate's readings are models (class S), recorded in
  `results/toy_gate/` and never presented as a benchmark result. The toy's regime is set from a real run's own files
  (the host's busy share, the response time, the replicas), never guessed.

## Orders of 17 October

- **One key for every gauge** (the founder's correction of 17 October, night: "a minus doesn't mean a loss and neither does a
  plus mean a gain if you don't understand what it's against"). LOSS is only time waited, missed or failed that rose, or work
  that fell. A peak, a swing, an unevenness, wear and every other resource spent or held is power: a fall is a cut, a GAIN, a
  rise is power given, never a LOSS; work per energy that falls is power given too. The CityLearn tool had filed peaks, swings
  and unevenness as misses and the grid had judged work per energy as work, so rows that were power given were printed LOSS;
  both read through `tools/readings.py` now, and every result was re-read: on the engine that stands, no LOSS.

- **Version 9: the fix proven in our own runs first, then pushed** (the founder's words: "Engine fix goes into models
  first ... Apply the fix, run it, and see in the toy sim that it works ... lock everything else that you're not touching
  ... Get rid of dead weight"; then "go go go"). omni-v9 is on main and on the branch `v9`; every page, manual, table and
  queue points at it. **Native as shipped**: MySQL, Redis and MongoDB run with native exactly as the vendor ships them
  beside the operator's setting (`--native shipped`); where the factory setting is already at the knob's top, the knob
  reads "at its limit on native" and Omni-Compass watches. **Every level on one page** (`docs/LEVELS.md`, `tools/levels.py`,
  checked by `verify.py`): the muscle, the organism, the cluster, its add-ons, the service, the plant, the cloud and a group
  of clusters, each with its counts, and any level whose gauges go the other way is named and taken to the founder.
- **Version 8 stands; push in all and update all** (the founder's words: "there's a new version 8. That means you got to
  push in all and update all ... We're going to start the GPU soon and the other two clouds"). omni-v8 is on main and on
  the branch `v8`; every page, manual, table and queue points at it; every benchmark runs again on it. The GPU runs on
  Lambda and the Google and Amazon sets start on his word: the GPU from one exact commit given to him, the two clouds by
  turning their `switch=` line on once their secrets are in the repository.
- **The page number in both bottom corners, the running head on every page.** Every page of both manuals but the title
  page carries the book's name on the left of the head and the part or chapter it belongs to on the right (openers and
  front matter included), and the page label in the left and the right bottom corner, "so that when somebody can flip
  through it" they know where they are. The notice stays at the foot of every page.
- **The navigation is checked row by row before every push**: every Contents row against the page where its heading is
  printed, every List of Figures row against the page of its caption, every index reference against the page it names,
  every figure against the paragraph that names it (under it when it fits, else at the top of the next page, never
  further, never more than two to a page, never in one block), the running head and both corner numbers on every page.
  "Every time and every fix and change and upgrade" realigns both manuals in the same push.
- **Every figure is read at referee level before it is placed**: what it pictures, where it lives, the mechanism it
  states (the book, the Python, the harness, the organisms), its mathematics, structure, grids, arrows and direction;
  anything under full comprehension is reworked before the push. Nothing may mislead the wiring of Omni-Compass into a
  stack.
- **Every benchmark that can exist has its place.** The register names every domain of the industry, every realm and
  every muscle with the software available to benchmark; where a benchmark is not yet run, its place is written and
  marked as not yet run, never with a result before the result exists. The gap audit against the whole industry (who we
  have, who we do not, whose software is available) is standing work.

## Orders of 16 October

- **Seven organisms, the spine the seventh.** The spine (267 muscles, every muscle in all four realms) is an organism in its
  own right: the base every stack runs on, as an operating system is the base of every program. With the four realms, the four
  stacked and the tower that makes seven; "all seven need to be wired, written everywhere, native, and with Omni-Compass wired
  on native." The spine is written into the runners and the pages (`docs/THE_SPINE.md`, bound into both manuals), never into a
  fingerprinted engine file; the engine's fingerprint does not move for it.
- **Older versions are history.** "Why do I want to hear about version 5?" Everything worked on is the newest engine; what is
  found to have more room goes into the next version. Reports say native against Omni-Compass,
  gauge by gauge, never one version against another; older fingerprints are the road, in `docs/history`.
- **Nothing is cancelled.** No run is ever cancelled; a problem found in a running benchmark is fixed and the benchmark run
  again. Everything except the GPU chips and the Google and Amazon clouds runs, pushes and benchmarks.
- **Azure finishes first.** The founder decides on Google and Amazon after the Azure results are where he needs them, because
  Azure teaches what the other two will need.
- **Both manuals carry every muscle with its physical wiring on any stack** (the wiring appendix, `docs/wiring_recipes.csv`),
  and the whole package is kept in line with the newest engine top to bottom, fixed and tightened as found, pushed to the real
  places: it is presented to one buyer.

## Orders of 14 October

- **In the cloud, the bill** (the founder's order of 14 October, night). In a cloud (Azure now; Google and Amazon when he
  starts them) Omni-Compass is to show one thing: the same work as native for a smaller bill, never a bigger one. Every
  cloud set runs Omni-Compass on top at the tune-down (`dial save`) on the machines alone (`OMNI_MACHINES_ONLY=1`): no pod
  autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's; the governor only parks a
  machine the cloud already made, after its own trial, and wakes it on a breach. No more pods and no more machines than
  native: the bill can only fall or stay. The bill and the machines aim lower, and work, speed and failures must read
  EVEN or GAIN. The benefit of the max belongs where Omni-Compass sits in the engine before the cloud, or in the
  chip at its other end. Runs of the max in the cloud are stopped and kept as such, counted in no bill result.
- **On autopilot: no babysitting tax** (the founder's words of 14 October, night). Omni-Compass is an autopilot,
  self-running, self-steering and self-auditing inside the system like a self-driving car: nobody turns a knob, nobody
  checks its work (every write read back, every give-back on its own trial, every reason in its audit) and nobody has to
  react, because it acts before the line is crossed. In the cloud the aim is no alert minute at all (a minute over the
  line wakes a person): an alert minute in the omni arm is found and fixed, never accepted.
- **Faster, but only where it hurts nothing** (the founder's words of 14 October, night). The governor is to move faster
  than every native controller under it (asked: a decision every 15, then 10, then 5 seconds), and no change is made
  until it is known to hurt nothing anywhere. Its fast checks already run every 5 s (native's pod autoscaler: 15 s); its
  full decision stays at 60 s in every run, because four of its rules count in decisions (a give-back trial's 20-decision
  phase would shrink to 100 s at 5 s and every trial would be abandoned, so the bill could never fall; at 15 s the phase is
  5 minutes and the wait after a breach 45 s instead of 3 minutes, and both are written in the engine). Native's own
  15-second check runs underneath untouched. The next engine version counts those rules in seconds and puts the fast
  checks on their own clock; it is used only when a test shows no LOSS. Every Kubernetes and cloud receipt shows it in both arms: the
  alert minutes (judged), the settings commands the governor wrote on its own and its additions made inside the line
  (shown) (`tools/live_reps.py`, `babysitting`); both manuals and the README say so.
- **Two manuals** (the founder's orders of 14 October, evening and night), both kept in the repository until the founder
  takes the Owner's Manual out:
  - **The Operator's Manual** (`docs/OMNI_COMPASS_MANUAL.md` and `.pdf`): the glove box, not the blueprint. It shows an
    engineering team how to embed, wire, tune, run and check Omni-Compass on a stacked, clustered system, or on any one
    muscle, in all its processes. It does not explain what is inside Omni-Compass or how it is built: no theory, no
    equations of the engine, no gains or internal rules, no engine source, no benchmark results (those stay in `results/`
    and `docs/STATE_OF_PLAY.md`). The engine is shown only as its shell and its process. Nothing in it explains or points
    to how the code is written, and nothing is disclosed or disclaimed about it. It is at least half the Owner's length
    (the founder's order of 14 October, night) and carries the implementer's whole cloud path (Part VI, chapters 13 to
    30, with the install files in `deploy/install/` and `deploy/Dockerfile.cloud`): Google and Amazon ready the way Azure
    is, the governor on the machines alone in every cloud.
  - **The Owner's Manual, the master** (`docs/OMNI_COMPASS_OWNERS_MANUAL.md` and `.pdf`, `build_book.py --owner`):
    everything and all, for whoever owns or licenses Omni-Compass and so must know the whole mechanism: the philosophy and
    theory (`docs/book/THEORY.md`, `docs/book/DECLARATION.md`), the mathematics, the mechanism, how it is built, the
    engine's source, every result, and the wiring. Every fix realigns both.
- **The manuals carry drawn figures, no plates and no blank pages** (the founder's orders of 14 October and of 16 October,
  night: "flow charts, illustrations to interpret the language of mathematics, build it in the manuals"; then, the same
  night: fifty more that interpret the code, the wiring and the receipts, "with another tool", so they do not all look the
  same). Two kits draw them from the book's own code and the repository's own files: `docs/book/figures.py` (reportlab: the
  two-way plug, the compass band and the two forces, one decision of the governor, the eight levels, the one pedal, the seven
  organisms, the three-run rule; in the Owner's Manual also the engine's six states and the double well) and
  `docs/book/schematics.py` (schemdraw and matplotlib: a wiring schematic for every stack in the grammar of an electrical
  drawing, the governor with its sense and motor terminals, the kill switch, the plug, the native controller, the muscle and
  the meters; the control-loop block diagrams; the flowcharts of the wire check, the paired run, the gate, the verdict, the
  stops, the toy gate, the reading rule; the timing diagrams and modelled traces, marked class S; the state machines; every
  receipt of the engine that stands charted from its own table; the grids of the organisms and the catalog). A chart of a
  receipt pictures the table and adds nothing to it. Each figure is placed where a manual carries an image line pointing at
  `book/figures/<key>.svg`, numbered, captioned, listed in a List of Figures after the Contents, and written as an SVG file
  in `docs/book/figures/` for the pages on GitHub. **Every word lives inside its cell** (the founder's order of 16
  October, night): the type in a figure is 9 pt (his order, the shells kept), every label is measured in its own type and
  wrapped to the width of its box before it is drawn, the kit records any label that would not fit (`schematics.OVERFLOWS`,
  empty on every build), and no figure is ever scaled below its type: a figure taller than a page is split into two,
  "continued". A chart's axis shows what the reader needs to read it: the benefit sheet's axis reads 0, 10, 25, 50 and
  100 % on a square-root scale so a small bar is seen, and a bar past 100 % is drawn to the edge and marked. The Operator's
  Manual carries the wiring, the flowcharts, the timing and the structure (no receipt charts, no engine internals); the
  Owner's carries all. None of the founder's plates (his illustration images) go in: no cover art, no title-page rose, no
  plates, no List of Plates; no chart of a result either. **No dead pages** (the founder's order of 16 October, night: "every
  page be fully populated, 80% at least"): a chapter starts on the next page unless that would leave the page before it
  under 80 % used, and then it opens on the same page under a short space; a figure that does not fit under its paragraph
  floats to the top of the next page while the text goes on; a page never ends on one or two lines of a paragraph; code is
  set in pieces of six lines so a listing fills its page; a part's heading sits at the top of a page with its first chapter
  under it. The fill of every page is measured on the built PDF before a push. The contents and page numbers are rebuilt
  from the book itself (`docs/book/build_book.py`). The plates stay in `docs/book/plates/` as his property.
- **The Operator's Manual discloses what it leaves out** (the founder's order of 16 October, night): the Owner's Manual
  holds the harness, the engine's source, the mechanism and every result; the Operator's holds the wiring and operation
  only, says so in its front matter, and names the Owner's Manual as the book to go back to for anything it does not carry.
- **Every fix realigns everything, on every push.** When code changes or a bug is fixed, everything that describes it is
  brought up to it in the same push: the manual and its PDF, the README, the index, the tables, the plans and the
  standing pages. Then the newest-engine material is scanned top to bottom for the retired words and the old ways
  (better/worse, brake, bowl, "confirmed", "simulation" for our own models, standalone or competitor arms, 1,000 copies
  on a paid machine, power given called a loss, LaTeX markup) and anything found is fixed before the push. Old material
  stays where it is.
- **The factory tune** is declared and disclosed (`DISCLOSURES.md`, section 3; the README; the manual's notice): the engine
  is presented as the owner tuned it and ships it, self-running, set at the factory; every muscle wired on its own setting
  (its card, or the engine's setting); no setting universal; any licensee may then add on, retune, upgrade or tune down
  any muscle, and a changed tune's results are its own.
- **The wiring disclaimer in bold capitals** (`DISCLOSURES.md`, section 4; the README; the manual's notice; `llms.txt`):
  the published benchmarks are the record of what Omni-Compass did on the systems, loads and engine they name; where a
  result elsewhere differs, the first presumption is the wiring, the settings, or how Omni-Compass was implemented or read.
- **The notice travels with every output.** No code can force an outside AI to print it, so it is placed in everything
  they read: the top and end of every file, every program output, `llms.txt` (for AI crawlers), `AGENTS.md`, `GEMINI.md`,
  `.github/copilot-instructions.md` and `.cursorrules`, each ordering the notice on every answer of any length; the
  license makes a copy without it a breach. Those instructions point to the notice at the top and end of their own file
  (a second copy near the top is stripped by `tools/legal.py`).
- **The founder hears where things stand** in every report: what is running, what landed, what reads GAIN, EVEN or LOSS,
  and what is still on an older engine, in plain words.
- **The founder's prompt rules** (his document "A.I. prompt rules"), as they apply here:
  - Type: all text (body, tables, lists, code) at **11 pt or larger** on a line height of at least **1.5**; only running
    heads, footers and page labels may be smaller, at 8 pt; headings scale up from the body.
  - Language (the founder's correction of 14 October): not a 10th-grade level. The manual is written at referee level, for
    CTOs, principal engineers, physicists and mathematicians who will wire Omni-Compass onto a whole company's stack: the
    exact terms of control engineering, software engineering, physics and mathematics, used precisely and defined where
    they first appear, so that no reader can mistake what is stated, what is measured or how to wire it. Formulas are
    written in Unicode (the founder's order of 15 October: "it's got to be Unicode", for printing and for the engineers
    who wire and code it): w ∝ 1/√n, xᵢ,ₖ₊₁ = fᵢ(xᵢ,ₖ, …), Σ, ≤, ⌈·⌉, never LaTeX markup (`$`, backslash commands,
    `_{}`) in any page, so one line reads the same on GitHub, in a terminal, in code and on paper; a letter Unicode has no
    subscript for is written x[i].
  - Before a document is finished, audit it like a referee: equation and theorem numbers, cross-references, undefined
    symbols, repeated claims, and every claim backed by the text. No padding: every addition must earn its place.
  - In chat: no greetings, no echoing the request, no sign-offs; no follow-up questions (decide and do it); do what can be
    done without listing what can't. This never hides a result: every row, LOSS included, is still reported (Honesty).

## Orders of 13 October

- **GAIN, EVEN, LOSS** (the founder's order of 13 October, evening: "better, same and worse are going to be gain, even and
  loss, wherever and ever, all over where it lives, where it used to live"). Every judged reading, in every table, page,
  report, program output and the manual, is GAIN, EVEN or LOSS, decided by what the gauge is for and never by the sign of
  its number: time waited, missed or failed, a fall is GAIN; work done, a rise is GAIN; a resource spent or held, a fall
  is a cut, a GAIN, and a rise is **power given**, never a loss. Better/worse, lower/higher-as-a-verdict and toward/away
  are not used. The key (G.A.I.N. Growth, Advantage, Improvement, Net-positive; E.V.E.N. Equalized, Verified baseline,
  Equilibrium, Neutral; L.O.S.S. Leakage, Off-track, Setback, Subpar), disclosed and disclaimed, is written once in
  `tools/readings.py` and stands at the top of the README, `docs/HOW_TO_READ_THE_RESULTS.md` and the manual's front matter
  (`python3 tools/readings.py --fix`; `--check` fails a page whose key differs). "Theoretically I should never see the word
  loss": a LOSS row is never cut; its cause is found and fixed and the test rerun. `python3 tools/summary.py` prints the whole
  summary straight after a pull. Raw machine records (JSON receipts, raw run folders) keep their recorded field values;
  every page that shows them uses the words. Next: the words become the code that tells Omni how to move (the next engine).
- Every muscle runs from 1 up to one click under its own capacity, read live from the system, never a number written in
  code: never below 1 (a pool's machines never below 2), no ceiling where the system can keep adding, and back down again;
  guardrailed so no muscle overworks and hurts the organism, and the organism never hurts a muscle. Where the brain's own
  math shares the machine, it counts in the body's load. Encoded in the live controllers as Omni v5 amendment 5 (digest
  `6093b2b8`, `docs/OMNI_V5.md`): machines, replicas, the power cap, the GPU's clock floor and heat line, batch.
- Omni's brain works for the organism, never for Omni: it decides what to push and pull so the whole system is the best it
  can be, collectively, one body.
- Never decide a benchmark's settings ourselves: the written ones stand (the Azure burst steps are `1 6 1 8 1 6`, as first
  preregistered; the founder's order of 14 October withdrew our amendment of 5 October that had set `1 3 1 4 1 3`). When a result comes in negative, find the cause and fix it at once, unasked; a test machine's limit is never
  reported as Omni's result.

- **Everything on the newest engine** (13 October, night): every benchmark runs again on the engine that stands, and its
  result carries that engine's name. Nothing is shown or compared as "v3" once v5 stands: a v3 table is the road, in
  `docs/history`, never a setting to go back to by name. More versions will follow (perhaps to v10); each one reruns
  everything. Where a change made a result worse, the fix is made inside the newest engine and rerun.
- **One cloud first** (13 October, night): Kubernetes on Azure is finished first; Google (GKE), Amazon (EKS) and the GPU
  chips (Lambda) are not run until the founder says the Azure Kubernetes results are where he needs them.
- **The company's telephone** (13 October, night; wording of 14 October; the landline added 16 October, night): "main
  office infrastructure, toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1", and under it the landline
  registered in Florida, 321-746-4411 (the toll-free number always on top), on every contact line where the company is
  named for reaching it (README, LICENSE and its copy, NOTICE, Enterprise License, Trademarks, Licensing FAQ, Security,
  Support, the manual's "Who to call", codemeta), always before the website, never inside the legal notice, which ends with
  www.omni-compass.com. The letters, read in order, are the company's own reading of how the engine runs (README "Contact",
  the manual's "Who to call"): DEX, Data Exchange (the input, the two-way plug); YLL, Yield Limit Line (the boundary, every
  muscle to its own limit and never past it, as a material is loaded to its yield limit and springs back unharmed); 1, one
  closed loop (the output; in code 1 is true, in science 1 is unity; one body, one brain). The founder's order of 14
  October: write it as the meaning, the way science and software people read it, wherever it fits in the manual; "years
  of life lost" is written nowhere. The founder's
  personal number is never written anywhere.
- **A copy he can keep**: the manual's PDF and the whole repository as a downloadable zip, in parts, from a pushed commit,
  sent to the founder after each landed change.

## Orders of 10 October (afternoon)

- The reflex rule is the whole mechanism: a trial runs to its full measurement and is never ended by the calm it causes;
  the brain never forces, it reacts to what the system shows; one body, one brain, the body's cost judged, nothing anywhere
  pushed to a LOSS to move one thing to a GAIN; one trial at a time inside a body; nothing permanent; the wall
  belongs to the body.
  Written into the engine as **Omni v4** (`docs/OMNI_V4_PLAN.md`), every wire forced through it, every result rerun.
- Everything is wired. Staying native is the brain's live decision every second, never a verdict from one run.
- **Six organisms**, never five (superseded on 16 October: seven, the spine an organism of its own): the four realms, all realms stacked (1,716), the whole catalog once (945). The live
  software products are never counted beside them. Realms are re-cut by a written rule at v4; new muscles raise the count.
- The word "simulation" is not used for our own models in reports: they are "modelled" (class S); live software is "the
  real thing" (class L); a meter is class P. The license's own phrase stays as written.
- The newest result is always at the front; the repository keeps itself current (the archive bot and the front page);
  old material goes to `docs/history`.
- Both manuals are printed books, front matter, body and back matter (Orders of 14 October: the Operator's Manual for
  the people who wire and run it, the Owner's Manual with everything); rebuilt as PDFs whenever they change.
- The founder hears what a result says before it goes up.

## Repository

- Referee and underwriter level. Only finals up front; old material goes to `docs/history` / `archive/` or is removed.
  One version is always the main one; `main` and the working branch, `v9` (the engine that stands, 17 October), stay in
  sync, and `v8`, `v7` and `v7-candidate` are kept level with them. **The `v5` branch
  is history** (the founder's order of 17 October: "We won long past 5"): it is never merged into `main` and `main` is
  never merged or pushed into it; nothing is read across engines.
- Verify before every push: `tools/release_manifest.py` under Python 3.12 (as GitHub runs it), 0 FAIL. Clear
  `/tmp/tmp*` first, because test leftovers fill the disk. Keep the Python 3.12 environment outside `/tmp` (for example
  `/root/v312`), because a container reset wipes `/tmp`. After a push, check the GitHub verify run itself, not only the
  local one.
- The Operator's Manual (`docs/OMNI_COMPASS_MANUAL.md`, `python3 docs/book/build_book.py`) is the wiring and operating
  manual, with every muscle's wiring and card (Appendix E); the Owner's Manual (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`,
  `build_book.py --owner`) explains the physics, philosophy, mechanism and wiring, how to read every metric, every result,
  and holds the muscle catalog, the register and the engine's source.
- Zips on request: split into parts under the upload limit, each part openable on its own, built from a pushed commit.
- Never put a model identifier in a commit, PR or file.

## Talking to the founder

- The founder is not an engineer. Use plain language: yes/no plus a number. When asked a question, answer it before
  doing any work.
- Say what each step costs and how long it takes. Give Lambda and Azure steps click by click (the founder types on a
  laptop and chats on a phone).
- Credentials go only into GitHub secrets. Never ask for them, never echo them back.
- Latest standing order (Oct 5): push everything on the newest engine, run it again and double-check it, keep the old
  runs going, don't ask questions, and work to the highest referee and underwriter level.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
