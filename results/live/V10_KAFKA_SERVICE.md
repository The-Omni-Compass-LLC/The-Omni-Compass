# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39109170592 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116292836 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39124642737 | `8b902df8d857` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 973, 975 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.4 | 365.6 | -0.2% (-0.8 to +0.3) | -0.0% (-0.5 to +0.4) | -0.2% (-1.2 to +0.8) | STEADY, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 429.6 | 429.6 | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,447 | +2.0% (-2.9 to +6.9) | -1.5% (-10.3 to +7.4) | +0.6% (-13.0 to +14.3) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,688 | 3,753 | +1.8% (-9.8 to +13.3) | -0.3% (-7.6 to +7.0) | +1.4% (-3.0 to +5.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.44 | 8.43 | -0.1% (-0.8 to +0.5) | -0.3% (-0.9 to +0.2) | -0.1% (-2.0 to +1.8) | STEADY, under the floor (the three runs' mean 0.19%) |
| end-to-end latency, mean (ms) | 319.8 | 324.3 | +1.4% (-5.1 to +7.9) | -0.7% (-6.6 to +5.3) | +1.8% (-8.5 to +12.2) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,701 | 1,708 | +0.4% (-6.8 to +7.6) | -1.3% (-7.6 to +5.1) | +0.7% (-4.9 to +6.3) | **the runs disagree** |
| consumer lag, mean messages waiting | 141.3 | 143.0 | +1.2% (-4.9 to +7.4) | -0.9% (-7.1 to +5.3) | +1.5% (-8.6 to +11.6) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | -0.5% (-3.5 to +2.6) | -0.3% (-3.2 to +2.6) | -0.7% (-2.7 to +1.3) | STEADY, under the floor (the three runs' mean 0.48%) |
| host CPU-seconds | 559.3 | 557.4 | -0.4% (-3.7 to +3.0) | -0.0% (-3.2 to +3.1) | -0.7% (-3.0 to +1.6) | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | -0.1% (-4.0 to +3.7) | -0.1% (-2.6 to +2.5) | -0.5% (-3.7 to +2.6) | STEADY, under the floor (the three runs' mean 0.23%) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 980, 972, 977 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343.0 | 342.2 | -0.2% (-0.6 to +0.1) | -0.9% (-1.8 to +0.1) | -0.1% (-0.5 to +0.2) | STEADY, under the floor (the three runs' mean 0.42%) |
| throughput (messages a second consumed) | 421.0 | 421.0 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,542 | 2,570 | +1.1% (-5.0 to +7.2) | +2.9% (-3.2 to +8.9) | -2.2% (-4.4 to +0.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,618 | 3,615 | -0.1% (-12.7 to +12.5) | +4.7% (-8.9 to +18.3) | -2.0% (-17.4 to +13.4) | **the runs disagree** |
| end-to-end latency, median (ms) | 9.65 | 9.5 | -1.5% (-16.1 to +13.1) | -2.3% (-9.9 to +5.3) | -1.3% (-6.2 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 384.2 | 388.1 | +1.0% (-0.8 to +2.8) | +4.2% (-2.9 to +11.4) | +0.0% (-1.7 to +1.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,672 | 1,654 | -1.1% (-5.4 to +3.1) | +1.4% (-1.8 to +4.7) | -0.3% (-0.9 to +0.3) | **the runs disagree** |
| consumer lag, mean messages waiting | 168.3 | 169.6 | +0.8% (-1.8 to +3.4) | +2.9% (-3.7 to +9.5) | +0.4% (-1.6 to +2.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.271 | 0.267 | -1.3% (-9.0 to +6.5) | -2.0% (-9.7 to +5.7) | -0.5% (-2.8 to +1.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 194.4 | 192.0 | -1.2% (-9.0 to +6.5) | -1.9% (-9.7 to +5.8) | -0.6% (-2.6 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.14 | 3.11 | -1.0% (-8.8 to +6.8) | -1.1% (-8.8 to +6.7) | -0.4% (-2.5 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.0 | 146.8 | -0.1% (-0.7 to +0.5) | -0.1% (-1.0 to +0.9) | +0.1% (-0.3 to +0.5) | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (messages a second consumed) | 172.9 | 172.9 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,528 | 2,515 | -0.5% (-8.4 to +7.4) | -0.2% (-9.3 to +9.0) | +0.3% (-3.8 to +4.5) | STEADY, under the floor (the three runs' mean 0.12%) |
| end-to-end latency, 99th percentile (ms) | 3,813 | 3,816 | +0.1% (-1.4 to +1.5) | +1.3% (-14.2 to +16.7) | -3.7% (-15.4 to +8.0) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% (-0.7 to +0.4) | -0.1% (-1.0 to +0.8) | -0.7% (-2.3 to +1.0) | STEADY, under the floor (the three runs' mean 0.30%) |
| end-to-end latency, mean (ms) | 340.2 | 340.3 | +0.1% (-5.4 to +5.5) | +0.4% (-10.4 to +11.1) | -2.0% (-8.5 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 719.0 | 718.0 | -0.1% (-7.4 to +7.1) | -1.9% (-11.3 to +7.5) | -2.3% (-3.2 to -1.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, mean messages waiting | 62.4 | 62.3 | -0.2% (-3.9 to +3.4) | -0.3% (-10.1 to +9.6) | -1.2% (-8.3 to +5.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.5% (-3.5 to +2.5) | -0.6% (-3.4 to +2.2) | -1.0% (-3.7 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 493.1 | 490.7 | -0.5% (-3.5 to +2.5) | -0.6% (-3.4 to +2.2) | -1.0% (-3.7 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.44 | 7.41 | -0.4% (-3.6 to +2.8) | -0.5% (-3.4 to +2.4) | -1.0% (-3.6 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,917, 1,930, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729.2 | 728.1 | -0.2% (-0.7 to +0.4) | -0.3% (-0.7 to +0.0) | -0.3% (-0.8 to +0.2) | STEADY, under the floor (the three runs' mean 0.27%) |
| throughput (messages a second consumed) | 843.3 | 843.3 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 1,971 | 1,943 | -1.4% (-8.8 to +5.9) | +0.6% (-3.4 to +4.6) | +1.4% (-5.8 to +8.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,170 | 3,235 | +2.0% (-7.4 to +11.5) | +0.4% (-6.1 to +7.0) | +3.8% (+1.5 to +6.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 7.29 | 7.14 | -2.1% (-7.2 to +3.1) | -6.3% (-16.7 to +4.0) | +0.8% (-2.4 to +4.1) | **the runs disagree** |
| end-to-end latency, mean (ms) | 250.9 | 253.4 | +1.0% (-1.7 to +3.6) | +0.8% (-5.6 to +7.3) | +3.6% (-5.3 to +12.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 2,893 | 2,914 | +0.7% (-1.1 to +2.5) | +0.4% (-2.6 to +3.3) | +2.0% (-3.7 to +7.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 215.6 | 216.9 | +0.6% (-2.9 to +4.1) | +0.4% (-5.9 to +6.6) | +3.9% (-5.0 to +12.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | +19.3% (+19.2 to +19.5) | +12.4% (-14.9 to +39.6) | -0.3% (-0.3 to -0.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 3 | +50.0% (+50.0 to +50.0) | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.332 | 0.334 | +0.6% (-0.9 to +2.1) | +0.8% (-1.6 to +3.1) | -0.6% (-3.3 to +2.0) | **the runs disagree** |
| host CPU-seconds | 591.8 | 595.8 | +0.7% (-1.1 to +2.4) | +1.2% (-1.5 to +3.9) | -0.5% (-2.7 to +1.7) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.82 | +0.8% (-0.9 to +2.6) | +1.5% (-1.0 to +4.0) | -0.2% (-2.3 to +1.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% (+200.0 to +200.0) | +166.7% (+23.2 to +310.1) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 6 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
