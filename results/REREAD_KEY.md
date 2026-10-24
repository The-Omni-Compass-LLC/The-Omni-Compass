# Every reading that moved under the rule of 24 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 24 October 2026: "Any gauge that gives anything over a 0.5 percent change either way is a change. I don't want to see even on shit that shows a 0.5% change up or down, it has to show its loss or gain." The rule is written once (`tools/readings.py` judge_runs and judge_one) and every published table was read again by it (`tools/reread_key.py`), from each row's own numbers; every row, run and number is kept. This page counts what moved and names every row that now reads LOSS, and every LOSS that now reads EVEN under the 0.5% floor (the floor of 20 October, now applied in every table: the stores' and the deterministic simulators' tools had not applied it). Every reading whose word moved is in the JSON twin, one a line.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

## The three-run tables and organism reports (`results/live/`)

| Before | Now | Readings |
|---|---|---:|
| EVEN | the runs disagree | 1,151 |
| EVEN | GAIN | 1,072 |
| EVEN | EVEN | 899 |
| EVEN | LOSS | 479 |
| EVEN | power given | 418 |
| GAIN | EVEN | 262 |
| power given | EVEN | 51 |
| LOSS | EVEN | 39 |
| GAIN | GAIN | 4 |
| the runs disagree | power given | 3 |
| the runs disagree | EVEN | 2 |
| the runs disagree | LOSS | 1 |

## Our own models (`results/toy_gate/`, evidence class S, never a benchmark result)

| Before | Now | Readings |
|---|---|---:|
| EVEN | EVEN | 480 |
| EVEN | LOSS | 275 |
| EVEN | GAIN | 242 |
| EVEN | power given | 92 |
| LOSS | EVEN | 40 |
| GAIN | EVEN | 22 |
| power given | EVEN | 2 |

## Every row that now reads LOSS

