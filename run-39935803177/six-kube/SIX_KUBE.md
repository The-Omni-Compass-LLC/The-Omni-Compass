# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2231 | 1987 | 2381 | 1982 | 2100 | 2478 | 1939 | 2108 | 2260 | 2645 | 3394 | 2145 | 2422 | 2861 |
| response time (ms), 99th percentile | 4520 | 4361 | 4648 | 4397 | 4573 | 5213 | 4106 | 4417 | 4201 | 4570 | 5832 | 4841 | 5200 | 4743 |
| time over the response line (% of samples) | 36.02 | 34.48 | 41.51 | 38.16 | 43.27 | 41.01 | 39.49 | 37.81 | 36.21 | 33.67 | 56.93 | 52.03 | 40.67 | 40.63 |
| failed requests (%) | 24.39 | 26.03 | 23.11 | 25.44 | 30.09 | 31.42 | 27.74 | 29.38 | 21.52 | 22.66 | 40.22 | 43.57 | 20.8 | 22.46 |
| HPA replicas, mean | 9.599 | 14.5 | 9.661 | 13.15 | 9.641 | 14.4 | 9.63 | 14.33 | 9.619 | 13.7 | 9.712 | 12.98 | 9.678 | 12.33 |
| pods started | 5.514 | 11.17 | 4.943 | 10.03 | 4.914 | 10.6 | 4.943 | 10.34 | 5.514 | 11.2 | 4.314 | 9.086 | 4.743 | 9.371 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | 183.9 | 183.6 | 183.9 | 183.9 | 183.3 | 182.8 | 183.1 | 183.2 | 185 | 184.9 | 184.2 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | 183.9 | 183.6 | 183.9 | 183.9 | 183.3 | 182.8 | 183.1 | 183.2 | 185 | 184.9 | 184.2 | 184.5 |
| CPU used with Omni's own (cores), mean | 2.275 | 2.326 | 2.329 | 2.365 | 2.338 | 2.382 | 2.259 | 2.305 | 2.266 | 2.309 | 2.447 | 2.49 | 2.345 | 2.398 |
| host CPU busy, the real machine under kind (%) | 67.12 | 68.97 | 68.38 | 70.3 | 69.46 | 71.28 | 67.39 | 69.2 | 66.44 | 68.41 | 73.12 | 75.82 | 70.05 | 74.14 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.01143 | 0.01143 | 0.002857 | 0.008571 | 0.01143 | 0.008571 | 0.005714 | 0.01714 | 0.09429 | 0.22 | 0.14 | 0.1686 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2231 | 1987 | -10.9% | -647.6 to +159.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4520 | 4361 | -3.5% | -849.1 to +532 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 36.02 | 34.48 | -4.3% | -2.298 to -0.7836 | GAIN |
| failed requests (%) | 24.39 | 26.03 | +6.7% | +0.5703 to +2.696 | LOSS |
| HPA replicas, mean | 9.599 | 14.5 | +51.0% | +4.687 to +5.11 | power given |
| pods started | 5.514 | 11.17 | +102.6% | +5.099 to +6.216 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.063e-16 to +5.108e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | -0.0% | -0.5143 to +0.43 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | -0.0% | -0.5143 to +0.43 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.326 | +2.2% | +0.03902 to +0.06318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.12 | 68.97 | +2.8% | +1.502 to +2.196 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2381 | 1982 | -16.8% | -746.8 to -51.95 | GAIN |
| response time (ms), 99th percentile | 4648 | 4397 | -5.4% | -907.5 to +406.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.51 | 38.16 | -8.1% | -4.993 to -1.72 | GAIN |
| failed requests (%) | 23.11 | 25.44 | +10.1% | +1.208 to +3.451 | LOSS |
| HPA replicas, mean | 9.661 | 13.15 | +36.1% | +3.112 to +3.858 | power given |
| pods started | 4.943 | 10.03 | +102.9% | +4.46 to +5.711 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.357e-16 to +7.594e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.6 | -0.2% | -0.8145 to +0.1102 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.6 | -0.2% | -0.8145 to +0.1102 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.329 | 2.365 | +1.5% | +0.02717 to +0.04429 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.38 | 70.3 | +2.8% | +1.669 to +2.16 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01143 | 0.01143 | +0.0% | -0.01666 to +0.01666 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2100 | 2478 | +18.0% | -160.3 to +916.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4573 | 5213 | +14.0% | -227.7 to +1509 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.27 | 41.01 | -5.2% | -3.497 to -1.02 | GAIN |
| failed requests (%) | 30.09 | 31.42 | +4.4% | +0.1118 to +2.551 | LOSS |
| HPA replicas, mean | 9.641 | 14.4 | +49.4% | +4.452 to +5.068 | power given |
| pods started | 4.914 | 10.6 | +115.7% | +5.02 to +6.351 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.139e-16 to +5.184e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.9 | -0.0% | -0.4356 to +0.4235 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.9 | -0.0% | -0.4356 to +0.4235 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.338 | 2.382 | +1.8% | +0.03257 to +0.05394 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.46 | 71.28 | +2.6% | +1.536 to +2.111 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 3 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1939 | 2108 | +8.7% | -386.9 to +723.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4106 | 4417 | +7.6% | -607.6 to +1230 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 39.49 | 37.81 | -4.3% | -2.588 to -0.7839 | GAIN |
| failed requests (%) | 27.74 | 29.38 | +5.9% | +0.7348 to +2.54 | LOSS |
| HPA replicas, mean | 9.63 | 14.33 | +48.8% | +4.402 to +4.995 | power given |
| pods started | 4.943 | 10.34 | +109.2% | +4.828 to +5.972 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.001576 to +0.00463 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.8 | -0.3% | -0.9395 to -0.02508 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.8 | -0.2% | -0.9092 to +0.006541 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.259 | 2.305 | +2.0% | +0.03781 to +0.05473 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.39 | 69.2 | +2.7% | +1.608 to +2.024 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.01143 | 0.008571 | -25.0% | -0.01599 to +0.01028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2260 | 2645 | +17.0% | +10.21 to +759.5 | LOSS |
| response time (ms), 99th percentile | 4201 | 4570 | +8.8% | -113.9 to +851.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 36.21 | 33.67 | -7.0% | -4.622 to -0.4565 | GAIN |
| failed requests (%) | 21.52 | 22.66 | +5.3% | -0.1794 to +2.476 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.619 | 13.7 | +42.5% | +3.7 to +4.47 | power given |
| pods started | 5.514 | 11.2 | +103.1% | +5.181 to +6.191 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.771e-16 to +2.741e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 183.2 | +0.0% | -0.4368 to +0.4819 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 183.2 | +0.0% | -0.4368 to +0.4819 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.266 | 2.309 | +1.9% | +0.03334 to +0.05301 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.44 | 68.41 | +3.0% | +1.742 to +2.186 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01714 | +200.0% | -0.004749 to +0.02761 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3394 | 2145 | -36.8% | -1887 to -610.1 | GAIN |
| response time (ms), 99th percentile | 5832 | 4841 | -17.0% | -1711 to -270.1 | GAIN |
| time over the response line (% of samples) | 56.93 | 52.03 | -8.6% | -6.156 to -3.651 | GAIN |
| failed requests (%) | 40.22 | 43.57 | +8.3% | +2.102 to +4.598 | LOSS |
| HPA replicas, mean | 9.712 | 12.98 | +33.7% | +2.963 to +3.576 | power given |
| pods started | 4.314 | 9.086 | +110.6% | +4.115 to +5.428 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001342 to +0.003942 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.9 | -0.1% | -0.5685 to +0.3794 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.9 | -0.0% | -0.5568 to +0.4201 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.49 | +1.8% | +0.0337 to +0.05332 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.12 | 75.82 | +3.7% | +2.417 to +2.987 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.09429 | 0.22 | +133.3% | +0.1031 to +0.1483 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2422 | 2861 | +18.1% | +85.91 to +793 | LOSS |
| response time (ms), 99th percentile | 5200 | 4743 | -8.8% | -973.1 to +59.17 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 40.67 | 40.63 | -0.1% | -1.72 to +1.634 | EVEN, inside the noise (cut) |
| failed requests (%) | 20.8 | 22.46 | +8.0% | +0.7285 to +2.596 | LOSS |
| HPA replicas, mean | 9.678 | 12.33 | +27.4% | +1.826 to +3.48 | power given |
| pods started | 4.743 | 9.371 | +97.6% | +3.856 to +5.401 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.252e-17 to +6.173e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | +0.1% | -0.1526 to +0.6805 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | +0.1% | -0.1526 to +0.6805 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.345 | 2.398 | +2.3% | +0.04437 to +0.0625 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.05 | 74.14 | +5.8% | +3.825 to +4.339 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.14 | 0.1686 | +20.4% | +0.005649 to +0.05149 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
