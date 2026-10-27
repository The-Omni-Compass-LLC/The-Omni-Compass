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
| response time (ms), 95th percentile | 4019 | 4395 | 3512 | 2825 | 4346 | 3703 | 3833 | 3276 | 3433 | 3314 |
| response time (ms), 99th percentile | 6171 | 6609 | 5931 | 5231 | 6476 | 6100 | 6197 | 5363 | 6231 | 5852 |
| time over the response line (% of samples) | 55.2 | 52.99 | 54.73 | 54.06 | 59.13 | 56.67 | 52.83 | 51.45 | 62.56 | 60.85 |
| failed requests (%) | 39.25 | 42 | 40.89 | 45.37 | 44.08 | 45.97 | 37.85 | 41.43 | 50.84 | 51.97 |
| HPA replicas, mean | 9.809 | 12.8 | 9.8 | 11.83 | 9.804 | 11.75 | 9.797 | 12.1 | 9.82 | 12.15 |
| pods started | 4.1 | 7.66 | 4.46 | 6.52 | 4.18 | 6.58 | 4.4 | 7 | 4.02 | 6.06 |
| worker nodes in service, mean | 6 | 5.997 | 5.999 | 6 | 6 | 5.999 | 6 | 6 | 6 | 5.995 |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.1 | 276.9 | 277.3 | 277.3 | 277.4 | 276.6 | 277 | 277.5 | 277.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277 | 276.9 | 277.3 | 277.3 | 277.4 | 276.6 | 276.9 | 277.5 | 277.6 |
| CPU used with Omni's own (cores), mean | 2.464 | 2.49 | 2.47 | 2.508 | 2.479 | 2.502 | 2.436 | 2.475 | 2.519 | 2.544 |
| host CPU busy, the real machine under kind (%) | 72.98 | 76.93 | 74.81 | 82.32 | 75.77 | 80.6 | 74.81 | 80.63 | 76.52 | 83.53 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.428 | 0.552 | 0.876 | 1.194 | 0.61 | 0.44 | 0.7 | 0.46 | 0.522 | 1.112 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4019 | 4395 | +9.3% | -274.3 to +1026 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6171 | 6609 | +7.1% | -72.66 to +949.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.2 | 52.99 | -4.0% | -3.354 to -1.059 | GAIN |
| failed requests (%) | 39.25 | 42 | +7.0% | +0.4477 to +5.052 | LOSS |
| HPA replicas, mean | 9.809 | 12.8 | +30.5% | +2.33 to +3.651 | power given |
| pods started | 4.1 | 7.66 | +86.8% | +2.764 to +4.356 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.006603 to +0.0008178 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.1 | +0.0% | -0.3902 to +0.5728 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277 | +0.0% | -0.5141 to +0.5217 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.49 | +1.0% | +0.01689 to +0.03384 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.98 | 76.93 | +5.4% | +3.728 to +4.154 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.428 | 0.552 | +29.0% | +0.07088 to +0.1771 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3512 | 2825 | -19.6% | -1306 to -69.54 | GAIN |
| response time (ms), 99th percentile | 5931 | 5231 | -11.8% | -1373 to -27.22 | GAIN |
| time over the response line (% of samples) | 54.73 | 54.06 | -1.2% | -2.441 to +1.111 | EVEN, inside the noise (cut) |
| failed requests (%) | 40.89 | 45.37 | +11.0% | +3.215 to +5.747 | LOSS |
| HPA replicas, mean | 9.8 | 11.83 | +20.8% | +1.515 to +2.552 | power given |
| pods started | 4.46 | 6.52 | +46.2% | +1.198 to +2.922 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005323 to +0.001586 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.3 | +0.1% | -0.08492 to +0.9082 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.3 | +0.2% | -0.06834 to +0.9233 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.508 | +1.6% | +0.02535 to +0.05183 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.81 | 82.32 | +10.0% | +7.199 to +7.826 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.876 | 1.194 | +36.3% | +0.2434 to +0.3926 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4346 | 3703 | -14.8% | -1400 to +114.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6476 | 6100 | -5.8% | -1019 to +268.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 59.13 | 56.67 | -4.2% | -3.477 to -1.45 | GAIN |
| failed requests (%) | 44.08 | 45.97 | +4.3% | +0.5101 to +3.266 | LOSS |
| HPA replicas, mean | 9.804 | 11.75 | +19.8% | +1.33 to +2.555 | power given |
| pods started | 4.18 | 6.58 | +57.4% | +1.47 to +3.33 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001898 to +0.0006369 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.4 | +0.1% | -0.2734 to +0.5681 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.4 | +0.0% | -0.2842 to +0.5405 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.479 | 2.502 | +0.9% | +0.01225 to +0.03359 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.77 | 80.6 | +6.4% | +4.539 to +5.114 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.61 | 0.44 | -27.9% | -0.2239 to -0.1161 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3833 | 3276 | -14.5% | -1382 to +266.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6197 | 5363 | -13.5% | -1511 to -156.6 | GAIN |
| time over the response line (% of samples) | 52.83 | 51.45 | -2.6% | -2.321 to -0.4197 | GAIN |
| failed requests (%) | 37.85 | 41.43 | +9.5% | +2.185 to +4.977 | LOSS |
| HPA replicas, mean | 9.797 | 12.1 | +23.5% | +1.704 to +2.906 | power given |
| pods started | 4.4 | 7 | +59.1% | +1.722 to +3.478 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0007437 to +0.0002496 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277 | +0.1% | -0.09315 to +0.8908 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.9 | +0.1% | -0.09985 to +0.8825 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.436 | 2.475 | +1.6% | +0.02515 to +0.05353 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.81 | 80.63 | +7.8% | +5.481 to +6.16 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7 | 0.46 | -34.3% | -0.3034 to -0.1766 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3433 | 3314 | -3.5% | -637.2 to +398.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6231 | 5852 | -6.1% | -955.8 to +197.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 62.56 | 60.85 | -2.7% | -3.207 to -0.2104 | GAIN |
| failed requests (%) | 50.84 | 51.97 | +2.2% | -0.1974 to +2.451 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.82 | 12.15 | +23.7% | +1.708 to +2.948 | power given |
| pods started | 4.02 | 6.06 | +50.7% | +1.102 to +2.978 | power given |
| worker nodes in service, mean | 6 | 5.995 | -0.1% | -0.01057 to +0.0006048 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.8 | +0.1% | -0.1632 to +0.675 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.6 | +0.0% | -0.3445 to +0.5555 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.519 | 2.544 | +1.0% | +0.01064 to +0.03954 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.52 | 83.53 | +9.2% | +6.63 to +7.374 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.522 | 1.112 | +113.0% | +0.5146 to +0.6654 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
