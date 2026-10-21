# Omni-Compass: state of play (read this first)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

<!-- where things stand (tools/summary.py --fix) -->

**Where things stand, read from the result files.** Written by `python3 tools/summary.py --fix` from the files it names; `verify.py` fails a push in which this block no longer matches them. Nothing in it is typed by hand. The live results run on the engines named in their own tables, and every one of them runs again on the newest engine.

- **The engine on this checkout:** omni-v13, fingerprint 0088837333c6f0fc (47 files).
- The muscles and the seven organisms on engine omni-v8 at the max (evidence class S, our own models; run 2026-10-17 15:39 UTC, commit 9819a903cba3, 1107 muscles; source: results/realms_v5/REALMS_V5.md):
  - every muscle alone, over its loads: EVEN 580, GAIN 527
  - the organisms under the normal load: the spine: GAIN (fewer misses), misses -0.145 pp, power given +0.011%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.070 pp, power given +0.009%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.121 pp, power given +0.010%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.118 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.067 pp, power given +0.002%; the four stacked: GAIN (fewer misses), misses -0.092 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
  - the organisms under the climb load: the spine: GAIN (more work + fewer misses), misses -0.632 pp, power given +0.039%; Compute / AI / Cloud: GAIN (more work + fewer misses), misses -0.390 pp, power given +0.046%; Physics / Robotics / Autonomous: GAIN (more work + fewer misses), misses -0.317 pp, power given +0.021%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.217 pp, power given +0.000%; Distribution / Specialized: GAIN (more work + fewer misses), misses -0.460 pp, power given +0.026%; the four stacked: GAIN (more work + fewer misses), misses -0.349 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.094 pp, power given +0.000%
  - the organisms under the line load: the spine: GAIN (fewer misses), misses -0.371 pp, power given +0.038%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.205 pp, power given +0.045%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.250 pp, power given +0.030%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.117 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.142 pp, power given +0.006%; the four stacked: GAIN (fewer misses), misses -0.176 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
- The grid (source: results/grid_v5/GRID.md): Across the grid: modelled, 36 of 36 squares of 10 and 100 runs GAIN (fewer misses); the 18 single runs: 18 with fewer misses; work +0.000%; power given +0.000% to +0.065%; with the cluster inside, 54 squares: 18 single repetitions (no reading); of the 36 of 10 and 100 repetitions, by gauge: "organism time over the line (% of steps)" GAIN in 36, LOSS in 0, "time over the response line (% of samples)" GAIN in 36, LOSS in 0, "response time (ms), 95th percentile" GAIN in 26, LOSS in 2, "energy (Wh)" GAIN in 26, power given in 0, "energy, parked workers still on at idle power (Wh)" GAIN in 26, power given in 0, "organism energy (J)" GAIN in 0, power given in 22, "organism work per energy" GAIN in 0, power given in 22, "failed requests (%)" GAIN in 18, LOSS in 0, "response time (ms), 99th percentile" GAIN in 12, LOSS in 2, "HPA replicas, mean" GAIN in 4, power given in 5, "pods started" GAIN in 3, power given in 0; off the clock in 3; invalid in 0.
- The Omni index (evidence class L, real machines, every measure the same in all three of our runs; the three-run tables of omni-v10 and omni-v11 and omni-v12, each named in its table): +4.3% GAIN on the resource reading (work, speed, machines, energy), +11.9% GAIN on the service reading (work and speed alone). Source: results/OMNI_INDEX.md.
  - Real Kubernetes (GitHub): +28.6% GAIN
  - Real cache (Redis, GitHub): +0.1% GAIN
  - Real messaging (Apache Kafka, GitHub): +0.1% GAIN
  - Real database cache (MongoDB under YCSB, GitHub): +0.1% GAIN
  - Real database (PostgreSQL behind PgBouncer, GitHub): +0.0% EVEN
  - Real database buffer pool (MySQL under sysbench, GitHub): +0.0% EVEN

**On the engine that stands (omni-v13): 0 of 26 benchmarks so far.** Every other row is that engine's own result, named in its Engine column, and runs again on the engine that stands (`scripts/reruns.txt`); results are never read across engines.

