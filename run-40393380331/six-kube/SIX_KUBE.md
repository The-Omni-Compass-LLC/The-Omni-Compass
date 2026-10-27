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
| response time (ms), 95th percentile | 4791 | 4887 | 3286 | 3616 | 5239 | 3860 | 4696 | 2336 | 3827 | 3955 |
| response time (ms), 99th percentile | 7390 | 6733 | 5293 | 4822 | 7670 | 6183 | 7660 | 5968 | 5912 | 6354 |
| time over the response line (% of samples) | 55.67 | 54.34 | 53.63 | 53.21 | 62.33 | 61 | 63.07 | 60.01 | 75.69 | 72.91 |
| failed requests (%) | 37.38 | 42.81 | 41.32 | 46.42 | 44.01 | 51.68 | 45.05 | 49.96 | 64.02 | 64.81 |
| HPA replicas, mean | 9.782 | 12.27 | 9.8 | 12.15 | 9.79 | 11.13 | 9.825 | 11.77 | 9.85 | 11.94 |
| pods started | 4.8 | 7 | 4.3 | 7.1 | 4.7 | 5.5 | 4.2 | 5.4 | 3.7 | 4.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 278.4 | 276.8 | 276.9 | 278.4 | 278.2 | 278.7 | 279.7 | 278.9 | 277.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 278.4 | 276.8 | 276.9 | 278.4 | 278.2 | 278.7 | 279.7 | 278.9 | 277.6 |
| CPU used with Omni's own (cores), mean | 2.516 | 2.555 | 2.427 | 2.475 | 2.552 | 2.565 | 2.601 | 2.63 | 2.615 | 2.632 |
| host CPU busy, the real machine under kind (%) | 74.21 | 78.53 | 73.75 | 81.74 | 77.5 | 82.15 | 79.7 | 85.31 | 80.12 | 86.78 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.43 | 0.51 | 0.84 | 1.15 | 0.54 | 0.42 | 0.87 | 0.4 | 0.49 | 1.25 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4791 | 4887 | +2.0% | -1918 to +2110 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 7390 | 6733 | -8.9% | -2198 to +884.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.67 | 54.34 | -2.4% | -4.277 to +1.629 | EVEN, inside the noise (cut) |
| failed requests (%) | 37.38 | 42.81 | +14.5% | -0.9126 to +11.78 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.782 | 12.27 | +25.4% | +0.7195 to +4.252 | power given |
| pods started | 4.8 | 7 | +45.8% | +0.01991 to +4.38 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.661e-15 to +5.957e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 278.4 | +0.6% | +0.4342 to +2.717 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 278.4 | +0.6% | +0.4342 to +2.717 | power given |
| CPU used with Omni's own (cores), mean | 2.516 | 2.555 | +1.6% | +0.01226 to +0.06672 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.21 | 78.53 | +5.8% | +3.37 to +5.269 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.43 | 0.51 | +18.6% | -0.09128 to +0.2513 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3286 | 3616 | +10.1% | -1743 to +2403 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5293 | 4822 | -8.9% | -2113 to +1170 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 53.63 | 53.21 | -0.8% | -2.02 to +1.177 | EVEN, inside the noise (cut) |
| failed requests (%) | 41.32 | 46.42 | +12.3% | +0.3065 to +9.894 | LOSS |
| HPA replicas, mean | 9.8 | 12.15 | +24.0% | +1.109 to +3.595 | power given |
| pods started | 4.3 | 7.1 | +65.1% | +0.8108 to +4.789 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.466e-15 to +9.334e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.9 | +0.0% | -1.003 to +1.21 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.9 | +0.0% | -1.003 to +1.21 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.427 | 2.475 | +2.0% | -0.003545 to +0.1006 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.75 | 81.74 | +10.8% | +6.465 to +9.531 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.84 | 1.15 | +36.9% | +0.212 to +0.408 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5239 | 3860 | -26.3% | -3744 to +985.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 7670 | 6183 | -19.4% | -3405 to +431.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 62.33 | 61 | -2.1% | -2.951 to +0.2924 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.01 | 51.68 | +17.4% | +1.427 to +13.91 | LOSS |
| HPA replicas, mean | 9.79 | 11.13 | +13.7% | -0.1742 to +2.853 | EVEN, inside the noise (up) |
| pods started | 4.7 | 5.5 | +17.0% | -1.432 to +3.032 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.392e-15 to +1.57e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.4 | 278.2 | -0.1% | -1.512 to +1.021 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.4 | 278.2 | -0.1% | -1.512 to +1.021 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.552 | 2.565 | +0.5% | -0.003671 to +0.02972 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.5 | 82.15 | +6.0% | +4.359 to +4.943 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.54 | 0.42 | -22.2% | -0.2142 to -0.02583 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4696 | 2336 | -50.3% | -4497 to -222.9 | GAIN |
| response time (ms), 99th percentile | 7660 | 5968 | -22.1% | -3729 to +346 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 63.07 | 60.01 | -4.8% | -5.644 to -0.4705 | GAIN |
| failed requests (%) | 45.05 | 49.96 | +10.9% | +0.6842 to +9.138 | LOSS |
| HPA replicas, mean | 9.825 | 11.77 | +19.8% | +0.462 to +3.424 | power given |
| pods started | 4.2 | 5.4 | +28.6% | -0.4101 to +2.81 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.29e-15 to +9.349e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.7 | 279.7 | +0.4% | -0.02781 to +1.989 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.7 | 279.7 | +0.4% | -0.02781 to +1.989 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.601 | 2.63 | +1.1% | +0.009943 to +0.04751 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.7 | 85.31 | +7.0% | +5.086 to +6.124 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.87 | 0.4 | -54.0% | -0.6752 to -0.2648 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3827 | 3955 | +3.4% | -1483 to +1739 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5912 | 6354 | +7.5% | -968.6 to +1852 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 75.69 | 72.91 | -3.7% | -3.905 to -1.67 | GAIN |
| failed requests (%) | 64.02 | 64.81 | +1.2% | -1.79 to +3.384 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.85 | 11.94 | +21.3% | +0.4905 to +3.698 | power given |
| pods started | 3.7 | 4.7 | +27.0% | -1.185 to +3.185 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.007697 to +0.002978 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.9 | 277.6 | -0.5% | -3.331 to +0.7725 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.9 | 277.6 | -0.5% | -3.552 to +0.8519 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.615 | 2.632 | +0.6% | +0.007579 to +0.02613 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.12 | 86.78 | +8.3% | +6.421 to +6.896 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.49 | 1.25 | +155.1% | +0.4755 to +1.045 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
