# Wire in, or watch: the verdict per knob, from every result in the repository

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Omni-Compass is wired **out of** every muscle: it reads every reading. It is wired **into** a knob only where the paired measurement shows no gauge of the muscle read **LOSS** against native. Where the measurement shows nothing (**EVEN**), or shows a LOSS, the muscle stays native and Omni only watches it: one wire out, no wire in. This is not a new rule. It is what the engine does on the muscle itself before it moves anything (`omnicompass/verdict.py`: the paired trial, and the verdict **left native** where no step is allowed), and it is the watch arm of every realms run (`docs/REALMS_PREREGISTRATION.md`: the governor reads every period and writes nothing). This page applies the same principle to every published result, one verdict per knob, so that an operator can see which knobs earn a wire in and which stay native. The founder's order of 9 October 2026: where Omni cannot beat native, the muscle lives by itself; we only wire out of it.

Every verdict here is computed by `tools/wiring_verdicts.py` from the test's own result file; nothing is typed in, and `verify.py` fails if this page differs from what the tables give. One row per knob and case: `results/WIRING_VERDICTS.csv` (1214 rows, the 1,107 modelled muscles included one by one, and the seven organisms under three loads).

## The rule

Every judged gauge of a table counts (rows marked "shown, not judged" never do). Every reading is **GAIN**, **EVEN** or **LOSS**, decided by what the gauge is for and never by the sign of its number (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times and failed requests are time waited, missed or failed, so a fall is GAIN; work done is GAIN when it rises; machines, energy, memory, connections, consumers and processor time are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, the price named beside what it bought. Each gauge's aim is its preregistration's; an operator whose aim differs reads the same numbers the other way. A knob reads:

- **write**: at least one gauge GAIN in all three of our runs, and no LOSS and no power given. Omni holds the knob.
- **watch**: no GAIN in all three of our runs. The knob stays native; Omni reads it and writes nothing. Where a gauge read LOSS or power given in all three of our runs, it is named and its cause given below. Where the runs disagree, nothing is settled and the knob stays native until it is.
- **operator's choice**: GAIN, and LOSS or power given, both the same in all three of our runs: a trade. Both readings of the Omni index are shown where the test is in it (the resource reading, the preregistered headline, and the service reading, work and speed alone), and the side that pays is named. The operator who wants the gain and can pay the price wires in; every other operator watches.

A modelled muscle (the 1,107 on their plants under its own load and work waiting in line, `results/realms_v5/MUSCLES_V5.csv`, engine omni-v5 at the max, the law omni-v6 carries unchanged) takes its verdict from its label by rule: a GAIN on work, speed or misses (MORE WORK, FASTER, FEWER MISSES, alone or together, on every load it ran) is write, and the energy the max took for it is power given, shown beside it and never a trade (the founder's order of 13 October); SAME AS NATIVE is watch, nothing moved beyond the noise; AT ITS LIMIT ON NATIVE is watch by design, the knob already at the top of its range on native, read and left native.

## The count

| Where | Knobs or cases | Write | Operator's choice | Watch |
|---|---:|---:|---:|---:|
| Real stacks, three runs each (Kubernetes under seven demands; the pool, the consumer group, the memory ceiling, the storage-engine cache and the buffer pool, each under its untouched workloads) | 26 | 9 | 5 | 12 |
| Independent simulators, three runs each (robot arms, grids, districts, swarms; evidence class S) | 38 | 20 | 15 | 3 |
| The 1,107 modelled muscles, alone on their plants under two loads (evidence class S) | 1107 | 527 | 0 | 580 |
| The organisms with the real cluster inside (GitHub at 10 and 100 copies; Azure at 1,000) | 14 | 12 | 1 | 1 |

In words: on the real stacks Omni earns its wire in on 9 of 26 knob-cases, trades on 5 and watches on 12. Of the 1,107 modelled muscles, 527 earn a wire in and 580 stay native: 421 of the 580 are at their limit on native (the knob already at the top of its range: nothing to push, read and left native) and 159 read the same as native (nothing moved beyond the noise). A knob left native costs nothing and earns nothing; it needs no wire in, and the page below says so muscle by muscle.

## The real stacks (evidence class L: live software, three separate GitHub runs on the frozen engine)

The reading of every judged gauge is in the test's own table (the Source column). The index columns are the two readings of `results/OMNI_INDEX.md` for that test, where it has one.

### Real Kubernetes: one knob under seven demands

The knob: the autoscaler's replicas, the floor and the machines, on top of the Horizontal Pod Autoscaler (kind clusters on GitHub, ten pairs a run).

| Demand | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| steady work | mean response cut 48% to 49%, p95 cut 64% to 65%, p99 cut 69% to 73%, time over the line cut 98% to 100%, alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 100% | none | **write** | +29.8% | +68.4% | 5 gauges GAIN in all three of our runs (mean response cut 48% to 49%, p95 cut 64% to 65%, p99 cut 69% to 73%, time over the line cut 98% to 100% and 1 more), none LOSS or power given; 7 gauges EVEN, inside the noise. Omni holds the knob | `results/live/V10_STEADY.md` |
| demand that wanders | parked-worker energy cut 0.3% to 0.4%, standby-model energy cut 0.3% to 0.4%, mean response cut 45% to 50%, p95 cut 57% to 65%, p99 cut 34% to 46%, time over the line cut 38% to 45%, alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 21% to 32% | none | **write** | +36.7% | +154.6% | 7 gauges GAIN in all three of our runs (parked-worker energy cut 0.3% to 0.4%, standby-model energy cut 0.3% to 0.4%, mean response cut 45% to 50%, p95 cut 57% to 65% and 3 more), none LOSS or power given; 6 gauges EVEN, inside the noise. Omni holds the knob | `results/live/V10_WANDERING.md` |
| all four at once | work inside the line up 47% to 79%, mean response cut 38% to 46%, p95 cut 56% to 61%, time over the line cut 35% to 46%, failed requests cut 9% to 14%, alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 16% to 34% | none | **write** | +39.7% | +95.3% | 6 gauges GAIN in all three of our runs (work inside the line up 47% to 79%, mean response cut 38% to 46%, p95 cut 56% to 61%, time over the line cut 35% to 46% and 2 more), none LOSS or power given; 8 gauges EVEN, inside the noise. Omni holds the knob | `results/live/V10_ALL_FOUR.md` |
| a noisy neighbour | time over the line cut 11% | none | **write** | +0.0% | +0.0% | 1 gauges GAIN in all three of our runs (time over the line cut 11%), none LOSS or power given; 16 gauges EVEN, inside the noise. Omni holds the knob | `results/live/V10_FAIRNESS.md` |
| faults | mean response cut 33% to 40%, p95 cut 54% to 63%, p99 cut 43% to 51%, time over the line cut 26% to 31% | power given: replicas up 14% to 20% | **operator's choice** | +33.6% | +138.4% | GAIN in all three of our runs: mean response cut 33% to 40%, p95 cut 54% to 63%, p99 cut 43% to 51%, time over the line cut 26% to 31%; power given in all three of our runs: replicas up 14% to 20% | `results/live/V10_FAULTS.md` |
| a queue of jobs | machines cut 6% to 14%, machine-hours cut 6% to 14%, standby-model energy cut 4.3% to 9.5%, mean response cut 10% to 12%, machines after the queue cut 10% to 22% | none | **write** | +10.2% | +12.7% | 5 gauges GAIN in all three of our runs (machines cut 6% to 14%, machine-hours cut 6% to 14%, standby-model energy cut 4.3% to 9.5%, mean response cut 10% to 12% and 1 more), none LOSS or power given; 11 gauges EVEN, inside the noise. Omni holds the knob | `results/live/V10_BATCH.md` |
| a public day of demand (Google 2011) | parked-worker energy cut 0.3% to 0.4%, standby-model energy cut 0.3% to 0.4%, mean response cut 48% to 50%, p95 cut 56% to 62%, p99 cut 38% to 51%, time over the line cut 74% to 77%, failed requests cut 15% to 18%, alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 61% to 66% | power given: pods started up 120% to 193% | **operator's choice** | +35.4% | +147.2% | GAIN in all three of our runs: parked-worker energy cut 0.3% to 0.4%, standby-model energy cut 0.3% to 0.4%, mean response cut 48% to 50%, p95 cut 56% to 62% and 4 more; power given in all three of our runs: pods started up 120% to 193% | `results/live/V10_TRACE_GOOGLE2011.md` |
| With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | mean response cut 36% to 37%, p95 cut 52% to 53%, p99 cut 57% to 61%, time over the line cut 97% to 100% | power given: parked-worker energy up 1.1% to 1.8%, standby-model energy up 1.1% to 1.8%, replicas up 1.8% to 3.1% | **operator's choice** | +27.8% | +111.6% | GAIN in all three of our runs: mean response cut 36% to 37%, p95 cut 52% to 53%, p99 cut 57% to 61%, time over the line cut 97% to 100%; power given in all three of our runs: parked-worker energy up 1.1% to 1.8%, standby-model energy up 1.1% to 1.8%, replicas up 1.8% to 3.1% | `results/live/V11_KEDA_CPU_REQUESTS.md` |
| With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | mean response cut 57%, p95 cut 72% to 74%, p99 cut 57% to 62%, time over the line cut 98% to 99%, alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) cut 100%, replicas cut 11% to 20% | power given: parked-worker energy up 1.6% to 2.2%, standby-model energy up 1.6% to 2.2% | **operator's choice** | +52.8% | +263.9% | GAIN in all three of our runs: mean response cut 57%, p95 cut 72% to 74%, p99 cut 57% to 62%, time over the line cut 98% to 99% and 2 more; power given in all three of our runs: parked-worker energy up 1.6% to 2.2%, standby-model energy up 1.6% to 2.2% | `results/live/V11_KEDA_REQUESTS.md` |

### Real database (PostgreSQL behind PgBouncer, GitHub)

The knob: the pooler's pool size (server connections).

| Workload | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| select | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_PGBENCH.md` |
| simple_update | none | power given: connections most at once up 8% to 10% | **watch** | +0.0% | +0.0% | Why: connections most at once up 8% to 10% (power given), because amendment 1's add rule ("slow, clients waiting for a server: add") fired 4 to 15 times an arm on this slow write workload and bought servers above the operator's 20, up to 36 at the peak; work, latency and CPU inside the noise, so nothing was bought for them (`docs/POSTGRES_PREREGISTRATION.md`, the second set). The rule stands as written and the verdict for this workload is to watch. | `results/live/V16_PGBENCH.md` |
| tpcb_hot | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_PGBENCH.md` |

### Real messaging (Apache Kafka, GitHub)

The knob: the consumer group's size.

| Workload | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | none | none | **watch** (not counted) |  |  | the runs disagree on consumers running (-0% to +21%); everything EVEN in all three of our runs (12 gauges inside the noise, 1 the same). Nothing is settled here, so the knob stays native until three runs agree. | `results/live/V16_KAFKA.md` |
| burst | consumers running cut 0.8% | none | **write** | +0.2% | +0.0% |  No LOSS and no power given: Omni holds the knob. | `results/live/V16_KAFKA.md` |
| heavy | consumers running cut 0.3% | none | **write** | +0.1% | +0.0% |  No LOSS and no power given: Omni holds the knob. | `results/live/V16_KAFKA.md` |
| light | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (13 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_KAFKA.md` |

### Real cache (Redis, GitHub)

The knob: the cache's memory ceiling.

| Workload | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | work inside the line up 0.8% to 1.1%, hit rate up 0.8% to 1.2% | power given: memory ceiling held up 1.9% to 2.9%, memory used up 1.4% to 2.0% | **operator's choice** (not counted) |  |  | Why: memory ceiling held up 1.9% to 2.9% (power given), because the knob itself: the ceiling grows while the cache is full and misses, so a wide working set is held instead of evicted; the memory is the price of the hit rate, declared in advance as the gauge expected to rise: the power given (`docs/REDIS_PREREGISTRATION.md`, the gauges); memory used up 1.4% to 2.0% (power given), because the memory actually used follows the ceiling: the working set the operator's 64 MB could not hold is held. | `results/live/V16_REDIS.md` |
| burst | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_REDIS.md` |
| large | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (10 gauges inside the noise, 2 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_REDIS.md` |
| small | work inside the line up 1.2% to 1.3%, hit rate up 1.2% to 1.3%, mean cut 1.7% to 1.8% | power given: memory ceiling held up 2.2% to 2.7%, memory used up 1.9% to 2.1% | **operator's choice** | -0.3% | +0.6% | Why: memory ceiling held up 2.2% to 2.7% (power given), because the knob itself: the ceiling grows while the cache is full and misses, so a wide working set is held instead of evicted; the memory is the price of the hit rate, declared in advance as the gauge expected to rise: the power given (`docs/REDIS_PREREGISTRATION.md`, the gauges); memory used up 1.9% to 2.1% (power given), because the memory actually used follows the ceiling: the working set the operator's 64 MB could not hold is held. The trade pays under the service reading (+0.6%) and not under the resource reading (-0.3%, the preregistered headline): the operator who runs Redis for its speed and has the memory wires in; the operator who counts the memory as the cost watches. | `results/live/V16_REDIS.md` |

### Real database cache (MongoDB under YCSB, GitHub)

The knob: the storage engine's cache size.

| Workload | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | none | none | **watch** (not counted) |  |  | everything EVEN in all three of our runs (10 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_YCSB.md` |
| b | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (10 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_YCSB.md` |
| burst | cache size held cut 1.7% to 2.2% | none | **write** | +0.5% | +0.0% |  No LOSS and no power given: Omni holds the knob. | `results/live/V16_YCSB.md` |
| c | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (10 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_YCSB.md` |
| f | cache size held cut 0.8% to 1.0% | none | **write** | +0.2% | +0.0% |  No LOSS and no power given: Omni holds the knob. | `results/live/V16_YCSB.md` |

### Real database buffer pool (MySQL under sysbench, GitHub)

The knob: the buffer pool's size.

| Workload | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | none | none | **watch** (not counted) |  |  | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_SYSBENCH.md` |
| burst | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_SYSBENCH.md` |
| read_only | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_SYSBENCH.md` |
| read_write | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_SYSBENCH.md` |
| update_index | none | none | **watch** | +0.0% | +0.0% | everything EVEN in all three of our runs (11 gauges inside the noise, 1 the same). EVEN under this workload: the knob stays native and Omni reads it. | `results/live/V16_SYSBENCH.md` |

## Every LOSS and every power given in all three of our runs on a real stack, and why

The founder's question was where the negatives are and why each is there. Every gauge that read LOSS or power given in all three of our runs on a real stack, with its cause read from the preregistration that carries the result:

- **Kubernetes, replicas: faults up 14% to 20%, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs up 1.8% to 3.1%, power given** (8.637 / 8.806 → 10.39 to 8.964 in run A). See the table. Verdict: **operator's choice** on every workload named.
- **Kubernetes, pods started: a public day of demand (Google 2011) up 120% to 193%, power given** (5.8 → 15.3 in run A). See the table. Verdict: **operator's choice**.
- **Kubernetes, parked-worker energy: With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs up 1.1% to 1.8%, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs up 1.6% to 2.2%, power given** (157.6 / 159 → 160.7 to 161.1 in run A). See the table. Verdict: **operator's choice** on every workload named.
- **Kubernetes, standby-model energy: With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs up 1.1% to 1.8%, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs up 1.6% to 2.2%, power given** (157.6 / 159 → 160.7 to 161.1 in run A). See the table. Verdict: **operator's choice** on every workload named.
- **PostgreSQL, connections most at once: simple_update up 8% to 10%, power given** (20 → 21.67 in run A). See the table. Verdict: **watch**.
- **Redis, memory ceiling held: small up 2.2% to 2.7%, power given** (64 → 65.39 in run A). See the table. Verdict: **operator's choice**.
- **Redis, memory used: small up 1.9% to 2.1%, power given** (60.7 → 61.85 in run A). See the table. Verdict: **operator's choice**.

What these have in common: every one is power given, a resource spent to buy the service the knob exists for (consumers and the CPU they poll with, memory, pages, connections), each declared in advance in its preregistration as the gauge expected to rise, or found on the first counted set and disclosed. None is a LOSS: on no real stack did work inside the line, p95 or failed requests read LOSS in all three of our runs. Where the resource was given and nothing was bought (PostgreSQL's `simple_update`), the verdict is watch; where it bought service, the verdict is the operator's, and both index readings say what the trade is worth.

## The independent simulators (evidence class S: deterministic models with their own native controllers)

### Robot arms (MuJoCo Menagerie, Google DeepMind)

The knob: the servo's speed override inside the takt.

| Case | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Why | Source |
|---|---|---|---|---|---|
| kinova_gen3 | energy per takt cut 0.8%, copper heating per cycle cut 11%, mechanical work per cycle cut 6.6%, peak joint torque cut 29%, tracking error, RMS cut 21%, end-point error at the waypoints cut 11% | none | **write** | No LOSS: the same job inside the same takt, hit more accurately with less force; the cycle is slower inside the takt (shown, not judged). | `results/live/V7_MUJOCO.md` |
| kuka_iiwa_14 | none | none | **watch** | The engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native). The trial's figures: 3157.3 J at full speed against 3757.3 J at the trial speed, reproduced over A, B, C: yes | `results/live/V7_MUJOCO.md` |
| universal_robots_ur5e | none | none | **watch** | The engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native). The trial's figures: 189.9 J at full speed against 210.5 J at the trial speed, reproduced over A, B, C: yes | `results/live/V7_MUJOCO.md` |

### The power grid (pandapower, SimBench grids)

The knob: the substation's voltage setpoint, one tap at a time.

| Case | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Why | Source |
|---|---|---|---|---|---|
| 1-MV-comm--0-sw (ZIP loads) | energy the loads drew cut 1.5%, energy dissipated in lines and transformers cut 1.0%, net import from the upstream grid cut 2.9%, tap operations cut 34% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-comm--1-sw (ZIP loads) | energy the loads drew cut 1.4%, energy dissipated in lines and transformers cut 0.8%, net import from the upstream grid cut 15%, tap operations cut 36% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-comm--2-sw (ZIP loads) | energy the loads drew cut 1.4%, energy dissipated in lines and transformers cut 0.3%, net import from the upstream grid cut 6.4%, tap operations cut 36% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-rural--1-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 1.4% | power given: energy dissipated in lines and transformers up 0.8%, tap operations up 100% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table); taps: the declared cost on a grid that barely taps on its own (4 a year, doubled). The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-rural--2-sw (ZIP loads) | energy the loads drew cut 1.3%, net import from the upstream grid cut 1.1%, bus-steps outside 0.95-1.05 cut 1.4e-04, tap operations cut 27% | power given: energy dissipated in lines and transformers up 1.5% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table). The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--0-sw (ZIP loads) | energy the loads drew cut 1.4%, energy dissipated in lines and transformers cut 1.0%, net import from the upstream grid cut 7.0%, tap operations cut 38% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--1-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 1.1%, tap operations cut 34% | power given: energy dissipated in lines and transformers up 0.7% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table). The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--2-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 0.9%, bus-steps outside 0.95-1.05 cut 1.4e-05, tap operations cut 24% | power given: energy dissipated in lines and transformers up 1.1% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table). The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--0-sw (ZIP loads) | energy the loads drew cut 1.5%, energy dissipated in lines and transformers cut 2.4%, net import from the upstream grid cut 2.0%, tap operations cut 31% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--1-sw (ZIP loads) | energy the loads drew cut 1.5%, energy dissipated in lines and transformers cut 2.4%, net import from the upstream grid cut 2.2%, tap operations cut 30% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--2-sw (ZIP loads) | energy the loads drew cut 1.5%, energy dissipated in lines and transformers cut 2.2%, net import from the upstream grid cut 3.1%, tap operations cut 23% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-comm--0-sw (constant-power loads) | energy dissipated in lines and transformers cut 0.5%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-comm--1-sw (constant-power loads) | energy dissipated in lines and transformers cut 0.4%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-comm--2-sw (constant-power loads) | energy dissipated in lines and transformers cut 0.0%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-rural--1-sw (constant-power loads) | none | power given: energy dissipated in lines and transformers up 0.6%, net import from the upstream grid up 0.0%, tap operations up 100% | **watch** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table); taps: the declared cost on a grid that barely taps on its own (4 a year, doubled); import: follows the line heating, hundredths of a percent. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-rural--2-sw (constant-power loads) | bus-steps outside 0.95-1.05 cut 1.4e-04, tap operations cut 16% | power given: energy dissipated in lines and transformers up 1.2%, net import from the upstream grid up 0.0% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table); import: follows the line heating, hundredths of a percent. The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--0-sw (constant-power loads) | energy dissipated in lines and transformers cut 0.9%, net import from the upstream grid cut 0.1%, tap operations cut 29% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--1-sw (constant-power loads) | tap operations cut 31% | power given: energy dissipated in lines and transformers up 0.6%, net import from the upstream grid up 0.0% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table); import: follows the line heating, hundredths of a percent. The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-semiurb--2-sw (constant-power loads) | bus-steps outside 0.95-1.05 cut 1.7e-05, tap operations cut 21% | power given: energy dissipated in lines and transformers up 0.9%, net import from the upstream grid up 0.0% | **operator's choice** | Why: line heating: an exporting grid pays the lower voltage in energy dissipated in its lines (the analysis under the table); import: follows the line heating, hundredths of a percent. The operator who wants the loads' energy and the upstream import cut wires in and gives the line heating; the operator who runs the grid to its line heating watches. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--0-sw (constant-power loads) | energy dissipated in lines and transformers cut 1.9%, net import from the upstream grid cut 0.0%, tap operations cut 30% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--1-sw (constant-power loads) | energy dissipated in lines and transformers cut 1.9%, net import from the upstream grid cut 0.0%, tap operations cut 27% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |
| 1-MV-urban--2-sw (constant-power loads) | energy dissipated in lines and transformers cut 1.8%, net import from the upstream grid cut 0.0%, tap operations cut 22% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_PANDAPOWER.md` |

**Why the line heating rose on four grids (power given).** The lower setpoint carries the grid's power at a lower voltage and therefore a higher current, and the energy dissipated in the lines rises with the square of the current. The four grids where it rose are four of the five that export more than they import (net import negative: rural 1 and 2, semiurb 1 and 2); on the importing grids the loads' own draw falls with the voltage under ZIP loads and the line heating falls with it. Under constant-power loads the loads draw the same at any voltage, so the setpoint saves nothing on the loads and the exporting grids give the line heating with nothing bought. Tap operations, declared in advance as Omni's expected cost (`docs/PANDAPOWER_PREREGISTRATION.md`): this grid barely taps on its own (4 a year), so Omni's moves double a very small count. The verdict on those four grids is the operator's: the loads' energy and the upstream import cut (GAIN) against the lines' heating up (power given); under constant-power loads on 1-MV-rural--1-sw, where nothing was bought, it is watch.

### Buildings and batteries (CityLearn, UT Austin)

The knob: the electric batteries' charge and discharge commands.

| Case | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Why | Source |
|---|---|---|---|---|---|
| ca_alameda_county_neighborhood | electricity bought cut 5.9%, daily peak draw cut 3.6%, highest peak cut 3.0%, ramping cut 3.9%, daily load unevenness cut 1.0%, monthly load unevenness cut 0.7%, distance from zero net energy cut 0.1% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2022_phase_all_robustness | electricity bill cut 8.6%, electricity bought cut 15%, carbon cut 12%, daily peak draw cut 14%, highest peak cut 2.7%, ramping cut 7.2%, daily load unevenness cut 2.9%, distance from zero net energy cut 6.1% | power given: monthly load unevenness up 0.1% | **operator's choice** | Why: the monthly load factor moved by a tenth of a percent against a bill cut 8.6%. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_local_evaluation | electricity bought cut 0.3%, carbon cut 0.2%, daily peak draw cut 1.6%, daily load unevenness cut 2.9%, distance from zero net energy cut 0.1% | LOSS: energy not served up 6.0%, time uncomfortable up 0.1%; power given: electricity bill up 0.3%, ramping up 6.2%, monthly load unevenness up 0.1% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_1 | electricity bought cut 0.1%, carbon cut 0.2%, daily peak draw cut 1.3%, highest peak cut 3.5%, daily load unevenness cut 2.0%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1% | LOSS: energy not served up 5.5%, time uncomfortable up 0.0%; power given: electricity bill up 0.3%, ramping up 5.6% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_2 | electricity bought cut 0.2%, carbon cut 0.2%, daily peak draw cut 1.3%, highest peak cut 3.5%, daily load unevenness cut 1.7%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1% | LOSS: energy not served up 6.2%, time uncomfortable up 0.1%; power given: electricity bill up 0.3%, ramping up 5.6% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_3 | electricity bought cut 0.2%, carbon cut 0.2%, daily peak draw cut 1.5%, highest peak cut 3.5%, daily load unevenness cut 2.3%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1%, time uncomfortable cut 0.0% | LOSS: energy not served up 9.8%; power given: electricity bill up 0.3%, ramping up 5.5% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_1 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.2%, daily load unevenness cut 4.0%, monthly load unevenness cut 1.2%, distance from zero net energy cut 0.0% | LOSS: energy not served up 2.0%, time uncomfortable up 0.0%; power given: electricity bill up 0.3%, highest peak up 2.5%, ramping up 4.5% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_2 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.2%, daily load unevenness cut 4.1%, monthly load unevenness cut 0.5% | LOSS: energy not served up 4.1%, time uncomfortable up 0.1%; power given: electricity bill up 0.2%, highest peak up 2.5%, ramping up 4.9%, distance from zero net energy up 0.0% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_3 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.6%, daily load unevenness cut 4.7%, monthly load unevenness cut 1.0%, distance from zero net energy cut 0.0% | LOSS: energy not served up 2.2%, time uncomfortable up 0.0%; power given: electricity bill up 0.3%, highest peak up 2.5%, ramping up 4.8% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V7_CITYLEARN.md` |
| tx_travis_county_neighborhood | electricity bought cut 3.0%, daily peak draw cut 1.9%, ramping cut 2.9%, daily load unevenness cut 1.1%, monthly load unevenness cut 0.7%, distance from zero net energy cut 0.6% | none | **write** | No LOSS and no power given: Omni holds the knob. | `results/live/V7_CITYLEARN.md` |
| baeda_3dem |  |  | **no knob** | no electric battery in the district (4 buildings, 7 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: none; reproduced: yes) | `results/live/V7_CITYLEARN.md` |
| quebec_neighborhood_with_demand_response_set_points |  |  | **no knob** | no electric battery in the district (20 buildings, 0 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: time uncomfortable +0.25%; reproduced: no) | `results/live/V7_CITYLEARN.md` |
| quebec_neighborhood_without_demand_response_set_points |  |  | **no knob** | no electric battery in the district (20 buildings, 0 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: time uncomfortable -0.28%; reproduced: no) | `results/live/V7_CITYLEARN.md` |

