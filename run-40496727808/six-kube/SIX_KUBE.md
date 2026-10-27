# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1892 | 1760 | 2016 | 2564 | 2112 | 2168 | 2389 | 2914 | 2036 | 2942 | 3743 | 4655 |
| response time (ms), 99th percentile | 4111 | 3517 | 4253 | 5442 | 5325 | 4812 | 5258 | 5849 | 4100 | 4603 | 5901 | 6743 |
| time over the response line (% of samples) | 34.92 | 31.16 | 40.04 | 35.64 | 45.8 | 40.43 | 45.47 | 40.42 | 36.55 | 33.79 | 53.6 | 48.64 |
| failed requests (%) | 23.01 | 23.22 | 22.55 | 21.66 | 30.83 | 31.65 | 29.75 | 28.47 | 22.91 | 22.78 | 35.48 | 35.53 |
| HPA replicas, mean | 9.587 | 12.18 | 9.693 | 13.14 | 9.655 | 12.36 | 9.682 | 12.2 | 9.632 | 12.16 | 9.73 | 12.81 |
| pods started | 5.45 | 8.65 | 4.45 | 8.35 | 4.85 | 7.2 | 4.55 | 7.1 | 5.25 | 8.15 | 3.9 | 7.25 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 6 | 5.997 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 183.2 | 183.9 | 183.8 | 184.4 | 184.2 | 184.6 | 185.1 | 182.5 | 182.9 | 184.7 | 184.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 183.2 | 183.9 | 183.8 | 184.4 | 184.2 | 184.6 | 185.1 | 182.5 | 182.9 | 184.6 | 184.4 |
| CPU used with Omni's own (cores), mean | 2.223 | 2.249 | 2.321 | 2.344 | 2.373 | 2.396 | 2.438 | 2.451 | 2.209 | 2.23 | 2.412 | 2.438 |
| host CPU busy, the real machine under kind (%) | 65.96 | 67.07 | 68.35 | 69.68 | 70.8 | 71.81 | 72.33 | 73.11 | 64.95 | 66.07 | 71.86 | 73.7 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 |
| organism behind its window (s) | 0 | 0 | 0.015 | 0.56 | 0.015 | 0.005 | 0.015 | 0.005 | 0.005 | 0.01 | 0.08 | 0.215 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1892 | 1760 | -7.0% | -657.6 to +393.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4111 | 3517 | -14.5% | -1520 to +331.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 34.92 | 31.16 | -10.8% | -5.55 to -1.975 | GAIN |
| failed requests (%) | 23.01 | 23.22 | +0.9% | -0.7753 to +1.202 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.587 | 12.18 | +27.1% | +1.426 to +3.761 | power given |
| pods started | 5.45 | 8.65 | +58.7% | +1.763 to +4.637 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001181 to +0.003341 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 183.2 | +0.3% | -0.03395 to +1.066 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 183.2 | +0.3% | -0.009914 to +1.086 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.223 | 2.249 | +1.2% | +0.01624 to +0.03669 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.96 | 67.07 | +1.7% | +0.6313 to +1.594 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2016 | 2564 | +27.2% | +60.59 to +1036 | LOSS |
| response time (ms), 99th percentile | 4253 | 5442 | +28.0% | +245.6 to +2134 | LOSS |
| time over the response line (% of samples) | 40.04 | 35.64 | -11.0% | -6.901 to -1.901 | GAIN |
| failed requests (%) | 22.55 | 21.66 | -3.9% | -1.837 to +0.05602 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.693 | 13.14 | +35.5% | +2.33 to +4.555 | power given |
| pods started | 4.45 | 8.35 | +87.6% | +2.517 to +5.283 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.868e-16 to +2.427e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.8 | -0.1% | -0.8668 to +0.6335 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.8 | -0.1% | -0.8668 to +0.6335 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.321 | 2.344 | +1.0% | +0.007159 to +0.03918 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.35 | 69.68 | +1.9% | +0.9191 to +1.743 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.015 | 0.56 | +3633.3% | -0.5849 to +1.675 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2112 | 2168 | +2.7% | -552.5 to +664.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5325 | 4812 | -9.6% | -1727 to +700.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 45.8 | 40.43 | -11.7% | -7.467 to -3.26 | GAIN |
| failed requests (%) | 30.83 | 31.65 | +2.7% | -0.3131 to +1.96 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.655 | 12.36 | +28.0% | +1.492 to +3.909 | power given |
| pods started | 4.85 | 7.2 | +48.5% | +0.8524 to +3.848 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.271e-16 to +3.718e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.2 | -0.1% | -0.8231 to +0.3336 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.2 | -0.1% | -0.8231 to +0.3336 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.373 | 2.396 | +1.0% | +0.007264 to +0.03951 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.8 | 71.81 | +1.4% | +0.5133 to +1.514 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.015 | 0.005 | -66.7% | -0.03093 to +0.01093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2389 | 2914 | +22.0% | -295.8 to +1347 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5258 | 5849 | +11.2% | -35.64 to +1218 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.47 | 40.42 | -11.1% | -6.993 to -3.092 | GAIN |
| failed requests (%) | 29.75 | 28.47 | -4.3% | -2.262 to -0.2934 | GAIN |
| HPA replicas, mean | 9.682 | 12.2 | +26.0% | +1.304 to +3.735 | power given |
| pods started | 4.55 | 7.1 | +56.0% | +0.8903 to +4.21 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.0% | -0.003052 to +0.008636 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 185.1 | +0.2% | -0.1429 to +1.02 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 185.1 | +0.3% | -0.1381 to +1.127 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.438 | 2.451 | +0.5% | +0.0006926 to +0.02525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.33 | 73.11 | +1.1% | +0.5013 to +1.053 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.015 | 0.005 | -66.7% | -0.03093 to +0.01093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2036 | 2942 | +44.5% | +214 to +1597 | LOSS |
| response time (ms), 99th percentile | 4100 | 4603 | +12.3% | -449.4 to +1455 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 36.55 | 33.79 | -7.5% | -4.926 to -0.584 | GAIN |
| failed requests (%) | 22.91 | 22.78 | -0.6% | -1.436 to +1.167 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.632 | 12.16 | +26.2% | +1.263 to +3.787 | power given |
| pods started | 5.25 | 8.15 | +55.2% | +1.398 to +4.402 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.395e-16 to +5.395e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.9 | +0.2% | -0.1292 to +1.03 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.9 | +0.2% | -0.1292 to +1.03 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.209 | 2.23 | +0.9% | +0.008743 to +0.0324 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.95 | 66.07 | +1.7% | +0.7258 to +1.509 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005 | 0.01 | +100.0% | -0.01344 to +0.02344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3743 | 4655 | +24.4% | +127.5 to +1696 | LOSS |
| response time (ms), 99th percentile | 5901 | 6743 | +14.3% | +160.3 to +1524 | LOSS |
| time over the response line (% of samples) | 53.6 | 48.64 | -9.2% | -7.227 to -2.681 | GAIN |
| failed requests (%) | 35.48 | 35.53 | +0.1% | -1.888 to +1.99 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.73 | 12.81 | +31.6% | +2.071 to +4.086 | power given |
| pods started | 3.9 | 7.25 | +85.9% | +1.868 to +4.832 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.0% | -0.002897 to +0.008199 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.4 | -0.1% | -0.7634 to +0.2262 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.4 | -0.1% | -0.7528 to +0.3218 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.412 | 2.438 | +1.1% | +0.0147 to +0.03828 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.86 | 73.7 | +2.6% | +1.556 to +2.116 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.08 | 0.215 | +168.8% | +0.1121 to +0.1579 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
