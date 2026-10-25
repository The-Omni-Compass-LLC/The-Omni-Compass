# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062228122 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067527221 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40130177581 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 983, 977 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.4 | 365.4 | -0.0% (-0.7 to +0.7) | +0.1% (-0.0 to +0.2) | -0.2% (-0.4 to +0.0) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (messages a second consumed) | 428.4 | 428.4 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,329 | -0.6% (-9.5 to +8.2) | -1.0% (-3.6 to +1.5) | +0.0% (-13.8 to +13.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,642 | 3,704 | +1.7% (-9.4 to +12.8) | +0.8% (-2.8 to +4.4) | +3.5% (-3.9 to +10.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.51 | 8.52 | +0.1% (-1.3 to +1.5) | -0.2% (-0.6 to +0.3) | -0.6% (-3.1 to +1.8) | EVEN, under the floor (the three runs' mean 0.24%) |
| end-to-end latency, mean (ms) | 312.6 | 312.0 | -0.2% (-11.3 to +10.9) | -0.8% (-4.3 to +2.6) | +1.4% (-5.3 to +8.1) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,664 | 1,654 | -0.6% (-6.8 to +5.6) | -1.4% (-5.7 to +2.9) | +0.7% (-5.0 to +6.4) | **the runs disagree** |
| consumer lag, mean messages waiting | 138.6 | 137.9 | -0.5% (-10.1 to +9.1) | -0.6% (-3.1 to +2.0) | +1.1% (-5.9 to +8.1) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | +12.2% (-14.8 to +39.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +33.3% (-38.4 to +105.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.305 | 0.306 | +0.2% (-0.7 to +1.1) | -0.5% (-1.9 to +0.9) | +0.4% (-3.5 to +4.3) | EVEN, under the floor (the three runs' mean 0.06%) |
| host CPU-seconds | 530.6 | 532.1 | +0.3% (-0.9 to +1.5) | -0.4% (-1.6 to +0.7) | +0.5% (-3.3 to +4.3) | EVEN, under the floor (the three runs' mean 0.11%) |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | +0.3% (-0.9 to +1.6) | -0.6% (-1.6 to +0.5) | +0.7% (-2.9 to +4.3) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +166.7% (+23.2 to +310.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 980, 972, 980 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.7 | 341.6 | -0.0% (-1.7 to +1.7) | -0.2% (-0.3 to -0.1) | -0.2% (-0.6 to +0.1) | EVEN, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 421.0 | 421.0 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,508 | -2.9% (-13.1 to +7.2) | +1.1% (-18.9 to +21.2) | +1.2% (-7.6 to +10.0) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,728 | 3,796 | +1.8% (-10.7 to +14.3) | -2.5% (-11.5 to +6.6) | -3.2% (-8.5 to +2.1) | **the runs disagree** |
| end-to-end latency, median (ms) | 15.0 | 11.0 | -26.7% (-127.2 to +73.8) | +0.0% (-0.7 to +0.7) | -0.5% (-4.4 to +3.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 397.2 | 395.1 | -0.5% (-14.5 to +13.5) | -0.0% (-10.3 to +10.3) | +0.8% (-0.0 to +1.6) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,688 | 1,707 | +1.1% (-4.1 to +6.4) | +0.4% (-3.1 to +4.0) | +0.6% (-0.0 to +1.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 174.2 | 171.9 | -1.3% (-17.4 to +14.7) | -0.3% (-10.5 to +10.0) | +0.9% (-1.0 to +2.9) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.268 | -0.3% (-6.4 to +5.9) | -0.7% (-2.4 to +1.1) | -0.8% (-4.6 to +3.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 192.6 | 192.2 | -0.2% (-6.2 to +5.8) | -0.6% (-2.4 to +1.1) | -0.8% (-4.7 to +3.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.12 | 3.12 | -0.2% (-4.9 to +4.5) | -0.4% (-2.2 to +1.4) | -0.6% (-4.2 to +3.1) | EVEN, under the floor (the three runs' mean 0.39%) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 394, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.7 | -0.3% (-0.4 to -0.1) | +0.0% (-0.5 to +0.5) | -0.3% (-0.4 to -0.2) | EVEN, under the floor (the three runs' mean 0.18%) |
| throughput (messages a second consumed) | 172.8 | 172.8 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,499 | +1.6% (-3.6 to +6.8) | -2.6% (-9.6 to +4.4) | +2.3% (-3.9 to +8.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,845 | 3,859 | +0.4% (-4.4 to +5.1) | -1.5% (-10.6 to +7.7) | +2.2% (-8.9 to +13.3) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% (-0.4 to +0.4) | -0.1% (-1.7 to +1.5) | -1.1% (-6.7 to +4.5) | EVEN, under the floor (the three runs' mean 0.39%) |
| end-to-end latency, mean (ms) | 332.1 | 338.4 | +1.9% (-3.0 to +6.8) | -1.5% (-7.7 to +4.7) | +3.1% (+0.9 to +5.2) | **the runs disagree** |
| consumer lag, most messages waiting at once | 703.0 | 716.7 | +1.9% (-3.0 to +6.9) | -1.7% (-8.3 to +4.9) | +2.0% (-3.9 to +7.8) | **the runs disagree** |
| consumer lag, mean messages waiting | 60.8 | 62.2 | +2.3% (-2.4 to +7.0) | -1.9% (-5.8 to +1.9) | +3.2% (+0.6 to +5.7) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.7% (-3.3 to +1.8) | -0.7% (-4.0 to +2.7) | -2.4% (-14.3 to +9.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 493.6 | 490.3 | -0.7% (-3.1 to +1.8) | -0.6% (-4.1 to +2.9) | -2.4% (-14.4 to +9.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.42 | -0.4% (-3.0 to +2.2) | -0.6% (-4.5 to +3.3) | -2.1% (-14.0 to +9.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,951, 1,950, 1,924 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732.9 | 731.2 | -0.2% (-0.8 to +0.4) | -0.1% (-0.6 to +0.4) | -1.4% (-4.4 to +1.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 858.0 | 858.3 | +0.0% (-0.1 to +0.2) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,293 | 2,319 | +1.1% (-3.0 to +5.3) | +1.0% (-1.6 to +3.5) | +70.9% (-87.7 to +229.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,605 | -2.3% (-9.7 to +5.1) | -1.5% (-4.7 to +1.7) | +58.9% (-68.0 to +185.8) | **the runs disagree** |
| end-to-end latency, median (ms) | 15.4 | 11.2 | -27.2% (-112.3 to +57.9) | -30.4% (-122.0 to +61.2) | -0.9% (-7.6 to +5.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 322.1 | 323.9 | +0.5% (-3.9 to +5.0) | -1.9% (-6.5 to +2.7) | +68.6% (-83.5 to +220.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,305 | 3,332 | +0.8% (-4.7 to +6.3) | -2.1% (-5.5 to +1.3) | +46.0% (-54.2 to +146.2) | **the runs disagree** |
| consumer lag, mean messages waiting | 285.7 | 284.7 | -0.3% (-5.0 to +4.3) | -2.5% (-6.7 to +1.7) | +66.1% (-81.2 to +213.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% (-14.9 to +39.5) | +12.4% (-15.0 to +39.7) | -0.3% (-0.3 to -0.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.286 | 0.283 | -1.0% (-7.4 to +5.4) | +0.1% (-1.8 to +2.1) | -1.4% (-3.8 to +1.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 510.2 | 505.5 | -0.9% (-6.9 to +5.0) | +0.1% (-1.9 to +2.2) | -1.1% (-3.8 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.54 | -0.7% (-6.1 to +4.7) | +0.3% (-1.3 to +1.8) | +0.2% (-4.7 to +5.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% (+23.2 to +310.1) | +200.0% (-48.4 to +448.4) | +166.7% (+23.2 to +310.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 10 gauge-rows GAIN, 3 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 EVEN, 13 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
