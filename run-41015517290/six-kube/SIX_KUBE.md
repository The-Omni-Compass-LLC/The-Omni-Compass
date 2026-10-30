# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4057 | 4633 | 4200 | 3124 | 4164 | 4366 | 3684 | 4126 | 3381 | 2894 |
| response time (ms), 99th percentile | 6302 | 6623 | 6372 | 5500 | 6738 | 6957 | 5826 | 5945 | 5448 | 5357 |
| time over the response line (% of samples) | 53.88 | 52.37 | 56.99 | 55.67 | 62.05 | 58.9 | 53.97 | 52.39 | 51.28 | 51.23 |
| failed requests (%) | 37.06 | 37.98 | 40.55 | 46.3 | 45.8 | 45.99 | 39.65 | 41.01 | 38.32 | 41.77 |
| HPA replicas, mean | 9.802 | 12.56 | 9.834 | 11.99 | 9.841 | 11.8 | 9.821 | 11.58 | 9.787 | 12.07 |
| pods started | 4.12 | 7.04 | 3.612 | 6.191 | 3.48 | 5.417 | 3.82 | 6.16 | 4.49 | 6.958 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.2 | 277.2 | 277.6 | 277.4 | 277.2 | 276.3 | 276.2 | 276.4 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.2 | 277.2 | 277.6 | 277.4 | 277.2 | 276.3 | 276.2 | 276.4 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.463 | 2.482 | 2.478 | 2.503 | 2.49 | 2.497 | 2.41 | 2.432 | 2.438 | 2.464 |
| host CPU busy, the real machine under kind (%) | 72.8 | 76.42 | 75.32 | 82.4 | 76.42 | 80.55 | 74.42 | 79.66 | 73.47 | 80.13 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.408 | 0.51 | 0.8939 | 1.189 | 0.592 | 0.4646 | 0.736 | 0.426 | 0.5163 | 1.06 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4057 | 4633 | +14.2% | +54.1 to +1098 | LOSS |
| response time (ms), 99th percentile | 6302 | 6623 | +5.1% | -29.19 to +671.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.88 | 52.37 | -2.8% | -2.599 to -0.4302 | GAIN |
| failed requests (%) | 37.06 | 37.98 | +2.5% | -1.037 to +2.886 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.802 | 12.56 | +28.2% | +2.073 to +3.448 | power given |
| pods started | 4.12 | 7.04 | +70.9% | +2.139 to +3.701 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.449e-16 to +2.607e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.2 | +0.1% | -0.2154 to +0.6111 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.2 | +0.1% | -0.2154 to +0.6111 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.463 | 2.482 | +0.8% | +0.01159 to +0.02597 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.8 | 76.42 | +5.0% | +3.43 to +3.795 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.408 | 0.51 | +25.0% | +0.06369 to +0.1403 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

46 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4179 | 3143 | -24.8% | -1778 to -294.1 | GAIN |
| response time (ms), 99th percentile | 6326 | 5435 | -14.1% | -1474 to -309.6 | GAIN |
| time over the response line (% of samples) | 55.6 | 55.24 | -0.7% | -2.061 to +1.331 | EVEN, inside the noise (cut) |
| failed requests (%) | 39.31 | 45.8 | +16.5% | +4.326 to +8.658 | LOSS |
| HPA replicas, mean | 9.825 | 11.98 | +21.9% | +1.642 to +2.661 | power given |
| pods started | 3.804 | 6.217 | +63.4% | +1.496 to +3.33 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.4e-16 to +1.096e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 277.5 | +0.1% | +0.003029 to +0.8257 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.1 | 277.5 | +0.1% | +0.003029 to +0.8257 | power given |
| CPU used with Omni's own (cores), mean | 2.468 | 2.5 | +1.3% | +0.01542 to +0.04721 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.95 | 82.29 | +9.8% | +6.931 to +7.754 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.8957 | 1.189 | +32.8% | +0.219 to +0.3679 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

48 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4147 | 4366 | +5.3% | -555.9 to +993 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6720 | 6957 | +3.5% | -225 to +698.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 61.3 | 58.9 | -3.9% | -3.129 to -1.67 | GAIN |
| failed requests (%) | 45.21 | 45.99 | +1.7% | -1.301 to +2.875 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.84 | 11.8 | +19.9% | +1.32 to +2.595 | power given |
| pods started | 3.5 | 5.417 | +54.8% | +1.109 to +2.724 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.841e-16 to +1.074e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.2 | -0.0% | -0.5281 to +0.363 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.2 | -0.0% | -0.5281 to +0.363 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.497 | +0.5% | +0.000994 to +0.02337 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.22 | 80.55 | +5.7% | +4.048 to +4.621 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5938 | 0.4646 | -21.8% | -0.1972 to -0.06114 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3684 | 4126 | +12.0% | -228.1 to +1113 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5826 | 5945 | +2.0% | -441.3 to +679.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.97 | 52.39 | -2.9% | -2.46 to -0.7119 | GAIN |
| failed requests (%) | 39.65 | 41.01 | +3.4% | -0.3212 to +3.048 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.821 | 11.58 | +17.9% | +1.22 to +2.294 | power given |
| pods started | 3.82 | 6.16 | +61.3% | +1.458 to +3.222 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.891e-17 to +7.639e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.2 | -0.1% | -0.4887 to +0.1907 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | -0.1% | -0.4887 to +0.1907 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.41 | 2.432 | +0.9% | +0.01092 to +0.03322 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.42 | 79.66 | +7.0% | +4.962 to +5.526 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.736 | 0.426 | -42.1% | -0.3652 to -0.2548 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

47 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3302 | 2832 | -14.2% | -907.4 to -31.64 | GAIN |
| response time (ms), 99th percentile | 5384 | 5285 | -1.8% | -460.3 to +261.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 50.14 | 50.73 | +1.2% | -1.278 to +2.463 | EVEN, inside the noise (up) |
| failed requests (%) | 37.3 | 41.21 | +10.5% | +1.337 to +6.478 | LOSS |
| HPA replicas, mean | 9.783 | 12.04 | +23.0% | +1.597 to +2.908 | power given |
| pods started | 4.553 | 7 | +53.7% | +1.424 to +3.469 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.538e-17 to +1.048e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.7 | +0.2% | -0.01126 to +0.8871 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.7 | +0.2% | -0.01126 to +0.8871 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.46 | +1.2% | +0.01379 to +0.04657 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.18 | 79.99 | +9.3% | +6.411 to +7.217 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5064 | 1.06 | +109.2% | +0.4845 to +0.6219 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
