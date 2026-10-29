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
| response time (ms), 95th percentile | 1932 | 1815 | 1816 | 2710 | 2513 | 2852 | 2458 | 2628 | 2375 | 3151 | 2944 | 4174 | 2080 | 4313 |
| response time (ms), 99th percentile | 3622 | 3613 | 3769 | 4878 | 5373 | 5823 | 4711 | 5558 | 5358 | 5947 | 4952 | 6185 | 4291 | 6715 |
| time over the response line (% of samples) | 33.01 | 29.13 | 39.89 | 36.85 | 46.18 | 41.77 | 43.02 | 39.08 | 48.24 | 43.3 | 50.02 | 47.64 | 49.43 | 48.9 |
| failed requests (%) | 21.77 | 21.36 | 22.88 | 20.77 | 30.63 | 29.9 | 28.14 | 27.35 | 29.88 | 27.67 | 34.38 | 30.41 | 27.44 | 26.23 |
| HPA replicas, mean | 9.574 | 11.3 | 9.676 | 13.07 | 9.65 | 12.34 | 9.647 | 12.23 | 9.662 | 13.13 | 9.724 | 13.41 | 9.744 | 12.95 |
| pods started | 5.429 | 8.086 | 4.6 | 8.686 | 4.853 | 7.529 | 4.714 | 7.6 | 5 | 8.771 | 3.971 | 8.529 | 3.657 | 7.121 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.6 | 183.4 | 183.7 | 184.4 | 184.9 | 183.7 | 184.1 | 183.9 | 185 | 184.1 | 184.6 | 184.7 | 185 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.6 | 183.4 | 183.6 | 184.4 | 184.9 | 183.7 | 184.1 | 183.9 | 185 | 184.1 | 184.6 | 184.7 | 185 |
| CPU used with Omni's own (cores), mean | 2.205 | 2.214 | 2.312 | 2.307 | 2.421 | 2.425 | 2.364 | 2.371 | 2.409 | 2.418 | 2.393 | 2.401 | 2.441 | 2.457 |
| host CPU busy, the real machine under kind (%) | 65.2 | 65.88 | 68.09 | 68.78 | 71.64 | 72.42 | 70.12 | 70.85 | 70.8 | 71.84 | 71.32 | 72.89 | 73.45 | 76.41 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01429 | 0.01143 | 0.005882 | 0.01176 | 0.008571 | 0.01143 | 0.01143 | 0.005714 | 0.1 | 0.25 | 0.1886 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1932 | 1815 | -6.1% | -482.6 to +248.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3622 | 3613 | -0.2% | -634 to +616.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 33.01 | 29.13 | -11.7% | -5.286 to -2.465 | GAIN |
| failed requests (%) | 21.77 | 21.36 | -1.9% | -1.133 to +0.3198 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.574 | 11.3 | +18.0% | +0.9438 to +2.501 | power given |
| pods started | 5.429 | 8.086 | +48.9% | +1.665 to +3.65 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.116e-17 to +1.107e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.6 | +0.2% | -0.01324 to +0.8386 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.6 | +0.2% | -0.01324 to +0.8386 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.205 | 2.214 | +0.4% | -0.004041 to +0.02286 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.2 | 65.88 | +1.0% | +0.2687 to +1.098 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1816 | 2710 | +49.3% | +436.9 to +1352 | LOSS |
| response time (ms), 99th percentile | 3769 | 4878 | +29.4% | +376.7 to +1841 | LOSS |
| time over the response line (% of samples) | 39.89 | 36.85 | -7.6% | -4.617 to -1.457 | GAIN |
| failed requests (%) | 22.88 | 20.77 | -9.2% | -3.067 to -1.146 | GAIN |
| HPA replicas, mean | 9.676 | 13.07 | +35.1% | +2.619 to +4.174 | power given |
| pods started | 4.6 | 8.686 | +88.8% | +3.078 to +5.094 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003046 to +0.001037 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.7 | +0.2% | -0.241 to +0.8525 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.6 | +0.2% | -0.2721 to +0.8431 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.312 | 2.307 | -0.2% | -0.01746 to +0.008813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.09 | 68.78 | +1.0% | +0.2392 to +1.134 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.01143 | -20.0% | -0.01841 to +0.0127 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2543 | 2823 | +11.0% | -455.1 to +1016 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5243 | 5747 | +9.6% | -101.3 to +1110 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.87 | 41.18 | -10.2% | -6.545 to -2.833 | GAIN |
| failed requests (%) | 30.32 | 29.58 | -2.5% | -1.783 to +0.2959 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.649 | 12.25 | +27.0% | +1.718 to +3.489 | power given |
| pods started | 4.848 | 7.485 | +54.4% | +1.588 to +3.685 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.857e-16 to +3.857e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.8 | +0.2% | -0.08649 to +0.9325 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.8 | +0.2% | -0.08649 to +0.9325 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.416 | 2.42 | +0.2% | -0.01404 to +0.02221 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.48 | 72.25 | +1.1% | +0.2915 to +1.23 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.006061 | 0.009091 | +50.0% | -0.007772 to +0.01383 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2458 | 2628 | +6.9% | -204.4 to +544.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4711 | 5558 | +18.0% | +155.5 to +1539 | LOSS |
| time over the response line (% of samples) | 43.02 | 39.08 | -9.2% | -5.579 to -2.303 | GAIN |
| failed requests (%) | 28.14 | 27.35 | -2.8% | -1.807 to +0.2327 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.647 | 12.23 | +26.8% | +1.662 to +3.506 | power given |
| pods started | 4.714 | 7.6 | +61.2% | +1.717 to +4.054 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.398e-16 to +2.86e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.1 | +0.2% | -0.1273 to +0.8823 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.1 | +0.2% | -0.1273 to +0.8823 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.364 | 2.371 | +0.3% | -0.002035 to +0.01636 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.12 | 70.85 | +1.0% | +0.4784 to +0.9725 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.008571 | 0.01143 | +33.3% | -0.0127 to +0.01841 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2375 | 3151 | +32.7% | +259.7 to +1292 | LOSS |
| response time (ms), 99th percentile | 5358 | 5947 | +11.0% | -132 to +1309 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 48.24 | 43.3 | -10.2% | -6.422 to -3.456 | GAIN |
| failed requests (%) | 29.88 | 27.67 | -7.4% | -3.242 to -1.184 | GAIN |
| HPA replicas, mean | 9.662 | 13.13 | +35.9% | +2.635 to +4.295 | power given |
| pods started | 5 | 8.771 | +75.4% | +2.934 to +4.609 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.95e-16 to +1.875e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 185 | +0.6% | +0.6872 to +1.478 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 185 | +0.6% | +0.6872 to +1.478 | power given |
| CPU used with Omni's own (cores), mean | 2.409 | 2.418 | +0.4% | -0.0002984 to +0.01881 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.8 | 71.84 | +1.5% | +0.7326 to +1.352 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01143 | 0.005714 | -50.0% | -0.02 to +0.008576 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 1

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2914 | 4174 | +43.2% | +642.4 to +1877 | LOSS |
| response time (ms), 99th percentile | 4867 | 6185 | +27.1% | +700.6 to +1935 | LOSS |
| time over the response line (% of samples) | 49.38 | 47.64 | -3.5% | -3.587 to +0.1113 | EVEN, inside the noise (cut) |
| failed requests (%) | 33.83 | 30.41 | -10.1% | -5.528 to -1.308 | GAIN |
| HPA replicas, mean | 9.718 | 13.41 | +38.0% | +3.102 to +4.29 | power given |
| pods started | 4.059 | 8.529 | +110.1% | +3.577 to +5.364 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.113e-16 to +1.411e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.6 | +0.3% | +0.1553 to +1.021 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.6 | +0.3% | +0.1553 to +1.021 | power given |
| CPU used with Omni's own (cores), mean | 2.386 | 2.401 | +0.6% | +0.006521 to +0.02382 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.11 | 72.89 | +2.5% | +1.567 to +1.986 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.25 | +150.0% | +0.1133 to +0.1867 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2083 | 4313 | +107.1% | +1568 to +2892 | LOSS |
| response time (ms), 99th percentile | 4177 | 6715 | +60.7% | +1762 to +3313 | LOSS |
| time over the response line (% of samples) | 48.5 | 48.9 | +0.8% | -1.806 to +2.61 | EVEN, inside the noise (up) |
| failed requests (%) | 26.83 | 26.23 | -2.2% | -1.699 to +0.5078 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.738 | 12.95 | +33.0% | +2.622 to +3.8 | power given |
| pods started | 3.727 | 7.121 | +91.1% | +2.539 to +4.249 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.7e-16 to +3.624e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 185 | +0.2% | -0.1528 to +0.888 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 185 | +0.2% | -0.1528 to +0.888 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.457 | +1.1% | +0.01315 to +0.0392 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.11 | 76.41 | +4.5% | +2.887 to +3.708 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1879 | 0.2 | +6.5% | -0.02307 to +0.04731 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