480 in the three-run tables and organism reports, 275 in our own models. Each one's cause is looked for as every LOSS's is (our own wiring first, then native's setup, then the scoring), and every one on the engine that stands goes on the next version's list.

| Page | Where | Gauge | Before | Now | The runs' changes |
|---|---|---|---|---|---|
| `results/live/SIX_KUBE.md` | stack_1226 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +5.8% (-2257 to +2996) |
| `results/live/V10_BATCH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.94%; +0.00% |
| `results/live/V10_BATCH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +142.42%; +18 (native 0); +0.00% |
| `results/live/V10_BATCH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +27.27%; +13.1 (native 0); +0.00% |
| `results/live/V10_BATCH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +0.55%; +0.93%; +0.79% |
| `results/live/V10_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; -4.76%; -3.12% |
| `results/live/V10_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; -4.88% |
| `results/live/V10_CRUISEKUBE.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +1.42%; +0.92%; +1.40% |
| `results/live/V10_CRUISEKUBE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.55%; +3.02%; +0.55% |
| `results/live/V10_CRUISEKUBE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +1.34%; +3.06%; +2.67% |
| `results/live/V10_KAFKA.md` | tuning | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.71%; +1.03%; +1.40% |
| `results/live/V10_KAFKA.md` | tuning | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.19%; +0.64%; +0.96% |
| `results/live/V10_KAFKA.md` | tuning | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.17%; +1.56%; +1.51% |
| `results/live/V10_KAFKA.md` | tuning | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.12%; +0.65%; +0.60% |
| `results/live/V10_KAFKA.md` | tuning | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.99%; +1.25%; +1.16% |
| `results/live/V10_KAFKA.md` | burst | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 2 of 3 clear of the noise) | -0.51%; +0.03%; -0.27% |
| `results/live/V10_KAFKA.md` | burst | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.01%; +2.89%; +0.46% |
| `results/live/V10_KAFKA.md` | heavy | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.27%; +0.52%; +2.49% |
| `results/live/V10_KAFKA.md` | heavy | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.72%; +0.92%; +0.74% |
| `results/live/V10_KAFKA.md` | heavy | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +1.99%; +1.49%; -0.03% |
| `results/live/V10_KAFKA_SERVICE.md` | tuning | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.77%; -0.27%; +1.38% |
| `results/live/V10_KAFKA_SERVICE.md` | burst | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.25%; -0.86%; -0.14% |
| `results/live/V10_KAFKA_SERVICE.md` | burst | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.00%; +4.22%; +0.04% |
| `results/live/V10_KAFKA_SERVICE.md` | burst | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.78%; +2.94%; +0.39% |
| `results/live/V10_KAFKA_SERVICE.md` | light | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +2.05%; +0.43%; +3.84% |
| `results/live/V10_KAFKA_SERVICE.md` | light | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.99%; +0.83%; +3.58% |
| `results/live/V10_KAFKA_SERVICE.md` | light | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.70%; +0.37%; +2.03% |
| `results/live/V10_KAFKA_SERVICE.md` | light | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.60%; +0.37%; +3.86% |
| `results/live/V10_KEDA_REQUESTS.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.01235 (native 0); +0.00%; +0.00% |
| `results/live/V10_REDIS.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.06%; +0.14%; +0.66% |
| `results/live/V10_REDIS_SERVICE.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.33%; +0.15%; +0.69% |
| `results/live/V10_REDIS_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.61%; -0.04%; +0.95% |
| `results/live/V10_REDIS_SERVICE.md` | small | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.15%; +2.67%; +0.33% |
| `results/live/V10_ROBUST_LONG.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +172.73%; +98.04%; +81.25% |
| `results/live/V10_SYSBENCH.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.31%; +0.06%; +3.92% |
| `results/live/V10_SYSBENCH.md` | burst | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; -0.69%; -0.03% |
| `results/live/V10_SYSBENCH.md` | burst | throughput (transactions a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -2.00%; -0.62%; +0.03% |
| `results/live/V10_SYSBENCH.md` | burst | queries a second | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -2.00%; -0.62%; +0.03% |
| `results/live/V10_SYSBENCH.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +1.82%; +1.85%; +0.60% |
| `results/live/V10_SYSBENCH.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.58%; +6.48%; -0.46% |
| `results/live/V10_TRACE_GOOGLE2011.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +76.06%; +116.25%; +45.09% |
| `results/live/V10_WANDERING.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +32.77%; +4.50%; +14.69% |
| `results/live/V10_YCSB.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.24%; -0.27%; +1.14% |
| `results/live/V10_YCSB.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.05%; +0.00%; +1.28% |
| `results/live/V10_YCSB.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.42%; +0.54%; +0.94% |
| `results/live/V11_CAPACITY.md` |   | completed work (requests answered within the line over the window) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | -6.79%; -1.59%; -1.96% |
| `results/live/V11_CAPACITY.md` |   | completed work (requests answered within the line over the window) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.16%; -0.86%; -0.71% |
| `results/live/V11_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; -6.45% |
| `results/live/V11_CAPACITY.md` |   | completed work (requests answered within the line over the window) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -1.67%; -0.33%; -1.41% |
| `results/live/V11_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | -2.70%; -5.41%; -2.63% |
| `results/live/V11_KAFKA.md` | tuning | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +1.05%; -0.38% |
| `results/live/V11_KAFKA.md` | burst | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.82%; +0.58%; +0.65% |
| `results/live/V11_KAFKA.md` | burst | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.78%; -0.05%; +1.35% |
| `results/live/V11_KAFKA.md` | light | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.38%; +2.94%; +0.04% |
| `results/live/V11_KAFKA_SERVICE.md` | heavy | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.19%; -0.07%; -1.60% |
| `results/live/V11_KAFKA_SERVICE.md` | heavy | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.95%; +1.00%; +57.70% |
| `results/live/V11_KAFKA_SERVICE.md` | heavy | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.04%; +0.46%; +54.93% |
| `results/live/V11_KAFKA_SERVICE.md` | heavy | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.29%; -0.33%; +35.09% |
| `results/live/V11_KAFKA_SERVICE.md` | heavy | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.71%; +0.43%; +50.48% |
| `results/live/V11_KEDA_REQUESTS.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.01198 (native 0); +0.00%; +0.00% |
| `results/live/V11_PGBENCH.md` | select | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +1.25%; +0.00% |
| `results/live/V11_PGBENCH_SERVICE.md` | select | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.39%; +0.12%; +0.89% |
| `results/live/V11_PGBENCH_SERVICE.md` | tpcb_hot | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.76%; +0.82%; -0.23% |
| `results/live/V11_REDIS.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.33%; +0.67%; +0.23% |
| `results/live/V11_REDIS_SHIPPED.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.97%; +0.03%; +0.04% |
| `results/live/V11_REDIS_SHIPPED.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +4.90%; +0.16%; -0.25% |
| `results/live/V11_REDIS_SHIPPED.md` | large | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.77%; -0.08%; -0.04% |
| `results/live/V11_ROBUST_LONG.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +268.18%; +135.71%; +138.10% |
| `results/live/V11_SYSBENCH.md` | read_only | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.16%; -0.08%; -0.50% |
| `results/live/V11_SYSBENCH.md` | read_write | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.70%; -0.43%; -0.12% |
| `results/live/V11_SYSBENCH.md` | read_write | throughput (transactions a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.30%; -0.85%; -0.11% |
| `results/live/V11_SYSBENCH.md` | read_write | queries a second | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.30%; -0.85%; -0.11% |
| `results/live/V11_SYSBENCH.md` | update_index | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.95%; +5.48%; +1.17% |
| `results/live/V11_SYSBENCH_SERVICE.md` | burst | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.30%; -0.65%; -0.03% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | tuning | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.39%; +1.22%; +0.00% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.61%; +0.00%; +0.01% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.61%; +0.01%; +0.00% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | read_only | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.61%; +0.57%; +0.00% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | read_write | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.17%; -2.57%; +0.37% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | update_index | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | -28.47%; -13.95%; -10.87% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | update_index | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +14.52%; +2.95%; +4.16% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | update_index | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +19.11%; +1.89%; +11.10% |
| `results/live/V11_SYSBENCH_SHIPPED.md` | update_index | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +6.42%; +0.66%; +3.43% |
| `results/live/V11_YCSB.md` | c | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.04%; -0.08%; -0.52% |
| `results/live/V11_YCSB.md` | c | throughput (operations a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.04%; -0.08%; -0.55% |
| `results/live/V11_YCSB.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.34%; +0.62%; +7.98% |
| `results/live/V11_YCSB.md` | f | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +1.15%; -0.23% |
| `results/live/V11_YCSB_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +2.87%; -0.19%; +0.10% |
| `results/live/V11_YCSB_SERVICE.md` | f | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.10%; -2.19%; -0.26% |
| `results/live/V11_YCSB_SERVICE.md` | f | throughput (operations a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.09%; -2.17%; -0.26% |
| `results/live/V11_YCSB_SERVICE.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.75%; +0.82%; -0.17% |
| `results/live/V11_YCSB_SERVICE.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.07%; +2.75%; -0.14% |
| `results/live/V11_YCSB_SHIPPED.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.13%; +0.64%; +1.02% |
| `results/live/V11_YCSB_SHIPPED.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.35%; +2.06%; +5.78% |
| `results/live/V11_YCSB_SHIPPED.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.13%; +0.89%; -0.25% |
| `results/live/V11_YCSB_SHIPPED.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.20%; -0.01%; +0.33% |
| `results/live/V11_YCSB_SHIPPED.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.58%; +0.38%; +0.37% |
| `results/live/V11_YCSB_SHIPPED.md` | f | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.72%; -0.10%; +0.64% |
| `results/live/V11_YCSB_SHIPPED.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.45%; +0.15%; +0.54% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.37%; +6.45%; +7.75% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +3.20%; +6.25%; +9.65% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +12.03%; +0.00%; +0.00% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.78%; +7.69%; +20.59% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +125.00%; +666.67%; +233.33% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +275.00%; +261.11%; +333.33% |
| `results/live/V12_ARMADA_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +1.41%; +2.25%; +1.59% |
| `results/live/V12_ARMADA_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +400.00%; +666.67%; +433.33% |
| `results/live/V12_ARMADA_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +425.00%; +366.67%; +494.44% |
| `results/live/V12_ARMADA_4W_TOP.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +400.00%; +2.3 (native 0); +6.67% |
| `results/live/V12_ARMADA_4W_VS.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.007637 (native 0); +0.00%; +0.00% |
| `results/live/V12_BINPACK.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.87%; +2.44%; +2.67% |
| `results/live/V12_BINPACK.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +39.99%; +27.74%; +14.83% |
| `results/live/V12_BINPACK.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +75.00%; +44.44%; +0.00% |
| `results/live/V12_BINPACK.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +500.00%; +400.00%; +0.00% |
| `results/live/V12_BINPACK.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +400.00%; +275.00%; +0.00% |
| `results/live/V12_BINPACK.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; +0.1 (native 0) |
| `results/live/V12_BINPACK_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +4.74%; +6.66%; +5.44% |
| `results/live/V12_BINPACK_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.26%; +3.52%; -0.32% |
| `results/live/V12_BINPACK_4W_BARE.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.93%; +11.59%; +3.61% |
| `results/live/V12_BINPACK_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.55%; +0.48%; +0.45% |
| `results/live/V12_BINPACK_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +4.41%; +3.58%; +4.30% |
| `results/live/V12_BINPACK_4W_BOTH.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +10.48%; +0.96%; +7.25% |
| `results/live/V12_BINPACK_4W_BOTH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +14.24%; +7.88%; +12.74% |
| `results/live/V12_BINPACK_4W_BOTH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.54%; +0.05%; -0.05% |
| `results/live/V12_BINPACK_4W_BOTH.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.93%; +2.69%; +4.44% |
| `results/live/V12_BINPACK_4W_ORCH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +13.84%; +14.74%; +9.94% |
| `results/live/V12_BINPACK_4W_TOP.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +80.00%; +100.00%; +0.6 (native 0) |
| `results/live/V12_BINPACK_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +260.00%; +62.50%; +0.6 (native 0) |
| `results/live/V12_BINPACK_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.19%; +2.39%; +5.19% |
| `results/live/V12_BINPACK_4W_VS.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.87%; +28.33%; +8.86% |
| `results/live/V12_BINPACK_4W_VS.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.38%; +0.65%; +0.77% |
| `results/live/V12_BINPACK_4W_VS.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.72%; +3.27%; +5.05% |
| `results/live/V12_CRANE_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +60.29%; +28.75%; +69.01% |
| `results/live/V12_CRANE_4W_BOTH.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.16%; +2.44%; +1.74% |
| `results/live/V12_CRANE_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +8.61%; +21.31%; +0.90% |
| `results/live/V12_CRANE_4W_VS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.58%; +16.76%; +7.84% |
| `results/live/V12_KAFKA.md` | burst | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.22%; +1.31%; +1.48% |
| `results/live/V12_KAFKA.md` | burst | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.51%; +2.34%; +0.49% |
| `results/live/V12_KAFKA.md` | burst | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +3.14%; -0.47%; +0.84% |
| `results/live/V12_KAFKA.md` | burst | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.07%; +0.91%; -0.32% |
| `results/live/V12_KAFKA.md` | heavy | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.35%; -0.41%; +0.90% |
| `results/live/V12_KAFKA.md` | heavy | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.97%; -0.16%; +0.71% |
| `results/live/V12_KAFKA.md` | light | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.36%; -0.83%; -0.06% |
| `results/live/V12_KAFKA_SERVICE.md` | tuning | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.41%; +1.56%; +1.29% |
| `results/live/V12_KAFKA_SERVICE.md` | tuning | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.59%; +0.97%; +1.22% |
| `results/live/V12_KAFKA_SERVICE.md` | tuning | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.00%; -0.44%; +1.82% |
| `results/live/V12_KAFKA_SERVICE.md` | tuning | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.31%; +1.07%; +0.45% |
| `results/live/V12_KAFKA_SERVICE.md` | burst | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -0.32%; +0.11%; -0.92% |
| `results/live/V12_KAFKA_SERVICE.md` | burst | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.08%; +0.96%; +7.11% |
| `results/live/V12_KAFKA_SERVICE.md` | heavy | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.80%; -0.35%; +0.32% |
| `results/live/V12_KAI.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.67%; +9.66%; +5.75% |
| `results/live/V12_KAI.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +8.85%; +42.28%; +6.53% |
| `results/live/V12_KAI.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +28.57%; +61.11%; +0.00% |
| `results/live/V12_KAI.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; +20.00% |
| `results/live/V12_KAI.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +1.45%; +5.34%; +2.25% |
| `results/live/V12_KAI_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.35%; +6.17%; +1.32% |
| `results/live/V12_KAI_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise) | +0.52%; +0.99%; +0.08% |
| `results/live/V12_KAI_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise) | +3.91%; +8.19%; +0.03% |
| `results/live/V12_KAI_4W_BOTH.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.62%; +7.11%; +6.86% |
| `results/live/V12_KAI_4W_BOTH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.33%; +4.31%; +5.50% |
| `results/live/V12_KAI_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +0.4 (native 0); +0.5 (native 0) |
| `results/live/V12_KAI_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +300.00%; +0.4 (native 0); +0.5 (native 0) |
| `results/live/V12_KAI_4W_ORCH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +1.16%; +6.90%; +6.42% |
| `results/live/V12_KAI_4W_TOP.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.76%; +3.38%; +4.41% |
| `results/live/V12_KAI_4W_TOP.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +3.74%; +3.40%; +0.49% |
| `results/live/V12_KAI_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +433.33%; +166.67%; +25.00% |
| `results/live/V12_KAI_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +0.83%; +1.10%; +0.56% |
| `results/live/V12_KAI_4W_TOP.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +62.50%; +15.38%; +14.29% |
| `results/live/V12_KAI_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +5.64%; +6.51%; +5.02% |
| `results/live/V12_KAI_4W_VS.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +16.20%; +5.03%; +8.25% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +12.72%; +4.65%; +4.00% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +14.98%; +7.45%; +5.74% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +14.71%; +8.85%; +4.81% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +300.00%; +1.2 (native 0); +1.9 (native 0) |
| `results/live/V12_KARMADA_4W_BARE.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +150.00%; +0.95 (native 0); +1.25 (native 0) |
| `results/live/V12_KARMADA_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +2.72%; +1.23%; +2.01% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +37.50%; +4.00%; +14.29% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +20.00%; +33.33%; +0.00% |
| `results/live/V12_KARMADA_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +11.56%; +2.16%; +5.82% |
| `results/live/V12_KARMADA_4W_BOTH.md` |   | failed requests (%) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +912.65%; +0.1452 (native 0); +1119.83% |
| `results/live/V12_KARMADA_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +600.00%; +1.9 (native 0); +2.2 (native 0) |
| `results/live/V12_KARMADA_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +98.10%; +1.033 (native 0); +1.225 (native 0) |
| `results/live/V12_KARMADA_4W_BOTH.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2550.00%; +3040.00%; +18419.05% |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +12.38%; +6.85%; +13.05% |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +424.23%; +0.0524 (native 0); +324.66% |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +1.1 (native 0); +1.1 (native 0) |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +50.00%; +0.65 (native 0); +0.85 (native 0) |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +4531.25%; +1692.00%; +11114.29% |
| `results/live/V12_KARMADA_4W_ORCH.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +6540.00%; +150.00%; +12780.00% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +13.90%; +10.54%; +2.74% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +20.01%; +16.70%; +2.54% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +11.96%; +11.11%; +3.96% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +4.92%; +5.40%; +8.31% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +93.17%; +177.17%; +187.25% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +250.00%; +72.73%; +100.00% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +32.06%; +58.97%; +44.12% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +4.29%; +4.07%; +3.03% |
| `results/live/V12_KARMADA_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +15.74%; +14.15%; +9.56% |
| `results/live/V12_KARMADA_4W_VS.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +9.09%; +72.73% |
| `results/live/V12_KARMADA_4W_VS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +66.67%; +46.15%; +47.06% |
| `results/live/V12_KOORDINATOR.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +300.00%; +300.00%; +350.00% |
| `results/live/V12_KOORDINATOR.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +200.00%; +300.00%; +225.00% |
| `results/live/V12_KOORDINATOR_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +5.77%; +6.94%; +5.84% |
| `results/live/V12_KOORDINATOR_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +6.62%; +7.26%; +3.56% |
| `results/live/V12_KOORDINATOR_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 2 of 3 clear of the noise) | +0.15%; +0.59%; +0.46% |
| `results/live/V12_KOORDINATOR_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +5.32%; +3.89%; +7.19% |
| `results/live/V12_KOORDINATOR_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +50.00%; +0.7 (native 0); +0.00% |
| `results/live/V12_KOORDINATOR_4W_BOTH.md` |   | queue: jobs unfinished at the window's end | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +5.3 (native 0); +10.7 (native 0); +8.8 (native 0) |
| `results/live/V12_KOORDINATOR_4W_ORCH.md` |   | queue: jobs unfinished at the window's end | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +4.9 (native 0); +9.4 (native 0); +9.6 (native 0) |
| `results/live/V12_KOORDINATOR_4W_TOP.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +100.00%; +0.00% |
| `results/live/V12_KOORDINATOR_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.75%; -0.01%; +1.77% |
| `results/live/V12_KOORDINATOR_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.90%; +1.89%; +3.36% |
| `results/live/V12_KOORDINATOR_4W_VS.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +40.44%; +148.21%; +71.41% |
| `results/live/V12_KOORDINATOR_4W_VS.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +4381.51%; +7419.52%; +8073.65% |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +6.30%; +6.98%; +3.39% |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.5556 (native 0); +0.5 (native 0); +0.6 (native 0) |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.5556 (native 0); +0.35 (native 0); +0.6 (native 0) |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +57.14%; +120.00%; +76.92% |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +200.00%; +0.00%; +50.00% |
| `results/live/V12_KUBERAY_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +6.80%; +4.99%; +6.13% |
| `results/live/V12_KUBERAY_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.111 (native 0); +0.2 (native 0); +0.8 (native 0) |
| `results/live/V12_KUBERAY_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.7407 (native 0); +0.2 (native 0); +0.8 (native 0) |
| `results/live/V12_KUBERAY_4W_ORCH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.2222 (native 0); +0.8 (native 0); +0.3 (native 0) |
| `results/live/V12_KUBERAY_4W_ORCH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.2222 (native 0); +0.55 (native 0); +0.3 (native 0) |
| `results/live/V12_KUBERAY_4W_TOP.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.92%; +5.63%; +0.55% |
| `results/live/V12_KUBERAY_4W_TOP.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.39%; +0.57%; +1.02% |
| `results/live/V12_KUEUE_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.82%; +1.61%; +4.35% |
| `results/live/V12_KUEUE_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.3 (native 0); +0.00% |
| `results/live/V12_KUEUE_4W_BARE.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.3 (native 0); +0.00% |
| `results/live/V12_KUEUE_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.46%; +0.31%; +0.64% |
| `results/live/V12_KUEUE_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +8.17%; +3.28%; +5.27% |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +10.65%; +13.12%; +11.79% |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.009302 (native 0); +0.00% |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.56%; +3.92%; +3.03% |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.1 (native 0); +0.3 (native 0); +1.222 (native 0) |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.1 (native 0); +0.3 (native 0); +0.7222 (native 0) |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +185.71%; +118.18%; +537.50% |
| `results/live/V12_KUEUE_4W_BOTH.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +100.00%; +0.00%; +800.00% |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +13.25%; +7.03%; +11.15% |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +5.18%; +3.91%; +7.16% |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.98%; +1.01% |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.4 (native 0); +0.4 (native 0); +0.3333 (native 0) |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.4 (native 0); +0.4 (native 0); +0.3333 (native 0) |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +0.91%; +1.09%; +1.44% |
| `results/live/V12_KUEUE_4W_ORCH.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +233.33%; +25.00%; +700.00% |
| `results/live/V12_KUEUE_4W_TOP.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.009302 (native 0); +0.00% |
| `results/live/V12_KUEUE_4W_TOP.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.56%; +2.91%; +2.00% |
| `results/live/V12_KUEUE_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.09%; +0.54%; +0.48% |
| `results/live/V12_KUEUE_4W_TOP.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +2.56%; -0.00%; -0.00% |
| `results/live/V12_KUEUE_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.94%; +4.17%; +3.46% |
| `results/live/V12_OCM_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +4.34%; +3.82%; +1.77% |
| `results/live/V12_OCM_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.09%; +5.05%; +3.03% |
| `results/live/V12_OCM_4W_BARE.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.68%; +2.42%; +10.89% |
| `results/live/V12_OCM_4W_BARE.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +112.50%; +1100.00%; +116.67% |
| `results/live/V12_OCM_4W_BARE.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +100.00%; +525.00%; +100.00% |
| `results/live/V12_OCM_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +2.30%; +1.45%; +1.02% |
| `results/live/V12_OCM_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +6.54%; +4.89%; +2.30% |
| `results/live/V12_OCM_4W_BOTH.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1075.09%; +1410.86%; +41.28% |
| `results/live/V12_OCM_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +262.50%; +1350.00%; +733.33% |
| `results/live/V12_OCM_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +181.82%; +708.33%; +516.67% |
| `results/live/V12_OCM_4W_ORCH.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +43.57%; +56.42%; +15.70% |
| `results/live/V12_OCM_4W_ORCH.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +38.75%; +52.71%; +9.82% |
| `results/live/V12_OCM_4W_ORCH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +34.36%; +48.24%; +10.77% |
| `results/live/V12_OCM_4W_ORCH.md` |   | time over the response line (% of samples) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +38.37%; +26.59%; +17.61% |
| `results/live/V12_OCM_4W_ORCH.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +18.12%; +19.35%; +19.80% |
| `results/live/V12_OCM_4W_ORCH.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +4589.19%; +5839.29%; +4080.25% |
| `results/live/V12_OCM_4W_ORCH.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5528.57%; +6887.50%; +1177.78% |
| `results/live/V12_OCM_4W_TOP.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +9.21%; +1.63%; +41.17% |
| `results/live/V12_OCM_4W_TOP.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +11.17%; +6.86%; +38.04% |
| `results/live/V12_OCM_4W_TOP.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +39.53%; +123.73%; +207.46% |
| `results/live/V12_OCM_4W_TOP.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +866.67%; +2.9 (native 0); +5 (native 0) |
| `results/live/V12_OCM_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +416.67%; +1.617 (native 0); +2.467 (native 0) |
| `results/live/V12_OCM_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +5.55%; +3.02%; +2.58% |
| `results/live/V12_OCM_4W_TOP.md` |   | queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +210.84%; +168.73%; +358.14% |
| `results/live/V12_OCM_4W_TOP.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +304.82%; +88.91%; +1389.47% |
| `results/live/V12_OCM_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +15.57%; +6.87%; +19.58% |
| `results/live/V12_PGBENCH.md` | select | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.09%; -0.10%; +0.72% |
| `results/live/V12_PGBENCH_SERVICE.md` | select | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.35%; +1.61%; +91.25% |
| `results/live/V12_PGBENCH_SERVICE.md` | select | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.20%; +0.67%; +0.17% |
| `results/live/V12_PGBENCH_SERVICE.md` | select | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.85%; +25.77%; +35.95% |
| `results/live/V12_PGBENCH_SERVICE.md` | simple_update | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.38%; -2.02%; -0.20% |
| `results/live/V12_PGBENCH_SERVICE.md` | simple_update | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.48%; +175.05%; +10.88% |
| `results/live/V12_PGBENCH_SERVICE.md` | simple_update | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.43%; +4.53%; -0.49% |
| `results/live/V12_PGBENCH_SERVICE.md` | tpcb_hot | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -2.17%; -1.42%; +0.13% |
| `results/live/V12_PGBENCH_SERVICE.md` | tpcb_hot | throughput (transactions a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -1.20%; +0.00%; -0.10% |
| `results/live/V12_REDIS_SERVICE.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.23%; +0.02%; +1.66% |
| `results/live/V12_REDIS_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.30%; -0.21%; +0.77% |
| `results/live/V12_REDIS_SERVICE.md` | small | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.17%; +0.08%; +0.08% |
| `results/live/V12_SYSBENCH.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +76.97%; +5.82%; +1.38% |
| `results/live/V12_SYSBENCH.md` | read_write | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.81%; +0.11%; -0.56% |
| `results/live/V12_SYSBENCH.md` | read_write | throughput (transactions a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.69%; +0.39%; -0.03% |
| `results/live/V12_SYSBENCH.md` | read_write | queries a second | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.69%; +0.39%; -0.03% |
| `results/live/V12_SYSBENCH.md` | read_write | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.52%; +1.22%; +3.80% |
| `results/live/V12_SYSBENCH.md` | read_write | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +17.57%; +3.01%; +634.36% |
| `results/live/V12_SYSBENCH.md` | read_write | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +5.46%; +0.39%; +77.68% |
| `results/live/V12_SYSBENCH_SERVICE.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +7.87%; +9.78%; +1.35% |
| `results/live/V12_SYSBENCH_SHIPPED.md` | burst | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.22%; -0.51%; -0.53% |
| `results/live/V12_SYSBENCH_SHIPPED.md` | update_index | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | -21.71%; -1.12%; -38.23% |
| `results/live/V12_VANILLA.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | -0.19%; +9.07%; +5.33% |
| `results/live/V12_VANILLA.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +1.02%; +5.70%; +4.55% |
| `results/live/V12_VANILLA.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; +28.89%; +22.06% |
| `results/live/V12_VOLCANO_4W_BARE.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +7.61%; +2.93%; +7.48% |
| `results/live/V12_VOLCANO_4W_BARE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +9.68%; -0.44%; +10.42% |
| `results/live/V12_VOLCANO_4W_BARE.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.45%; +0.22%; +0.57% |
| `results/live/V12_VOLCANO_4W_BARE.md` |   | queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; +25.00%; +150.00% |
| `results/live/V12_VOLCANO_4W_BARE.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +7.26%; +1.52%; +8.96% |
| `results/live/V12_VOLCANO_4W_BOTH.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; +366.67%; +500.00% |
| `results/live/V12_VOLCANO_4W_BOTH.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +366.67%; +500.00% |
| `results/live/V12_VOLCANO_4W_TOP.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.29%; +13.36%; +10.62% |
| `results/live/V12_VOLCANO_4W_TOP.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +1300.00%; +1.2 (native 0) |
| `results/live/V12_VOLCANO_4W_TOP.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +100.00%; +600.00%; +1.2 (native 0) |
| `results/live/V12_VOLCANO_4W_TOP.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.61%; +0.27%; +0.36% |
| `results/live/V12_VOLCANO_4W_TOP.md` |   | queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +6.38%; +1.81%; +2.33% |
| `results/live/V12_VOLCANO_4W_VS.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +20.02%; +11.44%; +13.06% |
| `results/live/V12_VOLCANO_4W_VS.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +73.31%; +9.55%; +23.55% |
| `results/live/V12_VOLCANO_4W_VS.md` |   | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +30.26%; +11.27%; +23.19% |
| `results/live/V12_YCSB_SERVICE.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.41%; +0.23%; +0.37% |
| `results/live/V12_YCSB_SHIPPED.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +1.90%; +2.33%; -0.44% |
| `results/live/V12_YCSB_SHIPPED.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.28%; -0.20%; -0.18% |
| `results/live/V14_PGBENCH_SERVICE.md` | select | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +17.92%; +8.00%; +54.65% |
| `results/live/V14_PGBENCH_SERVICE.md` | select | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.62%; +7.96%; +17.04% |
| `results/live/V14_PGBENCH_SERVICE.md` | simple_update | latency, median (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.72%; -0.18%; +0.11% |
| `results/live/V14_SYSBENCH_SERVICE.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +7.33%; +0.96%; +5.28% |
| `results/live/V14_SYSBENCH_SERVICE.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.81%; +7.66%; +1.79% |
| `results/live/V14_YCSB_SERVICE.md` | tuning | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.21%; +0.67%; +2.83% |
| `results/live/V14_YCSB_SERVICE.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.54%; +0.23%; -0.23% |
| `results/live/V14_YCSB_SERVICE.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.64%; +2.04%; +6.67% |
| `results/live/V14_YCSB_SERVICE.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.31%; +0.93%; +6.55% |
| `results/live/V14_YCSB_SERVICE.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.24%; +0.13%; +3.37% |
| `results/live/V14_YCSB_SERVICE.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.32%; +1.16%; +1.10% |
| `results/live/V14_YCSB_SERVICE.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.12%; +0.20%; +1.73% |
| `results/live/V14_YCSB_SERVICE.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -0.35%; +0.47%; +1.34% |
| `results/live/V14_YCSB_SERVICE.md` | f | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.17%; +1.24%; -0.05% |
| `results/live/V14_YCSB_SERVICE.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.27%; +0.32%; +1.39% |
| `results/live/V14_YCSB_SHIPPED.md` | tuning | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +1.70%; -0.20%; +1.67% |
| `results/live/V14_YCSB_SHIPPED.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.05%; +7.55%; -0.31% |
| `results/live/V14_YCSB_SHIPPED.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.34%; +0.71%; -0.41% |
| `results/live/V14_YCSB_SHIPPED.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.12%; +1.77%; -0.03% |
| `results/live/V14_YCSB_SHIPPED.md` | burst | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.39%; +0.06%; -1.43% |
| `results/live/V14_YCSB_SHIPPED.md` | burst | throughput (operations a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.39%; +0.07%; -1.49% |
| `results/live/V14_YCSB_SHIPPED.md` | c | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.87%; +0.81%; -0.06% |
| `results/live/V14_YCSB_SHIPPED.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.17%; +0.76%; +0.93% |
| `results/live/V14_YCSB_SHIPPED.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.11%; +0.31%; +0.32% |
| `results/live/V14_YCSB_SHIPPED.md` | f | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +1.56%; -0.05%; -0.10% |
| `results/live/V14_YCSB_SHIPPED.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.26%; +0.13%; +0.47% |
| `results/live/V16_KAFKA.md` | burst | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.13%; -0.12%; +1.95% |
| `results/live/V16_KAFKA.md` | burst | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +0.66%; +0.88%; -0.28% |
| `results/live/V16_KAFKA.md` | burst | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.23%; +1.19%; +0.54% |
| `results/live/V16_KAFKA.md` | heavy | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.91%; +0.32%; +2.98% |
| `results/live/V16_KAFKA.md` | heavy | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.31%; +1.16%; +2.29% |
| `results/live/V16_KAFKA.md` | heavy | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.57%; +1.32%; +3.63% |
| `results/live/V16_KAFKA_SERVICE.md` | tuning | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.53%; +2.85%; +1.38% |
| `results/live/V16_KAFKA_SERVICE.md` | burst | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +0.98%; +0.57%; +0.78% |
| `results/live/V16_PGBENCH.md` | select | latency, median (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +0.63%; +1.20%; +0.00% |
| `results/live/V16_PGBENCH.md` | simple_update | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.87%; -0.35%; -0.07% |
| `results/live/V16_PGBENCH.md` | tpcb_hot | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -6.55%; -1.29%; -0.11% |
| `results/live/V16_PGBENCH.md` | tpcb_hot | throughput (transactions a second) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -0.08%; -0.61%; -0.11% |
| `results/live/V16_PGBENCH.md` | tpcb_hot | latency, 95th percentile (ms, lag included) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +430.29%; +75.28%; -0.19% |
| `results/live/V16_PGBENCH_SERVICE.md` | select | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.26%; -0.73%; -0.01% |
| `results/live/V16_PGBENCH_SERVICE.md` | simple_update | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.78%; +0.04%; +0.12% |
| `results/live/V16_PGBENCH_SERVICE.md` | simple_update | throughput (transactions a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.75%; +0.01%; -0.27% |
| `results/live/V16_PGBENCH_SERVICE.md` | tpcb_hot | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -3.69%; -0.02%; +0.05% |
| `results/live/V16_PGBENCH_SERVICE.md` | tpcb_hot | latency, 95th percentile (ms, lag included) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +939.02%; +2.12%; +1.96% |
| `results/live/V16_PGBENCH_SERVICE.md` | tpcb_hot | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +380.87%; +21.92%; +5.47% |
| `results/live/V16_PGBENCH_SERVICE.md` | tpcb_hot | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +3.28%; -0.09%; -0.25% |
| `results/live/V16_REDIS_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.19%; +0.42%; +0.52% |
| `results/live/V16_REDIS_SERVICE.md` | small | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +2.24%; +0.17%; +0.08% |
| `results/live/V16_REDIS_SHIPPED.md` | large | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.37%; +1.65%; +1.18% |
| `results/live/V16_SYSBENCH.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.98%; +2.11%; +2.33% |
| `results/live/V16_SYSBENCH.md` | read_write | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -5.75%; +0.04%; -0.25% |
| `results/live/V16_SYSBENCH.md` | read_write | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +28.51%; -0.13%; +6.89% |
| `results/live/V16_SYSBENCH_SHIPPED.md` | read_only | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.61%; +0.64%; +0.00% |
| `results/live/V16_SYSBENCH_SHIPPED.md` | read_only | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.53%; +0.59%; -0.17% |
| `results/live/V16_YCSB.md` | tuning | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.19%; +3.14%; +0.54% |
| `results/live/V16_YCSB.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.70%; +3.70%; +2.60% |
| `results/live/V16_YCSB.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.24%; +2.57%; +5.50% |
| `results/live/V16_YCSB.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.97%; +0.23%; +2.12% |
| `results/live/V16_YCSB.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.06%; +0.22%; +2.10% |
| `results/live/V16_YCSB.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.33%; +1.50%; +0.88% |
| `results/live/V16_YCSB.md` | c | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.24%; -0.35%; +8.14% |
| `results/live/V16_YCSB.md` | c | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.37%; +1.39%; +1.54% |
| `results/live/V16_YCSB.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.09%; +3.59%; +6.98% |
| `results/live/V16_YCSB.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.31%; -0.47%; +11.55% |
| `results/live/V16_YCSB_SERVICE.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.59%; +1.25%; -0.22% |
| `results/live/V16_YCSB_SERVICE.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.18%; +0.82%; +0.14% |
| `results/live/V16_YCSB_SERVICE.md` | burst | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.08%; -0.51%; +0.02% |
| `results/live/V16_YCSB_SERVICE.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.45%; +0.82%; +0.74% |
| `results/live/V16_YCSB_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.93%; +5.58%; +0.21% |
| `results/live/V16_YCSB_SERVICE.md` | f | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +3.17%; +0.00%; +0.00% |
| `results/live/V16_YCSB_SERVICE.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.90%; -0.10%; -0.36% |
| `results/live/V16_YCSB_SHIPPED.md` | tuning | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.41%; -0.22%; +2.35% |
| `results/live/V16_YCSB_SHIPPED.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.07%; +0.84%; +1.07% |
| `results/live/V16_YCSB_SHIPPED.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.21%; +3.64%; +0.88% |
| `results/live/V16_YCSB_SHIPPED.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.50%; +5.18%; +0.09% |
| `results/live/V16_YCSB_SHIPPED.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.76%; +2.30%; -0.02% |
| `results/live/V16_YCSB_SHIPPED.md` | c | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.36%; +1.64%; +0.00% |
| `results/live/V16_YCSB_SHIPPED.md` | c | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +4.77%; +0.00%; +1.33% |
| `results/live/V16_YCSB_SHIPPED.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.87%; +2.54%; +0.20% |
| `results/live/V1_BATCH.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.38%; +0.44%; +2.47% |
| `results/live/V1_BATCH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise in 1 of 3 runs | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +0.88%; +0.76%; +0.72% |
| `results/live/V1_FAIRNESS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +6.33%; +9.00%; +23.81% |
| `results/live/V1_SIX_KUBE.md` | organism_656@10 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +7.3% (-3175 to +3893) |
| `results/live/V1_SIX_KUBE.md` | organism_656@100 | response time (ms), 95th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +12.5% (-1982 to +2695) |
| `results/live/V1_SIX_KUBE.md` | organism_656@100 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +11.1% (-1001 to +1967) |
| `results/live/V1_SIX_KUBE.md` | physics_robotics_autonomous@1000 | response time (ms), 95th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +28.6% (-4044 to +5609) |
| `results/live/V1_SIX_KUBE.md` | energy_facility_industrial@1000 | response time (ms), 95th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +17.9% (-4455 to +5669) |
| `results/live/V1_SIX_KUBE.md` | energy_facility_industrial@1000 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +22.3% (-3217 to +5916) |
| `results/live/V1_SIX_KUBE.md` | distribution_specialized@1000 | response time (ms), 95th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +33.1% (-3507 to +4954) |
| `results/live/V1_SIX_KUBE.md` | organism_656@1000 | response time (ms), 95th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +9.7% (-1991 to +2556) |
| `results/live/V1_SIX_KUBE.md` | organism_656@1000 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +4.5% (-1529 to +1971) |
| `results/live/V3_BATCH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.26%; +0.32%; +0.51% |
| `results/live/V3_FAIRNESS.md` |   | response time (ms), 95th percentile | EVEN, no difference beyond the noise in 2 of 3 runs | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +17.90%; +6.76%; +8.12% |
| `results/live/V3_FAIRNESS.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +8.20%; +8.91%; +6.68% |
| `results/live/V3_FAIRNESS.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +17.05%; +8.82%; +2.33% |
| `results/live/V3_FAIRNESS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +15.40%; +3.46%; +16.18% |
| `results/live/V3_KAFKA.md` | tuning | end-to-end latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +2.13%; +3.43%; +2.76% |
| `results/live/V3_KAFKA.md` | tuning | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.13%; +4.45%; +1.73% |
| `results/live/V3_KAFKA.md` | tuning | consumer lag, most messages waiting at once | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +1.76%; +2.76%; +0.71% |
| `results/live/V3_KAFKA.md` | tuning | consumer lag, mean messages waiting | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.12%; +4.22%; +1.28% |
| `results/live/V3_KAFKA.md` | heavy | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.04%; -0.81%; -0.09% |
| `results/live/V3_KAFKA_SERVICE.md` | burst | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.09%; -0.01%; -0.55% |
| `results/live/V3_KAFKA_SERVICE.md` | heavy | end-to-end latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.26%; +2.94%; -0.37% |
| `results/live/V3_KAFKA_SERVICE.md` | heavy | end-to-end latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.26%; +0.55%; -0.30% |
| `results/live/V3_KEDA_REQUESTS.md` |   | failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; +0.01227 (native 0) |
| `results/live/V3_KEDA_REQUESTS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +6.28%; +11.74%; +11.78% |
| `results/live/V3_PGBENCH.md` | select | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +32.94%; +0.49%; +2.29% |
| `results/live/V3_REDIS_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.76%; +0.25%; +0.30% |
| `results/live/V3_SIX_KUBE.md` | physics_robotics_autonomous@10 | response time (ms), 99th percentile | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +39.6% (-3171 to +4370) |
| `results/live/V3_SIX_KUBE.md` | energy_facility_industrial@100 | failed requests (%) | EVEN, inside the noise (up) | LOSS (not clear of the noise) | +1.5% (-1.077 to +2.178) |
| `results/live/V3_SYSBENCH.md` | read_write | work inside the response line (transactions a second answered within the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | -0.78%; -0.29%; -0.87% |
| `results/live/V3_SYSBENCH.md` | read_write | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +4.28%; +1.21%; +6.19% |
| `results/live/V3_SYSBENCH.md` | read_write | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (the same way in all three runs; 1 of 3 clear of the noise) | +1.22%; +0.55%; +4.30% |
| `results/live/V3_SYSBENCH.md` | read_write | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.72%; +0.39%; +1.86% |
| `results/live/V3_TRACE_GOOGLE2011.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +11.05%; +20.78%; +0.35% |
| `results/live/V3_YCSB.md` | tuning | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.23%; -1.15%; -0.09% |
| `results/live/V3_YCSB.md` | tuning | throughput (operations a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.24%; -1.16%; -0.10% |
| `results/live/V3_YCSB.md` | tuning | latency, 95th percentile (ms) | the runs disagree | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | -0.27%; +2.06%; +0.82% |
| `results/live/V3_YCSB.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.49%; +2.24%; -0.24% |
| `results/live/V3_YCSB.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.24%; +1.38%; +1.37% |
| `results/live/V3_YCSB.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +1.65%; +0.47%; +1.38% |
| `results/live/V3_YCSB.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +1.19%; +2.55%; +1.16% |
| `results/live/V3_YCSB.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.44%; -0.08%; +0.77% |
| `results/live/V3_YCSB.md` | c | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) | +0.87%; +1.92%; +0.11% |
| `results/live/V3_YCSB.md` | c | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.35%; +1.15%; +0.07% |
| `results/live/V3_YCSB.md` | c | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.47%; +8.46%; +0.19% |
| `results/live/V5_CAPACITY.md` |   | completed work (requests answered within the line over the window; the aim is higher) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | -4.66%; -2.66%; -2.26% |
| `results/live/V6_KEDA_CPU_REQUESTS.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.00%; +17.46%; +33.62% |
| `results/live/V6_KEDA_CPU_REQUESTS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +4.31%; +9.65%; +27.34% |
| `results/live/V6_KEDA_REQUESTS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +12.52%; +12.04%; +22.67% |
| `results/live/V7_BATCH.md` |   | batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.10%; +0.74%; +1.15% |
| `results/live/V7_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; -7.14%; -5.56% |
| `results/live/V7_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.00%; -5.56%; -8.33% |
| `results/live/V7_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; -3.23% |
| `results/live/V7_CAPACITY.md` |   | completed work (requests answered within the line over the window) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | -0.86%; -0.33%; -1.21% |
| `results/live/V7_CAPACITY.md` |   | work inside the response line (requests a second; the capacity test's own gauge) | EVEN, no difference beyond the noise (all three runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.00%; +0.00%; -8.82% |
| `results/live/V7_CRUISEKUBE.md` |   | response time (ms), mean | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.48%; +0.06%; +0.76% |
| `results/live/V7_CRUISEKUBE.md` |   | response time (ms), 99th percentile | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +3.14%; +0.02%; -0.09% |
| `results/live/V7_FAIRNESS.md` |   | second app: response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +5.90%; +5.96%; +4.48% |
| `results/live/V7_FAIRNESS.md` |   | second app: time over the response line (% of samples) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +0.14%; +1.95%; +0.79% |
| `results/live/V7_FAIRNESS.md` |   | second app: failed requests (%) | EVEN, no difference beyond the noise (all three runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.21%; +0.38%; +1.63% |
| `results/live/V7_KAFKA.md` | heavy | end-to-end latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.84%; -0.31%; -0.40% |
| `results/live/V7_KAFKA.md` | light | work inside the response line (messages a second handled within the line) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.23%; -0.84%; +0.04% |
| `results/live/V7_KEDA_REQUESTS.md` |   | pod start wait, mean (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +3.37%; +5.58%; +8.58% |
| `results/live/V7_PGBENCH.md` | simple_update | latency, median (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +2.95%; +1.11%; +0.30% |
| `results/live/V7_REDIS.md` | tuning | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.06%; +1.04%; +0.06% |
| `results/live/V7_REDIS_SERVICE.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | +0.51%; +0.28%; +0.11% |
| `results/live/V7_ROBUST_LONG.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (all three runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +94.64%; +9.84%; +162.07% |
| `results/live/V7_SYSBENCH.md` | tuning | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +1.49%; +2.27%; -0.21% |
| `results/live/V7_SYSBENCH.md` | read_write | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) | +15.31%; +0.00%; +1.82% |
| `results/live/V7_TRACE_GOOGLE2011.md` |   | pod start wait, total (s) | EVEN, no difference beyond the noise (1 of 3 runs) | LOSS (the same way in all three runs; 2 of 3 clear of the noise) | +58.92%; +25.71%; +51.70% |
| `results/live/V7_YCSB.md` | b | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +1.56%; -0.10%; +0.50% |
| `results/live/V7_YCSB.md` | b | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.00%; +0.73%; +0.53% |
| `results/live/V7_YCSB.md` | b | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (the same way in all three runs; 0 of 3 clear of the noise) | +2.53%; +1.42%; +1.42% |
| `results/live/V7_YCSB.md` | burst | work inside the response line (operations a second answered within the line) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -0.03%; -0.04%; -3.28% |
| `results/live/V7_YCSB.md` | burst | throughput (operations a second) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.03%; -0.04%; -3.24% |
| `results/live/V7_YCSB.md` | burst | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | -0.27%; -0.20%; +1.41% |
| `results/live/V7_YCSB.md` | burst | latency, 99th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.05%; +0.00%; +3.77% |
| `results/live/V7_YCSB.md` | burst | latency, mean (ms) | EVEN, no difference beyond the noise (2 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) | -0.05%; -0.42%; +4.41% |
| `results/live/V7_YCSB.md` | f | latency, 95th percentile (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.37%; +0.08%; +0.76% |
| `results/live/V7_YCSB.md` | f | latency, mean (ms) | EVEN, no difference beyond the noise (3 of 3 runs) | LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) | +0.27%; -0.19%; +0.64% |
| `results/toy_gate/SOLO_V18.md` | Omni-Compass and native against native | hpa_shortfall_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +1.13% |
| `results/toy_gate/TOY_GATE.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_base | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.10%; interval -18.88 to +20.48 |
| `results/toy_gate/TOY_GATE.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +225.77%; interval -1.37 to +29.63 |
| `results/toy_gate/TOY_GATE.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.60%; interval -0.03569 to +1.005 |
| `results/toy_gate/TOY_GATE.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +2.56%; interval -0.277 to +1.677 |
| `results/toy_gate/TOY_GATE.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.83%; interval -0.01653 to +1.017 |
| `results/toy_gate/TOY_GATE.md` | cluster15 gauges/hpa_shortfall_minutes_per_hour/base_vs_native | hpa_shortfall_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +0.60%; interval -0.002572 to +0.04632 |
| `results/toy_gate/TOY_GATE.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.47%; interval -0.1108 to +0.9108 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V10_VS_V9.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V10_VS_V9.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V10_VS_V9.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V11_VS_V10.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V11_VS_V10.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V11_VS_V10.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V11_VS_V10.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V11_VS_V10.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V11_VS_V10.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V11_VS_V10.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V12_VS_V11.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V12_VS_V11.md` | cluster candidate_as_first_pushed/gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V12_VS_V11.md` | cluster candidate_as_first_pushed/gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V12_VS_V11.md` | cluster candidate_as_first_pushed/gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 candidate_as_first_pushed/gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink candidate_as_first_pushed/gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V12_VS_V11.md` | cluster_blink candidate_as_first_pushed/gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V13_VS_V12.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V13_VS_V12.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V13_VS_V12.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V13_VS_V12.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V13_VS_V12.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V13_VS_V12.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V13_VS_V12.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V14_VS_V13.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V14_VS_V13.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V14_VS_V13.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V14_VS_V13.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V14_VS_V13.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V14_VS_V13.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V14_VS_V13.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V15_VS_V14.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V15_VS_V14.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V15_VS_V14.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V15_VS_V14.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V15_VS_V14.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V15_VS_V14.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V15_VS_V14.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V15_VS_V14.md` | card gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V15_VS_V14.md` | card gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V15_VS_V14.md` | card_floor gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V15_VS_V14.md` | card_floor gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V16_PACE.md` | pace_cloud reference_rows/pending_pod_minutes_per_hour/ref_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +155.21%; interval -7.138 to +32.54 |
| `results/toy_gate/V16_PACE.md` | pace_cloud reference_rows/alert_minutes/ref_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85%; interval -0.2741 to +1.274 |
| `results/toy_gate/V16_PACE.md` | pace_cloud against_reference/10/pending_pod_minutes_per_hour/pace_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +94.59%; interval -0.7431 to +16.22 |
| `results/toy_gate/V16_PACE.md` | pace_cloud against_reference/5/alert_minutes/pace_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85%; interval -0.1321 to +1.132 |
| `results/toy_gate/V16_PACE.md` | pace_kind against_reference/15/pending_pod_minutes_per_hour/pace_vs_ref | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.84%; interval -1.117 to +4.209 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V16_VS_V15.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V16_VS_V15.md` | cluster15 gauges/pending_pod_minutes_per_hour/cand_vs_base | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.63%; interval -1.062 to +2.497 |
| `results/toy_gate/V16_VS_V15.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V16_VS_V15.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V16_VS_V15.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V16_VS_V15.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V16_VS_V15.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V16_VS_V15.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V16_VS_V15.md` | cluster_shipped gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V16_VS_V15.md` | cluster_shipped gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V16_VS_V15.md` | cluster_shipped gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V16_VS_V15.md` | cluster_shipped gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V16_VS_V15.md` | card gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V16_VS_V15.md` | card gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V16_VS_V15.md` | card_floor gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V16_VS_V15.md` | card_floor gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/5/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/10/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +94.59% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/30/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.39% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/60/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +155.21% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/60/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/75/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +135.88% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/75/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.39% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/90/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +123.25% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/90/p95_ms/vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.51% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/90/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +2.31% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/120/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +71.22% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/20/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +84.89% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/20/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/40/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +2.49% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/40/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +161.58% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/40/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/45/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +127.52% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/45/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.85% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/50/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +23.01% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/50/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +213.92% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/50/p95_ms/vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.72% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/50/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/15/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.84% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/30/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +6.65% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/90/hpa_shortfall_minutes_per_hour/vs_main | hpa_shortfall_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +1.46% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/120/hpa_shortfall_minutes_per_hour/vs_main | hpa_shortfall_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.17% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/120/hpa_shortfall_minutes_per_hour/vs_native | hpa_shortfall_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +2.85% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/40/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +2.97% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/45/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +2.17% |
| `results/toy_gate/V17_LADDER.md` | pace_kind/rows/50/pending_pod_minutes_per_hour/vs_main | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +5.18% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_cloud/90/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +123.25% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_cloud/90/p95_ms/vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.51% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_cloud/90/alert_minutes/vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +2.31% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_cloud/120/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +71.22% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_kind/90/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +58.65% |
| `results/toy_gate/V17_LADDER.md` | toys/pace_kind/120/pending_pod_minutes_per_hour/vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +14.40% |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V17_VS_V16.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V17_VS_V16.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V17_VS_V16.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V17_VS_V16.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V17_VS_V16.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V17_VS_V16.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V17_VS_V16.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/pending_pod_minutes_per_hour/cand_vs_base | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +39.84%; interval -10.1 to +23.01 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/alert_minutes/cand_vs_base | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93%; interval -0.1371 to +0.6371 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V17_VS_V16.md` | card gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V17_VS_V16.md` | card gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V17_VS_V16.md` | card_floor gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V17_VS_V16.md` | card_floor gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V18_VS_V17.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V18_VS_V17.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V18_VS_V17.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.94%; interval -0.3413 to +0.8413 |
| `results/toy_gate/V18_VS_V17.md` | cluster_blink gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V18_VS_V17.md` | cluster_blink gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +204.86%; interval -3.206 to +33.16 |
| `results/toy_gate/V18_VS_V17.md` | cluster_blink gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V18_VS_V17.md` | cluster_blink gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.69%; interval -0.09359 to +1.199 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V18_VS_V17.md` | cluster_shipped gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V18_VS_V17.md` | card gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V18_VS_V17.md` | card gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +0.94%; interval -4.204 to +11.33 |
| `results/toy_gate/V18_VS_V17.md` | card_floor gauges/p99_ms/base_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V18_VS_V17.md` | card_floor gauges/p99_ms/cand_vs_native | p99_ms | EVEN | LOSS (not clear of the noise) | +4.59%; interval -4.183 to +39.14 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.897 to +35.58 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.897 to +35.58 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1676 to +1.179 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1676 to +1.179 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1548 to +1.155 |
| `results/toy_gate/V8_VS_V7.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1548 to +1.155 |
| `results/toy_gate/V8_VS_V7.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2695 to +1.019 |
| `results/toy_gate/V8_VS_V7.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2695 to +1.019 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/pending_pod_minutes_per_hour/base_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/pending_pod_minutes_per_hour/cand_vs_native | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +209.81%; interval -4.195 to +34.87 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/p95_ms/base_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/p95_ms/cand_vs_native | p95_ms | EVEN | LOSS (not clear of the noise) | +0.63%; interval -0.1442 to +1.156 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V9_VS_V8.md` | cluster gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.88%; interval -0.1321 to +1.132 |
| `results/toy_gate/V9_VS_V8.md` | cluster15 gauges/alert_minutes/base_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/V9_VS_V8.md` | cluster15 gauges/alert_minutes/cand_vs_native | alert_minutes | EVEN | LOSS (not clear of the noise) | +1.41%; interval -0.2471 to +0.9971 |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|20/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +22.17% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|30/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +16.36% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|60/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +63.72% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|75/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +85.47% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|75/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +13.28% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|90/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +36.16% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|120/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +160.06% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v16|120/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +58.84% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v15|10/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.05% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v15|30/vs_15/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +28.77% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v15|75/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +13.28% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v15|90/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +36.16% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | onsite|omni-v15|120/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +58.84% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_native/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_15/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.64% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_15/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.02% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|5/vs_60/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_native/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_15/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.64% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_15/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.82% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|10/vs_60/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|20/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +9.24% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|20/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +1.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|30/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +10.99% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|30/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +3.21% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|60/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.53% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|75/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +9.51% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|75/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +1.84% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|90/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +8.25% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|90/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|90/vs_15/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.56% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|90/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +0.66% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|90/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v16|120/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|5/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|5/vs_native/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|5/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +12.09% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|5/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|5/vs_60/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|10/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|10/vs_native/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|10/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.82% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|10/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.67% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|10/vs_60/alert_minutes | alert_minutes | EVEN | LOSS (not clear of the noise) | +0.93% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|15/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.61% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|15/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +13.61% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|15/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.61% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|20/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +13.21% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|20/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|20/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +5.28% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|20/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|30/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +10.99% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|30/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +3.21% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|60/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +7.53% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|75/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +9.51% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|75/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +1.84% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|90/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +8.25% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|90/vs_native/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|90/vs_60/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +0.66% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|90/vs_60/p99_ms | p99_ms | EVEN | LOSS (not clear of the noise) | +0.59% |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | cloud|omni-v15|120/vs_native/pending_pod_minutes_per_hour | pending_pod_minutes_per_hour | EVEN | LOSS (not clear of the noise) | +4.93% |

## Every LOSS that now reads EVEN, under the floor

A LOSS whose change was under 0.5% in every run now reads EVEN, under the floor, by the founder's floor; each is named here so none is lost from sight.

| Page | Where | Gauge | Before | Now | The runs' changes |
|---|---|---|---|---|---|
| `results/live/V1_BIG_ORGANISM.md` | organism_656@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-9.426e+07 to -9.426e+07) |
| `results/live/V1_BIG_ORGANISM.md` | stack_1226@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-5.684e+08 to -5.684e+08) |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2022_phase_all_robustness | monthly load unevenness (`monthly_one_minus_load_factor_average`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.11%) | +0.11%; +0.11%; +0.11% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_local_evaluation | monthly load unevenness (`monthly_one_minus_load_factor_average`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.07%) | +0.07%; +0.07%; +0.07% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_local_evaluation | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.12%) | +0.12%; +0.12%; +0.12% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.15%) | +0.15%; +0.15%; +0.15% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.09%) | +0.09%; +0.09%; +0.09% |
| `results/live/V1_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_3 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.01%) | +0.01%; +0.01%; +0.01% |
| `results/live/V1_SIX_KUBE.md` | stack_1226@10 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-2.8e+06 to -2.8e+06) |
| `results/live/V1_SIX_KUBE.md` | compute_ai_cloud@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-1.614e+07 to -1.614e+07) |
| `results/live/V1_SIX_KUBE.md` | physics_robotics_autonomous@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-9.249e+06 to -9.249e+06) |
| `results/live/V1_SIX_KUBE.md` | distribution_specialized@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-1.06e+07 to -1.06e+07) |
| `results/live/V1_SIX_KUBE.md` | stack_1226@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-6.349e+07 to -6.349e+07) |
| `results/live/V1_SIX_KUBE.md` | compute_ai_cloud@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-5.925e+08 to -5.925e+08) |
| `results/live/V1_SIX_KUBE.md` | physics_robotics_autonomous@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-5.354e+08 to -5.354e+08) |
| `results/live/V1_SIX_KUBE.md` | distribution_specialized@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-5.934e+08 to -5.934e+08) |
| `results/live/V1_SIX_KUBE.md` | organism_656@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-9.426e+07 to -9.426e+07) |
| `results/live/V3_BIG_ORGANISM.md` | tower@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-2.402e+08 to -2.402e+08) |
| `results/live/V3_BIG_ORGANISM.md` | stack@1000 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-7.813e+08 to -7.813e+08) |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2022_phase_all_robustness | monthly load unevenness (`monthly_one_minus_load_factor_average`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.11%) | +0.11%; +0.11%; +0.11% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_local_evaluation | monthly load unevenness (`monthly_one_minus_load_factor_average`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.07%) | +0.07%; +0.07%; +0.07% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_local_evaluation | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.12%) | +0.12%; +0.12%; +0.12% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.15%) | +0.15%; +0.15%; +0.15% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.09%) | +0.09%; +0.09%; +0.09% |
| `results/live/V3_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_3 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.01%) | +0.01%; +0.01%; +0.01% |
| `results/live/V3_SIX_KUBE.md` | stack@10 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-7.802e+06 to -7.802e+06) |
| `results/live/V3_SIX_KUBE.md` | compute_ai_cloud@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-1.579e+07 to -1.579e+07) |
| `results/live/V3_SIX_KUBE.md` | physics_robotics_autonomous@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-2.232e+07 to -2.232e+07) |
| `results/live/V3_SIX_KUBE.md` | stack@100 | organism work | LOSS | EVEN, under the floor (cut 0.00%) | -0.0% (-9.978e+07 to -9.978e+07) |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_local_evaluation | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.12%) | +0.12%; +0.12%; +0.12% |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_2_online_evaluation_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.15%) | +0.15%; +0.15%; +0.15% |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_1 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.02%) | +0.02%; +0.02%; +0.02% |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_2 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.09%) | +0.09%; +0.09%; +0.09% |
| `results/live/V7_CITYLEARN.md` | Districts with electric batteries / citylearn_challenge_2023_phase_3_3 | time uncomfortable (`discomfort_proportion`) | LOSS in all three of our runs | EVEN, under the floor (every run under 0.5%; the largest 0.01%) | +0.01%; +0.01%; +0.01% |
| `results/toy_gate/TOY_GATE.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.30%; interval +0.04582 to +0.437 |
| `results/toy_gate/V10_VS_V9.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V10_VS_V9.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V11_VS_V10.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V11_VS_V10.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V12_VS_V11.md` | cluster15 candidate_as_first_pushed/gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V13_VS_V12.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V13_VS_V12.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V13_VS_V12.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V14_VS_V13.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V14_VS_V13.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V14_VS_V13.md` | convey_batch gauges/batch_turnaround_s/base_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V14_VS_V13.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V15_VS_V14.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V15_VS_V14.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V15_VS_V14.md` | convey_batch gauges/batch_turnaround_s/base_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V15_VS_V14.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V16_PACE.md` | pace_cloud against_reference/15/p95_ms/pace_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.47%; interval +0.112 to +0.6394 |
| `results/toy_gate/V16_VS_V15.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V16_VS_V15.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V16_VS_V15.md` | cluster_shipped gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V16_VS_V15.md` | convey_batch gauges/batch_turnaround_s/base_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V16_VS_V15.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/15/p95_ms/vs_native | p95_ms | LOSS | EVEN, under the floor | +0.47% |
| `results/toy_gate/V17_LADDER.md` | pace_cloud/rows/30/p95_ms/vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36% |
| `results/toy_gate/V17_VS_V16.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V17_VS_V16.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V17_VS_V16.md` | cluster_shipped gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V17_VS_V16.md` | convey_batch gauges/batch_turnaround_s/base_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V17_VS_V16.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V18_VS_V17.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V18_VS_V17.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.36%; interval +0.04679 to +0.5279 |
| `results/toy_gate/V18_VS_V17.md` | convey_batch gauges/batch_turnaround_s/base_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V18_VS_V17.md` | convey_batch gauges/batch_turnaround_s/cand_vs_native | batch_turnaround_s | LOSS | EVEN, under the floor | +0.05%; interval +0.02453 to +0.1213 |
| `results/toy_gate/V8_VS_V7.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.01676 to +0.5155 |
| `results/toy_gate/V8_VS_V7.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.01676 to +0.5155 |
| `results/toy_gate/V9_VS_V8.md` | cluster15 gauges/p95_ms/base_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |
| `results/toy_gate/V9_VS_V8.md` | cluster15 gauges/p95_ms/cand_vs_native | p95_ms | LOSS | EVEN, under the floor | +0.33%; interval +0.02541 to +0.5068 |

