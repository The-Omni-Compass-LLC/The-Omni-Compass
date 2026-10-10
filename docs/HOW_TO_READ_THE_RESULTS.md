# How to Read the Results

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

This chapter teaches you to read every table Omni-Compass produces. You do not need to know Kubernetes or GPUs to
follow it. Read the five ideas first, then go to the table you have in front of you.

## The five ideas behind every table

1. **Native, and native with Omni-Compass on top.** Omni-Compass never runs a machine by itself. Every result compares
   a system running alone ("native": Kubernetes alone, the card's own firmware alone, a building's own controller
   alone) with the same system with Omni-Compass sitting on top of it. Same machine, same work, same moment: the only
   difference is Omni-Compass.
2. **Paired runs.** Each comparison is run many times ("repetitions" or "runs"), each time with both arms on the same
   seed (the same pattern of work). Each repetition gives one difference; the table reports the average difference.
3. **The 95% interval.** Next to each average is a range, for example `+0.092% (+0.090 to +0.093)`. It means: if we
   ran this again and again, the true answer would land inside that range 95 times out of 100.
   - If the whole range is on one side of zero, the difference is **proven** (the table says "yes" or "significant").
   - If the range crosses zero, the difference is **not proven**: it could be noise.
4. **Better is not always "up".** For energy, response time, failures, machines and time over the line, **lower is
   better**, so a minus sign is good. For work per energy and work done, **higher is better**, so a plus sign is good.
   Every table says which.
