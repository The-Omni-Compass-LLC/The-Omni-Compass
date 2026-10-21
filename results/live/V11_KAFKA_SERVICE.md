# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150481307 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39159000835 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39167574190 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 984, 976 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.3 | 364.9 | -0.1% (-0.6 to +0.4) | -0.1% (-0.5 to +0.3) | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 428.6 | 428.6 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,395 | 2,372 | -1.0% (-16.6 to +14.7) | +1.2% (-3.2 to +5.6) | -0.4% (-6.6 to +5.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,675 | 3,776 | +2.8% (-2.2 to +7.7) | -1.2% (-6.6 to +4.1) | -2.3% (-11.1 to +6.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.55 | 8.54 | -0.2% (-1.9 to +1.5) | +0.2% (-3.5 to +3.9) | -0.4% (-0.9 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 317.7 | 320.5 | +0.9% (-6.6 to +8.4) | +0.7% (-2.2 to +3.6) | -1.5% (-9.1 to +6.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,685 | 1,681 | -0.3% (-5.8 to +5.2) | -0.8% (-3.7 to +2.1) | +0.3% (-7.0 to +7.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 140.6 | 141.6 | +0.7% (-5.9 to +7.3) | +0.6% (-3.6 to +4.8) | -1.3% (-8.8 to +6.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | +0.3% (-2.3 to +2.8) | +0.4% (-6.1 to +6.8) | +0.0% (-3.2 to +3.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 534.4 | 537.7 | +0.6% (-2.1 to +3.3) | +0.5% (-5.8 to +6.8) | +0.3% (-3.0 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.27 | +0.7% (-1.5 to +2.9) | +0.6% (-5.4 to +6.6) | +0.4% (-3.2 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 973, 973 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.1 | 340.3 | +0.1% (-0.9 to +1.1) | -0.2% (-0.4 to +0.0) | -0.0% (-1.4 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 418.6 | 418.6 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,520 | 2,482 | -1.5% (-8.2 to +5.2) | +0.9% (-3.0 to +4.7) | +1.0% (-8.6 to +10.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,877 | 3,663 | -5.5% (-17.7 to +6.6) | +3.5% (-3.8 to +10.9) | -6.6% (-18.0 to +4.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 9.83 | 9.28 | -5.7% (-17.4 to +6.0) | -5.6% (-14.5 to +3.3) | -2.1% (-7.3 to +3.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 388.7 | 383.2 | -1.4% (-10.8 to +7.9) | +0.2% (-1.9 to +2.3) | -1.5% (-8.5 to +5.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,661 | 1,664 | +0.2% (-5.7 to +6.0) | +0.6% (-0.5 to +1.8) | -1.7% (-7.2 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 168.4 | 164.9 | -2.1% (-13.5 to +9.3) | -0.1% (-4.0 to +3.8) | -2.0% (-11.1 to +7.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% (-6.8 to +4.7) | -4.5% (-18.4 to +9.5) | -1.9% (-5.4 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 209.2 | 207.1 | -1.0% (-6.8 to +4.8) | -4.4% (-18.5 to +9.6) | -2.0% (-5.5 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.37 | -1.1% (-6.0 to +3.8) | -4.3% (-18.1 to +9.6) | -2.0% (-4.3 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 393, 377 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.8 | -0.2% (-0.6 to +0.2) | -0.1% (-0.7 to +0.6) | -1.6% (-8.7 to +5.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 172.8 | 172.8 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,403 | 2,450 | +1.9% (-10.6 to +14.5) | +1.0% (-8.2 to +10.2) | +57.7% (-186.1 to +301.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,767 | 3,826 | +1.6% (-6.8 to +9.9) | -1.1% (-11.6 to +9.4) | +45.1% (-139.9 to +230.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% (-0.6 to +0.6) | +0.2% (-0.4 to +0.8) | -0.3% (-1.4 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 324.8 | 331.4 | +2.0% (-1.3 to +5.4) | +0.5% (-8.4 to +9.3) | +54.9% (-173.5 to +283.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 693.3 | 691.3 | -0.3% (-7.3 to +6.7) | -0.3% (-10.2 to +9.5) | +35.1% (-103.3 to +173.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 59.6 | 60.6 | +1.7% (-4.9 to +8.3) | +0.4% (-7.6 to +8.4) | +50.5% (-160.2 to +261.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | +9.5% (-16.5 to +35.5) | EVEN, no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +50.0% (+50.0 to +50.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.283 | 0.284 | +0.1% (-3.0 to +3.1) | +0.2% (-1.5 to +1.9) | -1.1% (-1.5 to -0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 508.4 | 508.7 | +0.0% (-3.0 to +3.1) | +0.2% (-1.5 to +1.9) | -1.1% (-1.6 to -0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 7.69 | +0.2% (-2.5 to +3.0) | +0.3% (-0.7 to +1.3) | +0.6% (-7.3 to +8.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +266.7% (+123.2 to +410.1) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,933, 1,940, 1,953 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.5 | 724.5 | -0.3% (-0.5 to -0.1) | +0.1% (-0.2 to +0.4) | -0.0% (-1.1 to +1.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (messages a second consumed) | 850.3 | 850.3 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,329 | 2,315 | -0.6% (-13.4 to +12.2) | -3.5% (-10.7 to +3.8) | -2.2% (-14.1 to +9.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,574 | 3,725 | +4.2% (+2.0 to +6.5) | -1.6% (-11.8 to +8.6) | -2.8% (-12.6 to +7.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, median (ms) | 8.38 | 7.94 | -5.2% (-11.1 to +0.6) | -0.5% (-7.6 to +6.6) | +11.5% (-80.3 to +103.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 312.6 | 315.7 | +1.0% (-3.7 to +5.6) | -2.3% (-8.4 to +3.7) | -1.6% (-11.8 to +8.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 3,227 | 3,270 | +1.3% (-2.6 to +5.2) | -2.4% (-5.8 to +1.0) | -1.8% (-11.6 to +8.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 271.9 | 274.4 | +0.9% (-4.0 to +5.8) | -2.5% (-8.6 to +3.6) | -1.7% (-11.5 to +8.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +6.0% (-21.2 to +33.1) | +6.0% (-21.2 to +33.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.326 | 0.325 | -0.2% (-3.0 to +2.6) | -0.5% (-2.8 to +1.7) | -0.6% (-3.5 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 559.1 | 559.2 | +0.0% (-3.3 to +3.4) | -0.6% (-3.3 to +2.1) | -0.7% (-3.7 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | +0.3% (-3.1 to +3.8) | -0.6% (-3.5 to +2.2) | -0.6% (-4.4 to +3.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +133.3% (-10.1 to +276.8) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 1 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 41 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
