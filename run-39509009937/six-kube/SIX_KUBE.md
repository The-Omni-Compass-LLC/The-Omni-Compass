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
| response time (ms), 95th percentile | 4247 | 3111 | 2627 | 2965 | 2905 | 2719 | 3201 | 3547 | 2920 | 4092 | 3043 | 3203 | 2370 | 3729 |
| response time (ms), 99th percentile | 6991 | 6991 | 4986 | 5987 | 5133 | 5078 | 5458 | 6044 | 6038 | 6260 | 5319 | 6085 | 4372 | 6388 |
| time over the response line (% of samples) | 57.05 | 54.6 | 40.45 | 39.8 | 35.75 | 32.61 | 43.21 | 38.82 | 54.57 | 53.03 | 50.9 | 46.44 | 50.11 | 48.58 |
| failed requests (%) | 38.81 | 40.05 | 20.62 | 20.4 | 22.94 | 22.84 | 27.2 | 27.06 | 35.44 | 34.63 | 32.82 | 33.58 | 28.32 | 28.95 |
| HPA replicas, mean | 9.721 | 14.5 | 9.698 | 13.56 | 9.573 | 12.18 | 9.588 | 12.08 | 9.68 | 13.33 | 9.703 | 13.04 | 9.713 | 12.5 |
| pods started | 4.3 | 9.5 | 4.5 | 9.2 | 5.7 | 7.7 | 5.6 | 8.5 | 4.7 | 9.1 | 4.3 | 7.9 | 4.2 | 7.3 |
| worker nodes in service, mean | 6 | 5.996 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 187.3 | 184.4 | 184.5 | 182.8 | 183.8 | 184 | 184.6 | 184.7 | 184.8 | 184.5 | 184.4 | 185.6 | 184.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 187.2 | 184.4 | 184.5 | 182.8 | 183.8 | 184 | 184.6 | 184.7 | 184.8 | 184.5 | 184.4 | 185.6 | 184.8 |
| CPU used with Omni's own (cores), mean | 2.558 | 2.589 | 2.374 | 2.407 | 2.282 | 2.294 | 2.399 | 2.413 | 2.419 | 2.413 | 2.401 | 2.426 | 2.47 | 2.498 |
| host CPU busy, the real machine under kind (%) | 75.83 | 76.94 | 69.68 | 71.11 | 67.57 | 68.29 | 70.41 | 71.33 | 71.34 | 71.68 | 71.93 | 74 | 74.23 | 77.43 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.01 | 0.02 | 0.01 | 0.01 | 0 | 0 | 0 | 0.01 | 0.01 | 0.1 | 0.24 | 0.18 | 0.17 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4247 | 3111 | -26.8% | -1989 to -284.5 | GAIN |
| response time (ms), 99th percentile | 6991 | 6991 | -0.0% | -1398 to +1397 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57.05 | 54.6 | -4.3% | -5.584 to +0.6972 | EVEN, inside the noise (cut) |
| failed requests (%) | 38.81 | 40.05 | +3.2% | -0.02226 to +2.497 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.721 | 14.5 | +49.1% | +3.557 to +5.994 | power given |
| pods started | 4.3 | 9.5 | +120.9% | +3.39 to +7.01 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01153 to +0.00446 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 187.3 | +0.7% | +0.637 to +2.121 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 187.2 | +0.7% | +0.4401 to +2.176 | power given |
| CPU used with Omni's own (cores), mean | 2.558 | 2.589 | +1.2% | +0.01912 to +0.04115 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.83 | 76.94 | +1.5% | +0.8991 to +1.323 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2627 | 2965 | +12.9% | -238.4 to +914.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4986 | 5987 | +20.1% | -202.8 to +2205 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.45 | 39.8 | -1.6% | -4.496 to +3.184 | EVEN, inside the noise (cut) |
| failed requests (%) | 20.62 | 20.4 | -1.0% | -1.282 to +0.8562 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.698 | 13.56 | +39.8% | +2.259 to +5.465 | power given |
| pods started | 4.5 | 9.2 | +104.4% | +2.54 to +6.86 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +6.104e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.5 | +0.1% | -0.9787 to +1.272 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.5 | +0.1% | -0.9787 to +1.272 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.374 | 2.407 | +1.4% | +0.01509 to +0.0517 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.68 | 71.11 | +2.1% | +0.7328 to +2.125 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.01 | -50.0% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2905 | 2719 | -6.4% | -1978 to +1607 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5133 | 5078 | -1.1% | -1832 to +1723 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 35.75 | 32.61 | -8.8% | -5.63 to -0.6469 | GAIN |
| failed requests (%) | 22.94 | 22.84 | -0.4% | -2.71 to +2.517 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.573 | 12.18 | +27.3% | +0.631 to +4.589 | power given |
| pods started | 5.7 | 7.7 | +35.1% | +0.2479 to +3.752 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.989e-16 to +5.436e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.8 | +0.5% | -0.1708 to +2.033 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.8 | +0.5% | -0.1708 to +2.033 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.282 | 2.294 | +0.6% | -0.007539 to +0.03341 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.57 | 68.29 | +1.1% | +0.1551 to +1.296 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3201 | 3547 | +10.8% | -1513 to +2205 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5458 | 6044 | +10.7% | -1222 to +2395 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.21 | 38.82 | -10.2% | -7.672 to -1.121 | GAIN |
| failed requests (%) | 27.2 | 27.06 | -0.5% | -3.556 to +3.262 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.588 | 12.08 | +26.0% | +0.8167 to +4.164 | power given |
| pods started | 5.6 | 8.5 | +51.8% | +1.166 to +4.634 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.345e-16 to +1.167e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.6 | +0.3% | -0.2047 to +1.477 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.6 | +0.3% | -0.2047 to +1.477 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.399 | 2.413 | +0.6% | +0.005388 to +0.02226 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.41 | 71.33 | +1.3% | +0.6563 to +1.191 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2920 | 4092 | +40.1% | -226.2 to +2571 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6038 | 6260 | +3.7% | -922.3 to +1366 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.57 | 53.03 | -2.8% | -5.685 to +2.614 | EVEN, inside the noise (cut) |
| failed requests (%) | 35.44 | 34.63 | -2.3% | -4.092 to +2.488 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.68 | 13.33 | +37.8% | +2.007 to +5.302 | power given |
| pods started | 4.7 | 9.1 | +93.6% | +2.343 to +6.457 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.0% | -0.932 to +1.096 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.0% | -0.932 to +1.096 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.413 | -0.3% | -0.06128 to +0.04781 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.34 | 71.68 | +0.5% | -1.35 to +2.03 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3043 | 3203 | +5.3% | -1216 to +1536 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5319 | 6085 | +14.4% | -523.2 to +2054 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 50.9 | 46.44 | -8.8% | -7.632 to -1.277 | GAIN |
| failed requests (%) | 32.82 | 33.58 | +2.3% | -2.289 to +3.82 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.703 | 13.04 | +34.4% | +2.029 to +4.638 | power given |
| pods started | 4.3 | 7.9 | +83.7% | +1.717 to +5.483 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.029e-15 to +2.095e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.4 | -0.1% | -0.7052 to +0.5082 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.4 | -0.1% | -0.7052 to +0.5082 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.401 | 2.426 | +1.0% | +0.01414 to +0.03616 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.93 | 74 | +2.9% | +1.756 to +2.391 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.24 | +140.0% | +0.08999 to +0.19 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2370 | 3729 | +57.4% | -27.87 to +2746 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4372 | 6388 | +46.1% | +482.2 to +3550 | LOSS |
| time over the response line (% of samples) | 50.11 | 48.58 | -3.0% | -5.016 to +1.961 | EVEN, inside the noise (cut) |
| failed requests (%) | 28.32 | 28.95 | +2.2% | -1.904 to +3.164 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.713 | 12.5 | +28.7% | +1.626 to +3.954 | power given |
| pods started | 4.2 | 7.3 | +73.8% | +1.538 to +4.662 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.262e-15 to +7.291e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 184.8 | -0.4% | -1.615 to +0.1473 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 184.8 | -0.4% | -1.615 to +0.1473 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.498 | +1.1% | +0.01231 to +0.043 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.23 | 77.43 | +4.3% | +2.821 to +3.579 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.18 | 0.17 | -5.6% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
