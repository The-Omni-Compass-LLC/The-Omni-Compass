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
| response time (ms), 95th percentile | 2451 | 2575 | 2584 | 3699 | 2470 | 2353 | 2407 | 2727 | 2571 | 3088 | 3646 | 3873 | 2532 | 2958 |
| response time (ms), 99th percentile | 5211 | 5322 | 5323 | 6523 | 5217 | 5226 | 5764 | 6536 | 4923 | 5622 | 5904 | 6112 | 4758 | 5224 |
| time over the response line (% of samples) | 45.74 | 40.84 | 49 | 44.29 | 41.11 | 35.76 | 52.87 | 49.32 | 41.88 | 37.67 | 51.79 | 46.67 | 44.4 | 40.85 |
| failed requests (%) | 31.92 | 31.62 | 26.2 | 25.24 | 27.88 | 27.24 | 37.36 | 37.2 | 24.46 | 23.83 | 34.24 | 34.21 | 23.57 | 24.7 |
| HPA replicas, mean | 9.654 | 12.3 | 9.696 | 14.02 | 9.631 | 11.31 | 9.719 | 13.62 | 9.656 | 13.1 | 9.687 | 13.17 | 9.668 | 12.51 |
| pods started | 4.914 | 7.657 | 4.629 | 9.4 | 5.086 | 6.429 | 4.171 | 7.714 | 5.114 | 9.429 | 4.6 | 8.171 | 4.886 | 6.971 |
| worker nodes in service, mean | 6 | 5.995 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.7 | 185.7 | 185.6 | 183.9 | 183.8 | 185.5 | 185.9 | 184.4 | 184.2 | 184.9 | 184.4 | 184.4 | 184 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.6 | 185.7 | 185.6 | 183.9 | 183.8 | 185.5 | 185.9 | 184.4 | 184.2 | 184.9 | 184.4 | 184.4 | 184 |
| CPU used with Omni's own (cores), mean | 2.4 | 2.414 | 2.494 | 2.519 | 2.339 | 2.358 | 2.513 | 2.539 | 2.367 | 2.383 | 2.41 | 2.431 | 2.355 | 2.384 |
| host CPU busy, the real machine under kind (%) | 71.05 | 71.75 | 73.17 | 74.71 | 69.54 | 70.41 | 74.73 | 75.92 | 69.25 | 70.47 | 71.81 | 73.56 | 70.62 | 73.89 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.01429 | 0.02 | 0.002857 | 0.01143 | 0.005714 | 0.002857 | 0.002857 | 0.005714 | 0.1143 | 0.22 | 0.16 | 0.6114 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2451 | 2575 | +5.0% | -447.3 to +693.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5211 | 5322 | +2.1% | -774.2 to +997.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.74 | 40.84 | -10.7% | -6.3 to -3.51 | GAIN |
| failed requests (%) | 31.92 | 31.62 | -0.9% | -1.24 to +0.6425 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 12.3 | +27.4% | +1.817 to +3.466 | power given |
| pods started | 4.914 | 7.657 | +55.8% | +1.718 to +3.768 | power given |
| worker nodes in service, mean | 6 | 5.995 | -0.1% | -0.01571 to +0.006026 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.7 | +0.1% | -0.2549 to +0.6351 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.6 | +0.1% | -0.4879 to +0.6729 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.4 | 2.414 | +0.6% | +0.002858 to +0.02534 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.05 | 71.75 | +1.0% | +0.4278 to +0.9733 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2584 | 3699 | +43.1% | +698.1 to +1531 | LOSS |
| response time (ms), 99th percentile | 5323 | 6523 | +22.5% | +520.8 to +1878 | LOSS |
| time over the response line (% of samples) | 49 | 44.29 | -9.6% | -5.971 to -3.452 | GAIN |
| failed requests (%) | 26.2 | 25.24 | -3.7% | -1.689 to -0.2296 | GAIN |
| HPA replicas, mean | 9.696 | 14.02 | +44.6% | +3.726 to +4.932 | power given |
| pods started | 4.629 | 9.4 | +103.1% | +4.059 to +5.484 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.988e-16 to +6.556e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.6 | -0.0% | -0.5007 to +0.3514 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.6 | -0.0% | -0.5007 to +0.3514 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.494 | 2.519 | +1.0% | +0.01821 to +0.03194 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.17 | 74.71 | +2.1% | +1.351 to +1.716 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.02 | +40.0% | -0.01281 to +0.02423 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2470 | 2353 | -4.7% | -655.2 to +421.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5217 | 5226 | +0.2% | -623.6 to +641.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.11 | 35.76 | -13.0% | -7.054 to -3.663 | GAIN |
| failed requests (%) | 27.88 | 27.24 | -2.3% | -1.688 to +0.4174 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.631 | 11.31 | +17.4% | +0.8889 to +2.472 | power given |
| pods started | 5.086 | 6.429 | +26.4% | +0.3788 to +2.307 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.674e-16 to +4.689e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.8 | -0.0% | -0.5519 to +0.4236 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.8 | -0.0% | -0.5519 to +0.4236 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.339 | 2.358 | +0.8% | +0.004489 to +0.03286 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.54 | 70.41 | +1.3% | +0.4148 to +1.333 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.01143 | +300.0% | -0.01074 to +0.02788 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2407 | 2727 | +13.3% | -143.9 to +783.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5764 | 6536 | +13.4% | -8.735 to +1553 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.87 | 49.32 | -6.7% | -5.101 to -1.989 | GAIN |
| failed requests (%) | 37.36 | 37.2 | -0.4% | -1.16 to +0.8417 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.719 | 13.62 | +40.1% | +3.123 to +4.671 | power given |
| pods started | 4.171 | 7.714 | +84.9% | +2.498 to +4.588 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.915e-16 to +3.407e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185.9 | +0.2% | -0.1623 to +0.8862 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 185.9 | +0.2% | -0.1623 to +0.8862 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.513 | 2.539 | +1.1% | +0.01099 to +0.04196 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.73 | 75.92 | +1.6% | +0.8068 to +1.576 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.005714 | 0.002857 | -50.0% | -0.01301 to +0.007297 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2571 | 3088 | +20.1% | +34.2 to +999.4 | LOSS |
| response time (ms), 99th percentile | 4923 | 5622 | +14.2% | +142.4 to +1255 | LOSS |
| time over the response line (% of samples) | 41.88 | 37.67 | -10.0% | -5.769 to -2.64 | GAIN |
| failed requests (%) | 24.46 | 23.83 | -2.6% | -1.33 to +0.07766 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.656 | 13.1 | +35.7% | +2.608 to +4.283 | power given |
| pods started | 5.114 | 9.429 | +84.4% | +3.351 to +5.278 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.411e-16 to +3.061e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.2 | -0.1% | -0.6938 to +0.2637 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.2 | -0.1% | -0.6938 to +0.2637 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.383 | +0.7% | +0.004885 to +0.02613 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.25 | 70.47 | +1.8% | +0.9034 to +1.545 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.002857 | 0.005714 | +100.0% | -0.007297 to +0.01301 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3646 | 3873 | +6.2% | -294.1 to +748.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5904 | 6112 | +3.5% | -302.1 to +717.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 51.79 | 46.67 | -9.9% | -6.908 to -3.339 | GAIN |
| failed requests (%) | 34.24 | 34.21 | -0.1% | -0.7597 to +0.7028 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.687 | 13.17 | +36.0% | +2.87 to +4.095 | power given |
| pods started | 4.6 | 8.171 | +77.6% | +2.717 to +4.426 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.608e-16 to +4.623e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.4 | -0.3% | -0.9769 to -0.05884 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.4 | -0.3% | -0.9769 to -0.05884 | GAIN |
| CPU used with Omni's own (cores), mean | 2.41 | 2.431 | +0.9% | +0.01161 to +0.03157 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.81 | 73.56 | +2.4% | +1.45 to +2.033 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1143 | 0.22 | +92.5% | +0.07945 to +0.132 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2532 | 2958 | +16.8% | -26.25 to +877.7 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4758 | 5224 | +9.8% | -240.7 to +1173 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 44.4 | 40.85 | -8.0% | -5.052 to -2.052 | GAIN |
| failed requests (%) | 23.57 | 24.7 | +4.8% | -0.06079 to +2.318 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.668 | 12.51 | +29.4% | +2.101 to +3.577 | power given |
| pods started | 4.886 | 6.971 | +42.7% | +1.272 to +2.899 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.966e-16 to +4.488e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184 | -0.2% | -0.7633 to +0.08393 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184 | -0.2% | -0.7633 to +0.08393 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.355 | 2.384 | +1.3% | +0.02216 to +0.03723 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.62 | 73.89 | +4.6% | +3.067 to +3.475 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.6114 | +282.1% | -0.4421 to +1.345 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
