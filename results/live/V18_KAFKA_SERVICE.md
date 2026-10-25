# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062235164 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067533814 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40131354530 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 975, 976 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.3 | 364.9 | -0.1% (-0.1 to -0.1) | -0.1% (-0.7 to +0.6) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.09%) |
| throughput (messages a second consumed) | 427.7 | 427.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,311 | -0.9% (-6.5 to +4.6) | +1.7% (-9.4 to +12.9) | -2.6% (-13.9 to +8.6) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,674 | +0.1% (-6.3 to +6.4) | -0.8% (-9.5 to +7.9) | -1.0% (-8.8 to +6.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.85 | 8.76 | -1.0% (-6.6 to +4.5) | -0.4% (-2.3 to +1.4) | +0.1% (-1.8 to +2.0) | EVEN, under the floor (the three runs' mean 0.44%) |
| end-to-end latency, mean (ms) | 310.1 | 306.6 | -1.2% (-5.6 to +3.3) | +0.7% (-4.0 to +5.5) | -2.0% (-8.6 to +4.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,655 | 1,646 | -0.5% (-4.5 to +3.5) | +1.1% (-5.1 to +7.3) | -2.6% (-12.3 to +7.1) | **the runs disagree** |
| consumer lag, mean messages waiting | 136.6 | 135.2 | -1.0% (-4.8 to +2.7) | +0.5% (-5.1 to +6.2) | -2.1% (-9.6 to +5.3) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% (-21.2 to +33.1) | -0.3% (-0.3 to -0.3) | +0.7% (-3.9 to +5.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.339 | 0.331 | -2.3% (-10.8 to +6.2) | -1.6% (-9.1 to +6.0) | +1.0% (-5.5 to +7.5) | **the runs disagree** |
| host CPU-seconds | 588.7 | 576.2 | -2.1% (-10.4 to +6.2) | -1.6% (-9.9 to +6.7) | +1.1% (-5.6 to +7.8) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.51 | -2.0% (-10.3 to +6.2) | -1.5% (-10.5 to +7.4) | +1.3% (-5.4 to +7.9) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 981, 978, 977 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.7 | 340.8 | -0.5% (-2.2 to +1.2) | -0.2% (-0.6 to +0.3) | -0.3% (-0.5 to -0.1) | EVEN, under the floor (the three runs' mean 0.34%) |
| throughput (messages a second consumed) | 421.7 | 421.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,646 | +3.2% (-0.0 to +6.4) | -2.9% (-6.9 to +1.1) | -0.8% (-10.8 to +9.2) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,787 | -4.9% (-25.8 to +16.0) | +0.5% (-6.2 to +7.3) | +0.9% (-16.5 to +18.4) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.9 | 10.0 | -16.2% (-54.4 to +22.0) | +0.5% (-3.0 to +4.0) | -0.9% (-6.2 to +4.4) | **the runs disagree** |
| end-to-end latency, mean (ms) | 398.6 | 407.8 | +2.3% (-6.9 to +11.6) | +0.8% (+0.4 to +1.2) | +0.4% (-1.3 to +2.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, most messages waiting at once | 1,733 | 1,730 | -0.2% (-10.2 to +9.8) | +0.4% (+0.3 to +0.6) | +0.5% (-2.7 to +3.7) | EVEN, under the floor (the three runs' mean 0.25%) |
| consumer lag, mean messages waiting | 174.9 | 178.7 | +2.2% (-6.1 to +10.4) | +0.6% (-1.8 to +3.1) | -0.2% (-3.4 to +3.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.27 | +0.7% (-5.0 to +6.5) | -0.6% (-3.5 to +2.4) | -0.8% (-4.4 to +2.9) | **the runs disagree** |
| host CPU-seconds | 192.3 | 193.7 | +0.8% (-4.9 to +6.5) | -0.6% (-3.5 to +2.3) | -0.7% (-4.3 to +2.9) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.11 | 3.15 | +1.3% (-2.6 to +5.2) | -0.4% (-3.8 to +3.0) | -0.4% (-3.9 to +3.0) | EVEN, under the floor (the three runs' mean 0.16%) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 393, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.6 | -0.3% (-1.1 to +0.4) | +0.2% (+0.1 to +0.3) | +5.9% (-19.9 to +31.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (messages a second consumed) | 172.8 | 172.8 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,538 | +3.2% (+1.4 to +5.1) | -1.2% (-6.3 to +3.8) | -35.6% (-179.1 to +107.9) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,843 | 3,824 | -0.5% (-12.9 to +11.9) | -5.7% (-11.3 to -0.2) | -36.2% (-160.3 to +87.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.3% (-0.6 to +0.1) | -0.0% (-0.2 to +0.2) | -0.7% (-2.0 to +0.6) | EVEN, under the floor (the three runs' mean 0.32%) |
| end-to-end latency, mean (ms) | 332.8 | 344.2 | +3.4% (-3.5 to +10.3) | -3.1% (-4.7 to -1.4) | -35.1% (-167.8 to +97.7) | **the runs disagree** |
| consumer lag, most messages waiting at once | 711.3 | 720.0 | +1.2% (-5.4 to +7.9) | -3.1% (-12.6 to +6.4) | -28.4% (-142.1 to +85.3) | **the runs disagree** |
| consumer lag, mean messages waiting | 61.0 | 63.1 | +3.4% (-0.8 to +7.7) | -2.5% (-6.9 to +1.8) | -34.6% (-165.8 to +96.7) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | +9.3% (-28.6 to +47.2) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +50.0% (+50.0 to +50.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.285 | 0.281 | -1.2% (-4.6 to +2.2) | -0.0% (-2.2 to +2.1) | -0.4% (-4.1 to +3.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 501.7 | 495.7 | -1.2% (-4.8 to +2.4) | -0.0% (-2.3 to +2.2) | -0.4% (-4.1 to +3.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.5 | -0.9% (-3.7 to +2.0) | -0.2% (-2.4 to +2.0) | -5.5% (-24.4 to +13.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +200.0% (+200.0 to +200.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,929, 1,940, 1,949 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.0 | 724.5 | -0.2% (-0.5 to +0.1) | -0.4% (-1.1 to +0.2) | -0.3% (-0.4 to -0.2) | EVEN, under the floor (the three runs' mean 0.30%) |
| throughput (messages a second consumed) | 848.4 | 848.4 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,213 | 2,258 | +2.0% (-5.2 to +9.2) | +9.2% (-10.6 to +29.1) | +1.3% (-0.9 to +3.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,685 | +0.6% (-8.3 to +9.6) | +7.9% (-4.7 to +20.6) | +0.3% (-5.7 to +6.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.43 | 8.36 | -0.8% (-4.6 to +3.1) | +0.8% (-2.0 to +3.7) | -0.6% (-1.3 to +0.2) | **the runs disagree** |
| end-to-end latency, mean (ms) | 304.1 | 310.1 | +2.0% (-2.5 to +6.4) | +10.6% (-5.8 to +27.0) | +1.9% (-4.3 to +8.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,205 | 3,222 | +0.5% (-5.2 to +6.3) | +2.8% (-11.3 to +16.9) | +0.1% (-4.9 to +5.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 264.1 | 269.1 | +1.9% (-3.0 to +6.8) | +9.7% (-5.9 to +25.4) | +1.5% (-2.7 to +5.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +0.7% (-3.9 to +5.4) | -0.3% (-0.3 to -0.3) | EVEN, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.332 | 0.329 | -1.2% (-7.3 to +5.0) | +2.4% (-0.4 to +5.3) | -0.4% (-4.2 to +3.4) | **the runs disagree** |
| host CPU-seconds | 571.2 | 565.7 | -1.0% (-6.6 to +4.6) | +2.5% (-0.4 to +5.4) | -0.2% (-3.9 to +3.5) | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | -0.8% (-6.3 to +4.8) | +3.0% (+0.4 to +5.6) | +0.1% (-3.6 to +3.7) | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 6 gauge-rows GAIN, 7 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 EVEN, 13 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
