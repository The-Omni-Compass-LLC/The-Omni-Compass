# Omni-Compass: state of play (read this first)

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Protected by copyright, patents and trademarks: Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

**Everything run again (10 October 2026, 01:24 to 01:31 UTC).** At the founder's order that every result be as of today, every
benchmark with a result was dispatched again on the current commit `3aac0ab7` (Omni v3, digest `b53d05449ee04c4b`, by
`tools/omni_version.py --commit`), native and omni, the wiring of each checked against its preregistration before the dispatch:
70 GitHub runs (the seven Kubernetes tests, the five live stacks on the brain's own verdict, the four simulators, the realms table
and the kill and long robustness scenarios, three runs each; the six organisms with the real cluster inside; the modelled grid at
1, 10, 100 and 1,000 copies) and the two big organisms at 1,000 copies on rented Azure machines, plus one replacement run for a Kafka
job GitHub's runner cut off (the record says which and why). Every table on this page stands
until its new set lands; the new set is then the result and the old table goes whole to `docs/history`. The record, run by run
with inputs, times and ids, is `docs/RERUN_2026-10-10.md`. Not restarted, and why: the three 24-hour robustness machines (started
8 October on the same harness, byte for byte, ending about 10:15 UTC today) and the Azure fleet that can show one machine, which
waits on the family allowance those machines hold.


## In one paragraph (2026-10-07, Omni v3)

