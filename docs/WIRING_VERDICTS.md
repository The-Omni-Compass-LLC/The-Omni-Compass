# Wire in, or watch: the verdict per knob, from every result in the repository

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Omni-Compass is wired **out of** every muscle: it reads every reading. It is wired **into** a knob only where the paired measurement shows the muscle no worse for it. Where the measurement shows nothing, or shows a loss, the muscle stays native and Omni only watches it: one wire out, no wire in. This is not a new rule. It is what the engine does on the muscle itself before it moves anything (`omnicompass/verdict.py`: the paired trial, and the verdict **left native** where no step is allowed), and it is the watch arm of every realms run (`docs/REALMS_PREREGISTRATION.md`: the governor reads every period and writes nothing). This page applies the same principle to every published result, one verdict per knob, so that an operator can see which knobs earn a wire in and which stay native. The founder's order of 9 October 2026: where Omni cannot beat native, the muscle lives by itself; we only wire out of it.

Every verdict here is computed by `tools/wiring_verdicts.py` from the test's own result file; nothing is typed in, and `verify.py` fails if this page differs from what the tables give. One row per knob and case: `results/WIRING_VERDICTS.csv` (1035 rows, the 945 modelled muscles included one by one).

## The rule

Every judged gauge of a table counts (rows marked "shown, not judged" never do). Every change on this page is said in words, never by a bare sign: a gauge that fell when falling is good reads **cut** (less waiting, fewer machines, less energy, less memory), one that rose when rising is good reads **up**, and each carries **good** or **cost**. In the result tables the same change keeps its raw sign (a cut reads minus there), with the Reading column beside it saying which way is good. A knob reads:

- **write**: at least one gauge confirmed better over all three runs and none confirmed worse. Omni holds the knob.
- **watch**: nothing confirmed better. The knob stays native; Omni reads it and writes nothing. Where a gauge is confirmed worse, the loss is named and its cause given below. Where the runs disagree, nothing is settled and the knob stays native until it is.
- **operator's choice**: gains and losses both confirmed, a trade. Both readings of the Omni index are shown where the test is in it (the resource reading, the preregistered headline, and the service reading, work and speed alone), and the side that pays is named. The operator who wants the gain and can pay the cost wires in; every other operator watches.

A modelled muscle (the 945 on their plants, `results/realms/MUSCLES.csv`) takes its verdict from its label by rule: SUPERIOR WITHIN GUARDRAILS is write; ENERGY IMPROVEMENT WITH SERVICE TRADEOFF and SERVICE IMPROVEMENT WITH ENERGY TRADEOFF are operator's choice; NONINFERIOR / INCONCLUSIVE, NOT ESTABLISHED and WORSE are watch.

## The count

| Where | Knobs or cases | Write | Operator's choice | Watch |
|---|---:|---:|---:|---:|
| Real stacks, three runs each (Kubernetes under seven demands; the pool, the consumer group, the memory ceiling, the storage-engine cache and the buffer pool, each under its untouched workloads) | 24 | 10 | 0 | 14 |
| Independent simulators, three runs each (robot arms, grids, districts, swarms; evidence class S) | 39 | 21 | 15 | 3 |
| The 945 modelled muscles, alone on their plants (evidence class S) | 945 | 124 | 13 | 808 |
| The organisms with the real cluster inside (GitHub at 10 and 100 copies; Azure at 1,000) | 14 | 12 | 1 | 1 |

In words: on the real stacks Omni earns its wire in on 10 of 24 knob-cases, trades on 0 and watches on 14. Of the 945 modelled muscles, 124 earn a wire in, 13 are trades and 808 stay native: 746 of the 808 wrote nothing in any run, because the native controller already held the reading inside the band and the law never left its cushion. A knob that never writes costs nothing and earns nothing; it needs no wire in, and the page below says so muscle by muscle.

## The real stacks (evidence class L: live software, three separate GitHub runs on the frozen engine)

The reading of every judged gauge is in the test's own table (the Source column). The index columns are the two readings of `results/OMNI_INDEX.md` for that test, where it has one.

### Real Kubernetes: one knob under seven demands

The knob: the autoscaler's replicas, the floor and the machines, on top of the Horizontal Pod Autoscaler (kind clusters on GitHub, ten pairs a run).

| Demand | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| steady work | machines cut 1.7% to 2.0%, machine-hours cut 1.7% to 2.0%, standby-model energy cut 1.3% to 1.8%, mean response cut 47% to 48%, p95 cut 64% to 66%, p99 cut 69% to 73%, time over the line cut 97% to 99% | none | **write** | +30.5% | +68.8% | confirmed better on 7 gauges, nothing confirmed worse; 5 gauges inside the noise. Omni holds the knob | `results/live/V3_STEADY.md` |
| demand that wanders | parked-worker energy cut 0.1% to 0.4%, mean response cut 45% to 50%, p95 cut 56% to 64%, time over the line cut 36% to 42%, failed requests cut 12% to 13% | none | **write** | +37.0% | +156.5% | confirmed better on 5 gauges, nothing confirmed worse; 8 gauges inside the noise. Omni holds the knob | `results/live/V3_WANDERING.md` |
| all four at once | work inside the line up 54% to 68%, mean response cut 43% to 48%, p95 cut 57% to 62%, time over the line cut 38% to 41%, failed requests cut 11% to 14% | none | **write** | +41.7% | +100.9% | confirmed better on 5 gauges, nothing confirmed worse; 9 gauges inside the noise. Omni holds the knob | `results/live/V3_ALL_FOUR.md` |
| a noisy neighbour | none | none | **watch** | +0.0% | +0.0% | every judged gauge inside the noise or the same (16 inside the noise, 3 the same), the neighbour's own rows included: Omni neither helped nor hurt beside a noisy neighbour, so under this demand there is nothing to earn and nothing lost. The same knob writes under the other six demands | `results/live/V3_FAIRNESS.md` |
| faults | mean response cut 34% to 51%, p95 cut 58% to 63%, time over the line cut 27% to 43%, failed requests cut 14% to 18% | none | **write** | +36.6% | +154.8% | confirmed better on 4 gauges, nothing confirmed worse; 9 gauges inside the noise. Omni holds the knob | `results/live/V3_FAULTS.md` |
| a queue of jobs | machines cut 16% to 20%, machine-hours cut 16% to 20%, standby-model energy cut 11% to 14%, mean response cut 11% to 13%, machines after the queue cut 26% to 33% | none | **write** | +16.5% | +14.1% | confirmed better on 5 gauges, nothing confirmed worse; 10 gauges inside the noise. Omni holds the knob | `results/live/V3_BATCH.md` |
| a public day of demand (Google 2011) | machines cut 7.3% to 9.2%, machine-hours cut 7.4% to 9.2%, parked-worker energy cut 0.3% to 0.4%, standby-model energy cut 5.3% to 6.7%, mean response cut 51% to 53%, p95 cut 64% to 66%, p99 cut 60% to 62%, time over the line cut 81% to 82%, failed requests cut 11% to 18%, replicas cut 3.8% to 8.3% | none | **write** | +46.4% | +187.5% | confirmed better on 10 gauges, nothing confirmed worse; 3 gauges inside the noise. Omni holds the knob | `results/live/V3_TRACE_GOOGLE2011.md` |

