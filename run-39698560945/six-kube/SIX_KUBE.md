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
| response time (ms), 95th percentile | 1763 | 1241 | 1797 | 2807 | 2390 | 2035 | 2779 | 2853 | 2483 | 3346 | 3518 | 4521 | 1542 | 2989 |
| response time (ms), 99th percentile | 3839 | 3914 | 3593 | 5031 | 4288 | 4735 | 4538 | 5832 | 5145 | 5049 | 6293 | 6866 | 3485 | 5063 |
| time over the response line (% of samples) | 23.87 | 21.25 | 41.42 | 36.82 | 34.36 | 30.43 | 46.12 | 44.16 | 42.22 | 39.11 | 47.08 | 44.25 | 31.47 | 31.27 |
| failed requests (%) | 13.42 | 14.02 | 24.29 | 21.19 | 22.9 | 23.22 | 31.81 | 31.14 | 24.3 | 23.86 | 29.33 | 27.86 | 16.66 | 16.99 |
| HPA replicas, mean | 9.58 | 12.2 | 9.648 | 12.98 | 9.591 | 11.31 | 9.698 | 13.07 | 9.65 | 13.18 | 9.709 | 14.26 | 9.624 | 11.93 |
| pods started | 5.4 | 9.6 | 5.5 | 8.6 | 5.1 | 7.8 | 4.2 | 9 | 5 | 10.2 | 4.3 | 10 | 5.4 | 8.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.6 | 183.9 | 183.9 | 182 | 182.6 | 184.4 | 184.8 | 183.5 | 184.2 | 184.5 | 185.2 | 182.1 | 182.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.6 | 183.9 | 183.9 | 182 | 182.6 | 184.4 | 184.8 | 183.5 | 184.2 | 184.5 | 185.2 | 182.1 | 182.8 |
| CPU used with Omni's own (cores), mean | 2.109 | 2.129 | 2.356 | 2.374 | 2.199 | 2.214 | 2.396 | 2.419 | 2.295 | 2.311 | 2.432 | 2.46 | 2.197 | 2.225 |
| host CPU busy, the real machine under kind (%) | 62.21 | 63.2 | 69.27 | 70.3 | 65.52 | 66.34 | 71.28 | 72.4 | 67.54 | 68.77 | 72.35 | 74.25 | 66.16 | 69.22 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.02 | 0.01 | 0 | 0 | 0 | 0.01 | 0.02 | 0.02 | 0.09 | 0.21 | 0.19 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1763 | 1241 | -29.6% | -849.4 to -194.4 | GAIN |
| response time (ms), 99th percentile | 3839 | 3914 | +1.9% | -1012 to +1161 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.87 | 21.25 | -11.0% | -4.58 to -0.6736 | GAIN |
| failed requests (%) | 13.42 | 14.02 | +4.5% | -0.629 to +1.829 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.58 | 12.2 | +27.3% | +0.9697 to +4.265 | power given |
| pods started | 5.4 | 9.6 | +77.8% | +2.046 to +6.354 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +6.104e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.6 | -0.3% | -1.44 to +0.4524 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.6 | -0.3% | -1.44 to +0.4524 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.109 | 2.129 | +0.9% | -0.01771 to +0.05622 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.21 | 63.2 | +1.6% | -0.1084 to +2.096 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1797 | 2807 | +56.2% | +112.1 to +1909 | LOSS |
| response time (ms), 99th percentile | 3593 | 5031 | +40.0% | -401.6 to +3278 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.42 | 36.82 | -11.1% | -6.507 to -2.705 | GAIN |
| failed requests (%) | 24.29 | 21.19 | -12.7% | -5.504 to -0.6826 | GAIN |
| HPA replicas, mean | 9.648 | 12.98 | +34.5% | +1.588 to +5.073 | power given |
| pods started | 5.5 | 8.6 | +56.4% | +1.613 to +4.587 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.735e-15 to -4.108e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.9 | -0.0% | -1.061 to +0.9996 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.9 | -0.0% | -1.061 to +0.9996 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.356 | 2.374 | +0.8% | -0.005942 to +0.04141 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.27 | 70.3 | +1.5% | +0.2836 to +1.775 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.01 | -50.0% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2390 | 2035 | -14.9% | -956.8 to +246.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4288 | 4735 | +10.4% | -222.9 to +1117 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 34.36 | 30.43 | -11.4% | -8.142 to +0.2811 | EVEN, inside the noise (cut) |
| failed requests (%) | 22.9 | 23.22 | +1.4% | -1.045 to +1.69 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.591 | 11.31 | +17.9% | -0.1399 to +3.568 | EVEN, inside the noise (up) |
| pods started | 5.1 | 7.8 | +52.9% | +1.081 to +4.319 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.121e-15 to +1.121e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 182.6 | +0.3% | -0.06584 to +1.135 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 182.6 | +0.3% | -0.06584 to +1.135 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.199 | 2.214 | +0.7% | -0.005299 to +0.03493 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.52 | 66.34 | +1.2% | +0.2306 to +1.406 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2779 | 2853 | +2.7% | -1017 to +1166 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4538 | 5832 | +28.5% | -297 to +2886 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 46.12 | 44.16 | -4.3% | -4.662 to +0.738 | EVEN, inside the noise (cut) |
| failed requests (%) | 31.81 | 31.14 | -2.1% | -2.555 to +1.223 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.698 | 13.07 | +34.8% | +1.61 to +5.134 | power given |
| pods started | 4.2 | 9 | +114.3% | +2.568 to +7.032 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.066e-16 to +9.395e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.8 | +0.2% | -0.4852 to +1.153 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.8 | +0.2% | -0.4852 to +1.153 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.396 | 2.419 | +1.0% | +0.001408 to +0.04524 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.28 | 72.4 | +1.6% | +0.4536 to +1.788 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2483 | 3346 | +34.8% | -320.5 to +2047 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5145 | 5049 | -1.9% | -1290 to +1099 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 42.22 | 39.11 | -7.3% | -5.661 to -0.5439 | GAIN |
| failed requests (%) | 24.3 | 23.86 | -1.8% | -2.262 to +1.379 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 13.18 | +36.6% | +1.743 to +5.321 | power given |
| pods started | 5 | 10.2 | +104.0% | +2.918 to +7.482 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.989e-16 to +5.436e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | +0.4% | -0.2363 to +1.543 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | +0.4% | -0.2363 to +1.543 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.295 | 2.311 | +0.7% | +2.589e-05 to +0.03099 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.54 | 68.77 | +1.8% | +0.8181 to +1.638 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.02 | 0.02 | +0.0% | -0.04769 to +0.04769 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3518 | 4521 | +28.5% | -411.1 to +2418 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6293 | 6866 | +9.1% | -382.4 to +1530 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 47.08 | 44.25 | -6.0% | -6.505 to +0.8425 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.33 | 27.86 | -5.0% | -4.463 to +1.524 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.709 | 14.26 | +46.9% | +4.14 to +4.957 | power given |
| pods started | 4.3 | 10 | +132.6% | +4.228 to +7.172 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.738e-15 to +6.725e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 185.2 | +0.4% | -0.2916 to +1.635 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 185.2 | +0.4% | -0.2916 to +1.635 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.432 | 2.46 | +1.1% | +0.01458 to +0.04009 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.35 | 74.25 | +2.6% | +1.739 to +2.058 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.09 | 0.21 | +133.3% | +0.06358 to +0.1764 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1542 | 2989 | +93.9% | -66.12 to +2961 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3485 | 5063 | +45.3% | -409.1 to +3565 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 31.47 | 31.27 | -0.7% | -1.908 to +1.498 | EVEN, inside the noise (cut) |
| failed requests (%) | 16.66 | 16.99 | +2.0% | -1.719 to +2.37 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.624 | 11.93 | +24.0% | +0.9052 to +3.71 | power given |
| pods started | 5.4 | 8.6 | +59.3% | +1.269 to +5.131 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.451e-16 to +4.675e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 182.8 | +0.4% | -0.2356 to +1.574 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 182.8 | +0.4% | -0.2356 to +1.574 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.197 | 2.225 | +1.3% | +0.004467 to +0.05281 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.16 | 69.22 | +4.6% | +2.379 to +3.744 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.19 | 0.18 | -5.3% | -0.07263 to +0.05263 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
