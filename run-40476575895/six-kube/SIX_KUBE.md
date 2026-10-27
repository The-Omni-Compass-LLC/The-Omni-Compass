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
| response time (ms), 95th percentile | 1882 | 1490 | 1704 | 1550 | 2276 | 2021 | 1900 | 1880 | 2044 | 1739 | 1549 | 1335 | 1958 | 1780 |
| response time (ms), 99th percentile | 5546 | 5217 | 5064 | 5058 | 6392 | 5914 | 5858 | 5875 | 4939 | 4679 | 3906 | 4267 | 5928 | 5733 |
| time over the response line (% of samples) | 18.78 | 13.72 | 24.2 | 18.32 | 23.4 | 17.43 | 19.59 | 14.8 | 28.7 | 20.82 | 23.73 | 16.9 | 31.4 | 23.44 |
| failed requests (%) | 6.351 | 5.826 | 10.51 | 9.391 | 8.269 | 7.456 | 6.604 | 5.788 | 9.88 | 8.78 | 9.739 | 7.73 | 13.6 | 12.45 |
| HPA replicas, mean | 9.579 | 13.28 | 9.637 | 12.73 | 9.647 | 13.86 | 9.605 | 13.41 | 9.615 | 13.53 | 9.578 | 11.61 | 9.716 | 12.97 |
| pods started | 5.55 | 9.9 | 5.3 | 11.4 | 5.1 | 10.75 | 5.4 | 9.9 | 5.1 | 9.6 | 5.35 | 10.05 | 4.75 | 10.35 |
| worker nodes in service, mean | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 179.5 | 181 | 181.1 | 182.3 | 180.9 | 181 | 180.3 | 181.8 | 181.7 | 179.7 | 179.6 | 183 | 183.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 179.5 | 180.9 | 181.1 | 182.3 | 180.9 | 181 | 180.3 | 181.8 | 181.7 | 179.7 | 179.6 | 183 | 183.5 |
| CPU used with Omni's own (cores), mean | 1.967 | 1.963 | 2.056 | 2.074 | 2.139 | 2.136 | 2.041 | 2.041 | 2.157 | 2.174 | 1.974 | 1.968 | 2.298 | 2.311 |
| host CPU busy, the real machine under kind (%) | 58.32 | 58.47 | 61.02 | 61.8 | 62.97 | 63.35 | 60.25 | 60.51 | 63.85 | 64.38 | 58.43 | 58.45 | 68.02 | 68.65 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.095 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 1

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1882 | 1490 | -20.9% | -732.8 to -52.18 | GAIN |
| response time (ms), 99th percentile | 5546 | 5217 | -5.9% | -740.5 to +83.19 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.78 | 13.72 | -26.9% | -6.816 to -3.3 | GAIN |
| failed requests (%) | 6.351 | 5.826 | -8.3% | -0.9223 to -0.1275 | GAIN |
| HPA replicas, mean | 9.579 | 13.28 | +38.6% | +2.799 to +4.595 | power given |
| pods started | 5.55 | 9.9 | +78.4% | +3.221 to +5.479 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.732e-16 to +3.956e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 179.5 | -0.5% | -1.529 to -0.1636 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 179.5 | -0.5% | -1.529 to -0.1636 | GAIN |
| CPU used with Omni's own (cores), mean | 1.967 | 1.963 | -0.2% | -0.01427 to +0.006892 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.32 | 58.47 | +0.3% | -0.08818 to +0.3838 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.958e+05 to +7.988e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.407e-05 to -9.371e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1704 | 1550 | -9.0% | -586.8 to +280.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5064 | 5058 | -0.1% | -608.5 to +595.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.2 | 18.32 | -24.3% | -8.289 to -3.468 | GAIN |
| failed requests (%) | 10.51 | 9.391 | -10.6% | -2.247 to +0.008686 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.637 | 12.73 | +32.1% | +2.313 to +3.869 | power given |
| pods started | 5.3 | 11.4 | +115.1% | +5.153 to +7.047 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.00191 to +0.005404 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 181.1 | +0.1% | -0.4877 to +0.7052 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 181.1 | +0.1% | -0.4475 to +0.7359 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.056 | 2.074 | +0.9% | +0.004714 to +0.03175 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.02 | 61.8 | +1.3% | +0.4748 to +1.094 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.63e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.148e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2276 | 2021 | -11.2% | -731.8 to +221.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6392 | 5914 | -7.5% | -1200 to +243.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.4 | 17.43 | -25.5% | -7.405 to -4.538 | GAIN |
| failed requests (%) | 8.269 | 7.456 | -9.8% | -1.54 to -0.08535 | GAIN |
| HPA replicas, mean | 9.647 | 13.86 | +43.7% | +3.467 to +4.964 | power given |
| pods started | 5.1 | 10.75 | +110.8% | +5.057 to +6.243 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.188e-16 to +4.635e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 180.9 | -0.8% | -2.085 to -0.7689 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 180.9 | -0.8% | -2.085 to -0.7689 | GAIN |
| CPU used with Omni's own (cores), mean | 2.139 | 2.136 | -0.1% | -0.01532 to +0.008985 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.97 | 63.35 | +0.6% | -0.002732 to +0.7625 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1900 | 1880 | -1.1% | -374.2 to +333.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5858 | 5875 | +0.3% | -554.1 to +589.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.59 | 14.8 | -24.5% | -6.22 to -3.37 | GAIN |
| failed requests (%) | 6.604 | 5.788 | -12.4% | -1.395 to -0.2378 | GAIN |
| HPA replicas, mean | 9.605 | 13.41 | +39.6% | +2.933 to +4.67 | power given |
| pods started | 5.4 | 9.9 | +83.3% | +3.534 to +5.466 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.013e-16 to +4.124e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.3 | -0.4% | -1.354 to -0.004324 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.3 | -0.4% | -1.354 to -0.004324 | GAIN |
| CPU used with Omni's own (cores), mean | 2.041 | 2.041 | -0.0% | -0.01293 to +0.01233 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.25 | 60.51 | +0.4% | -0.0758 to +0.5995 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2044 | 1739 | -14.9% | -494.3 to -115.8 | GAIN |
| response time (ms), 99th percentile | 4939 | 4679 | -5.3% | -865 to +345.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.7 | 20.82 | -27.5% | -10.55 to -5.206 | GAIN |
| failed requests (%) | 9.88 | 8.78 | -11.1% | -1.584 to -0.6145 | GAIN |
| HPA replicas, mean | 9.615 | 13.53 | +40.7% | +2.961 to +4.875 | power given |
| pods started | 5.1 | 9.6 | +88.2% | +3.198 to +5.802 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.576e-16 to +6.945e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.7 | -0.1% | -0.7342 to +0.5302 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.7 | -0.1% | -0.7342 to +0.5302 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.157 | 2.174 | +0.8% | +0.003888 to +0.03023 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.85 | 64.38 | +0.8% | +0.2163 to +0.8611 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1549 | 1335 | -13.8% | -528.1 to +100.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3906 | 4267 | +9.3% | -340.6 to +1063 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.73 | 16.9 | -28.8% | -9.935 to -3.721 | GAIN |
| failed requests (%) | 9.739 | 7.73 | -20.6% | -3.382 to -0.6363 | GAIN |
| HPA replicas, mean | 9.578 | 11.61 | +21.2% | +1.033 to +3.028 | power given |
| pods started | 5.35 | 10.05 | +87.9% | +3.484 to +5.916 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.614e-16 to +6.167e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.6 | -0.1% | -0.5715 to +0.3792 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.6 | -0.1% | -0.5715 to +0.3792 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.974 | 1.968 | -0.3% | -0.01889 to +0.005917 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.43 | 58.45 | +0.0% | -0.3232 to +0.3646 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1958 | 1780 | -9.1% | -474.3 to +118.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5928 | 5733 | -3.3% | -1029 to +639.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 31.4 | 23.44 | -25.4% | -10 to -5.923 | GAIN |
| failed requests (%) | 13.6 | 12.45 | -8.5% | -2.273 to -0.0298 | GAIN |
| HPA replicas, mean | 9.716 | 12.97 | +33.5% | +2.518 to +3.998 | power given |
| pods started | 4.75 | 10.35 | +117.9% | +4.82 to +6.38 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.654e-16 to +4.431e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.5 | +0.2% | -0.07223 to +0.968 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.5 | +0.2% | -0.07223 to +0.968 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.298 | 2.311 | +0.6% | -0.002998 to +0.03058 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.02 | 68.65 | +0.9% | +0.2961 to +0.9606 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.095 | +0.095 | +0.07656 to +0.1134 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
