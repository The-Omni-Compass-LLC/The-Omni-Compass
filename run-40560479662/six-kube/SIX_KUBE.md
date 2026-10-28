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
| response time (ms), 95th percentile | 1579 | 2100 | 1881 | 3631 | 2310 | 2168 | 2430 | 3436 | 1920 | 2567 |
| response time (ms), 99th percentile | 4165 | 4725 | 4436 | 6030 | 5005 | 4535 | 4848 | 6096 | 4366 | 4831 |
| time over the response line (% of samples) | 53.57 | 56.53 | 52.84 | 57.3 | 55.07 | 50.24 | 59.94 | 63.36 | 54.98 | 50.86 |
| failed requests (%) | 47.82 | 49.34 | 44.84 | 46.88 | 46.08 | 43.94 | 51.89 | 53.52 | 47.53 | 45.24 |
| HPA replicas, mean | 9.899 | 10.69 | 9.895 | 10.13 | 9.901 | 10.55 | 9.908 | 11.1 | 9.919 | 10.79 |
| pods started | 5.52 | 6.04 | 5.56 | 5.84 | 5.52 | 5.96 | 5.32 | 6.125 | 5.44 | 6.28 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1384 | 1375 | 1382 | 1378 | 1376 | 1380 | 1388 | 1378 | 1377 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1384 | 1375 | 1382 | 1378 | 1376 | 1380 | 1387 | 1378 | 1377 |
| CPU used with Omni's own (cores), mean | 2.419 | 2.554 | 2.435 | 2.534 | 2.464 | 2.459 | 2.501 | 2.6 | 2.461 | 2.457 |
| host CPU busy, the real machine under kind (%) | 71.37 | 78.31 | 73.63 | 82.81 | 74.67 | 78.61 | 76.48 | 84.12 | 73.81 | 79.38 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.116 | 2.76 | 4.352 | 5.524 | 3.104 | 3.7 | 3.584 | 4.4 | 3.84 | 5.004 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1579 | 2100 | +33.1% | -545.4 to +1589 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4165 | 4725 | +13.4% | -997.5 to +2117 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.57 | 56.53 | +5.5% | -11.75 to +17.66 | EVEN, inside the noise (up) |
| failed requests (%) | 47.82 | 49.34 | +3.2% | -12.17 to +15.19 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.899 | 10.69 | +8.0% | +0.09989 to +1.483 | power given |
| pods started | 5.52 | 6.04 | +9.4% | -0.5059 to +1.546 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001473 to +0.0001635 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1384 | +0.7% | -2.147 to +21.71 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1384 | +0.7% | -2.259 to +21.63 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.554 | +5.6% | -0.02435 to +0.2941 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.37 | 78.31 | +9.7% | +2.123 to +11.77 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.116 | 2.76 | +30.4% | +0.4456 to +0.8424 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1881 | 3631 | +93.0% | +654.8 to +2845 | LOSS |
| response time (ms), 99th percentile | 4436 | 6030 | +35.9% | -190.7 to +3377 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.84 | 57.3 | +8.4% | -15.26 to +24.17 | EVEN, inside the noise (up) |
| failed requests (%) | 44.84 | 46.88 | +4.6% | -17.55 to +21.63 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.895 | 10.13 | +2.4% | -0.1735 to +0.6444 | EVEN, inside the noise (up) |
| pods started | 5.56 | 5.84 | +5.0% | -0.6393 to +1.199 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001835 to +0.0006373 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1382 | +0.5% | -7.52 to +21.12 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1382 | +0.5% | -7.546 to +20.97 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.435 | 2.534 | +4.1% | -0.09219 to +0.2903 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.63 | 82.81 | +12.5% | +2.878 to +15.49 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.352 | 5.524 | +26.9% | +0.8374 to +1.507 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2310 | 2168 | -6.2% | -1291 to +1006 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5005 | 4535 | -9.4% | -2052 to +1112 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.07 | 50.24 | -8.8% | -22.82 to +13.15 | EVEN, inside the noise (cut) |
| failed requests (%) | 46.08 | 43.94 | -4.7% | -20.14 to +15.86 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 10.55 | +6.6% | +0.1064 to +1.197 | power given |
| pods started | 5.52 | 5.96 | +8.0% | -0.1686 to +1.049 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0004077 to +0.0001416 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1376 | -0.1% | -14.37 to +11.65 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1376 | -0.1% | -14.39 to +11.63 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.459 | -0.2% | -0.1807 to +0.1702 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.67 | 78.61 | +5.3% | -1.728 to +9.61 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.104 | 3.7 | +19.2% | +0.4093 to +0.7827 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 8

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2520 | 3436 | +36.4% | -468.2 to +2302 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5033 | 6096 | +21.1% | -736.4 to +2862 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 62.42 | 63.36 | +1.5% | -12.39 to +14.27 | EVEN, inside the noise (up) |
| failed requests (%) | 54.05 | 53.52 | -1.0% | -11.87 to +10.82 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.91 | 11.1 | +12.0% | +0.4129 to +1.974 | power given |
| pods started | 5.25 | 6.125 | +16.7% | -0.09219 to +1.842 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008646 to +0.0001944 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1388 | +0.4% | -6.907 to +16.83 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1387 | +0.4% | -6.962 to +16.79 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.53 | 2.6 | +2.8% | -0.08716 to +0.2281 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.41 | 84.12 | +8.7% | +1.868 to +11.54 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 3.613 | 4.4 | +21.8% | +0.5045 to +1.07 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 8

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1920 | 2567 | +33.7% | -512.6 to +1806 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4366 | 4831 | +10.6% | -1173 to +2102 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.98 | 50.86 | -7.5% | -21.49 to +13.26 | EVEN, inside the noise (cut) |
| failed requests (%) | 47.53 | 45.24 | -4.8% | -18.98 to +14.4 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.919 | 10.79 | +8.8% | +0.04448 to +1.694 | power given |
| pods started | 5.44 | 6.28 | +15.4% | -0.1689 to +1.849 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001493 to +0.0004054 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1377 | -0.0% | -14.69 to +13.32 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1377 | -0.1% | -14.77 to +13.24 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.461 | 2.457 | -0.2% | -0.1879 to +0.1796 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.81 | 79.38 | +7.5% | -0.1983 to +11.33 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.84 | 5.004 | +30.3% | +0.8748 to +1.453 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
