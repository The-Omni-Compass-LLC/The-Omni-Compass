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
| response time (ms), 95th percentile | 3602 | 4564 | 3762 | 2898 | 4063 | 3617 | 3900 | 3758 | 3333 | 3067 |
| response time (ms), 99th percentile | 5777 | 6300 | 5729 | 5009 | 6360 | 6476 | 6123 | 6228 | 5419 | 5386 |
| time over the response line (% of samples) | 52.22 | 51.34 | 49.44 | 48.01 | 55.43 | 53.67 | 52.77 | 51.13 | 52.51 | 52.68 |
| failed requests (%) | 36.9 | 36.76 | 34.46 | 39.26 | 38.1 | 41.2 | 37.16 | 38.67 | 39.94 | 43.18 |
| HPA replicas, mean | 9.805 | 12.46 | 9.781 | 11.34 | 9.802 | 11.54 | 9.791 | 11.77 | 9.797 | 12.11 |
| pods started | 4.06 | 7.42 | 4.7 | 6.82 | 4.306 | 6.49 | 4.449 | 6.918 | 4.24 | 7.08 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.5 | 275.8 | 276.3 | 276.9 | 277.1 | 276.7 | 276.7 | 276.8 | 277.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.5 | 275.8 | 276.3 | 276.9 | 277.1 | 276.7 | 276.7 | 276.8 | 277.2 |
| CPU used with Omni's own (cores), mean | 2.413 | 2.433 | 2.392 | 2.428 | 2.464 | 2.48 | 2.432 | 2.457 | 2.455 | 2.481 |
| host CPU busy, the real machine under kind (%) | 71.45 | 75.3 | 72.39 | 79.9 | 75.04 | 79.67 | 74.5 | 79.92 | 74.04 | 80.78 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.416 | 0.544 | 0.89 | 1.204 | 0.5653 | 0.4388 | 0.7163 | 0.4265 | 0.488 | 1.074 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3602 | 4564 | +26.7% | +531 to +1392 | LOSS |
| response time (ms), 99th percentile | 5777 | 6300 | +9.1% | +70.39 to +975.4 | LOSS |
| time over the response line (% of samples) | 52.22 | 51.34 | -1.7% | -1.859 to +0.1071 | EVEN, inside the noise (cut) |
| failed requests (%) | 36.9 | 36.76 | -0.4% | -2.406 to +2.135 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.805 | 12.46 | +27.1% | +1.983 to +3.335 | power given |
| pods started | 4.06 | 7.42 | +82.8% | +2.486 to +4.234 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.708e-16 to +1.024e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.5 | +0.1% | -0.2374 to +0.6286 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.5 | +0.1% | -0.2374 to +0.6286 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.413 | 2.433 | +0.8% | +0.01174 to +0.02917 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.45 | 75.3 | +5.4% | +3.536 to +4.162 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.416 | 0.544 | +30.8% | +0.08313 to +0.1729 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3762 | 2898 | -23.0% | -1684 to -44.89 | GAIN |
| response time (ms), 99th percentile | 5729 | 5009 | -12.6% | -1382 to -57.77 | GAIN |
| time over the response line (% of samples) | 49.44 | 48.01 | -2.9% | -3.01 to +0.1453 | EVEN, inside the noise (cut) |
| failed requests (%) | 34.46 | 39.26 | +13.9% | +2.706 to +6.886 | LOSS |
| HPA replicas, mean | 9.781 | 11.34 | +16.0% | +1.057 to +2.063 | power given |
| pods started | 4.7 | 6.82 | +45.1% | +1.275 to +2.965 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.001e-16 to +1.347e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.3 | +0.2% | +0.06625 to +0.9258 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 276.3 | +0.2% | +0.06625 to +0.9258 | power given |
| CPU used with Omni's own (cores), mean | 2.392 | 2.428 | +1.5% | +0.01973 to +0.0521 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.39 | 79.9 | +10.4% | +7.087 to +7.92 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.89 | 1.204 | +35.3% | +0.2402 to +0.3878 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4063 | 3617 | -11.0% | -1290 to +396.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6360 | 6476 | +1.8% | -352.6 to +584.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.43 | 53.67 | -3.2% | -2.991 to -0.5295 | GAIN |
| failed requests (%) | 38.1 | 41.2 | +8.1% | +0.5178 to +5.678 | LOSS |
| HPA replicas, mean | 9.802 | 11.54 | +17.7% | +1.132 to +2.343 | power given |
| pods started | 4.306 | 6.49 | +50.7% | +1.169 to +3.199 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.439e-16 to +7.152e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.1 | +0.1% | -0.1369 to +0.5538 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.1 | +0.1% | -0.1369 to +0.5538 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.48 | +0.6% | +0.003182 to +0.02783 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.04 | 79.67 | +6.2% | +4.21 to +5.04 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5653 | 0.4388 | -22.4% | -0.1789 to -0.07415 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3900 | 3758 | -3.6% | -911.9 to +629.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6123 | 6228 | +1.7% | -466 to +676.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.77 | 51.13 | -3.1% | -2.767 to -0.5297 | GAIN |
| failed requests (%) | 37.16 | 38.67 | +4.1% | -0.2723 to +3.297 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.791 | 11.77 | +20.2% | +1.382 to +2.582 | power given |
| pods started | 4.449 | 6.918 | +55.5% | +1.646 to +3.293 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0006235 to +0.001857 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.7 | -0.0% | -0.4812 to +0.3372 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.7 | -0.0% | -0.4649 to +0.3583 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.432 | 2.457 | +1.0% | +0.01178 to +0.03768 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.5 | 79.92 | +7.3% | +5.062 to +5.763 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7163 | 0.4265 | -40.5% | -0.3393 to -0.2403 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3333 | 3067 | -8.0% | -738.8 to +207.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5419 | 5386 | -0.6% | -491.2 to +424.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 52.51 | 52.68 | +0.3% | -1.608 to +1.963 | EVEN, inside the noise (up) |
| failed requests (%) | 39.94 | 43.18 | +8.1% | +0.8184 to +5.643 | LOSS |
| HPA replicas, mean | 9.797 | 12.11 | +23.6% | +1.703 to +2.922 | power given |
| pods started | 4.24 | 7.08 | +67.0% | +2.046 to +3.634 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.917e-16 to +1.2e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 277.2 | +0.1% | +0.02453 to +0.7148 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 277.2 | +0.1% | +0.02453 to +0.7148 | power given |
| CPU used with Omni's own (cores), mean | 2.455 | 2.481 | +1.1% | +0.0115 to +0.04055 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.04 | 80.78 | +9.1% | +6.367 to +7.109 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.488 | 1.074 | +120.1% | +0.5277 to +0.6443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
