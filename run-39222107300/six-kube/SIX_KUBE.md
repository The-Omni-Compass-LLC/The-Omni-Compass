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
| response time (ms), 95th percentile | 2287 | 2595 | 2250 | 2998 | 2560 | 2246 | 1860 | 2555 | 3502 | 3539 | 3436 | 3752 | 2362 | 3105 |
| response time (ms), 99th percentile | 4585 | 5196 | 4475 | 5977 | 5744 | 4991 | 4381 | 4905 | 6059 | 5633 | 5792 | 6371 | 4394 | 5907 |
| time over the response line (% of samples) | 43.99 | 39.14 | 43.8 | 39.53 | 41.94 | 36.35 | 40.78 | 38.8 | 49.56 | 45.44 | 54.15 | 49.47 | 48.78 | 45.65 |
| failed requests (%) | 30.16 | 29.81 | 24.47 | 24.07 | 27.74 | 27.33 | 28.61 | 28.31 | 31.04 | 30.17 | 36.8 | 36.45 | 27.59 | 28.5 |
| HPA replicas, mean | 9.61 | 12.33 | 9.676 | 13.38 | 9.643 | 13.05 | 9.656 | 13.26 | 9.67 | 13.31 | 9.686 | 13.61 | 9.692 | 12.63 |
| pods started | 5.55 | 7.95 | 4.75 | 9.05 | 5.053 | 8.75 | 4.75 | 8.95 | 4.9 | 9.45 | 4.45 | 8.35 | 4.55 | 7.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.8 | 183.1 | 184.4 | 184.3 | 184.1 | 183.9 | 184.5 | 184.7 | 185 | 184.9 | 184.4 | 184.7 | 184.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.8 | 183.1 | 184.4 | 184.3 | 184.1 | 183.9 | 184.5 | 184.7 | 185 | 184.9 | 184.4 | 184.7 | 184.8 |
| CPU used with Omni's own (cores), mean | 2.344 | 2.364 | 2.345 | 2.373 | 2.343 | 2.323 | 2.335 | 2.365 | 2.405 | 2.439 | 2.401 | 2.425 | 2.403 | 2.458 |
| host CPU busy, the real machine under kind (%) | 69.47 | 70.18 | 69.13 | 70.53 | 70.01 | 69.77 | 69.44 | 70.66 | 70.81 | 72.38 | 71.84 | 73.76 | 72.61 | 76.25 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.005 | 0.015 | 6.69 | 0.02 | 0 | 0.01 | 0.01 | 0.02 | 0.02 | 0 | 0.105 | 0.215 | 0.19 | 0.195 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2287 | 2595 | +13.5% | -449.4 to +1065 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4585 | 5196 | +13.3% | -485.7 to +1707 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.99 | 39.14 | -11.0% | -6.568 to -3.134 | GAIN |
| failed requests (%) | 30.16 | 29.81 | -1.2% | -2.092 to +1.396 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.61 | 12.33 | +28.3% | +1.499 to +3.939 | power given |
| pods started | 5.55 | 7.95 | +43.2% | +0.871 to +3.929 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.834e-16 to +1.616e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.8 | +0.6% | +0.2877 to +1.743 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.8 | +0.6% | +0.2877 to +1.743 | power given |
| CPU used with Omni's own (cores), mean | 2.344 | 2.364 | +0.9% | +0.001472 to +0.03902 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.47 | 70.18 | +1.0% | +0.1951 to +1.234 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.005 | 0.015 | +200.0% | -0.01093 to +0.03093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3; OFF THE CLOCK in 1 of 20 repetitions (the organism ended up to 134 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2250 | 2998 | +33.3% | +196.5 to +1300 | LOSS |
| response time (ms), 99th percentile | 4475 | 5977 | +33.6% | +824.5 to +2180 | LOSS |
| time over the response line (% of samples) | 43.8 | 39.53 | -9.7% | -6.007 to -2.532 | GAIN |
| failed requests (%) | 24.47 | 24.07 | -1.7% | -1.853 to +1.039 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.676 | 13.38 | +38.3% | +2.633 to +4.778 | power given |
| pods started | 4.75 | 9.05 | +90.5% | +2.875 to +5.725 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.238e-16 to +1.797e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 184.4 | +0.7% | -0.3685 to +2.87 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 184.4 | +0.7% | -0.3685 to +2.87 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.345 | 2.373 | +1.2% | +0.01233 to +0.0435 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.13 | 70.53 | +2.0% | +0.9932 to +1.805 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 6.69 | 0.02 | -99.7% | -20.63 to +7.29 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