### Real database (PostgreSQL behind PgBouncer, GitHub)

The knob: the pooler's pool size (server connections).

| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| select | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_PGBENCH.md` |
| simple_update | none | connections most at once up 8% to 12% | **watch** | +0.0% | +0.0% | the runs disagree on connections held open (-4.0% to +2.2%). Why: connections most at once up 8% to 12%: cost, because amendment 1's add rule ("slow, clients waiting for a server: add") fired 4 to 15 times an arm on this slow write workload and bought servers above the operator's 20, up to 36 at the peak; work, latency and CPU inside the noise, so nothing was bought for them (`docs/POSTGRES_PREREGISTRATION.md`, the second set). The rule stands as written and the verdict for this workload is to watch. | `results/live/V3_PGBENCH.md` |
| tpcb_hot | connections held open cut 7% to 13% | none | **write** | +2.8% | +0.0% |  Nothing worse: Omni holds the knob. | `results/live/V3_PGBENCH.md` |

### Real messaging (Apache Kafka, GitHub)

The knob: the consumer group's size.

| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | consumers running cut 0.3% | none | **write** (not counted) |  |  |  Nothing worse: Omni holds the knob. | `results/live/V3_KAFKA.md` |
| burst | consumers running cut 0.8% | none | **write** | +0.2% | +0.0% |  Nothing worse: Omni holds the knob. | `results/live/V3_KAFKA.md` |
| heavy | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (13 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_KAFKA.md` |
| light | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (13 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_KAFKA.md` |

### Real cache (Redis, GitHub)

The knob: the cache's memory ceiling.

| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | work inside the line up 4.4% to 4.9%, hit rate up 4.4% to 5.0%, mean cut 14% to 16% | memory ceiling held up 19% to 26%, memory used up 16% to 21% | **operator's choice** (not counted) |  |  | Why: memory ceiling held up 19% to 26%: cost, because the knob itself: the ceiling grows while the cache is full and misses, so a wide working set is held instead of evicted; the memory is the price of the hit rate, declared in advance as the cost that reads worse (`docs/REDIS_PREREGISTRATION.md`, the gauges); memory used up 16% to 21%: cost, because the memory actually used follows the ceiling: the working set the operator's 64 MB could not hold is held. | `results/live/V3_REDIS.md` |
| burst | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_REDIS.md` |
| large | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (10 gauges inside the noise, 2 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_REDIS.md` |
| small | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_REDIS.md` |

### Real database cache (MongoDB under YCSB, GitHub)

The knob: the storage engine's cache size.

| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | none | none | **watch** (not counted) |  |  | the runs disagree on p95 (-0.3% to +2.1%); nothing confirmed either way (9 gauges inside the noise, 1 the same). Nothing is settled here, so the knob stays native until three runs agree. | `results/live/V3_YCSB.md` |
| b | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (10 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_YCSB.md` |
| burst | cache size held cut 10% to 13%, cache in use cut 10% to 13% | none | **write** | +3.1% | +0.0% |  Nothing worse: Omni holds the knob. | `results/live/V3_YCSB.md` |
| c | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (10 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_YCSB.md` |
| f | cache size held cut 13% to 15%, cache in use cut 12% to 14% | none | **write** | +3.7% | +0.0% |  Nothing worse: Omni holds the knob. | `results/live/V3_YCSB.md` |

### Real database buffer pool (MySQL under sysbench, GitHub)

The knob: the buffer pool's size.

| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |
|---|---|---|---|---:|---:|---|---|
| tuning (tuning workload: shown, never counted) | none | none | **watch** (not counted) |  |  | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_SYSBENCH.md` |
| burst | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_SYSBENCH.md` |
| read_only | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_SYSBENCH.md` |
| read_write | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_SYSBENCH.md` |
| update_index | none | none | **watch** | +0.0% | +0.0% | nothing confirmed either way (11 gauges inside the noise, 1 the same). Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it. | `results/live/V3_SYSBENCH.md` |

## Every confirmed loss on a real stack, and why

The founder's question was where the negatives are and why each is there. Every gauge confirmed worse on a real stack, with its cause read from the preregistration that carries the result:

- **PostgreSQL, connections most at once: simple_update up 8% to 12%, a cost** (20 → 21.67 in run A). Amendment 1's add rule ("slow, clients waiting for a server: add") fired 4 to 15 times an arm on this slow write workload and bought servers above the operator's 20, up to 36 at the peak; work, latency and CPU inside the noise, so nothing was bought for them (`docs/POSTGRES_PREREGISTRATION.md`, the second set). The rule stands as written and the verdict for this workload is to watch. Verdict: **watch**.

What the losses have in common: every one is a resource spent to buy the service the knob exists for (consumers and the CPU they poll with, memory, pages, connections), and each was declared in advance in its preregistration as the cost that would read worse, or found on the first counted set and disclosed. None is a service loss: on no real stack did work inside the line, p95 or failed requests read confirmed worse. Where the resource was spent and nothing was bought (PostgreSQL's `simple_update`), the verdict is watch; where it bought service, the verdict is the operator's, and both index readings say what the trade is worth.

## The independent simulators (evidence class S: deterministic models with their own native controllers)

### Robot arms (MuJoCo Menagerie, Google DeepMind)

The knob: the servo's speed override inside the takt.

| Case | Confirmed better | Confirmed worse | Verdict | Why | Source |
|---|---|---|---|---|---|
| kinova_gen3 | energy per takt cut 0.8%, copper loss per cycle cut 11%, mechanical work per cycle cut 6.6%, peak joint torque cut 29%, tracking error, RMS cut 21%, end-point error at the waypoints cut 11% | none | **write** | Nothing worse: the same job inside the same takt, hit more accurately with less force; the cycle is slower inside the takt (shown, not judged). | `results/live/V3_MUJOCO.md` |
| kuka_iiwa_14 | none | none | **watch** | The engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native). The trial's figures: 3157.3 J at full speed against 3757.3 J at the trial speed, reproduced over A, B, C: yes | `results/live/V3_MUJOCO.md` |
| universal_robots_ur5e | none | none | **watch** | The engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native). The trial's figures: 189.9 J at full speed against 210.5 J at the trial speed, reproduced over A, B, C: yes | `results/live/V3_MUJOCO.md` |

### The power grid (pandapower, SimBench grids)

The knob: the substation's voltage setpoint, one tap at a time.

| Case | Confirmed better | Confirmed worse | Verdict | Why | Source |
|---|---|---|---|---|---|
| 1-MV-comm--0-sw (ZIP loads) | energy the loads drew cut 1.5%, line and transformer losses cut 1.0%, net import from the upstream grid cut 2.9%, tap operations cut 34% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-comm--1-sw (ZIP loads) | energy the loads drew cut 1.4%, line and transformer losses cut 0.8%, net import from the upstream grid cut 15%, tap operations cut 36% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-comm--2-sw (ZIP loads) | energy the loads drew cut 1.4%, line and transformer losses cut 0.3%, net import from the upstream grid cut 6.4%, tap operations cut 36% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-rural--1-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 1.4% | line and transformer losses up 0.8%, tap operations up 100% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table); taps: the declared cost on a grid that barely taps on its own (4 a year, doubled). The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-rural--2-sw (ZIP loads) | energy the loads drew cut 1.3%, net import from the upstream grid cut 1.1%, bus-steps outside 0.95-1.05 up -1.4e-04, tap operations cut 27% | line and transformer losses up 1.5% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table). The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--0-sw (ZIP loads) | energy the loads drew cut 1.4%, line and transformer losses cut 1.0%, net import from the upstream grid cut 7.0%, tap operations cut 38% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--1-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 1.1%, tap operations cut 34% | line and transformer losses up 0.7% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table). The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--2-sw (ZIP loads) | energy the loads drew cut 1.4%, net import from the upstream grid cut 0.9%, bus-steps outside 0.95-1.05 up -1.4e-05, tap operations cut 24% | line and transformer losses up 1.1% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table). The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--0-sw (ZIP loads) | energy the loads drew cut 1.5%, line and transformer losses cut 2.4%, net import from the upstream grid cut 2.0%, tap operations cut 31% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--1-sw (ZIP loads) | energy the loads drew cut 1.5%, line and transformer losses cut 2.4%, net import from the upstream grid cut 2.2%, tap operations cut 30% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--2-sw (ZIP loads) | energy the loads drew cut 1.5%, line and transformer losses cut 2.2%, net import from the upstream grid cut 3.1%, tap operations cut 23% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-comm--0-sw (constant-power loads) | line and transformer losses cut 0.5%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-comm--1-sw (constant-power loads) | line and transformer losses cut 0.4%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-comm--2-sw (constant-power loads) | line and transformer losses cut 0.0%, net import from the upstream grid cut 0.0%, tap operations cut 31% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-rural--1-sw (constant-power loads) | none | line and transformer losses up 0.6%, net import from the upstream grid up 0.0%, tap operations up 100% | **watch** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table); taps: the declared cost on a grid that barely taps on its own (4 a year, doubled); import: follows the losses, hundredths of a percent. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-rural--2-sw (constant-power loads) | bus-steps outside 0.95-1.05 up -1.4e-04, tap operations cut 16% | line and transformer losses up 1.2%, net import from the upstream grid up 0.0% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table); import: follows the losses, hundredths of a percent. The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--0-sw (constant-power loads) | line and transformer losses cut 0.9%, net import from the upstream grid cut 0.1%, tap operations cut 29% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--1-sw (constant-power loads) | tap operations cut 31% | line and transformer losses up 0.6%, net import from the upstream grid up 0.0% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table); import: follows the losses, hundredths of a percent. The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-semiurb--2-sw (constant-power loads) | bus-steps outside 0.95-1.05 up -1.7e-05, tap operations cut 21% | line and transformer losses up 0.9%, net import from the upstream grid up 0.0% | **operator's choice** | Why: losses: an exporting grid pays the lower voltage in line losses (the analysis under the table); import: follows the losses, hundredths of a percent. The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--0-sw (constant-power loads) | line and transformer losses cut 1.9%, net import from the upstream grid cut 0.0%, tap operations cut 30% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--1-sw (constant-power loads) | line and transformer losses cut 1.9%, net import from the upstream grid cut 0.0%, tap operations cut 27% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |
| 1-MV-urban--2-sw (constant-power loads) | line and transformer losses cut 1.8%, net import from the upstream grid cut 0.0%, tap operations cut 22% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_PANDAPOWER.md` |

**Why the losses rose on four grids.** The lower setpoint carries the grid's power at a lower voltage and therefore a higher current, and line losses rise with the square of the current. The four grids where losses rose are four of the five that export more than they import (net import negative: rural 1 and 2, semiurb 1 and 2); on the importing grids the loads' own draw falls with the voltage under ZIP loads and losses fall with it. Under constant-power loads the loads draw the same at any voltage, so the setpoint saves nothing on the loads and the exporting grids pay the losses with nothing bought. Tap operations, declared in advance as Omni's expected cost (`docs/PANDAPOWER_PREREGISTRATION.md`): this grid barely taps on its own (4 a year), so Omni's moves double a very small count. The verdict on those four grids is the operator's: the loads' energy and the upstream import down against the lines' losses up; under constant-power loads on 1-MV-rural--1-sw, where nothing was bought, it is watch.

### Buildings and batteries (CityLearn, UT Austin)

The knob: the electric batteries' charge and discharge commands.

| Case | Confirmed better | Confirmed worse | Verdict | Why | Source |
|---|---|---|---|---|---|
| ca_alameda_county_neighborhood | electricity bought cut 5.9%, daily peak draw cut 3.6%, highest peak cut 3.0%, ramping cut 3.9%, daily load unevenness cut 1.0%, monthly load unevenness cut 0.7%, distance from zero net energy cut 0.1% | none | **write** | Nothing worse: Omni holds the knob. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2022_phase_all_robustness | electricity bill cut 8.6%, electricity bought cut 15%, carbon cut 12%, daily peak draw cut 14%, highest peak cut 2.7%, ramping cut 7.2%, daily load unevenness cut 2.9%, distance from zero net energy cut 6.1% | monthly load unevenness up 0.1% | **operator's choice** | Why: the monthly load factor moved by a tenth of a percent against a bill 8.6% lower. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_local_evaluation | electricity bought cut 0.3%, carbon cut 0.2%, daily peak draw cut 1.6%, daily load unevenness cut 2.9%, distance from zero net energy cut 0.1% | electricity bill up 0.3%, ramping up 6.2%, monthly load unevenness up 0.1%, energy not served up 6.0%, time uncomfortable up 0.1% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_1 | electricity bought cut 0.1%, carbon cut 0.2%, daily peak draw cut 1.3%, highest peak cut 3.5%, daily load unevenness cut 2.0%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1% | electricity bill up 0.3%, ramping up 5.6%, energy not served up 5.5%, time uncomfortable up 0.0% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_2 | electricity bought cut 0.2%, carbon cut 0.2%, daily peak draw cut 1.3%, highest peak cut 3.5%, daily load unevenness cut 1.7%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1% | electricity bill up 0.3%, ramping up 5.6%, energy not served up 6.2%, time uncomfortable up 0.1% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_2_online_evaluation_3 | electricity bought cut 0.2%, carbon cut 0.2%, daily peak draw cut 1.5%, highest peak cut 3.5%, daily load unevenness cut 2.3%, monthly load unevenness cut 1.9%, distance from zero net energy cut 0.1%, time uncomfortable cut 0.0% | electricity bill up 0.3%, ramping up 5.5%, energy not served up 9.8% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_1 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.2%, daily load unevenness cut 4.0%, monthly load unevenness cut 1.2%, distance from zero net energy cut 0.0% | electricity bill up 0.3%, highest peak up 2.5%, ramping up 4.5%, energy not served up 2.0%, time uncomfortable up 0.0% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_2 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.2%, daily load unevenness cut 4.1%, monthly load unevenness cut 0.5% | electricity bill up 0.2%, highest peak up 2.5%, ramping up 4.9%, distance from zero net energy up 0.0%, energy not served up 4.1%, time uncomfortable up 0.1% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| citylearn_challenge_2023_phase_3_3 | electricity bought cut 0.1%, carbon cut 0.1%, daily peak draw cut 2.6%, daily load unevenness cut 4.7%, monthly load unevenness cut 1.0%, distance from zero net energy cut 0.0% | electricity bill up 0.3%, highest peak up 2.5%, ramping up 4.8%, energy not served up 2.2%, time uncomfortable up 0.0% | **operator's choice** | Why: the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table). By rule a trade; by what the battery is for (the bill), a watch. | `results/live/V3_CITYLEARN.md` |
| tx_travis_county_neighborhood | electricity bought cut 3.0%, daily peak draw cut 1.9%, ramping cut 2.9%, daily load unevenness cut 1.1%, monthly load unevenness cut 0.7%, distance from zero net energy cut 0.6% | none | **write** | the runs differ on time uncomfortable (+0.0%). Nothing worse: Omni holds the knob. | `results/live/V3_CITYLEARN.md` |
| vt_chittenden_county_neighborhood | electricity bought cut 2.1%, daily peak draw cut 0.8%, ramping cut 1.3%, daily load unevenness cut 0.3%, monthly load unevenness cut 0.2%, distance from zero net energy cut 0.3% | none | **write** | the runs differ on time uncomfortable (+0.0%). Nothing worse: Omni holds the knob. | `results/live/V3_CITYLEARN.md` |
| baeda_3dem |  |  | **no knob** | no electric battery in the district (4 buildings, 7 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: none; reproduced: yes) | `results/live/V3_CITYLEARN.md` |
| quebec_neighborhood_with_demand_response_set_points |  |  | **no knob** | no electric battery in the district (20 buildings, 0 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: time uncomfortable +0.09%; reproduced: no) | `results/live/V3_CITYLEARN.md` |
| quebec_neighborhood_without_demand_response_set_points |  |  | **no knob** | no electric battery in the district (20 buildings, 0 water tanks left native): there is nothing for Omni to hold, so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation (scores that differ in A: time uncomfortable +0.18%; reproduced: no) | `results/live/V3_CITYLEARN.md` |

**Why the 2023 districts read worse on the bill.** The seven 2023 challenge districts are small (3 to 6 buildings) and short (720 to 2,208 hours), and in them the energy not served and the comfort rows move, where in the county neighbourhoods they read the same: the compass steers the batteries from the district's electricity reading alone (one wire, one muscle, `docs/CITYLEARN_PREREGISTRATION.md`), flattening the draw it sees, and in these districts that leaves less in the batteries for the hours that count against the bill, the hour-to-hour ramping and the energy not served. The bill, what the battery is bought to lower, is confirmed worse here by 0.2% to 0.4%, so for the operator who pays the bill this is a watch. The cause is a reading of the tables, not yet tested on its own.

### Drone swarms (gym-pybullet-drones, University of Toronto)

The knob: the autopilot's cruise override.

| Case | Confirmed better | Confirmed worse | Verdict | Why | Source |
|---|---|---|---|---|---|
| tuning (the tuning swarm: shown, never counted) | energy per mission cut 16%, fleet energy over the window cut 16%, missions per charge at the autopilot's reserve up 19% | none | **write** (not counted) | the runs differ on closest two drones ever came (-51% to -45%), tracking error, RMS (+88% to +91%), cruise override, mean (+49%). Nothing worse: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V3_SWARM.md` |
| long | energy per mission cut 20%, fleet energy over the window cut 20%, missions per charge at the autopilot's reserve up 25% | none | **write** | the runs differ on closest two drones ever came (-5.7% to -1.5%), tracking error, RMS (+92% to +93%), cruise override, mean (+52%). Nothing worse: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V3_SWARM.md` |
| mixed | energy per mission cut 18%, fleet energy over the window cut 18%, missions per charge at the autopilot's reserve up 22% | none | **write** | the runs differ on closest two drones ever came (-46% to -42%), tracking error, RMS (+83% to +86%), cruise override, mean (+48% to +49%). Nothing worse: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V3_SWARM.md` |
| short | energy per mission cut 7.4%, fleet energy over the window cut 7.4%, missions per charge at the autopilot's reserve up 8.0% | none | **write** | the runs differ on closest two drones ever came (-49% to -26%). Nothing worse: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved. | `results/live/V3_SWARM.md` |

