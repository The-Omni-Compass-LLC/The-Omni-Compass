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
| response time (ms), 95th percentile | 1995 | 2444 | 1419 | 1752 | 1572 | 1139 | 2061 | 1635 | 1984 | 1799 | 1864 | 1586 | 1489 | 1386 |
| response time (ms), 99th percentile | 6380 | 6331 | 5156 | 6220 | 4618 | 4208 | 5498 | 5521 | 5535 | 5111 | 4446 | 4064 | 4810 | 4749 |
| time over the response line (% of samples) | 24.06 | 17.83 | 29.09 | 22.93 | 16.22 | 12.4 | 19.09 | 14.28 | 32.14 | 24.79 | 23.32 | 17.82 | 25.5 | 17.37 |
| failed requests (%) | 8.721 | 7.731 | 13.64 | 11.67 | 6.014 | 5.721 | 7.721 | 6.406 | 11.58 | 11.19 | 10.41 | 7.81 | 10.97 | 8.738 |
| HPA replicas, mean | 9.684 | 14.58 | 9.692 | 13.94 | 9.533 | 13.68 | 9.604 | 13.81 | 9.613 | 14.41 | 9.543 | 13.18 | 9.69 | 13.9 |
| pods started | 4.5 | 10.6 | 4.9 | 11.5 | 5.6 | 11.5 | 5 | 10.6 | 4.8 | 10 | 5.4 | 11.5 | 4.5 | 11.3 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.4 | 182.8 | 183.6 | 178.6 | 179 | 179.9 | 179.7 | 182.2 | 183 | 179.5 | 180 | 181.9 | 181.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.4 | 182.8 | 183.6 | 178.6 | 179 | 179.9 | 179.7 | 182.2 | 183 | 179.5 | 180 | 181.9 | 181.4 |
| CPU used with Omni's own (cores), mean | 2.168 | 2.185 | 2.264 | 2.293 | 1.849 | 1.884 | 1.956 | 1.968 | 2.224 | 2.262 | 1.945 | 1.96 | 2.098 | 2.108 |
| host CPU busy, the real machine under kind (%) | 63.71 | 64.9 | 66.96 | 68.1 | 54.95 | 56.32 | 58.01 | 58.64 | 65.68 | 67.05 | 57.77 | 58.81 | 62.19 | 62.86 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1995 | 2444 | +22.5% | -347.8 to +1246 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6380 | 6331 | -0.8% | -839.7 to +742.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.06 | 17.83 | -25.9% | -8.736 to -3.72 | GAIN |
| failed requests (%) | 8.721 | 7.731 | -11.4% | -1.797 to -0.1844 | GAIN |
| HPA replicas, mean | 9.684 | 14.58 | +50.5% | +4.105 to +5.678 | power given |
| pods started | 4.5 | 10.6 | +135.6% | +5.474 to +6.726 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.881e-15 to +1.051e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.4 | +0.1% | -0.6093 to +1.12 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.4 | +0.1% | -0.6093 to +1.12 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.168 | 2.185 | +0.8% | +0.0001506 to +0.03373 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.71 | 64.9 | +1.9% | +0.8296 to +1.55 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.938e+05 to +7.996e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.347e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1419 | 1752 | +23.5% | -160.1 to +827.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5156 | 6220 | +20.6% | +560.3 to +1567 | LOSS |
| time over the response line (% of samples) | 29.09 | 22.93 | -21.2% | -8.567 to -3.747 | GAIN |
| failed requests (%) | 13.64 | 11.67 | -14.4% | -3.242 to -0.6957 | GAIN |
| HPA replicas, mean | 9.692 | 13.94 | +43.8% | +3.479 to +5.018 | power given |
| pods started | 4.9 | 11.5 | +134.7% | +5.634 to +7.566 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.6 | +0.4% | +0.04477 to +1.401 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.6 | +0.4% | +0.04477 to +1.401 | power given |
| CPU used with Omni's own (cores), mean | 2.264 | 2.293 | +1.3% | +0.01335 to +0.04464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.96 | 68.1 | +1.7% | +0.8329 to +1.453 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.63e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1572 | 1139 | -27.5% | -956.2 to +90.63 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4618 | 4208 | -8.9% | -1164 to +343.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 16.22 | 12.4 | -23.6% | -6.508 to -1.142 | GAIN |
| failed requests (%) | 6.014 | 5.721 | -4.9% | -0.7577 to +0.1707 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.533 | 13.68 | +43.5% | +2.958 to +5.339 | power given |
| pods started | 5.6 | 11.5 | +105.4% | +4.71 to +7.09 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.154e-15 to +2.002e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 179 | +0.2% | -0.3012 to +1.117 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 179 | +0.2% | -0.3012 to +1.117 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.849 | 1.884 | +1.9% | +0.02432 to +0.04565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.95 | 56.32 | +2.5% | +1.071 to +1.667 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2061 | 1635 | -20.7% | -1490 to +637.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5498 | 5521 | +0.4% | -658.1 to +704.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.09 | 14.28 | -25.2% | -9.234 to -0.3876 | GAIN |
| failed requests (%) | 7.721 | 6.406 | -17.0% | -4.237 to +1.606 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 13.81 | +43.8% | +2.942 to +5.478 | power given |
| pods started | 5 | 10.6 | +112.0% | +4.011 to +7.189 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179.7 | -0.1% | -1.316 to +0.9566 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179.7 | -0.1% | -1.316 to +0.9566 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.956 | 1.968 | +0.6% | -0.01773 to +0.04199 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.01 | 58.64 | +1.1% | -0.2022 to +1.457 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1984 | 1799 | -9.3% | -720.4 to +350 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5535 | 5111 | -7.7% | -1227 to +378.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 32.14 | 24.79 | -22.9% | -11.18 to -3.515 | GAIN |
| failed requests (%) | 11.58 | 11.19 | -3.3% | -0.8492 to +0.07388 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.613 | 14.41 | +49.9% | +4.019 to +5.578 | power given |
| pods started | 4.8 | 10 | +108.3% | +4.321 to +6.079 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.471e-15 to +2.28e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 183 | +0.4% | +0.02088 to +1.581 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 183 | +0.4% | +0.02088 to +1.581 | power given |
| CPU used with Omni's own (cores), mean | 2.224 | 2.262 | +1.7% | +0.02482 to +0.05124 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.68 | 67.05 | +2.1% | +0.857 to +1.881 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1864 | 1586 | -14.9% | -1489 to +933.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4446 | 4064 | -8.6% | -1248 to +483.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.32 | 17.82 | -23.6% | -9.806 to -1.189 | GAIN |
| failed requests (%) | 10.41 | 7.81 | -25.0% | -5.533 to +0.3312 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.543 | 13.18 | +38.1% | +2.289 to +4.982 | power given |
| pods started | 5.4 | 11.5 | +113.0% | +4.467 to +7.733 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.338e-16 to +4.785e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 180 | +0.3% | -0.3661 to +1.3 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 180 | +0.3% | -0.3661 to +1.3 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.945 | 1.96 | +0.8% | -0.006297 to +0.03615 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.77 | 58.81 | +1.8% | +0.5615 to +1.506 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1489 | 1386 | -6.9% | -776.2 to +570.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4810 | 4749 | -1.3% | -1256 to +1135 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 25.5 | 17.37 | -31.9% | -13.42 to -2.839 | GAIN |
| failed requests (%) | 10.97 | 8.738 | -20.3% | -4.501 to +0.04035 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.69 | 13.9 | +43.5% | +3.07 to +5.357 | power given |
| pods started | 4.5 | 11.3 | +151.1% | +5.8 to +7.8 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.01e-15 to +1.187e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.4 | -0.3% | -1.475 to +0.517 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.4 | -0.3% | -1.475 to +0.517 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.098 | 2.108 | +0.5% | -0.0101 to +0.03015 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.19 | 62.86 | +1.1% | +0.1429 to +1.198 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.07 | +0.07 | +0.03545 to +0.1046 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
