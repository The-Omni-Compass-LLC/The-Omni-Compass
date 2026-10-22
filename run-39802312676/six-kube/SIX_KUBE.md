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
| response time (ms), 95th percentile | 3020 | 3110 | 2260 | 3044 | 2982 | 3857 | 1978 | 3081 | 2125 | 3970 | 1886 | 2692 | 1785 | 1810 |
| response time (ms), 99th percentile | 6164 | 5752 | 4985 | 5425 | 6991 | 7568 | 4549 | 6223 | 4744 | 7024 | 3548 | 4296 | 3584 | 3586 |
| time over the response line (% of samples) | 41.13 | 38.86 | 53.8 | 46.99 | 59.62 | 55.74 | 43.99 | 43.76 | 46.9 | 44.06 | 28.51 | 25.28 | 36.84 | 36.08 |
| failed requests (%) | 26.73 | 26.24 | 30.91 | 33.04 | 41.53 | 42.09 | 29.57 | 31.22 | 29.22 | 31.22 | 17.12 | 17.26 | 20.42 | 21.53 |
| HPA replicas, mean | 9.621 | 14.85 | 9.698 | 13.34 | 9.731 | 13.98 | 9.682 | 14.58 | 9.7 | 13.29 | 9.605 | 13.72 | 9.713 | 11.92 |
| pods started | 5.5 | 10.8 | 4.6 | 9.2 | 4.3 | 9 | 4.4 | 10 | 4.4 | 10.6 | 5.7 | 11 | 4 | 7.9 |
| worker nodes in service, mean | 6 | 5.966 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.9 | 185.7 | 185.4 | 185.6 | 186 | 184 | 184.6 | 184.9 | 184.9 | 181.8 | 182.1 | 183.6 | 183.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.2 | 185.7 | 185.4 | 185.6 | 186 | 184 | 184.6 | 184.9 | 184.9 | 181.8 | 182.1 | 183.6 | 183.4 |
| CPU used with Omni's own (cores), mean | 2.417 | 2.435 | 2.549 | 2.585 | 2.567 | 2.602 | 2.389 | 2.434 | 2.439 | 2.475 | 2.128 | 2.168 | 2.28 | 2.333 |
| host CPU busy, the real machine under kind (%) | 70.86 | 72.47 | 74.89 | 76.99 | 76.45 | 78.06 | 71.16 | 73.09 | 71.42 | 73.43 | 63.48 | 65.86 | 68.42 | 72.73 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02 | 0 | 0 | 0 | 0 | 0.03 | 0 | 0 | 0.1 | 0.23 | 0.16 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3020 | 3110 | +3.0% | -1354 to +1534 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6164 | 5752 | -6.7% | -1748 to +924.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.13 | 38.86 | -5.5% | -4.933 to +0.395 | EVEN, inside the noise (cut) |
| failed requests (%) | 26.73 | 26.24 | -1.8% | -3.372 to +2.401 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.621 | 14.85 | +54.4% | +5.01 to +5.456 | power given |
| pods started | 5.5 | 10.8 | +96.4% | +4.405 to +6.195 | power given |
| worker nodes in service, mean | 6 | 5.966 | -0.6% | -0.1124 to +0.04349 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.9 | +0.4% | -0.4336 to +1.73 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.2 | -0.0% | -2.654 to +2.55 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.417 | 2.435 | +0.8% | -0.02671 to +0.06376 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.86 | 72.47 | +2.3% | +1.315 to +1.895 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.874e+07 to +7.876e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008373 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2260 | 3044 | +34.7% | -854.4 to +2423 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4985 | 5425 | +8.8% | -1671 to +2551 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.8 | 46.99 | -12.7% | -8.961 to -4.653 | GAIN |
| failed requests (%) | 30.91 | 33.04 | +6.9% | -0.4621 to +4.721 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.698 | 13.34 | +37.6% | +2.781 to +4.507 | power given |
| pods started | 4.6 | 9.2 | +100.0% | +3.202 to +5.998 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.4 | -0.1% | -1.305 to +0.7565 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.4 | -0.1% | -1.305 to +0.7565 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.549 | 2.585 | +1.4% | +0.02725 to +0.04386 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.89 | 76.99 | +2.8% | +1.96 to +2.251 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0 | -100.0% | -0.05016 to +0.01016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2982 | 3857 | +29.4% | -915.6 to +2666 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6991 | 7568 | +8.3% | -668 to +1822 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.62 | 55.74 | -6.5% | -6.863 to -0.8944 | GAIN |
| failed requests (%) | 41.53 | 42.09 | +1.4% | -2.335 to +3.458 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.731 | 13.98 | +43.7% | +3.644 to +4.854 | power given |
| pods started | 4.3 | 9 | +109.3% | +3.529 to +5.871 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.345e-16 to +1.167e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 186 | +0.2% | -0.6063 to +1.41 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 186 | +0.2% | -0.6063 to +1.41 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.567 | 2.602 | +1.4% | +0.0223 to +0.04855 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.45 | 78.06 | +2.1% | +1.481 to +1.741 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1978 | 3081 | +55.8% | +71.37 to +2135 | LOSS |
| response time (ms), 99th percentile | 4549 | 6223 | +36.8% | -60.05 to +3409 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.99 | 43.76 | -0.5% | -2.328 to +1.872 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.57 | 31.22 | +5.6% | -0.182 to +3.479 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.682 | 14.58 | +50.5% | +4.45 to +5.336 | power given |
| pods started | 4.4 | 10 | +127.3% | +4.577 to +6.623 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.304e-15 to +4.161e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.6 | +0.3% | -0.5978 to +1.624 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.6 | +0.3% | -0.5978 to +1.624 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.389 | 2.434 | +1.9% | +0.03644 to +0.05285 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.16 | 73.09 | +2.7% | +1.787 to +2.073 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.03 | +0.03 | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2125 | 3970 | +86.8% | +133.9 to +3555 | LOSS |
| response time (ms), 99th percentile | 4744 | 7024 | +48.1% | +730.9 to +3831 | LOSS |
| time over the response line (% of samples) | 46.9 | 44.06 | -6.1% | -5.926 to +0.2435 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.22 | 31.22 | +6.9% | +0.4947 to +3.512 | LOSS |
| HPA replicas, mean | 9.7 | 13.29 | +37.1% | +2.471 to +4.719 | power given |
| pods started | 4.4 | 10.6 | +140.9% | +4.994 to +7.406 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.471e-16 to +9.471e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.9 | -0.0% | -1.198 to +1.158 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.9 | -0.0% | -1.198 to +1.158 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.439 | 2.475 | +1.5% | +0.02573 to +0.04697 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.42 | 73.43 | +2.8% | +1.672 to +2.343 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1886 | 2692 | +42.7% | -79.53 to +1691 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3548 | 4296 | +21.1% | -27.91 to +1523 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.51 | 25.28 | -11.3% | -5.697 to -0.7744 | GAIN |
| failed requests (%) | 17.12 | 17.26 | +0.8% | -1.495 to +1.768 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.605 | 13.72 | +42.9% | +3.308 to +4.925 | power given |
| pods started | 5.7 | 11 | +93.0% | +4.542 to +6.058 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.732e-16 to +1.306e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 182.1 | +0.2% | -0.9618 to +1.549 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 182.1 | +0.2% | -0.9618 to +1.549 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.128 | 2.168 | +1.8% | +0.01185 to +0.06683 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.48 | 65.86 | +3.8% | +1.533 to +3.233 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.23 | +130.0% | +0.06214 to +0.1979 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1785 | 1810 | +1.4% | -354.9 to +404.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3584 | 3586 | +0.1% | -1213 to +1217 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 36.84 | 36.08 | -2.0% | -4.336 to +2.829 | EVEN, inside the noise (cut) |
| failed requests (%) | 20.42 | 21.53 | +5.5% | -0.5638 to +2.789 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.713 | 11.92 | +22.8% | +0.593 to +3.828 | power given |
| pods started | 4 | 7.9 | +97.5% | +1.755 to +6.045 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.4 | -0.1% | -0.9608 to +0.5517 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.4 | -0.1% | -0.9608 to +0.5517 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.28 | 2.333 | +2.4% | +0.03154 to +0.0764 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.42 | 72.73 | +6.3% | +3.546 to +5.075 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.18 | +12.5% | -0.04573 to +0.08573 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
