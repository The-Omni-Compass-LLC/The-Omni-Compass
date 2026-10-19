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
| response time (ms), 95th percentile | 2511 | 2847 | 2235 | 3229 | 2495 | 2522 | 2122 | 2599 | 2402 | 3047 | 3272 | 4111 | 2662 | 3518 |
| response time (ms), 99th percentile | 4938 | 5896 | 4385 | 5996 | 5448 | 5815 | 4489 | 5076 | 4589 | 4997 | 6040 | 6457 | 5512 | 6728 |
| time over the response line (% of samples) | 46.26 | 42.62 | 44.9 | 41.83 | 43.49 | 40.23 | 40.64 | 36.81 | 45.73 | 42.4 | 55.88 | 53.13 | 58.58 | 56.49 |
| failed requests (%) | 31.36 | 31.14 | 26.12 | 25.31 | 29.58 | 29.31 | 27.17 | 26.78 | 29.56 | 28.57 | 40.52 | 40.25 | 33.5 | 35.61 |
| HPA replicas, mean | 9.637 | 13.41 | 9.68 | 13.25 | 9.624 | 12.45 | 9.624 | 12.96 | 9.638 | 13.23 | 9.728 | 13.41 | 9.733 | 13.19 |
| pods started | 5.2 | 9.114 | 4.914 | 9.171 | 5.143 | 8.257 | 5.143 | 8.486 | 5.314 | 9.343 | 4.029 | 7.8 | 4.114 | 6.743 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | 184.7 | 184.8 | 184.2 | 184.3 | 183.6 | 183.9 | 183.4 | 183.9 | 185.1 | 184.5 | 186.2 | 185.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | 184.7 | 184.8 | 184.2 | 184.3 | 183.5 | 183.9 | 183.4 | 183.9 | 185.1 | 184.5 | 186.2 | 185.9 |
| CPU used with Omni's own (cores), mean | 2.387 | 2.411 | 2.409 | 2.436 | 2.378 | 2.402 | 2.303 | 2.34 | 2.298 | 2.318 | 2.412 | 2.443 | 2.53 | 2.576 |
| host CPU busy, the real machine under kind (%) | 70.79 | 71.84 | 71.05 | 72.33 | 70.46 | 71.57 | 68.6 | 69.89 | 67.71 | 68.9 | 72.56 | 74.35 | 76.46 | 79.98 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.01143 | 0.02286 | 0.002857 | 0.005714 | 0 | 0.01714 | 0.005714 | 0.02286 | 0.1057 | 0.2171 | 0.1714 | 0.2086 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2511 | 2847 | +13.4% | -209.6 to +881.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4938 | 5896 | +19.4% | +145.8 to +1770 | LOSS |
| time over the response line (% of samples) | 46.26 | 42.62 | -7.9% | -4.912 to -2.376 | GAIN |
| failed requests (%) | 31.36 | 31.14 | -0.7% | -0.9291 to +0.4912 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.637 | 13.41 | +39.1% | +2.938 to +4.599 | power given |
| pods started | 5.2 | 9.114 | +75.3% | +2.997 to +4.832 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001523 to +0.0005184 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.0% | -0.5844 to +0.7133 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.0% | -0.6095 to +0.7181 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.387 | 2.411 | +1.0% | +0.008996 to +0.03896 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.79 | 71.84 | +1.5% | +0.903 to +1.208 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2235 | 3229 | +44.4% | +380.3 to +1606 | LOSS |
| response time (ms), 99th percentile | 4385 | 5996 | +36.7% | +899.6 to +2322 | LOSS |
| time over the response line (% of samples) | 44.9 | 41.83 | -6.8% | -4.64 to -1.502 | GAIN |
| failed requests (%) | 26.12 | 25.31 | -3.1% | -1.565 to -0.04569 | GAIN |
| HPA replicas, mean | 9.68 | 13.25 | +36.9% | +2.854 to +4.293 | power given |
| pods started | 4.914 | 9.171 | +86.6% | +3.263 to +5.251 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.117e-16 to +5.655e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.1% | -0.3804 to +0.6629 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.1% | -0.3804 to +0.6629 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.436 | +1.1% | +0.01729 to +0.03745 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.05 | 72.33 | +1.8% | +0.9949 to +1.565 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01143 | 0.02286 | +100.0% | -0.006768 to +0.02963 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2495 | 2522 | +1.1% | -413.9 to +469.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5448 | 5815 | +6.7% | -180 to +913.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.49 | 40.23 | -7.5% | -4.574 to -1.938 | GAIN |
| failed requests (%) | 29.58 | 29.31 | -0.9% | -1.318 to +0.7898 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.624 | 12.45 | +29.4% | +1.962 to +3.693 | power given |
| pods started | 5.143 | 8.257 | +60.6% | +2.045 to +4.184 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.053e-16 to +4.053e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.1% | -0.3379 to +0.5313 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.1% | -0.3379 to +0.5313 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.378 | 2.402 | +1.0% | +0.01468 to +0.03169 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.46 | 71.57 | +1.6% | +0.8647 to +1.352 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.005714 | +100.0% | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2122 | 2599 | +22.5% | -12.8 to +967.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4489 | 5076 | +13.1% | -132.9 to +1307 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.64 | 36.81 | -9.4% | -5.108 to -2.553 | GAIN |
| failed requests (%) | 27.17 | 26.78 | -1.5% | -1.091 to +0.2998 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.624 | 12.96 | +34.7% | +2.469 to +4.213 | power given |
| pods started | 5.143 | 8.486 | +65.0% | +2.386 to +4.3 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.0% | -0.0026 to +0.007638 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.9 | +0.2% | -0.2052 to +0.8215 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | -0.2004 to +0.9178 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.303 | 2.34 | +1.6% | +0.02128 to +0.05256 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.6 | 69.89 | +1.9% | +0.8213 to +1.747 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01714 | +0.0171 | +0.004009 to +0.03028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2402 | 3047 | +26.8% | +145 to +1145 | LOSS |
| response time (ms), 99th percentile | 4589 | 4997 | +8.9% | -73.63 to +889.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.73 | 42.4 | -7.3% | -4.742 to -1.911 | GAIN |
| failed requests (%) | 29.56 | 28.57 | -3.4% | -1.913 to -0.06771 | GAIN |
| HPA replicas, mean | 9.638 | 13.23 | +37.3% | +2.751 to +4.435 | power given |
| pods started | 5.314 | 9.343 | +75.8% | +3.11 to +4.947 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.728e-16 to +2.713e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.9 | +0.3% | -0.02267 to +0.9927 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.9 | +0.3% | -0.02267 to +0.9927 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.298 | 2.318 | +0.9% | +0.009852 to +0.02966 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.71 | 68.9 | +1.8% | +0.9186 to +1.461 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.02286 | +300.0% | +0.00159 to +0.0327 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3272 | 4111 | +25.6% | +262.5 to +1416 | LOSS |
| response time (ms), 99th percentile | 6040 | 6457 | +6.9% | -102.5 to +936.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.88 | 53.13 | -4.9% | -4.032 to -1.476 | GAIN |
| failed requests (%) | 40.52 | 40.25 | -0.7% | -1.166 to +0.6373 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.728 | 13.41 | +37.9% | +3.087 to +4.285 | power given |
| pods started | 4.029 | 7.8 | +93.6% | +2.917 to +4.625 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.139e-16 to +5.184e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.5 | -0.3% | -0.8548 to -0.2281 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.5 | -0.3% | -0.8548 to -0.2281 | GAIN |
| CPU used with Omni's own (cores), mean | 2.412 | 2.443 | +1.3% | +0.02213 to +0.03925 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.56 | 74.35 | +2.5% | +1.527 to +2.046 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1057 | 0.2171 | +105.4% | +0.08821 to +0.1347 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2662 | 3518 | +32.2% | +296.9 to +1415 | LOSS |
| response time (ms), 99th percentile | 5512 | 6728 | +22.1% | +490.4 to +1942 | LOSS |
| time over the response line (% of samples) | 58.58 | 56.49 | -3.6% | -3.755 to -0.4345 | GAIN |
| failed requests (%) | 33.5 | 35.61 | +6.3% | +0.8982 to +3.323 | LOSS |
| HPA replicas, mean | 9.733 | 13.19 | +35.5% | +3.046 to +3.867 | power given |
| pods started | 4.114 | 6.743 | +63.9% | +1.967 to +3.29 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.035e-16 to +3.513e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.2 | 185.9 | -0.2% | -0.6416 to +0.006779 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.2 | 185.9 | -0.2% | -0.6416 to +0.006779 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.53 | 2.576 | +1.8% | +0.0396 to +0.05353 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.46 | 79.98 | +4.6% | +3.311 to +3.727 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1714 | 0.2086 | +21.7% | +0.009407 to +0.06488 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
