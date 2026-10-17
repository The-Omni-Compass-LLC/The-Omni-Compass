# Omni-Compass: state of play (read this first)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

<!-- where things stand (tools/summary.py --fix) -->

**Where things stand, read from the result files.** Written by `python3 tools/summary.py --fix` from the files it names; `verify.py` fails a push in which this block no longer matches them. Nothing in it is typed by hand. The live results run on the engines named in their own tables, and every one of them runs again on the newest engine.

- **The engine on this checkout:** omni-v8, fingerprint f93d233136a1f902 (46 files).
- The muscles and the seven organisms on engine omni-v7 at the max (evidence class S, our own models; run 2026-10-16 04:34 UTC, commit 1637d32cd26c, 1107 muscles; source: results/realms_v5/REALMS_V5.md):
  - every muscle alone, over its loads: EVEN 580, GAIN 527
  - the organisms under the normal load: the spine: GAIN (fewer misses), misses -0.145 pp, power given +0.011%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.070 pp, power given +0.009%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.121 pp, power given +0.010%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.118 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.067 pp, power given +0.002%; the four stacked: GAIN (fewer misses), misses -0.092 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
  - the organisms under the climb load: the spine: GAIN (more work + fewer misses), misses -0.632 pp, power given +0.039%; Compute / AI / Cloud: GAIN (more work + fewer misses), misses -0.390 pp, power given +0.046%; Physics / Robotics / Autonomous: GAIN (more work + fewer misses), misses -0.317 pp, power given +0.021%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.217 pp, power given +0.000%; Distribution / Specialized: GAIN (more work + fewer misses), misses -0.460 pp, power given +0.026%; the four stacked: GAIN (more work + fewer misses), misses -0.349 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.094 pp, power given +0.000%
  - the organisms under the line load: the spine: GAIN (fewer misses), misses -0.371 pp, power given +0.038%; Compute / AI / Cloud: GAIN (fewer misses), misses -0.205 pp, power given +0.045%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses -0.250 pp, power given +0.030%; Energy / Facility / Industrial: GAIN (fewer misses), misses -0.117 pp, power given +0.000%; Distribution / Specialized: GAIN (fewer misses), misses -0.142 pp, power given +0.006%; the four stacked: GAIN (fewer misses), misses -0.176 pp, power given +0.000%; the whole tower: GAIN (fewer misses), misses -0.051 pp, power given +0.000%
- The grid (source: results/grid_v5/GRID.md): Across the grid: modelled, 36 of 36 squares of 10 and 100 runs GAIN (fewer misses); the 18 single runs: 18 with fewer misses; work +0.000%; power given +0.000% to +0.065%; with the cluster inside, 54 squares: 18 single repetitions (no reading); of the 36 of 10 and 100 repetitions, by gauge: "organism time over the line (% of steps)" GAIN in 36, LOSS in 0, "time over the response line (% of samples)" GAIN in 36, LOSS in 0, "response time (ms), 95th percentile" GAIN in 26, LOSS in 2, "energy (Wh)" GAIN in 26, power given in 0, "energy, parked workers still on at idle power (Wh)" GAIN in 26, power given in 0, "organism energy (J)" GAIN in 0, power given in 22, "organism work per energy" GAIN in 0, LOSS in 22, "failed requests (%)" GAIN in 18, LOSS in 0, "response time (ms), 99th percentile" GAIN in 12, LOSS in 2, "HPA replicas, mean" GAIN in 4, power given in 5, "pods started" GAIN in 3, power given in 0; off the clock in 3; invalid in 0.
- The Omni index (evidence class L, real machines, every measure the same in all three of our runs; the three-run tables of omni-v7, each named in its table): +4.2% GAIN on the resource reading (work, speed, machines, energy), +11.5% GAIN on the service reading (work and speed alone). Source: results/OMNI_INDEX.md.
  - Real Kubernetes (GitHub): +27.2% GAIN
  - Real cache (Redis, GitHub): +0.2% GAIN
  - Real messaging (Apache Kafka, GitHub): +0.1% GAIN
  - Real database (PostgreSQL behind PgBouncer, GitHub): +0.0% EVEN
  - Real database cache (MongoDB under YCSB, GitHub): +0.0% EVEN
  - Real database buffer pool (MySQL under sysbench, GitHub): +0.0% EVEN

