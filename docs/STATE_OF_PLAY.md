# Omni-Compass: state of play (read this first)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

<!-- where things stand (tools/summary.py --fix) -->

**Where things stand, read from the result files.** Written by `python3 tools/summary.py --fix` from the files it names; `verify.py` fails a push in which this block no longer matches them. Nothing in it is typed by hand. The live results run on the engines named in their own tables, and every one of them runs again on the newest engine.

- **The engine on this checkout:** omni-v7, fingerprint d6d467b824c585f1 (46 files).
- The muscles and the seven organisms on engine omni-v7 at the max (evidence class S, our own models; run 2026-10-16 04:34 UTC, commit 1637d32cd26c, 1107 muscles; source: results/realms_v5/REALMS_V5.md):
  - every muscle alone, over its loads: EVEN 580, GAIN 527
  - the organisms under the normal load: the spine: GAIN (fewer misses), misses -0.145 pp, power given +0.011%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.070 pp, power given +0.009%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.121 pp, power given +0.010%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.118 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.067 pp, power given +0.002%; the four stacked: GAIN (fewer misses), misses -0.092 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
  - the organisms under the climb load: the spine: GAIN (more work + fewer misses), misses -0.632 pp, power given +0.039%; Compute / AI / Cloud: GAIN (more work + fewer misses), misses -0.390 pp, power given +0.046%; Physics / Robotics / Autonomous: GAIN (more work + fewer misses), misses -0.317 pp, power given +0.021%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.217 pp, power given +0.000%; Distribution / Specialized: GAIN (more work + fewer misses), misses -0.460 pp, power given +0.026%; the four stacked: GAIN (more work + fewer misses), misses -0.349 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.094 pp, power given +0.000%
  - the organisms under the line load: the spine: GAIN (fewer misses), misses -0.371 pp, power given +0.038%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.205 pp, power given +0.045%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.250 pp, power given +0.030%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.117 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.142 pp, power given +0.006%; the four stacked: GAIN (fewer misses), misses -0.176 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
- The grid (source: results/grid_v5/GRID.md): Across the grid: modelled, 36 of 36 squares of 10 and 100 runs GAIN (fewer misses); the 18 single runs: 18 with fewer misses; work +0.000%; power given +0.000% to +0.065%; with the cluster inside, 54 squares: 18 single repetitions (no reading); of the 36 of 10 and 100 repetitions, by gauge: "organism time over the line (% of steps)" GAIN in 36, LOSS in 0, "time over the response line (% of samples)" GAIN in 36, LOSS in 0, "response time (ms), 95th percentile" GAIN in 26, LOSS in 2, "energy (Wh)" GAIN in 26, power given in 0, "energy, parked workers still on at idle power (Wh)" GAIN in 26, power given in 0, "organism energy (J)" GAIN in 0, power given in 22, "organism work per energy" GAIN in 0, LOSS in 22, "failed requests (%)" GAIN in 18, LOSS in 0, "response time (ms), 99th percentile" GAIN in 12, LOSS in 2, "HPA replicas, mean" GAIN in 4, power given in 5, "pods started" GAIN in 3, power given in 0; off the clock in 3; invalid in 0.
- The Omni index (evidence class L, real machines, every measure the same in all three of our runs; the three-run tables of omni-v3, each named in its table): +5.2% GAIN on the resource reading (work, speed, machines, energy), +12.5% GAIN on the service reading (work and speed alone). Source: results/OMNI_INDEX.md.
  - Real Kubernetes (GitHub): +31.8% GAIN
  - Real database cache (MongoDB under YCSB, GitHub): +1.7% GAIN
  - Real database (PostgreSQL behind PgBouncer, GitHub): +0.9% GAIN
  - Real messaging (Apache Kafka, GitHub): +0.1% GAIN
  - Real cache (Redis, GitHub): +0.0% EVEN
  - Real database buffer pool (MySQL under sysbench, GitHub): +0.0% EVEN

**On the engine that stands (omni-v7): 4 of 26 benchmarks so far.** Every other row is that engine's own result, named in its Engine column, and runs again on the engine that stands (`scripts/reruns.txt`); results are never read across engines.

