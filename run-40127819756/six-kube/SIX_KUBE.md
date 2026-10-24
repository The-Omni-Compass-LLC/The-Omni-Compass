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
| response time (ms), 95th percentile | 1372 | 1474 | 1665 | 1682 | 1314 | 1483 | 1655 | 1822 | 1651 | 1371 | 1775 | 1625 | 1663 | 1227 |
| response time (ms), 99th percentile | 4791 | 4666 | 4897 | 5975 | 4829 | 4682 | 6687 | 6466 | 5861 | 5209 | 4987 | 5144 | 5062 | 4685 |
| time over the response line (% of samples) | 14.71 | 10.94 | 28.65 | 21.21 | 15.37 | 11.28 | 23.7 | 17.03 | 21.74 | 15.61 | 29.39 | 21.03 | 22.88 | 14.78 |
| failed requests (%) | 4.218 | 3.729 | 12.76 | 11.02 | 4.601 | 4.001 | 8.596 | 7.364 | 6.101 | 5.083 | 11.65 | 9.569 | 9.674 | 7.099 |
| HPA replicas, mean | 9.555 | 13.44 | 9.685 | 12.87 | 9.569 | 13.17 | 9.687 | 13.66 | 9.559 | 13.28 | 9.632 | 12.99 | 9.687 | 13.06 |
| pods started | 6 | 11.3 | 5 | 10.9 | 5.8 | 10.2 | 4.4 | 10.6 | 5.9 | 10.8 | 5 | 10 | 4.5 | 11.3 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 178.8 | 183.2 | 182.8 | 179.4 | 178.3 | 182.3 | 181.9 | 181.8 | 181.9 | 181.9 | 181.5 | 180.7 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 178.8 | 183.2 | 182.8 | 179.4 | 178.3 | 182.3 | 181.9 | 181.8 | 181.9 | 181.9 | 181.5 | 180.7 | 180.8 |
| CPU used with Omni's own (cores), mean | 1.837 | 1.855 | 2.243 | 2.253 | 1.902 | 1.881 | 2.163 | 2.156 | 2.118 | 2.16 | 2.161 | 2.145 | 2.075 | 2.059 |
| host CPU busy, the real machine under kind (%) | 54.59 | 55.27 | 66.11 | 66.63 | 56.49 | 56.17 | 63.57 | 63.88 | 62.49 | 63.44 | 63.58 | 63.66 | 61.14 | 61.58 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1372 | 1474 | +7.4% | -462.5 to +665.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4791 | 4666 | -2.6% | -666.1 to +415.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.71 | 10.94 | -25.6% | -5.892 to -1.65 | GAIN |
| failed requests (%) | 4.218 | 3.729 | -11.6% | -1.179 to +0.199 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.555 | 13.44 | +40.7% | +2.984 to +4.789 | power given |
| pods started | 6 | 11.3 | +88.3% | +4.542 to +6.058 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.155e-16 to +1.348e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 178.8 | +0.1% | -0.9677 to +1.287 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 178.8 | +0.1% | -0.9677 to +1.287 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.837 | 1.855 | +1.0% | -0.01576 to +0.05309 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.59 | 55.27 | +1.2% | -0.0409 to +1.4 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.972e+05 to +8.004e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.425e-05 to -9.388e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1665 | 1682 | +1.1% | -358 to +393.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4897 | 5975 | +22.0% | -470.6 to +2627 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.65 | 21.21 | -26.0% | -10.27 to -4.612 | GAIN |
| failed requests (%) | 12.76 | 11.02 | -13.6% | -3.908 to +0.4269 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.685 | 12.87 | +32.9% | +2.257 to +4.116 | power given |
| pods started | 5 | 10.9 | +118.0% | +4.92 to +6.88 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 182.8 | -0.2% | -1.526 to +0.771 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 182.8 | -0.2% | -1.526 to +0.771 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.243 | 2.253 | +0.4% | -0.01848 to +0.03735 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.11 | 66.63 | +0.8% | -0.1835 to +1.232 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.63e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1314 | 1483 | +12.9% | -603.2 to +943 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4829 | 4682 | -3.0% | -1154 to +861.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 15.37 | 11.28 | -26.6% | -6.384 to -1.792 | GAIN |
| failed requests (%) | 4.601 | 4.001 | -13.0% | -1.389 to +0.1892 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.569 | 13.17 | +37.6% | +2.179 to +5.014 | power given |
| pods started | 5.8 | 10.2 | +75.9% | +2.922 to +5.878 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.924e-16 to +7.924e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.3 | -0.6% | -1.858 to -0.3607 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.3 | -0.6% | -1.858 to -0.3607 | GAIN |
| CPU used with Omni's own (cores), mean | 1.902 | 1.881 | -1.1% | -0.03744 to -0.004844 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.49 | 56.17 | -0.6% | -0.9958 to +0.3497 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.242e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1655 | 1822 | +10.1% | -666.4 to +1002 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6687 | 6466 | -3.3% | -856.9 to +414.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.7 | 17.03 | -28.2% | -8.957 to -4.386 | GAIN |
| failed requests (%) | 8.596 | 7.364 | -14.3% | -2.105 to -0.3577 | GAIN |
| HPA replicas, mean | 9.687 | 13.66 | +41.0% | +2.811 to +5.139 | power given |
| pods started | 4.4 | 10.6 | +140.9% | +4.359 to +8.041 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.523e-15 to +2.792e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.9 | -0.2% | -1.283 to +0.5819 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.9 | -0.2% | -1.283 to +0.5819 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.163 | 2.156 | -0.3% | -0.02096 to +0.008843 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.57 | 63.88 | +0.5% | -0.002063 to +0.6061 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1651 | 1371 | -17.0% | -772.8 to +212.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5861 | 5209 | -11.1% | -1264 to -38.77 | GAIN |
| time over the response line (% of samples) | 21.74 | 15.61 | -28.2% | -10.81 to -1.46 | GAIN |
| failed requests (%) | 6.101 | 5.083 | -16.7% | -2.247 to +0.2111 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.559 | 13.28 | +38.9% | +2.654 to +4.788 | power given |
| pods started | 5.9 | 10.8 | +83.1% | +3.375 to +6.425 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.576e-16 to +3.8e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.9 | +0.0% | -1.187 to +1.312 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.9 | +0.0% | -1.187 to +1.312 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.118 | 2.16 | +2.0% | -0.0188 to +0.103 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.49 | 63.44 | +1.5% | -0.452 to +2.348 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.379e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.72e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1775 | 1625 | -8.5% | -322.3 to +21.21 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4987 | 5144 | +3.1% | -576.9 to +891 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.39 | 21.03 | -28.4% | -12.07 to -4.645 | GAIN |
| failed requests (%) | 11.65 | 9.569 | -17.9% | -3.662 to -0.4988 | GAIN |
| HPA replicas, mean | 9.632 | 12.99 | +34.9% | +1.762 to +4.952 | power given |
| pods started | 5 | 10 | +100.0% | +3.418 to +6.582 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.5 | -0.2% | -1.432 to +0.6003 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.5 | -0.2% | -1.432 to +0.6003 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.161 | 2.145 | -0.8% | -0.0371 to +0.003421 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.58 | 63.66 | +0.1% | -0.4839 to +0.655 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1663 | 1227 | -26.2% | -998.4 to +126.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5062 | 4685 | -7.5% | -1495 to +740.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.88 | 14.78 | -35.4% | -14.36 to -1.835 | GAIN |
| failed requests (%) | 9.674 | 7.099 | -26.6% | -6.326 to +1.176 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.687 | 13.06 | +34.8% | +2.429 to +4.316 | power given |
| pods started | 4.5 | 11.3 | +151.1% | +4.754 to +8.846 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.013e-15 to +1.368e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.8 | +0.1% | -0.7039 to +1.053 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.8 | +0.1% | -0.7039 to +1.053 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.075 | 2.059 | -0.8% | -0.03803 to +0.005704 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.14 | 61.58 | +0.7% | -0.09088 to +0.9879 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.07 | +0.07 | +0.03545 to +0.1046 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
