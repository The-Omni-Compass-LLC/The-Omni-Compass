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
| response time (ms), 95th percentile | 3625 | 3491 | 4145 | 3161 | 2846 | 2122 | 2153 | 1800 | 2736 | 5180 |
| response time (ms), 99th percentile | 5755 | 5515 | 6008 | 5229 | 5395 | 4828 | 3660 | 3843 | 4514 | 7576 |
| time over the response line (% of samples) | 57.38 | 56.73 | 69.81 | 67.96 | 47.48 | 47.21 | 34.06 | 34 | 64.57 | 63.84 |
| failed requests (%) | 44.47 | 47.7 | 54.62 | 59.01 | 36.05 | 40.31 | 23.93 | 27.26 | 53.07 | 49.53 |
| HPA replicas, mean | 9.811 | 12.66 | 9.824 | 10.57 | 9.808 | 11.9 | 9.771 | 12.55 | 9.809 | 11.52 |
| pods started | 4.2 | 10 | 3.8 | 5.9 | 3.8 | 8.8 | 4.7 | 14 | 4.4 | 6.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.9 | 277.8 | 277.9 | 275.1 | 275.6 | 273.2 | 273.6 | 278.6 | 278.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.9 | 277.8 | 277.9 | 275.1 | 275.6 | 273.2 | 273.6 | 278.6 | 278.5 |
| CPU used with Omni's own (cores), mean | 2.449 | 2.505 | 2.548 | 2.574 | 2.351 | 2.395 | 2.213 | 2.287 | 2.557 | 2.609 |
| host CPU busy, the real machine under kind (%) | 72.76 | 77.58 | 77.95 | 85.89 | 72.37 | 77.85 | 68.24 | 75.4 | 77.37 | 84.75 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.44 | 0.5 | 0.87 | 1.29 | 0.58 | 0.43 | 0.72 | 0.45 | 0.54 | 1.22 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3625 | 3491 | -3.7% | -2409 to +2141 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5755 | 5515 | -4.2% | -2515 to +2036 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57.38 | 56.73 | -1.1% | -3.914 to +2.609 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.47 | 47.7 | +7.3% | -3.314 to +9.771 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.811 | 12.66 | +29.1% | +1.763 to +3.939 | power given |
| pods started | 4.2 | 10 | +138.1% | +2.864 to +8.736 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.262e-15 to +7.291e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.9 | -0.0% | -1.035 to +1 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.9 | -0.0% | -1.035 to +1 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.449 | 2.505 | +2.3% | +0.01764 to +0.09498 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.76 | 77.58 | +6.6% | +3.768 to +5.862 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.44 | 0.5 | +13.6% | -0.02396 to +0.144 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4145 | 3161 | -23.7% | -2198 to +230.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6008 | 5229 | -13.0% | -2260 to +702.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 69.81 | 67.96 | -2.7% | -5.003 to +1.303 | EVEN, inside the noise (cut) |
| failed requests (%) | 54.62 | 59.01 | +8.0% | -0.9391 to +9.709 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.824 | 10.57 | +7.6% | -0.2843 to +1.779 | EVEN, inside the noise (up) |
| pods started | 3.8 | 5.9 | +55.3% | +0.3014 to +3.899 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.544e-15 to +1.188e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 277.9 | +0.0% | -0.867 to +1.112 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 277.9 | +0.0% | -0.867 to +1.112 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.548 | 2.574 | +1.0% | -0.01401 to +0.06565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.95 | 85.89 | +10.2% | +6.853 to +9.029 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.87 | 1.29 | +48.3% | +0.1727 to +0.6673 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2846 | 2122 | -25.4% | -1739 to +292.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5395 | 4828 | -10.5% | -1777 to +642.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 47.48 | 47.21 | -0.6% | -2.525 to +1.987 | EVEN, inside the noise (cut) |
| failed requests (%) | 36.05 | 40.31 | +11.8% | +1.118 to +7.402 | LOSS |
| HPA replicas, mean | 9.808 | 11.9 | +21.3% | +0.4504 to +3.73 | power given |
| pods started | 3.8 | 8.8 | +131.6% | +2.261 to +7.739 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.057e-15 to +8.793e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.6 | +0.2% | -0.2663 to +1.373 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 275.6 | +0.2% | -0.2663 to +1.373 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.351 | 2.395 | +1.9% | +0.01052 to +0.07879 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.37 | 77.85 | +7.6% | +4.523 to +6.449 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.58 | 0.43 | -25.9% | -0.3054 to +0.005441 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2153 | 1800 | -16.4% | -1708 to +1002 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3660 | 3843 | +5.0% | -1324 to +1690 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 34.06 | 34 | -0.2% | -0.9661 to +0.8421 | EVEN, inside the noise (cut) |
| failed requests (%) | 23.93 | 27.26 | +13.9% | -0.4241 to +7.085 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.771 | 12.55 | +28.5% | +1.356 to +4.204 | power given |
| pods started | 4.7 | 14 | +197.9% | +4.775 to +13.82 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.108e-15 to +1.641e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.6 | +0.1% | -0.7534 to +1.508 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 273.6 | +0.1% | -0.7534 to +1.508 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.213 | 2.287 | +3.4% | +0.02751 to +0.1212 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.24 | 75.4 | +10.5% | +5.85 to +8.466 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.72 | 0.45 | -37.5% | -0.4319 to -0.1081 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2736 | 5180 | +89.3% | +675.6 to +4212 | LOSS |
| response time (ms), 99th percentile | 4514 | 7576 | +67.8% | +1100 to +5025 | LOSS |
| time over the response line (% of samples) | 64.57 | 63.84 | -1.1% | -3.227 to +1.772 | EVEN, inside the noise (cut) |
| failed requests (%) | 53.07 | 49.53 | -6.7% | -8.837 to +1.761 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.809 | 11.52 | +17.4% | +0.3684 to +3.048 | power given |
| pods started | 4.4 | 6.8 | +54.5% | -0.3228 to +5.123 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.556e-15 to +1.556e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 278.6 | 278.5 | -0.0% | -0.8695 to +0.7056 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.6 | 278.5 | -0.0% | -0.8695 to +0.7056 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.557 | 2.609 | +2.0% | +0.001678 to +0.102 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.37 | 84.75 | +9.5% | +5.793 to +8.958 | shown, not judged |
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