**On the engine that stands (omni-v8): 0 of 24 benchmarks so far.** Every other row is that engine's own result, named in its Engine column, and runs again on the engine that stands (`scripts/reruns.txt`); results are never read across engines.

| Benchmark | Engine | Its one number | Its word | Class |
|---|---|---:|---|---|
| Every real test together: the Omni index | omni-v7 | +4.2% | GAIN, power given | L |
| Robustness: the two-hour run | omni-v7 | +0.0% | EVEN | L |
| Robot arms (MuJoCo), the three untouched robots | omni-v7 | +3.8% | GAIN | S |
| Redis, the cache's memory ceiling | omni-v7 | +0.2% | GAIN, power given | L |
| Real Kubernetes, faults | omni-v7 | +35.0% | GAIN, power given | L |
| Real Kubernetes, all four at once | omni-v7 | +37.4% | GAIN | L |
| Real Kubernetes, a queue of jobs | omni-v7 | +12.5% | GAIN | L |
| Real Kubernetes, a public day of demand (Google 2011) | omni-v7 | +31.5% | GAIN, power given | L |
| Real Kubernetes, a noisy neighbour | omni-v7 | +0.0% | EVEN | L |
| Power grids (SimBench), both load models | omni-v7 | +5.8% | GAIN, power given | S |
| PostgreSQL, the pooler's pool size | omni-v7 | +0.0% | EVEN | L |
| MySQL, the buffer pool's size | omni-v7 | +0.0% | EVEN | L |
| MongoDB, the storage engine's cache size | omni-v7 | +0.0% | EVEN | L |
| Kafka, the consumer group's size | omni-v7 | +0.1% | GAIN | L |
| Drone swarms, the three untouched cells | omni-v7 | +6.1% | GAIN | S |
| Buildings and batteries (CityLearn), the districts with batteries | omni-v7 | +0.8% | GAIN AND LOSS | S |
| Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs | omni-v7 | +18.0% | GAIN, power given | L |
| Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs | omni-v7 | +0.0% | EVEN | L |
| Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v7 | +78.3% | GAIN, power given | L |
| Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v7 | +44.8% | GAIN, power given | L |
| The six organisms with the real cluster inside, 10 and 100 copies | omni-v3 | +5.3% | GAIN, power given | L, the cluster; S, the organism around it |
| The big organisms with the real cluster inside, 1,000 copies on Azure | omni-v3 | +155.0% | GAIN | L, the cluster; S, the organism around it |
| The 945 modelled muscles as one tower, every muscle written at once | omni-v3 | +0.3% | GAIN | S |
| Robustness: the governor killed outright mid-run | omni-v3 | +8.6% | GAIN | L |

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


## In one paragraph (2026-10-17, the engine that stands is omni-v8)

**The engine that stands is omni-v8** (`OMNI_V8.json`, digest `f93d233136a1f902`, 46 files; `docs/OMNI_V8.md`), on main since
17 October by the founder's order. It is omni-v7 with one wire changed, the CityLearn runner: a battery whose building simulates
power outages stays native, because its charge is also the building's reserve. omni-v7's CityLearn table read LOSS in all three
of our runs in the seven 2023 districts, the only districts CityLearn ships with outages; the cause was ours, found on CityLearn
itself and reproduced to the last digit, and three narrower repairs were refused on the tuning district before this one. Read
locally before any GitHub run, omni-v8 gives native's numbers on the 2023 districts and omni-v7's on every other district. The
other 45 engine files are omni-v7's bytes. Every benchmark runs again on omni-v8 (`scripts/reruns.txt`, released a few a tick by
the grid conductor, A of every benchmark, then B, then C; the grid and every Azure set restarted on it the same day); until a
benchmark's three runs land, its row names the engine it ran on (`docs/BENEFIT_SHEET.md` and the standing block above). Results
are never read across engines. The standing block is written from the result files by `tools/summary.py --fix` and checked on
every push; the prose below says the same in words.

