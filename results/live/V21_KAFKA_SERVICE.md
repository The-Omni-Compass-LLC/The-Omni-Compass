# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40236926576 | `23c7e8eb27be` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40259312876 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40283010023 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 969, 970, 970 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.8 | 363.1 | -0.7% (-2.8 to +1.3) | +0.1% (-0.3 to +0.4) | +0.1% (-0.4 to +0.6) | EVEN, under the floor (the three runs' mean 0.19%) |
| throughput (messages a second consumed) | 426.1 | 426.1 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,092 | 2,185 | +4.4% (-6.4 to +15.2) | -0.7% (-1.8 to +0.4) | -3.9% (-8.7 to +0.9) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,428 | 3,392 | -1.1% (-5.2 to +3.1) | -2.1% (-5.5 to +1.3) | +0.3% (-17.3 to +18.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.58 | 8.55 | -0.4% (-0.9 to +0.2) | -0.1% (-1.3 to +1.1) | -0.0% (-2.0 to +2.0) | EVEN, under the floor (the three runs' mean 0.16%) |
| end-to-end latency, mean (ms) | 281.1 | 292.6 | +4.1% (-8.8 to +17.0) | -0.7% (-3.2 to +1.7) | -1.8% (-10.1 to +6.5) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,568 | 1,564 | -0.3% (-6.9 to +6.3) | -1.4% (-4.4 to +1.5) | -1.1% (-3.8 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 124.3 | 129.3 | +4.0% (-8.7 to +16.8) | -0.5% (-3.0 to +2.0) | -2.0% (-10.6 to +6.6) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.07 | +3.4% (-4.5 to +11.2) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 3 | +50.0% (+50.0 to +50.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.305 | 0.303 | -0.5% (-4.5 to +3.6) | -0.5% (-4.4 to +3.3) | -0.1% (-3.2 to +3.0) | EVEN, under the floor (the three runs' mean 0.36%) |
| host CPU-seconds | 529.5 | 527.5 | -0.4% (-5.0 to +4.2) | -0.4% (-4.4 to +3.5) | -0.1% (-3.3 to +3.1) | EVEN, under the floor (the three runs' mean 0.32%) |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.23 | +0.4% (-4.6 to +5.4) | -0.5% (-4.8 to +3.7) | -0.2% (-3.9 to +3.5) | EVEN, under the floor (the three runs' mean 0.12%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 974, 985 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.4 | 341.2 | -0.4% (-1.4 to +0.7) | +0.1% (-0.1 to +0.3) | -0.5% (-1.6 to +0.6) | EVEN, under the floor (the three runs' mean 0.25%) |
| throughput (messages a second consumed) | 418.5 | 418.5 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | -0.7% (-6.3 to +4.8) | +2.2% (-7.4 to +11.9) | +5.4% (-2.3 to +13.1) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,432 | 3,678 | +7.1% (-1.5 to +15.8) | -4.9% (-12.7 to +3.0) | -1.8% (-8.5 to +4.9) | **the runs disagree** |
| end-to-end latency, median (ms) | 9.86 | 12.0 | +21.5% (-30.5 to +73.5) | -2.5% (-14.8 to +9.8) | -38.4% (-165.4 to +88.5) | **the runs disagree** |
| end-to-end latency, mean (ms) | 362.2 | 371.4 | +2.5% (-4.5 to +9.6) | -0.3% (-3.4 to +2.8) | +3.3% (-3.3 to +9.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,565 | 1,574 | +0.5% (-6.5 to +7.5) | +1.3% (-4.8 to +7.4) | +2.9% (+1.9 to +3.9) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, mean messages waiting | 158.0 | 162.6 | +2.9% (-4.1 to +9.9) | -0.2% (-5.9 to +5.4) | +2.4% (-4.4 to +9.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.3% (-7.9 to +3.3) | -0.8% (-7.0 to +5.3) | +2.2% (-10.0 to +14.4) | **the runs disagree** |
| host CPU-seconds | 191.0 | 186.7 | -2.3% (-7.8 to +3.3) | -0.9% (-7.2 to +5.4) | +2.2% (-9.9 to +14.2) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.09 | 3.03 | -1.9% (-6.7 to +2.9) | -1.0% (-7.2 to +5.3) | +2.6% (-8.3 to +13.6) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 394, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 147.1 | -0.2% (-0.8 to +0.5) | -0.2% (-1.0 to +0.6) | -0.2% (-0.9 to +0.5) | EVEN, under the floor (the three runs' mean 0.21%) |
| throughput (messages a second consumed) | 172.1 | 172.1 | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,205 | 2,168 | -1.6% (-5.3 to +2.0) | +1.1% (-9.7 to +11.9) | +2.5% (-6.7 to +11.7) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,404 | 3,415 | +0.3% (-6.3 to +6.9) | +1.6% (-3.3 to +6.6) | -0.5% (-3.6 to +2.7) | EVEN, under the floor (the three runs' mean 0.50%) |
| end-to-end latency, median (ms) | 11.0 | 10.9 | -0.3% (-1.5 to +0.9) | -0.1% (-0.5 to +0.3) | +0.1% (-0.4 to +0.6) | EVEN, under the floor (the three runs' mean 0.10%) |
| end-to-end latency, mean (ms) | 289.1 | 287.8 | -0.4% (-2.4 to +1.5) | +1.9% (-9.9 to +13.8) | +2.7% (-4.3 to +9.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 646.3 | 654.0 | +1.2% (-14.0 to +16.4) | +1.3% (-4.3 to +6.9) | +1.5% (-7.4 to +10.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 52.7 | 52.4 | -0.5% (-8.2 to +7.2) | +1.9% (-10.3 to +14.0) | +1.7% (-2.4 to +5.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | +1.1% (-3.5 to +5.7) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.36%) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.262 | 0.261 | -0.5% (-2.5 to +1.6) | -0.9% (-5.0 to +3.2) | -0.2% (-3.0 to +2.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 470.2 | 468.0 | -0.5% (-2.4 to +1.5) | -0.9% (-4.9 to +3.1) | -0.2% (-2.9 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.09 | 7.07 | -0.3% (-2.5 to +1.9) | -0.7% (-5.5 to +4.1) | -0.0% (-2.0 to +2.0) | EVEN, under the floor (the three runs' mean 0.33%) |
| consumer changes written (the knob's moves) | 2 | 2.67 | +33.3% (-110.1 to +176.8) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,927, 1,927, 1,915 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.8 | 715.5 | -1.3% (-3.1 to +0.5) | -0.6% (-2.8 to +1.5) | -0.4% (-2.2 to +1.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 847.7 | 845.8 | -0.2% (-1.2 to +0.7) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.07%) |
| end-to-end latency, 95th percentile (ms) | 2,272 | 2,293 | +0.9% (-6.0 to +7.9) | +2.6% (-0.7 to +5.9) | -0.1% (-2.6 to +2.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,679 | +4.4% (-8.4 to +17.2) | +1.2% (-1.0 to +3.5) | -1.4% (-14.1 to +11.3) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.45 | 8.14 | -3.7% (-12.3 to +4.8) | -4.0% (-12.5 to +4.5) | -0.6% (-5.7 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 304.5 | 320.9 | +5.4% (-9.7 to +20.5) | +3.9% (-3.9 to +11.7) | +1.8% (-7.6 to +11.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,199 | 3,226 | +0.8% (-1.3 to +2.9) | +0.3% (-7.3 to +7.9) | -0.9% (-1.8 to +0.1) | **the runs disagree** |
| consumer lag, mean messages waiting | 266.5 | 277.3 | +4.0% (-11.0 to +19.1) | +3.7% (-4.4 to +11.7) | +1.7% (-7.3 to +10.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | +13.5% (-15.4 to +42.4) | +8.0% (-12.3 to +28.2) | +4.9% (-15.4 to +25.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 3.67 | +83.3% (+11.6 to +155.1) | +50.0% (+50.0 to +50.0) | +50.0% (-74.2 to +174.2) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.329 | 0.331 | +0.6% (-5.3 to +6.4) | -0.5% (-4.8 to +3.9) | -1.5% (-3.7 to +0.7) | **the runs disagree** |
| host CPU-seconds | 565.6 | 570.2 | +0.8% (-5.8 to +7.4) | -0.5% (-4.7 to +3.7) | -1.7% (-3.2 to -0.3) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.77 | +1.9% (-3.8 to +7.6) | +0.1% (-1.9 to +2.2) | -1.3% (-3.8 to +1.2) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 11.3 | +466.7% (-331.9 to +1265.3) | +300.0% (-560.6 to +1160.6) | +166.7% (-350.5 to +683.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 3 gauge-rows GAIN, 10 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 EVEN, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
