# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003710547 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40020507060 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40035619419 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 977, 964 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.5 | 365.4 | -0.0% (-0.5 to +0.5) | -0.2% (-0.6 to +0.3) | -0.3% (-2.2 to +1.6) | STEADY, under the floor (the three runs' mean 0.18%) |
| throughput (messages a second consumed) | 427.5 | 427.5 | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,255 | 2,227 | -1.3% (-7.1 to +4.6) | +1.6% (-6.4 to +9.6) | +1.9% (-13.9 to +17.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,573 | 3,521 | -1.4% (-11.1 to +8.2) | +4.0% (-7.5 to +15.5) | +0.5% (-12.2 to +13.3) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.62 | 8.58 | -0.5% (-4.2 to +3.2) | -0.4% (-0.9 to +0.1) | -0.8% (-6.9 to +5.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 302.1 | 298.6 | -1.1% (-8.1 to +5.8) | +1.9% (-7.3 to +11.2) | +2.0% (-16.6 to +20.6) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,634 | 1,604 | -1.8% (-6.0 to +2.3) | -0.1% (-8.2 to +8.0) | -0.2% (-10.9 to +10.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 133.8 | 132.0 | -1.4% (-9.8 to +7.0) | +1.9% (-7.1 to +10.9) | +1.7% (-14.9 to +18.2) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | +19.1% (+18.9 to +19.4) | **power given by the mean of our three runs, beyond the noise in 3 of 3** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +50.0% (+50.0 to +50.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.313 | 0.311 | -0.6% (-11.1 to +9.8) | -0.8% (-2.4 to +0.9) | -2.1% (-10.8 to +6.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 543.3 | 541.1 | -0.4% (-10.7 to +9.9) | -0.6% (-2.1 to +1.0) | -2.1% (-10.5 to +6.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.29 | -0.4% (-11.2 to +10.4) | -0.4% (-2.3 to +1.4) | -1.8% (-12.1 to +8.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +200.0% (+200.0 to +200.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 975, 976, 973 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.0 | 340.0 | -0.3% (-0.9 to +0.3) | +0.0% (-0.9 to +1.0) | -0.4% (-1.6 to +0.8) | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (messages a second consumed) | 418.9 | 418.9 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,511 | 2,550 | +1.6% (-4.3 to +7.4) | -0.7% (-10.3 to +8.9) | -0.5% (-5.3 to +4.3) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,687 | -4.8% (-13.1 to +3.5) | -0.5% (-12.0 to +11.0) | -0.4% (-4.7 to +3.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.37 | 9.59 | +2.3% (-2.9 to +7.4) | -2.8% (-11.7 to +6.1) | +0.1% (-2.4 to +2.6) | **the runs disagree** |
| end-to-end latency, mean (ms) | 385.9 | 386.6 | +0.2% (-3.0 to +3.4) | -0.7% (-1.6 to +0.1) | +2.1% (-3.7 to +7.8) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,675 | 1,667 | -0.5% (-10.7 to +9.8) | -0.3% (-3.4 to +2.8) | -0.9% (-6.2 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 166.3 | 167.1 | +0.5% (-1.2 to +2.1) | -1.0% (-3.9 to +1.8) | +0.7% (-5.1 to +6.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.296 | 0.292 | -1.3% (-6.4 to +3.8) | -1.0% (-5.3 to +3.4) | -0.9% (-5.5 to +3.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 206.9 | 204.4 | -1.2% (-6.0 to +3.7) | -0.9% (-5.2 to +3.4) | -0.8% (-5.3 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.33 | -0.9% (-6.3 to +4.4) | -1.0% (-5.1 to +3.2) | -0.5% (-5.7 to +4.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 390, 394, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.9 | 146.3 | -0.4% (-1.1 to +0.2) | +0.0% (-0.4 to +0.4) | -0.1% (-0.6 to +0.3) | STEADY, under the floor (the three runs' mean 0.17%) |
| throughput (messages a second consumed) | 171.6 | 171.6 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,135 | 2,176 | +1.9% (-3.1 to +6.9) | -2.9% (-7.1 to +1.4) | +0.7% (-8.6 to +10.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,429 | 3,496 | +2.0% (-3.8 to +7.7) | +3.7% (-3.3 to +10.7) | +0.4% (-5.8 to +6.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 10.9 | 10.8 | -0.8% (-1.5 to -0.1) | -1.3% (-6.7 to +4.1) | -0.1% (-0.3 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, mean (ms) | 285.0 | 296.3 | +4.0% (-4.0 to +11.9) | -0.9% (-5.9 to +4.0) | +0.7% (-5.5 to +6.9) | **the runs disagree** |
| consumer lag, most messages waiting at once | 648.7 | 659.7 | +1.7% (-7.4 to +10.8) | +0.5% (-4.2 to +5.3) | -0.9% (-8.2 to +6.4) | **the runs disagree** |
| consumer lag, mean messages waiting | 52.0 | 54.0 | +3.9% (-1.7 to +9.5) | -0.7% (-3.5 to +2.2) | -0.6% (-6.2 to +5.0) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% (-14.9 to +39.4) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.258 | 0.255 | -1.1% (-4.3 to +2.1) | -1.3% (-7.1 to +4.4) | -0.7% (-4.3 to +2.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 463.4 | 458.3 | -1.1% (-4.3 to +2.1) | -1.3% (-7.0 to +4.4) | -0.7% (-4.3 to +2.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7 | 6.95 | -0.7% (-3.4 to +2.0) | -1.3% (-7.0 to +4.4) | -0.6% (-3.8 to +2.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,930, 1,949, 1,936 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.9 | 724.9 | -0.0% (-0.8 to +0.8) | +0.1% (-0.4 to +0.5) | +0.4% (-1.4 to +2.1) | STEADY, under the floor (the three runs' mean 0.13%) |
| throughput (messages a second consumed) | 849.0 | 849.0 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,328 | -0.8% (-6.9 to +5.4) | -2.4% (-9.9 to +5.1) | -12.1% (-64.5 to +40.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,666 | 3,612 | -1.5% (-9.9 to +6.9) | -2.1% (-12.3 to +8.1) | -12.5% (-58.2 to +33.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.21 | 8.03 | -2.2% (-7.8 to +3.4) | +5.2% (-83.6 to +94.0) | -3.5% (-13.5 to +6.5) | **the runs disagree** |
| end-to-end latency, mean (ms) | 313.7 | 308.2 | -1.8% (-10.6 to +7.1) | -3.0% (-9.3 to +3.3) | -10.8% (-54.3 to +32.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,277 | 3,225 | -1.6% (-6.4 to +3.3) | -1.7% (-6.8 to +3.4) | -7.5% (-42.3 to +27.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 272.4 | 266.6 | -2.1% (-12.5 to +8.2) | -2.8% (-7.8 to +2.3) | -10.8% (-53.4 to +31.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% (-14.8 to +39.3) | +12.4% (-14.9 to +39.6) | +12.3% (-14.9 to +39.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +33.3% (-38.4 to +105.0) | +33.3% (-38.4 to +105.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.343 | 0.347 | +1.4% (-2.0 to +4.7) | -0.4% (-4.3 to +3.5) | +0.1% (-9.0 to +9.2) | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds | 588.9 | 596.6 | +1.3% (-1.9 to +4.5) | -0.4% (-4.1 to +3.2) | +0.1% (-9.9 to +10.2) | STEADY, under the floor (the three runs' mean 0.34%) |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.83 | +1.3% (-1.7 to +4.4) | -0.5% (-4.1 to +3.2) | -0.2% (-10.9 to +10.5) | STEADY, under the floor (the three runs' mean 0.21%) |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +166.7% (+23.2 to +310.1) | +200.0% (+200.0 to +200.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 15 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