## Page by page

| Page | What moved |
|---|---|
| `results/live/SIX_KUBE.md` | 29 EVEN to GAIN; 18 GAIN to EVEN; 10 EVEN to EVEN; 2 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V10_ALL_FOUR.md` | 3 EVEN to EVEN; 2 EVEN to GAIN; 2 EVEN to power given; 1 EVEN to the runs disagree |
| `results/live/V10_BATCH.md` | 4 EVEN to LOSS; 3 EVEN to GAIN; 2 EVEN to power given; 1 EVEN to EVEN; 1 EVEN to the runs disagree |
| `results/live/V10_CAPACITY.md` | 4 EVEN to GAIN; 2 EVEN to the runs disagree; 2 EVEN to LOSS |
| `results/live/V10_CITYLEARN.md` | 2 GAIN to EVEN; 1 power given to EVEN |
| `results/live/V10_CRUISEKUBE.md` | 3 EVEN to EVEN; 3 EVEN to LOSS; 3 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to power given |
| `results/live/V10_FAIRNESS.md` | 7 EVEN to the runs disagree; 5 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V10_FAULTS.md` | 4 EVEN to EVEN; 3 EVEN to the runs disagree; 2 EVEN to GAIN |
| `results/live/V10_GOLDILOCKS.md` | 3 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V10_KAFKA.md` | 15 EVEN to the runs disagree; 12 EVEN to GAIN; 10 EVEN to LOSS; 7 EVEN to EVEN; 4 EVEN to power given; 1 GAIN to EVEN |
| `results/live/V10_KAFKA_SERVICE.md` | 15 EVEN to GAIN; 12 EVEN to the runs disagree; 8 EVEN to EVEN; 8 EVEN to LOSS; 2 GAIN to EVEN; 2 EVEN to power given; 1 the runs disagree to power given |
| `results/live/V10_KEDA_CPU_REQUESTS.md` | 2 EVEN to GAIN; 2 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V10_KEDA_REQUESTS.md` | 1 EVEN to EVEN; 1 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V10_PANDAPOWER.md` | 10 GAIN to EVEN; 4 power given to EVEN |
| `results/live/V10_PGBENCH.md` | 14 EVEN to GAIN; 11 EVEN to the runs disagree; 3 EVEN to EVEN; 3 EVEN to power given |
| `results/live/V10_REDIS.md` | 13 EVEN to EVEN; 8 EVEN to GAIN; 8 EVEN to the runs disagree; 4 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V10_REDIS_SERVICE.md` | 13 EVEN to the runs disagree; 11 EVEN to EVEN; 4 EVEN to GAIN; 3 EVEN to LOSS |
| `results/live/V10_ROBUST_LONG.md` | 5 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V10_STEADY.md` | 3 EVEN to EVEN; 3 EVEN to GAIN; 1 EVEN to the runs disagree |
| `results/live/V10_SYSBENCH.md` | 17 EVEN to the runs disagree; 16 EVEN to GAIN; 11 EVEN to EVEN; 6 EVEN to LOSS; 5 EVEN to power given |
| `results/live/V10_TRACE_GOOGLE2011.md` | 2 GAIN to EVEN; 1 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V10_WANDERING.md` | 2 GAIN to EVEN; 2 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V10_YCSB.md` | 18 EVEN to GAIN; 16 EVEN to the runs disagree; 9 EVEN to EVEN; 3 EVEN to LOSS; 3 EVEN to power given |
| `results/live/V11_CAPACITY.md` | 5 EVEN to LOSS; 2 EVEN to the runs disagree; 1 EVEN to GAIN |
| `results/live/V11_CITYLEARN.md` | 2 GAIN to EVEN; 1 power given to EVEN |
| `results/live/V11_GOLDILOCKS.md` | 1 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to GAIN |
| `results/live/V11_KAFKA.md` | 16 EVEN to the runs disagree; 15 EVEN to GAIN; 9 EVEN to EVEN; 6 EVEN to power given; 4 EVEN to LOSS |
| `results/live/V11_KAFKA_SERVICE.md` | 13 EVEN to the runs disagree; 13 EVEN to GAIN; 10 EVEN to EVEN; 7 EVEN to power given; 5 EVEN to LOSS; 1 GAIN to EVEN |
| `results/live/V11_KEDA_CPU_REQUESTS.md` | 3 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to EVEN |
| `results/live/V11_KEDA_REQUESTS.md` | 2 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V11_PANDAPOWER.md` | 10 GAIN to EVEN; 4 power given to EVEN |
| `results/live/V11_PGBENCH.md` | 11 EVEN to EVEN; 8 EVEN to the runs disagree; 7 EVEN to GAIN; 4 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V11_PGBENCH_SERVICE.md` | 11 EVEN to the runs disagree; 9 EVEN to power given; 8 EVEN to EVEN; 2 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V11_REDIS.md` | 14 EVEN to EVEN; 12 EVEN to the runs disagree; 4 EVEN to GAIN; 4 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V11_REDIS_SERVICE.md` | 14 EVEN to EVEN; 13 EVEN to the runs disagree; 5 EVEN to GAIN; 3 EVEN to power given |
| `results/live/V11_REDIS_SHIPPED.md` | 21 EVEN to EVEN; 14 EVEN to the runs disagree; 3 EVEN to LOSS; 1 power given to EVEN |
| `results/live/V11_ROBUST_KILL.md` | 6 EVEN to the runs disagree; 3 EVEN to EVEN |
| `results/live/V11_ROBUST_LONG.md` | 3 EVEN to EVEN; 3 EVEN to GAIN; 1 EVEN to power given; 1 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V11_SYSBENCH.md` | 23 EVEN to the runs disagree; 16 EVEN to GAIN; 8 EVEN to EVEN; 5 EVEN to LOSS; 2 the runs disagree to EVEN; 1 EVEN to power given |
| `results/live/V11_SYSBENCH_SERVICE.md` | 23 EVEN to the runs disagree; 17 EVEN to GAIN; 12 EVEN to EVEN; 2 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V11_SYSBENCH_SHIPPED.md` | 13 EVEN to EVEN; 12 EVEN to the runs disagree; 12 EVEN to power given; 9 EVEN to LOSS; 4 EVEN to GAIN |
| `results/live/V11_YCSB.md` | 17 EVEN to GAIN; 15 EVEN to the runs disagree; 10 EVEN to EVEN; 4 EVEN to LOSS; 3 EVEN to power given |
| `results/live/V11_YCSB_SERVICE.md` | 16 EVEN to GAIN; 11 EVEN to the runs disagree; 10 EVEN to EVEN; 6 EVEN to power given; 5 EVEN to LOSS; 1 GAIN to GAIN |
| `results/live/V11_YCSB_SHIPPED.md` | 19 EVEN to the runs disagree; 12 EVEN to EVEN; 7 EVEN to LOSS; 4 EVEN to GAIN; 3 EVEN to power given |
| `results/live/V12_ARMADA_4W_BARE.md` | 7 EVEN to LOSS; 5 EVEN to GAIN; 3 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_ARMADA_4W_BOTH.md` | 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V12_ARMADA_4W_ORCH.md` | 3 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to power given |
| `results/live/V12_ARMADA_4W_TOP.md` | 5 EVEN to EVEN; 2 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V12_ARMADA_4W_VS.md` | 3 EVEN to GAIN; 3 EVEN to the runs disagree; 1 EVEN to LOSS; 1 EVEN to power given |
| `results/live/V12_BINPACK.md` | 6 EVEN to LOSS; 2 EVEN to EVEN; 2 EVEN to the runs disagree; 1 EVEN to GAIN; 1 EVEN to power given |
| `results/live/V12_BINPACK_4W_BARE.md` | 5 EVEN to LOSS; 5 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to power given |
| `results/live/V12_BINPACK_4W_BOTH.md` | 5 EVEN to the runs disagree; 4 EVEN to LOSS; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_BINPACK_4W_ORCH.md` | 7 EVEN to the runs disagree; 4 EVEN to EVEN; 2 EVEN to GAIN; 1 EVEN to LOSS; 1 EVEN to power given |
| `results/live/V12_BINPACK_4W_TOP.md` | 5 EVEN to the runs disagree; 3 EVEN to LOSS; 2 EVEN to EVEN; 2 EVEN to power given; 1 EVEN to GAIN |
| `results/live/V12_BINPACK_4W_VS.md` | 5 EVEN to the runs disagree; 4 EVEN to GAIN; 3 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_CRANE_4W_BARE.md` | 4 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V12_CRANE_4W_BOTH.md` | 5 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to LOSS |
| `results/live/V12_CRANE_4W_ORCH.md` | 4 EVEN to the runs disagree; 3 EVEN to GAIN; 3 EVEN to power given |
| `results/live/V12_CRANE_4W_TOP.md` | 4 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V12_CRANE_4W_VS.md` | 5 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to the runs disagree; 1 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V12_KAFKA.md` | 19 EVEN to the runs disagree; 10 EVEN to GAIN; 7 EVEN to EVEN; 7 EVEN to LOSS; 5 EVEN to power given; 1 GAIN to EVEN |
| `results/live/V12_KAFKA_SERVICE.md` | 16 EVEN to GAIN; 14 EVEN to the runs disagree; 7 EVEN to LOSS; 6 EVEN to EVEN; 6 EVEN to power given; 1 GAIN to EVEN; 1 the runs disagree to power given |
| `results/live/V12_KAI.md` | 6 EVEN to the runs disagree; 5 EVEN to LOSS; 2 EVEN to EVEN |
| `results/live/V12_KAI_4W_BARE.md` | 7 EVEN to the runs disagree; 3 EVEN to LOSS; 2 EVEN to GAIN; 1 EVEN to EVEN |
| `results/live/V12_KAI_4W_BOTH.md` | 4 EVEN to GAIN; 4 EVEN to LOSS; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_KAI_4W_ORCH.md` | 3 EVEN to EVEN; 3 EVEN to the runs disagree; 1 EVEN to GAIN; 1 EVEN to LOSS; 1 EVEN to power given |
| `results/live/V12_KAI_4W_TOP.md` | 6 EVEN to LOSS; 4 EVEN to GAIN; 3 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_KAI_4W_VS.md` | 3 EVEN to GAIN; 2 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to LOSS |
| `results/live/V12_KARMADA_4W_BARE.md` | 9 EVEN to LOSS; 4 EVEN to GAIN; 3 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_KARMADA_4W_BOTH.md` | 4 EVEN to GAIN; 4 EVEN to LOSS; 2 EVEN to power given |
| `results/live/V12_KARMADA_4W_ORCH.md` | 6 EVEN to LOSS; 3 EVEN to EVEN; 2 EVEN to power given |
| `results/live/V12_KARMADA_4W_TOP.md` | 9 EVEN to LOSS; 4 EVEN to GAIN; 3 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_KARMADA_4W_VS.md` | 8 EVEN to GAIN; 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_KOORDINATOR.md` | 6 EVEN to GAIN; 4 EVEN to the runs disagree; 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | 7 EVEN to the runs disagree; 4 EVEN to LOSS; 1 EVEN to EVEN; 1 EVEN to GAIN |
| `results/live/V12_KOORDINATOR_4W_BOTH.md` | 6 EVEN to GAIN; 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V12_KOORDINATOR_4W_ORCH.md` | 4 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | 8 EVEN to the runs disagree; 6 EVEN to GAIN; 3 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_KOORDINATOR_4W_VS.md` | 4 EVEN to the runs disagree; 2 EVEN to LOSS; 1 EVEN to EVEN; 1 EVEN to GAIN |
| `results/live/V12_KUBERAY_4W_BARE.md` | 6 EVEN to LOSS; 2 EVEN to power given; 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to the runs disagree |
| `results/live/V12_KUBERAY_4W_BOTH.md` | 3 EVEN to GAIN; 2 EVEN to the runs disagree; 2 EVEN to power given; 2 EVEN to LOSS |
| `results/live/V12_KUBERAY_4W_ORCH.md` | 2 EVEN to the runs disagree; 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_KUBERAY_4W_TOP.md` | 8 EVEN to GAIN; 6 EVEN to the runs disagree; 2 EVEN to EVEN; 2 EVEN to LOSS |
| `results/live/V12_KUBERAY_4W_VS.md` | 5 EVEN to the runs disagree; 1 EVEN to power given |
| `results/live/V12_KUEUE_4W_BARE.md` | 5 EVEN to LOSS; 3 EVEN to the runs disagree; 3 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_KUEUE_4W_BOTH.md` | 7 EVEN to LOSS; 2 EVEN to GAIN; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_KUEUE_4W_ORCH.md` | 7 EVEN to LOSS; 3 EVEN to EVEN; 2 EVEN to power given |
| `results/live/V12_KUEUE_4W_TOP.md` | 6 EVEN to the runs disagree; 5 EVEN to LOSS; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_KUEUE_4W_VS.md` | 9 EVEN to GAIN; 1 EVEN to EVEN |
| `results/live/V12_OCM_4W_BARE.md` | 7 EVEN to GAIN; 7 EVEN to LOSS; 2 EVEN to the runs disagree; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_OCM_4W_BOTH.md` | 4 EVEN to GAIN; 3 EVEN to LOSS; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V12_OCM_4W_ORCH.md` | 7 EVEN to LOSS; 4 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to the runs disagree |
| `results/live/V12_OCM_4W_TOP.md` | 9 EVEN to LOSS; 4 EVEN to GAIN; 2 EVEN to power given; 2 EVEN to the runs disagree |
| `results/live/V12_OCM_4W_VS.md` | 12 EVEN to GAIN; 2 EVEN to power given |
| `results/live/V12_PGBENCH.md` | 18 EVEN to the runs disagree; 7 EVEN to power given; 3 EVEN to EVEN; 3 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V12_PGBENCH_SERVICE.md` | 10 EVEN to the runs disagree; 8 EVEN to LOSS; 7 EVEN to power given; 5 EVEN to EVEN; 2 EVEN to GAIN |
| `results/live/V12_REDIS.md` | 13 EVEN to GAIN; 13 EVEN to EVEN; 6 EVEN to the runs disagree; 3 EVEN to power given |
| `results/live/V12_REDIS_SERVICE.md` | 12 EVEN to EVEN; 10 EVEN to the runs disagree; 6 EVEN to power given; 3 EVEN to LOSS; 2 EVEN to GAIN |
| `results/live/V12_REDIS_SHIPPED.md` | 21 EVEN to EVEN; 11 EVEN to the runs disagree; 5 EVEN to GAIN; 2 power given to EVEN |
| `results/live/V12_SYSBENCH.md` | 21 EVEN to GAIN; 10 EVEN to the runs disagree; 8 EVEN to EVEN; 8 EVEN to power given; 7 EVEN to LOSS |
| `results/live/V12_SYSBENCH_SERVICE.md` | 24 EVEN to the runs disagree; 13 EVEN to GAIN; 10 EVEN to EVEN; 7 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V12_SYSBENCH_SHIPPED.md` | 18 EVEN to the runs disagree; 13 EVEN to GAIN; 10 EVEN to power given; 9 EVEN to EVEN; 2 EVEN to LOSS |
| `results/live/V12_VANILLA.md` | 5 EVEN to the runs disagree; 3 EVEN to LOSS; 2 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_VOLCANO_4W_BARE.md` | 7 EVEN to GAIN; 5 EVEN to LOSS; 2 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_VOLCANO_4W_BOTH.md` | 4 EVEN to GAIN; 2 EVEN to LOSS; 1 EVEN to EVEN; 1 EVEN to the runs disagree; 1 EVEN to power given |
| `results/live/V12_VOLCANO_4W_ORCH.md` | 5 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to the runs disagree |
| `results/live/V12_VOLCANO_4W_TOP.md` | 5 EVEN to LOSS; 5 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V12_VOLCANO_4W_VS.md` | 4 EVEN to the runs disagree; 3 EVEN to GAIN; 3 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V12_YCSB_SERVICE.md` | 11 EVEN to the runs disagree; 4 EVEN to EVEN; 3 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V12_YCSB_SHIPPED.md` | 3 EVEN to EVEN; 3 EVEN to GAIN; 2 EVEN to LOSS; 1 EVEN to the runs disagree |
| `results/live/V14_PGBENCH_SERVICE.md` | 13 EVEN to the runs disagree; 6 EVEN to EVEN; 5 EVEN to power given; 4 EVEN to GAIN; 3 EVEN to LOSS |
| `results/live/V14_SYSBENCH_SERVICE.md` | 22 EVEN to the runs disagree; 14 EVEN to GAIN; 10 EVEN to EVEN; 7 EVEN to power given; 2 EVEN to LOSS |
| `results/live/V14_YCSB_SERVICE.md` | 14 EVEN to the runs disagree; 12 EVEN to GAIN; 10 EVEN to LOSS; 9 EVEN to EVEN; 3 EVEN to power given; 1 GAIN to GAIN |
| `results/live/V14_YCSB_SHIPPED.md` | 14 EVEN to the runs disagree; 12 EVEN to EVEN; 11 EVEN to LOSS; 6 EVEN to power given; 2 EVEN to GAIN |
| `results/live/V16_KAFKA.md` | 18 EVEN to the runs disagree; 12 EVEN to GAIN; 8 EVEN to EVEN; 6 EVEN to LOSS; 3 EVEN to power given; 1 the runs disagree to power given; 1 GAIN to EVEN |
| `results/live/V16_KAFKA_SERVICE.md` | 21 EVEN to the runs disagree; 10 EVEN to GAIN; 9 EVEN to power given; 7 EVEN to EVEN; 2 EVEN to LOSS |
| `results/live/V16_PGBENCH.md` | 11 EVEN to the runs disagree; 9 EVEN to power given; 5 EVEN to LOSS; 4 EVEN to EVEN; 3 EVEN to GAIN |
| `results/live/V16_PGBENCH_SERVICE.md` | 14 EVEN to the runs disagree; 7 EVEN to LOSS; 5 EVEN to power given; 3 EVEN to GAIN; 2 EVEN to EVEN |
| `results/live/V16_REDIS.md` | 12 EVEN to EVEN; 11 EVEN to GAIN; 7 EVEN to power given; 4 EVEN to the runs disagree |
| `results/live/V16_REDIS_SERVICE.md` | 12 EVEN to EVEN; 6 EVEN to GAIN; 6 EVEN to the runs disagree; 5 EVEN to power given; 2 EVEN to LOSS |
| `results/live/V16_REDIS_SHIPPED.md` | 23 EVEN to EVEN; 12 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V16_SYSBENCH.md` | 19 EVEN to the runs disagree; 17 EVEN to GAIN; 10 EVEN to EVEN; 6 EVEN to power given; 3 EVEN to LOSS |
| `results/live/V16_SYSBENCH_SERVICE.md` | 21 EVEN to the runs disagree; 16 EVEN to GAIN; 10 EVEN to EVEN; 8 EVEN to power given |
| `results/live/V16_SYSBENCH_SHIPPED.md` | 13 EVEN to EVEN; 13 EVEN to the runs disagree; 13 EVEN to power given; 12 EVEN to GAIN; 2 EVEN to LOSS |
| `results/live/V16_YCSB.md` | 14 EVEN to the runs disagree; 12 EVEN to EVEN; 10 EVEN to LOSS; 7 EVEN to GAIN; 5 EVEN to power given |
| `results/live/V16_YCSB_SERVICE.md` | 13 EVEN to EVEN; 10 EVEN to the runs disagree; 9 EVEN to power given; 9 EVEN to GAIN; 7 EVEN to LOSS |
| `results/live/V16_YCSB_SHIPPED.md` | 20 EVEN to the runs disagree; 15 EVEN to EVEN; 8 EVEN to LOSS; 2 EVEN to GAIN |
| `results/live/V1_ALL_FOUR.md` | 7 EVEN to GAIN; 1 EVEN to EVEN |
| `results/live/V1_BATCH.md` | 3 EVEN to the runs disagree; 2 EVEN to LOSS; 2 EVEN to GAIN; 2 EVEN to power given; 1 EVEN to EVEN |
| `results/live/V1_BIG_ORGANISM.md` | 6 EVEN to EVEN; 5 GAIN to EVEN; 3 EVEN to GAIN; 2 LOSS to EVEN |
| `results/live/V1_CITYLEARN.md` | 25 GAIN to EVEN; 8 LOSS to EVEN; 8 power given to EVEN |
| `results/live/V1_FAIRNESS.md` | 10 EVEN to the runs disagree; 3 EVEN to EVEN; 2 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V1_FAULTS.md` | 4 EVEN to EVEN; 3 EVEN to GAIN; 2 EVEN to the runs disagree; 1 EVEN to power given |
| `results/live/V1_PANDAPOWER.md` | 10 GAIN to EVEN; 4 power given to EVEN |
| `results/live/V1_SIX_KUBE.md` | 84 EVEN to GAIN; 62 EVEN to EVEN; 57 GAIN to EVEN; 9 EVEN to LOSS; 9 LOSS to EVEN; 8 EVEN to power given |
| `results/live/V1_STEADY.md` | 3 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to GAIN |
| `results/live/V1_WANDERING.md` | 6 EVEN to GAIN; 1 GAIN to EVEN; 1 GAIN to GAIN |
| `results/live/V3_ALL_FOUR.md` | 5 EVEN to GAIN; 4 EVEN to EVEN |
| `results/live/V3_BATCH.md` | 5 EVEN to the runs disagree; 3 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to LOSS |
| `results/live/V3_BIG_ORGANISM.md` | 5 GAIN to EVEN; 4 EVEN to EVEN; 3 EVEN to GAIN; 2 LOSS to EVEN |
| `results/live/V3_CITYLEARN.md` | 25 GAIN to EVEN; 8 LOSS to EVEN; 8 power given to EVEN |
| `results/live/V3_FAIRNESS.md` | 5 EVEN to GAIN; 4 EVEN to LOSS; 3 EVEN to EVEN; 3 EVEN to the runs disagree; 1 EVEN to power given |
| `results/live/V3_FAULTS.md` | 5 EVEN to GAIN; 2 EVEN to the runs disagree; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V3_KAFKA.md` | 15 EVEN to the runs disagree; 14 EVEN to EVEN; 10 EVEN to GAIN; 5 EVEN to LOSS; 4 EVEN to power given; 1 GAIN to EVEN |
| `results/live/V3_KAFKA_SERVICE.md` | 21 EVEN to GAIN; 11 EVEN to the runs disagree; 8 EVEN to EVEN; 5 EVEN to power given; 3 EVEN to LOSS; 1 GAIN to EVEN |
| `results/live/V3_KEDA_CPU_REQUESTS.md` | 3 EVEN to GAIN; 3 EVEN to power given; 2 EVEN to the runs disagree |
| `results/live/V3_KEDA_REQUESTS.md` | 3 EVEN to GAIN; 2 EVEN to LOSS |
| `results/live/V3_PANDAPOWER.md` | 10 GAIN to EVEN; 4 power given to EVEN |
| `results/live/V3_PGBENCH.md` | 12 EVEN to the runs disagree; 9 EVEN to GAIN; 4 EVEN to EVEN; 4 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V3_REDIS.md` | 15 EVEN to EVEN; 10 EVEN to GAIN; 9 EVEN to the runs disagree; 4 EVEN to power given |
| `results/live/V3_REDIS_SERVICE.md` | 14 EVEN to EVEN; 12 EVEN to the runs disagree; 2 EVEN to GAIN; 2 EVEN to power given; 1 GAIN to GAIN; 1 EVEN to LOSS |
| `results/live/V3_ROBUST_KILL.md` | 6 EVEN to GAIN; 3 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to the runs disagree |
| `results/live/V3_ROBUST_LONG.md` | 8 EVEN to GAIN; 4 EVEN to the runs disagree; 1 EVEN to EVEN |
| `results/live/V3_SIX_KUBE.md` | 34 EVEN to GAIN; 33 GAIN to EVEN; 30 EVEN to EVEN; 8 EVEN to power given; 4 LOSS to EVEN; 2 EVEN to LOSS |
| `results/live/V3_STEADY.md` | 4 EVEN to GAIN; 1 EVEN to the runs disagree |
| `results/live/V3_SYSBENCH.md` | 17 EVEN to the runs disagree; 14 EVEN to EVEN; 14 EVEN to GAIN; 6 EVEN to power given; 4 EVEN to LOSS |
| `results/live/V3_TRACE_GOOGLE2011.md` | 1 GAIN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V3_WANDERING.md` | 8 EVEN to GAIN; 1 GAIN to EVEN |
| `results/live/V3_YCSB.md` | 14 EVEN to GAIN; 13 EVEN to the runs disagree; 10 EVEN to LOSS; 8 EVEN to EVEN; 1 the runs disagree to LOSS |
| `results/live/V5_CAPACITY.md` | 6 EVEN to the runs disagree; 1 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V5_GOLDILOCKS.md` | 3 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V6_CRUISEKUBE.md` | 9 EVEN to the runs disagree; 3 EVEN to GAIN; 1 EVEN to power given |
| `results/live/V6_GOLDILOCKS.md` | 4 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V6_KEDA_CPU_REQUESTS.md` | 3 EVEN to GAIN; 2 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V6_KEDA_REQUESTS.md` | 2 EVEN to GAIN; 1 EVEN to the runs disagree; 1 EVEN to LOSS |
| `results/live/V7_ALL_FOUR.md` | 3 EVEN to EVEN; 2 EVEN to GAIN; 2 EVEN to the runs disagree; 1 EVEN to power given |
| `results/live/V7_BATCH.md` | 5 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V7_CAPACITY.md` | 5 EVEN to LOSS; 3 EVEN to the runs disagree |
| `results/live/V7_CITYLEARN.md` | 22 GAIN to EVEN; 10 power given to EVEN; 6 LOSS to EVEN |
| `results/live/V7_CRUISEKUBE.md` | 4 EVEN to the runs disagree; 4 EVEN to power given; 2 EVEN to LOSS; 1 EVEN to EVEN |
| `results/live/V7_FAIRNESS.md` | 8 EVEN to the runs disagree; 3 EVEN to EVEN; 3 EVEN to GAIN; 3 EVEN to LOSS |
| `results/live/V7_FAULTS.md` | 5 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to the runs disagree |
| `results/live/V7_GOLDILOCKS.md` | 3 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to the runs disagree |
| `results/live/V7_KAFKA.md` | 23 EVEN to the runs disagree; 10 EVEN to EVEN; 9 EVEN to GAIN; 2 GAIN to EVEN; 2 EVEN to LOSS; 2 EVEN to power given |
| `results/live/V7_KAFKA_SERVICE.md` | 19 EVEN to the runs disagree; 17 EVEN to GAIN; 8 EVEN to EVEN; 6 EVEN to power given |
| `results/live/V7_KEDA_CPU_REQUESTS.md` | 3 EVEN to the runs disagree; 2 EVEN to GAIN; 1 EVEN to EVEN; 1 EVEN to power given |
| `results/live/V7_KEDA_REQUESTS.md` | 1 EVEN to EVEN; 1 EVEN to GAIN; 1 EVEN to LOSS |
| `results/live/V7_PANDAPOWER.md` | 10 GAIN to EVEN; 4 power given to EVEN |
| `results/live/V7_PGBENCH.md` | 13 EVEN to the runs disagree; 8 EVEN to power given; 6 EVEN to GAIN; 4 EVEN to EVEN; 1 EVEN to LOSS |
| `results/live/V7_REDIS.md` | 14 EVEN to EVEN; 7 EVEN to the runs disagree; 7 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V7_REDIS_SERVICE.md` | 12 EVEN to EVEN; 7 EVEN to GAIN; 7 EVEN to the runs disagree; 3 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V7_ROBUST_LONG.md` | 7 EVEN to GAIN; 3 EVEN to EVEN; 2 EVEN to power given; 1 EVEN to LOSS |
| `results/live/V7_SYSBENCH.md` | 24 EVEN to the runs disagree; 13 EVEN to EVEN; 12 EVEN to GAIN; 3 EVEN to power given; 2 EVEN to LOSS |
| `results/live/V7_TRACE_GOOGLE2011.md` | 3 EVEN to EVEN; 1 EVEN to power given; 1 EVEN to LOSS; 1 EVEN to GAIN |
| `results/live/V7_YCSB.md` | 16 EVEN to the runs disagree; 15 EVEN to GAIN; 10 EVEN to LOSS; 9 EVEN to EVEN |
| `results/toy_gate/HEARTBEAT_SWEEP.md` | 216 EVEN to EVEN; 67 EVEN to LOSS; 57 EVEN to GAIN; 30 EVEN to power given; 20 GAIN to EVEN; 2 power given to EVEN |
| `results/toy_gate/SOLO_V18.md` | 3 EVEN to EVEN; 1 EVEN to LOSS |
| `results/toy_gate/TOY_GATE.md` | 8 EVEN to EVEN; 7 EVEN to LOSS; 4 EVEN to GAIN; 1 LOSS to EVEN |
| `results/toy_gate/V10_VS_V9.md` | 8 EVEN to LOSS; 6 EVEN to EVEN; 2 EVEN to GAIN; 2 LOSS to EVEN |
| `results/toy_gate/V11_VS_V10.md` | 12 EVEN to LOSS; 8 EVEN to EVEN; 2 EVEN to GAIN; 2 LOSS to EVEN |
| `results/toy_gate/V12_VS_V11.md` | 18 EVEN to LOSS; 16 EVEN to EVEN; 9 EVEN to GAIN; 3 LOSS to EVEN; 1 EVEN to power given; 1 GAIN to EVEN |
| `results/toy_gate/V13_VS_V12.md` | 12 EVEN to LOSS; 9 EVEN to EVEN; 3 EVEN to GAIN; 3 LOSS to EVEN; 1 GAIN to EVEN |
| `results/toy_gate/V14_VS_V13.md` | 12 EVEN to LOSS; 10 EVEN to EVEN; 4 EVEN to GAIN; 4 LOSS to EVEN |
| `results/toy_gate/V15_VS_V14.md` | 16 EVEN to LOSS; 14 EVEN to EVEN; 7 EVEN to GAIN; 6 EVEN to power given; 4 LOSS to EVEN |
| `results/toy_gate/V16_PACE.md` | 26 EVEN to EVEN; 22 EVEN to GAIN; 11 EVEN to power given; 5 EVEN to LOSS; 1 LOSS to EVEN |
| `results/toy_gate/V16_VS_V15.md` | 21 EVEN to LOSS; 21 EVEN to EVEN; 10 EVEN to power given; 7 EVEN to GAIN; 5 LOSS to EVEN |
| `results/toy_gate/V17_LADDER.md` | 106 EVEN to GAIN; 100 EVEN to EVEN; 36 EVEN to LOSS; 29 EVEN to power given; 2 LOSS to EVEN |
| `results/toy_gate/V17_VS_V16.md` | 22 EVEN to LOSS; 17 EVEN to EVEN; 9 EVEN to GAIN; 5 LOSS to EVEN; 3 EVEN to power given |
| `results/toy_gate/V18_VS_V17.md` | 22 EVEN to LOSS; 14 EVEN to EVEN; 6 EVEN to GAIN; 4 LOSS to EVEN; 2 EVEN to power given |
| `results/toy_gate/V8_VS_V7.md` | 8 EVEN to LOSS; 6 EVEN to EVEN; 2 EVEN to GAIN; 2 LOSS to EVEN |
| `results/toy_gate/V9_VS_V8.md` | 8 EVEN to LOSS; 6 EVEN to EVEN; 2 EVEN to GAIN; 2 LOSS to EVEN |

The organism reports' lines (the count of words under each organism) were written again too: 45 lines.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
