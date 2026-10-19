# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2722 | 2502 | 2774 | 3726 | 1708 | 1699 | 2497 | 2572 | 2092 | 2949 | 3048 | 3369 | 1467 | 2158 |
| response time (ms), 99th percentile | 5461 | 5362 | 5310 | 7589 | 3224 | 3724 | 4729 | 5278 | 4997 | 4899 | 5632 | 6001 | 3800 | 4350 |
| time over the response line (% of samples) | 45.43 | 44.67 | 57.22 | 50.94 | 29.89 | 27.25 | 40.2 | 37.56 | 42.3 | 37.61 | 47.89 | 44.74 | 35.7 | 35.55 |
| failed requests (%) | 31.95 | 33.48 | 34.84 | 33.76 | 20.12 | 21.47 | 28.18 | 27.92 | 24.74 | 23.99 | 32.58 | 33.61 | 19.9 | 21.27 |
| HPA replicas, mean | 9.647 | 13.63 | 9.718 | 14.06 | 9.56 | 11.99 | 9.644 | 12.23 | 9.604 | 13.16 | 9.734 | 13.41 | 9.633 | 12.35 |
| pods started | 5.1 | 9.7 | 4.1 | 7.9 | 5.6 | 7.9 | 4.8 | 7.7 | 5.7 | 8.8 | 3.7 | 7.8 | 5.4 | 7.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.5 | 185.6 | 185.3 | 182 | 181.7 | 183.2 | 183.4 | 183.5 | 184.1 | 184.3 | 184.2 | 183.5 | 183.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.5 | 185.6 | 185.3 | 182 | 181.7 | 183.2 | 183.4 | 183.5 | 184.1 | 184.3 | 184.2 | 183.5 | 183.2 |
| CPU used with Omni's own (cores), mean | 2.408 | 2.441 | 2.494 | 2.522 | 2.131 | 2.125 | 2.286 | 2.301 | 2.294 | 2.322 | 2.367 | 2.396 | 2.269 | 2.302 |
| host CPU busy, the real machine under kind (%) | 71.5 | 72.56 | 73.84 | 75.28 | 63.68 | 63.83 | 68.19 | 69.2 | 67.24 | 68.51 | 71.19 | 73.08 | 68.43 | 71.91 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02 | 0 | 0 | 0.01 | 0.01 | 0.02 | 0 | 0.05 | 0.09 | 0.24 | 0.13 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2722 | 2502 | -8.1% | -1586 to +1146 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5461 | 5362 | -1.8% | -1277 to +1081 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 45.43 | 44.67 | -1.7% | -4.256 to +2.75 | EVEN, inside the noise (cut) |
| failed requests (%) | 31.95 | 33.48 | +4.8% | -0.368 to +3.427 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.647 | 13.63 | +41.3% | +2.412 to +5.554 | power given |
| pods started | 5.1 | 9.7 | +90.2% | +2.976 to +6.224 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.788e-16 to +3.235e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.5 | +0.1% | -0.7262 to +0.9253 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.5 | +0.1% | -0.7262 to +0.9253 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.441 | +1.4% | +0.01764 to +0.04846 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.5 | 72.56 | +1.5% | +0.8423 to +1.281 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2774 | 3726 | +34.3% | -166.4 to +2070 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5310 | 7589 | +42.9% | +1180 to +3379 | LOSS |
| time over the response line (% of samples) | 57.22 | 50.94 | -11.0% | -10.58 to -1.994 | GAIN |
| failed requests (%) | 34.84 | 33.76 | -3.1% | -3.383 to +1.213 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.718 | 14.06 | +44.7% | +3.234 to +5.445 | power given |
| pods started | 4.1 | 7.9 | +92.7% | +1.898 to +5.702 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.3 | -0.2% | -1.232 to +0.5841 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185.3 | -0.2% | -1.232 to +0.5841 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.494 | 2.522 | +1.1% | +0.008082 to +0.04727 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.84 | 75.28 | +1.9% | +1.067 to +1.81 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.05016 to +0.01016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1708 | 1699 | -0.6% | -648.2 to +628.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3224 | 3724 | +15.5% | -244.9 to +1246 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.89 | 27.25 | -8.8% | -5.001 to -0.269 | GAIN |
| failed requests (%) | 20.12 | 21.47 | +6.7% | -0.422 to +3.125 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.56 | 11.99 | +25.4% | +0.4822 to +4.383 | power given |
| pods started | 5.6 | 7.9 | +41.1% | +0.5462 to +4.054 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.7 | -0.2% | -1.109 to +0.4989 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.7 | -0.2% | -1.109 to +0.4989 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.131 | 2.125 | -0.2% | -0.04144 to +0.03099 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.68 | 63.83 | +0.2% | -1.046 to +1.349 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2497 | 2572 | +3.0% | -419.8 to +571.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4729 | 5278 | +11.6% | -570 to +1668 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.2 | 37.56 | -6.6% | -5.487 to +0.2179 | EVEN, inside the noise (cut) |
| failed requests (%) | 28.18 | 27.92 | -0.9% | -2.436 to +1.93 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 12.23 | +26.8% | +0.5991 to +4.567 | power given |
| pods started | 4.8 | 7.7 | +60.4% | +0.7554 to +5.045 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.4 | +0.2% | -0.4603 to +1.027 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.4 | +0.2% | -0.4603 to +1.027 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.286 | 2.301 | +0.6% | -0.01253 to +0.04198 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.19 | 69.2 | +1.5% | +0.4467 to +1.562 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.0306 to +0.0506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2092 | 2949 | +40.9% | -4.729 to +1717 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4997 | 4899 | -2.0% | -1431 to +1235 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 42.3 | 37.61 | -11.1% | -8.301 to -1.076 | GAIN |
| failed requests (%) | 24.74 | 23.99 | -3.0% | -3.639 to +2.131 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 13.16 | +37.0% | +1.726 to +5.381 | power given |
| pods started | 5.7 | 8.8 | +54.4% | +1.433 to +4.767 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.012e-16 to +1.312e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.1 | +0.3% | -0.4977 to +1.708 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.1 | +0.3% | -0.4977 to +1.708 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.294 | 2.322 | +1.2% | +0.01814 to +0.03873 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.24 | 68.51 | +1.9% | +0.985 to +1.559 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0.05 | +0.05 | +0.0123 to +0.0877 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3048 | 3369 | +10.5% | -838.8 to +1481 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5632 | 6001 | +6.6% | -265.3 to +1004 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 47.89 | 44.74 | -6.6% | -5.741 to -0.5571 | GAIN |
| failed requests (%) | 32.58 | 33.61 | +3.2% | -0.2081 to +2.266 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.734 | 13.41 | +37.8% | +2.257 to +5.1 | power given |
| pods started | 3.7 | 7.8 | +110.8% | +2.239 to +5.961 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.318e-16 to +1.009e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.2 | -0.0% | -0.6902 to +0.5345 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.2 | -0.0% | -0.6902 to +0.5345 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.396 | +1.2% | +0.009802 to +0.04827 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.19 | 73.08 | +2.7% | +1.395 to +2.383 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.09 | 0.24 | +166.7% | +0.09942 to +0.2006 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1467 | 2158 | +47.1% | +0.1765 to +1383 | LOSS |
| response time (ms), 99th percentile | 3800 | 4350 | +14.5% | -1464 to +2563 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 35.7 | 35.55 | -0.4% | -3.398 to +3.105 | EVEN, inside the noise (cut) |
| failed requests (%) | 19.9 | 21.27 | +6.9% | -0.02038 to +2.752 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.633 | 12.35 | +28.2% | +1.344 to +4.081 | power given |
| pods started | 5.4 | 7.8 | +44.4% | +0.7073 to +4.093 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.571e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.2 | -0.2% | -1.387 to +0.8204 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.2 | -0.2% | -1.387 to +0.8204 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.269 | 2.302 | +1.5% | +0.01292 to +0.05317 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.43 | 71.91 | +5.1% | +2.919 to +4.032 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.13 | 0.2 | +53.8% | +0.03545 to +0.1046 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
