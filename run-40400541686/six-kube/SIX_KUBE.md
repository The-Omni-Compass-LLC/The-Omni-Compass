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
| response time (ms), 95th percentile | 1494 | 1512 | 1722 | 2122 | 1534 | 2185 | 1882 | 2333 | 1713 | 1898 |
| response time (ms), 99th percentile | 4800 | 3445 | 4080 | 3875 | 4282 | 4037 | 5019 | 4996 | 4872 | 3897 |
| time over the response line (% of samples) | 67.27 | 46.45 | 48.36 | 37.1 | 59.56 | 39.08 | 66.17 | 48.65 | 67.15 | 49.29 |
| failed requests (%) | 59.43 | 40.36 | 38.21 | 29.23 | 53.14 | 27.99 | 58.31 | 42.49 | 60.3 | 43.69 |
| HPA replicas, mean | 9.922 | 11.12 | 9.896 | 10.29 | 9.907 | 11.7 | 9.914 | 11.41 | 9.931 | 10.24 |
| pods started | 4.9 | 6.6 | 5.7 | 6.444 | 5.4 | 7.556 | 5.4 | 7.111 | 5.1 | 7 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 5.996 | 6 | 5.996 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1378 | 1376 | 1370 | 1380 | 1368 | 1387 | 1374 | 1385 | 1376 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1378 | 1376 | 1369 | 1380 | 1367 | 1387 | 1374 | 1385 | 1376 |
| CPU used with Omni's own (cores), mean | 2.633 | 2.473 | 2.444 | 2.395 | 2.489 | 2.388 | 2.575 | 2.423 | 2.561 | 2.461 |
| host CPU busy, the real machine under kind (%) | 77.88 | 75.99 | 73.18 | 77.46 | 75.73 | 75.76 | 78.75 | 78.17 | 77.3 | 78.77 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.29 | 2.79 | 4.4 | 5.056 | 3.02 | 3.578 | 3.5 | 4.3 | 3.91 | 4.9 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1494 | 1512 | +1.2% | -662.1 to +698.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4800 | 3445 | -28.2% | -3448 to +738.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 67.27 | 46.45 | -30.9% | -45.24 to +3.6 | EVEN, inside the noise (cut) |
| failed requests (%) | 59.43 | 40.36 | -32.1% | -45.81 to +7.666 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.922 | 11.12 | +12.0% | -0.2614 to +2.652 | EVEN, inside the noise (up) |
| pods started | 4.9 | 6.6 | +34.7% | -0.7093 to +4.109 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.25e-15 to +3.623e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1378 | -0.9% | -28.59 to +3.624 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1378 | -0.9% | -28.59 to +3.624 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.633 | 2.473 | -6.1% | -0.3802 to +0.061 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.88 | 75.99 | -2.4% | -9.411 to +5.632 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.29 | 2.79 | +21.8% | +0.07481 to +0.9252 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 9

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1864 | 2122 | +13.8% | -1544 to +2060 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4454 | 3875 | -13.0% | -3330 to +2173 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 53.37 | 37.1 | -30.5% | -42.32 to +9.779 | EVEN, inside the noise (cut) |
| failed requests (%) | 42.45 | 29.23 | -31.1% | -45.07 to +18.64 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.899 | 10.29 | +4.0% | -0.5823 to +1.367 | EVEN, inside the noise (up) |
| pods started | 5.556 | 6.444 | +16.0% | -0.5203 to +2.298 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 5.999 | 5.996 | -0.1% | -0.01269 to +0.005311 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1370 | -0.6% | -32.38 to +15.39 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1369 | -0.7% | -33.06 to +14.96 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.475 | 2.395 | -3.3% | -0.3908 to +0.2292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.3 | 77.46 | +4.3% | -6.416 to +12.74 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.456 | 5.056 | +13.5% | +0.08293 to +1.117 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1671 | 2185 | +30.8% | -1554 to +2583 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4707 | 4037 | -14.2% | -3688 to +2349 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 66.1 | 39.08 | -40.9% | -64.19 to +10.16 | EVEN, inside the noise (cut) |
| failed requests (%) | 59.05 | 27.99 | -52.6% | -68.08 to +5.98 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.914 | 11.7 | +18.1% | +0.01421 to +3.566 | power given |
| pods started | 5.222 | 7.556 | +44.7% | +0.3736 to +4.293 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01273 to +0.00503 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1368 | -1.2% | -44.87 to +10.61 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1367 | -1.3% | -44.82 to +9.406 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.556 | 2.388 | -6.6% | -0.5988 to +0.2634 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.82 | 75.76 | -2.6% | -15.81 to +11.69 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.056 | 3.578 | +17.1% | -0.007235 to +1.052 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 1 (pods started), EVEN (inside the noise) on 7

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1876 | 2333 | +24.4% | -1462 to +2376 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4957 | 4996 | +0.8% | -3404 to +3481 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 65 | 48.65 | -25.2% | -53.08 to +20.38 | EVEN, inside the noise (cut) |
| failed requests (%) | 56.79 | 42.49 | -25.2% | -47.15 to +18.55 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.914 | 11.41 | +15.0% | -0.3746 to +3.357 | EVEN, inside the noise (up) |
| pods started | 5.444 | 7.111 | +30.6% | +0.2286 to +3.105 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.087e-16 to +1.096e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1386 | 1374 | -0.8% | -40.89 to +18.11 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1386 | 1374 | -0.8% | -40.89 to +18.11 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.567 | 2.423 | -5.6% | -0.5331 to +0.2455 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.38 | 78.17 | -0.3% | -13.25 to +12.84 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 3.533 | 4.3 | +21.7% | +0.02839 to +1.505 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 9

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1713 | 1898 | +10.8% | -1242 to +1612 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4872 | 3897 | -20.0% | -3655 to +1704 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 67.15 | 49.29 | -26.6% | -52.59 to +16.88 | EVEN, inside the noise (cut) |
| failed requests (%) | 60.3 | 43.69 | -27.6% | -48.52 to +15.29 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.931 | 10.24 | +3.1% | -0.7072 to +1.333 | EVEN, inside the noise (up) |
| pods started | 5.1 | 7 | +37.3% | -0.7217 to +4.522 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003077 to +0.001191 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1376 | -0.6% | -34.5 to +17.13 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1376 | -0.6% | -34.63 to +16.98 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.561 | 2.461 | -3.9% | -0.4411 to +0.2408 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.3 | 78.77 | +1.9% | -10.15 to +13.09 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.91 | 4.9 | +25.3% | +0.4163 to +1.564 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