## The 945 modelled muscles, alone on their plants (evidence class S)

Every muscle's own row, with its verdict and the reason, is in `results/WIRING_VERDICTS.csv`; the labels and intervals are the realms table's (`results/realms/REALMS.md`, `results/realms/MUSCLES.csv`; seeds 3000 to 3009, ten paired seeds a muscle).

| Label (by rule) | Muscles | Verdict |
|---|---:|---|
| NONINFERIOR / INCONCLUSIVE | 807 | **watch** |
| SUPERIOR WITHIN GUARDRAILS | 124 | **write** |
| ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | 9 | **operator's choice** |
| SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | 4 | **operator's choice** |
| NOT ESTABLISHED | 1 | **watch** |

### By knob

| Knob | Muscles | Write | Operator's choice | Watch | Of the watch, wrote nothing in any run |
|---|---:|---:|---:|---:|---:|
| capacity | 454 | 19 | 0 | 435 | 392 |
| setpoint | 134 | 82 | 8 | 44 | 37 |
| power | 102 | 23 | 5 | 74 | 62 |
| admission | 255 | 0 | 0 | 255 | 255 |

### By family

| Realm: family | Muscles | Write | Operator's choice | Watch | Wrote nothing |
|---|---:|---:|---:|---:|---:|
| Compute / AI / Cloud: AI Inference Serving | 24 | 1 | 0 | 23 | 23 |
| Compute / AI / Cloud: AI Training | 18 | 1 | 0 | 17 | 17 |
| Compute / AI / Cloud: Cloud VM & Capacity | 21 | 0 | 0 | 21 | 21 |
| Compute / AI / Cloud: Container Resources | 23 | 0 | 0 | 23 | 23 |
| Compute / AI / Cloud: Cross-Cluster, Multi-Region & Edge | 15 | 0 | 0 | 15 | 14 |
| Compute / AI / Cloud: DPU SmartNIC & Programmable IO | 12 | 0 | 0 | 12 | 12 |
| Compute / AI / Cloud: Distributed Cluster Managers | 15 | 0 | 0 | 15 | 15 |
| Compute / AI / Cloud: GPU Fabric & RDMA | 18 | 0 | 0 | 18 | 18 |
| Compute / AI / Cloud: HPC & Distributed Compute | 19 | 2 | 0 | 17 | 17 |
| Compute / AI / Cloud: Host CPU & Memory | 23 | 11 | 1 | 11 | 11 |
| Compute / AI / Cloud: Kubernetes Dynamic Device Allocation | 8 | 0 | 0 | 8 | 8 |
| Compute / AI / Cloud: Kubernetes Placement & Scheduling | 20 | 0 | 0 | 20 | 20 |
| Compute / AI / Cloud: Kubernetes Workload Scaling | 31 | 0 | 0 | 31 | 31 |
| Compute / AI / Cloud: NVIDIA GPU Hardware | 19 | 6 | 0 | 13 | 13 |
| Compute / AI / Cloud: Node Fleet & Karpenter-Class Control | 24 | 0 | 0 | 24 | 24 |
| Compute / AI / Cloud: OpenShift & Machine API | 9 | 0 | 0 | 9 | 9 |
| Compute / AI / Cloud: Quantum Computing Control Simulation | 16 | 0 | 0 | 16 | 16 |
| Compute / AI / Cloud: Work Admission & Demand Shaping | 19 | 0 | 0 | 19 | 19 |
| Distribution / Specialized: Cache & Memory Services | 16 | 0 | 0 | 16 | 16 |
| Distribution / Specialized: Commerce & Payment Systems | 15 | 0 | 0 | 15 | 15 |
| Distribution / Specialized: Data Analytics & ETL | 15 | 0 | 0 | 15 | 15 |
| Distribution / Specialized: Database & Transactions | 19 | 0 | 0 | 19 | 19 |
| Distribution / Specialized: Messaging & Streaming | 18 | 0 | 0 | 18 | 18 |
| Distribution / Specialized: Network Routing & Switching | 19 | 0 | 0 | 19 | 19 |
| Distribution / Specialized: Observability & Telemetry | 9 | 0 | 0 | 9 | 9 |
| Distribution / Specialized: Reliability, Security & Recovery | 12 | 0 | 0 | 12 | 12 |
| Distribution / Specialized: Runtime & Application | 17 | 0 | 0 | 17 | 17 |
| Distribution / Specialized: Search, Indexing & Vector DB | 16 | 0 | 0 | 16 | 16 |
| Distribution / Specialized: Service Mesh & API Reliability | 16 | 0 | 0 | 16 | 16 |
| Distribution / Specialized: Storage Block/File/Object | 20 | 0 | 0 | 20 | 20 |
| Distribution / Specialized: Telecom RAN & Edge Radio | 12 | 1 | 0 | 11 | 11 |
| Distribution / Specialized: Workflow, Logistics & Fulfillment | 15 | 0 | 0 | 15 | 15 |
| Energy / Facility / Industrial: Building & Critical Environment HVAC | 15 | 5 | 0 | 10 | 4 |
| Energy / Facility / Industrial: Cooling, Chillers & Thermodynamics | 18 | 6 | 0 | 12 | 12 |
| Energy / Facility / Industrial: Energy Storage & Microgrid | 19 | 0 | 3 | 16 | 16 |
| Energy / Facility / Industrial: Facility & Grid Optimization | 15 | 0 | 1 | 14 | 14 |
| Energy / Facility / Industrial: Grid Transmission & Distribution | 12 | 4 | 0 | 8 | 4 |
| Energy / Facility / Industrial: Industrial PLC & Process Automation | 18 | 6 | 0 | 12 | 3 |
| Energy / Facility / Industrial: PDU, UPS & Electrical Distribution | 18 | 0 | 0 | 18 | 18 |
| Energy / Facility / Industrial: Semiconductor Fab & Precision Manufacturing | 13 | 2 | 0 | 11 | 4 |
| Energy / Facility / Industrial: Water Wastewater & Pumping | 12 | 4 | 0 | 8 | 5 |
| Physics / Robotics / Autonomous: Automotive EV & Mobile Powertrain | 14 | 0 | 0 | 14 | 14 |
| Physics / Robotics / Autonomous: Aviation & Autonomous Flight | 20 | 7 | 0 | 13 | 13 |
| Physics / Robotics / Autonomous: Robotics Fleet & Warehouse Automation | 15 | 0 | 0 | 15 | 15 |
| Physics / Robotics / Autonomous: Robotics Motion Control | 18 | 8 | 0 | 10 | 10 |
| Physics / Robotics / Autonomous: Spacecraft & Flight Software | 14 | 4 | 4 | 6 | 6 |
| Energy / Facility / Industrial: Healthcare Critical Environments | 13 | 7 | 0 | 6 | 3 |
| Distribution / Specialized: Medical Imaging & Clinical Systems | 12 | 0 | 0 | 12 | 12 |
| Energy / Facility / Industrial: Agriculture & Irrigation | 14 | 10 | 0 | 4 | 1 |
| Energy / Facility / Industrial: Oil & Gas Pipelines | 14 | 8 | 0 | 6 | 3 |
| Physics / Robotics / Autonomous: Rail Traction & Train Control | 14 | 0 | 0 | 14 | 14 |
| Physics / Robotics / Autonomous: Marine Propulsion & Vessel Automation | 12 | 0 | 0 | 12 | 11 |
| Distribution / Specialized: Ports & Maritime Logistics | 12 | 1 | 0 | 11 | 11 |
| Energy / Facility / Industrial: Mining & Mineral Processing | 14 | 5 | 0 | 9 | 2 |
| Energy / Facility / Industrial: District Heating & Cooling | 13 | 3 | 4 | 6 | 2 |
| Energy / Facility / Industrial: Power Generation & Turbine Control | 14 | 10 | 0 | 4 | 2 |
| Energy / Facility / Industrial: Renewable Generation & Inverter Control | 13 | 2 | 0 | 11 | 3 |
| Physics / Robotics / Autonomous: Elevators & Vertical Transport | 12 | 0 | 0 | 12 | 11 |
| Energy / Facility / Industrial: Pharmaceutical & Food Manufacturing | 14 | 10 | 0 | 4 | 4 |

