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
| response time (ms), 95th percentile | 2101 | 1910 | 1942 | 2852 | 2326 | 2529 | 2974 | 2840 | 2509 | 2857 | 3593 | 4012 | 3010 | 3569 |
| response time (ms), 99th percentile | 4528 | 4491 | 4078 | 4966 | 5305 | 5108 | 5736 | 5922 | 5111 | 4820 | 5718 | 6012 | 5651 | 6712 |
| time over the response line (% of samples) | 42.07 | 38.82 | 37.37 | 32.65 | 41.55 | 38.21 | 49.35 | 46.19 | 44.6 | 39.83 | 49.06 | 45.08 | 45.53 | 43.33 |
| failed requests (%) | 29.31 | 30.2 | 20.71 | 19.71 | 28.23 | 28.11 | 33.75 | 34.04 | 29.23 | 26.85 | 31.13 | 30.38 | 22.34 | 24.02 |
| HPA replicas, mean | 9.639 | 12.79 | 9.642 | 13.08 | 9.643 | 12.46 | 9.683 | 13.05 | 9.661 | 13.3 | 9.676 | 13.19 | 9.704 | 12.51 |
| pods started | 5 | 8.314 | 5.314 | 8.971 | 4.943 | 7.743 | 4.571 | 8.629 | 5.057 | 9.353 | 4.686 | 8.4 | 4.457 | 7.314 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | 183.2 | 183.4 | 183.9 | 184.2 | 184.8 | 185 | 183.9 | 183.9 | 184.6 | 184.3 | 185.5 | 184.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | 183.2 | 183.4 | 183.9 | 184.2 | 184.8 | 185 | 183.9 | 183.9 | 184.6 | 184.3 | 185.5 | 184.9 |
| CPU used with Omni's own (cores), mean | 2.313 | 2.332 | 2.275 | 2.306 | 2.332 | 2.36 | 2.45 | 2.474 | 2.33 | 2.353 | 2.381 | 2.406 | 2.435 | 2.476 |
| host CPU busy, the real machine under kind (%) | 68.65 | 69.53 | 66.93 | 68.44 | 69.62 | 70.61 | 72.85 | 74.03 | 68.62 | 69.99 | 70.93 | 72.87 | 72.94 | 76.35 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02571 | 0.01143 | 0 | 0.02 | 0.008571 | 0.01143 | 0.01714 | 0.02353 | 0.1 | 0.2229 | 0.1657 | 0.1771 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2101 | 1910 | -9.1% | -696.2 to +312.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4528 | 4491 | -0.8% | -829.7 to +756.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 42.07 | 38.82 | -7.7% | -4.53 to -1.969 | GAIN |
| failed requests (%) | 29.31 | 30.2 | +3.0% | -0.2342 to +2.011 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.639 | 12.79 | +32.7% | +2.316 to +3.986 | power given |
| pods started | 5 | 8.314 | +66.3% | +2.365 to +4.263 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.762e-16 to +5.284e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | +0.2% | -0.04872 to +0.8444 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | -0.04872 to +0.8444 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.313 | 2.332 | +0.8% | +0.007763 to +0.03069 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.65 | 69.53 | +1.3% | +0.5969 to +1.163 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1942 | 2852 | +46.8% | +371.2 to +1448 | LOSS |
| response time (ms), 99th percentile | 4078 | 4966 | +21.8% | +149.1 to +1627 | LOSS |
| time over the response line (% of samples) | 37.37 | 32.65 | -12.6% | -6.347 to -3.101 | GAIN |
| failed requests (%) | 20.71 | 19.71 | -4.8% | -1.625 to -0.3755 | GAIN |
| HPA replicas, mean | 9.642 | 13.08 | +35.6% | +2.63 to +4.238 | power given |
| pods started | 5.314 | 8.971 | +68.8% | +2.711 to +4.603 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.824e-16 to -1.311e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.4 | +0.1% | -0.3197 to +0.6893 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.4 | +0.1% | -0.3197 to +0.6893 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.306 | +1.4% | +0.01662 to +0.04629 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.93 | 68.44 | +2.3% | +1.096 to +1.926 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02571 | 0.01143 | -55.6% | -0.03124 to +0.00267 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2326 | 2529 | +8.8% | -268.6 to +675.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5305 | 5108 | -3.7% | -830.3 to +436.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.55 | 38.21 | -8.0% | -4.647 to -2.033 | GAIN |
| failed requests (%) | 28.23 | 28.11 | -0.4% | -0.961 to +0.7093 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.643 | 12.46 | +29.2% | +1.912 to +3.723 | power given |
| pods started | 4.943 | 7.743 | +56.6% | +1.812 to +3.788 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.898e-16 to +1.345e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.2 | +0.2% | -0.02375 to +0.7085 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.2 | +0.2% | -0.02375 to +0.7085 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.36 | +1.2% | +0.01936 to +0.03598 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.62 | 70.61 | +1.4% | +0.7613 to +1.217 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.02 | +0.02 | +0.006061 to +0.03394 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2974 | 2840 | -4.5% | -690 to +421.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5736 | 5922 | +3.2% | -480.2 to +851.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 49.35 | 46.19 | -6.4% | -4.726 to -1.585 | GAIN |
| failed requests (%) | 33.75 | 34.04 | +0.9% | -0.5331 to +1.125 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.683 | 13.05 | +34.7% | +2.518 to +4.207 | power given |
| pods started | 4.571 | 8.629 | +88.8% | +2.819 to +5.295 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.004489 to +0.001528 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185 | +0.1% | -0.2889 to +0.6738 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185 | +0.1% | -0.3533 to +0.6786 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.474 | +1.0% | +0.01369 to +0.03516 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.85 | 74.03 | +1.6% | +0.9849 to +1.366 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.008571 | 0.01143 | +33.3% | -0.0127 to +0.01841 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2368 | 2857 | +20.7% | +44.38 to +933.9 | LOSS |
| response time (ms), 99th percentile | 5045 | 4820 | -4.5% | -739 to +289.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 42.97 | 39.83 | -7.3% | -4.402 to -1.881 | GAIN |
| failed requests (%) | 27.24 | 26.85 | -1.5% | -1.121 to +0.3302 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.651 | 13.3 | +37.8% | +2.833 to +4.465 | power given |
| pods started | 5.206 | 9.353 | +79.7% | +3.163 to +5.131 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.478e-16 to +5.523e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.9 | +0.2% | -0.2058 to +0.7713 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.9 | +0.2% | -0.2058 to +0.7713 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.327 | 2.353 | +1.1% | +0.01548 to +0.03584 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.67 | 69.99 | +1.9% | +1.063 to +1.588 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01176 | 0.02353 | +100.0% | -0.00699 to +0.03052 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3593 | 4012 | +11.7% | -152.2 to +989.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5718 | 6012 | +5.1% | -221.2 to +808.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 49.06 | 45.08 | -8.1% | -6.003 to -1.97 | GAIN |
| failed requests (%) | 31.13 | 30.38 | -2.4% | -1.969 to +0.4613 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.676 | 13.19 | +36.3% | +2.859 to +4.169 | power given |
| pods started | 4.686 | 8.4 | +79.3% | +2.781 to +4.648 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.883e-16 to +2.33e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.3 | -0.2% | -0.7162 to +0.1357 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.3 | -0.2% | -0.7162 to +0.1357 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.381 | 2.406 | +1.0% | +0.01513 to +0.03377 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.93 | 72.87 | +2.7% | +1.642 to +2.239 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.2229 | +122.9% | +0.09512 to +0.1506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3010 | 3569 | +18.6% | +186.1 to +932 | LOSS |
| response time (ms), 99th percentile | 5651 | 6712 | +18.8% | +351.5 to +1770 | LOSS |
| time over the response line (% of samples) | 45.53 | 43.33 | -4.8% | -3.881 to -0.5282 | GAIN |
| failed requests (%) | 22.34 | 24.02 | +7.5% | +0.8241 to +2.531 | LOSS |
| HPA replicas, mean | 9.704 | 12.51 | +28.9% | +2.114 to +3.497 | power given |
| pods started | 4.457 | 7.314 | +64.1% | +1.975 to +3.739 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.984e-16 to +3.984e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 184.9 | -0.3% | -0.8495 to -0.2286 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 184.9 | -0.3% | -0.8495 to -0.2286 | GAIN |
| CPU used with Omni's own (cores), mean | 2.435 | 2.476 | +1.7% | +0.03453 to +0.04735 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.94 | 76.35 | +4.7% | +3.216 to +3.618 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1657 | 0.1771 | +6.9% | -0.01179 to +0.03465 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