**Why the bill is up in the 2023 districts (power given), with the ramping and the energy not served (LOSS).** The seven 2023 challenge districts are small (3 to 6 buildings) and short (720 to 2,208 hours), and in them the energy not served and the comfort rows move, where in the county neighbourhoods they read the same: the compass steers the batteries from the district's electricity reading alone (one wire, one muscle, `docs/CITYLEARN_PREREGISTRATION.md`), flattening the draw it sees, and in these districts that leaves less in the batteries for the hours that count against the bill, the hour-to-hour ramping and the energy not served. The bill, what the battery is bought to lower, is up 0.2% to 0.4% in all three of our runs here (power given), so for the operator who pays the bill this is a watch. The cause is a reading of the tables, not yet tested on its own.

### Drone swarms (gym-pybullet-drones, University of Toronto)

The knob: the autopilot's cruise override.

| Case | GAIN in all three of our runs | LOSS or power given in all three of our runs | Verdict | Why | Source |
|---|---|---|---|---|---|
| tuning (the tuning swarm: shown, never counted) | energy per mission cut 16%, fleet energy over the window cut 16%, missions per charge at the autopilot's reserve up 19% | none | **write** (not counted) | the runs differ on closest two drones ever came (-51% to -45%), tracking error, RMS (+88% to +91%), cruise override, mean (+49%). No LOSS: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V7_SWARM.md` |
| long | energy per mission cut 20%, fleet energy over the window cut 20%, missions per charge at the autopilot's reserve up 25% | none | **write** | the runs differ on closest two drones ever came (-5.7% to -1.5%), tracking error, RMS (+92% to +93%), cruise override, mean (+52%). No LOSS: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V7_SWARM.md` |
| mixed | energy per mission cut 18%, fleet energy over the window cut 18%, missions per charge at the autopilot's reserve up 22% | none | **write** | the runs differ on closest two drones ever came (-46% to -42%), tracking error, RMS (+83% to +86%), cruise override, mean (+48% to +49%). No LOSS: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V7_SWARM.md` |
| short | energy per mission cut 7.4%, fleet energy over the window cut 7.4%, missions per charge at the autopilot's reserve up 8.0% | none | **write** | No LOSS: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V7_SWARM.md` |