### Why the watch muscles are watch

- **746 muscles wrote nothing in any run.** Their plants' native controllers held the reading inside the compass's band for the whole hour on every seed, so the law never left its cushion and had nothing to push. On these muscles Omni on top is native: nothing earned, nothing lost, and no wire in is needed. They are 392 capacity knobs, 255 admission knobs, 62 power knobs and 37 setpoint knobs, 567 of them on the compute plant, whose native autoscaler and fixed admission limit already serve the modelled demand inside its line.
- **All 255 admission muscles are watch**, and all wrote nothing: the admission knob is native while change is permitted, and limits what is let in only while it is not (a power or heat stress; `docs/REALMS_PREREGISTRATION.md`). No run reached that state, so the knob was never touched. This is the knob's design, not a failure: admission is a brake for an emergency the hour did not hold.
- **62 muscles wrote and showed nothing**: their work per energy moved by at most +1.8% with an interval across zero. They are process loops, inverters, chambers, mills and zones where the law moved the knob inside its band and the plant's output did not measurably follow. Watch, by rule.
- **One muscle is not established** (Elevators & Vertical Transport, `hoist_speed_target`): the interval is too wide to read and the work guardrail did not hold. Watch, until a longer run decides it.

### The trades, muscle by muscle

| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) | Verdict |
|---|---|---|---|---:|---:|---:|---|
| `cpufreq_min` | Host CPU & Memory | power | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +1.41% (+1.12 to +1.71) | +0.00% | +0.11 | **operator's choice** |
| `battery_soc_reserve` | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.21% (-0.22 to -0.21) | +0.00% | -1.40 | **operator's choice** |
| `time_of_use_schedule` | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.21% (-0.22 to -0.21) | +0.00% | -1.39 | **operator's choice** |
| `microgrid_emergency_reserve` | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.21% (-0.21 to -0.20) | +0.00% | -1.40 | **operator's choice** |
| `pue_target` | Facility & Grid Optimization | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.12% (-0.13 to -0.12) | +0.00% | -0.81 | **operator's choice** |
| `payload_duty_cycle` | Spacecraft & Flight Software | power | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +0.82% (+0.66 to +0.98) | +0.00% | +0.92 | **operator's choice** |
| `space_power_budget` | Spacecraft & Flight Software | power | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +0.75% (+0.66 to +0.84) | +0.00% | +0.50 | **operator's choice** |
| `space_thermal_command` | Spacecraft & Flight Software | power | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +0.80% (+0.76 to +0.85) | +0.00% | +0.36 | **operator's choice** |
| `rcs_authority` | Spacecraft & Flight Software | power | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +0.84% (+0.75 to +0.93) | +0.00% | +0.36 | **operator's choice** |
| `return_temperature_target` | District Heating & Cooling | setpoint | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +5.15% (+2.49 to +7.80) | -0.02% | +0.04 | **operator's choice** |
| `differential_pressure_setpoint` | District Heating & Cooling | setpoint | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +3.74% (+0.62 to +6.87) | -0.06% | +0.06 | **operator's choice** |
| `thermal_storage_level_target` | District Heating & Cooling | setpoint | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +3.88% (+1.08 to +6.69) | -0.03% | +0.06 | **operator's choice** |
| `cooling_storage_level_target` | District Heating & Cooling | setpoint | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | +3.47% (+0.51 to +6.43) | -0.11% | +0.10 | **operator's choice** |
| `hoist_speed_target` | Elevators & Vertical Transport | capacity | NOT ESTABLISHED | -1.63% (-7.65 to +4.39) | -2.50% | +0.00 | **watch** |

