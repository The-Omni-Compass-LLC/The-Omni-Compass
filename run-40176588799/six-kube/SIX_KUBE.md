# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1684 | 2023 | 1495 | 1650 | 2297 | 2479 | 2042 | 1863 | 1480 | 1434 | 3326 | 4416 | 1932 | 3361 |
| response time (ms), 99th percentile | 3956 | 4101 | 2729 | 2779 | 5426 | 5202 | 3889 | 4407 | 3389 | 3213 | 5935 | 6331 | 4565 | 5951 |
| time over the response line (% of samples) | 41.45 | 37.43 | 20.08 | 17.25 | 41.27 | 35.78 | 34.78 | 30.9 | 23.29 | 20.21 | 57.15 | 51.87 | 51.65 | 51.93 |
| failed requests (%) | 29.84 | 30.5 | 9.02 | 8.592 | 28.03 | 27.35 | 23.91 | 23.76 | 13.68 | 13.66 | 39.68 | 39.17 | 31.43 | 32.58 |
| HPA replicas, mean | 9.634 | 12.9 | 9.585 | 11.69 | 9.647 | 11.19 | 9.574 | 11.45 | 9.563 | 10.74 | 9.735 | 13.39 | 9.728 | 13.45 |
| pods started | 5 | 9 | 5.7 | 8.7 | 4.8 | 6.4 | 5.9 | 7.1 | 6.2 | 8.5 | 3.8 | 7.5 | 4 | 7.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 184.2 | 180.9 | 181.1 | 183.9 | 184.8 | 183.1 | 183.3 | 180.9 | 181.4 | 185.5 | 185 | 185.5 | 186 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184.2 | 180.9 | 181.1 | 183.9 | 184.8 | 183.1 | 183.3 | 180.9 | 181.4 | 185.5 | 185 | 185.5 | 186 |
| CPU used with Omni's own (cores), mean | 2.308 | 2.329 | 2.022 | 2.043 | 2.384 | 2.382 | 2.232 | 2.259 | 2.044 | 2.061 | 2.444 | 2.465 | 2.466 | 2.508 |
| host CPU busy, the real machine under kind (%) | 68.59 | 69.57 | 59.23 | 60.4 | 70.47 | 70.98 | 66.24 | 67.36 | 59.94 | 60.98 | 73.02 | 74.8 | 74.45 | 78.12 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.02 | 0 | 0.01 | 0 | 0.01 | 0 | 0.01 | 0 | 0 | 0.11 | 0.31 | 0.17 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1684 | 2023 | +20.2% | -908.1 to +1587 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3956 | 4101 | +3.7% | -894.8 to +1186 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.45 | 37.43 | -9.7% | -7.727 to -0.3044 | GAIN |
| failed requests (%) | 29.84 | 30.5 | +2.2% | -1.167 to +2.479 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.634 | 12.9 | +33.9% | +1.526 to +5.011 | power given |
| pods started | 5 | 9 | +80.0% | +1.841 to +6.159 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.159e-15 to +4.484e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 184.2 | +0.4% | +0.03841 to +1.592 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184.2 | +0.4% | +0.03841 to +1.592 | power given |
| CPU used with Omni's own (cores), mean | 2.308 | 2.329 | +0.9% | +0.00593 to +0.03663 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.59 | 69.57 | +1.4% | +0.3601 to +1.596 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.02 | +0.02 | -0.01016 to +0.05016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1495 | 1650 | +10.4% | -376.6 to +686.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 2729 | 2779 | +1.8% | -675.8 to +775.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.08 | 17.25 | -14.1% | -5.24 to -0.4165 | GAIN |
| failed requests (%) | 9.02 | 8.592 | -4.7% | -1.226 to +0.3699 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.585 | 11.69 | +21.9% | +0.2251 to +3.979 | power given |
| pods started | 5.7 | 8.7 | +52.6% | +0.713 to +5.287 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 181.1 | +0.1% | -0.6023 to +0.9942 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 181.1 | +0.1% | -0.6023 to +0.9942 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.022 | 2.043 | +1.0% | -0.004287 to +0.04603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.23 | 60.4 | +2.0% | +0.4284 to +1.911 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2297 | 2479 | +7.9% | -530.3 to +892.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5426 | 5202 | -4.1% | -1047 to +599 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 41.27 | 35.78 | -13.3% | -9.273 to -1.709 | GAIN |
| failed requests (%) | 28.03 | 27.35 | -2.5% | -1.845 to +0.4691 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.647 | 11.19 | +16.0% | -0.2446 to +3.329 | EVEN, inside the noise (up) |
| pods started | 4.8 | 6.4 | +33.3% | -0.5905 to +3.79 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.337e-15 to +2.707e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.8 | +0.5% | +0.3829 to +1.441 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.8 | +0.5% | +0.3829 to +1.441 | power given |
| CPU used with Omni's own (cores), mean | 2.384 | 2.382 | -0.1% | -0.02451 to +0.01911 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.47 | 70.98 | +0.7% | -0.2708 to +1.287 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2042 | 1863 | -8.7% | -1525 to +1168 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3889 | 4407 | +13.3% | -1059 to +2094 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 34.78 | 30.9 | -11.2% | -6.621 to -1.146 | GAIN |
| failed requests (%) | 23.91 | 23.76 | -0.6% | -1.738 to +1.429 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.574 | 11.45 | +19.6% | +0.08821 to +3.666 | power given |
| pods started | 5.9 | 7.1 | +20.3% | -0.9801 to +3.38 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 183.3 | +0.1% | -0.6346 to +1.028 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 183.3 | +0.1% | -0.6346 to +1.028 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.232 | 2.259 | +1.2% | +0.008235 to +0.04412 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.24 | 67.36 | +1.7% | +0.46 to +1.77 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 5 (pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1480 | 1434 | -3.2% | -998.5 to +904.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3389 | 3213 | -5.2% | -884 to +532.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.29 | 20.21 | -13.2% | -5.296 to -0.8632 | GAIN |
| failed requests (%) | 13.68 | 13.66 | -0.2% | -0.3815 to +0.3301 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.563 | 10.74 | +12.3% | -0.4444 to +2.795 | EVEN, inside the noise (up) |
| pods started | 6.2 | 8.5 | +37.1% | +0.166 to +4.434 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 181.4 | +0.3% | +0.006891 to +1.128 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 181.4 | +0.3% | +0.006891 to +1.128 | power given |
| CPU used with Omni's own (cores), mean | 2.044 | 2.061 | +0.8% | -0.00288 to +0.03712 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.94 | 60.98 | +1.7% | +0.3158 to +1.768 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3326 | 4416 | +32.8% | -146.1 to +2327 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5935 | 6331 | +6.7% | -842.1 to +1634 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 57.15 | 51.87 | -9.2% | -8.61 to -1.945 | GAIN |
| failed requests (%) | 39.68 | 39.17 | -1.3% | -2.193 to +1.179 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.735 | 13.39 | +37.5% | +2.231 to +5.078 | power given |
| pods started | 3.8 | 7.5 | +97.4% | +1.979 to +5.421 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +9.868e-17 to +1.145e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185 | -0.3% | -1.537 to +0.5223 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 185 | -0.3% | -1.537 to +0.5223 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.444 | 2.465 | +0.8% | +0.01286 to +0.02777 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.02 | 74.8 | +2.4% | +1.574 to +1.989 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.11 | 0.31 | +181.8% | +0.09884 to +0.3012 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1932 | 3361 | +73.9% | +350.4 to +2506 | LOSS |
| response time (ms), 99th percentile | 4565 | 5951 | +30.4% | -514.4 to +3286 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 51.65 | 51.93 | +0.5% | -2.896 to +3.449 | EVEN, inside the noise (up) |
| failed requests (%) | 31.43 | 32.58 | +3.6% | -0.2784 to +2.571 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.728 | 13.45 | +38.3% | +2.703 to +4.748 | power given |
| pods started | 4 | 7.7 | +92.5% | +1.791 to +5.609 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.608e-15 to +1.252e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 186 | +0.3% | -0.5582 to +1.487 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 186 | +0.3% | -0.5582 to +1.487 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.466 | 2.508 | +1.7% | +0.0289 to +0.05431 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.45 | 78.12 | +4.9% | +3.417 to +3.925 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.17 | 0.2 | +17.6% | -0.03786 to +0.09786 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
