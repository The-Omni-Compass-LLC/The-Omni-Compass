# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149249969 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39157787056 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39166374877 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 976, 981 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.6 | 365.9 | -0.2% (-0.7 to +0.3) | -0.4% (-1.1 to +0.3) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.22%) |
| throughput (messages a second consumed) | 427.7 | 427.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.02%) |
| end-to-end latency, 95th percentile (ms) | 2,178 | 2,249 | +3.3% (-11.0 to +17.6) | +1.0% (-7.0 to +9.0) | -0.9% (-13.2 to +11.3) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,424 | 3,465 | +1.2% (-6.6 to +9.0) | +2.6% (-0.5 to +5.8) | -3.1% (-17.8 to +11.5) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.2 | 8.19 | -0.2% (-2.9 to +2.5) | -0.1% (-1.1 to +1.0) | -0.5% (-2.9 to +1.9) | STEADY, under the floor (the three runs' mean 0.24%) |
| end-to-end latency, mean (ms) | 284.7 | 292.4 | +2.7% (-10.9 to +16.4) | +3.2% (-5.9 to +12.2) | -1.1% (-15.6 to +13.4) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,588 | 1,588 | +0.0% (-2.8 to +2.8) | +1.1% (-7.3 to +9.4) | -0.4% (-13.0 to +12.2) | STEADY, under the floor (the three runs' mean 0.22%) |
| consumer lag, mean messages waiting | 125.7 | 128.7 | +2.4% (-10.4 to +15.2) | +2.7% (-6.4 to +11.8) | -1.7% (-15.1 to +11.6) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% (-3.9 to +5.4) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.297 | 0.296 | -0.2% (-2.7 to +2.3) | -0.4% (-4.2 to +3.5) | -1.2% (-3.7 to +1.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 529.7 | 529.1 | -0.1% (-2.2 to +2.0) | -0.1% (-3.8 to +3.7) | -1.1% (-3.5 to +1.2) | STEADY, under the floor (the three runs' mean 0.44%) |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.21 | +0.1% (-1.6 to +1.9) | +0.3% (-3.5 to +4.0) | -1.1% (-3.6 to +1.4) | STEADY, under the floor (the three runs' mean 0.25%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 976, 976, 979 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.9 | 340.8 | -0.0% (-0.1 to +0.1) | -0.3% (-0.3 to -0.3) | -0.3% (-0.8 to +0.3) | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (messages a second consumed) | 419.1 | 419.1 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.1% (-0.5 to +0.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| end-to-end latency, 95th percentile (ms) | 2,515 | 2,536 | +0.9% (-7.1 to +8.8) | -1.8% (-7.3 to +3.7) | +0.5% (-3.3 to +4.3) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,727 | -3.8% (-18.0 to +10.4) | +1.7% (-8.0 to +11.4) | +2.4% (-11.1 to +16.0) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.96 | 8.77 | -2.2% (-7.5 to +3.2) | -0.8% (-1.4 to -0.1) | +1.0% (-5.4 to +7.5) | **the runs disagree** |
| end-to-end latency, mean (ms) | 379.0 | 382.1 | +0.8% (-1.2 to +2.8) | +0.6% (-1.2 to +2.3) | +0.6% (-0.7 to +2.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,664 | 1,661 | -0.2% (-4.4 to +4.1) | -0.8% (-3.2 to +1.6) | +0.3% (-3.5 to +4.1) | STEADY, under the floor (the three runs' mean 0.20%) |
| consumer lag, mean messages waiting | 163.5 | 164.8 | +0.8% (-1.0 to +2.5) | -0.1% (-3.2 to +3.1) | +1.3% (-1.6 to +4.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.308 | 0.304 | -1.1% (-7.9 to +5.6) | -0.9% (-4.6 to +2.8) | -0.4% (-4.5 to +3.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 220.9 | 218.4 | -1.1% (-7.8 to +5.6) | -0.9% (-4.6 to +2.8) | -0.3% (-4.1 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.55 | -1.1% (-7.7 to +5.5) | -0.6% (-4.2 to +3.1) | -0.1% (-4.3 to +4.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 394, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 149.7 | +1.8% (-5.9 to +9.4) | +0.2% (-0.5 to +0.9) | -0.0% (-0.1 to +0.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 172.6 | 172.6 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,374 | 2,430 | +2.4% (-13.7 to +18.4) | -1.8% (-6.9 to +3.3) | +1.9% (-2.7 to +6.5) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,663 | 3,843 | +4.9% (-21.6 to +31.5) | -5.1% (-12.9 to +2.7) | -3.3% (-9.5 to +2.9) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% (-1.1 to +1.1) | -0.1% (-1.0 to +0.9) | -0.2% (-0.3 to -0.2) | STEADY, under the floor (the three runs' mean 0.10%) |
| end-to-end latency, mean (ms) | 319.1 | 308.2 | -3.4% (-16.5 to +9.6) | -3.0% (-10.6 to +4.5) | -0.2% (-1.9 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 698.0 | 729.0 | +4.4% (-11.9 to +20.8) | -2.4% (-7.9 to +3.0) | +1.9% (-4.4 to +8.1) | **the runs disagree** |
| consumer lag, mean messages waiting | 59.0 | 56.2 | -4.7% (-21.8 to +12.5) | -2.8% (-9.5 to +3.9) | -0.0% (-0.4 to +0.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% (-3.9 to +5.4) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.279 | 0.28 | +0.2% (-2.1 to +2.5) | -0.8% (-4.0 to +2.5) | -0.6% (-2.8 to +1.5) | STEADY, under the floor (the three runs' mean 0.41%) |
| host CPU-seconds | 491.2 | 492.7 | +0.3% (-2.1 to +2.7) | -0.8% (-4.0 to +2.5) | -0.7% (-2.9 to +1.6) | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.31 | -1.4% (-10.1 to +7.3) | -1.0% (-4.0 to +2.1) | -0.6% (-2.9 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,930, 1,935, 1,933 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725.5 | 725.0 | -0.1% (-1.0 to +0.9) | -0.3% (-1.0 to +0.4) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.12%) |
| throughput (messages a second consumed) | 848.7 | 848.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,250 | 2,242 | -0.4% (-14.1 to +13.4) | +2.9% (-4.3 to +10.2) | +0.0% (-1.9 to +1.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,564 | 3,544 | -0.6% (-6.4 to +5.2) | -0.9% (-7.7 to +5.9) | -2.2% (-13.0 to +8.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.38 | 7.86 | -6.2% (-15.3 to +2.9) | -3.9% (-11.1 to +3.3) | -2.3% (-13.5 to +8.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 304.4 | 302.8 | -0.5% (-10.7 to +9.6) | +2.0% (-9.8 to +13.9) | -0.5% (-1.9 to +1.0) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,212 | 3,206 | -0.2% (-5.9 to +5.5) | +1.7% (-6.2 to +9.6) | -1.0% (-4.5 to +2.6) | **the runs disagree** |
| consumer lag, mean messages waiting | 264.6 | 262.8 | -0.7% (-10.7 to +9.3) | +1.1% (-10.6 to +12.8) | -0.5% (-1.5 to +0.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% (-14.9 to +39.5) | +6.0% (-21.3 to +33.3) | +5.9% (-21.0 to +32.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.325 | 0.327 | +0.6% (-4.0 to +5.3) | +1.8% (-1.0 to +4.6) | -1.3% (-8.8 to +6.2) | **the runs disagree** |
| host CPU-seconds | 557.0 | 561.9 | +0.9% (-4.6 to +6.4) | +2.1% (-0.9 to +5.2) | -1.2% (-9.8 to +7.4) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | +1.0% (-4.6 to +6.5) | +2.4% (-0.5 to +5.2) | -1.2% (-9.9 to +7.6) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +133.3% (-10.1 to +276.8) | +133.3% (-10.1 to +276.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 10 gauge-rows GAIN, 3 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