The nine energy-for-service trades are the CPU's minimum clock (`cpufreq_min`), four spacecraft power knobs and four district heating setpoints: energy saved at a measurable cost in work or in time in violation. The four service-for-energy trades are three microgrid reserves and a facility's PUE target: time in violation proven lower at a small energy cost. Each is the operator's to take or leave; none is wired in by default.

### The setpoint muscles, and what the band alone gives

Of the 82 setpoint muscles that read SUPERIOR, a fixed setpoint at the band's calm end (the `fixed_calm` arm, the native controller with the setpoint fixed, no governor) gave as much or more work per energy on every one. On 64 of them the fixed setpoint also held the service guardrails, so the gain is the band's and an operator may simply fix the setpoint; on 18 the fixed setpoint broke the service guardrail (ENERGY IMPROVEMENT WITH SERVICE TRADEOFF), and there the governor's moving hand is what keeps the service while the energy is saved. The CSV says which is which, muscle by muscle.

## The organisms

### The five modelled organisms (every muscle written at once, one governor)

| Organism | Muscles | Label | Verdict | Figures |
|---|---:|---|---|---|
| Compute / AI / Cloud | 430 muscles | SUPERIOR WITHIN GUARDRAILS | **write** | SUPERIOR WITHIN GUARDRAILS: work per energy +0.1% (+0.1 to +0.1), work +0.0%, energy -0.1%, violations -0.012 pp; valid: yes |
| Physics / Robotics / Autonomous | 376 muscles | SUPERIOR WITHIN GUARDRAILS | **write** | SUPERIOR WITHIN GUARDRAILS: work per energy +0.1% (+0.1 to +0.1), work +0.0%, energy -0.1%, violations -0.003 pp; valid: yes |
| Energy / Facility / Industrial | 470 muscles | SUPERIOR WITHIN GUARDRAILS | **write** | SUPERIOR WITHIN GUARDRAILS: work per energy +0.3% (+0.2 to +0.4), work +0.0%, energy -0.3%, violations -0.013 pp; valid: yes |
| Distribution / Specialized | 440 muscles | SUPERIOR WITHIN GUARDRAILS | **write** | SUPERIOR WITHIN GUARDRAILS: work per energy +0.2% (+0.1 to +0.2), work +0.0%, energy -0.2%, violations -0.009 pp; valid: yes |
| The whole tower, every muscle once | 945 muscles | SUPERIOR WITHIN GUARDRAILS | **write** | SUPERIOR WITHIN GUARDRAILS: work per energy +0.3% (+0.2 to +0.4), work +0.0%, energy -0.3%, violations -0.004 pp; valid: yes |

