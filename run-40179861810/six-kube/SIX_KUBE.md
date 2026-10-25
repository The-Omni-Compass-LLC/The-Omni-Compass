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
| response time (ms), 95th percentile | 3745 | 4258 | 4724 | 3494 | 4052 | 3149 | 2403 | 1605 | 2858 | 2123 |
| response time (ms), 99th percentile | 5614 | 6204 | 6619 | 7076 | 5955 | 5492 | 4714 | 4479 | 4550 | 4304 |
| time over the response line (% of samples) | 50.89 | 49.34 | 70.34 | 67.47 | 50.37 | 49.93 | 41.58 | 40.76 | 41.57 | 43.6 |
| failed requests (%) | 35.63 | 38.51 | 56.78 | 59.63 | 36.94 | 41.07 | 29.36 | 33.37 | 31.53 | 35.35 |
| HPA replicas, mean | 9.773 | 12.13 | 9.818 | 11.62 | 9.793 | 11.74 | 9.764 | 11.57 | 9.738 | 12.3 |
| pods started | 4.7 | 8.1 | 4.2 | 4.9 | 4.2 | 6.9 | 5.1 | 7.7 | 5.4 | 8.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 5.995 | 5.997 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 277.6 | 278 | 278.8 | 275.2 | 275.2 | 275.6 | 275.9 | 274.9 | 276.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 277.6 | 278 | 278.8 | 275.1 | 275.2 | 275.6 | 275.9 | 274.9 | 276.4 |
| CPU used with Omni's own (cores), mean | 2.437 | 2.479 | 2.552 | 2.591 | 2.361 | 2.4 | 2.351 | 2.406 | 2.36 | 2.421 |
| host CPU busy, the real machine under kind (%) | 71.8 | 76.14 | 78.34 | 86.14 | 72.46 | 77.54 | 72.03 | 78.41 | 71 | 78.79 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.4 | 0.52 | 0.89 | 1.25 | 0.59 | 0.39 | 0.74 | 0.38 | 0.47 | 1.01 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3745 | 4258 | +13.7% | -474.7 to +1501 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5614 | 6204 | +10.5% | -462.1 to +1641 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 50.89 | 49.34 | -3.0% | -4.094 to +1.006 | EVEN, inside the noise (cut) |
| failed requests (%) | 35.63 | 38.51 | +8.1% | -2.703 to +8.46 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.773 | 12.13 | +24.2% | +0.6453 to +4.077 | power given |
| pods started | 4.7 | 8.1 | +72.3% | +1.641 to +5.159 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.066e-15 to +7.108e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 277.6 | +0.5% | +0.6035 to +2.222 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 277.6 | +0.5% | +0.6035 to +2.222 | power given |
| CPU used with Omni's own (cores), mean | 2.437 | 2.479 | +1.7% | +0.01832 to +0.06577 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.8 | 76.14 | +6.0% | +3.512 to +5.163 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4 | 0.52 | +30.0% | +0.01444 to +0.2256 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4724 | 3494 | -26.0% | -3051 to +591.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6619 | 7076 | +6.9% | -1152 to +2067 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 70.34 | 67.47 | -4.1% | -5.281 to -0.4664 | GAIN |
| failed requests (%) | 56.78 | 59.63 | +5.0% | -0.4874 to +6.195 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.818 | 11.62 | +18.4% | +0.7095 to +2.894 | power given |
| pods started | 4.2 | 4.9 | +16.7% | -1.268 to +2.668 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003594 to +0.001391 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278 | 278.8 | +0.3% | -0.4135 to +1.948 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278 | 278.8 | +0.3% | -0.4218 to +1.89 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.552 | 2.591 | +1.5% | -0.004222 to +0.08331 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.34 | 86.14 | +10.0% | +6.565 to +9.041 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.89 | 1.25 | +40.4% | +0.2243 to +0.4957 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4052 | 3149 | -22.3% | -2230 to +424.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5955 | 5492 | -7.8% | -2217 to +1292 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 50.37 | 49.93 | -0.9% | -2.264 to +1.377 | EVEN, inside the noise (cut) |
| failed requests (%) | 36.94 | 41.07 | +11.2% | -0.9238 to +9.184 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.793 | 11.74 | +19.9% | +0.2369 to +3.665 | power given |
| pods started | 4.2 | 6.9 | +64.3% | +0.566 to +4.834 | power given |
| worker nodes in service, mean | 5.995 | 5.997 | +0.0% | -0.002091 to +0.005405 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.2 | +0.0% | -0.9555 to +1.009 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 275.2 | +0.0% | -0.8387 to +0.9919 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.361 | 2.4 | +1.6% | +0.007131 to +0.07017 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.46 | 77.54 | +7.0% | +4.306 to +5.862 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.59 | 0.39 | -33.9% | -0.3012 to -0.09884 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2403 | 1605 | -33.2% | -1983 to +386.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4714 | 4479 | -5.0% | -2017 to +1546 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.58 | 40.76 | -2.0% | -3.767 to +2.115 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.36 | 33.37 | +13.7% | +0.1577 to +7.869 | LOSS |
| HPA replicas, mean | 9.764 | 11.57 | +18.5% | +0.5359 to +3.082 | power given |
| pods started | 5.1 | 7.7 | +51.0% | +0.4356 to +4.764 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.72e-15 to +1.213e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 275.9 | +0.1% | -0.5093 to +1.029 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 275.9 | +0.1% | -0.5093 to +1.029 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.351 | 2.406 | +2.3% | +0.02712 to +0.08304 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.03 | 78.41 | +8.9% | +5.381 to +7.387 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.74 | 0.38 | -48.6% | -0.5078 to -0.2122 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2858 | 2123 | -25.7% | -2243 to +773.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4550 | 4304 | -5.4% | -1119 to +627.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.57 | 43.6 | +4.9% | -1.926 to +5.974 | EVEN, inside the noise (up) |
| failed requests (%) | 31.53 | 35.35 | +12.1% | -2.487 to +10.14 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.738 | 12.3 | +26.3% | +0.9339 to +4.185 | power given |
| pods started | 5.4 | 8.6 | +59.3% | +0.994 to +5.406 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.286e-16 to +9.063e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 276.4 | +0.5% | +0.4657 to +2.507 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 276.4 | +0.5% | +0.4657 to +2.507 | power given |
| CPU used with Omni's own (cores), mean | 2.36 | 2.421 | +2.6% | +0.01044 to +0.1112 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71 | 78.79 | +11.0% | +6.323 to +9.268 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.47 | 1.01 | +114.9% | +0.4002 to +0.6798 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
