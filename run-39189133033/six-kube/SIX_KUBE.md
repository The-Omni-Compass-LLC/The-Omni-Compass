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
| response time (ms), 95th percentile | 3689 | 4471 | 3201 | 3382 | 3496 | 3174 | 2902 | 3197 | 3093 | 2617 |
| response time (ms), 99th percentile | 6156 | 7144 | 5668 | 5848 | 5756 | 5667 | 5266 | 5266 | 5718 | 5101 |
| time over the response line (% of samples) | 59.78 | 58.1 | 49.99 | 51.69 | 52.85 | 52.46 | 54.67 | 54.95 | 53.74 | 54.5 |
| failed requests (%) | 44.44 | 44.93 | 32.02 | 38.61 | 38.82 | 44.21 | 43.18 | 46.12 | 40.96 | 45.21 |
| HPA replicas, mean | 9.821 | 13.03 | 9.803 | 12.54 | 9.79 | 12.23 | 9.786 | 11.98 | 9.77 | 12.84 |
| pods started | 3.889 | 7.444 | 4.4 | 7.3 | 4.7 | 8.5 | 4.5 | 6.1 | 5.2 | 7.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 5.997 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 277.9 | 276.6 | 278 | 276.6 | 277.5 | 275.5 | 275.5 | 277.3 | 277.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.3 | 277.9 | 276.6 | 277.9 | 276.6 | 277.4 | 275.5 | 275.5 | 277.3 | 277.2 |
| CPU used with Omni's own (cores), mean | 2.512 | 2.539 | 2.455 | 2.518 | 2.453 | 2.487 | 2.365 | 2.403 | 2.467 | 2.508 |
| host CPU busy, the real machine under kind (%) | 75.03 | 79.21 | 74.73 | 83.13 | 74.89 | 79.83 | 75.6 | 81.36 | 74.35 | 81.27 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.4667 | 0.5222 | 0.95 | 1.21 | 0.52 | 0.38 | 0.82 | 0.6 | 0.57 | 1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3689 | 4471 | +21.2% | -588.4 to +2153 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6156 | 7144 | +16.1% | -408.2 to +2386 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.78 | 58.1 | -2.8% | -3.376 to +0.016 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.44 | 44.93 | +1.1% | -3.623 to +4.603 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.821 | 13.03 | +32.7% | +1.449 to +4.965 | power given |
| pods started | 3.889 | 7.444 | +91.4% | +1.966 to +5.145 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.677e-15 to +1.282e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 277.9 | -0.1% | -1.574 to +0.8149 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.3 | 277.9 | -0.1% | -1.574 to +0.8149 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.512 | 2.539 | +1.1% | +0.006039 to +0.0485 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.03 | 79.21 | +5.6% | +3.784 to +4.584 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4667 | 0.5222 | +11.9% | -0.0539 to +0.165 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3201 | 3382 | +5.7% | -1407 to +1770 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5668 | 5848 | +3.2% | -1221 to +1580 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 49.99 | 51.69 | +3.4% | -3.311 to +6.703 | EVEN, inside the noise (up) |
| failed requests (%) | 32.02 | 38.61 | +20.6% | +1.327 to +11.85 | LOSS |
| HPA replicas, mean | 9.803 | 12.54 | +27.9% | +1.264 to +4.206 | power given |
| pods started | 4.4 | 7.3 | +65.9% | +0.6519 to +5.148 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003811 to +0.001475 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 278 | +0.5% | +0.5489 to +2.198 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 277.9 | +0.5% | +0.5519 to +2.124 | power given |
| CPU used with Omni's own (cores), mean | 2.455 | 2.518 | +2.6% | +0.02507 to +0.1018 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.73 | 83.13 | +11.2% | +7.364 to +9.424 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.95 | 1.21 | +27.4% | +0.1011 to +0.4189 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3496 | 3174 | -9.2% | -1856 to +1210 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5756 | 5667 | -1.5% | -1519 to +1342 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 52.85 | 52.46 | -0.7% | -2.648 to +1.87 | EVEN, inside the noise (cut) |
| failed requests (%) | 38.82 | 44.21 | +13.9% | +1.212 to +9.575 | LOSS |
| HPA replicas, mean | 9.79 | 12.23 | +25.0% | +1.162 to +3.726 | power given |
| pods started | 4.7 | 8.5 | +80.9% | +2.087 to +5.513 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.009436 to +0.00365 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277.5 | +0.3% | +0.25 to +1.548 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 277.4 | +0.3% | +0.1561 to +1.466 | power given |
| CPU used with Omni's own (cores), mean | 2.453 | 2.487 | +1.4% | +0.01684 to +0.0508 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.89 | 79.83 | +6.6% | +4.268 to +5.629 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.52 | 0.38 | -26.9% | -0.19 to -0.08999 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2902 | 3197 | +10.2% | -1209 to +1800 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5266 | 5266 | +0.0% | -1685 to +1686 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.67 | 54.95 | +0.5% | -1.479 to +2.028 | EVEN, inside the noise (up) |
| failed requests (%) | 43.18 | 46.12 | +6.8% | +0.2177 to +5.668 | LOSS |
| HPA replicas, mean | 9.786 | 11.98 | +22.4% | +0.8611 to +3.527 | power given |
| pods started | 4.5 | 6.1 | +35.6% | +0.01122 to +3.189 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.744e-15 to +5.009e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.5 | +0.0% | -1.634 to +1.646 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.5 | +0.0% | -1.634 to +1.646 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.365 | 2.403 | +1.6% | +0.0014 to +0.07385 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.6 | 81.36 | +7.6% | +4.514 to +7.017 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.82 | 0.6 | -26.8% | -0.5906 to +0.1506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3093 | 2617 | -15.4% | -1569 to +615.5 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5718 | 5101 | -10.8% | -1704 to +469.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 53.74 | 54.5 | +1.4% | -4.342 to +5.866 | EVEN, inside the noise (up) |
| failed requests (%) | 40.96 | 45.21 | +10.4% | -1.432 to +9.933 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.77 | 12.84 | +31.4% | +1.419 to +4.722 | power given |
| pods started | 5.2 | 7.8 | +50.0% | +0.308 to +4.892 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.254e-15 to +1.721e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.2 | -0.0% | -1.263 to +1.046 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.2 | -0.0% | -1.263 to +1.046 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.467 | 2.508 | +1.6% | +0.01289 to +0.06807 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.35 | 81.27 | +9.3% | +6.373 to +7.473 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.57 | 1 | +75.4% | +0.2908 to +0.5692 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
