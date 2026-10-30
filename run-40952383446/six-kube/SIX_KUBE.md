# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2459 | 2471 | 2154 | 3069 | 2173 | 2236 | 2122 | 2562 | 2079 | 2816 | 3295 | 4445 | 1949 | 3442 |
| response time (ms), 99th percentile | 5116 | 5715 | 4802 | 5996 | 4617 | 4804 | 4575 | 5184 | 4288 | 5038 | 5761 | 6607 | 4074 | 5110 |
| time over the response line (% of samples) | 43.66 | 39.24 | 47.13 | 42.96 | 39.56 | 35.62 | 47.81 | 42.85 | 40.28 | 36.82 | 52.82 | 49.41 | 35.28 | 34.05 |
| failed requests (%) | 28.73 | 28.34 | 27.25 | 25.25 | 26.74 | 25.95 | 32.36 | 30.67 | 24.38 | 22.54 | 33.8 | 31.05 | 17.94 | 17.43 |
| HPA replicas, mean | 9.652 | 12.31 | 9.702 | 13.93 | 9.634 | 11.71 | 9.695 | 12.39 | 9.664 | 12.85 | 9.719 | 12.98 | 9.656 | 11.86 |
| pods started | 4.853 | 7.529 | 4.486 | 8.914 | 4.829 | 7.314 | 4.2 | 7.333 | 4.714 | 8.629 | 3.971 | 7.647 | 4.943 | 6.771 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.6 | 184.6 | 185.3 | 183.4 | 183.8 | 184.3 | 184.6 | 182.9 | 183.7 | 184.6 | 185.3 | 182.9 | 183.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.6 | 184.6 | 185.3 | 183.4 | 183.8 | 184.3 | 184.6 | 182.9 | 183.7 | 184.6 | 185.3 | 182.9 | 183.3 |
| CPU used with Omni's own (cores), mean | 2.373 | 2.38 | 2.446 | 2.458 | 2.301 | 2.315 | 2.413 | 2.416 | 2.275 | 2.284 | 2.424 | 2.434 | 2.247 | 2.247 |
| host CPU busy, the real machine under kind (%) | 70.32 | 70.96 | 71.86 | 73.12 | 68.43 | 69.24 | 71.95 | 72.6 | 66.81 | 67.89 | 72.18 | 73.85 | 67.34 | 69.75 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002941 | 0.01429 | 0.01143 | 0.002857 | 0.01143 | 0.008571 | 0.01212 | 0.005714 | 0.005714 | 0.1029 | 0.2647 | 0.1571 | 0.1743 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2432 | 2500 | +2.8% | -462.8 to +599.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5013 | 5602 | +11.8% | -364.6 to +1544 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.2 | 38.92 | -9.9% | -5.785 to -2.77 | GAIN |
| failed requests (%) | 28.33 | 27.87 | -1.6% | -1.56 to +0.628 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 12.31 | +27.6% | +1.787 to +3.539 | power given |
| pods started | 4.879 | 7.545 | +54.7% | +1.627 to +3.707 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.049e-16 to +2.357e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.5 | +0.4% | +0.314 to +1.313 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.5 | +0.4% | +0.314 to +1.313 | power given |
| CPU used with Omni's own (cores), mean | 2.366 | 2.373 | +0.3% | -0.009468 to +0.02304 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.14 | 70.77 | +0.9% | +0.1679 to +1.097 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.00303 | +0.00303 | -0.003142 to +0.009203 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2154 | 3069 | +42.4% | +347.3 to +1482 | LOSS |
| response time (ms), 99th percentile | 4802 | 5996 | +24.9% | +285 to +2104 | LOSS |
| time over the response line (% of samples) | 47.13 | 42.96 | -8.8% | -5.773 to -2.56 | GAIN |
| failed requests (%) | 27.25 | 25.25 | -7.3% | -3.009 to -0.9899 | GAIN |
| HPA replicas, mean | 9.702 | 13.93 | +43.5% | +3.577 to +4.871 | power given |
| pods started | 4.486 | 8.914 | +98.7% | +3.526 to +5.331 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.081e-16 to +1.514e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 185.3 | +0.4% | +0.2478 to +1.285 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 185.3 | +0.4% | +0.2478 to +1.285 | power given |
| CPU used with Omni's own (cores), mean | 2.446 | 2.458 | +0.5% | +0.005463 to +0.01863 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.86 | 73.12 | +1.7% | +1.065 to +1.448 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.01143 | -20.0% | -0.0205 to +0.01479 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2173 | 2236 | +2.9% | -660.5 to +787.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4617 | 4804 | +4.1% | -416.1 to +790.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 39.56 | 35.62 | -9.9% | -5.587 to -2.285 | GAIN |
| failed requests (%) | 26.74 | 25.95 | -3.0% | -1.694 to +0.1053 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.634 | 11.71 | +21.5% | +1.226 to +2.919 | power given |
| pods started | 4.829 | 7.314 | +51.5% | +1.383 to +3.589 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.038e-16 to +4.561e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.8 | +0.2% | -0.1382 to +0.9282 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.8 | +0.2% | -0.1382 to +0.9282 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.301 | 2.315 | +0.6% | +0.002108 to +0.02451 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.43 | 69.24 | +1.2% | +0.4469 to +1.157 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.01143 | +300.0% | -0.004257 to +0.0214 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2092 | 2562 | +22.5% | -65.32 to +1005 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4455 | 5184 | +16.4% | -198.3 to +1657 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 47.02 | 42.85 | -8.9% | -5.888 to -2.438 | GAIN |
| failed requests (%) | 31.88 | 30.67 | -3.8% | -2.101 to -0.3057 | GAIN |
| HPA replicas, mean | 9.692 | 12.39 | +27.8% | +1.801 to +3.598 | power given |
| pods started | 4.212 | 7.333 | +74.1% | +1.92 to +4.323 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.311e-16 to +5.388e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.6 | +0.2% | -0.1791 to +0.821 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.6 | +0.2% | -0.1791 to +0.821 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.403 | 2.416 | +0.6% | +0.0004843 to +0.0267 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.65 | 72.6 | +1.3% | +0.5624 to +1.335 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.009091 | 0.01212 | +33.3% | -0.01352 to +0.01958 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2079 | 2816 | +35.4% | +226.3 to +1247 | LOSS |
| response time (ms), 99th percentile | 4288 | 5038 | +17.5% | +64.16 to +1435 | LOSS |
| time over the response line (% of samples) | 40.28 | 36.82 | -8.6% | -5.07 to -1.849 | GAIN |
| failed requests (%) | 24.38 | 22.54 | -7.5% | -2.949 to -0.7239 | GAIN |
| HPA replicas, mean | 9.664 | 12.85 | +33.0% | +2.313 to +4.057 | power given |
| pods started | 4.714 | 8.629 | +83.0% | +2.827 to +5.002 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.791e-16 to +5.298e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.7 | +0.4% | +0.3556 to +1.085 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.7 | +0.4% | +0.3556 to +1.085 | power given |
| CPU used with Omni's own (cores), mean | 2.275 | 2.284 | +0.4% | -0.002284 to +0.01907 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.81 | 67.89 | +1.6% | +0.6746 to +1.471 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.00833 to +0.00833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 0

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3223 | 4431 | +37.5% | +428.6 to +1989 | LOSS |
| response time (ms), 99th percentile | 5703 | 6581 | +15.4% | +235.2 to +1521 | LOSS |
| time over the response line (% of samples) | 52.04 | 48.74 | -6.3% | -4.759 to -1.83 | GAIN |
| failed requests (%) | 33.23 | 30.5 | -8.2% | -4.294 to -1.18 | GAIN |
| HPA replicas, mean | 9.712 | 12.93 | +33.1% | +2.504 to +3.933 | power given |
| pods started | 4.061 | 7.667 | +88.8% | +2.765 to +4.447 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.624e-16 to +4.7e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 185.2 | +0.4% | +0.261 to +1.041 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 185.2 | +0.4% | +0.261 to +1.041 | power given |
| CPU used with Omni's own (cores), mean | 2.418 | 2.429 | +0.4% | +0.005588 to +0.01611 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.99 | 73.65 | +2.3% | +1.519 to +1.805 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.103 | 0.2667 | +158.8% | +0.1204 to +0.2069 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1949 | 3442 | +76.6% | +850.8 to +2135 | LOSS |
| response time (ms), 99th percentile | 4074 | 5110 | +25.4% | +291.9 to +1781 | LOSS |
| time over the response line (% of samples) | 35.28 | 34.05 | -3.5% | -2.881 to +0.4332 | EVEN, inside the noise (cut) |
| failed requests (%) | 17.94 | 17.43 | -2.8% | -1.594 to +0.5745 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.656 | 11.86 | +22.8% | +1.422 to +2.979 | power given |
| pods started | 4.943 | 6.771 | +37.0% | +1.119 to +2.538 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.639e-16 to +5.162e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.3 | +0.2% | -0.05081 to +0.722 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.3 | +0.2% | -0.05081 to +0.722 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.247 | 2.247 | -0.0% | -0.01985 to +0.01967 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.34 | 69.75 | +3.6% | +1.723 to +3.084 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1571 | 0.1743 | +10.9% | -0.01345 to +0.04773 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