An organism's label is the whole's: every muscle written at once. The wiring an operator takes from this page is finer: the write muscles wired in, the trades chosen, the watch muscles left native with one wire out. The organism result says the whole, written at once, was no worse and a little better; this page says which parts carried it.

### The organisms with the real cluster inside

The knob is the cluster's (the autoscaler's replicas, the floor and the machines), under the organism's own demand, with the modelled muscles around it. The cluster's gauges decide the verdict; the organism's modelled work and energy are shown beside them and are judged muscle by muscle above.

| Cell | Verdict | The table's reading, and the figures | Source |
|---|---|---|---|
| compute_ai_cloud at 10 copies (GitHub) | **write** | the table's own reading: better on 5, worse on 0, inside the noise on 6. The cluster's gauges: 2 better (p95, time over the line), 0 worse. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| physics_robotics_autonomous at 10 copies (GitHub) | **watch** | the table's own reading: better on 3, worse on 0, inside the noise on 8. The cluster's gauges: 0 better, 0 worse. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| energy_facility_industrial at 10 copies (GitHub) | **operator's choice** | the table's own reading: better on 4, worse on 1 (HPA replicas, mean), inside the noise on 6. The cluster's gauges: 1 better (time over the line), 1 worse (HPA replicas, mean). The organism's modelled energy -0.3%. | `results/live/V3_SIX_KUBE.md` |
| distribution_specialized at 10 copies (GitHub) | **write** | the table's own reading: better on 5, worse on 0, inside the noise on 6. The cluster's gauges: 2 better (p95, time over the line), 0 worse. The organism's modelled energy -0.2%. | `results/live/V3_SIX_KUBE.md` |
| tower at 10 copies (GitHub) | **write** | the table's own reading: better on 6, worse on 0, inside the noise on 5. The cluster's gauges: 3 better (p95, time over the line, failed requests), 0 worse. The organism's modelled energy -0.3%. | `results/live/V3_SIX_KUBE.md` |
| stack at 10 copies (GitHub) | **write** | the table's own reading: better on 5, worse on 1 (organism work), inside the noise on 6. The cluster's gauges: 2 better (time over the line, failed requests), 0 worse. The organism's modelled work -0.0006% (6 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| compute_ai_cloud at 100 copies (GitHub) | **write** | the table's own reading: better on 4, worse on 1 (organism work), inside the noise on 7. The cluster's gauges: 1 better (time over the line), 0 worse. The organism's modelled work -0.0008% (8 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| physics_robotics_autonomous at 100 copies (GitHub) | **write** | the table's own reading: better on 4, worse on 1 (organism work), inside the noise on 7. The cluster's gauges: 1 better (time over the line), 0 worse. The organism's modelled work -0.0011% (11 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.1%. | `results/live/V3_SIX_KUBE.md` |
| energy_facility_industrial at 100 copies (GitHub) | **write** | the table's own reading: better on 7, worse on 0, inside the noise on 5. The cluster's gauges: 3 better (time over the line, parked-worker energy, standby-model energy), 0 worse. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| distribution_specialized at 100 copies (GitHub) | **write** | the table's own reading: better on 6, worse on 0, inside the noise on 6. The cluster's gauges: 2 better (p95, time over the line), 0 worse. The organism's modelled energy -0.2%. | `results/live/V3_SIX_KUBE.md` |
| tower at 100 copies (GitHub) | **write** | the table's own reading: better on 5, worse on 0, inside the noise on 6. The cluster's gauges: 1 better (time over the line), 0 worse. The organism's modelled energy -0.4%. | `results/live/V3_SIX_KUBE.md` |
| stack at 100 copies (GitHub) | **write** | the table's own reading: better on 4, worse on 1 (organism work), inside the noise on 6; OFF THE CLOCK in 3 of 5 repetitions (the organism ended up to 277 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest). The cluster's gauges: 1 better (time over the line), 0 worse. The organism's modelled work -0.0008% (8 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. Off the clock in 3 of 5 repetitions. | `results/live/V3_SIX_KUBE.md` |
| tower at 1000 copies (Azure) | **write** | the table's own reading: better on 7, worse on 1 (organism work), inside the noise on 4. The cluster's gauges: 4 better (p95, p99, time over the line, failed requests), 0 worse. The organism's modelled work -0.0004% (4 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_BIG_ORGANISM.md` |
| stack at 1000 copies (Azure) | **write** | the table's own reading: better on 7, worse on 1 (organism work), inside the noise on 3. The cluster's gauges: 4 better (p95, p99, time over the line, failed requests), 0 worse. The organism's modelled work -0.0006% (6 parts in a million, rounding level), the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's. The organism's modelled energy -0.4%. | `results/live/V3_BIG_ORGANISM.md` |

## Not decided here

- **Azure's managed Kubernetes (the bill):** the two tables are on Omni v1 (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`) on a 4-worker fleet, where every gauge read no difference beyond the noise but the burst's p99 in one run. A fleet too small to show one machine decides nothing; the fleet that can (`docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine) decides this knob on v3 when it runs. Until then the verdict on Azure is watch, for want of a result rather than because of one.
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
| The 945 modelled muscles | each muscle's knob | one directive from the organism's governor, no trial per muscle; 746 never wrote, 13 are trades | the law's own push and pull | Omni v3 (the verdict per muscle is Omni v4, `docs/OMNI_V4_PLAN.md`, not built) |
| The machine itself: the Linux kernel's frequency ceiling (`docs/CPU_POWER_PREREGISTRATION.md`) | one knob | `tools/knob_verdict.py` around the engine's verdict: every notch down tried on the machine first, under the index's reading for one machine (energy x latency / work) or energy per request inside the line | give back only (the ceiling cannot go above the top; the top always free) | outside the engine; built 10 October, waiting for a machine on the metal, no run yet |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
