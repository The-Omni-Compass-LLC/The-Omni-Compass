# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1643 | 1625 | 1664 | 1741 | 1360 | 1191 | 1668 | 1469 | 1744 | 1533 | 1736 | 1980 | 1689 | 1559 |
| response time (ms), 99th percentile | 5272 | 5335 | 4636 | 4947 | 4619 | 4628 | 5472 | 5149 | 4782 | 4911 | 4616 | 5142 | 4803 | 5079 |
| time over the response line (% of samples) | 20.67 | 15.79 | 29.03 | 22.92 | 15.57 | 11.84 | 19.27 | 14.73 | 25.98 | 20.07 | 27.56 | 22.65 | 29.94 | 22.73 |
| failed requests (%) | 7.217 | 6.828 | 13.29 | 12.26 | 5.063 | 4.915 | 6.542 | 6.309 | 8.425 | 7.865 | 10.93 | 10.45 | 13.81 | 12.25 |
| HPA replicas, mean | 9.602 | 14.21 | 9.664 | 13.91 | 9.576 | 13.92 | 9.624 | 14.03 | 9.598 | 14.24 | 9.619 | 14.2 | 9.681 | 14.18 |
| pods started | 5.286 | 10.34 | 4.743 | 12.09 | 5.4 | 11.34 | 4.943 | 11.29 | 5.143 | 11.09 | 5.143 | 11.09 | 4.686 | 11.94 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.9 | 181.4 | 181.8 | 179.3 | 178.7 | 180.4 | 179.6 | 181.9 | 181.7 | 181.8 | 182.3 | 182.1 | 182.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.9 | 181.4 | 181.8 | 179.3 | 178.7 | 180.4 | 179.6 | 181.9 | 181.7 | 181.8 | 182.3 | 182.1 | 182.6 |
| CPU used with Omni's own (cores), mean | 2.003 | 2.029 | 2.132 | 2.163 | 1.877 | 1.907 | 1.983 | 2.011 | 2.124 | 2.161 | 2.158 | 2.191 | 2.194 | 2.223 |
| host CPU busy, the real machine under kind (%) | 59.34 | 60.47 | 63.04 | 64.31 | 55.64 | 56.86 | 58.5 | 59.7 | 62.82 | 64.17 | 63.78 | 64.99 | 64.93 | 66.4 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08571 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1643 | 1625 | -1.1% | -295.4 to +259.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5272 | 5335 | +1.2% | -441.1 to +565.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.67 | 15.79 | -23.6% | -6.049 to -3.717 | GAIN |
| failed requests (%) | 7.217 | 6.828 | -5.4% | -0.7891 to +0.01077 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.602 | 14.21 | +48.0% | +4.125 to +5.097 | power given |
| pods started | 5.286 | 10.34 | +95.7% | +4.531 to +5.584 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.081e-15 to -2.39e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.9 | -0.4% | -1.27 to -0.3392 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.9 | -0.4% | -1.27 to -0.3392 | GAIN |
| CPU used with Omni's own (cores), mean | 2.003 | 2.029 | +1.3% | +0.01582 to +0.03599 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.34 | 60.47 | +1.9% | +0.859 to +1.394 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.965e+05 to +7.99e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.408e-05 to -9.379e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1664 | 1741 | +4.6% | -269.3 to +423.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4636 | 4947 | +6.7% | -277.7 to +900 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.03 | 22.92 | -21.0% | -8.989 to -3.224 | GAIN |
| failed requests (%) | 13.29 | 12.26 | -7.8% | -2.217 to +0.1516 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.664 | 13.91 | +43.9% | +3.83 to +4.663 | power given |
| pods started | 4.743 | 12.09 | +154.8% | +6.81 to +7.876 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.439e-16 to -6.969e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181.8 | +0.2% | -0.1005 to +0.8893 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181.8 | +0.2% | -0.1005 to +0.8893 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.132 | 2.163 | +1.5% | +0.01738 to +0.0447 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.04 | 64.31 | +2.0% | +0.8906 to +1.648 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1360 | 1191 | -12.5% | -368.5 to +29.15 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4619 | 4628 | +0.2% | -293.9 to +312.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.57 | 11.84 | -23.9% | -4.781 to -2.679 | GAIN |
| failed requests (%) | 5.063 | 4.915 | -2.9% | -0.4659 to +0.1696 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.576 | 13.92 | +45.3% | +3.841 to +4.837 | power given |
| pods started | 5.4 | 11.34 | +110.1% | +5.458 to +6.428 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.724e-16 to +6.292e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.7 | -0.3% | -1.111 to -0.1358 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.7 | -0.3% | -1.111 to -0.1358 | GAIN |
| CPU used with Omni's own (cores), mean | 1.877 | 1.907 | +1.6% | +0.02235 to +0.03813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.64 | 56.86 | +2.2% | +0.9913 to +1.45 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1668 | 1469 | -11.9% | -483.4 to +84.79 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5472 | 5149 | -5.9% | -647.5 to +1.266 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.27 | 14.73 | -23.6% | -5.639 to -3.449 | GAIN |
| failed requests (%) | 6.542 | 6.309 | -3.6% | -0.6387 to +0.1715 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.624 | 14.03 | +45.7% | +3.909 to +4.894 | power given |
| pods started | 4.943 | 11.29 | +128.3% | +5.803 to +6.882 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.714e-16 to +8.639e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.6 | -0.5% | -1.311 to -0.399 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.6 | -0.5% | -1.311 to -0.399 | GAIN |
| CPU used with Omni's own (cores), mean | 1.983 | 2.011 | +1.4% | +0.02008 to +0.0364 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.5 | 59.7 | +2.1% | +0.9398 to +1.47 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1744 | 1533 | -12.1% | -383.6 to -38.86 | GAIN |
| response time (ms), 99th percentile | 4782 | 4911 | +2.7% | -354.5 to +611 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 25.98 | 20.07 | -22.8% | -8.03 to -3.799 | GAIN |
| failed requests (%) | 8.425 | 7.865 | -6.6% | -1.513 to +0.394 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.598 | 14.24 | +48.3% | +4.144 to +5.136 | power given |
| pods started | 5.143 | 11.09 | +115.6% | +5.337 to +6.549 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.332e-16 to +1.795e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.7 | -0.1% | -0.5932 to +0.157 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.7 | -0.1% | -0.5932 to +0.157 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.124 | 2.161 | +1.8% | +0.02298 to +0.05155 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.82 | 64.17 | +2.1% | +0.9539 to +1.74 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1736 | 1980 | +14.1% | -68.98 to +557.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4616 | 5142 | +11.4% | +3.919 to +1049 | LOSS |
| time over the response line (% of samples) | 27.56 | 22.65 | -17.8% | -6.584 to -3.245 | GAIN |
| failed requests (%) | 10.93 | 10.45 | -4.4% | -1.294 to +0.3394 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.619 | 14.2 | +47.6% | +4.186 to +4.975 | power given |
| pods started | 5.143 | 11.09 | +115.6% | +5.397 to +6.489 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.507e-16 to +1.447e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 182.3 | +0.3% | +0.00289 to +0.9087 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 182.3 | +0.3% | +0.00289 to +0.9087 | power given |
| CPU used with Omni's own (cores), mean | 2.158 | 2.191 | +1.5% | +0.01984 to +0.04525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.78 | 64.99 | +1.9% | +0.8413 to +1.59 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1689 | 1559 | -7.7% | -382.6 to +121.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4803 | 5079 | +5.7% | -222.5 to +773 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.94 | 22.73 | -24.1% | -9.296 to -5.121 | GAIN |
| failed requests (%) | 13.81 | 12.25 | -11.3% | -2.696 to -0.4283 | GAIN |
| HPA replicas, mean | 9.681 | 14.18 | +46.5% | +4.158 to +4.844 | power given |
| pods started | 4.686 | 11.94 | +154.9% | +6.678 to +7.836 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.391e-16 to +3.391e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 182.6 | +0.3% | -0.005852 to +0.9515 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 182.6 | +0.3% | -0.005852 to +0.9515 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.194 | 2.223 | +1.3% | +0.01707 to +0.04072 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.93 | 66.4 | +2.3% | +1.076 to +1.854 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08571 | +0.0857 | +0.07352 to +0.09791 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
