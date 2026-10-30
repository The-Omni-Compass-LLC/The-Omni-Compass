# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1639 | 2558 | 2590 | 3056 | 2603 | 3050 | 3151 | 4300 |
| response time (ms), 99th percentile | 3876 | 4999 | 5625 | 5947 | 5350 | 5260 | 5635 | 7218 |
| time over the response line (% of samples) | 43.44 | 39.12 | 43.92 | 38.01 | 47.47 | 43.03 | 45.97 | 42.96 |
| failed requests (%) | 25.77 | 23.39 | 27.38 | 26.49 | 29.11 | 28.38 | 21.22 | 21.86 |
| HPA replicas, mean | 9.701 | 13.03 | 9.644 | 12.05 | 9.676 | 12.96 | 9.688 | 12.12 |
| pods started | 4.391 | 8.273 | 5 | 7.522 | 4.739 | 8.261 | 4.652 | 6.652 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.3 | 184.3 | 185.2 | 183.8 | 184.2 | 184.9 | 185.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.3 | 184.3 | 185.2 | 183.8 | 184.2 | 184.9 | 185.7 |
| CPU used with Omni's own (cores), mean | 2.36 | 2.371 | 2.408 | 2.427 | 2.379 | 2.388 | 2.461 | 2.478 |
| host CPU busy, the real machine under kind (%) | 69.48 | 70.49 | 71.19 | 72.25 | 69.9 | 71.23 | 73.12 | 75.91 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.004348 | 0.009091 | 0.004348 | 0.01739 | 0.004348 | 0.004348 | 0.1435 | 0.1739 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

22 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1655 | 2558 | +54.6% | +378.8 to +1428 | LOSS |
| response time (ms), 99th percentile | 3852 | 4999 | +29.8% | +226.6 to +2068 | LOSS |
| time over the response line (% of samples) | 42.86 | 39.12 | -8.7% | -6.048 to -1.416 | GAIN |
| failed requests (%) | 25.1 | 23.39 | -6.8% | -2.981 to -0.4347 | GAIN |
| HPA replicas, mean | 9.693 | 13.03 | +34.5% | +2.264 to +4.415 | power given |
| pods started | 4.5 | 8.273 | +83.8% | +2.588 to +4.957 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.761e-16 to +2.531e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.3 | +0.3% | -0.139 to +1.302 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.3 | +0.3% | -0.139 to +1.302 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.348 | 2.371 | +1.0% | +0.01331 to +0.03227 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.13 | 70.49 | +2.0% | +1.093 to +1.616 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.004545 | 0.009091 | +100.0% | -0.01209 to +0.02118 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2590 | 3056 | +18.0% | -370.4 to +1303 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5625 | 5947 | +5.7% | -786.3 to +1431 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 43.92 | 38.01 | -13.4% | -7.914 to -3.899 | GAIN |
| failed requests (%) | 27.38 | 26.49 | -3.3% | -1.833 to +0.05265 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 12.05 | +24.9% | +1.426 to +3.378 | power given |
| pods started | 5 | 7.522 | +50.4% | +1.106 to +3.937 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.066e-16 to +5.383e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 185.2 | +0.5% | +0.3061 to +1.357 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 185.2 | +0.5% | +0.3061 to +1.357 | power given |
| CPU used with Omni's own (cores), mean | 2.408 | 2.427 | +0.8% | +0.006654 to +0.03225 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.19 | 72.25 | +1.5% | +0.6644 to +1.457 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.004348 | 0.01739 | +300.0% | -0.00675 to +0.03284 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2603 | 3050 | +17.2% | -440.5 to +1336 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5350 | 5260 | -1.7% | -1071 to +891.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 47.47 | 43.03 | -9.4% | -6.331 to -2.55 | GAIN |
| failed requests (%) | 29.11 | 28.38 | -2.5% | -1.788 to +0.3307 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.676 | 12.96 | +33.9% | +2.2 to +4.36 | power given |
| pods started | 4.739 | 8.261 | +74.3% | +2.143 to +4.901 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.603e-17 to +6.067e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.2 | +0.2% | -0.5882 to +1.254 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.2 | +0.2% | -0.5882 to +1.254 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.379 | 2.388 | +0.4% | +0.002157 to +0.01627 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.9 | 71.23 | +1.9% | +1.093 to +1.568 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.004348 | 0.004348 | +0.0% | -0.01304 to +0.01304 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3151 | 4300 | +36.4% | +417.5 to +1879 | LOSS |
| response time (ms), 99th percentile | 5635 | 7218 | +28.1% | +672.9 to +2493 | LOSS |
| time over the response line (% of samples) | 45.97 | 42.96 | -6.5% | -4.955 to -1.051 | GAIN |
| failed requests (%) | 21.22 | 21.86 | +3.0% | -1.037 to +2.319 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.688 | 12.12 | +25.1% | +1.464 to +3.405 | power given |
| pods started | 4.652 | 6.652 | +43.0% | +0.7768 to +3.223 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.579e-16 to +4.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 185.7 | +0.4% | +0.1655 to +1.46 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 185.7 | +0.4% | +0.1655 to +1.46 | power given |
| CPU used with Omni's own (cores), mean | 2.461 | 2.478 | +0.7% | +0.005299 to +0.02891 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.12 | 75.91 | +3.8% | +2.337 to +3.246 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1435 | 0.1739 | +21.2% | -0.007434 to +0.0683 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