19 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2560 | 2357 | -7.9% | -954.3 to +549.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5744 | 5244 | -8.7% | -1565 to +564.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.94 | 38.26 | -8.8% | -5.694 to -1.658 | GAIN |
| failed requests (%) | 27.74 | 28.77 | +3.7% | -0.4203 to +2.474 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.643 | 13.25 | +37.4% | +2.378 to +4.828 | power given |
| pods started | 5.053 | 8.842 | +75.0% | +2.56 to +5.019 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.019e-16 to +6.043e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.4 | +0.0% | -0.6217 to +0.7902 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.4 | +0.0% | -0.6217 to +0.7902 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.343 | 2.356 | +0.6% | -0.008232 to +0.03431 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.01 | 70.77 | +1.1% | +0.2518 to +1.274 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.01053 | +0.0105 | -0.004671 to +0.02572 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1860 | 2555 | +37.4% | +288.3 to +1103 | LOSS |
| response time (ms), 99th percentile | 4381 | 4905 | +11.9% | -394.9 to +1441 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.78 | 38.8 | -4.9% | -3.65 to -0.3086 | GAIN |
| failed requests (%) | 28.61 | 28.31 | -1.0% | -1.324 to +0.7243 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.656 | 13.26 | +37.3% | +2.464 to +4.743 | power given |
| pods started | 4.75 | 8.95 | +88.4% | +2.906 to +5.494 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.42e-16 to +7.637e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.5 | +0.3% | +0.0452 to +1.169 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.5 | +0.3% | +0.0452 to +1.169 | power given |
| CPU used with Omni's own (cores), mean | 2.335 | 2.365 | +1.3% | +0.01732 to +0.04391 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.44 | 70.66 | +1.8% | +0.8126 to +1.631 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.01093 to +0.03093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3502 | 3539 | +1.1% | -801.2 to +875.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6059 | 5633 | -7.0% | -1554 to +700.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 49.56 | 45.44 | -8.3% | -5.968 to -2.264 | GAIN |
| failed requests (%) | 31.04 | 30.17 | -2.8% | -2.025 to +0.2943 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.67 | 13.31 | +37.7% | +2.632 to +4.652 | power given |
| pods started | 4.9 | 9.45 | +92.9% | +3.13 to +5.97 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.775e-16 to +5.44e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185 | +0.1% | -0.4224 to +0.8935 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185 | +0.1% | -0.4224 to +0.8935 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.405 | 2.439 | +1.4% | +0.02014 to +0.0481 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.81 | 72.38 | +2.2% | +1.193 to +1.95 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.03921 to -0.0007933 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3436 | 3752 | +9.2% | -420.1 to +1051 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5792 | 6371 | +10.0% | -197.9 to +1355 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.15 | 49.47 | -8.7% | -6.291 to -3.083 | GAIN |
| failed requests (%) | 36.8 | 36.45 | -1.0% | -1.794 to +1.089 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.686 | 13.61 | +40.5% | +3.216 to +4.63 | power given |
| pods started | 4.45 | 8.35 | +87.6% | +2.838 to +4.962 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.763e-16 to +6.428e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.4 | -0.3% | -1.113 to +0.08864 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.4 | -0.3% | -1.113 to +0.08864 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.401 | 2.425 | +1.0% | +0.01276 to +0.03464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.84 | 73.76 | +2.7% | +1.783 to +2.061 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.105 | 0.215 | +104.8% | +0.07639 to +0.1436 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2362 | 3105 | +31.4% | -50.45 to +1536 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4394 | 5907 | +34.5% | +383.5 to +2644 | LOSS |
| time over the response line (% of samples) | 48.78 | 45.65 | -6.4% | -5.818 to -0.4528 | GAIN |
| failed requests (%) | 27.59 | 28.5 | +3.3% | -0.8147 to +2.629 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.692 | 12.63 | +30.3% | +2.147 to +3.726 | power given |
| pods started | 4.55 | 7.1 | +56.0% | +1.379 to +3.721 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.897e-16 to +4.345e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.1% | -0.517 to +0.774 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.1% | -0.517 to +0.774 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.403 | 2.458 | +2.3% | +0.02066 to +0.09029 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.61 | 76.25 | +5.0% | +2.632 to +4.644 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.19 | 0.195 | +2.6% | -0.03651 to +0.04651 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