## The 1,107 modelled muscles, alone on their plants (evidence class S)

Every muscle's own row, with its verdict and the reason, is in `results/WIRING_VERDICTS.csv`; the labels and figures are the v5 realms table's (`results/realms_v5/REALMS_V5.md`, `results/realms_v5/MUSCLES_V5.csv`; engine omni-v5 at the max, every muscle its own card; seeds 3000 to 3009, ten paired seeds a muscle, under its own load and under work waiting in line). The label is the muscle's over every load it ran; the Why column gives each load's own.

| Reading (the label over every load, its word first) | Muscles | Verdict |
|---|---:|---|
| EVEN (at its limit on native) | 421 | **watch** |
| GAIN (faster + fewer misses) | 345 | **write** |
| EVEN (the same as native) | 159 | **watch** |
| GAIN (faster) | 115 | **write** |
| GAIN (fewer misses) | 34 | **write** |
| GAIN (more work + faster + fewer misses) | 30 | **write** |
| GAIN (more work + faster) | 3 | **write** |

### By knob

| Knob | Muscles | Write | Watch: at its limit on native | Watch: the same as native | Of the watch, wrote nothing in any run |
|---|---:|---:|---:|---:|---:|
| capacity | 539 | 472 | 50 | 17 | 58 |
| setpoint | 174 | 44 | 0 | 130 | 111 |
| power | 119 | 11 | 96 | 12 | 96 |
| admission | 275 | 0 | 275 | 0 | 275 |