**The engine is Omni v3, frozen and fingerprinted** (`OMNI_V3.json`, `docs/OMNI_V3.md`: v1's law and controllers byte
for byte, 945 muscles in 59 families, a do-no-harm gate on speed knobs). Every benchmark runs three times as separate
GitHub runs on it (A the result, B and C the replications) and every judged row reads confirmed better, confirmed worse,
no difference beyond the noise, or the runs disagree (`docs/OMNI_V1.md`, the rule). **Real Kubernetes, six tests, ten
pairs each, all six confirmed on v3** (`results/live/V3_*.md`): work inside the response line **+35% to +49%** in all
three runs of the all-four test (21.0 → 31.2 requests a second in run A); the 95th percentile **−47% to −66%** in every
run of the steady, wandering, all-four and fault tests; failed requests −9% to −14% where load swings; machines −1.5% to
−2.9% at steady load and −19% to −23% on the batch queue, with the standby-model energy −13% to −16% there; beside a
noisy neighbour no difference beyond the noise on every row. **A real database** (PostgreSQL behind PgBouncer,
`results/live/V3_PGBENCH.md`, the second counted set): 36% to 38% fewer connections held open for the same work and latency
on the read-only workload, host CPU and median latency inside the noise on all three workloads (the first set's CPU cost was
measured and found to be our own harness, and is gone); on the slow write workload the add rule bought connections above
the operator's setting, confirmed worse, nothing bought; the runs disagree on the third. **Real messaging** (Apache
Kafka as shipped, `results/live/V3_KAFKA.md`): on all three untouched workloads work inside the 500 ms line **+16% to
+21%**, the 95th percentile 1.6 s → 9 to 14 ms and messages waiting −92% to −97%, confirmed better, no message lost;
consumers held 2 → 6 to 8, **confirmed worse**, the resource the gain costs; host CPU worse on one workload, inside the
noise on two. **A real cache** (Redis as shipped, `results/live/V3_REDIS.md`): on all three untouched workloads work inside
the 2 ms line **+14% to +27%**, the hit rate +14% to +27% and the mean latency −30% to −61%, confirmed better; the memory
ceiling held 64 → 200 to 270 MB, **confirmed worse**, the resource the gain costs; host CPU inside the noise. **A real
database's storage-engine cache** (MongoDB as its publisher ships it under YCSB, `results/live/V3_YCSB.md`): on four
untouched workloads the cache size held fell **−21% to −36%, confirmed better** on all four (the second counted set of 9
October, on the miss-share gate; the first set's larger saving was a cold cache emptied before its first eviction, kept in
the history), settling where the gate finds the working set; work inside the 1 ms line, p95, mean latency and host CPU
inside the noise on all four; no failed operation; 8 rows better, 0 worse. **A public day of demand on the real cluster** (the Google cluster trace of 2011, its first day of job submissions turned
into the wandering test's schedule by a rule written before the runs, `results/live/V3_TRACE_GOOGLE2011.md`): p95 **−65% to
−71%**, time over the line −81% to −84%, failed requests −8% to −17%, **machines in service −6% to −10%**, confirmed better in
three runs of ten pairs; pods started +23% to +35% as point estimates, inside the noise in one run; 9 rows better, 0 worse. **A real database's buffer pool** (MySQL as Ubuntu ships it under sysbench, `results/live/V3_SYSBENCH.md`): on the four
untouched workloads (the third counted set of 9 October, on the rule that grows the pool only while it is missing) the pool
held fell **−49% to −56% on burst, confirmed better**; on read_write the pages the pool holds rose **+44% to +52%, confirmed
worse** (memory bought on real misses for a written working set) with the host's CPU **−4% to −6%, confirmed better**, a
trade; read_only inside the noise (the second set's −50% to −56% there was in part the first chunk given back before any
read, now refused) and update_index disagreeing; work inside the line, p95, p99 inside the noise everywhere; no error; the
pool handed back on all 45 omni arms; the second set is kept whole in `docs/history/V3_SYSBENCH_set2.md`. The first counted set
(every row inside the noise, 15 arms not handed back because the plug's restore met the server's unfinished shrink) is kept
whole in `docs/history/V3_SYSBENCH_set1.md`, the plug fixed and the fix declared in `docs/MYSQL_PREREGISTRATION.md`. **The
Omni index, real machines only, confirmed three times: +20.5%** (`results/OMNI_INDEX.md`; Kubernetes +28.8% over seven tests, the database
+4.0%, Kafka +166.9%, Redis −24.9%, the database's cache +8.5%, the database's buffer pool +5.2%, each category weighed the same; a row inside the noise counts as exactly 1; the three database categories read their second or third counted sets of 9 October, on which the harness costs of the first sets were removed and the gains came down to what is real; a second reading, declared 9 October at the founder's question about what a cache is for, scores service alone (work and speed, resources shown and not scored) and stands at **+71.8%** beside the +20.5%, Redis +8.8%, Kafka +1,193%, Kubernetes +83%, the database stacks nothing, both readings in the index file and the first the headline; Kafka's speed ratio
is large because native's queue grew at nine tenths of its capacity and Omni's did not; Redis's category is negative
because the memory it holds for a wide working set is the resource it trades and reads worse by rule; MongoDB's is
positive because there the governor gave memory back). The v1 tables read the same and stay as the first engine's record.

**What is shown and what is not.** Shown: more work inside the response line on the same machines and a faster tail,
on real Kubernetes, three times on a frozen engine; a real database holding fewer connections for the same service; a
real message queue kept short at the cost of more consumers running.
Not yet shown: an energy or cloud-bill saving on real machines. Energy on kind is a declared model (the machines are
containers on one runner); Azure's bill on a 4-worker fleet read no difference beyond the noise on every gauge
(`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`), which is a fleet too small to show one machine; the fleet of 40
workers in nine machine families that can show one is preregistered and dispatched (`docs/K8S_COMPASS_PREREGISTRATION.md`,
the fleet that can show one machine, amendments 1 to 3), waiting on Azure's own capacity in eastus. The real card has
not run on the current governor; every earlier card result is obsolete and is run again by the founder on rented cards.

**Wire in, or watch (9 October).** The founder's order: Omni need not be wired into every muscle; where it cannot beat
native, the muscle stays native and Omni only reads it. `docs/WIRING_VERDICTS.md` (`tools/wiring_verdicts.py`, checked by
`verify.py` against every table it reads) gives every knob in every result one of three words. Real stacks: 12 of 24
knob-cases **write** (six of the seven Kubernetes demands, PostgreSQL's read-only workload, MongoDB's four workloads, MySQL's
burst); 7 are **the operator's choice** (Kafka's three workloads, where consumers buy a hundredfold shorter queue and both
readings of the index say the trade pays; Redis's three, where memory buys the hit rate and only the service reading says it
pays; MySQL's read_write, pages for CPU); 5 **watch** (Kubernetes beside a noisy neighbour, PostgreSQL's simple_update, where
connections were bought above the operator's setting and nothing bought for them, and tpcb_hot, where the runs disagree;
MySQL's read_only and update_index). Every confirmed loss on a real stack is a resource spent for the knob's own service,
declared in advance or disclosed on the first counted set; none is a service loss. The simulators: 21 write, 15 trades (the
four SimBench grids that export, where the lower voltage costs line losses; the seven 2023 CityLearn districts, where the bill
is worse), 3 watch (two robots the engine itself left native, one grid where nothing was bought). The 945 modelled muscles:
124 write, 13 trades, 808 watch, 746 of them because the native controller kept the reading in band and the law never wrote;
all 255 admission muscles are among the 746. The 14 organism cells with the real cluster inside all write on the cluster's
gauges. The engine is unchanged; the page decides what an operator connects.

**The brain's own verdict, live (built 9 October, running since 10 October).** The founder's order of the same evening: the verdict must
be the brain's, in real time, on the knob, before it writes; a knob that cannot prove it pays stays native. `tools/knob_verdict.py`
wraps the frozen engine's verdict (`omnicompass/verdict.py`, unchanged) around every live knob of the five database, messaging
and cache harnesses: the knob starts in watch, a paired trial on the stack itself allows one notch at a time under the declared
objective (resource, the index's reading, or service), a refused step is not taken, a trial holds the knob, a fail-up never
spends beyond the allowance, the operator's setting is always free. Declared as amendments in the five preregistrations with the
expectation written before the runs: Redis left native under the resource objective (the first notch refused), Kafka allowed step
by step while each consumer pays, PostgreSQL's add above the operator's setting refused on simple_update, MySQL's read_write
chunks refused, MongoDB's cache given back a notch a trial. The 21 runs (the five stacks under the resource objective; Redis and
Kafka also under the service objective; three runs each) were dispatched on 10 October at 01:28 to 01:29 UTC on commit `3aac0ab7`
(`docs/RERUN_2026-10-10.md`); the tables are read from them when they land. Where the brain's verdict stands today, knob by knob
(the five stacks both ways; the cluster's machines, the card's clock, the robots' speed and the drones' cruise by the engine's own
verdict; the grids, the districts and the 945 modelled muscles by the law alone), is the last table of `docs/WIRING_VERDICTS.md`.
Inside the modelled realms the organism still
takes one directive for every muscle; the verdict per muscle there is the next engine, Omni v4, designed in
`docs/OMNI_V4_PLAN.md` and not built, because every result must be run again on a new engine.

## Measured on real systems (evidence class L), Omni v3

| Test, ten pairs × three runs | Work | Speed (p95) | Machines | Energy (declared model) | Source |
|---|---|---|---|---|---|
| All four in one run | **+35% to +49%** | −61% to −66% | inside the noise | inside the noise | `results/live/V3_ALL_FOUR.md` |
| Steady work in steps | equal by design | −65% to −66% | **−1.5% to −2.9%** | −1.3% to −2.1% | `results/live/V3_STEADY.md` |
| Demand that wanders | failed requests −9% to −12% | −57% to −63% | inside the noise | inside the noise | `results/live/V3_WANDERING.md` |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time (`docs/TRACES_PREREGISTRATION.md`) | failed requests **−8% to −17%**, confirmed better; no pod ever without a machine | **−65% to −71%** (p99 −49% to −61%) | **−6% to −10%, confirmed better** (replicas −5% to −6%) | standby model **−4% to −7%, confirmed better**; idle-power model inside the noise in one run | `results/live/V3_TRACE_GOOGLE2011.md` |
| Faults: machine down, spike, runaway pod, blind probe | failed requests lower in all three, clear of the noise in one | −47% to −62% | inside the noise | inside the noise | `results/live/V3_FAULTS.md` |
| A queue of batch jobs | queue finished no difference beyond the noise | mean response −10% to −14% | **−19% to −23%** (−29% to −35% after the queue) | **−13% to −16%** | `results/live/V3_BATCH.md` |
| Fairness, a noisy neighbour | inside the noise on every row | inside the noise | inside the noise | inside the noise | `results/live/V3_FAIRNESS.md` |
| PostgreSQL behind PgBouncer, three workloads (the second counted set) | inside the noise | inside the noise (median and p95; the tails worse as point estimates on `select`, inside the noise by the rule) | connections held open **−36% to −38% on `select`, confirmed better**; the runs disagree on `tpcb_hot`; `simple_update` connections most at once **+72% to +80%, confirmed worse** | host CPU-seconds inside the noise on all three (the first set's +14% to +28% was our harness's own `psql` launches, measured and removed) | `results/live/V3_PGBENCH.md` |
| Apache Kafka, a consumer group's size, three workloads | work inside the line **+16% to +21%**; no message lost | p95 **1.6 s → 9 to 14 ms**, lag −92% to −97% | consumers held **2 → 5.8 to 7.9, confirmed worse** | host CPU-seconds +10% to +20% confirmed worse on light, inside the noise on heavy and burst; CPU per message inside the line −10% to −12% on burst | `results/live/V3_KAFKA.md` |
| Redis, a cache's memory ceiling, three workloads | work inside the line **+14% to +27%**, hit rate +14% to +27%; no failed request | mean latency −30% to −61%; p95 within a hair of native's (a miss is a miss in both arms) | memory ceiling held **64 → 200 to 270 MB, confirmed worse** | host CPU-seconds inside the noise on all three | `results/live/V3_REDIS.md` |
| MongoDB under YCSB, a database's storage-engine cache size, four workloads (the second counted set) | inside the noise on all four; no failed operation | p95, p99 and mean latency inside the noise on all four (the first set's burst mean +2% to +4% worse is gone) | cache size held **−21% to −36% on all four, confirmed better**, settling at 330 to 405 MB where the gate finds the working set | host CPU-seconds inside the noise on all four | `results/live/V3_YCSB.md` |
| MySQL under sysbench, a database's buffer pool size, four workloads (the third counted set) | inside the noise on all four; no error | p95, p99 and mean inside the noise on all four | pool held **−49% to −56% on burst, confirmed better**; on read_write the pages held **+44% to +52%, confirmed worse**; read_only inside the noise; update_index the runs disagree; handed back on all 45 omni arms (the two earlier sets kept whole in the history) | host CPU **−4% to −6% on read_write, confirmed better**; inside the noise elsewhere | `results/live/V3_SYSBENCH.md` |
| Robustness: the governor killed outright at 40% of the window, 10 pairs × 3 runs | **every setting back at the operator's 7 to 11 s after the kill, 30 of 30**; a second governor to the end; failed requests over the window −9% to −15% | the 120 s after the kill inside the noise against native; the whole window p95 −42% to −45% | inside the noise | inside the noise | `results/live/V3_ROBUST_KILL.md` |
| Robustness: the long run, 7,200 s an arm, 3 pairs × 3 runs | decisions 97.5% or more of expected (valid); failed requests inside the noise | service confirmed better in A, inside the noise in B and C (no difference beyond the noise in 2 of 3) | inside the noise; **memory at most 1.07 of its first ten minutes (no leak)**; decision time at most 1.20 (no slowing); every setting handed back at the end | inside the noise | `results/live/V3_ROBUST_LONG.md` |
| The six organisms with the real cluster inside, 10 and 100 copies, 5 pairs a cell | the organisms' work unchanged | p95 better in every cell | 6 in both arms (no autoscaler under kind) | the organisms' energy lower in every cell | `results/live/V3_SIX_KUBE.md` (v1 at 1 to 1,000 copies: `V1_SIX_KUBE.md`, `V1_BIG_ORGANISM.md`) |

