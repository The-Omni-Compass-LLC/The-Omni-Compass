# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3973 | 4531 | 3477 | 2773 | 3709 | 2606 | 3782 | 3075 | 3899 | 2354 |
| response time (ms), 99th percentile | 6059 | 6763 | 6091 | 5433 | 5961 | 5044 | 5978 | 5429 | 6072 | 5092 |
| time over the response line (% of samples) | 53.82 | 52.86 | 58.73 | 58.57 | 52.83 | 52.28 | 55.39 | 54.97 | 60.56 | 59.96 |
| failed requests (%) | 37.8 | 40.93 | 44.69 | 49.39 | 39.59 | 44.92 | 41.29 | 46.05 | 48.61 | 53.29 |
| HPA replicas, mean | 9.784 | 12.71 | 9.817 | 12.07 | 9.782 | 12.3 | 9.812 | 12.43 | 9.817 | 12.87 |
| pods started | 4.7 | 7.58 | 4.16 | 6.9 | 4.7 | 7.5 | 4.18 | 7.48 | 4.26 | 6.68 |
| worker nodes in service, mean | 6 | 5.989 | 5.999 | 5.999 | 6 | 5.997 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 277.1 | 277.5 | 277.7 | 276.4 | 276.7 | 277 | 277.1 | 277.3 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.7 | 277.5 | 277.7 | 276.4 | 276.6 | 277 | 277.1 | 277.3 | 277.3 |
| CPU used with Omni's own (cores), mean | 2.443 | 2.47 | 2.506 | 2.552 | 2.421 | 2.463 | 2.453 | 2.494 | 2.492 | 2.534 |
| host CPU busy, the real machine under kind (%) | 72.37 | 76.42 | 76.28 | 84.15 | 74.09 | 79.15 | 75.54 | 81.31 | 76.05 | 83.27 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.422 | 0.552 | 0.916 | 1.216 | 0.584 | 0.422 | 0.728 | 0.468 | 0.494 | 1.114 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3973 | 4531 | +14.0% | +163.1 to +952.8 | LOSS |
| response time (ms), 99th percentile | 6059 | 6763 | +11.6% | +283.6 to +1125 | LOSS |
| time over the response line (% of samples) | 53.82 | 52.86 | -1.8% | -1.847 to -0.06864 | GAIN |
| failed requests (%) | 37.8 | 40.93 | +8.3% | +1.371 to +4.887 | LOSS |
| HPA replicas, mean | 9.784 | 12.71 | +29.9% | +2.251 to +3.594 | power given |
| pods started | 4.7 | 7.58 | +61.3% | +2.102 to +3.658 | power given |
| worker nodes in service, mean | 6 | 5.989 | -0.2% | -0.02956 to +0.007675 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 277.1 | +0.2% | -0.2711 to +1.443 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.7 | +0.1% | -0.5166 to +0.988 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.443 | 2.47 | +1.1% | +0.007655 to +0.04603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.37 | 76.42 | +5.6% | +3.807 to +4.287 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.422 | 0.552 | +30.8% | +0.06151 to +0.1985 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3477 | 2773 | -20.2% | -1308 to -99.37 | GAIN |
| response time (ms), 99th percentile | 6091 | 5433 | -10.8% | -1297 to -17.01 | GAIN |
| time over the response line (% of samples) | 58.73 | 58.57 | -0.3% | -1.66 to +1.336 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.69 | 49.39 | +10.5% | +3.465 to +5.941 | LOSS |
| HPA replicas, mean | 9.817 | 12.07 | +22.9% | +1.776 to +2.723 | power given |
| pods started | 4.16 | 6.9 | +65.9% | +2.032 to +3.448 | power given |
| worker nodes in service, mean | 5.999 | 5.999 | +0.0% | -0.002195 to +0.002438 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.7 | +0.1% | -0.5945 to +1.036 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.7 | +0.1% | -0.6349 to +1.084 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.552 | +1.8% | +0.02772 to +0.06406 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.28 | 84.15 | +10.3% | +7.462 to +8.277 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.916 | 1.216 | +32.8% | +0.2188 to +0.3812 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3709 | 2606 | -29.7% | -1773 to -432.3 | GAIN |
| response time (ms), 99th percentile | 5961 | 5044 | -15.4% | -1532 to -302.1 | GAIN |
| time over the response line (% of samples) | 52.83 | 52.28 | -1.0% | -1.56 to +0.4591 | EVEN, inside the noise (cut) |
| failed requests (%) | 39.59 | 44.92 | +13.5% | +3.548 to +7.116 | LOSS |
| HPA replicas, mean | 9.782 | 12.3 | +25.8% | +1.986 to +3.055 | power given |
| pods started | 4.7 | 7.5 | +59.6% | +1.782 to +3.818 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.007622 to +0.0006912 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.7 | +0.1% | -0.2243 to +0.7379 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.6 | +0.1% | -0.3734 to +0.6778 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.421 | 2.463 | +1.7% | +0.02907 to +0.05407 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.09 | 79.15 | +6.8% | +4.727 to +5.41 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.584 | 0.422 | -27.7% | -0.2203 to -0.1037 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3782 | 3075 | -18.7% | -1405 to -9.043 | GAIN |
| response time (ms), 99th percentile | 5978 | 5429 | -9.2% | -1266 to +169.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.39 | 54.97 | -0.7% | -1.367 to +0.5357 | EVEN, inside the noise (cut) |
| failed requests (%) | 41.29 | 46.05 | +11.5% | +2.985 to +6.54 | LOSS |
| HPA replicas, mean | 9.812 | 12.43 | +26.6% | +2.07 to +3.156 | power given |
| pods started | 4.18 | 7.48 | +78.9% | +2.45 to +4.15 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002751 to +0.001702 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.1 | +0.0% | -0.5129 to +0.6098 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.1 | +0.0% | -0.5377 to +0.603 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.453 | 2.494 | +1.7% | +0.02799 to +0.05315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.54 | 81.31 | +7.6% | +5.484 to +6.039 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.728 | 0.468 | -35.7% | -0.3239 to -0.1961 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3899 | 2354 | -39.6% | -2169 to -922.1 | GAIN |
| response time (ms), 99th percentile | 6072 | 5092 | -16.1% | -1675 to -284.7 | GAIN |
| time over the response line (% of samples) | 60.56 | 59.96 | -1.0% | -1.933 to +0.7435 | EVEN, inside the noise (cut) |
| failed requests (%) | 48.61 | 53.29 | +9.6% | +3.259 to +6.107 | LOSS |
| HPA replicas, mean | 9.817 | 12.87 | +31.1% | +2.571 to +3.539 | power given |
| pods started | 4.26 | 6.68 | +56.8% | +1.637 to +3.203 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002839 to +0.0009526 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.4 | +0.0% | -0.8784 to +0.9533 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.3 | +0.0% | -0.9121 to +0.9303 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.492 | 2.534 | +1.7% | +0.0257 to +0.05946 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.05 | 83.27 | +9.5% | +6.837 to +7.587 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.494 | 1.114 | +125.5% | +0.5568 to +0.6832 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