**On omni-v7, the engine of 16 to 17 October: twenty-two three-run tables** (`results/live/V7_*.md`, ten pairs a run on real
Kubernetes, three paired repetitions a run on the live stacks; native against Omni-Compass on top). Twenty-one read no LOSS:

- **Real Kubernetes (evidence class L).** All four in one run: work inside the response line **+41% to +61%**, the 95th
  percentile −56% to −62%, failed requests −9% to −14%, alert minutes −20% to −35%, GAIN in all three of our runs, machines the
  same. Faults: the 95th percentile −51% to −63%, failed requests −11% to −17%, GAIN; replicas +13% to +21% and pods started +34%
  to +41%, power given. A queue of batch jobs: machines and node-hours **−12% to −15%**, standby energy −8% to −11%, GAIN, the
  queue finished EVEN. The Google day of 2011: the 95th percentile −54% to −58%, time over the line −72% to −74%, alert minutes
  −52% to −67%, GAIN; pods started +107% to +143%, power given. A noisy neighbour: EVEN on every row. On top of Goldilocks: response
  time −45% to −47% mean and −60% to −62% at the 95th percentile, GAIN. On top of KEDA's HTTP add-on: −57% to −58% mean, −71% to
  −75% at the 95th percentile, alert minutes −93% to −96%, replicas −15% to −19%, GAIN. On top of KEDA on the CPU target and the
  requests: −36% to −38% mean, −52% to −54% at the 95th percentile, GAIN. CruiseKube and fixed capacity: EVEN, nothing to move.
  Parked-worker energy on the add-on tests +1.1% to +2.3%, power given. The two-hour run: no leak, every decision valid, every
  setting handed back, service EVEN.
- **The live stacks (L).** Redis: work inside the 2 ms line +1.2% to +1.7%, mean latency −1.8% to −7.9%, GAIN; memory +2.4% on
  `small`, power given. Kafka: consumers −0.3% to −0.8%, GAIN, the rest EVEN. PostgreSQL behind PgBouncer, MySQL under sysbench
  and MongoDB under YCSB: EVEN on every judged row but one MySQL row where the runs disagree; the verdict refused every give-back
  that could not prove it cost nothing.
- **The independent simulators (S, published models, never in the headline).** Power grids (11 SimBench grids): 67 gauge-rows
  GAIN, 14 power given, no LOSS. Robot arms (MuJoCo Menagerie): on the Kinova Gen3 peak torque −28.6% and tracking error −21.3%,
  GAIN; two arms left native. Drone swarms: energy a mission −7% to −20%, missions a charge +8% to +25%, GAIN, no near miss.
- **The one that read LOSS: buildings with batteries (CityLearn 3.0.2, S).** Electricity bought and the daily peak GAIN in all
  ten battery districts; in the seven 2023 districts the energy not served +2.0% to +9.8%, the time uncomfortable, the ramping
  and (in three) the highest peak, LOSS in all three of our runs: fixed in omni-v8 (above). One row stays and is said here: the
  2022 robustness district's monthly unevenness +0.11%, LOSS in all three of our runs, beside the bill −8.6%, the electricity
  bought −14.7% and the daily peak −14.0%, all GAIN; a ratio that rose because the energy fell faster than each month's top
  hours. omni-v8 does not change it; it is the next repair, in the toy gate first.
- **The one number.** The Omni index over the real tests: **+4.2% GAIN** on the resource reading (work, speed, machines,
  energy) and **+11.5% GAIN** on the service reading (`results/OMNI_INDEX.md`).

