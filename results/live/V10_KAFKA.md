# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108188053 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116273889 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39123591485 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 970, 982 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.7 | 364.8 | -0.2% (-0.6 to +0.1) | -0.2% (-0.8 to +0.5) | -0.2% (-0.8 to +0.4) | EVEN, under the floor (the three runs' mean 0.21%) |
| throughput (messages a second consumed) | 428.5 | 428.5 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,387 | +1.7% (-2.5 to +6.0) | +1.0% (-1.2 to +3.3) | +1.4% (-6.3 to +9.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,617 | 3,610 | -0.2% (-6.2 to +5.8) | +0.6% (-13.1 to +14.4) | +1.0% (-12.6 to +14.5) | EVEN, under the floor (the three runs' mean 0.47%) |
| end-to-end latency, median (ms) | 8.56 | 8.5 | -0.6% (-2.2 to +0.9) | -0.1% (-0.5 to +0.3) | +0.2% (-1.4 to +1.9) | EVEN, under the floor (the three runs' mean 0.19%) |
| end-to-end latency, mean (ms) | 313.2 | 316.8 | +1.2% (-3.7 to +6.0) | +1.6% (-8.8 to +11.9) | +1.5% (-9.7 to +12.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,668 | 1,670 | +0.1% (-3.6 to +3.9) | +0.6% (-2.1 to +3.3) | +0.6% (-4.0 to +5.2) | EVEN, under the floor (the three runs' mean 0.46%) |
| consumer lag, mean messages waiting | 139.0 | 140.4 | +1.0% (-3.2 to +5.2) | +1.3% (-9.1 to +11.6) | +1.2% (-10.2 to +12.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.306 | -0.4% (-3.1 to +2.2) | -0.6% (-4.6 to +3.3) | -0.6% (-2.6 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 532.1 | 531.7 | -0.1% (-3.1 to +2.9) | -0.4% (-5.0 to +4.2) | -0.6% (-2.9 to +1.7) | EVEN, under the floor (the three runs' mean 0.36%) |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | +0.2% (-2.5 to +2.8) | -0.2% (-4.2 to +3.8) | -0.4% (-2.4 to +1.5) | EVEN, under the floor (the three runs' mean 0.16%) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 975, 965 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.0 | 339.3 | -0.5% (-0.9 to -0.1) | +0.0% (-0.6 to +0.7) | -0.3% (-0.5 to -0.0) | EVEN, under the floor (the three runs' mean 0.25%) |
| throughput (messages a second consumed) | 418.7 | 418.7 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,517 | 2,555 | +1.5% (-4.9 to +8.0) | -5.4% (-6.7 to -4.2) | -0.4% (-12.4 to +11.5) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,785 | +1.0% (-14.2 to +16.2) | +2.9% (-10.0 to +15.7) | +0.5% (-12.6 to +13.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.45 | 9.57 | +1.2% (-3.3 to +5.8) | +0.7% (-9.4 to +10.8) | -1.8% (-7.2 to +3.5) | **the runs disagree** |
| end-to-end latency, mean (ms) | 382.3 | 392.0 | +2.5% (-5.4 to +10.5) | -0.7% (-8.7 to +7.3) | +0.5% (-0.7 to +1.6) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,659 | 1,670 | +0.6% (-2.6 to +3.8) | -0.7% (-5.3 to +3.8) | +0.3% (-1.4 to +2.0) | **the runs disagree** |
| consumer lag, mean messages waiting | 166.3 | 168.8 | +1.5% (-7.2 to +10.3) | -0.7% (-7.9 to +6.5) | +0.1% (-2.1 to +2.3) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.294 | -1.1% (-8.1 to +5.9) | -1.3% (-7.1 to +4.6) | -1.2% (-6.3 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 207.9 | 205.7 | -1.1% (-8.2 to +6.1) | -1.3% (-7.0 to +4.5) | -1.1% (-6.3 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.36 | -0.6% (-7.3 to +6.2) | -1.3% (-6.7 to +4.2) | -0.8% (-5.9 to +4.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 146.9 | -0.3% (-0.9 to +0.4) | -0.1% (-0.4 to +0.2) | -0.1% (-0.6 to +0.4) | EVEN, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 172.6 | 172.6 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,354 | 2,348 | -0.3% (-5.3 to +4.8) | +0.5% (-4.3 to +5.3) | +2.5% (-0.4 to +5.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,647 | +0.2% (-2.2 to +2.6) | +0.5% (-6.8 to +7.8) | -2.1% (-7.6 to +3.4) | EVEN, under the floor (the three runs' mean 0.47%) |
| end-to-end latency, median (ms) | 11.3 | 11.2 | -0.3% (-0.9 to +0.2) | -0.0% (-0.7 to +0.6) | -1.3% (-5.7 to +3.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 314.4 | 316.7 | +0.7% (-2.2 to +3.6) | +0.9% (-2.0 to +3.8) | +0.7% (-2.8 to +4.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 687.7 | 680.0 | -1.1% (-4.6 to +2.4) | -1.1% (-8.1 to +5.9) | -0.3% (-11.6 to +11.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 57.0 | 58.1 | +2.0% (-3.9 to +7.9) | +1.5% (+0.8 to +2.2) | -0.0% (-3.7 to +3.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.6% (-1.4 to +2.5) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (the three runs' mean 0.04%) |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.275 | 0.272 | -0.9% (-3.8 to +2.1) | -0.7% (-3.8 to +2.3) | -1.8% (-6.9 to +3.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 491.8 | 487.6 | -0.9% (-3.7 to +2.0) | -0.7% (-3.9 to +2.6) | -1.8% (-6.9 to +3.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.38 | -0.6% (-2.8 to +1.6) | -0.6% (-4.0 to +2.9) | -1.6% (-6.9 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,951, 1,934, 1,921 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732.2 | 731.3 | -0.1% (-0.2 to -0.1) | +5.4% (-18.1 to +28.8) | -0.9% (-2.4 to +0.6) | **the runs disagree** |
| throughput (messages a second consumed) | 858.2 | 858.2 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,431 | 2,418 | -0.5% (-5.6 to +4.5) | -33.4% (-163.0 to +96.2) | +4.4% (+0.9 to +8.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,680 | -1.1% (-1.9 to -0.3) | -30.6% (-163.2 to +101.9) | +4.8% (-4.2 to +13.7) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.15 | 8.56 | +5.1% (-13.1 to +23.2) | -5.7% (-20.2 to +8.9) | -3.2% (-14.7 to +8.3) | **the runs disagree** |
| end-to-end latency, mean (ms) | 324.9 | 329.0 | +1.2% (-2.9 to +5.3) | -31.5% (-160.2 to +97.1) | +6.2% (-2.4 to +14.8) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,348 | 3,342 | -0.2% (-1.2 to +0.9) | -29.9% (-142.6 to +82.8) | +3.4% (-2.6 to +9.4) | **the runs disagree** |
| consumer lag, mean messages waiting | 286.3 | 288.8 | +0.9% (-3.1 to +4.9) | -31.4% (-159.4 to +96.5) | +5.9% (-3.5 to +15.3) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +16.2% (-22.1 to +54.5) | +6.2% (-21.3 to +33.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +50.0% (-74.2 to +174.2) | +33.3% (-38.4 to +105.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.316 | 0.306 | -3.2% (-12.9 to +6.5) | +0.9% (+0.1 to +1.8) | +0.1% (-3.7 to +3.9) | **the runs disagree** |
| host CPU-seconds | 563.1 | 545.8 | -3.1% (-12.5 to +6.4) | +1.2% (+0.2 to +2.1) | +0.3% (-3.4 to +3.9) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.66 | -3.0% (-12.4 to +6.4) | -3.6% (-25.1 to +18.0) | +1.2% (-2.9 to +5.3) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +200.0% (-48.4 to +448.4) | +166.7% (+23.2 to +310.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 9 gauge-rows GAIN, 4 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 EVEN, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
