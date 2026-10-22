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
| response time (ms), 95th percentile | 1738 | 1678 | 1078 | 1059 | 1474 | 1394 | 1316 | 1596 | 1898 | 1632 | 1946 | 2092 | 1632 | 1514 |
| response time (ms), 99th percentile | 4759 | 4749 | 3620 | 3002 | 4621 | 4618 | 4696 | 4729 | 4844 | 4331 | 4750 | 5044 | 5167 | 5247 |
| time over the response line (% of samples) | 15.91 | 12.36 | 14.55 | 10.98 | 19.07 | 12.98 | 17.16 | 13.8 | 28.93 | 19.65 | 34.2 | 25.76 | 30.57 | 21.04 |
| failed requests (%) | 5.324 | 4.224 | 5.992 | 4.951 | 6.569 | 5.151 | 6.685 | 5.81 | 9.784 | 8.713 | 13.64 | 11.51 | 13.58 | 10.54 |
| HPA replicas, mean | 9.55 | 12.68 | 9.55 | 10.69 | 9.589 | 13.17 | 9.591 | 12.86 | 9.597 | 13.64 | 9.684 | 13.5 | 9.685 | 12.75 |
| pods started | 5.7 | 9.9 | 6 | 9.7 | 5.2 | 9.9 | 5 | 9.2 | 5.1 | 9.6 | 4.1 | 10.4 | 4.9 | 9.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.4 | 178.6 | 178.2 | 179.9 | 179.5 | 178.8 | 179.3 | 181.9 | 181.7 | 183.2 | 182.8 | 182.9 | 183.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.4 | 178.6 | 178.2 | 179.9 | 179.5 | 178.8 | 179.3 | 181.9 | 181.7 | 183.2 | 182.8 | 182.9 | 183.2 |
| CPU used with Omni's own (cores), mean | 1.862 | 1.868 | 1.807 | 1.793 | 1.951 | 1.933 | 1.877 | 1.886 | 2.122 | 2.134 | 2.236 | 2.246 | 2.255 | 2.249 |
| host CPU busy, the real machine under kind (%) | 55.53 | 55.76 | 53.82 | 53.67 | 57.95 | 57.68 | 56.17 | 56.3 | 62.97 | 63.44 | 66.54 | 66.9 | 66.58 | 66.92 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1738 | 1678 | -3.4% | -507.6 to +387.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4759 | 4749 | -0.2% | -415.4 to +395.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 15.91 | 12.36 | -22.3% | -5.553 to -1.555 | GAIN |
| failed requests (%) | 5.324 | 4.224 | -20.6% | -2.33 to +0.1311 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.55 | 12.68 | +32.8% | +1.524 to +4.745 | power given |
| pods started | 5.7 | 9.9 | +73.7% | +2.1 to +6.3 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.805e-16 to +8.91e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.4 | +0.1% | -1.016 to +1.437 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.4 | +0.1% | -1.016 to +1.437 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.862 | 1.868 | +0.3% | -0.01065 to +0.02156 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.53 | 55.76 | +0.4% | -0.1622 to +0.6211 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +7.992e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.411e-05 to -9.394e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1078 | 1059 | -1.8% | -451.9 to +413.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3620 | 3002 | -17.1% | -1375 to +140.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.55 | 10.98 | -24.6% | -7.312 to +0.163 | EVEN, inside the noise (cut) |
| failed requests (%) | 5.992 | 4.951 | -17.4% | -2.897 to +0.8158 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.55 | 10.69 | +11.9% | +0.05278 to +2.22 | power given |
| pods started | 6 | 9.7 | +61.7% | +1.761 to +5.639 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 178.2 | -0.2% | -1.172 to +0.454 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 178.2 | -0.2% | -1.172 to +0.454 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.807 | 1.793 | -0.8% | -0.04321 to +0.01567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.82 | 53.67 | -0.3% | -1.028 to +0.7245 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.614e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.138e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1474 | 1394 | -5.4% | -870.5 to +711 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4621 | 4618 | -0.1% | -747.6 to +741.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.07 | 12.98 | -32.0% | -10.53 to -1.661 | GAIN |
| failed requests (%) | 6.569 | 5.151 | -21.6% | -2.832 to -0.003517 | GAIN |
| HPA replicas, mean | 9.589 | 13.17 | +37.3% | +1.973 to +5.18 | power given |
| pods started | 5.2 | 9.9 | +90.4% | +2.914 to +6.486 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.003e-15 to +4.702e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179.5 | -0.2% | -1.169 to +0.3849 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179.5 | -0.2% | -1.169 to +0.3849 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.951 | 1.933 | -0.9% | -0.05851 to +0.02347 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.95 | 57.68 | -0.5% | -1.364 to +0.825 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.241e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1316 | 1596 | +21.2% | -137.6 to +696.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4696 | 4729 | +0.7% | -687.1 to +752.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.16 | 13.8 | -19.6% | -5.601 to -1.116 | GAIN |
| failed requests (%) | 6.685 | 5.81 | -13.1% | -1.757 to +0.006714 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.591 | 12.86 | +34.1% | +1.426 to +5.113 | power given |
| pods started | 5 | 9.2 | +84.0% | +2.1 to +6.3 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.395e-16 to +4.066e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.3 | +0.3% | -0.6019 to +1.519 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.3 | +0.3% | -0.6019 to +1.519 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.877 | 1.886 | +0.5% | -0.01926 to +0.03725 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.17 | 56.3 | +0.2% | -0.6819 to +0.9401 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1898 | 1632 | -14.0% | -761.2 to +228.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4844 | 4331 | -10.6% | -1327 to +301.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.93 | 19.65 | -32.1% | -14.17 to -4.381 | GAIN |
| failed requests (%) | 9.784 | 8.713 | -10.9% | -1.898 to -0.2438 | GAIN |
| HPA replicas, mean | 9.597 | 13.64 | +42.1% | +2.553 to +5.533 | power given |
| pods started | 5.1 | 9.6 | +88.2% | +2.806 to +6.194 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.7 | -0.1% | -1.281 to +0.9545 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.7 | -0.1% | -1.281 to +0.9545 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.122 | 2.134 | +0.5% | -0.006092 to +0.02873 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.97 | 63.44 | +0.7% | -0.01759 to +0.9587 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1946 | 2092 | +7.5% | -886.5 to +1179 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4750 | 5044 | +6.2% | -972.1 to +1561 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 34.2 | 25.76 | -24.7% | -14.46 to -2.41 | GAIN |
| failed requests (%) | 13.64 | 11.51 | -15.6% | -5.742 to +1.481 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.684 | 13.5 | +39.4% | +2.498 to +5.126 | power given |
| pods started | 4.1 | 10.4 | +153.7% | +4.681 to +7.919 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 182.8 | -0.2% | -1.526 to +0.74 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 182.8 | -0.2% | -1.526 to +0.74 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.236 | 2.246 | +0.5% | -0.01556 to +0.0362 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.54 | 66.9 | +0.5% | -0.3665 to +1.074 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1632 | 1514 | -7.2% | -400.4 to +164 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5167 | 5247 | +1.5% | -1122 to +1281 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 30.57 | 21.04 | -31.2% | -16.53 to -2.546 | GAIN |
| failed requests (%) | 13.58 | 10.54 | -22.4% | -7.588 to +1.506 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.685 | 12.75 | +31.6% | +1.872 to +4.256 | power given |
| pods started | 4.9 | 9.7 | +98.0% | +3.503 to +6.097 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.187e-15 to +1.01e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.2 | +0.2% | -0.5987 to +1.195 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.2 | +0.2% | -0.5987 to +1.195 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.255 | 2.249 | -0.3% | -0.05575 to +0.04314 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.58 | 66.92 | +0.5% | -0.8729 to +1.543 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.987e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08 | +0.08 | +0.04984 to +0.1102 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
