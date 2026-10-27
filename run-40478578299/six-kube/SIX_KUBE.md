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
| response time (ms), 95th percentile | 2191 | 2070 | 2022 | 2361 | 2888 | 2306 | 2246 | 1986 | 2463 | 2722 | 3392 | 4338 | 2016 | 2842 |
| response time (ms), 99th percentile | 4608 | 4691 | 3845 | 4522 | 6096 | 5630 | 5204 | 5144 | 4693 | 5025 | 6073 | 6579 | 4378 | 5605 |
| time over the response line (% of samples) | 37.06 | 33.07 | 34.59 | 31.07 | 45.03 | 39.37 | 41.19 | 37.83 | 35.8 | 31.77 | 54.34 | 50.35 | 43.75 | 41.67 |
| failed requests (%) | 24.83 | 24.7 | 19.64 | 19.68 | 31.05 | 30.25 | 28.01 | 28.11 | 18.95 | 18.74 | 35.59 | 35.88 | 25.24 | 25.7 |
| HPA replicas, mean | 9.603 | 11.91 | 9.662 | 12.85 | 9.644 | 11.22 | 9.663 | 12.3 | 9.636 | 13.22 | 9.717 | 13.65 | 9.709 | 12.81 |
| pods started | 5.371 | 7.886 | 4.914 | 8.486 | 4.914 | 6.486 | 4.571 | 7.886 | 5.371 | 9.714 | 4.229 | 8.114 | 4.114 | 7 |
| worker nodes in service, mean | 5.999 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.3 | 182.8 | 182.8 | 184.3 | 184.4 | 183.8 | 184 | 183.8 | 183.6 | 185.3 | 185.1 | 184.3 | 184.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.3 | 182.8 | 182.8 | 184.3 | 184.4 | 183.8 | 184 | 183.8 | 183.6 | 185.3 | 185.1 | 184.3 | 184.2 |
| CPU used with Omni's own (cores), mean | 2.265 | 2.281 | 2.235 | 2.254 | 2.391 | 2.41 | 2.328 | 2.343 | 2.312 | 2.344 | 2.454 | 2.484 | 2.364 | 2.394 |
| host CPU busy, the real machine under kind (%) | 66.74 | 67.59 | 65.81 | 66.95 | 70.72 | 71.77 | 69.18 | 70.12 | 67.64 | 69.21 | 73.16 | 75.15 | 70.95 | 74.14 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.01429 | 0.02 | 0.01143 | 0.005714 | 0 | 0.01143 | 0.002857 | 0.01429 | 0.1029 | 0.2257 | 0.9571 | 0.3647 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2191 | 2070 | -5.5% | -676.3 to +434 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4608 | 4691 | +1.8% | -642.5 to +807.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 37.06 | 33.07 | -10.8% | -5.534 to -2.444 | GAIN |
| failed requests (%) | 24.83 | 24.7 | -0.5% | -0.6928 to +0.4259 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.603 | 11.91 | +24.0% | +1.449 to +3.166 | power given |
| pods started | 5.371 | 7.886 | +46.8% | +1.473 to +3.556 | power given |
| worker nodes in service, mean | 5.999 | 5.997 | -0.0% | -0.007425 to +0.00437 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.3 | +0.0% | -0.3178 to +0.4929 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.3 | +0.0% | -0.3647 to +0.4779 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.265 | 2.281 | +0.7% | +0.006792 to +0.02648 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.74 | 67.59 | +1.3% | +0.5763 to +1.122 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2022 | 2361 | +16.8% | -56.65 to +735.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3845 | 4522 | +17.6% | +104.4 to +1249 | LOSS |
| time over the response line (% of samples) | 34.59 | 31.07 | -10.2% | -4.744 to -2.296 | GAIN |
| failed requests (%) | 19.64 | 19.68 | +0.2% | -1.129 to +1.216 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.662 | 12.85 | +33.0% | +2.313 to +4.061 | power given |
| pods started | 4.914 | 8.486 | +72.7% | +2.462 to +4.681 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.808e-16 to -2.824e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 182.8 | -0.0% | -0.5146 to +0.3862 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 182.8 | -0.0% | -0.5146 to +0.3862 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.235 | 2.254 | +0.8% | +0.008447 to +0.02918 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.81 | 66.95 | +1.7% | +0.7951 to +1.484 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.02 | +40.0% | -0.01459 to +0.02602 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2888 | 2306 | -20.2% | -1197 to +32.24 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6096 | 5630 | -7.6% | -1172 to +241.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 45.03 | 39.37 | -12.6% | -7.274 to -4.052 | GAIN |
| failed requests (%) | 31.05 | 30.25 | -2.6% | -1.731 to +0.1276 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 11.22 | +16.3% | +0.7458 to +2.397 | power given |
| pods started | 4.914 | 6.486 | +32.0% | +0.6169 to +2.526 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.755e-16 to +2.232e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.4 | +0.1% | -0.3287 to +0.6873 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.4 | +0.1% | -0.3287 to +0.6873 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.391 | 2.41 | +0.8% | +0.008556 to +0.02827 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.72 | 71.77 | +1.5% | +0.8152 to +1.289 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01143 | 0.005714 | -50.0% | -0.01733 to +0.005897 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2246 | 1986 | -11.6% | -778.1 to +258.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5204 | 5144 | -1.2% | -762.9 to +642.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.19 | 37.83 | -8.1% | -5.082 to -1.626 | GAIN |
| failed requests (%) | 28.01 | 28.11 | +0.3% | -0.6292 to +0.8135 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.663 | 12.3 | +27.3% | +1.758 to +3.518 | power given |
| pods started | 4.571 | 7.886 | +72.5% | +2.344 to +4.285 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.52e-16 to +3.012e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184 | +0.1% | -0.2536 to +0.6072 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184 | +0.1% | -0.2536 to +0.6072 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.328 | 2.343 | +0.6% | +0.003004 to +0.02635 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.18 | 70.12 | +1.4% | +0.5959 to +1.288 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01143 | +0.0114 | +0.0003412 to +0.02252 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2463 | 2722 | +10.5% | -154.3 to +673 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4693 | 5025 | +7.1% | -181 to +845.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 35.8 | 31.77 | -11.3% | -5.556 to -2.514 | GAIN |
| failed requests (%) | 18.95 | 18.74 | -1.1% | -0.8734 to +0.4552 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.636 | 13.22 | +37.2% | +2.797 to +4.371 | power given |
| pods started | 5.371 | 9.714 | +80.9% | +3.431 to +5.255 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.528e-16 to +2.991e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.6 | -0.1% | -0.8261 to +0.5396 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.6 | -0.1% | -0.8261 to +0.5396 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.312 | 2.344 | +1.4% | +0.02214 to +0.04163 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.64 | 69.21 | +2.3% | +1.288 to +1.853 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.002857 | 0.01429 | +400.0% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3392 | 4338 | +27.9% | +348 to +1543 | LOSS |
| response time (ms), 99th percentile | 6073 | 6579 | +8.3% | +40.01 to +971.4 | LOSS |
| time over the response line (% of samples) | 54.34 | 50.35 | -7.3% | -5.184 to -2.805 | GAIN |
| failed requests (%) | 35.59 | 35.88 | +0.8% | -0.5893 to +1.184 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.717 | 13.65 | +40.5% | +3.356 to +4.511 | power given |
| pods started | 4.229 | 8.114 | +91.9% | +3.079 to +4.692 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.404e-16 to +4.419e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.1 | -0.1% | -0.529 to +0.3061 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.1 | -0.1% | -0.529 to +0.3061 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.454 | 2.484 | +1.2% | +0.02122 to +0.03765 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.16 | 75.15 | +2.7% | +1.79 to +2.19 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1029 | 0.2257 | +119.4% | +0.0964 to +0.1493 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1986 | 2842 | +43.1% | +289.2 to +1421 | LOSS |
| response time (ms), 99th percentile | 4335 | 5605 | +29.3% | +543.8 to +1996 | LOSS |
| time over the response line (% of samples) | 43.23 | 41.67 | -3.6% | -3.488 to +0.371 | EVEN, inside the noise (cut) |
| failed requests (%) | 24.84 | 25.7 | +3.4% | +0.04019 to +1.665 | LOSS |
| HPA replicas, mean | 9.705 | 12.81 | +32.0% | +2.414 to +3.803 | power given |
| pods started | 4.176 | 7 | +67.6% | +1.98 to +3.667 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.622e-16 to +3.524e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.2 | -0.0% | -0.4216 to +0.4055 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.2 | -0.0% | -0.4216 to +0.4055 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.357 | 2.394 | +1.6% | +0.03237 to +0.04241 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.71 | 74.14 | +4.8% | +3.265 to +3.58 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.9794 | 0.3647 | -62.8% | -2.363 to +1.133 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
