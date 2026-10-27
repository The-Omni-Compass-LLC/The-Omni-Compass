# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2573 | 2638 | 2144 | 2754 | 2513 | 2340 | 2684 | 2555 | 2972 | 3025 | 2978 | 3612 | 2192 | 2697 |
| response time (ms), 99th percentile | 6010 | 5731 | 5255 | 5792 | 5452 | 5140 | 5782 | 5739 | 5650 | 5556 | 4893 | 5430 | 4296 | 4634 |
| time over the response line (% of samples) | 47.71 | 44.25 | 45.5 | 41.28 | 38.99 | 35.81 | 47.59 | 42.63 | 49.03 | 45.05 | 41.68 | 38.84 | 32.44 | 31.07 |
| failed requests (%) | 32.94 | 33.12 | 27.22 | 26.43 | 27.03 | 27.76 | 31.83 | 31.47 | 31.72 | 31.23 | 27.23 | 26.62 | 15.72 | 17.05 |
| HPA replicas, mean | 9.685 | 12.62 | 9.693 | 13.93 | 9.638 | 12.34 | 9.657 | 12.01 | 9.676 | 12.9 | 9.68 | 12.92 | 9.642 | 12.06 |
| pods started | 4.486 | 8.057 | 4.4 | 9.257 | 4.771 | 7.943 | 5.057 | 7.257 | 4.829 | 8.4 | 4.529 | 8.5 | 5.229 | 7.6 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 | 6 | 5.996 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.1 | 184.3 | 184.4 | 183.7 | 183.1 | 185 | 185.3 | 184.3 | 184.5 | 183.8 | 183.2 | 182.9 | 182.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.1 | 184.3 | 184.4 | 183.7 | 183 | 185 | 185.3 | 184.3 | 184.5 | 183.8 | 183.2 | 182.9 | 182.9 |
| CPU used with Omni's own (cores), mean | 2.45 | 2.465 | 2.394 | 2.426 | 2.317 | 2.332 | 2.45 | 2.468 | 2.392 | 2.409 | 2.28 | 2.306 | 2.207 | 2.238 |
| host CPU busy, the real machine under kind (%) | 72.32 | 73.16 | 70.51 | 72.02 | 68.75 | 69.68 | 72.57 | 73.52 | 70.26 | 71.5 | 68.05 | 70.03 | 66.08 | 69.13 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.005714 | 0.005714 | 0.005714 | 1.206 | 0.002857 | 0.005714 | 0.005714 | 0.01429 | 0 | 0.01429 | 0.1 | 0.2206 | 0.1457 | 0.1886 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2573 | 2638 | +2.5% | -538 to +668.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6010 | 5731 | -4.6% | -1183 to +625.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 47.71 | 44.25 | -7.3% | -4.905 to -2.026 | GAIN |
| failed requests (%) | 32.94 | 33.12 | +0.5% | -0.7994 to +1.159 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.685 | 12.62 | +30.3% | +2.094 to +3.777 | power given |
| pods started | 4.486 | 8.057 | +79.6% | +2.5 to +4.642 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.352e-16 to +1.276e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.1 | +0.0% | -0.4946 to +0.5059 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.1 | +0.0% | -0.4946 to +0.5059 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.465 | +0.6% | +0.006008 to +0.02467 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.32 | 73.16 | +1.2% | +0.5971 to +1.074 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.00833 to +0.00833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2144 | 2754 | +28.4% | +93.33 to +1126 | LOSS |
| response time (ms), 99th percentile | 5255 | 5792 | +10.2% | -99.39 to +1174 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.5 | 41.28 | -9.3% | -5.968 to -2.488 | GAIN |
| failed requests (%) | 27.22 | 26.43 | -2.9% | -1.61 to +0.02758 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.693 | 13.93 | +43.8% | +3.54 to +4.944 | power given |
| pods started | 4.4 | 9.257 | +110.4% | +3.956 to +5.759 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.00103 to +0.003027 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.4 | +0.0% | -0.5112 to +0.6772 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.4 | +0.1% | -0.4903 to +0.6967 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.394 | 2.426 | +1.3% | +0.02663 to +0.03762 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.51 | 72.02 | +2.1% | +1.346 to +1.668 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.005714 | 1.206 | +21000.0% | -1.203 to +3.603 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2513 | 2340 | -6.9% | -738.5 to +392.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5452 | 5140 | -5.7% | -973.8 to +349.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 38.99 | 35.81 | -8.2% | -4.154 to -2.203 | GAIN |
| failed requests (%) | 27.03 | 27.76 | +2.7% | -0.0457 to +1.508 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.638 | 12.34 | +28.0% | +1.785 to +3.613 | power given |
| pods started | 4.771 | 7.943 | +66.5% | +2.084 to +4.259 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01001 to +0.002664 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.1 | -0.3% | -1.682 to +0.4719 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183 | -0.4% | -1.878 to +0.5193 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.317 | 2.332 | +0.6% | -0.002555 to +0.03131 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.75 | 69.68 | +1.4% | +0.7659 to +1.107 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.005714 | +100.0% | -0.007297 to +0.01301 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2684 | 2555 | -4.8% | -558.4 to +298.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5782 | 5739 | -0.7% | -778.5 to +693.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 47.59 | 42.63 | -10.4% | -6.535 to -3.382 | GAIN |
| failed requests (%) | 31.83 | 31.47 | -1.1% | -1.481 to +0.7661 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.657 | 12.01 | +24.4% | +1.468 to +3.24 | power given |
| pods started | 5.057 | 7.257 | +43.5% | +1.055 to +3.345 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0006098 to +0.001792 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185.3 | +0.2% | -0.1616 to +0.7581 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185.3 | +0.2% | -0.1583 to +0.7786 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.468 | +0.7% | +0.007995 to +0.02711 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.57 | 73.52 | +1.3% | +0.8239 to +1.088 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.005714 | 0.01429 | +150.0% | -0.006724 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2972 | 3025 | +1.8% | -389.3 to +495.3 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5650 | 5556 | -1.7% | -622.8 to +434.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 49.03 | 45.05 | -8.1% | -5.495 to -2.455 | GAIN |
| failed requests (%) | 31.72 | 31.23 | -1.5% | -1.487 to +0.5045 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.676 | 12.9 | +33.3% | +2.346 to +4.093 | power given |
| pods started | 4.829 | 8.4 | +74.0% | +2.384 to +4.759 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.426e-16 to +1.858e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.5 | +0.1% | -0.2272 to +0.6387 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.5 | +0.1% | -0.2272 to +0.6387 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.409 | +0.7% | +0.009471 to +0.0242 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.26 | 71.5 | +1.8% | +1.033 to +1.451 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0.01429 | +0.0143 | +0.002091 to +0.02648 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2978 | 3612 | +21.3% | +18.15 to +1250 | LOSS |
| response time (ms), 99th percentile | 4893 | 5430 | +11.0% | -3.767 to +1078 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.68 | 38.84 | -6.8% | -4.153 to -1.53 | GAIN |
| failed requests (%) | 27.23 | 26.62 | -2.2% | -1.579 to +0.3611 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.68 | 12.92 | +33.5% | +2.595 to +3.882 | power given |
| pods started | 4.529 | 8.5 | +87.7% | +3.047 to +4.894 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.243e-16 to +6.468e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.2 | -0.3% | -0.9379 to -0.2289 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.2 | -0.3% | -0.9379 to -0.2289 | GAIN |
| CPU used with Omni's own (cores), mean | 2.28 | 2.306 | +1.1% | +0.01535 to +0.03689 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.05 | 70.03 | +2.9% | +1.686 to +2.287 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.2206 | +120.6% | +0.09822 to +0.143 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2192 | 2697 | +23.0% | +21.55 to +988.2 | LOSS |
| response time (ms), 99th percentile | 4296 | 4634 | +7.9% | -272.4 to +947.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 32.44 | 31.07 | -4.2% | -2.539 to -0.2001 | GAIN |
| failed requests (%) | 15.72 | 17.05 | +8.4% | +0.3489 to +2.304 | LOSS |
| HPA replicas, mean | 9.642 | 12.06 | +25.1% | +1.653 to +3.192 | power given |
| pods started | 5.229 | 7.6 | +45.4% | +1.497 to +3.245 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.603e-16 to +3.095e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 182.9 | +0.0% | -0.403 to +0.4082 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 182.9 | +0.0% | -0.403 to +0.4082 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.207 | 2.238 | +1.4% | +0.02322 to +0.03803 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.08 | 69.13 | +4.6% | +2.824 to +3.268 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1457 | 0.1886 | +29.4% | +0.01487 to +0.07084 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
