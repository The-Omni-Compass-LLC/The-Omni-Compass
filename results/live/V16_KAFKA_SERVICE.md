# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39823828673 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39844651167 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39864227589 | `681ff70efadd` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 972, 975 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.1 | 365.4 | +0.1% (-0.3 to +0.4) | -0.3% (-0.8 to +0.3) | -0.2% (-0.3 to -0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.30%) |
| throughput (messages a second consumed) | 427.9 | 427.9 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,357 | 2,237 | -5.1% (-9.4 to -0.8) | +1.5% (+0.9 to +2.1) | +1.2% (-0.6 to +3.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,506 | 3,594 | +2.5% (-5.5 to +10.6) | +2.9% (+0.7 to +5.0) | +1.4% (-1.4 to +4.1) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| end-to-end latency, median (ms) | 8.56 | 8.51 | -0.6% (-1.9 to +0.7) | -0.3% (-1.1 to +0.5) | +0.3% (-1.5 to +2.1) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 308.5 | 301.2 | -2.4% (-7.3 to +2.6) | +2.1% (-2.8 to +7.1) | +1.5% (-0.5 to +3.4) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,637 | 1,615 | -1.3% (-6.3 to +3.7) | +0.4% (-2.8 to +3.5) | +1.3% (-2.1 to +4.6) | **the runs disagree** |
| consumer lag, mean messages waiting | 136.8 | 132.7 | -3.0% (-7.1 to +1.1) | +1.8% (-3.0 to +6.6) | +1.6% (-1.8 to +4.9) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% (-14.8 to +39.3) | +6.0% (-21.2 to +33.1) | -0.3% (-0.3 to -0.3) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.305 | 0.305 | -0.0% (-3.9 to +3.8) | +2.0% (+0.2 to +3.7) | +0.6% (-1.0 to +2.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds | 529.6 | 530.3 | +0.1% (-4.2 to +4.4) | +2.4% (+0.4 to +4.4) | +0.6% (-1.3 to +2.4) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.22 | +0.0% (-4.4 to +4.5) | +2.7% (+0.2 to +5.1) | +0.8% (-1.1 to +2.7) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 977, 974 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.7 | 340.1 | -0.2% (-0.8 to +0.5) | -0.2% (-0.5 to +0.1) | -0.1% (-0.7 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.20%) |
| throughput (messages a second consumed) | 418.4 | 418.4 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,502 | -2.5% (-13.4 to +8.4) | -4.2% (-12.3 to +3.8) | +3.0% (-9.2 to +15.3) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,763 | 3,696 | -1.8% (-7.7 to +4.1) | +8.7% (+2.6 to +14.8) | -2.9% (-20.0 to +14.2) | **the runs disagree** |
| end-to-end latency, median (ms) | 9.05 | 8.88 | -2.0% (-9.3 to +5.4) | +0.3% (-3.1 to +3.7) | +1.4% (-2.3 to +5.1) | **the runs disagree** |
| end-to-end latency, mean (ms) | 376.4 | 380.1 | +1.0% (-1.9 to +3.8) | +0.6% (-0.9 to +2.1) | +0.8% (-0.1 to +1.7) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| consumer lag, most messages waiting at once | 1,658 | 1,639 | -1.1% (-4.6 to +2.4) | +1.1% (-1.7 to +4.0) | -0.8% (-3.5 to +1.9) | **the runs disagree** |
| consumer lag, mean messages waiting | 162.7 | 162.7 | -0.0% (-2.9 to +2.9) | +0.4% (-1.3 to +2.2) | +0.2% (-0.6 to +1.0) | EVEN, under the floor (every run under 0.5%; the largest 0.42%) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | +0.1% (-7.3 to +7.4) | -1.2% (-5.9 to +3.4) | -0.7% (-4.7 to +3.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 221.1 | 221.3 | +0.1% (-7.2 to +7.3) | -1.2% (-5.7 to +3.3) | -0.7% (-4.7 to +3.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.6 | +0.2% (-7.0 to +7.4) | -1.0% (-5.2 to +3.3) | -0.6% (-4.9 to +3.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 393, 391 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 144.6 | -1.9% (-4.9 to +1.1) | +5.7% (-18.9 to +30.3) | -0.2% (-0.6 to +0.2) | **the runs disagree** |
| throughput (messages a second consumed) | 171.8 | 171.8 | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,232 | +6.6% (+1.2 to +11.9) | -35.0% (-169.3 to +99.3) | +2.3% (-5.0 to +9.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,445 | 3,633 | +5.5% (-11.9 to +22.8) | -31.3% (-173.9 to +111.2) | +0.4% (-5.1 to +6.0) | **the runs disagree** |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% (-0.9 to +0.4) | -0.5% (-4.4 to +3.4) | +0.2% (-1.1 to +1.5) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 280.1 | 313.8 | +12.0% (-1.2 to +25.3) | -32.3% (-166.1 to +101.5) | +3.1% (-5.1 to +11.2) | **the runs disagree** |
| consumer lag, most messages waiting at once | 653.0 | 642.7 | -1.6% (-10.7 to +7.5) | -31.0% (-158.1 to +96.1) | +1.0% (-9.6 to +11.7) | **the runs disagree** |
| consumer lag, mean messages waiting | 51.2 | 57.6 | +12.7% (-3.5 to +28.8) | -32.2% (-167.0 to +102.6) | +3.2% (-4.7 to +11.2) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | -0.1% (-0.6 to +0.5) | +9.3% (-32.2 to +50.9) | -0.3% (-0.3 to -0.3) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.253 | 0.252 | -0.6% (-3.0 to +1.7) | +0.2% (-2.5 to +3.0) | -0.2% (-3.6 to +3.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 454.2 | 451.3 | -0.6% (-3.0 to +1.7) | +0.3% (-2.4 to +2.9) | -0.2% (-3.6 to +3.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 messages inside the line | 6.85 | 6.94 | +1.3% (-1.7 to +4.2) | -4.7% (-27.3 to +18.0) | +0.0% (-3.7 to +3.8) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,932, 1,949, 1,931 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.4 | 725.2 | -0.2% (-0.4 to +0.1) | +5.9% (-19.1 to +31.0) | -0.0% (-0.5 to +0.5) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (messages a second consumed) | 849.8 | 849.8 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,298 | 2,297 | -0.0% (-10.2 to +10.2) | -35.6% (-167.0 to +95.9) | -2.2% (-10.7 to +6.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, 99th percentile (ms) | 3,658 | 3,775 | +3.2% (-7.8 to +14.1) | -39.2% (-156.9 to +78.4) | -0.2% (-10.0 to +9.7) | **the runs disagree** |
| end-to-end latency, median (ms) | 7.86 | 7.78 | -1.1% (-4.2 to +2.1) | -5.8% (-23.6 to +12.1) | -0.1% (-2.9 to +2.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| end-to-end latency, mean (ms) | 305.7 | 310.3 | +1.5% (-2.6 to +5.6) | -35.5% (-161.4 to +90.5) | -1.0% (-8.6 to +6.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,222 | 3,287 | +2.0% (-0.4 to +4.5) | -33.1% (-145.1 to +78.9) | -1.1% (-5.4 to +3.1) | **the runs disagree** |
| consumer lag, mean messages waiting | 264.4 | 268.5 | +1.5% (-2.2 to +5.3) | -35.2% (-160.4 to +89.9) | -1.0% (-8.4 to +6.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +9.8% (-33.7 to +53.2) | +6.0% (-21.3 to +33.3) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.346 | 0.342 | -1.2% (-3.4 to +0.9) | +0.8% (-3.7 to +5.3) | +0.6% (-6.0 to +7.2) | **the runs disagree** |
| host CPU-seconds | 601.2 | 595.4 | -1.0% (-3.3 to +1.3) | +0.7% (-3.3 to +4.7) | +0.6% (-6.2 to +7.5) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.82 | -0.8% (-3.2 to +1.6) | -4.4% (-24.0 to +15.1) | +0.7% (-6.6 to +7.9) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +133.3% (-10.1 to +276.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 10 gauge-rows GAIN (1 in all three of our runs), 1 LOSS (0 in all three of our runs), 4 power given (0 in all three of our runs), 9 EVEN, 18 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