## Measured on a real cloud (Azure, its own bill), Omni v1

| Test | Reading | Source |
|---|---|---|
| Steady load, 4 workers, 5 pairs | no difference beyond the noise on any gauge; the bill −4.7% with its interval across zero | `results/live/V1_AKS_STEADY.md` |
| A burst sized to the cluster, 4 workers, 5 pairs | the bill +5.0% with its interval across zero; p99 −34% clear of the noise in this one run; the rest inside the noise | `results/live/V1_AKS_BURST.md` |
| The fleet that can show one machine (40 workers, nine families) on v3 | dispatched; two earlier dispatches refused by the subscription's family allowances before any arm ran, the third by Azure's own cluster capacity in eastus; every refusal cost cents and is recorded | `docs/K8S_COMPASS_PREREGISTRATION.md` |

## Simulated (evidence class S: models, never counted in the headline), Omni v3

| What | Reading | Source |
|---|---|---|
| The 945 muscles and six organisms, A/B/C | reproduced to the digit in 3 of 3; 0 muscles worse; every organism superior within guardrails (work per energy +0.1% to +0.3%) | `results/realms/REALMS.md` |
| The whole tower at 1,000 copies (945,000 modelled muscles) with the real cluster inside, on a rented machine, 3 pairs (v3) | the organism's work unchanged (rounding-level) | the cluster's p95 **6.7 s → 160 ms**, p99 −98%, time over the line **76% → 0**, failed requests **4.8% → 0** | 6 machines in both arms | inside the noise (standby model); the organism's energy −0.4% (model) | `results/live/V3_BIG_ORGANISM.md` |
| The four stacked at 1,000 copies with the real cluster inside, on a rented machine, 3 pairs (v3) | the organism's work unchanged (rounding-level) | the cluster's p95 **2.9 s → 150 ms**, p99 −97%, time over the line **51% → 0**, failed requests **0.14% → 0** | 6 machines in both arms | inside the noise (standby model); the organism's energy −0.4% (model) | `results/live/V3_BIG_ORGANISM.md` |
| The organisms at 1, 10, 100 and 1,000 copies × 1 to 1,000 runs, 84 of 90 cells | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left are beyond the machines available | `results/scale/GRID.md` |
| Power grid, 11 SimBench grids in pandapower, A/B/C (v1 and v3 identical) | with ZIP loads energy drawn and net import better in all 11; losses better in 7, worse in 4; tap operations fewer in 10, 4 → 8 a year in one (worse, the declared cost) | `results/live/V3_PANDAPOWER.md` |
| Robot arms, MuJoCo Menagerie, A/B/C | Gen3 and Panda: peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%; the Panda's copper +14% worse; UR5e and iiwa left native | `results/live/V3_MUJOCO.md`, `V1_MUJOCO_PANDA.md` |
| CityLearn, every district, A/B/C | electricity bought, peak and unevenness better in all 11 battery districts, carbon in 8; the bill worse in 7, ramping worse in 7 | `results/live/V3_CITYLEARN.md` |
| Drone swarms, gym-pybullet-drones, 20 drones in three cells, A/B/C | energy a mission −7% to −20% and missions a charge +8% to +25%, confirmed better; no late mission, reserve breach, near miss or collision in any arm | `results/live/V3_SWARM.md` |

