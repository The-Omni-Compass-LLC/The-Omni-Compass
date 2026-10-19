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
| response time (ms), 95th percentile | 2034 | 1965 | 1393 | 1214 | 2086 | 1632 | 1524 | 1433 | 2106 | 1823 | 1867 | 1791 | 1541 | 1251 |
| response time (ms), 99th percentile | 5384 | 5647 | 4414 | 4188 | 6108 | 5677 | 5313 | 4597 | 5670 | 5671 | 4692 | 4798 | 4352 | 4267 |
| time over the response line (% of samples) | 20.26 | 14.91 | 23.48 | 17.64 | 21.22 | 15.53 | 17.8 | 12.93 | 31.78 | 22.69 | 27.99 | 20.4 | 28.1 | 20.69 |
| failed requests (%) | 6.974 | 6.392 | 9.679 | 9.212 | 7.065 | 6.822 | 5.54 | 5.082 | 10.69 | 9.863 | 12.33 | 9.325 | 12.86 | 11.25 |
| HPA replicas, mean | 9.622 | 13.65 | 9.619 | 12.49 | 9.633 | 13.85 | 9.572 | 13.21 | 9.647 | 14.05 | 9.584 | 12.69 | 9.661 | 12.21 |
| pods started | 5.3 | 9.7 | 5.5 | 10.25 | 5.15 | 9.85 | 5.6 | 9.7 | 4.9 | 9.9 | 5.3 | 9.55 | 5.1 | 10.05 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180 | 180.3 | 180.5 | 181.4 | 180.7 | 179.3 | 178.7 | 183.4 | 183.2 | 180.4 | 180.9 | 181.5 | 181.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180 | 180.3 | 180.5 | 181.4 | 180.7 | 179.3 | 178.7 | 183.4 | 183.2 | 180.4 | 180.9 | 181.5 | 181.5 |
| CPU used with Omni's own (cores), mean | 2.023 | 2.022 | 2.024 | 2.036 | 2.072 | 2.074 | 1.899 | 1.909 | 2.278 | 2.299 | 2.074 | 2.075 | 2.129 | 2.133 |
| host CPU busy, the real machine under kind (%) | 59.88 | 60.16 | 60.13 | 60.59 | 61.05 | 61.52 | 57.99 | 58.28 | 67.31 | 67.85 | 61.51 | 61.62 | 63.3 | 63.61 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2034 | 1965 | -3.4% | -474.4 to +336.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5384 | 5647 | +4.9% | -172.2 to +696.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.26 | 14.91 | -26.4% | -7.384 to -3.317 | GAIN |
| failed requests (%) | 6.974 | 6.392 | -8.3% | -1.271 to +0.1071 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.622 | 13.65 | +41.9% | +3.021 to +5.039 | power given |
| pods started | 5.3 | 9.7 | +83.0% | +3.29 to +5.51 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.069e-15 to -8.594e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180 | -0.6% | -1.634 to -0.3879 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180 | -0.6% | -1.634 to -0.3879 | GAIN |
| CPU used with Omni's own (cores), mean | 2.023 | 2.022 | -0.1% | -0.01251 to +0.01019 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.88 | 60.16 | +0.5% | -0.06413 to +0.632 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.975e+05 to +7.987e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.405e-05 to -9.391e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1393 | 1214 | -12.8% | -437.6 to +79.92 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4414 | 4188 | -5.1% | -969.9 to +519.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.48 | 17.64 | -24.9% | -8.514 to -3.163 | GAIN |
| failed requests (%) | 9.679 | 9.212 | -4.8% | -1.317 to +0.3833 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.619 | 12.49 | +29.8% | +1.833 to +3.908 | power given |
| pods started | 5.5 | 10.25 | +86.4% | +3.565 to +5.935 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.338e-16 to +2.232e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180.5 | +0.2% | -0.2074 to +0.7841 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180.5 | +0.2% | -0.2074 to +0.7841 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.024 | 2.036 | +0.6% | +0.0005338 to +0.02292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.13 | 60.59 | +0.8% | +0.1963 to +0.7326 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 6 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 1

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2086 | 1632 | -21.8% | -829 to -78.39 | GAIN |
| response time (ms), 99th percentile | 6108 | 5677 | -7.1% | -835.1 to -28.1 | GAIN |
| time over the response line (% of samples) | 21.22 | 15.53 | -26.8% | -7.571 to -3.812 | GAIN |
| failed requests (%) | 7.065 | 6.822 | -3.4% | -0.7513 to +0.2642 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.633 | 13.85 | +43.7% | +3.316 to +5.109 | power given |
| pods started | 5.15 | 9.85 | +91.3% | +3.543 to +5.857 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.493e-16 to +2.387e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.7 | -0.4% | -1.453 to -0.08222 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.7 | -0.4% | -1.453 to -0.08222 | GAIN |
| CPU used with Omni's own (cores), mean | 2.072 | 2.074 | +0.1% | -0.006887 to +0.01251 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.05 | 61.52 | +0.8% | +0.2036 to +0.7309 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1524 | 1433 | -6.0% | -600.2 to +417.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5313 | 4597 | -13.5% | -1283 to -149.7 | GAIN |
| time over the response line (% of samples) | 17.8 | 12.93 | -27.3% | -6.753 to -2.982 | GAIN |
| failed requests (%) | 5.54 | 5.082 | -8.3% | -1.06 to +0.1451 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.572 | 13.21 | +38.1% | +2.604 to +4.68 | power given |
| pods started | 5.6 | 9.7 | +73.2% | +2.84 to +5.36 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.829e-16 to +7.158e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.7 | -0.3% | -1.103 to +0.0482 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.7 | -0.3% | -1.103 to +0.0482 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.899 | 1.909 | +0.5% | -0.001018 to +0.02093 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.99 | 58.28 | +0.5% | -0.008356 to +0.5962 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2106 | 1823 | -13.4% | -477.5 to -88.13 | GAIN |
| response time (ms), 99th percentile | 5670 | 5671 | +0.0% | -637.7 to +639.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 31.78 | 22.69 | -28.6% | -11.18 to -6.997 | GAIN |
| failed requests (%) | 10.69 | 9.863 | -7.8% | -1.223 to -0.4375 | GAIN |
| HPA replicas, mean | 9.647 | 14.05 | +45.6% | +3.655 to +5.145 | power given |
| pods started | 4.9 | 9.9 | +102.0% | +3.864 to +6.136 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.204e-16 to +1.987e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.2 | -0.1% | -0.8936 to +0.516 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.2 | -0.1% | -0.8936 to +0.516 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.278 | 2.299 | +0.9% | +0.008753 to +0.03375 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.31 | 67.85 | +0.8% | +0.2046 to +0.871 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1867 | 1791 | -4.1% | -315.5 to +164.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4692 | 4798 | +2.3% | -464.7 to +677 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.99 | 20.4 | -27.1% | -10.76 to -4.414 | GAIN |
| failed requests (%) | 12.33 | 9.325 | -24.4% | -4.794 to -1.215 | GAIN |
| HPA replicas, mean | 9.584 | 12.69 | +32.4% | +2.015 to +4.197 | power given |
| pods started | 5.3 | 9.55 | +80.2% | +3.328 to +5.172 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.084e-15 to +1.067e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.9 | +0.3% | +0.07175 to +0.9365 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.9 | +0.3% | +0.07175 to +0.9365 | power given |
| CPU used with Omni's own (cores), mean | 2.074 | 2.075 | +0.1% | -0.01046 to +0.01259 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.51 | 61.62 | +0.2% | -0.1873 to +0.4223 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1541 | 1251 | -18.8% | -524.3 to -55.27 | GAIN |
| response time (ms), 99th percentile | 4352 | 4267 | -1.9% | -688.2 to +519.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.1 | 20.69 | -26.4% | -10.74 to -4.079 | GAIN |
| failed requests (%) | 12.86 | 11.25 | -12.5% | -2.853 to -0.3597 | GAIN |
| HPA replicas, mean | 9.661 | 12.21 | +26.4% | +1.641 to +3.458 | power given |
| pods started | 5.1 | 10.05 | +97.1% | +3.721 to +6.179 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.868e-16 to +2.427e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.5 | +0.0% | -0.5091 to +0.6877 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.5 | +0.0% | -0.5091 to +0.6877 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.129 | 2.133 | +0.2% | -0.01397 to +0.02068 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.3 | 63.61 | +0.5% | -0.1261 to +0.7452 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.085 | +0.085 | +0.06785 to +0.1021 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