| Benchmark | Engine | Its one number | Its word | Class |
|---|---|---:|---|---|
| Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs | omni-v7 | +18.0% | GAIN, power given | L |
| Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs | omni-v7 | +0.0% | EVEN | L |
| Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v7 | +78.3% | GAIN, power given | L |
| Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v7 | +44.8% | GAIN, power given | L |
| Every real test together: the Omni index | omni-v3 | +5.2% | GAIN, power given | L |
| The six organisms with the real cluster inside, 10 and 100 copies | omni-v3 | +5.3% | GAIN, power given | L, the cluster; S, the organism around it |
| The big organisms with the real cluster inside, 1,000 copies on Azure | omni-v3 | +155.0% | GAIN | L, the cluster; S, the organism around it |
| The 945 modelled muscles as one tower, every muscle written at once | omni-v3 | +0.3% | GAIN | S |
| Robustness: the two-hour run | omni-v3 | +0.0% | EVEN | L |
| Robustness: the governor killed outright mid-run | omni-v3 | +8.6% | GAIN | L |
| Robot arms (MuJoCo), the three untouched robots | omni-v3 | +3.8% | GAIN | S |
| Redis, the cache's memory ceiling | omni-v3 | +0.0% | EVEN | L |
| Real Kubernetes, steady work | omni-v3 | +30.5% | GAIN | L |
| Real Kubernetes, faults | omni-v3 | +36.6% | GAIN | L |
| Real Kubernetes, demand that wanders | omni-v3 | +37.0% | GAIN | L |
| Real Kubernetes, all four at once | omni-v3 | +41.7% | GAIN | L |
| Real Kubernetes, a queue of jobs | omni-v3 | +16.5% | GAIN | L |
| Real Kubernetes, a public day of demand (Google 2011) | omni-v3 | +46.4% | GAIN | L |
| Real Kubernetes, a noisy neighbour | omni-v3 | +0.0% | EVEN | L |
| Power grids (SimBench), both load models | omni-v3 | +5.8% | GAIN, power given | S |
| PostgreSQL, the pooler's pool size | omni-v3 | +0.9% | GAIN, power given | L |
| MySQL, the buffer pool's size | omni-v3 | +0.0% | EVEN | L |
| MongoDB, the storage engine's cache size | omni-v3 | +1.7% | GAIN | L |
| Kafka, the consumer group's size | omni-v3 | +0.1% | GAIN | L |
| Drone swarms, the three untouched cells | omni-v3 | +5.9% | GAIN | S |
| Buildings and batteries (CityLearn), the districts with batteries | omni-v3 | +0.8% | GAIN AND LOSS | S |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- end of where things stand -->

**The afternoon of 10 October: Omni v4 ordered, the sweep closed, two faults found, the second set landed.** The founder ordered
the collective mechanism as the next engine (`docs/OMNI_V4_PLAN.md`: one body, one brain, one tick a second; a trial runs to its
full measurement and is never ended by the calm it causes; the body's cost judged, nothing anywhere pushed to a LOSS to move one thing
toward its own; one trial at a time inside a body; nothing permanent; the wall belonging to the body; every wire forced through it; the
six organisms, the four realms, all realms stacked and the whole catalog, re-cut by a written rule). The final coverage sweep
against the internet added register rows 74 to 78 and five catalog families for v4, and mapped the mega-caps' closed systems to
the open analogs that carry the same muscles (`docs/COVERAGE_MAP.md`). Two faults GitHub's own runs showed and no local check had
were fixed: the release manifest, not refreshed after the morning's last document edits, and the cpu-power workflow file, refused
by GitHub since its first push for an unquoted colon; the verifier now parses every workflow file. The five live products' second
set on the amended trial rule landed (21 runs) and is archived; its early reading, from the logs, is in `docs/RERUN_2026-10-10.md`
and the manual's 16.6c: on Kafka the brain allowed the third consumer once and the whole gain returned at 2.5 consumers instead of
6 to 8, and refused on every other repetition; the trial's measurement, not the law, is the fault, and four trial rules for v4
follow from it. The legal wording on every page outside the frozen engine now reads "all rights reserved" and "all patents,
copyrights and trademarks filed in the USA", followed by www.omni-compass.com and nothing after it. The repository now
keeps itself current: after every finished live run the front-page workflow archives it and `tools/front_page.py` rebuilds every
table whose three runs are in, the pages read from the tables, and the README's latest lines (`results/live/FRONT_PAGE_STATE.json`
records what each table was built from).

