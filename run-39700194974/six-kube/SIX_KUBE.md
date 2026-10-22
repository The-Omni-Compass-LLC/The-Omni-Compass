# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2537 | 3350 | 3944 | 2714 | 4170 | 3848 | 4167 | 4316 | 5513 | 3257 |
| response time (ms), 99th percentile | 4353 | 4324 | 6451 | 5174 | 5999 | 5292 | 6578 | 6750 | 8148 | 6339 |
| time over the response line (% of samples) | 38.16 | 37.5 | 59.69 | 57.49 | 51.67 | 50.29 | 59.95 | 60.56 | 69.34 | 67.73 |
| failed requests (%) | 29.46 | 28.25 | 45.13 | 49.27 | 37.45 | 40.59 | 44.17 | 50.27 | 55.37 | 59.23 |
| HPA replicas, mean | 9.777 | 12.63 | 9.835 | 11.47 | 9.779 | 12 | 9.819 | 12.27 | 9.854 | 12.51 |
| pods started | 4.5 | 7.4 | 3.5 | 5.889 | 4.6 | 8.1 | 4.2 | 6.6 | 3.2 | 5.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 5.998 | 5.997 | 6 | 6 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | 277.3 | 276.9 | 275.3 | 275.7 | 278.3 | 278.5 | 277.8 | 278.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273 | 277.3 | 276.9 | 275.3 | 275.6 | 278.3 | 278.5 | 277.8 | 278.8 |
| CPU used with Omni's own (cores), mean | 2.214 | 2.233 | 2.475 | 2.491 | 2.381 | 2.412 | 2.534 | 2.562 | 2.541 | 2.551 |
| host CPU busy, the real machine under kind (%) | 65.91 | 69.13 | 75.54 | 82.11 | 72.89 | 77.51 | 77.91 | 83.39 | 77.95 | 84.55 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.38 | 0.51 | 0.94 | 1.178 | 0.74 | 0.46 | 0.74 | 0.4 | 0.54 | 1.22 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2537 | 3350 | +32.1% | -911.5 to +2539 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4353 | 4324 | -0.7% | -1294 to +1236 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 38.16 | 37.5 | -1.7% | -2.544 to +1.231 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.46 | 28.25 | -4.1% | -4.149 to +1.747 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.777 | 12.63 | +29.2% | +1.078 to +4.624 | power given |
| pods started | 4.5 | 7.4 | +64.4% | +0.8642 to +4.936 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.787e-15 to -3.445e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | -0.1% | -1.408 to +0.761 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273 | -0.1% | -1.408 to +0.761 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.214 | 2.233 | +0.8% | -0.01613 to +0.05339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.91 | 69.13 | +4.9% | +2.109 to +4.342 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.38 | 0.51 | +34.2% | +0.008188 to +0.2518 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3794 | 2714 | -28.5% | -2865 to +704 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6115 | 5174 | -15.4% | -2369 to +485.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57.69 | 57.49 | -0.3% | -3.068 to +2.665 | EVEN, inside the noise (cut) |
| failed requests (%) | 42.78 | 49.27 | +15.2% | +2.532 to +10.46 | LOSS |
| HPA replicas, mean | 9.817 | 11.47 | +16.9% | +0.417 to +2.895 | power given |
| pods started | 3.889 | 5.889 | +51.4% | +0.562 to +3.438 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.339e-15 to +3.313e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 276.9 | -0.1% | -1.28 to +0.834 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.1 | 276.9 | -0.1% | -1.28 to +0.834 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.457 | 2.491 | +1.4% | +0.006719 to +0.06242 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.93 | 82.11 | +9.6% | +6.493 to +7.864 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.9556 | 1.178 | +23.3% | -0.04894 to +0.4934 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4170 | 3848 | -7.7% | -2742 to +2097 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5999 | 5292 | -11.8% | -2688 to +1274 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 51.67 | 50.29 | -2.7% | -3.051 to +0.2988 | EVEN, inside the noise (cut) |
| failed requests (%) | 37.45 | 40.59 | +8.4% | -0.9096 to +7.188 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.779 | 12 | +22.7% | +0.7018 to +3.745 | power given |
| pods started | 4.6 | 8.1 | +76.1% | +1.361 to +5.639 | power given |
| worker nodes in service, mean | 5.998 | 5.997 | -0.0% | -0.009967 to +0.006953 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 275.7 | +0.1% | -0.459 to +1.231 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 275.6 | +0.1% | -0.6668 to +1.347 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.381 | 2.412 | +1.3% | -0.001502 to +0.06337 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.89 | 77.51 | +6.3% | +3.454 to +5.784 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.74 | 0.46 | -37.8% | -0.4641 to -0.09593 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4167 | 4316 | +3.6% | -2249 to +2546 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6578 | 6750 | +2.6% | -1459 to +1803 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.95 | 60.56 | +1.0% | -1.263 to +2.472 | EVEN, inside the noise (up) |
| failed requests (%) | 44.17 | 50.27 | +13.8% | +1.397 to +10.79 | LOSS |
| HPA replicas, mean | 9.819 | 12.27 | +24.9% | +1.272 to +3.626 | power given |
| pods started | 4.2 | 6.6 | +57.1% | +0.8474 to +3.953 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.108e-16 to +1.066e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 278.5 | +0.1% | -0.8478 to +1.251 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.3 | 278.5 | +0.1% | -0.8478 to +1.251 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.534 | 2.562 | +1.1% | +0.004301 to +0.05041 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.91 | 83.39 | +7.0% | +4.891 to +6.071 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.74 | 0.4 | -45.9% | -0.4477 to -0.2323 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5513 | 3257 | -40.9% | -4128 to -384.7 | GAIN |
| response time (ms), 99th percentile | 8148 | 6339 | -22.2% | -3141 to -478.3 | GAIN |
| time over the response line (% of samples) | 69.34 | 67.73 | -2.3% | -4.172 to +0.9619 | EVEN, inside the noise (cut) |
| failed requests (%) | 55.37 | 59.23 | +7.0% | -0.009388 to +7.723 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.854 | 12.51 | +27.0% | +1.347 to +3.966 | power given |
| pods started | 3.2 | 5.6 | +75.0% | +0.7758 to +4.024 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005601 to +0.002167 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 278.8 | +0.4% | +0.3048 to +1.788 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 278.8 | +0.4% | +0.1864 to +1.802 | power given |
| CPU used with Omni's own (cores), mean | 2.541 | 2.551 | +0.4% | -0.009799 to +0.02965 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.95 | 84.55 | +8.5% | +6.42 to +6.79 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.54 | 1.22 | +125.9% | +0.4065 to +0.9535 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