5. **Evidence class.** Every result is marked with how it was measured:
   - **T**: a theorem;
   - **V**: verified in code;
   - **S**: a model (simulation);
   - **L**: live software (real Kubernetes);
   - **P**: a physical meter (a real card's own power meter).

   Only **P** speaks for hardware energy.

## The words in the tables

| Word | What it means | Better is |
|---|---|---|
| Work per energy | work done for each unit of energy (requests per kilojoule on a card) | higher |
| Energy (J, Wh) | the energy used | lower |
| Work, requests served | how much was done; both arms must serve the same work | equal |
| Response time, median (p50) | half of the answers were faster than this | lower |
| Response time, p95 | 95 of 100 answers were faster than this: the slow answers, what service promises are written on | lower |
| Response time, p99 | 99 of 100 answers were faster than this: the slowest answers | lower |
| Time over the line, violations (pp) | the share of time the service was past its promise, in percentage points | lower |
| Failed requests, not served | answers that never came | zero |
| Machines in service, node-hours | how many machines were kept on, and for how long | lower |
| Band first | the founder's rule: no win unless time over the line is no higher than native's | "held" |
| Knobs handed back, restored | at the end every setting Omni-Compass touched was put back exactly | True / yes |
| Label | the verdict, chosen by a rule written before the run, never by hand | see each table |

## The GPU card (`results/gpu/run-<stamp>/GPU_REPS.md`)

One card, three arms, many repetitions:
- **native**: the card's firmware alone;
- **watch**: Omni-Compass running and deciding but writing nothing. It must equal native: this proves Omni-Compass
  watching costs nothing;
- **omni**: Omni-Compass on top, moving the card's clock ceiling and power limit.

Read it in this order:
1. **The verdict line** at the top, one of: *better, proven*; *worse, proven*; *not proven*; *better on energy, fails
   the service guardrail*.
2. **Work per energy** (requests per kilojoule): the headline. A plus sign with a range wholly above zero is a proven
   gain.
3. **Requests served** must be equal in every arm. More energy saved by serving less work would be cheating; the bench
   checks it.
4. **p95 and p99**: the slow answers. With the verdict rule (`omnicompass/verdict.py`), Omni-Compass never takes a step
   that makes a request more than 2% slower.
5. **Writes and restore**: how many settings were changed, and that every arm ended at the card's own limit.

The file `omni-gpu-<stamp>-confirmations.tar.gz` holds two such tables: compute-bound work (matrix products) and AI
token generation (memory-bound work).

## The card inside the six organisms (`results/hil/run-<stamp>/HIL.md`)

The real card is wired into each of the six organisms (the four realms, the four stacked, the whole tower) at four
sizes (1, 10, 100 and 1,000 copies). Each row is one size, one organism and one part:
- **stacks (model)**: the simulated machines (evidence S);
- **card (meter)**: the real card, its own meter (evidence P);
- **both**: the two added together.

The second table lists the card's own receipts for every arm: its energy, requests served, p95, and its power limit at
the start and at the end, which must be equal.

## Real Kubernetes (`results/live/LIVE_REPS_<n>.md`)

Each set is 10 paired repetitions on a real Kubernetes cluster (kind): native Kubernetes (its HPA and scheduler)
against the same Kubernetes with Omni-Compass on top. Read:
1. **worker nodes in service** and **node-hours**: how many machines were kept busy. Minus is better.
2. **response time p95 and p99**: minus is faster.
3. **failed requests**: must be zero on both sides.
4. **CPU used with Omni's own**: Omni-Compass's own cost included; "no" in the significant column means it costs
   nothing measurable overall.
5. **The label** at the bottom, by the rule written before the run.

Energy on kind is a declared model, not a meter: kind keeps every machine powered.

## The three-run tables (`results/live/V1_<TEST>.md`, `V3_<TEST>.md`)

Every benchmark since the engine was frozen runs three separate times, A, B and C, on the same bytes, and the table
shows all three beside each gauge. Read the last column first: **confirmed better** or **confirmed worse** (the same sign
in all three, every interval clear of zero), **no difference beyond the noise** (an interval over zero in at least one
run: that is the result), or **the runs disagree** (the test is unstable there and is looked into). Nothing reads "not
confirmed". The `V1_` or `V3_` in the name is the engine the runs carried (`python3 tools/omni_version.py --commit <sha>`);
a table never mixes engines, and a reading is never carried from one engine to another. Losses are in the table beside
the gains: the database's host CPU-seconds, the grid's losses in four grids, the Panda's copper, CityLearn's bill.

## The workload tables (`V3_PGBENCH.md`, `V3_KAFKA.md`, `V3_REDIS.md`, `V3_YCSB.md`) and the swarm table (`V3_SWARM.md`)

The database, the broker and the cache share one shape. The head names the three runs, their commits and the engine each
carried. Then one section per **workload**: the tuning workload first, marked "shown and not counted" because the rules were
fitted on it, then the untouched workloads, which are the judged ones. Each section says what the workload is (value sizes,
rates, steps) and what native's own capacity measured on that run, so the reader knows how hard native was pushed. The
rows are the gauges with their direction in the name: the first row is always **work inside the response line**, the
product number; then throughput, the latency percentiles, failures (any increase in any run is WORSE), **the resource
held** (connections, consumers, the memory ceiling: lower is better, and Omni-Compass holds more of it wherever it bought
a gain, so expect WORSE there), the host's CPU (the compass's own cost included), and the knob's moves (shown, not
judged). The last line of each section says whether every arm handed the knob back; the last line of the table counts the
rows better, worse and disagreeing across the untouched workloads. The swarm table reads the same way with cells instead
of workloads, with collisions voiding a cell, and with a declared reproduction tolerance (one part in a thousand) because
PyBullet does not reproduce to the bit across machines; its amendment says so.

## The governor's own cost (`V3_OWN_COST.md`) and the robustness tables

`V3_OWN_COST.md` is Omni-Compass's own CPU, from the `overhead` record every omni arm's audit carries, by organism and
copies, under the engine each run carried; it is shown and not judged, and it is a few thousandths of one core at every
size. The robustness tables (V3_ROBUST_KILL.md and V3_ROBUST_LONG.md in `results/live/`, when they land) add rows that belong to the omni
arm alone, since native has no governor to kill: the seconds from the kill until every setting was back at the operator's
(the allowance is 60 s, declared before the run), whether a second governor started and governed to the end, and the
governor's memory in the last ten minutes over the first ten (a quarter's growth is a leak, declared before the run); the
120 s after the kill are compared between the arms like any paired gauge.

## The organisms with a real cluster inside (`V1_SIX_KUBE.md`, `V3_SIX_KUBE.md`, `V1_BIG_ORGANISM.md`)

