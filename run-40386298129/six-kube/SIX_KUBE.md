# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2025 | 1536 | 1411 | 1170 | 1587 | 1799 | 1711 | 1922 | 1612 | 1402 | 2718 | 1970 | 928.2 | 633 |
| response time (ms), 99th percentile | 4884 | 5081 | 3806 | 4026 | 6358 | 5946 | 6623 | 6428 | 4075 | 4307 | 5524 | 5454 | 2446 | 2841 |
| time over the response line (% of samples) | 17.82 | 12.43 | 23.26 | 16.37 | 23.89 | 17.37 | 24.02 | 17.8 | 20.65 | 15.64 | 33.14 | 24.42 | 13 | 9.161 |
| failed requests (%) | 5.774 | 5.418 | 10.28 | 8.592 | 9.202 | 7.491 | 9.477 | 8.032 | 6.195 | 6.137 | 15.33 | 11.78 | 5.25 | 4.313 |
| HPA replicas, mean | 9.564 | 12.93 | 9.607 | 12.07 | 9.634 | 13.79 | 9.682 | 13.74 | 9.545 | 12.58 | 9.694 | 13.21 | 9.552 | 11.67 |
| pods started | 5.6 | 9.6 | 5.6 | 11.7 | 4.9 | 10.3 | 4.8 | 10.2 | 5.7 | 9.4 | 4.1 | 9.3 | 5.8 | 9.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179 | 181 | 180.3 | 181.8 | 180.9 | 182.9 | 182.2 | 180.2 | 180.8 | 182 | 182.6 | 177.6 | 177.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179 | 181 | 180.3 | 181.8 | 180.9 | 182.9 | 182.2 | 180.2 | 180.8 | 182 | 182.6 | 177.6 | 177.5 |
| CPU used with Omni's own (cores), mean | 1.934 | 1.928 | 2.011 | 2.014 | 2.089 | 2.097 | 2.212 | 2.217 | 1.994 | 2.017 | 2.228 | 2.233 | 1.731 | 1.74 |
| host CPU busy, the real machine under kind (%) | 56.94 | 57.11 | 59.66 | 59.79 | 61.86 | 62.28 | 65.08 | 65.32 | 59.21 | 59.84 | 65.48 | 65.84 | 51.56 | 52.29 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.06 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2025 | 1536 | -24.1% | -1358 to +380.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4884 | 5081 | +4.0% | -654 to +1049 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.82 | 12.43 | -30.2% | -8.293 to -2.487 | GAIN |
| failed requests (%) | 5.774 | 5.418 | -6.2% | -1.073 to +0.3616 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.564 | 12.93 | +35.2% | +1.801 to +4.927 | power given |
| pods started | 5.6 | 9.6 | +71.4% | +2.348 to +5.652 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.038e-15 to +3.277e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179 | -0.4% | -1.853 to +0.2909 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179 | -0.4% | -1.853 to +0.2909 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.934 | 1.928 | -0.3% | -0.0166 to +0.004242 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.94 | 57.11 | +0.3% | -0.1939 to +0.5338 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.935e+05 to +7.993e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.412e-05 to -9.343e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1411 | 1170 | -17.1% | -490.1 to +6.839 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3806 | 4026 | +5.8% | -1019 to +1459 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.26 | 16.37 | -29.6% | -12 to -1.784 | GAIN |
| failed requests (%) | 10.28 | 8.592 | -16.4% | -3.45 to +0.0792 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 12.07 | +25.7% | +1.131 to +3.803 | power given |
| pods started | 5.6 | 11.7 | +108.9% | +4.613 to +7.587 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.279e-15 to +2.128e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.3 | -0.4% | -1.627 to +0.1419 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.3 | -0.4% | -1.627 to +0.1419 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.011 | 2.014 | +0.2% | -0.0163 to +0.02339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.66 | 59.79 | +0.2% | -0.4337 to +0.7017 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.142e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1587 | 1799 | +13.4% | -221 to +646.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6358 | 5946 | -6.5% | -1263 to +440.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.89 | 17.37 | -27.3% | -9.663 to -3.381 | GAIN |
| failed requests (%) | 9.202 | 7.491 | -18.6% | -2.927 to -0.4945 | GAIN |
| HPA replicas, mean | 9.634 | 13.79 | +43.1% | +2.674 to +5.628 | power given |
| pods started | 4.9 | 10.3 | +110.2% | +4.323 to +6.477 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.535e-15 to +4.694e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 180.9 | -0.5% | -1.812 to +0.1582 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 180.9 | -0.5% | -1.812 to +0.1582 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.089 | 2.097 | +0.4% | -0.01144 to +0.02696 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.86 | 62.28 | +0.7% | -0.07108 to +0.9242 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1711 | 1922 | +12.3% | -327.1 to +749.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6623 | 6428 | -2.9% | -1279 to +889.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.02 | 17.8 | -25.9% | -8.411 to -4.02 | GAIN |
| failed requests (%) | 9.477 | 8.032 | -15.2% | -2.134 to -0.7548 | GAIN |
| HPA replicas, mean | 9.682 | 13.74 | +42.0% | +3.146 to +4.978 | power given |
| pods started | 4.8 | 10.2 | +112.5% | +4.129 to +6.671 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.102e-15 to +9.246e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 182.2 | -0.4% | -1.561 to +0.2569 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 182.2 | -0.4% | -1.561 to +0.2569 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.212 | 2.217 | +0.2% | -0.009099 to +0.01879 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.08 | 65.32 | +0.4% | -0.05504 to +0.5292 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1612 | 1402 | -13.0% | -733.6 to +315.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4075 | 4307 | +5.7% | -565.8 to +1030 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.65 | 15.64 | -24.3% | -8.012 to -2.008 | GAIN |
| failed requests (%) | 6.195 | 6.137 | -0.9% | -0.5794 to +0.4627 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.545 | 12.58 | +31.8% | +1.432 to +4.631 | power given |
| pods started | 5.7 | 9.4 | +64.9% | +1.761 to +5.639 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.8 | +0.3% | -0.1844 to +1.291 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.8 | +0.3% | -0.1844 to +1.291 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.994 | 2.017 | +1.1% | +0.002269 to +0.04339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.21 | 59.84 | +1.1% | -0.03511 to +1.279 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.72e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2718 | 1970 | -27.5% | -1910 to +414.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5524 | 5454 | -1.3% | -988.5 to +849.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 33.14 | 24.42 | -26.3% | -13.98 to -3.466 | GAIN |
| failed requests (%) | 15.33 | 11.78 | -23.2% | -7.357 to +0.2493 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.694 | 13.21 | +36.3% | +1.911 to +5.128 | power given |
| pods started | 4.1 | 9.3 | +126.8% | +3.903 to +6.497 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.216e-15 to +1.5e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 182.6 | +0.3% | +0.2394 to +0.9339 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 182.6 | +0.3% | +0.2394 to +0.9339 | power given |
| CPU used with Omni's own (cores), mean | 2.228 | 2.233 | +0.2% | -0.01055 to +0.02061 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.48 | 65.84 | +0.5% | +0.05763 to +0.6459 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 928.2 | 633 | -31.8% | -526.3 to -64.06 | GAIN |
| response time (ms), 99th percentile | 2446 | 2841 | +16.1% | -426.3 to +1216 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 13 | 9.161 | -29.5% | -7.983 to +0.3055 | EVEN, inside the noise (cut) |
| failed requests (%) | 5.25 | 4.313 | -17.8% | -2.561 to +0.6872 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.552 | 11.67 | +22.2% | +0.6288 to +3.605 | power given |
| pods started | 5.8 | 9.7 | +67.2% | +2.133 to +5.667 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 177.6 | 177.5 | -0.0% | -0.9996 to +0.9018 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.6 | 177.5 | -0.0% | -0.9996 to +0.9018 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.731 | 1.74 | +0.5% | -0.0133 to +0.0315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 51.56 | 52.29 | +1.4% | -0.0215 to +1.481 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.987e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.06 | +0.06 | +0.02306 to +0.09694 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