### By family

| Realm: family | Muscles | Write | Watch: at its limit on native | Watch: the same as native |
|---|---:|---:|---:|---:|
| Compute / AI / Cloud: AI Inference Serving | 24 | 15 | 9 | 0 |
| Compute / AI / Cloud: AI Training | 18 | 16 | 2 | 0 |
| Compute / AI / Cloud: Cloud VM & Capacity | 21 | 20 | 1 | 0 |
| Compute / AI / Cloud: Container Resources | 25 | 22 | 3 | 0 |
| Compute / AI / Cloud: Cross-Cluster, Multi-Region & Edge | 18 | 10 | 7 | 1 |
| Compute / AI / Cloud: DPU SmartNIC & Programmable IO | 12 | 10 | 2 | 0 |
| Compute / AI / Cloud: Distributed Cluster Managers | 15 | 8 | 7 | 0 |
| Compute / AI / Cloud: GPU Fabric & RDMA | 18 | 14 | 4 | 0 |
| Compute / AI / Cloud: HPC & Distributed Compute | 19 | 11 | 8 | 0 |
| Compute / AI / Cloud: Host CPU & Memory | 26 | 10 | 16 | 0 |
| Compute / AI / Cloud: Kubernetes Dynamic Device Allocation | 8 | 7 | 1 | 0 |
| Compute / AI / Cloud: Kubernetes Placement & Scheduling | 21 | 16 | 5 | 0 |
| Compute / AI / Cloud: Kubernetes Workload Scaling | 32 | 24 | 8 | 0 |
| Compute / AI / Cloud: GPU Hardware | 22 | 11 | 11 | 0 |
| Compute / AI / Cloud: Node Fleet & Karpenter-Class Control | 24 | 19 | 5 | 0 |
| Compute / AI / Cloud: OpenShift & Machine API | 9 | 5 | 4 | 0 |
| Compute / AI / Cloud: Quantum Computing Control Simulation | 16 | 11 | 5 | 0 |
| Compute / AI / Cloud: Work Admission & Demand Shaping | 19 | 0 | 19 | 0 |
| Distribution / Specialized: Cache & Memory Services | 16 | 12 | 4 | 0 |
| Distribution / Specialized: Commerce & Payment Systems | 15 | 7 | 8 | 0 |
| Distribution / Specialized: Data Analytics & ETL | 15 | 11 | 4 | 0 |
| Distribution / Specialized: Database & Transactions | 19 | 14 | 5 | 0 |
| Distribution / Specialized: Messaging & Streaming | 22 | 13 | 7 | 2 |
| Distribution / Specialized: Network Routing & Switching | 19 | 12 | 7 | 0 |
| Distribution / Specialized: Observability & Telemetry | 9 | 6 | 3 | 0 |
| Distribution / Specialized: Reliability, Security & Recovery | 18 | 9 | 8 | 1 |
| Distribution / Specialized: Runtime & Application | 21 | 14 | 5 | 2 |
| Distribution / Specialized: Search, Indexing & Vector DB | 16 | 10 | 6 | 0 |
| Distribution / Specialized: Service Mesh & API Reliability | 16 | 9 | 7 | 0 |
| Distribution / Specialized: Storage Block/File/Object | 20 | 17 | 3 | 0 |
| Distribution / Specialized: Telecom RAN & Edge Radio | 12 | 8 | 4 | 0 |
| Distribution / Specialized: Workflow, Logistics & Fulfillment | 15 | 10 | 5 | 0 |
| Energy / Facility / Industrial: Building & Critical Environment HVAC | 15 | 0 | 4 | 11 |
| Energy / Facility / Industrial: Cooling, Chillers & Thermodynamics | 18 | 0 | 4 | 14 |
| Energy / Facility / Industrial: Energy Storage & Microgrid | 19 | 14 | 2 | 3 |
| Energy / Facility / Industrial: Facility & Grid Optimization | 15 | 9 | 5 | 1 |
| Energy / Facility / Industrial: Grid Transmission & Distribution | 12 | 0 | 8 | 4 |
| Energy / Facility / Industrial: Industrial PLC & Process Automation | 18 | 0 | 12 | 6 |
| Energy / Facility / Industrial: PDU, UPS & Electrical Distribution | 18 | 7 | 3 | 8 |
| Energy / Facility / Industrial: Semiconductor Fab & Precision Manufacturing | 13 | 0 | 11 | 2 |
| Energy / Facility / Industrial: Water Wastewater & Pumping | 12 | 0 | 8 | 4 |
| Physics / Robotics / Autonomous: Automotive EV & Mobile Powertrain | 14 | 1 | 13 | 0 |
| Physics / Robotics / Autonomous: Aviation & Autonomous Flight | 28 | 14 | 14 | 0 |
| Physics / Robotics / Autonomous: Robotics Fleet & Warehouse Automation | 17 | 14 | 3 | 0 |
| Physics / Robotics / Autonomous: Robotics Motion Control | 26 | 19 | 5 | 2 |
| Physics / Robotics / Autonomous: Spacecraft & Flight Software | 14 | 0 | 14 | 0 |
| Energy / Facility / Industrial: Healthcare Critical Environments | 13 | 0 | 3 | 10 |
| Distribution / Specialized: Medical Imaging & Clinical Systems | 12 | 3 | 9 | 0 |
| Energy / Facility / Industrial: Agriculture & Irrigation | 14 | 0 | 4 | 10 |
| Energy / Facility / Industrial: Oil & Gas Pipelines | 14 | 0 | 6 | 8 |
| Physics / Robotics / Autonomous: Rail Traction & Train Control | 14 | 0 | 14 | 0 |
| Physics / Robotics / Autonomous: Marine Propulsion & Vessel Automation | 12 | 5 | 7 | 0 |
| Distribution / Specialized: Ports & Maritime Logistics | 12 | 6 | 6 | 0 |
| Energy / Facility / Industrial: Mining & Mineral Processing | 14 | 0 | 6 | 8 |
| Energy / Facility / Industrial: District Heating & Cooling | 13 | 0 | 6 | 7 |
| Energy / Facility / Industrial: Power Generation & Turbine Control | 14 | 0 | 4 | 10 |
| Energy / Facility / Industrial: Renewable Generation & Inverter Control | 13 | 0 | 7 | 6 |
| Physics / Robotics / Autonomous: Elevators & Vertical Transport | 12 | 0 | 12 | 0 |
| Energy / Facility / Industrial: Pharmaceutical & Food Manufacturing | 14 | 0 | 4 | 10 |
| Compute / AI / Cloud: Linux Kernel & OS Control | 20 | 9 | 3 | 8 |
| Compute / AI / Cloud: Serverless & Functions (FaaS) | 9 | 6 | 2 | 1 |
| Compute / AI / Cloud: Virtualization & Hypervisor | 9 | 6 | 2 | 1 |
| Distribution / Specialized: Content Delivery & Edge Cache | 6 | 2 | 2 | 2 |
| Compute / AI / Cloud: Gut: Data-plane Intake & Waste | 8 | 0 | 5 | 3 |
| Compute / AI / Cloud: Skin: Perimeter & Admission | 5 | 1 | 4 | 0 |
| Distribution / Specialized: Financial Markets & Trading Systems | 14 | 7 | 3 | 4 |
| Compute / AI / Cloud: Media Streaming & CDN | 14 | 5 | 4 | 5 |
| Compute / AI / Cloud: Game Servers & Real-Time Interactive | 12 | 7 | 3 | 2 |
| Compute / AI / Cloud: Blockchain & Ledger Nodes | 10 | 5 | 3 | 2 |
| Compute / AI / Cloud: CI/CD & Build Farms | 10 | 6 | 3 | 1 |