Two kinds of rows, kept apart: **the cluster** (real Kubernetes, measured) and **the organism** (the modelled stacks
around it, evidence S). "Organism behind its window (s)" is shown and not judged; a repetition reads **OFF THE CLOCK**
when either arm ended more than 5% of its window late (its last steps saw a cluster whose load had already ended). The
pairing stands, the mark stays, and the remedy is a longer window for that size on that machine.

## The one number (`results/OMNI_INDEX.md`)

Every measure is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work, speed, machines,
energy. A test's index is the geometric mean of its ratios, a category's of its tests, the headline of the real
categories, each weighted the same. A measure enters only as its three-run reading allows; no difference beyond the
noise enters as exactly 1. Modelled muscles are shown beside the index, never inside it.

## The six organisms grid (`results/scale/GRID.md`)

Columns are **size × runs**: 1, 10, 100 and 1,000 clusters, each at 1, 10, 100 and 1,000 paired runs. Rows are the six
organisms. There is one table each for work per energy, energy, time over the line and work done. Read a cell as
"with Omni-Compass on top, against native, at this size, over this many runs". Cells that are still computing say so;
1,000 runs at 1,000 clusters is beyond the machines available and says so.

## Kubernetes at scale (`KWOK.md`, from the `kwok-scale` workflow)

Real Kubernetes at 50, 500 and 1,000 nodes (KWOK nodes: real Kubernetes objects with no machines behind them):
- **decision time** is how long Omni-Compass takes to decide, at that size;
- **memory** is what it uses;
- **master switch** must read "yes": everything handed back.

## One number, one meaning of the sign (`docs/BENEFIT_SHEET.md`)

In the tables a change keeps its raw sign: a response time that fell reads "-65%", a cache that grew reads "+300%", and
whether each is good depends on the gauge. The benefit sheet turns every one the same way round: **plus is always good for
Omni, minus is always bad**, whatever the gauge measures, and the number carries its word, **gain**, **loss** or
**nothing**. Beside it every confirmed change is written out in words, never as a bare sign: a gauge that fell when
falling is good reads **cut** (less waiting, fewer machines, less energy, less memory, fewer failures), a gauge that rose
when rising is good reads **up**, and each carries **good** or **cost**. So "p95 cut 65%: good" and "memory ceiling held up
215%: cost" cannot be misread against a table that shows the same changes as "-65%" and "+215%". One number per benchmark,
by the index's own rule, with **yes**, **no**, **none** or **trade** beside it. Read that sheet first; read the tables for
the rows behind a number, and read their Reading column, never the sign alone. The wiring page uses the same words.

## Wire in, or watch (`docs/WIRING_VERDICTS.md`)

One of three words per knob, by one rule from the tables above. **Write**: a gauge confirmed better over all three runs
and none confirmed worse; Omni holds the knob. **Watch**: nothing confirmed better; the knob stays native and Omni only
reads it (one wire out, no wire in), and a confirmed loss is named with its cause. **Operator's choice**: gains and losses
both confirmed, a trade, shown with both readings of the index. Rows marked "shown, not judged" never count. A modelled
muscle takes its word from its label: superior is write, a tradeoff label is the operator's choice, the rest is watch. The
CSV beside the page (`results/WIRING_VERDICTS.csv`) has one row per knob and per muscle.

## Where to start

1. `docs/STATE_OF_PLAY.md`: one page, every result and how strong it is.
2. `docs/DOSSIER.md`: every result with its chart.
3. This chapter, next to the table in front of you.
4. `DISCLOSURES.md`: what a result is and is not.

## Reading the benefit: more work, or the same work for less

With the work held equal in both arms, the gain from Omni-Compass on top is *G = C_native / C_omni − 1*, where *C* is a
resource (machine-hours, CPU core-hours, joules). The same work then needs *1 / (1 + G)* of the resources, a saving of
*G / (1 + G)*: a third more work is a quarter off the bill. The full explanation, the three rules for reading a receipt
and where every number stands today are in the manual, section 3 (`docs/OMNI_COMPASS_MANUAL.md`).

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