## The card (evidence class P)

Every earlier card result ran on a controller since replaced and is obsolete. The one-card, card-inside-the-organisms
and eight-card runs are the founder's, on rented cards, after the CPU and cloud work, at one named commit
(`docs/GPU_RUN_GUIDE.md`, `docs/GPU_PREREGISTRATION.md`).

## Verified in code

| Property | Where |
|---|---|
| The canonical engine is `symmetric_verified`; the printed chart is a named variant, not benchmarked | `docs/CANONICAL_ENGINE.md` |
| Nine laws twinned in C++20 and proven equal to the Python; sealed by fingerprint | `results/SEAL.json`, `tools/seal.py` |
| The conveyance law conserves its budget and converges (proof and 20,000 random systems) | `docs/CONVEYANCE_LAW.md`, `tests/test_conveyance.py` |
| Safety shield: 2,000,000 adversarial cases, 0 violations; C++ engine: 100,000,000 decisions, no failures | `tests/test_shield_properties.py`, `results/SOAK.json` |


## Open

1. **Azure, the fleet that can show one machine**: steady and burst on 40 workers, v3; waiting on Azure's cluster
   capacity in eastus (the only region where this subscription has more than 10 cores). Then B and C.
2. **The four stacked and the tower at 1,000 copies with the real cluster inside, on v3: both done, 3 of 3 on the clock**
   (`results/live/V3_BIG_ORGANISM.md`). The stack: the cluster's p95 2.9 s → 150 ms, time over the line 51% → 0, failed
   requests 0.14% → 0, machines and energy unchanged, 22 s behind a 10,800 s window. The tower (945,000 modelled muscles,
   collected 9 October by run 37945866426 after 25 hours on its rented machine): the cluster's **p95 6.7 s → 160 ms (−98%)**,
   p99 9.1 s → 187 ms, **time over the line 76% → 0, failed requests 4.8% → 0**, all clear of zero; replicas, pods started
   and machines (6 in both arms) the same; energy inside the noise; 14 s behind the window in both arms; the organism's own
   model (shown, never in the index) energy −0.4% and work rounding-level worse by rule. Both machines deleted.