### Why the watch muscles are watch

- **421 muscles are at their limit on native.** Native already runs the knob at the top of its range: every admission knob lets everything in while change is permitted (275 admission knobs), a power knob runs the full clock or the full battery power (96 power knobs), and 50 capacity and setpoint knobs sit where native's own controller already has what the plant needs. There is nothing for the max to push; the knob is read and left native, EVEN by design, and no wire in is needed.
- **159 muscles read the same as native**: 40 of them wrote and nothing moved beyond the noise on work, speed or misses, 119 wrote nothing because native held the reading and the law had nothing to push. Watch, by rule; these are the room the next engine looks for a gain in, in the toy gate first.

### Power given, muscle by muscle

The max buys work and speed; the energy it takes is **power given**, shown beside what it bought and never a trade or a loss (the founder's order of 13 October). The write muscles whose power given on their own load is the largest:

| Muscle | Family | Knob | Reading | Misses (pp) | Work | Power given |
|---|---|---|---|---:|---:|---:|
| `db_replicas` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -5.54 | +0.27% | +104.31% |
| `io_capacity` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -6.89 | +0.35% | +96.73% |
| `read_route` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -6.31 | +0.35% | +90.41% |
| `synchronous_replication` | Database & Transactions | capacity | GAIN (fewer misses) | -3.90 | +0.39% | +89.14% |
| `payment_failover` | Commerce & Payment Systems | capacity | GAIN (more work + fewer misses) | -5.71 | +0.17% | +88.88% |
| `buffer_pool` | Database & Transactions | capacity | GAIN (fewer misses) | -3.82 | +0.23% | +88.65% |
| `placement_group` | Cloud VM & Capacity | capacity | GAIN (fewer misses) | -2.49 | +0.10% | +88.00% |
| `parallel_workers` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -3.92 | +0.24% | +87.92% |
| `pulse_duration` | Quantum Computing Control Simulation | setpoint | GAIN (fewer misses) | -0.85 | +0.00% | +86.36% |
| `interruption_response` | Cloud VM & Capacity | capacity | GAIN (fewer misses) | -2.32 | +0.14% | +83.97% |
| `multi_cluster_dispatch` | Cross-Cluster, Multi-Region & Edge | capacity | GAIN (fewer misses) | -2.39 | +0.14% | +83.95% |
| `nodepool_weight` | Node Fleet & Karpenter-Class Control | setpoint | GAIN (more work + fewer misses) | -2.99 | +0.19% | +83.62% |
| `db_failover` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -6.15 | +0.44% | +83.17% |
| `kubelet_reserved_resources` | Node Fleet & Karpenter-Class Control | capacity | GAIN (fewer misses) | -2.22 | +0.26% | +82.84% |
| `asg_min` | Cloud VM & Capacity | capacity | GAIN (fewer misses) | -1.53 | +0.01% | +82.21% |
| `runner_scale_set_max_runners` | CI/CD & Build Farms | capacity | GAIN (fewer misses) | -2.57 | +0.31% | +82.16% |
| `checkpoint_rate` | Database & Transactions | capacity | GAIN (fewer misses) | -5.18 | +0.46% | +81.95% |
| `background_writer` | Database & Transactions | capacity | GAIN (more work + fewer misses) | -3.94 | +0.26% | +81.69% |
| `pulse_phase` | Quantum Computing Control Simulation | capacity | GAIN (fewer misses) | -2.01 | +0.00% | +81.01% |
| `db_memory` | Database & Transactions | capacity | GAIN (fewer misses) | -5.32 | +0.09% | +80.86% |

Of the 527 write muscles, 523 took power for their gain on their own load and 4 took none (the gain came from timing, not from more energy). Every muscle's figure, on both loads, is in the CSV.

## The organisms

### The seven modelled organisms under three loads (every muscle written at once, one brain)

| Organism and load | Muscles | Reading | Verdict | Figures |
|---|---:|---|---|---|
| The spine, the muscles every stack runs on, the normal load | 267 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.145 pp (-0.176 to -0.115), work +0.000%, power given +0.011%; valid: yes |
| Compute / AI / Cloud, the normal load | 540 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.070 pp (-0.084 to -0.057), work +0.000%, power given +0.009%; valid: yes |
| Physics / Robotics / Autonomous, the normal load | 404 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.121 pp (-0.145 to -0.097), work +0.000%, power given +0.010%; valid: yes |
| Energy / Facility / Industrial, the normal load | 480 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.118 pp (-0.144 to -0.093), work +0.000%, power given +0.000%; valid: yes |
| Distribution / Specialized, the normal load | 484 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.067 pp (-0.082 to -0.052), work +0.000%, power given +0.002%; valid: yes |
| The four stacked, every duplicate kept, the normal load | 1908 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.092 pp (-0.106 to -0.078), work +0.000%, power given +0.000%; valid: yes |
| The whole tower, every muscle once, the normal load | 1107 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.051 pp (-0.062 to -0.040), work +0.000%, power given +0.000%; valid: yes |
| The spine, the muscles every stack runs on, the climb load | 267 muscles | GAIN (more work + fewer misses) | **write** | GAIN (more work + fewer misses): misses -0.632 pp (-0.697 to -0.567), work +0.003%, power given +0.039%; valid: yes |
| Compute / AI / Cloud, the climb load | 540 muscles | GAIN (more work + fewer misses) | **write** | GAIN (more work + fewer misses): misses -0.390 pp (-0.421 to -0.358), work +0.002%, power given +0.046%; valid: yes |
| Physics / Robotics / Autonomous, the climb load | 404 muscles | GAIN (more work + fewer misses) | **write** | GAIN (more work + fewer misses): misses -0.317 pp (-0.361 to -0.274), work +0.002%, power given +0.021%; valid: yes |
| Energy / Facility / Industrial, the climb load | 480 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.217 pp (-0.247 to -0.187), work +0.000%, power given +0.000%; valid: yes |
| Distribution / Specialized, the climb load | 484 muscles | GAIN (more work + fewer misses) | **write** | GAIN (more work + fewer misses): misses -0.460 pp (-0.489 to -0.431), work +0.003%, power given +0.026%; valid: yes |
| The four stacked, every duplicate kept, the climb load | 1908 muscles | GAIN (more work + fewer misses) | **write** | GAIN (more work + fewer misses): misses -0.349 pp (-0.370 to -0.327), work +0.002%, power given +0.000%; valid: yes |
| The whole tower, every muscle once, the climb load | 1107 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.094 pp (-0.107 to -0.082), work +0.000%, power given +0.000%; valid: yes |
| The spine, the muscles every stack runs on, the line load | 267 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.371 pp (-0.402 to -0.340), work +0.000%, power given +0.038%; valid: yes |
| Compute / AI / Cloud, the line load | 540 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.205 pp (-0.217 to -0.193), work +0.000%, power given +0.045%; valid: yes |
| Physics / Robotics / Autonomous, the line load | 404 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.250 pp (-0.275 to -0.225), work +0.000%, power given +0.030%; valid: yes |
| Energy / Facility / Industrial, the line load | 480 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.117 pp (-0.143 to -0.092), work +0.000%, power given +0.000%; valid: yes |
| Distribution / Specialized, the line load | 484 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.142 pp (-0.167 to -0.117), work +0.000%, power given +0.006%; valid: yes |
| The four stacked, every duplicate kept, the line load | 1908 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.176 pp (-0.190 to -0.163), work +0.000%, power given +0.000%; valid: yes |
| The whole tower, every muscle once, the line load | 1107 muscles | GAIN (fewer misses) | **write** | GAIN (fewer misses): misses -0.051 pp (-0.062 to -0.040), work +0.000%, power given +0.000%; valid: yes |

An organism's label is the whole's: every muscle written at once. The wiring an operator takes from this page is finer: the write muscles wired in, the watch muscles left native with one wire out. The organism result says the whole, written at once, read GAIN (fewer misses, and under the climb more work) in every organism under every load, the power given shown beside it; this page says which parts carried it.

### The organisms with the real cluster inside

The knob is the cluster's (the autoscaler's replicas, the floor and the machines), under the organism's own demand, with the modelled muscles around it. The cluster's gauges decide the verdict; the organism's modelled work and energy are shown beside them and are judged muscle by muscle above.