| Benchmark | Engine | Its one number | Its word | Class |
|---|---|---:|---|---|
| Every real test together: the Omni index | omni-v10 and omni-v11 and omni-v12 | +4.3% | GAIN, power given | L |
| Redis, the cache's memory ceiling | omni-v12 | +0.1% | GAIN, power given | L |
| PostgreSQL, the pooler's pool size | omni-v12 | +0.0% | EVEN | L |
| MySQL, the buffer pool's size | omni-v12 | +0.0% | EVEN | L |
| Kafka, the consumer group's size | omni-v12 | +0.1% | GAIN | L |
| The six organisms with the real cluster inside, 10 and 100 copies | omni-v3 | +5.3% | GAIN, power given | L, the cluster; S, the organism around it |
| The big organisms with the real cluster inside, 1,000 copies on Azure | omni-v3 | +155.0% | GAIN | L, the cluster; S, the organism around it |
| The 945 modelled muscles as one tower, every muscle written at once | omni-v3 | +0.3% | GAIN | S |
| Robustness: the two-hour run | omni-v11 | +3.8% | GAIN, power given | L |
| Robustness: the governor killed outright mid-run | omni-v11 | +10.7% | GAIN, power given | L |
| Robot arms (MuJoCo), the three untouched robots | omni-v11 | +3.8% | GAIN | S |
| Real Kubernetes, steady work | omni-v10 | +29.8% | GAIN | L |
| Real Kubernetes, faults | omni-v10 | +33.6% | GAIN, power given | L |
| Real Kubernetes, demand that wanders | omni-v10 | +36.7% | GAIN | L |
| Real Kubernetes, all four at once | omni-v10 | +39.7% | GAIN | L |
| Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs | omni-v11 | +72.9% | GAIN, power given | L |
| Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs | omni-v10 | +0.0% | EVEN | L |
| Real Kubernetes, a queue of jobs | omni-v10 | +10.2% | GAIN | L |
| Real Kubernetes, a public day of demand (Google 2011) | omni-v10 | +35.4% | GAIN, power given | L |
| Real Kubernetes, a noisy neighbour | omni-v10 | +0.0% | GAIN | L |
| Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v11 | +59.7% | GAIN, power given | L |
| Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v11 | +41.0% | GAIN, power given | L |
| Power grids (SimBench), both load models | omni-v11 | +5.8% | GAIN, power given | S |
| MongoDB, the storage engine's cache size | omni-v11 | +0.1% | GAIN | L |
| Drone swarms, the three untouched cells | omni-v11 | +5.9% | GAIN | S |
| Buildings and batteries (CityLearn), the districts with batteries | omni-v11 | +1.5% | GAIN, power given | S |

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


## In one paragraph (2026-10-20, the engine that stands is omni-v13)