3. **The real card**: the founder's runs on Lambda, one exact commit.
4. **Robustness** (`docs/ROBUSTNESS_PREREGISTRATION.md`, no engine file changes): the kill scenario is done
   (`results/live/V3_ROBUST_KILL.md`: every setting back 7 to 11 s after the kill in 30 of 30 repetitions) and the
   governor's own CPU is tabulated (`results/live/V3_OWN_COST.md`); the long run is done (`results/live/V3_ROBUST_LONG.md`, 3 pairs × 3 runs, 7,200 s an arm: no leak, the decisions valid, no slowing, every setting handed back at the end; service inside the noise in two of three runs);
   the 24-hour run on three rented machines (scenario 2b, started 8 October 10:15 UTC) ends about 10:15 UTC on 10 October and is
   collected by the scheduled collect; the kill and long scenarios were dispatched again on 10 October (`docs/RERUN_2026-10-10.md`).
5. **YCSB on MongoDB, done** (`docs/YCSB_PREREGISTRATION.md`, `results/live/V3_YCSB.md`): the operator's WiredTiger cache
   as native, Omni on the cache size through the server's own console; four smoke runs recorded, then A, B and C on v3; the
   cache held given back by about half on two untouched workloads at no measurable cost in work, p95 or CPU, one confirmed
   loss (the burst mean latency, +2% to +4%) that the second counted set of 9 October removed (item 6); the index spans six
   real categories at +20.5%. Cassandra and Redis under YCSB and HammerDB are next in row 24.
