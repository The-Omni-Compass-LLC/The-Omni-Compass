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
| response time (ms), 95th percentile | 2017 | 3085 | 3437 | 3939 | 2012 | 1549 | 2972 | 2790 | 2479 | 3225 | 3364 | 3480 | 2709 | 3946 |
| response time (ms), 99th percentile | 5428 | 5898 | 5925 | 7328 | 4863 | 3565 | 5554 | 6123 | 4702 | 5018 | 5594 | 5470 | 5461 | 6997 |
| time over the response line (% of samples) | 45.06 | 42.13 | 46.44 | 41.76 | 37.2 | 31.13 | 37.85 | 32.72 | 41.35 | 38.28 | 48.9 | 45.79 | 53.2 | 50.28 |
| failed requests (%) | 32.08 | 31.1 | 21.35 | 21.93 | 24.13 | 24.18 | 23.95 | 22.76 | 25.53 | 25.38 | 34.87 | 35.27 | 28.59 | 29.99 |
| HPA replicas, mean | 9.651 | 12.86 | 9.699 | 13.86 | 9.602 | 11.45 | 9.587 | 10.59 | 9.649 | 13.07 | 9.716 | 13.7 | 9.758 | 13.66 |
| pods started | 4.9 | 8.3 | 4.7 | 9.6 | 5.5 | 7.8 | 5.7 | 6.6 | 5.2 | 8.4 | 4.2 | 8.8 | 3.6 | 7.5 |
| worker nodes in service, mean | 6 | 6 | 5.99 | 6 | 6 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.8 | 185.6 | 185.2 | 183.8 | 183.7 | 183.6 | 183.6 | 184.2 | 183.8 | 184.8 | 183.8 | 185.5 | 185.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.8 | 185.4 | 185.2 | 183.8 | 183.7 | 183.6 | 183.6 | 184.2 | 183.7 | 184.8 | 183.8 | 185.5 | 185.1 |
| CPU used with Omni's own (cores), mean | 2.382 | 2.408 | 2.475 | 2.506 | 2.326 | 2.346 | 2.359 | 2.373 | 2.339 | 2.343 | 2.385 | 2.4 | 2.508 | 2.535 |
| host CPU busy, the real machine under kind (%) | 70.46 | 71.38 | 72.21 | 73.99 | 68.54 | 69.41 | 69.25 | 69.94 | 68.71 | 69.7 | 71.38 | 72.78 | 74.85 | 78.18 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0 | 0.01 | 0.02 | 0 | 0 | 0 | 0.01 | 0.02 | 0 | 0.12 | 0.22 | 0.15 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2017 | 3085 | +52.9% | -456.5 to +2592 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5428 | 5898 | +8.7% | -1248 to +2189 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.06 | 42.13 | -6.5% | -6.388 to +0.515 | EVEN, inside the noise (cut) |
| failed requests (%) | 32.08 | 31.1 | -3.1% | -2.406 to +0.4388 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.651 | 12.86 | +33.3% | +1.258 to +5.165 | power given |
| pods started | 4.9 | 8.3 | +69.4% | +1.609 to +5.191 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.8 | +0.4% | -0.005529 to +1.346 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.8 | +0.4% | -0.005529 to +1.346 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.382 | 2.408 | +1.1% | +0.01056 to +0.0403 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.46 | 71.38 | +1.3% | +0.6097 to +1.228 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3437 | 3939 | +14.6% | -646.3 to +1650 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5925 | 7328 | +23.7% | +47 to +2760 | LOSS |
| time over the response line (% of samples) | 46.44 | 41.76 | -10.1% | -7.874 to -1.489 | GAIN |
| failed requests (%) | 21.35 | 21.93 | +2.7% | -0.5964 to +1.757 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.699 | 13.86 | +42.9% | +3.073 to +5.258 | power given |
| pods started | 4.7 | 9.6 | +104.3% | +3.07 to +6.73 | power given |
| worker nodes in service, mean | 5.99 | 6 | +0.2% | -0.01298 to +0.03356 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.2 | -0.2% | -1.785 to +0.9353 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.2 | -0.1% | -1.619 to +1.186 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.475 | 2.506 | +1.3% | +0.006626 to +0.0555 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.21 | 73.99 | +2.5% | +1.06 to +2.517 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.0306 to +0.0506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2012 | 1549 | -23.0% | -1081 to +154.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4863 | 3565 | -26.7% | -2274 to -322.3 | GAIN |
| time over the response line (% of samples) | 37.2 | 31.13 | -16.3% | -9.076 to -3.068 | GAIN |
| failed requests (%) | 24.13 | 24.18 | +0.2% | -1.316 to +1.414 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.602 | 11.45 | +19.2% | +0.1973 to +3.491 | power given |
| pods started | 5.5 | 7.8 | +41.8% | +0.062 to +4.538 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.7 | -0.1% | -1.143 to +0.9068 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.7 | -0.1% | -1.143 to +0.9068 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.326 | 2.346 | +0.8% | +0.005868 to +0.03365 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.54 | 69.41 | +1.3% | +0.5475 to +1.18 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 0, EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2972 | 2790 | -6.1% | -930.5 to +566.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5554 | 6123 | +10.3% | -676.7 to +1815 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 37.85 | 32.72 | -13.5% | -7.844 to -2.411 | GAIN |
| failed requests (%) | 23.95 | 22.76 | -5.0% | -2.731 to +0.3499 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.587 | 10.59 | +10.5% | -0.5077 to +2.523 | EVEN, inside the noise (up) |
| pods started | 5.7 | 6.6 | +15.8% | -0.7329 to +2.533 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.28e-16 to +1.471e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.6 | -0.0% | -0.5178 to +0.5133 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.6 | -0.0% | -0.5178 to +0.5133 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.359 | 2.373 | +0.6% | -0.0003535 to +0.02725 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.25 | 69.94 | +1.0% | +0.368 to +0.9967 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2479 | 3225 | +30.1% | -216.9 to +1710 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4702 | 5018 | +6.7% | -922.9 to +1556 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.35 | 38.28 | -7.4% | -7.44 to +1.312 | EVEN, inside the noise (cut) |
| failed requests (%) | 25.53 | 25.38 | -0.6% | -3.034 to +2.724 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.649 | 13.07 | +35.5% | +1.668 to +5.176 | power given |
| pods started | 5.2 | 8.4 | +61.5% | +1.154 to +5.246 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01135 to +0.004392 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 183.8 | -0.2% | -1.389 to +0.6907 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 183.7 | -0.2% | -1.417 to +0.5767 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.339 | 2.343 | +0.2% | -0.02792 to +0.03557 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.71 | 69.7 | +1.4% | +0.4374 to +1.544 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.05016 to +0.01016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3364 | 3480 | +3.4% | -1443 to +1674 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5594 | 5470 | -2.2% | -1720 to +1472 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 48.9 | 45.79 | -6.4% | -6.315 to +0.09685 | EVEN, inside the noise (cut) |
| failed requests (%) | 34.87 | 35.27 | +1.2% | -0.07584 to +0.8923 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.716 | 13.7 | +41.0% | +2.91 to +5.065 | power given |
| pods started | 4.2 | 8.8 | +109.5% | +3.202 to +5.998 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.905e-16 to +1.101e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 183.8 | -0.5% | -1.998 to +0.05089 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 183.8 | -0.5% | -1.998 to +0.05089 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.4 | +0.6% | -0.03138 to +0.06034 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.38 | 72.78 | +2.0% | -0.06735 to +2.879 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.12 | 0.22 | +83.3% | +0.06628 to +0.1337 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2709 | 3946 | +45.6% | +207.1 to +2266 | LOSS |
| response time (ms), 99th percentile | 5461 | 6997 | +28.1% | +180 to +2893 | LOSS |
| time over the response line (% of samples) | 53.2 | 50.28 | -5.5% | -6.863 to +1.036 | EVEN, inside the noise (cut) |
| failed requests (%) | 28.59 | 29.99 | +4.9% | -0.5826 to +3.381 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.758 | 13.66 | +40.0% | +2.8 to +5.003 | power given |
| pods started | 3.6 | 7.5 | +108.3% | +2.07 to +5.73 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.213e-15 to +5.023e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185.1 | -0.2% | -1.441 to +0.6427 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 185.1 | -0.2% | -1.441 to +0.6427 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.508 | 2.535 | +1.1% | +0.01978 to +0.03457 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.85 | 78.18 | +4.4% | +3.174 to +3.481 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.15 | 0.18 | +20.0% | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