**Everything run again (10 October 2026, 01:24 to 01:31 UTC).** At the founder's order that every result be as of today, every
benchmark with a result was dispatched again on the current commit `3aac0ab7` (Omni v3, digest `b53d05449ee04c4b`, by
`tools/omni_version.py --commit`), native and omni, the wiring of each checked against its preregistration before the dispatch:
70 GitHub runs (the seven Kubernetes tests, the five live stacks on the brain's own verdict, the four simulators, the realms table
and the kill and long robustness scenarios, three runs each; the organisms with the real cluster inside; the modelled grid at
1, 10, 100 and 1,000 copies) and the two big organisms at 1,000 copies on rented Azure machines, plus one replacement run for a Kafka
job GitHub's runner cut off (the record says which and why). By 12:30 UTC 69 of the 71 had landed and every
table on this page was remade from them; the tables they supersede are whole in `docs/history`. The one shard the runner's
six-hour limit cut off (the tower at 1,000 copies in the modelled grid) runs again, and that row reads the earlier run until it lands. The record, run by run
with inputs, times and ids, is `docs/RERUN_2026-10-10.md`. Not restarted, and why: the three 24-hour robustness machines (started
8 October on the same harness, byte for byte, ending about 10:15 UTC today) and the Azure fleet that can show one machine, which
waits on the family allowance those machines hold.


## In one paragraph (2026-10-16, the engine that stands is omni-v7)

**The engine that stands is omni-v7** (`OMNI_V7.json`, digest `d6d467b824c585f1`, 46 files; `docs/OMNI_V7.md`), on main since
16 October by the founder's order: the v5 law at the max on the 1,107-muscle catalog with every muscle's own card, the shared-host
capacity repair in the Kubernetes controller, conveyance bounded by each namespace's CPU quota (an unreadable quota is no budget
known, Kubernetes admission is the authority), the verdict reading a trial in the reports' words, every rule in seconds, the
cloud's rule as one flag. Its first trials as pushed on 15 October found a fault in its quota budget (an unreadable ResourceQuota
read as a zero allowance, so conveyance never raised a limit), fixed on 16 October in the toy gate first and then in the engine;
the corrected trials are its first runs (below). Every benchmark runs again on the engine that stands (`scripts/reruns.txt`,
released a few a tick by the grid conductor, A of every benchmark, then B, then C; the grid and every Azure set restarted on it
the same day); every row stands as its own engine's result (omni-v6 for the four Kubernetes add-on tables of 15 October, omni-v3
for the rest, named in its Engine column on `docs/BENEFIT_SHEET.md` and in the standing block above) until its three runs on v7
land. Results are never read across engines. The standing block at the top of this page is written from the result files by
`tools/summary.py --fix` and checked on every push; the prose below says the same in words.

**On omni-v7, the engine that stands, real Kubernetes (evidence class L), ten pairs × three runs each**
(`results/live/V7_*.md`, runs 38843260818 to 38843289946, every one omni-v7; no row reads LOSS on the three-run rule):

- **A service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top** (`V7_GOLDILOCKS.md`): response time
  **−45% to −47% mean, −60% to −62% at the 95th percentile, −67% to −69% at the 99th**, time over the response line −100%,
  GAIN in all three of our runs; machines (node-hours) and failed requests EVEN; replicas, pods started, pod start wait and
  alert minutes EVEN (each clear of the noise in one run only, and there on the GAIN side except replicas +3.4%, power given);
  parked-worker energy +1.6% to +2.3%, power given; 14 to 18 settings commands a run. One number: **+18% GAIN, power given**.
- **KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top** (`V7_KEDA_REQUESTS.md`): response time **−57% to
  −58% mean, −71% to −75% at the 95th percentile**, time over the line −94% to −95%, alert minutes **−93% to −96%**, HPA
  replicas **−15% to −19%**, pods started **−17% to −23%**, all GAIN in all three of our runs; machines and failed requests
  EVEN; parked-worker energy +2.2% to +2.3%, power given; 4 to 5 settings commands a run. One number: **+78% GAIN, power given**.
- **KEDA on the CPU target and the live requests in flight, Omni-Compass on top** (`V7_KEDA_CPU_REQUESTS.md`): response time
  **−36% to −38% mean, −52% to −54% at the 95th percentile, −57% to −59% at the 99th**, time over the line −98% to −100%,
  GAIN in all three of our runs; machines, failed requests, replicas and alert minutes EVEN; parked-worker energy +1.1% to
  +1.7%, power given; 17 to 20 settings commands a run. One number: **+45% GAIN, power given**.
- **A service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top** (`V7_CRUISEKUBE.md`): every
  gauge EVEN; CruiseKube's own rightsizing leaves Omni-Compass nothing to move and it wrote no setting. Run A alone read the
  99th percentile +3.1% and run B the node-hours +1.0%, each inside the noise in the other two runs. One number: **0%, EVEN**.