6. **The costs in the database tables, traced and amended with the engine locked** (8 October; `docs/POSTGRES_PREREGISTRATION.md`
   amendment 2, `docs/MYSQL_PREREGISTRATION.md` amendment 2, `docs/YCSB_PREREGISTRATION.md` amendment 1; Omni v3 before and
   after, the harnesses are outside the fingerprint). PostgreSQL's +14% to +28% host CPU was our harness launching a `psql`
   process for every reading (measured: 52 ms of CPU a launch, 7,956 console logins in one workload's pooler log, +55.9 CPU-s
   on the launches against a +52.8 s host difference on a metered repetition; the pooler +1.2 s), and its +15% to +17% median
   latency was the pool shrunk into a queue the pooler itself reported: one console connection an arm and the queue line (a
   server taken back only while clients waited under 1% of the pooler's time, servers added back one per percent of
   waiting, up to the operator's 20). MySQL's read_write pool was bought for slow writes the pool cannot mend (36 of 82 grows at a miss share under
   1%): the pool grows only while missing. MongoDB's memory saving on b, c and burst was a cold cache given back before its
   first eviction (four notches in the first five seconds of every arm) and held at the floor evicting: the give-back gate is
   the miss share, as MySQL's, and the saving may fall to the noise, said beforehand. The second (PostgreSQL, MongoDB) and
   third (MySQL) counted sets run on these rules, dispatched 23:16 UTC on commit `310cf318` (PostgreSQL 37858494179,
   37858496620, 37858499033; MySQL 37858501997, 37858505059, 37858509109; MongoDB 37858512907, 37858515717, 37858519010).
   **Done, 9 October; the earlier tables are whole in `docs/history`.** PostgreSQL: CPU and median latency inside the noise on
   all three workloads, connections −36% to −38% on `select` confirmed better, the runs disagree on `tpcb_hot`, and on
   `simple_update` the add rule of amendment 1 buys connections above the operator's 20 (most at once +72% to +80%,
   confirmed worse, nothing bought): category +4.0% from +14.2%. MongoDB: the cache −21% to −36% on all four workloads,
   confirmed better, the latency cost gone, 8 rows better and 0 worse: category +8.5% from +10.2%. MySQL: burst −49% to −56%
   confirmed better; read_write memory +44% to +52% worse with CPU −4% to −6% better, a trade; read_only inside the noise
   (its earlier saving was in part the cold-start give-back); update_index disagree: category +5.2% from +12.2%. The index
   headline moves from +24.1% to **+20.5%**: smaller, and every number in it is now a gain without a harness cost under it.
7. **The queue** (`docs/REGISTER.md` section 4, `docs/PROOF_PROGRAM.md`): drone swarms on PX4 and ArduPilot (gym-pybullet-drones done), YCSB on
   Cassandra and Redis and HammerDB, Spark, OpenSearch, fio, Open-RMF, the 24-hour robustness run, Basilisk, Orekit and GMAT,
   RocketPy, Cantera (Kafka and Redis done); one or two at a time, each preregistered.