| Cell | Verdict | The table's reading, and the figures | Source |
|---|---|---|---|
| compute_ai_cloud at 10 copies (GitHub) | **write** | each gauge's word: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 6. The cluster's gauges: 2 GAIN (p95 -50.3%, time over the line -31.6%), 0 LOSS, 0 power given. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| physics_robotics_autonomous at 10 copies (GitHub) | **watch** | each gauge's word: GAIN on 3 (organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 8. The cluster's gauges: 0 GAIN, 0 LOSS, 0 power given. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| energy_facility_industrial at 10 copies (GitHub) | **operator's choice** | each gauge's word: GAIN on 4 (time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 6. The cluster's gauges: 1 GAIN (time over the line -32.6%), 0 LOSS, 1 power given (replicas +0.6%). The organism's modelled energy -0.3%. | `results/live/V3_SIX_KUBE.md` |
| distribution_specialized at 10 copies (GitHub) | **write** | each gauge's word: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 6. The cluster's gauges: 2 GAIN (p95 -51.7%, time over the line -35.9%), 0 LOSS, 0 power given. The organism's modelled energy -0.2%. | `results/live/V3_SIX_KUBE.md` |
| tower at 10 copies (GitHub) | **write** | each gauge's word: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 5. The cluster's gauges: 3 GAIN (p95 -41.6%, time over the line -20.1%, failed requests -8.4%), 0 LOSS, 0 power given. The organism's modelled energy -0.3%. | `results/live/V3_SIX_KUBE.md` |
| stack at 10 copies (GitHub) | **write** | each gauge's word: GAIN on 5 (time over the response line (% of samples); failed requests (%); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 6. The cluster's gauges: 2 GAIN (time over the line -12.1%, failed requests -8.5%), 0 LOSS, 0 power given. The organism's modelled work -0.0006% (6 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| compute_ai_cloud at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 4 (time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 7. The cluster's gauges: 1 GAIN (time over the line -9.8%), 0 LOSS, 0 power given. The organism's modelled work -0.0008% (8 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| physics_robotics_autonomous at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 4 (time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 7. The cluster's gauges: 1 GAIN (time over the line -8.4%), 0 LOSS, 0 power given. The organism's modelled work -0.0011% (11 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| energy_facility_industrial at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 7 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh); energy (Wh); organism work; organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 5. The cluster's gauges: 3 GAIN (time over the line -14.9%, parked-worker energy -0.3%, standby-model energy -0.3%), 0 LOSS, 0 power given. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| distribution_specialized at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); organism work; organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 6. The cluster's gauges: 2 GAIN (p95 -31.9%, time over the line -21.9%), 0 LOSS, 0 power given. The organism's modelled energy -0.2%. | `results/live/V3_SIX_KUBE.md` |
| tower at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 5 (time over the response line (% of samples); organism work; organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 0, power given on 0, EVEN (inside the noise) on 6. The cluster's gauges: 1 GAIN (time over the line -8.7%), 0 LOSS, 0 power given. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| stack at 100 copies (GitHub) | **write** | each gauge's word: GAIN on 4 (time over the response line (% of samples); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 6; OFF THE CLOCK in 3 of 5 repetitions (the organism ended up to 277 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest). The cluster's gauges: 1 GAIN (time over the line -14.6%), 0 LOSS, 0 power given. The organism's modelled work -0.0008% (8 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. Off the clock in 3 of 5 repetitions. | `results/live/V3_SIX_KUBE.md` |
| tower at 1000 copies (Azure) | **write** | each gauge's word: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 4. The cluster's gauges: 4 GAIN (p95 -97.6%, p99 -97.9%, time over the line -100.0%, failed requests -100.0%), 0 LOSS, 0 power given. The organism's modelled work -0.0004% (4 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_BIG_ORGANISM.md` |
| stack at 1000 copies (Azure) | **write** | each gauge's word: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism energy (J); organism time over the line (% of steps); organism work per energy), LOSS on 1 (organism work), power given on 0, EVEN (inside the noise) on 3. The cluster's gauges: 4 GAIN (p95 -94.8%, p99 -96.9%, time over the line -100.0%, failed requests -100.0%), 0 LOSS, 0 power given. The organism's modelled work -0.0006% (6 parts in a million, rounding level) (LOSS or power given) is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_BIG_ORGANISM.md` |

## Not decided here

- **Azure's managed Kubernetes (the bill):** the two tables are on Omni v1 (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`) on a 4-worker fleet, where every gauge read EVEN, no difference beyond the noise, but the burst's p99 in one run. A fleet too small to show one machine decides nothing; the fleet that can (`docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine) decides this knob on v3 when it runs. Until then the verdict on Azure is watch, for want of a result rather than because of one.
- **The card (NVIDIA, its own meter):** every earlier card result is obsolete; the current governor has not run on a real card. Nothing to decide yet.
- **The 24-hour robustness machines:** running; they test the governor's own staying power, not a knob's value.

## What this means for the wiring

The two-way plug stays one wire in and one wire out (`docs/WIRING_GUIDE.md`). This page decides, per knob, whether the wire in is connected. A knob marked **write** is wired both ways. A knob marked **watch** is wired out only: Omni reads it, learns from it, and never writes it; the native controller lives by itself. A knob marked **operator's choice** is wired out, and in only by the operator who wants that trade. The engine's verdict (`omnicompass/verdict.py`) does the same on the muscle itself at run time, and a knob it has left native is a watch knob whatever this page says. Nothing on this page changes the engine, which stays Omni v3; it changes what an operator connects.

## The same verdict, live: the brain decides on the knob before it writes

This page judges after the fact, from published tables. The founder's order of 9 October is that the brain judge in real time, on the knob, before it writes, and that a knob which cannot prove it pays stay native. On the five live stacks (the pool, the consumer group, the memory ceiling, the storage-engine cache, the buffer pool) that is now built into the harnesses: `tools/knob_verdict.py` wraps the frozen engine's own verdict (`omnicompass/verdict.py`, unchanged) around every live knob. The knob starts in watch; a paired trial on the stack itself (the knob held at the deepest step already allowed, then one notch further, under the same traffic) allows one notch at a time under the declared objective, the resource reading of the index by default or the service reading at the operator's choice; a refused step is not taken and not retried for a minute; a trial holds the knob; a fail-up never spends beyond the allowance; the operator's setting is always free. The audit carries the cost sample and the verdict's state every second, the arm record sums it, and the three-run tables print the verdict per workload. It is declared as an amendment in each of the five preregistrations with the expectation written before the runs (Redis: left native under the resource objective; Kafka: allowed step by step while each consumer pays; PostgreSQL: the add above the operator's setting refused on `simple_update`; MySQL: the `read_write` chunks refused; MongoDB: the cache given back a notch a trial). The runs on it were dispatched on 10 October 2026 (`docs/RERUN_2026-10-10.md`); this page is then read again from their tables. Inside the modelled realms the organism still takes one directive for every muscle; the verdict per muscle there is the next engine, Omni v4, designed in `docs/OMNI_V4_PLAN.md` and not built.

**Where the brain's verdict stands today, knob by knob.** Who decides, in real time, whether a knob pays before it is written, and in which directions (spend: more resource for service; give back: less resource where the service holds):

| Where | The knob | Who decides it pays, and when | Directions tried | Engine |
|---|---|---|---|---|
| The five live stacks: Redis's memory ceiling, Kafka's consumers, PostgreSQL's pool, MySQL's buffer pool, MongoDB's cache | one knob each | `tools/knob_verdict.py` around the engine's verdict: the knob starts in watch; a paired trial on the stack itself before every notch, one notch a trial, under the declared objective | spend and give back, both tried; the operator's setting always free | outside the engine (Omni v3 unchanged); running since 10 October |
| Kubernetes: the machines | nodes in service | the engine's verdict (`omnicompass/verdict.py`): a paired trial before a machine is taken | give back (a machine taken only when the trial shows the service holds); gas and brake on replicas and the floor by the compass law's band, no trial | Omni v3 |
| The card: the clock ceiling | one 15 MHz step at a time | the engine's verdict: a paired trial per step while the service is calm; no step passing, the card runs as it does alone; the power lid stays at the operator's | give back (slower clock for the same service); the speed floor never under the card's own busy clock | Omni v3 (`omni_controller/gpu_compass.py`) |
| Robot arms: the speed override; drones: the cruise | one knob each | the engine's verdict on the robot and the swarm; two of four robots left native by it | give back | Omni v3 |
| Power grids: the tap; buildings: the batteries | one knob each | the compass law alone, no trial; the trades on four exporting grids and seven 2023 districts are read from the tables above as the operator's choice | the law's own push and pull | Omni v3 (a trial there is the next engine) |
| The 1,107 modelled muscles | each muscle's knob | the max on every muscle, every muscle its own card; the knobs native already runs at the top of their range read and left native | the law's own push and pull | Omni v5 at the max (the law omni-v6 carries), `docs/OMNI_V5.md` |
| The machine itself: the Linux kernel's frequency ceiling (`docs/CPU_POWER_PREREGISTRATION.md`) | one knob | `tools/knob_verdict.py` around the engine's verdict: every notch down tried on the machine first, under the index's reading for one machine (energy x latency / work) or energy per request inside the line | give back only (the ceiling cannot go above the top; the top always free) | outside the engine; built 10 October, waiting for a machine on the metal, no run yet |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