- **Fixed capacity, four CPU caps, Omni-Compass on top at native's cap** (`V7_CAPACITY.md`): completed work and work inside the
  response line EVEN at every cap (run A alone read +3.8% completed work at 1 core, inside the noise in B and C): the cap is a
  quota on the service's CPU and blocks the one lever Omni-Compass has there.

**On omni-v6, the engine of 15 October, real Kubernetes (evidence class L), ten pairs × three runs each** (`results/live/V6_*.md`;
that engine's own record, run again on v7 above):

- **A service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top** (`V6_GOLDILOCKS.md`): response
  time **-45% to -47% mean, -58% to -61% at the 95th percentile, -65% to -69% at the 99th**, time over the response line
  -99% to -100%, GAIN in all three of our runs; machines, node-hours, failed requests and the alert minutes EVEN; the
  parked-worker energy +1.8% to +2.7%, power given; HPA replicas EVEN. One number: **+54% GAIN, power given**.
- **KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top** (`V6_KEDA_REQUESTS.md`): response time
  **-59% mean, -73% to -75% at the 95th percentile**, time over the line -97% to -99%, alert minutes -98% to -100%, HPA
  replicas **-11% to -18%**, all GAIN in all three of our runs; parked-worker energy +1.6% to +2.1%, power given. One
  number: **+105% GAIN, power given**.
- **KEDA on the CPU target and the live requests in flight, Omni-Compass on top** (`V6_KEDA_CPU_REQUESTS.md`): response
  time **-37% to -41% mean, -55% to -57% at the 95th percentile, -59% to -63% at the 99th**, GAIN in all three of our
  runs; machines, failed requests, alert minutes and replicas EVEN; parked-worker energy +1.2% to +1.6%, power given. One
  number: **+15% GAIN, power given**.
- **A service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top** (`V6_CRUISEKUBE.md`):
  every gauge EVEN, no difference beyond the noise: CruiseKube's own rightsizing leaves Omni-Compass nothing to move on
  this service. One number: **0%, EVEN**.

In every one of these the governor ran on autopilot: no person touched a setting in either arm; the settings commands it
wrote on its own (15 to 17 a run on Goldilocks and on KEDA with the CPU target, 4 to 5 on KEDA's HTTP add-on) are in each
run's audit with their reasons, and the alert minutes (a whole minute over the line, when an on-call page would be open)
are judged in every table.

**Still on omni-v3, each named as that engine's result and queued to run again on v6** (`docs/BENEFIT_SHEET.md`): the
seven real-Kubernetes demands (steady +31%, faults +37%, wandering +37%, all four at once +42%, a queue of jobs +16%, the
Google day of 2011 +46%, all GAIN; a noisy neighbour EVEN), the five live stacks (PostgreSQL +0.9% GAIN with power given,
MongoDB +1.7% GAIN, Kafka +0.1% GAIN, MySQL EVEN, Redis EVEN), robustness (the governor killed mid-run +8.6% GAIN; the
two-hour run EVEN), the six organisms with the real cluster inside at 10 and 100 copies (+5.3% GAIN, power given), the
big organisms at 1,000 copies on Azure (+155% GAIN), the modelled tower of that engine's 945 muscles (+0.3% GAIN), the robot
arms (+3.8% GAIN), the power grids (+5.8% GAIN, power given), the drone swarms (+5.9% GAIN) and the buildings with batteries
(+0.8%, GAIN AND LOSS: the bill in the 2023 districts read power given), and the Omni index over the real tests (+5.2% GAIN,
power given). None of these is shown in front of a v6 result, and none is read beside one.

**The muscles and the seven organisms, modelled (evidence class S, our own models, never counted in the headline)**, on
the engine that stands, omni-v7, at the max (run again on 16 October, commit `1637d32cd26c`, with the spine as the seventh
organism; every reading reproduces the 13 October table to the digit): 1,107 muscles in 70 families (`realms/catalog_v5.csv`),
every muscle its own card (`realms/muscle_cards_v5.csv`), every muscle alone over its loads EVEN 580 and GAIN 527, LOSS 0; every
one of the seven organisms (the spine 267, the muscles every stack runs on; Compute / AI / Cloud 540, Physics / Robotics /
Autonomous 404, Energy / Facility / Industrial 480, Distribution / Specialized 484, the four stacked 1,908, the whole tower
1,107) GAIN (fewer misses, and under the climb more work) under the normal, climb and line loads, not one plant with less work
or more misses in any of them, the power given +0.00% to +0.05%; the spine alone cuts its misses 6.1% under its own load, 7.9%
under the climb (with more work) and 8.8% with work waiting in line, power given +0.01% to +0.04%
(`results/realms_v5/REALMS_V5.md`, `docs/THE_SPINE.md`); the grid, 36 of 36 squares of 10 and 100 runs GAIN with the six
organisms run so far alone and, with the real cluster inside, the organism's time over the line GAIN in 36 of 36; the spine's
squares are in the conductor's queue (`results/grid_v5/GRID.md`). Every
muscle is written out, organism by organism, the spine first, in `docs/REALM_MUSCLES.md`, and explained, wired and carded in
`docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix, with every family's wiring on a real stack from
`docs/wiring_recipes.csv`).

**The cloud (Azure), the bill at native's work.** The founder's order of 14 October: in a cloud Omni-Compass shows one
thing, the same work as native for a smaller bill, at the tune-down on the machines alone. The sets ran at the tune-down on
14 October (steady, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9; `aks-metered`, every run's title
carrying `dial save`), and a full-wiring burst (`aks-metered-full`, the pod autoscaler moved too) ran on 15 October; their
receipts are archived by this push and their tables follow, each on the engine it ran on. The only Azure tables up so far
are v1's 4-worker fleet (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): every gauge EVEN, a fleet too small to show
one machine. Google (GKE) and Amazon (EKS) are built (`gke-metered`, `eks-metered`; the Operator's Manual's appendices G
and H, click by click) and run only when the founder opens the accounts and says so.

**The card (evidence class P)**: every earlier card result is obsolete; the founder's runs on rented cards come after the
CPU and cloud work, at one named commit. **Linux's own CPU governor and meter** (`cpu-power`): built and preregistered; it
waits for a machine on the metal, because GitHub's machines are virtual and expose neither.

**What is shown and what is not.** Shown, on the engine that stands and on real Kubernetes: a faster tail and more work
inside the response line on the same machines, on top of the operator's own rightsizers and autoscalers (Goldilocks, KEDA),
three times each. Shown on the older engine and queued to run again: the same on seven demands, memory and connections
given back on real databases and a broker at no measured cost, the governor's hand-back when killed. Not yet shown: an
energy or cloud-bill saving on real machines (energy on kind is a declared model; the Azure tables at the tune-down are
being made), and anything on a real card.

## Open

1. **Every benchmark on omni-v7**: 4 of 26 benchmarks have their three-run table on it (Goldilocks, KEDA's two add-on tests,
   CruiseKube; the fixed-capacity test too, which carries no sheet row); the rest released A, then B, then C by the conductor
   from `scripts/reruns.txt`; each table replaces its older row on the sheet when its three runs land.
2. **The grid and Azure on omni-v7**: restarted on 16 October; the v6 shards still running and the queued Azure set finish and
   stand as that engine's record, nothing cancelled.
3. **Azure at the tune-down**: the receipts of 14 and 15 October into tables (archive requested), checked against the
   cloud toy's finding that the machines-only setting barely cuts the bill while pods wait for a place.
4. **Google and Amazon**: on the founder's word; the accounts and secrets are his to make (appendices G and H).
5. **The card**: the founder's runs on Lambda, one exact commit, after the CPU and cloud work.
6. **Linux**: a machine on the metal for `cpu-power`.
7. **More room**: 453 of the 2,214 muscle-load cases read SAME AS NATIVE and 14 of 26 knob-cases on the real stacks read
   watch; the next engine looks for a gain in each, in the toy gate first.
8. **Omni-Compass 1.0**: when the founder declares the engine final, the engine that stands then is published as 1.0 and
   the older fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the Operator's Manual: how to embed, wire, tune, run and check Omni-Compass; every muscle's wiring and card (Appendix E) |
| `docs/OMNI_COMPASS_OWNERS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`) | the Owner's Manual: the theory, the mechanism, the engine's source, every result, every muscle (Appendix G) |
| `docs/BENEFIT_SHEET.md` | one number per benchmark, its word, its engine, every change in words |
| `docs/REGISTER.md` | every muscle family wired, every benchmark run, every benchmark still to run |
| `docs/WIRING_VERDICTS.md` | write, watch or the operator's choice, per knob, from every result |
| `docs/OMNI_V6.md`, `docs/OMNI_V5.md`, `docs/OMNI_V3.md`, `docs/OMNI_V2.md`, `docs/OMNI_V1.md` | what each engine is and every result read on it; v7's page is on its branch |
| `docs/history/STATE_OF_PLAY_2026-10-10.md` | this page as it stood on 10 October, on Omni v3, moved here whole |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
