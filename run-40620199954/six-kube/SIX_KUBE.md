# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2361 | 2597 | 1516 | 3779 | 1753 | 3320 | 1293 | 2816 |
| response time (ms), 99th percentile | 5069 | 4709 | 3386 | 6324 | 3781 | 5703 | 3840 | 4726 |
| time over the response line (% of samples) | 58.31 | 48.87 | 44.14 | 59.14 | 48.41 | 53.8 | 51.28 | 47.97 |
| failed requests (%) | 50.79 | 40.28 | 36.53 | 49.21 | 41.67 | 43.99 | 45.65 | 41.36 |
| HPA replicas, mean | 9.91 | 10.89 | 9.892 | 10.9 | 9.895 | 11.01 | 9.912 | 11.24 |
| pods started | 5.032 | 6.2 | 5.742 | 6.516 | 5.71 | 6.774 | 5.71 | 7.452 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 5.999 | 6 | 5.999 | 5.999 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1377 | 1370 | 1382 | 1373 | 1379 | 1375 | 1375 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1377 | 1370 | 1382 | 1373 | 1379 | 1375 | 1375 |
| CPU used with Omni's own (cores), mean | 2.485 | 2.466 | 2.357 | 2.534 | 2.401 | 2.486 | 2.426 | 2.437 |
| host CPU busy, the real machine under kind (%) | 73.47 | 75.93 | 71.71 | 83.16 | 73 | 79.51 | 72.8 | 78.69 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.129 | 2.743 | 4.268 | 5.681 | 3.035 | 3.89 | 3.745 | 4.826 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

30 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2384 | 2597 | +8.9% | -1164 to +1591 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5108 | 4709 | -7.8% | -2429 to +1631 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57.69 | 48.87 | -15.3% | -27.93 to +10.28 | EVEN, inside the noise (cut) |
| failed requests (%) | 50.12 | 40.28 | -19.6% | -27.81 to +8.119 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.909 | 10.89 | +9.9% | +0.2814 to +1.673 | power given |
| pods started | 5.067 | 6.2 | +22.4% | +0.1444 to +2.122 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0005809 to +0.001348 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1377 | -0.2% | -15.94 to +11.46 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1377 | -0.2% | -15.89 to +11.53 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.481 | 2.466 | -0.6% | -0.1964 to +0.1673 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.29 | 75.93 | +3.6% | -3.169 to +8.452 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.13 | 2.743 | +28.8% | +0.4459 to +0.7808 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 5 (HPA replicas, mean; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

31 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1516 | 3779 | +149.3% | +1186 to +3340 | LOSS |
| response time (ms), 99th percentile | 3386 | 6324 | +86.8% | +1453 to +4423 | LOSS |
| time over the response line (% of samples) | 44.14 | 59.14 | +34.0% | -0.9971 to +30.99 | EVEN, inside the noise (up) |
| failed requests (%) | 36.53 | 49.21 | +34.7% | -3.453 to +28.8 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.892 | 10.9 | +10.2% | +0.4071 to +1.607 | power given |
| pods started | 5.742 | 6.516 | +13.5% | -0.1177 to +1.666 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 5.999 | 5.999 | +0.0% | -0.002203 to +0.003482 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1382 | +0.9% | +0.5976 to +24.66 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1382 | +0.9% | +0.7343 to +24.72 | power given |
| CPU used with Omni's own (cores), mean | 2.357 | 2.534 | +7.5% | +0.01719 to +0.3367 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.71 | 83.16 | +16.0% | +6.536 to +16.36 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.268 | 5.681 | +33.1% | +1.144 to +1.682 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

31 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1753 | 3320 | +89.4% | +309.4 to +2825 | LOSS |
| response time (ms), 99th percentile | 3781 | 5703 | +50.9% | +208 to +3637 | LOSS |
| time over the response line (% of samples) | 48.41 | 53.8 | +11.2% | -11.53 to +22.33 | EVEN, inside the noise (up) |
| failed requests (%) | 41.67 | 43.99 | +5.6% | -13.84 to +18.48 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.895 | 11.01 | +11.3% | +0.4948 to +1.736 | power given |
| pods started | 5.71 | 6.774 | +18.6% | +0.2285 to +1.9 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00213 to +0.0009031 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1379 | +0.4% | -6.919 to +18.28 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1379 | +0.4% | -7.025 to +18.2 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.401 | 2.486 | +3.6% | -0.08565 to +0.2563 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73 | 79.51 | +8.9% | +0.9048 to +12.12 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.035 | 3.89 | +28.2% | +0.6585 to +1.051 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

31 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1293 | 2816 | +117.8% | +527.4 to +2519 | LOSS |
| response time (ms), 99th percentile | 3840 | 4726 | +23.1% | -788.1 to +2559 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 51.28 | 47.97 | -6.5% | -22.14 to +15.52 | EVEN, inside the noise (cut) |
| failed requests (%) | 45.65 | 41.36 | -9.4% | -22.56 to +13.97 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.912 | 11.24 | +13.4% | +0.4942 to +2.171 | power given |
| pods started | 5.71 | 7.452 | +30.5% | +0.5631 to +2.921 | power given |
| worker nodes in service, mean | 5.999 | 5.999 | +0.0% | -0.001647 to +0.002453 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1375 | +0.0% | -13.25 to +14.17 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1375 | +0.0% | -13.09 to +14.14 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.437 | +0.4% | -0.1749 to +0.1953 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.8 | 78.69 | +8.1% | -0.2707 to +12.05 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.745 | 4.826 | +28.9% | +0.8684 to +1.293 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