8. **The gaps the tree shows (the founder's reading, 10 October).** The index's six real categories are the cluster, PostgreSQL,
   Kafka, Redis, MongoDB and MySQL; Azure waits on its three-run close (item 1) and the card on its run on the current controller
   (item 3); the power grids and the districts are in as simulations, never in the index by rule. Not yet a category: **a second
   and a third cloud**, AWS and Google Cloud under Azure's method (`docs/REGISTER.md` row 38; each needs its own account credential
   in a GitHub secret and an allowance of about 90 cores, about $12 a steady and $22 a burst run, nothing spent until the account
   exists); **CPU power through Linux's own governor with the RAPL meter**: **built and preregistered the same day**
   (`docs/CPU_POWER_PREREGISTRATION.md`; `tools/run_cpu_power.py`, one command `scripts/cpu_power_run.sh`, workflow `cpu-power`,
   the three-run table `tools/cpu_power_abc.py`): the kernel's governor stays native, Omni moves the frequency ceiling on top
   inside [half the top clock, the top], every notch down tried on the machine first by the brain's verdict, energy from the
   processor's own meter and a wall plug where fitted; it waits for a machine on the metal, the founder's own tower or laptop on
   Linux (free) or a rented bare-metal server (about $10), because GitHub's machines are virtual and expose neither the governor
   nor the meter (the workflow's probe says so on every dispatch); **the card's energy meter**, which the card harness already
   has (the integral of the device's power draw, the CPU package by RAPL, the wall plug where fitted, `tools/gpu_reps.py`) and
   which reads on the founder's run. **The founder's sweep of the same day** (nothing with value left out: operating systems,
   television and telecom, satellites and signals, energy, oil and minerals, finance, the platforms and social media, science and
   physics, robotics to the top) added rows 39 to 57 to the register's queue and section 3.5 to the proof program, each an open
   benchmark with a shipped controller for native and one knob for Omni, each to be preregistered before its first run; aerospace
   and rockets were already rows 32 to 36. **The second check the same night** (cars, self-driving, batteries, nuclear, power plants,
   medicine, surgery named) is written as `docs/COVERAGE_MAP.md`: every domain in the world of controllers against the register,
   with the abbreviations (AKS, CPU, UPS, GPU, AWS and the rest) each given its place; it added rows 58 to 73 (self-driving stacks,
   the EV powertrain, mobility fleets, stream processing, storage clusters, AI batch admission, games, thermal plants with nuclear as
   the model only, fabs, surgical robot servos, the other Kubernetes scalers, distributed SQL, the other brokers, CDN caches, air
   traffic, observability pipelines) and wrote the exclusions by rule: safety reserves, clinical dosing, trading decisions, weapons, a
   person's command, solvers without a controller.
9. **Omni-Compass 1.0**: when the founder declares the engine final, v3 as it stands is published as 1.0 and the older
   fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the manual: the governor, its mechanism, the wiring stack by stack, the frozen engines, the three-run rule, every result |
| `docs/RERUN_2026-10-10.md` | every benchmark dispatched again on 10 October 2026 on one commit: the record, run by run |
| `docs/OMNI_V3.md`, `docs/OMNI_V1.md` | what each engine is and every result read on it |
| `docs/REGISTER.md`, `docs/PROOF_PROGRAM.md` | every muscle, every benchmark run and still to run; the program to full size |
| `results/live/V3_*.md`, `V1_*.md`, `results/live/raw/` | the three-run tables and every archived run's files |
| `results/OMNI_INDEX.md` | the one combined number |
| `docs/BENEFIT_SHEET.md` | one number per benchmark, plus always good for Omni and minus always bad, whatever the gauge measures; yes, no, none or trade beside it |
| `docs/WIRING_VERDICTS.md`, `results/WIRING_VERDICTS.csv` | which knobs earn a wire in: write, watch or the operator's choice, per knob and per muscle, from every table, every loss with its cause |
| `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md` | wiring it in yourself |
| `docs/METRICS_CATALOG.md` | every gauge, and whether it is measured or modelled |
| `omnicompass/`, `omni_controller/`, `realms/`, `cpp/` | the engine, the controllers, the muscles, the C++20 twins |
| `docs/HISTORY.md` | earlier states of play, kept whole |

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
