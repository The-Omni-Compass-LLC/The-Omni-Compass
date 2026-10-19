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
| response time (ms), 95th percentile | 1939 | 1656 | 1431 | 1274 | 1754 | 1585 | 1745 | 1672 | 1823 | 1546 | 2013 | 2046 | 1564 | 1493 |
| response time (ms), 99th percentile | 5526 | 5326 | 4211 | 4251 | 5205 | 4829 | 5233 | 5137 | 4719 | 4638 | 4875 | 5167 | 4889 | 4626 |
| time over the response line (% of samples) | 19.65 | 14.4 | 24.37 | 18.54 | 18.31 | 13.53 | 18.7 | 13.9 | 26.05 | 18.75 | 32.97 | 24.82 | 25.86 | 19.34 |
| failed requests (%) | 6.638 | 6.172 | 10.96 | 9.633 | 5.661 | 5.46 | 6.28 | 5.729 | 8.289 | 7.414 | 14.22 | 11.66 | 11.61 | 9.71 |
| HPA replicas, mean | 9.636 | 13.72 | 9.612 | 12.3 | 9.579 | 13.29 | 9.591 | 13.28 | 9.607 | 13.54 | 9.646 | 13.18 | 9.656 | 12.17 |
| pods started | 4.971 | 10.11 | 5.629 | 9.714 | 5.657 | 10.26 | 5.286 | 9.571 | 5.171 | 10 | 4.857 | 9.857 | 5.229 | 9.829 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.2 | 180.5 | 180.6 | 180.2 | 179.5 | 180.4 | 179.4 | 181.8 | 181.9 | 182.3 | 182.6 | 181.3 | 181.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.2 | 180.5 | 180.6 | 180.2 | 179.5 | 180.4 | 179.4 | 181.8 | 181.9 | 182.3 | 182.6 | 181.3 | 181.1 |
| CPU used with Omni's own (cores), mean | 2.031 | 2.03 | 2.035 | 2.044 | 1.953 | 1.962 | 1.966 | 1.967 | 2.14 | 2.15 | 2.216 | 2.224 | 2.109 | 2.106 |
| host CPU busy, the real machine under kind (%) | 59.93 | 60.38 | 60.37 | 60.77 | 57.86 | 58.45 | 58.25 | 58.67 | 63.32 | 63.8 | 65.65 | 66.05 | 62.58 | 62.78 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1939 | 1656 | -14.6% | -603 to +37.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5526 | 5326 | -3.6% | -512.7 to +114.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.65 | 14.4 | -26.7% | -6.461 to -4.046 | GAIN |
| failed requests (%) | 6.638 | 6.172 | -7.0% | -0.8323 to -0.1008 | GAIN |
| HPA replicas, mean | 9.636 | 13.72 | +42.4% | +3.395 to +4.768 | power given |
| pods started | 4.971 | 10.11 | +103.4% | +4.361 to +5.925 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.185e-16 to -4.431e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.2 | -0.5% | -1.278 to -0.3559 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.2 | -0.5% | -1.278 to -0.3559 | GAIN |
| CPU used with Omni's own (cores), mean | 2.031 | 2.03 | -0.0% | -0.007936 to +0.006656 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.93 | 60.38 | +0.7% | +0.2223 to +0.6664 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +7.985e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.403e-05 to -9.394e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1431 | 1274 | -11.0% | -368.8 to +55 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4211 | 4251 | +1.0% | -337.4 to +418.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 24.37 | 18.54 | -23.9% | -7.639 to -4.025 | GAIN |
| failed requests (%) | 10.96 | 9.633 | -12.1% | -1.806 to -0.8473 | GAIN |
| HPA replicas, mean | 9.612 | 12.3 | +28.0% | +1.962 to +3.412 | power given |
| pods started | 5.629 | 9.714 | +72.6% | +3.303 to +4.869 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.221e-16 to +5.251e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.6 | +0.0% | -0.3591 to +0.5311 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.6 | +0.0% | -0.3591 to +0.5311 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.035 | 2.044 | +0.5% | -0.001726 to +0.02016 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.37 | 60.77 | +0.7% | +0.1639 to +0.6324 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1754 | 1585 | -9.6% | -474 to +137.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5205 | 4829 | -7.2% | -821.1 to +70.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.31 | 13.53 | -26.1% | -6.025 to -3.55 | GAIN |
| failed requests (%) | 5.661 | 5.46 | -3.5% | -0.6624 to +0.2608 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.579 | 13.29 | +38.7% | +2.974 to +4.445 | power given |
| pods started | 5.657 | 10.26 | +81.3% | +3.809 to +5.391 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.49e-16 to +8.921e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.5 | -0.4% | -1.178 to -0.2082 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.5 | -0.4% | -1.178 to -0.2082 | GAIN |
| CPU used with Omni's own (cores), mean | 1.953 | 1.962 | +0.5% | -0.0003779 to +0.01797 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.86 | 58.45 | +1.0% | +0.3374 to +0.834 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1745 | 1672 | -4.2% | -363.7 to +218.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5233 | 5137 | -1.8% | -501.4 to +309.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.7 | 13.9 | -25.7% | -5.928 to -3.668 | GAIN |
| failed requests (%) | 6.28 | 5.729 | -8.8% | -0.9733 to -0.1293 | GAIN |
| HPA replicas, mean | 9.591 | 13.28 | +38.5% | +2.92 to +4.459 | power given |
| pods started | 5.286 | 9.571 | +81.1% | +3.334 to +5.238 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.4 | -0.6% | -1.526 to -0.5323 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.4 | -0.6% | -1.526 to -0.5323 | GAIN |
| CPU used with Omni's own (cores), mean | 1.966 | 1.967 | +0.0% | -0.007139 to +0.009085 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.25 | 58.67 | +0.7% | +0.207 to +0.6334 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1823 | 1546 | -15.2% | -484.8 to -69.93 | GAIN |
| response time (ms), 99th percentile | 4719 | 4638 | -1.7% | -441.4 to +278.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.05 | 18.75 | -28.0% | -8.941 to -5.662 | GAIN |
| failed requests (%) | 8.289 | 7.414 | -10.6% | -1.314 to -0.4365 | GAIN |
| HPA replicas, mean | 9.607 | 13.54 | +41.0% | +3.32 to +4.554 | power given |
| pods started | 5.171 | 10 | +93.4% | +3.989 to +5.668 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.589e-16 to +2.052e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.9 | +0.0% | -0.4593 to +0.5222 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.9 | +0.0% | -0.4593 to +0.5222 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.14 | 2.15 | +0.5% | -0.0001297 to +0.01994 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.32 | 63.8 | +0.8% | +0.2547 to +0.6992 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2013 | 2046 | +1.6% | -207.2 to +272.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4875 | 5167 | +6.0% | -234.4 to +819.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 32.97 | 24.82 | -24.7% | -10.01 to -6.284 | GAIN |
| failed requests (%) | 14.22 | 11.66 | -18.0% | -3.648 to -1.483 | GAIN |
| HPA replicas, mean | 9.646 | 13.18 | +36.6% | +2.879 to +4.187 | power given |
| pods started | 4.857 | 9.857 | +102.9% | +4.032 to +5.968 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.858e-16 to -2.628e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.6 | +0.1% | -0.2049 to +0.7098 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.6 | +0.1% | -0.2049 to +0.7098 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.216 | 2.224 | +0.4% | -0.004022 to +0.02013 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.65 | 66.05 | +0.6% | +0.07703 to +0.7307 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1564 | 1493 | -4.5% | -230.5 to +89.95 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4889 | 4626 | -5.4% | -716.6 to +189.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 25.86 | 19.34 | -25.2% | -8.454 to -4.572 | GAIN |
| failed requests (%) | 11.61 | 9.71 | -16.4% | -2.803 to -0.9998 | GAIN |
| HPA replicas, mean | 9.656 | 12.17 | +26.1% | +1.903 to +3.129 | power given |
| pods started | 5.229 | 9.829 | +88.0% | +3.657 to +5.543 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.585e-16 to +1.525e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 181.1 | -0.1% | -0.5499 to +0.2462 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 181.1 | -0.1% | -0.5499 to +0.2462 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.109 | 2.106 | -0.2% | -0.01399 to +0.006574 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.58 | 62.78 | +0.3% | -0.05826 to +0.4555 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.09143 | +0.0914 | +0.07613 to +0.1067 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