**The engine that stands is omni-v13** (`OMNI_V13.json`, digest `0088837333c6f0fc`, 47 files; `docs/OMNI_V13.md`), on main since
20 October by the founder's order that every fix land as the next version. It is omni-v12 with one fault fixed in the Kubernetes
governor's conveyance, found on KubeRay's rig with the organism alone (the queue 0.6% to 0.8% later and the web's 99th
percentile 4% to 13% higher, LOSS in all three runs): the web pods' CPU limits, raised in the queue's first half minute, stayed
through the saturated queue, so the batch pods hashed 7.6% slower while the web served no faster; no machine was parked during a
saturated queue (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 11). On a shared host at its top beside another workload's room
every limit given now goes back to the operator's, and every other pod is counted by its own limit. In the toy gate
(`results/toy_gate/V13_VS_V12.md`) omni-v13 reads no LOSS against omni-v12 in any toy, identical on the web-only toys, and in a
batch toy set from the KubeRay runs' own files brings the queue and the job turnaround back to native's. **omni-v12**
(`docs/OMNI_V12.md`), on main from 19 October, was omni-v11 with two faults fixed, both found on the
omni-v11 runs: a CPU-limit raise the cluster's admission refuses is held instead of being written again at every fast check (in
the omni-v11 capacity test the governor asked again about 9 times a minute, 970 to 1,000 refused writes an hour, though nothing
wrong was ever set), and the swarm's proximity reflex hands back the planner's cruise in the tick it is triggered (the omni-v11
reflex slowed over a second, and on a mission draw outside the counted cells two drones collided). In the toy gate
(`results/toy_gate/V12_VS_V11.md`) omni-v12 reads identical to omni-v11 on every gauge of every toy but the one whose every raise
is refused, where it writes 97.5% fewer commands, GAIN. **omni-v11** (`docs/OMNI_V11.md`) is omni-v10 with one guard in the
Kubernetes governor: a reading with no machine in service is blind, so the governor holds, says why, decides nothing from it and
writes nothing (found in the omni-v10 CruiseKube test, where every kind worker left service for two minutes; the toy gate in
`results/toy_gate/V11_VS_V10.md`). **omni-v10** (`docs/OMNI_V10.md`) is omni-v9 with the CityLearn battery wire's glide at 0.0875 of its range an hour (omni-v9:
0.0625), the speed that cuts the bill most with no LOSS: omni-v9 had stopped at the fastest glide where no score rose, and by the
one key (the founder's correction of 17 October) a rise in the ramping or in the distance from net zero is power held, power
given, never a LOSS. Read on CityLearn before it was pushed, it cuts the bill 8.4% to 20.1% in every district with a price, a
further 1.1 to 2.4 points beyond omni-v9, and reads no LOSS against native in any district read before the push; the electricity bought, the carbon and
the peaks fall a little less than on omni-v9, every one still GAIN, and two rows of the 2022 phase 3 are power given (the ramping
+6.18%, the net-zero shortfall +0.25%). A change that would have steered the outage buildings' batteries outside the outage hours
was refused: energy not served +0.69% in one 2023 district, a LOSS (`docs/OMNI_V10.md`, section 3). **omni-v9** (`docs/OMNI_V9.md`)
made the wire read the coming hour (the mean of the same hour over the past seven days, only hours already seen) and made every
95% interval exact (Student t): the reading of the hour gone had run about five hours behind the day (on omni-v8 the 2022
robustness district's monthly unevenness rose 0.11%: power held, power given by the key). **omni-v8** (`docs/OMNI_V8.md`) was omni-v7 with one wire changed, the CityLearn runner: a battery whose building simulates
power outages stays native, because its charge is also the building's reserve. omni-v7's CityLearn table read LOSS in all three
of our runs in the seven 2023 districts, the only districts CityLearn ships with outages; the cause was ours, found on CityLearn
itself and reproduced to the last digit, and three narrower repairs were refused on the tuning district before this one. Read
locally before any GitHub run, omni-v8 gives native's numbers on the 2023 districts and omni-v7's on every other district. The
other 45 engine files were omni-v7's bytes. Every benchmark runs again on omni-v13 (`scripts/reruns.txt`, released a few a tick by
the grid conductor, A of every benchmark, then B, then C; the grid and every Azure set restarted on it the same day); until a
benchmark's three runs land, its row names the engine it ran on (`docs/BENEFIT_SHEET.md` and the standing block above). Results
are never read across engines. The standing block is written from the result files by `tools/summary.py --fix` and checked on
every push; the prose below says the same in words.

**On omni-v11: twenty-three three-run tables, each benchmark's newest until omni-v13's land** (`results/live/V11_*.md`, 19
October; 1,039 judged rows, **0 LOSS**), each rebuilt byte for byte from its raw receipts (`tools/reproduce.py`):

- **Real Kubernetes (evidence class L), ten pairs a run.** On top of Goldilocks: response time −47% to −48% mean, −61% to −64%
  at the 95th percentile, alert minutes −100%, pods started −53% to −61%, GAIN. On top of KEDA's HTTP add-on: −57% mean, −72% to
  −74% at the 95th percentile, alert minutes −100%, replicas −11% to −20%, GAIN; the pod start wait, omni-v10's one LOSS, reads
  EVEN with the served image pre-pulled. On top of KEDA on the CPU target and the requests: −36% to −38% mean, −52% to −53% at the
  95th percentile, GAIN; replicas +2% to +3%, power given. Fixed capacity: EVEN at every cap. Parked-worker energy +1.1% to +2.3%,
  power given. In all 90 paired repetitions Omni-Compass's 95th and 99th percentiles were below native's
  (`docs/TAIL_LATENCY.md`).
- **The live stacks (L), three pairs a run.** Redis: work inside the 2 ms line and hit rate +1.3% to +1.6%, mean latency −1.7%
  to −7.3%, GAIN; memory +1.7% to +1.9% on `small`, power given; native as shipped EVEN. Kafka: consumers −0.8% on `burst`, GAIN
  under both objectives. MongoDB: the cache −0.9% to −1.0% on `f`, GAIN; at the max −0.4% to −0.8% on `b` and `f`, GAIN.
  PostgreSQL: the most connections open +8% to +10%, power given; at the max the connections held −10% to −22%, GAIN. MySQL:
  EVEN but its update throughput, where the runs disagree; from the factory pool the pool +5% to +16%, power given; at the max
  EVEN on every row.
- **Robustness (L), on the kind rig with the served image pre-pulled.** The governor killed outright: every setting back 8 to
  11 s after the kill in 30 of 30 repetitions, a second governor to the end in every one. The long run: no leak, no failed
  decision, no slowing, everything handed back. No LOSS in either.
- **The independent simulators (S, published models, never in the headline).** Power grids: 67 gauge-rows GAIN, 14 power given,
  no LOSS. Robot arms: on the Kinova Gen3 peak torque −28.6% and tracking error −21.3%, GAIN; two arms left native. CityLearn:
  27 score-rows GAIN, 1 power given, no LOSS; the outage districts' batteries native. Drone swarms: energy a mission −7% to −20%,
  missions a charge +8% to +25%, GAIN, no near miss in the counted cells; **a fault found beyond them**: the wire spent the
  closest-approach margin (to about 0.16 m, shown) and, on a mission draw outside the preregistered seeds, let drones collide
  where native did not, because its proximity reflex slowed over a second instead of at once. The fix held every drone outside
  the keep-out on every draw tried (`results/toy_gate/V12_SWARM_REFLEX.md`) and landed in omni-v12, whose swarm runs judge a
  collision as a LOSS and fly three mission draws never flown (`docs/SWARM_PREREGISTRATION.md`, amendment 2).

**On omni-v10, until their omni-v11 runs land** (`results/live/V10_*.md`, 18 October, ten pairs a run): steady work in steps,
the 95th percentile −64% to −65%; demand that wanders, −57% to −66%; all four in one run, work inside the line **+47% to +79%**
and the 95th percentile −56% to −61%; faults, −54% to −63%, replicas +14% to +20% power given; a queue of jobs, machines and
node-hours **−6% to −14%**, the queue finished EVEN; a noisy neighbour, its own rows EVEN and the governed service's time over
the line −11%; the Google day of 2011, −56% to −62%, pods started +120% to +193% power given; CruiseKube, EVEN; the two-hour run,
no leak, every decision valid, every setting handed back, the mean response −33% to −35%. All GAIN in all three of our runs
where written so; no LOSS but the pod start wait, since read EVEN on omni-v11.

**The one number.** The Omni index over the real tests, each test on its newest table with a reading (4 on omni-v12, 3 on
omni-v11, 7 on omni-v10): **+4.3% GAIN** on the resource reading (work, speed, machines, energy) and **+11.9% GAIN** on the service reading
(`results/OMNI_INDEX.md`).

**The muscles and the seven organisms, modelled (evidence class S, our own models, never counted in the headline)**: 1,107
muscles in 70 families (`realms/catalog_v5.csv`), every muscle its own card (`realms/muscle_cards_v5.csv`), every muscle alone
over its loads EVEN 580 and GAIN 527, LOSS 0; every one of the seven organisms (the spine 267, the muscles every stack runs on;
Compute / AI / Cloud 540, Physics / Robotics / Autonomous 404, Energy / Facility / Industrial 480, Distribution / Specialized
484, the four stacked 1,908, the whole tower 1,107) GAIN (fewer misses, and under the climb more work) under the normal, climb
and line loads, the power given +0.00% to +0.05% (`results/realms_v5/REALMS_V5.md`, the engine it ran on named in its header;
`docs/THE_SPINE.md`); the grid, 36 of 36 squares of 10 and 100 runs GAIN with the six organisms run so far alone and, with the
real cluster inside, the organism's time over the line GAIN in 36 of 36 (`results/grid_v5/GRID.md`); the grid on omni-v11 has
its own manifest (`results/grid_v11/`). Every muscle is written out, organism by organism, the spine first, in
`docs/REALM_MUSCLES.md`, and explained, wired and carded in `docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix, with every
family's wiring on a real stack from `docs/wiring_recipes.csv`).

**The cloud (Azure), the bill at native's work.** The founder's order of 14 October: in a cloud Omni-Compass shows one thing,
the same work as native for a smaller bill, at the tune-down on the machines alone (`--give-back-only`). The Azure sets (the
steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9; A, B and C) run one at a time in their region
on omni-v11; the sets of earlier engines already started run to their end as their own record. The only Azure tables up so far are v1's
4-worker fleet (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): every gauge EVEN, a fleet too small to show one machine.
**Google (GKE) and Amazon (EKS)** carry the same four sets on the same harness (`scripts/google_queue.txt`,
`scripts/amazon_queue.txt`), each behind its own `switch=` line; the founder put their secrets in and switched both on on
18 October (the Operator's Manual's appendices G and H, click by click). Their first sets, on omni-v10, stopped at the login at
no cost and stay as its record: Google's stored key had been cut short when it was copied from Cloud Shell's screen, and
Amazon's account is on its Free plan, whose policy denies every machine read. Both queues are on again behind a $0 check
(`cloud-check`): the conductor starts a cloud's set only after that cloud's check passed (the key whole, the login, the plan,
the machine type and every quota; a short Amazon quota is asked of Amazon by the check itself), so nothing more is spent on a
login. Google waits for its key stored whole (downloaded as a file, never copied from the screen; appendix G, its step 4);
Amazon waits for its account on the Paid plan (appendix H, its step 1a). Then the sets start on their own, A, B and C on
omni-v11, one at a time in each machine-family queue.

**The card (evidence class P)**: every earlier card result is obsolete; the founder's runs on rented cards (Lambda) come at one
exact commit of the engine that stands, on his word. **Linux's own CPU governor and meter** (`cpu-power`): built and
preregistered; it waits for a machine on the metal, because GitHub's machines are virtual and expose neither.

**What is shown and what is not.** Shown, on real Kubernetes, three times each: a faster tail and more work inside the response
line on the same machines, on top of the operator's own autoscalers and rightsizers (the HPA, Goldilocks, KEDA), through
faults and a public day of demand, and fewer machines on a queue of jobs; on the live stacks, small gains on the cache and the
broker and the do-no-harm reading on three databases. Not yet shown: an energy or cloud-bill saving on real machines (energy on
kind is a declared model; the Azure tables at the tune-down are being made), and anything on a real card.

## The whole system, every layer composed (20 October)

The founder's question of 20 October: the cloud is the wire between the chip and the software, Omni-Compass sits at both ends
and at every layer between, what is the total? `results/WHOLE_SYSTEM.md` (built by `tools/whole_system.py`) answers it from the
tables that stand: each layer's ratio toward its gauge's aim, Rℓ(g) = oℓ/nℓ or nℓ/oℓ, measured with the layer under it as
native runs it (the card against its own limiter, the cluster against the HPA, the governors against the orchestrator as
shipped, the cloud against Azure's own autoscaler), composed by the product law R(g) = ∏ℓ Rℓ(g), every run's paired interval
carried through by the delta method, the three runs pooled by inverse variance, the layers added in the log. Two readings:
by the index's rule (an EVEN or one-run gauge counts as exactly 1) and with every interval carried. The product's
assumption, that a layer's factor does not change when the layers around it carry Omni-Compass too, is tested where the
tables allow (the governors' four ways: Omni-Compass on the organism alone against on top of the orchestrator, in the same
repetitions). The composition is class S over class P and L tables and across engines, said so on the page; the stacked
run (Omni-Compass at every layer at once) is the measurement that would replace it, and the page is remade as each layer's
omni-v13 runs land. The numbers stand on that page, never copied here.

## Open

1. **Every benchmark on omni-v11**: released A, then B, then C by the conductor from `scripts/reruns.txt` (the steady and
   wandering Kubernetes tests among them, MySQL, Redis and MongoDB with native as shipped beside the operator's setting,
   and every data store at the max beside the tune-down: MySQL, MongoDB and PostgreSQL had run at the tune-down alone);
   each table replaces its earlier engine's row on the sheet when its three runs land. CityLearn's omni-v11 table must read no
   LOSS in any district, as it did locally.
2. **The pod start wait under KEDA's HTTP add-on**: LOSS in omni-v10's three runs (+13.0%, +14.1%, +21.1% a pod), root-caused
   on 18 October to the test machine (`docs/POD_START_WAIT.md`): a pod on a node that never served unpacked its image inside
   the window on the one runner all kind nodes share. With the served image pre-pulled onto every worker before each arm, the
   same in both arms, it reads **EVEN** in omni-v11's three runs (`results/live/V11_KEDA_REQUESTS.md`). Closed.
3. **The kill test and the long run** on omni-v11 (`results/live/V11_ROBUST_KILL.md`, `V11_ROBUST_LONG.md`): every setting
   back at the operator's 8 to 11 s after the kill in 30 of 30 repetitions, a second governor to the end in every one; over
   two hours no leak, no failed decision, no slowing, everything handed back; no LOSS in either. Closed; the extended faults'
   table lands when its runs do.
4. **The swarm's proximity reflex** (a fault found 19 October beyond the counted cells): the fix makes the next engine version,
   with every wire that holds a governor's rules taken into the fingerprint, on the founder's word
   (`docs/CHANGE_CONTROL.md`).
5. **The grid and Azure on omni-v11**: restarted on 18 October; nothing cancelled.
6. **Google and Amazon**: on behind their $0 check; they start on their own once Google's key is stored whole and Amazon's
   account is on its Paid plan, the four sets A, B and C on omni-v11.
7. **The card**: the founder's runs on Lambda, one exact commit of omni-v11.
8. **Linux**: a machine on the metal for `cpu-power`.
9. **More room**: of the 159 muscles that read EVEN (the same as native) on the realms table, the room search of 16 October
   (`docs/OMNI_V7.md`) found none under the max's gauges within each muscle's own knob; six process loops miss at most 0.56% of
   decisions, a card candidate for a later version. The 14 of 26 knob-cases on the real stacks that read watch stay the next
   engine's question, in the toy gate first.
10. **Omni-Compass 1.0**: when the founder declares the engine final, the engine that stands then is published as 1.0 and
   the older fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the Operator's Manual: how to embed, wire, tune, run and check Omni-Compass; every muscle's wiring and card (Appendix E) |
| `docs/OMNI_COMPASS_OWNERS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`) | the Owner's Manual: the theory, the mechanism, the engine's source, every result, every muscle (Appendix G) |
| `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` (PDF: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`) | the Live Engine Manual: how to read the live engine page, its monitors, gauges and knobs, native beside Omni-Compass; what to do when a tile reads LOSS |
| `docs/BENEFIT_SHEET.md` | one number per benchmark, its word, its engine, every change in words |
| `docs/LEVELS.md` | every level on one page (muscle, organism, cluster, add-ons, service, plant, cloud, group of clusters), its counts of GAIN, EVEN, power given and LOSS, and any level whose gauges go the other way |
| `docs/REGISTER.md` | every muscle family wired, every benchmark run, every benchmark still to run |
| `docs/WIRING_VERDICTS.md` | write, watch or the operator's choice, per knob, from every result |
| `docs/OMNI_V12.md` | the engine that stands, what changed and how it was read; the earlier engines' pages (`docs/OMNI_V11.md`, `docs/OMNI_V10.md`, `docs/OMNI_V9.md`, `docs/OMNI_V8.md`, `docs/OMNI_V7.md`, `OMNI_V6.md`, `OMNI_V5.md`, `OMNI_V3.md`, `OMNI_V2.md`, `OMNI_V1.md`) stay with their own results as the road |
| `docs/history/STATE_OF_PLAY_2026-10-10.md` | this page as it stood on 10 October, on Omni v3, moved here whole |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
