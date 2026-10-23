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
| response time (ms), 95th percentile | 1934 | 2547 | 2561 | 2310 | 2530 | 2762 | 2506 | 2141 | 2839 | 3918 | 3327 | 2795 | 2700 | 2978 |
| response time (ms), 99th percentile | 4601 | 5105 | 5021 | 4912 | 5816 | 6128 | 4695 | 4043 | 5321 | 6288 | 5387 | 5119 | 5339 | 5492 |
| time over the response line (% of samples) | 41.97 | 40.66 | 40.82 | 36.32 | 49.69 | 47.46 | 36.19 | 33.92 | 48.23 | 44.73 | 52.42 | 49.68 | 47.28 | 46.76 |
| failed requests (%) | 28.94 | 30.41 | 21.21 | 22.22 | 34.54 | 36.69 | 24.79 | 25.82 | 29.74 | 29.96 | 36.24 | 40.15 | 26.23 | 28.33 |
| HPA replicas, mean | 9.641 | 14.6 | 9.628 | 13.66 | 9.7 | 14.72 | 9.623 | 14.48 | 9.669 | 13.66 | 9.717 | 12.71 | 9.726 | 11.52 |
| pods started | 5.15 | 11.1 | 5.45 | 10.2 | 4.3 | 9.85 | 5 | 10.6 | 5.05 | 10.65 | 4.1 | 9.25 | 4.15 | 8.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.8 | 184 | 183.6 | 184.9 | 184.3 | 183.2 | 183.8 | 185 | 184.9 | 184.7 | 184.1 | 185.2 | 185.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.8 | 184 | 183.6 | 184.9 | 184.3 | 183.2 | 183.8 | 185 | 184.9 | 184.7 | 184.1 | 185.2 | 185.1 |
| CPU used with Omni's own (cores), mean | 2.343 | 2.391 | 2.341 | 2.386 | 2.435 | 2.458 | 2.278 | 2.317 | 2.426 | 2.468 | 2.372 | 2.412 | 2.437 | 2.486 |
| host CPU busy, the real machine under kind (%) | 69.27 | 71.23 | 68.47 | 70.6 | 72.49 | 74.2 | 67.43 | 69.05 | 71 | 72.95 | 70.7 | 73.22 | 73.13 | 77.03 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.015 | 1.38 | 0 | 0.01 | 0 | 0.01 | 0.01 | 0.015 | 0.105 | 0.23 | 0.18 | 0.195 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1934 | 2547 | +31.7% | +15.17 to +1211 | LOSS |
| response time (ms), 99th percentile | 4601 | 5105 | +11.0% | -759.4 to +1769 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.97 | 40.66 | -3.1% | -2.753 to +0.1316 | EVEN, inside the noise (cut) |
| failed requests (%) | 28.94 | 30.41 | +5.1% | +0.2055 to +2.748 | LOSS |
| HPA replicas, mean | 9.641 | 14.6 | +51.4% | +4.637 to +5.274 | power given |
| pods started | 5.15 | 11.1 | +115.5% | +5.315 to +6.585 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.905e-16 to +2.576e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.8 | +0.0% | -0.5189 to +0.5998 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.8 | +0.0% | -0.5189 to +0.5998 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.343 | 2.391 | +2.1% | +0.04233 to +0.05391 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.27 | 71.23 | +2.8% | +1.704 to +2.219 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2561 | 2310 | -9.8% | -588 to +84.63 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5021 | 4912 | -2.2% | -901.8 to +682.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 40.82 | 36.32 | -11.0% | -6.362 to -2.632 | GAIN |
| failed requests (%) | 21.21 | 22.22 | +4.8% | -0.1629 to +2.185 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.628 | 13.66 | +41.9% | +3.437 to +4.633 | power given |
| pods started | 5.45 | 10.2 | +87.2% | +4.108 to +5.392 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.324e-15 to +8.034e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.6 | -0.2% | -1.408 to +0.6896 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.6 | -0.2% | -1.408 to +0.6896 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.341 | 2.386 | +1.9% | +0.03583 to +0.05351 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.47 | 70.6 | +3.1% | +1.962 to +2.31 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.015 | 1.38 | +9100.0% | -1.514 to +4.244 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2530 | 2762 | +9.2% | -463.3 to +927 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5816 | 6128 | +5.4% | -301.9 to +926.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 49.69 | 47.46 | -4.5% | -3.822 to -0.6497 | GAIN |
| failed requests (%) | 34.54 | 36.69 | +6.2% | +1.001 to +3.296 | LOSS |
| HPA replicas, mean | 9.7 | 14.72 | +51.8% | +4.675 to +5.371 | power given |
| pods started | 4.3 | 9.85 | +129.1% | +4.846 to +6.254 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.546e-16 to +2.217e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.3 | -0.3% | -1.308 to +0.09686 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.3 | -0.3% | -1.308 to +0.09686 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.435 | 2.458 | +0.9% | -0.008895 to +0.05483 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.49 | 74.2 | +2.4% | +1.434 to +1.99 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.004405 to +0.02441 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2506 | 2141 | -14.6% | -1090 to +360.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4695 | 4043 | -13.9% | -1588 to +284.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 36.19 | 33.92 | -6.3% | -3.583 to -0.953 | GAIN |
| failed requests (%) | 24.79 | 25.82 | +4.2% | -0.2284 to +2.292 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.623 | 14.48 | +50.5% | +4.528 to +5.19 | power given |
| pods started | 5 | 10.6 | +112.0% | +5.044 to +6.156 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.861e-16 to +3.196e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.8 | +0.3% | +0.02306 to +1.059 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.8 | +0.3% | +0.02306 to +1.059 | power given |
| CPU used with Omni's own (cores), mean | 2.278 | 2.317 | +1.7% | +0.02667 to +0.05142 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.43 | 69.05 | +2.4% | +1.295 to +1.961 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.004405 to +0.02441 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2839 | 3918 | +38.0% | +239.8 to +1919 | LOSS |
| response time (ms), 99th percentile | 5321 | 6288 | +18.2% | -101.5 to +2037 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 48.23 | 44.73 | -7.2% | -5.023 to -1.968 | GAIN |
| failed requests (%) | 29.74 | 29.96 | +0.7% | -1.537 to +1.965 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.669 | 13.66 | +41.2% | +3.531 to +4.443 | power given |
| pods started | 5.05 | 10.65 | +110.9% | +4.931 to +6.269 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.803e-16 to +7.244e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.9 | -0.0% | -0.7487 to +0.6021 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.9 | -0.0% | -0.7487 to +0.6021 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.468 | +1.7% | +0.02035 to +0.06303 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71 | 72.95 | +2.7% | +1.346 to +2.545 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01 | 0.015 | +50.0% | -0.01344 to +0.02344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3327 | 2795 | -16.0% | -1440 to +377.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5387 | 5119 | -5.0% | -1087 to +550.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 52.42 | 49.68 | -5.2% | -5.016 to -0.4749 | GAIN |
| failed requests (%) | 36.24 | 40.15 | +10.8% | +2.329 to +5.493 | LOSS |
| HPA replicas, mean | 9.717 | 12.71 | +30.8% | +2.391 to +3.601 | power given |
| pods started | 4.1 | 9.25 | +125.6% | +4.315 to +5.985 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.007629 to +0.002696 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.1 | -0.3% | -1.013 to -0.05781 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.1 | -0.3% | -1.056 to -0.115 | GAIN |
| CPU used with Omni's own (cores), mean | 2.372 | 2.412 | +1.7% | +0.02504 to +0.05385 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.7 | 73.22 | +3.6% | +2.165 to +2.882 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.105 | 0.23 | +119.0% | +0.09511 to +0.1549 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2700 | 2978 | +10.3% | -316.6 to +873.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5339 | 5492 | +2.9% | -607.6 to +914.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 47.28 | 46.76 | -1.1% | -2.915 to +1.864 | EVEN, inside the noise (cut) |
| failed requests (%) | 26.23 | 28.33 | +8.0% | +0.6688 to +3.539 | LOSS |
| HPA replicas, mean | 9.726 | 11.52 | +18.4% | +0.7104 to +2.876 | power given |
| pods started | 4.15 | 8.8 | +112.0% | +3.359 to +5.941 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.595e-16 to +3.707e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 185.1 | -0.0% | -0.7826 to +0.6759 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 185.1 | -0.0% | -0.7826 to +0.6759 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.437 | 2.486 | +2.0% | +0.04037 to +0.05767 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.13 | 77.03 | +5.3% | +3.693 to +4.112 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.18 | 0.195 | +8.3% | -0.03367 to +0.06367 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