**The muscles and the seven organisms, modelled (evidence class S, our own models, never counted in the headline)**: 1,107
muscles in 70 families (`realms/catalog_v5.csv`), every muscle its own card (`realms/muscle_cards_v5.csv`), every muscle alone
over its loads EVEN 580 and GAIN 527, LOSS 0; every one of the seven organisms (the spine 267, the muscles every stack runs on;
Compute / AI / Cloud 540, Physics / Robotics / Autonomous 404, Energy / Facility / Industrial 480, Distribution / Specialized
484, the four stacked 1,908, the whole tower 1,107) GAIN (fewer misses, and under the climb more work) under the normal, climb
and line loads, the power given +0.00% to +0.05% (`results/realms_v5/REALMS_V5.md`, the engine it ran on named in its header;
`docs/THE_SPINE.md`); the grid, 36 of 36 squares of 10 and 100 runs GAIN with the six organisms run so far alone and, with the
real cluster inside, the organism's time over the line GAIN in 36 of 36 (`results/grid_v5/GRID.md`); the grid on omni-v8 has
its own manifest (`results/grid_v8/`). Every muscle is written out, organism by organism, the spine first, in
`docs/REALM_MUSCLES.md`, and explained, wired and carded in `docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix, with every
family's wiring on a real stack from `docs/wiring_recipes.csv`).

**The cloud (Azure), the bill at native's work.** The founder's order of 14 October: in a cloud Omni-Compass shows one thing,
the same work as native for a smaller bill, at the tune-down on the machines alone (`--give-back-only`). The Azure sets (the
steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9; A, B and C) run one at a time in their region
on omni-v8; the omni-v7 sets already started run to their end as omni-v7's record. The only Azure tables up so far are v1's
4-worker fleet (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): every gauge EVEN, a fleet too small to show one machine.
**Google (GKE) and Amazon (EKS)** carry the same four sets on the same harness (`scripts/google_queue.txt`,
`scripts/amazon_queue.txt`), each behind its own `switch=` line, off until that cloud's secrets are in the repository and the
founder turns it on (the Operator's Manual's appendices G and H, click by click).

**The card (evidence class P)**: every earlier card result is obsolete; the founder's runs on rented cards (Lambda) come at one
exact commit of the engine that stands, on his word. **Linux's own CPU governor and meter** (`cpu-power`): built and
preregistered; it waits for a machine on the metal, because GitHub's machines are virtual and expose neither.

**What is shown and what is not.** Shown, on real Kubernetes, three times each: a faster tail and more work inside the response
line on the same machines, on top of the operator's own autoscalers and rightsizers (the HPA, Goldilocks, KEDA), through
faults and a public day of demand, and fewer machines on a queue of jobs; on the live stacks, small gains on the cache and the
broker and the do-no-harm reading on three databases. Not yet shown: an energy or cloud-bill saving on real machines (energy on
kind is a declared model; the Azure tables at the tune-down are being made), and anything on a real card.

## Open

1. **Every benchmark on omni-v8**: released A, then B, then C by the conductor from `scripts/reruns.txt` (the steady and
   wandering Kubernetes tests among them); each table replaces its omni-v7 row on the sheet when its three runs land. CityLearn's
   omni-v8 table must read no LOSS in the 2023 districts and the omni-v7 table everywhere else.
2. **The 2022 robustness district's monthly unevenness** (+0.11%, LOSS): the next repair, in the toy gate first.
3. **The kill test**: three omni-v7 runs on the fixed harness started 17 October (they finish and stand as omni-v7's record);
   its omni-v8 runs are in the queue.
4. **The grid and Azure on omni-v8**: restarted on 17 October; nothing cancelled.
5. **Google and Amazon**: on the founder's word, once their secrets are in the repository (appendices G and H).
6. **The card**: the founder's runs on Lambda, one exact commit of omni-v8.
7. **Linux**: a machine on the metal for `cpu-power`.
8. **More room**: of the 159 muscles that read SAME AS NATIVE on the realms table, the room search of 16 October
   (`docs/OMNI_V7.md`) found none under the max's gauges within each muscle's own knob; six process loops miss at most 0.56% of
   decisions, a card candidate for a later version. The 14 of 26 knob-cases on the real stacks that read watch stay the next
   engine's question, in the toy gate first.
9. **Omni-Compass 1.0**: when the founder declares the engine final, the engine that stands then is published as 1.0 and
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
