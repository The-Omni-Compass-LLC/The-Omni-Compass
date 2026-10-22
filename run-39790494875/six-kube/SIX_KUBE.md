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
| response time (ms), 95th percentile | 1550 | 1398 | 1092 | 1234 | 1330 | 769.9 | 1647 | 1815 | 2201 | 1681 | 1711 | 2083 | 1148 | 1129 |
| response time (ms), 99th percentile | 4762 | 5264 | 3688 | 4136 | 4155 | 3377 | 5928 | 7097 | 5367 | 5175 | 4387 | 4698 | 4017 | 4142 |
| time over the response line (% of samples) | 21.37 | 15.56 | 16.8 | 12.53 | 14.16 | 9.941 | 24.89 | 18.36 | 29.42 | 21.62 | 28.17 | 24.51 | 19.34 | 14.4 |
| failed requests (%) | 8.6 | 7.679 | 6.762 | 5.71 | 4.762 | 4.903 | 9.878 | 8.173 | 10.05 | 8.829 | 11.46 | 11.21 | 8.039 | 7.347 |
| HPA replicas, mean | 9.646 | 13.66 | 9.577 | 13.09 | 9.546 | 13.45 | 9.7 | 14.66 | 9.662 | 14.31 | 9.629 | 14.06 | 9.607 | 13.6 |
| pods started | 4.4 | 9.9 | 5.7 | 13 | 5.2 | 11.5 | 4.4 | 10.3 | 4.1 | 10 | 4.7 | 11.6 | 5.4 | 13 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.1 | 179.4 | 178.9 | 178.4 | 178.1 | 182.3 | 181.8 | 181.8 | 181.6 | 181.9 | 182 | 179.6 | 179.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.1 | 179.4 | 178.9 | 178.4 | 178.1 | 182.3 | 181.8 | 181.8 | 181.6 | 181.9 | 182 | 179.6 | 179.6 |
| CPU used with Omni's own (cores), mean | 2.003 | 2.023 | 1.865 | 1.895 | 1.787 | 1.804 | 2.192 | 2.203 | 2.15 | 2.173 | 2.128 | 2.132 | 1.901 | 1.937 |
| host CPU busy, the real machine under kind (%) | 59.29 | 60.24 | 55.74 | 56.74 | 53.29 | 54.19 | 64.63 | 65.17 | 63.88 | 65.23 | 63.05 | 63.6 | 56.81 | 58.08 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1550 | 1398 | -9.8% | -522.2 to +217.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4762 | 5264 | +10.5% | -697.2 to +1702 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 21.37 | 15.56 | -27.2% | -9.254 to -2.377 | GAIN |
| failed requests (%) | 8.6 | 7.679 | -10.7% | -1.921 to +0.07962 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.646 | 13.66 | +41.6% | +2.482 to +5.541 | power given |
| pods started | 4.4 | 9.9 | +125.0% | +3.527 to +7.473 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.337e-15 to +2.707e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.1 | -0.4% | -1.817 to +0.209 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.1 | -0.4% | -1.817 to +0.209 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.003 | 2.023 | +1.0% | +0.004992 to +0.0344 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.29 | 60.24 | +1.6% | +0.5459 to +1.35 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +7.988e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.407e-05 to -9.39e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1092 | 1234 | +13.0% | -136.4 to +420 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3688 | 4136 | +12.1% | -498.8 to +1395 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 16.8 | 12.53 | -25.4% | -8.176 to -0.3736 | GAIN |
| failed requests (%) | 6.762 | 5.71 | -15.6% | -2.586 to +0.482 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.577 | 13.09 | +36.7% | +2.303 to +4.729 | power given |
| pods started | 5.7 | 13 | +128.1% | +5.992 to +8.608 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.989e-16 to +5.436e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.9 | -0.3% | -1.658 to +0.5799 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.9 | -0.3% | -1.658 to +0.5799 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.865 | 1.895 | +1.6% | +0.009944 to +0.05003 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.74 | 56.74 | +1.8% | +0.455 to +1.538 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1330 | 769.9 | -42.1% | -1340 to +218.5 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4155 | 3377 | -18.7% | -1322 to -234.2 | GAIN |
| time over the response line (% of samples) | 14.16 | 9.941 | -29.8% | -7.708 to -0.7378 | GAIN |
| failed requests (%) | 4.762 | 4.903 | +3.0% | -0.3203 to +0.6017 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.546 | 13.45 | +40.9% | +2.585 to +5.226 | power given |
| pods started | 5.2 | 11.5 | +121.2% | +5.231 to +7.369 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.547e-15 to +1.259e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 178.1 | -0.2% | -1.674 to +1.076 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 178.1 | -0.2% | -1.674 to +1.076 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.787 | 1.804 | +0.9% | -0.007894 to +0.04178 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.29 | 54.19 | +1.7% | +0.2277 to +1.581 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1647 | 1815 | +10.1% | -271 to +605.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5928 | 7097 | +19.7% | +97.75 to +2241 | LOSS |
| time over the response line (% of samples) | 24.89 | 18.36 | -26.2% | -8.464 to -4.588 | GAIN |
| failed requests (%) | 9.878 | 8.173 | -17.3% | -2.557 to -0.8536 | GAIN |
| HPA replicas, mean | 9.7 | 14.66 | +51.1% | +4.25 to +5.672 | power given |
| pods started | 4.4 | 10.3 | +134.1% | +4.81 to +6.99 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.69e-16 to +2.585e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.8 | -0.3% | -1.745 to +0.8002 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.8 | -0.3% | -1.745 to +0.8002 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.192 | 2.203 | +0.5% | -0.01157 to +0.03375 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.63 | 65.17 | +0.8% | +0.001591 to +1.088 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2201 | 1681 | -23.6% | -1063 to +22.47 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5367 | 5175 | -3.6% | -1091 to +706.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 29.42 | 21.62 | -26.5% | -12.21 to -3.398 | GAIN |
| failed requests (%) | 10.05 | 8.829 | -12.2% | -2.537 to +0.09404 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.662 | 14.31 | +48.1% | +3.603 to +5.694 | power given |
| pods started | 4.1 | 10 | +143.9% | +4.575 to +7.225 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.193e-15 to +3.046e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.6 | -0.1% | -1.306 to +0.8472 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.6 | -0.1% | -1.306 to +0.8472 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.15 | 2.173 | +1.1% | +0.002611 to +0.04371 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.88 | 65.23 | +2.1% | +0.8079 to +1.893 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1711 | 2083 | +21.8% | -458.3 to +1203 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4387 | 4698 | +7.1% | -1737 to +2360 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.17 | 24.51 | -13.0% | -8.107 to +0.7805 | EVEN, inside the noise (cut) |
| failed requests (%) | 11.46 | 11.21 | -2.2% | -3.604 to +3.103 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.629 | 14.06 | +46.1% | +3.472 to +5.399 | power given |
| pods started | 4.7 | 11.6 | +146.8% | +5.92 to +7.88 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.295e-15 to +5.13e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 182 | +0.1% | -1.62 to +1.938 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 182 | +0.1% | -1.62 to +1.938 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.128 | 2.132 | +0.2% | -0.07313 to +0.08155 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.05 | 63.6 | +0.9% | -1.873 to +2.98 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1148 | 1129 | -1.6% | -280.6 to +243.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4017 | 4142 | +3.1% | -654.5 to +904.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.34 | 14.4 | -25.6% | -9.841 to -0.05389 | GAIN |
| failed requests (%) | 8.039 | 7.347 | -8.6% | -2.217 to +0.8335 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 13.6 | +41.5% | +2.986 to +4.997 | power given |
| pods started | 5.4 | 13 | +140.7% | +6.523 to +8.677 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 179.6 | +0.0% | -0.9477 to +0.9574 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 179.6 | +0.0% | -0.9477 to +0.9574 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.901 | 1.937 | +1.9% | +0.01542 to +0.05669 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.81 | 58.08 | +2.2% | +0.7648 to +1.772 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.987e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.1 | +0.1 | +0.1 to +0.1 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
