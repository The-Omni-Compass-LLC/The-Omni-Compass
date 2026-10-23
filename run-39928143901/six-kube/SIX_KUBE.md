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
| response time (ms), 95th percentile | 2160 | 2769 | 1930 | 1998 | 2296 | 2241 | 2269 | 2744 | 3169 | 3866 | 3149 | 1801 | 2166 | 2277 |
| response time (ms), 99th percentile | 4474 | 5510 | 4242 | 4568 | 5452 | 5407 | 4946 | 5311 | 5687 | 6373 | 5088 | 4073 | 4471 | 4316 |
| time over the response line (% of samples) | 43.3 | 41.49 | 41.29 | 38.12 | 43.04 | 41.99 | 44.5 | 41.91 | 54.46 | 50.39 | 46.97 | 43.07 | 37.03 | 36.91 |
| failed requests (%) | 30.14 | 31.02 | 24.4 | 26.32 | 29.97 | 32.08 | 30.23 | 31.49 | 34.81 | 36.44 | 33.41 | 36.43 | 19.46 | 21.64 |
| HPA replicas, mean | 9.636 | 14.52 | 9.673 | 13.19 | 9.661 | 14.34 | 9.654 | 14.35 | 9.668 | 13.32 | 9.683 | 13.19 | 9.694 | 12.7 |
| pods started | 5.114 | 10.77 | 4.743 | 10 | 4.657 | 10.66 | 4.829 | 10.71 | 5.057 | 10.63 | 4.629 | 9.514 | 4.543 | 9.4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184 | 183.9 | 183.8 | 184.2 | 183.5 | 184.3 | 184.3 | 185 | 185.1 | 184 | 183.5 | 184 | 183.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184 | 183.9 | 183.8 | 184.2 | 183.4 | 184.3 | 184.3 | 185 | 185.1 | 184 | 183.5 | 184 | 183.8 |
| CPU used with Omni's own (cores), mean | 2.362 | 2.407 | 2.332 | 2.381 | 2.348 | 2.39 | 2.372 | 2.414 | 2.462 | 2.505 | 2.306 | 2.342 | 2.305 | 2.359 |
| host CPU busy, the real machine under kind (%) | 69.97 | 71.74 | 68.63 | 70.86 | 70.77 | 72.56 | 70.43 | 72.13 | 72.36 | 74.42 | 69.14 | 71.54 | 69.15 | 73.23 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02 | 0.01143 | 0.008571 | 0.6714 | 0 | 0.01143 | 0.008571 | 0.01143 | 0.09143 | 0.2114 | 0.1457 | 0.1743 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2160 | 2769 | +28.2% | +24.85 to +1192 | LOSS |
| response time (ms), 99th percentile | 4474 | 5510 | +23.2% | +255.9 to +1816 | LOSS |
| time over the response line (% of samples) | 43.3 | 41.49 | -4.2% | -3.004 to -0.6098 | GAIN |
| failed requests (%) | 30.14 | 31.02 | +2.9% | -0.09939 to +1.858 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.636 | 14.52 | +50.7% | +4.625 to +5.148 | power given |
| pods started | 5.114 | 10.77 | +110.6% | +5.225 to +6.09 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.807e-17 to +6.164e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184 | -0.1% | -0.5897 to +0.2837 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184 | -0.1% | -0.5897 to +0.2837 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.362 | 2.407 | +1.9% | +0.03702 to +0.05253 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.97 | 71.74 | +2.5% | +1.607 to +1.927 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1930 | 1998 | +3.6% | -291.4 to +428.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4242 | 4568 | +7.7% | -365.6 to +1018 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.29 | 38.12 | -7.7% | -4.6 to -1.731 | GAIN |
| failed requests (%) | 24.4 | 26.32 | +7.9% | +1.149 to +2.695 | LOSS |
| HPA replicas, mean | 9.673 | 13.19 | +36.4% | +3.16 to +3.877 | power given |
| pods started | 4.743 | 10 | +110.8% | +4.678 to +5.836 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.818e-16 to +3.803e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.8 | -0.0% | -0.4837 to +0.3251 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.8 | -0.0% | -0.4837 to +0.3251 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.381 | +2.1% | +0.03812 to +0.06053 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.63 | 70.86 | +3.3% | +1.902 to +2.57 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.01143 | -42.9% | -0.02599 to +0.008846 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2296 | 2241 | -2.4% | -536.6 to +426.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5452 | 5407 | -0.8% | -724.8 to +635.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 43.04 | 41.99 | -2.4% | -2.258 to +0.1544 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.97 | 32.08 | +7.0% | +1.032 to +3.192 | LOSS |
| HPA replicas, mean | 9.661 | 14.34 | +48.4% | +4.434 to +4.923 | power given |
| pods started | 4.657 | 10.66 | +128.8% | +5.544 to +6.456 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.006424 to +0.002186 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 183.5 | -0.4% | -2.217 to +0.771 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 183.4 | -0.4% | -2.256 to +0.7244 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.348 | 2.39 | +1.8% | +0.02326 to +0.06008 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.77 | 72.56 | +2.5% | +1.291 to +2.289 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.6714 | +7733.3% | -0.6722 to +1.998 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2269 | 2744 | +20.9% | -122.9 to +1072 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4946 | 5311 | +7.4% | -258.9 to +987.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 44.5 | 41.91 | -5.8% | -3.723 to -1.451 | GAIN |
| failed requests (%) | 30.23 | 31.49 | +4.2% | +0.2315 to +2.284 | LOSS |
| HPA replicas, mean | 9.654 | 14.35 | +48.6% | +4.439 to +4.946 | power given |
| pods started | 4.829 | 10.71 | +121.9% | +5.374 to +6.398 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.473e-16 to +4.488e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.3 | -0.0% | -0.4664 to +0.4408 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.3 | -0.0% | -0.4664 to +0.4408 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.372 | 2.414 | +1.8% | +0.03402 to +0.04913 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.43 | 72.13 | +2.4% | +1.495 to +1.919 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01143 | +0.0114 | +0.0003412 to +0.02252 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3169 | 3866 | +22.0% | +55.59 to +1337 | LOSS |
| response time (ms), 99th percentile | 5687 | 6373 | +12.1% | +67 to +1306 | LOSS |
| time over the response line (% of samples) | 54.46 | 50.39 | -7.5% | -5.313 to -2.829 | GAIN |
| failed requests (%) | 34.81 | 36.44 | +4.7% | +0.468 to +2.796 | LOSS |
| HPA replicas, mean | 9.668 | 13.32 | +37.7% | +3.283 to +4.016 | power given |
| pods started | 5.057 | 10.63 | +110.2% | +5.098 to +6.045 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.683e-16 to +3.176e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185.1 | +0.0% | -0.4795 to +0.6465 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185.1 | +0.0% | -0.4795 to +0.6465 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.462 | 2.505 | +1.7% | +0.03631 to +0.0495 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.36 | 74.42 | +2.9% | +1.881 to +2.249 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.008571 | 0.01143 | +33.3% | -0.0127 to +0.01841 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 6 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3149 | 1801 | -42.8% | -2072 to -624.4 | GAIN |
| response time (ms), 99th percentile | 5088 | 4073 | -19.9% | -1843 to -186.9 | GAIN |
| time over the response line (% of samples) | 46.97 | 43.07 | -8.3% | -5.679 to -2.114 | GAIN |
| failed requests (%) | 33.41 | 36.43 | +9.1% | +1.494 to +4.56 | LOSS |
| HPA replicas, mean | 9.683 | 13.19 | +36.2% | +3.096 to +3.912 | power given |
| pods started | 4.629 | 9.514 | +105.6% | +4.142 to +5.63 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.927e-16 to +3.435e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.5 | -0.3% | -0.925 to -0.06127 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.5 | -0.3% | -0.925 to -0.06127 | GAIN |
| CPU used with Omni's own (cores), mean | 2.306 | 2.342 | +1.5% | +0.02304 to +0.0484 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.14 | 71.54 | +3.5% | +2.126 to +2.672 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.09143 | 0.2114 | +131.3% | +0.1017 to +0.1383 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2166 | 2277 | +5.1% | -180.5 to +401.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4471 | 4316 | -3.5% | -909.3 to +598.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 37.03 | 36.91 | -0.3% | -1.767 to +1.533 | EVEN, inside the noise (cut) |
| failed requests (%) | 19.46 | 21.64 | +11.2% | +1.306 to +3.043 | LOSS |
| HPA replicas, mean | 9.694 | 12.7 | +31.0% | +2.209 to +3.804 | power given |
| pods started | 4.543 | 9.4 | +106.9% | +4.024 to +5.691 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.155e-16 to +5.186e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.8 | -0.1% | -0.61 to +0.2555 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.8 | -0.1% | -0.61 to +0.2555 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.305 | 2.359 | +2.4% | +0.04433 to +0.06466 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.15 | 73.23 | +5.9% | +3.788 to +4.385 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1457 | 0.1743 | +19.6% | -0.002117 to +0.05926 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
