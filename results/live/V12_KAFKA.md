# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39379918375 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39410587818 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39459233023 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 979, 974 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.3 | 366.1 | -0.1% (-0.2 to +0.1) | +5.8% (-18.8 to +30.3) | -0.0% (-0.4 to +0.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (messages a second consumed) | 429.7 | 429.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,431 | -1.2% (-5.2 to +2.8) | -33.9% (-170.4 to +102.6) | -1.8% (-3.0 to -0.6) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,781 | +0.4% (-8.3 to +9.0) | -33.6% (-160.8 to +93.5) | +1.6% (-14.4 to +17.5) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.49 | 8.48 | -0.1% (-1.3 to +1.2) | -1.7% (-7.7 to +4.3) | -0.3% (-0.7 to +0.1) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 322.9 | 322.2 | -0.2% (-2.2 to +1.7) | -33.4% (-161.5 to +94.7) | -1.6% (-6.5 to +3.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 1,707 | 1,706 | -0.0% (-1.5 to +1.5) | -31.3% (-160.7 to +98.0) | +0.9% (-4.8 to +6.6) | **the runs disagree** |
| consumer lag, mean messages waiting | 142.7 | 142.4 | -0.2% (-1.8 to +1.4) | -33.5% (-161.9 to +95.0) | -1.7% (-5.7 to +2.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +9.2% (-31.9 to +50.3) | -0.3% (-0.3 to -0.3) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.319 | 0.318 | -0.4% (-2.3 to +1.5) | +0.9% (-1.2 to +3.1) | -0.6% (-3.5 to +2.2) | **the runs disagree** |
| host CPU-seconds | 558.6 | 556.9 | -0.3% (-2.2 to +1.6) | +0.8% (-1.5 to +3.2) | -0.6% (-3.5 to +2.2) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.38 | -0.3% (-2.1 to +1.6) | -4.1% (-24.7 to +16.5) | -0.6% (-3.7 to +2.5) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 981, 973, 976 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.6 | 341.6 | -0.3% (-2.2 to +1.6) | -0.4% (-1.5 to +0.6) | -0.1% (-0.3 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.41%) |
| throughput (messages a second consumed) | 421.4 | 421.4 | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.1% (-0.3 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| end-to-end latency, 95th percentile (ms) | 2,564 | 2,603 | +1.5% (-13.1 to +16.1) | +0.3% (-7.8 to +8.4) | -2.2% (-9.5 to +5.1) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,717 | 3,762 | +1.2% (-19.0 to +21.5) | +1.3% (-4.2 to +6.8) | +1.5% (-10.7 to +13.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| end-to-end latency, median (ms) | 10.3 | 12.0 | +17.0% (-38.9 to +72.9) | -0.5% (-5.2 to +4.1) | +0.8% (-5.5 to +7.0) | **the runs disagree** |
| end-to-end latency, mean (ms) | 394.0 | 403.9 | +2.5% (-14.7 to +19.7) | +2.3% (-4.8 to +9.5) | +0.5% (-1.4 to +2.4) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 1,688 | 1,741 | +3.1% (-11.5 to +17.7) | -0.5% (-5.6 to +4.7) | +0.8% (-2.5 to +4.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer lag, mean messages waiting | 173.0 | 176.6 | +2.1% (-12.6 to +16.7) | +0.9% (-4.3 to +6.1) | -0.3% (-3.2 to +2.5) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.267 | 0.264 | -1.0% (-9.5 to +7.4) | +0.1% (-4.7 to +4.9) | -0.8% (-2.5 to +0.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 191.9 | 189.9 | -1.0% (-9.4 to +7.4) | +0.0% (-4.7 to +4.8) | -0.8% (-2.2 to +0.5) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 3.1 | 3.08 | -0.7% (-7.8 to +6.3) | +0.5% (-4.7 to +5.6) | -0.6% (-2.5 to +1.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 392, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.9 | -0.1% (-0.7 to +0.5) | -0.0% (-0.4 to +0.3) | -0.1% (-0.2 to -0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| throughput (messages a second consumed) | 173.2 | 173.2 | -0.0% (-0.0 to -0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,519 | 2,528 | +0.3% (-9.3 to +9.9) | -0.4% (-2.7 to +1.9) | +0.9% (-4.4 to +6.2) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,918 | -0.8% (-10.3 to +8.8) | -0.7% (-13.4 to +11.9) | +0.5% (-8.9 to +9.9) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.7 | 11.8 | +0.4% (-0.9 to +1.7) | -0.1% (-0.7 to +0.4) | -0.1% (-0.5 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.40%) |
| end-to-end latency, mean (ms) | 342.2 | 345.6 | +1.0% (-7.9 to +9.8) | -0.2% (-3.3 to +3.0) | +0.7% (-1.5 to +2.9) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 719.7 | 731.7 | +1.7% (-3.7 to +7.0) | -2.4% (-9.6 to +4.7) | -1.7% (-3.2 to -0.2) | **the runs disagree** |
| consumer lag, mean messages waiting | 62.8 | 63.5 | +1.1% (-8.9 to +11.0) | -1.4% (-4.9 to +2.1) | +0.1% (-2.3 to +2.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.292 | +0.7% (-3.3 to +4.7) | -1.0% (-2.8 to +0.8) | -0.4% (-2.6 to +1.7) | **the runs disagree** |
| host CPU-seconds | 510.3 | 514.2 | +0.8% (-3.1 to +4.6) | -1.0% (-2.9 to +0.9) | -0.4% (-2.6 to +1.7) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 7.7 | 7.77 | +0.9% (-2.9 to +4.7) | -1.0% (-3.1 to +1.2) | -0.3% (-2.5 to +1.9) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,941, 1,932, 1,935 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728.0 | 725.4 | -0.4% (-0.9 to +0.1) | -0.8% (-3.0 to +1.4) | -0.1% (-0.2 to +0.1) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (messages a second consumed) | 853.5 | 853.5 | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| end-to-end latency, 95th percentile (ms) | 2,364 | 2,451 | +3.7% (+2.4 to +5.0) | +31.4% (-104.1 to +166.8) | -1.1% (-4.9 to +2.8) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,749 | 3,797 | +1.3% (-0.1 to +2.7) | +23.4% (-67.8 to +114.5) | -0.8% (-6.6 to +5.0) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.29 | 8.09 | -2.5% (-15.6 to +10.6) | +0.0% (-3.4 to +3.5) | +0.1% (-1.9 to +2.1) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 322.8 | 335.4 | +3.9% (+0.9 to +6.9) | +28.8% (-94.0 to +151.7) | -0.7% (-2.0 to +0.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,374 | 3,389 | +0.4% (-3.4 to +4.3) | +20.0% (-63.6 to +103.6) | -0.7% (-1.3 to -0.1) | **the runs disagree** |
| consumer lag, mean messages waiting | 283.0 | 292.7 | +3.4% (+0.3 to +6.6) | +28.5% (-91.9 to +148.8) | -0.7% (-2.1 to +0.6) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +0.8% (-3.8 to +5.3) | -0.3% (-0.3 to -0.3) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.32 | 0.32 | -0.0% (-2.4 to +2.4) | -1.3% (-4.1 to +1.6) | +1.3% (-1.6 to +4.2) | **the runs disagree** |
| host CPU-seconds | 548.4 | 549.1 | +0.1% (-2.7 to +3.0) | -1.1% (-3.9 to +1.6) | +1.4% (-1.4 to +4.2) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.67 | 1.68 | +0.5% (-1.9 to +2.9) | -0.4% (-3.3 to +2.6) | +1.4% (-1.2 to +4.1) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +166.7% (+23.2 to +310.1) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 5 gauge-rows GAIN (1 in all three of our runs), 7 LOSS (0 in all three of our runs), 3 power given (0 in all three of our runs), 12 EVEN, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
