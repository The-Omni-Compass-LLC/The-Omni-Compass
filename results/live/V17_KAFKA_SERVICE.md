# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005908588 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40022521256 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40037209884 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 973, 972 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.0 | 365.3 | -0.2% (-1.1 to +0.7) | -0.2% (-0.3 to -0.0) | -0.1% (-0.2 to +0.0) | STEADY, under the floor (the three runs' mean 0.16%) |
| throughput (messages a second consumed) | 427.9 | 427.8 | -0.0% (-0.2 to +0.1) | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,239 | 2,235 | -0.1% (-10.0 to +9.7) | -1.4% (-6.2 to +3.4) | +0.5% (-2.3 to +3.4) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,580 | 3,627 | +1.3% (-9.1 to +11.7) | +4.3% (-10.9 to +19.6) | +0.2% (-9.9 to +10.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.34 | 8.27 | -0.8% (-1.5 to -0.0) | +1.5% (-0.8 to +3.7) | +0.6% (-2.2 to +3.5) | **the runs disagree** |
| end-to-end latency, mean (ms) | 295.1 | 298.5 | +1.1% (-9.5 to +11.8) | +1.7% (-0.1 to +3.5) | +0.8% (-0.1 to +1.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,608 | 1,614 | +0.4% (-5.3 to +6.0) | -0.1% (-2.4 to +2.3) | -0.7% (-3.3 to +1.9) | STEADY, under the floor (the three runs' mean 0.15%) |
| consumer lag, mean messages waiting | 129.9 | 131.4 | +1.2% (-8.7 to +11.0) | +1.7% (+0.2 to +3.1) | +1.1% (-0.7 to +2.9) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% (-21.2 to +33.1) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.31 | 0.308 | -0.5% (-1.2 to +0.2) | +3.3% (-2.8 to +9.3) | +0.7% (-0.6 to +2.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 553.1 | 551.4 | -0.3% (-1.0 to +0.4) | +3.3% (-2.7 to +9.2) | +0.6% (-0.7 to +1.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.35 | -0.1% (-1.4 to +1.1) | +3.5% (-2.5 to +9.5) | +0.7% (-0.7 to +2.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 968, 948, 983 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 338.6 | 363.8 | +7.4% (-22.2 to +37.1) | -0.0% (-3.2 to +3.1) | -0.3% (-0.9 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 416.1 | 416.1 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,508 | 1,592 | -36.5% (-153.5 to +80.4) | +30.3% (-90.8 to +151.4) | +0.0% (-5.3 to +5.4) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,822 | 2,548 | -33.3% (-128.9 to +62.2) | +28.6% (-60.1 to +117.3) | +1.0% (-9.1 to +11.1) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.66 | 8.46 | -2.3% (-11.5 to +6.9) | -1.0% (-6.5 to +4.4) | -8.7% (-153.5 to +136.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 381.1 | 244.4 | -35.9% (-142.3 to +70.6) | +23.3% (-54.4 to +101.1) | +1.1% (-1.3 to +3.4) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,622 | 1,179 | -27.3% (-108.3 to +53.7) | +23.0% (-61.8 to +107.9) | -0.3% (-3.4 to +2.8) | **the runs disagree** |
| consumer lag, mean messages waiting | 163.5 | 105.2 | -35.6% (-140.9 to +69.7) | +22.9% (-53.5 to +99.2) | +1.6% (-2.3 to +5.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% (-44.1 to +68.6) | -0.7% (-1.1 to -0.3) | -0.8% (-0.8 to -0.8) | **the runs disagree** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-110.1 to +176.8) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.293 | 0.293 | +0.1% (-1.2 to +1.5) | +2.0% (-5.0 to +9.0) | -0.2% (-3.6 to +3.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 210.0 | 210.3 | +0.2% (-1.3 to +1.6) | +2.0% (-4.8 to +8.9) | -0.2% (-3.5 to +3.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.23 | -6.0% (-31.3 to +19.3) | +2.0% (-4.0 to +8.0) | +0.2% (-3.0 to +3.3) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (-120.2 to +453.5) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.8 | -0.2% (-0.8 to +0.4) | +0.0% (-0.6 to +0.7) | +0.1% (-0.1 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (messages a second consumed) | 173.2 | 173.2 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,550 | +0.1% (-2.9 to +3.2) | -1.9% (-12.9 to +9.2) | -3.9% (-11.5 to +3.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,841 | 3,955 | +3.0% (-7.3 to +13.3) | +0.6% (-11.0 to +12.2) | -2.1% (-8.2 to +4.1) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.7 | 11.6 | -0.3% (-1.0 to +0.4) | -0.2% (-0.8 to +0.4) | +0.0% (-1.1 to +1.1) | STEADY, under the floor (the three runs' mean 0.17%) |
| end-to-end latency, mean (ms) | 341.2 | 348.3 | +2.1% (-6.1 to +10.3) | -1.3% (-10.7 to +8.0) | -3.6% (-6.4 to -0.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 711.3 | 732.0 | +2.9% (-1.5 to +7.3) | +0.9% (-7.2 to +9.0) | -2.2% (-6.8 to +2.4) | **the runs disagree** |
| consumer lag, mean messages waiting | 62.5 | 63.5 | +1.6% (-5.5 to +8.8) | -1.4% (-11.9 to +9.2) | -3.7% (-5.9 to -1.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.289 | 0.284 | -1.6% (-4.7 to +1.4) | -0.9% (-4.4 to +2.5) | -0.4% (-4.6 to +3.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 509.1 | 500.9 | -1.6% (-4.7 to +1.4) | -1.0% (-4.5 to +2.5) | -0.5% (-4.8 to +3.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 7.58 | -1.4% (-4.9 to +2.1) | -1.0% (-4.9 to +2.9) | -0.6% (-4.9 to +3.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,927, 1,907, 1,963 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.2 | 724.4 | +0.0% (-0.7 to +0.8) | +0.0% (-0.9 to +1.0) | -0.2% (-0.8 to +0.5) | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (messages a second consumed) | 847.7 | 847.8 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,269 | 2,236 | -1.4% (-9.3 to +6.4) | -0.1% (-4.0 to +3.8) | +0.1% (-10.5 to +10.7) | STEADY, under the floor (the three runs' mean 0.48%) |
| end-to-end latency, 99th percentile (ms) | 3,636 | 3,542 | -2.6% (-4.9 to -0.2) | -1.8% (-9.2 to +5.7) | -1.2% (-7.3 to +4.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 8.13 | 8.11 | -0.4% (-10.8 to +10.1) | -1.3% (-2.5 to -0.2) | -7.6% (-11.4 to -3.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, mean (ms) | 306.2 | 301.7 | -1.5% (-8.4 to +5.5) | -1.2% (-10.3 to +8.0) | +0.1% (-10.9 to +11.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,259 | 3,170 | -2.8% (-7.6 to +2.1) | -1.3% (-5.3 to +2.6) | -0.8% (-5.6 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 265.7 | 261.4 | -1.6% (-9.1 to +5.8) | -1.5% (-9.8 to +6.9) | -0.3% (-10.7 to +10.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% (-15.0 to +39.9) | +13.0% (-15.7 to +41.6) | -0.3% (-0.3 to -0.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.347 | 0.337 | -2.7% (-9.9 to +4.5) | -0.3% (-5.9 to +5.3) | +7.5% (-5.7 to +20.6) | **the runs disagree** |
| host CPU-seconds | 595.6 | 580.1 | -2.6% (-10.6 to +5.4) | -0.2% (-5.7 to +5.4) | +7.3% (-5.6 to +20.2) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.78 | -2.6% (-11.4 to +6.1) | -0.2% (-6.7 to +6.2) | +7.5% (-5.7 to +20.6) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +166.7% (+23.2 to +310.1) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
