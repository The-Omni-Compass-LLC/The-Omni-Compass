# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39821402572 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39840024618 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39860244280 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 954, 984 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.2 | 365.5 | -0.2% (-0.7 to +0.3) | +0.5% (-0.8 to +1.7) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.47%) |
| throughput (messages a second consumed) | 429.4 | 429.4 | +0.0% (-0.3 to +0.3) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,453 | +1.5% (-2.3 to +5.2) | -1.7% (-9.4 to +5.9) | -1.2% (-6.4 to +4.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,844 | +2.1% (-6.0 to +10.3) | -5.9% (-16.8 to +4.9) | -1.5% (-5.7 to +2.7) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.49 | 8.53 | +0.4% (-1.5 to +2.4) | -1.8% (-4.3 to +0.8) | -0.5% (-2.0 to +0.9) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 320.1 | 325.5 | +1.7% (-2.0 to +5.4) | -5.2% (-19.0 to +8.6) | -1.1% (-4.4 to +2.1) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,698 | 1,710 | +0.7% (-4.6 to +6.0) | -3.0% (-16.0 to +10.1) | -0.9% (-4.9 to +3.2) | **the runs disagree** |
| consumer lag, mean messages waiting | 141.3 | 143.4 | +1.5% (-1.3 to +4.3) | -5.8% (-17.5 to +6.0) | -1.4% (-3.7 to +1.0) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +20.8% (+18.8 to +22.8) | -0.3% (-0.3 to -0.3) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +50.0% (+50.0 to +50.0) | +0.0% (+0.0 to +0.0) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.326 | 0.331 | +1.4% (-3.3 to +6.1) | -1.1% (-5.8 to +3.6) | -0.5% (-4.8 to +3.8) | **the runs disagree** |
| host CPU-seconds | 581.9 | 590.4 | +1.5% (-3.3 to +6.2) | -1.0% (-5.6 to +3.7) | -0.4% (-4.4 to +3.6) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.53 | 3.59 | +1.7% (-3.4 to +6.7) | -1.4% (-4.8 to +1.9) | -0.3% (-4.5 to +3.8) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +300.0% (+300.0 to +300.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (4 trials, 1 allowed, 1 refused); acting: 2 to 3 (4 trials, 1 allowed, 1 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 979, 974, 983 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.0 | 341.9 | -0.0% (-2.1 to +2.1) | -0.2% (-0.4 to -0.1) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.25%) |
| throughput (messages a second consumed) | 420.9 | 420.9 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,484 | 2,506 | +0.9% (-13.8 to +15.5) | +0.7% (-8.8 to +10.2) | -4.8% (-17.7 to +8.1) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,838 | 3,843 | +0.1% (-1.4 to +1.7) | -0.1% (-11.7 to +11.4) | +1.9% (-9.1 to +13.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, median (ms) | 9.16 | 9.18 | +0.2% (-21.7 to +22.0) | -1.5% (-6.1 to +3.1) | -40.6% (-111.5 to +30.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 385.0 | 387.6 | +0.7% (-14.2 to +15.5) | +0.9% (+0.4 to +1.4) | -0.3% (-2.1 to +1.5) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 1,644 | 1,681 | +2.2% (-6.7 to +11.1) | +1.2% (-3.2 to +5.6) | +0.5% (-6.5 to +7.5) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| consumer lag, mean messages waiting | 167.8 | 168.9 | +0.7% (-12.6 to +14.0) | +1.2% (-0.7 to +3.2) | -0.8% (-2.8 to +1.2) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | -0.6% (-6.9 to +5.8) | -1.3% (-7.2 to +4.7) | -0.5% (-2.7 to +1.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 189.9 | 189.0 | -0.5% (-6.8 to +5.9) | -1.2% (-7.3 to +4.9) | -0.5% (-2.6 to +1.7) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 3.06 | -0.5% (-8.9 to +7.9) | -1.0% (-7.1 to +5.1) | -0.4% (-2.8 to +2.0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 392, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 146.8 | -0.3% (-0.5 to -0.1) | -0.0% (-0.8 to +0.8) | -0.3% (-0.8 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.30%) |
| throughput (messages a second consumed) | 172.9 | 172.9 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,470 | +3.2% (-2.5 to +8.9) | -0.6% (-14.8 to +13.5) | +1.4% (-10.9 to +13.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,784 | 3,821 | +1.0% (-1.3 to +3.2) | -1.2% (-14.6 to +12.2) | +1.4% (-3.8 to +6.6) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.2% (-0.4 to -0.1) | -0.5% (-2.6 to +1.6) | +0.2% (-1.2 to +1.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 325.0 | 334.4 | +2.9% (-3.1 to +8.9) | +0.3% (-12.1 to +12.8) | +3.0% (-6.2 to +12.1) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 693.3 | 709.3 | +2.3% (-13.1 to +17.8) | +1.2% (-5.4 to +7.7) | +2.3% (-2.0 to +6.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| consumer lag, mean messages waiting | 59.8 | 61.3 | +2.6% (-6.5 to +11.6) | +1.3% (-8.9 to +11.5) | +3.6% (-2.1 to +9.3) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.288 | 0.287 | -0.5% (-2.8 to +1.8) | -1.7% (-8.0 to +4.6) | +0.2% (-6.3 to +6.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 508.8 | 506.3 | -0.5% (-2.8 to +1.8) | -1.7% (-8.1 to +4.7) | +0.4% (-6.2 to +6.9) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 7.68 | 7.66 | -0.2% (-2.3 to +1.9) | -1.7% (-8.8 to +5.5) | +0.6% (-6.4 to +7.7) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,938, 1,966, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727.3 | 725.3 | -0.3% (-0.8 to +0.3) | +0.0% (-0.5 to +0.5) | -0.0% (-0.5 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.27%) |
| throughput (messages a second consumed) | 852.2 | 852.2 | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,399 | +1.0% (+0.4 to +1.6) | -1.8% (-8.0 to +4.5) | +1.7% (-5.1 to +8.4) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,749 | +2.7% (-4.3 to +9.7) | +0.4% (-2.7 to +3.5) | -6.2% (-16.8 to +4.4) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.37 | 8.23 | -1.7% (-11.7 to +8.3) | -2.4% (-3.0 to -1.7) | -1.2% (-6.6 to +4.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 320.2 | 326.2 | +1.9% (-5.6 to +9.3) | -1.3% (-5.7 to +3.0) | -1.1% (-5.8 to +3.6) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,288 | 3,353 | +2.0% (-0.2 to +4.2) | -1.2% (-2.5 to +0.0) | -1.2% (-4.3 to +1.9) | **the runs disagree** |
| consumer lag, mean messages waiting | 279.0 | 285.0 | +2.1% (-5.1 to +9.4) | -1.7% (-5.1 to +1.6) | -1.1% (-5.0 to +2.8) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% (-21.3 to +33.3) | -0.3% (-0.3 to -0.3) | +5.9% (-21.0 to +32.9) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.324 | 0.322 | -0.5% (-2.6 to +1.6) | -1.1% (-2.9 to +0.6) | +0.3% (-1.1 to +1.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 555.9 | 552.9 | -0.5% (-2.8 to +1.7) | -1.0% (-2.4 to +0.5) | +0.3% (-1.4 to +2.0) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.69 | -0.3% (-2.0 to +1.4) | -1.0% (-2.6 to +0.7) | +0.3% (-0.9 to +1.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 12 gauge-rows GAIN (1 in all three of our runs), 6 LOSS (0 in all three of our runs), 2 power given (0 in all three of our runs), 12 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
