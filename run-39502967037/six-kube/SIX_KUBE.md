# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1768 | 1419 | 1542 | 1354 | 2381 | 2202 | 2002 | 1969 | 1421 | 1229 | 1086 | 966.6 | 1531 | 1605 |
| response time (ms), 99th percentile | 6376 | 5664 | 4295 | 4709 | 7603 | 6740 | 6070 | 6384 | 4300 | 3922 | 3010 | 3323 | 4950 | 5398 |
| time over the response line (% of samples) | 22.34 | 16.78 | 26.3 | 18.57 | 28.08 | 19.3 | 22.2 | 16.29 | 20.7 | 14.31 | 15.67 | 11.9 | 26.46 | 19.9 |
| failed requests (%) | 8.177 | 7.188 | 12.26 | 9.503 | 10.03 | 7.901 | 7.745 | 6.686 | 5.904 | 5.267 | 6.434 | 5.168 | 11.89 | 10.06 |
| HPA replicas, mean | 9.705 | 14.52 | 9.632 | 12.67 | 9.69 | 14.88 | 9.667 | 13.99 | 9.607 | 13.76 | 9.492 | 11.4 | 9.666 | 12.78 |
| pods started | 4.1 | 10.7 | 5.3 | 11 | 4.8 | 10.5 | 4.5 | 10.1 | 4.9 | 11.3 | 6 | 9.8 | 5.1 | 9.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 182 | 181.8 | 181.1 | 183.3 | 182.7 | 181.3 | 181.9 | 181 | 180.2 | 178.3 | 178.1 | 182.2 | 182.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 182 | 181.8 | 181.1 | 183.3 | 182.7 | 181.3 | 181.9 | 181 | 180.2 | 178.3 | 178.1 | 182.2 | 182.2 |
| CPU used with Omni's own (cores), mean | 2.171 | 2.157 | 2.096 | 2.093 | 2.287 | 2.27 | 2.093 | 2.097 | 2.014 | 2.011 | 1.786 | 1.783 | 2.165 | 2.166 |
| host CPU busy, the real machine under kind (%) | 63.93 | 64.12 | 62.3 | 62.06 | 67.33 | 67.22 | 62.31 | 62.44 | 59.7 | 60.17 | 52.93 | 53.48 | 64.07 | 64.57 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1768 | 1419 | -19.7% | -872.7 to +175 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6376 | 5664 | -11.2% | -1690 to +265.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.34 | 16.78 | -24.9% | -7.301 to -3.811 | GAIN |
| failed requests (%) | 8.177 | 7.188 | -12.1% | -1.925 to -0.05433 | GAIN |
| HPA replicas, mean | 9.705 | 14.52 | +49.6% | +4.373 to +5.26 | power given |
| pods started | 4.1 | 10.7 | +161.0% | +5.523 to +7.677 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.594e-16 to +7.818e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 182 | +0.0% | -1.055 to +1.134 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 182 | +0.0% | -1.055 to +1.134 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.171 | 2.157 | -0.6% | -0.02671 to -0.0007067 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.93 | 64.12 | +0.3% | -0.2598 to +0.6369 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.932e+05 to +7.992e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.411e-05 to -9.34e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1542 | 1354 | -12.2% | -555.7 to +179.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4295 | 4709 | +9.6% | -384.9 to +1213 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 26.3 | 18.57 | -29.4% | -11.66 to -3.79 | GAIN |
| failed requests (%) | 12.26 | 9.503 | -22.5% | -4.671 to -0.8493 | GAIN |
| HPA replicas, mean | 9.632 | 12.67 | +31.6% | +1.545 to +4.54 | power given |
| pods started | 5.3 | 11 | +107.5% | +3.566 to +7.834 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.1 | -0.4% | -1.753 to +0.2168 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.1 | -0.4% | -1.753 to +0.2168 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.096 | 2.093 | -0.1% | -0.02082 to +0.01486 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.3 | 62.06 | -0.4% | -0.7898 to +0.3165 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2381 | 2202 | -7.5% | -890.8 to +532.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 7603 | 6740 | -11.3% | -1597 to -127.9 | GAIN |
| time over the response line (% of samples) | 28.08 | 19.3 | -31.3% | -11.16 to -6.4 | GAIN |
| failed requests (%) | 10.03 | 7.901 | -21.2% | -3.91 to -0.3543 | GAIN |
| HPA replicas, mean | 9.69 | 14.88 | +53.6% | +4.952 to +5.427 | power given |
| pods started | 4.8 | 10.5 | +118.8% | +4.942 to +6.458 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.7 | -0.3% | -1.7 to +0.5299 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.7 | -0.3% | -1.7 to +0.5299 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.287 | 2.27 | -0.8% | -0.03565 to +0.00118 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.33 | 67.22 | -0.2% | -0.6429 to +0.4274 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2002 | 1969 | -1.7% | -682.5 to +615.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6070 | 6384 | +5.2% | -473.2 to +1101 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.2 | 16.29 | -26.6% | -8.421 to -3.402 | GAIN |
| failed requests (%) | 7.745 | 6.686 | -13.7% | -2.303 to +0.1849 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.667 | 13.99 | +44.7% | +2.929 to +5.721 | power given |
| pods started | 4.5 | 10.1 | +124.4% | +3.809 to +7.391 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.038e-15 to +3.277e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 181.9 | +0.3% | -0.2243 to +1.349 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 181.9 | +0.3% | -0.2243 to +1.349 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.093 | 2.097 | +0.2% | -0.01474 to +0.02293 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.31 | 62.44 | +0.2% | -0.4143 to +0.6672 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1421 | 1229 | -13.5% | -442.9 to +59.72 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4300 | 3922 | -8.8% | -1067 to +310.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.7 | 14.31 | -30.9% | -10.59 to -2.191 | GAIN |
| failed requests (%) | 5.904 | 5.267 | -10.8% | -1.312 to +0.03695 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 13.76 | +43.3% | +3.015 to +5.3 | power given |
| pods started | 4.9 | 11.3 | +130.6% | +4.578 to +8.222 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.531e-16 to +1.264e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.2 | -0.4% | -1.846 to +0.3411 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.2 | -0.4% | -1.846 to +0.3411 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.014 | 2.011 | -0.1% | -0.02083 to +0.01611 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.7 | 60.17 | +0.8% | +0.05569 to +0.887 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1086 | 966.6 | -11.0% | -405.7 to +167.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3010 | 3323 | +10.4% | -417.9 to +1044 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.67 | 11.9 | -24.0% | -7.197 to -0.3385 | GAIN |
| failed requests (%) | 6.434 | 5.168 | -19.7% | -2.904 to +0.3721 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.492 | 11.4 | +20.1% | +0.04509 to +3.768 | power given |
| pods started | 6 | 9.8 | +63.3% | +1.869 to +5.731 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.086e-15 to +3.098e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.1 | -0.1% | -1.142 to +0.7638 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.1 | -0.1% | -1.142 to +0.7638 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.786 | 1.783 | -0.2% | -0.01723 to +0.01097 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.93 | 53.48 | +1.0% | -0.007655 to +1.098 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1531 | 1605 | +4.8% | -532.4 to +680.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4950 | 5398 | +9.0% | -672.5 to +1567 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 26.46 | 19.9 | -24.8% | -9.707 to -3.411 | GAIN |
| failed requests (%) | 11.89 | 10.06 | -15.4% | -3.207 to -0.4566 | GAIN |
| HPA replicas, mean | 9.666 | 12.78 | +32.2% | +1.644 to +4.589 | power given |
| pods started | 5.1 | 9.9 | +94.1% | +3.377 to +6.223 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.417e-15 to +1.735e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.2 | -0.0% | -1.12 to +0.9852 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.2 | -0.0% | -1.12 to +0.9852 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.165 | 2.166 | +0.0% | -0.02717 to +0.02768 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.07 | 64.57 | +0.8% | -0.2007 to +1.197 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08 | +0.08 | +0.04984 to +0.1102 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
