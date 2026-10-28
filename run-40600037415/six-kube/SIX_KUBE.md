# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1609 | 1767 | 1846 | 2733 | 2068 | 2908 | 2085 | 3946 | 1679 | 3428 |
| response time (ms), 99th percentile | 4633 | 4113 | 4020 | 4947 | 4546 | 5174 | 5116 | 6117 | 4203 | 6332 |
| time over the response line (% of samples) | 57.45 | 48.93 | 45.82 | 48.77 | 58.04 | 59.81 | 62.14 | 58.93 | 59.45 | 59.93 |
| failed requests (%) | 49.12 | 43.43 | 40.21 | 41.56 | 50.84 | 51.22 | 54.21 | 49.47 | 53.34 | 52.77 |
| HPA replicas, mean | 9.909 | 10.45 | 9.891 | 10.59 | 9.906 | 10.38 | 9.909 | 11.46 | 9.926 | 11.76 |
| pods started | 5.32 | 5.72 | 5.64 | 6.28 | 5.44 | 5.76 | 5.24 | 7.04 | 5.2 | 7.25 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.998 | 6 | 5.999 | 6 | 5.999 | 5.999 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1373 | 1368 | 1375 | 1379 | 1383 | 1383 | 1380 | 1379 | 1381 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1373 | 1368 | 1374 | 1379 | 1383 | 1383 | 1380 | 1379 | 1381 |
| CPU used with Omni's own (cores), mean | 2.549 | 2.415 | 2.332 | 2.443 | 2.481 | 2.552 | 2.526 | 2.501 | 2.488 | 2.53 |
| host CPU busy, the real machine under kind (%) | 74.87 | 74.55 | 70.55 | 79.75 | 75.81 | 81.19 | 77.35 | 81.39 | 74.86 | 82.03 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.152 | 2.804 | 4.296 | 5.4 | 3.16 | 3.888 | 3.52 | 4.456 | 3.956 | 5.175 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1609 | 1767 | +9.9% | -812.3 to +1130 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4633 | 4113 | -11.2% | -2228 to +1189 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57.45 | 48.93 | -14.8% | -26.53 to +9.498 | EVEN, inside the noise (cut) |
| failed requests (%) | 49.12 | 43.43 | -11.6% | -23.93 to +12.56 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.909 | 10.45 | +5.4% | +0.01114 to +1.063 | power given |
| pods started | 5.32 | 5.72 | +7.5% | -0.6111 to +1.411 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0009297 to +0.0005523 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1373 | -0.8% | -23.57 to +1.969 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1373 | -0.8% | -23.6 to +1.945 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.549 | 2.415 | -5.2% | -0.304 to +0.03704 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.87 | 74.55 | -0.4% | -5.883 to +5.236 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.152 | 2.804 | +30.3% | +0.4181 to +0.8859 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1846 | 2733 | +48.0% | -411.5 to +2185 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4020 | 4947 | +23.1% | -985.5 to +2839 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.82 | 48.77 | +6.4% | -19.22 to +25.13 | EVEN, inside the noise (up) |
| failed requests (%) | 40.21 | 41.56 | +3.4% | -18.64 to +21.33 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.891 | 10.59 | +7.1% | +0.06597 to +1.335 | power given |
| pods started | 5.64 | 6.28 | +11.3% | -0.2587 to +1.539 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.00404 to +0.000788 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1368 | 1375 | +0.5% | -10.26 to +23.76 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1368 | 1374 | +0.5% | -10.52 to +23.52 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.443 | +4.7% | -0.119 to +0.3396 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.55 | 79.75 | +13.0% | +1.751 to +16.64 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.296 | 5.4 | +25.7% | +0.8661 to +1.342 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2068 | 2908 | +40.6% | -417.4 to +2097 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4546 | 5174 | +13.8% | -1133 to +2388 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 58.04 | 59.81 | +3.0% | -15.67 to +19.21 | EVEN, inside the noise (up) |
| failed requests (%) | 50.84 | 51.22 | +0.8% | -15.51 to +16.28 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.906 | 10.38 | +4.8% | +0.02244 to +0.9321 | power given |
| pods started | 5.44 | 5.76 | +5.9% | -0.4021 to +1.042 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001921 to +0.001 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1383 | +0.3% | -8.542 to +16.75 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1383 | +0.3% | -8.583 to +16.65 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.481 | 2.552 | +2.9% | -0.09565 to +0.2381 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.81 | 81.19 | +7.1% | -0.1731 to +10.94 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.16 | 3.888 | +23.0% | +0.4857 to +0.9703 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2085 | 3946 | +89.2% | +565.7 to +3156 | LOSS |
| response time (ms), 99th percentile | 5116 | 6117 | +19.6% | -901.4 to +2904 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 62.14 | 58.93 | -5.2% | -23.58 to +17.17 | EVEN, inside the noise (cut) |
| failed requests (%) | 54.21 | 49.47 | -8.7% | -25.18 to +15.69 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.909 | 11.46 | +15.6% | +0.6754 to +2.418 | power given |
| pods started | 5.24 | 7.04 | +34.4% | +0.7476 to +2.852 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001736 to +2.706e-05 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1380 | -0.2% | -17.78 to +12.1 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1380 | -0.2% | -17.91 to +11.97 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.526 | 2.501 | -1.0% | -0.2244 to +0.1741 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.35 | 81.39 | +5.2% | -2.944 to +11.03 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 3.52 | 4.456 | +26.6% | +0.6174 to +1.255 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1737 | 3428 | +97.4% | +431.5 to +2951 | LOSS |
| response time (ms), 99th percentile | 4360 | 6332 | +45.2% | +251.5 to +3693 | LOSS |
| time over the response line (% of samples) | 61.89 | 59.93 | -3.2% | -19.65 to +15.71 | EVEN, inside the noise (cut) |
| failed requests (%) | 55.57 | 52.77 | -5.0% | -19.01 to +13.42 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.928 | 11.76 | +18.4% | +0.7283 to +2.927 | power given |
| pods started | 5.125 | 7.25 | +41.5% | +0.8409 to +3.409 | power given |
| worker nodes in service, mean | 5.999 | 5.997 | -0.0% | -0.00521 to +0.00173 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1381 | -0.0% | -13.73 to +13.28 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1381 | -0.0% | -13.97 to +13 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.516 | 2.53 | +0.6% | -0.1635 to +0.1921 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.71 | 82.03 | +8.4% | +0.4936 to +12.16 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.971 | 5.175 | +30.3% | +0.8783 to +1.53 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
