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
| response time (ms), 95th percentile | 2145 | 1852 | 1585 | 1549 | 2032 | 1887 | 1735 | 1776 | 1480 | 1270 | 2276 | 2169 | 1671 | 1220 |
| response time (ms), 99th percentile | 6050 | 5610 | 4821 | 5322 | 5574 | 5415 | 5165 | 5367 | 4503 | 4433 | 5537 | 6062 | 4801 | 4586 |
| time over the response line (% of samples) | 20.09 | 15.68 | 27.87 | 20.56 | 20 | 14.98 | 19.91 | 14.18 | 21.5 | 15.72 | 36.54 | 27.41 | 26.59 | 18.13 |
| failed requests (%) | 6.621 | 6.442 | 12.94 | 10.84 | 6.453 | 5.795 | 7.099 | 6.193 | 6.93 | 6.444 | 15.83 | 12.58 | 11.38 | 9.452 |
| HPA replicas, mean | 9.604 | 13.52 | 9.642 | 12.39 | 9.597 | 13.24 | 9.62 | 13.31 | 9.557 | 12.9 | 9.67 | 13.87 | 9.644 | 12.5 |
| pods started | 5.343 | 9.943 | 5.371 | 9.743 | 5.343 | 9.6 | 5.114 | 9.314 | 5.457 | 9.8 | 4.914 | 10.2 | 5.171 | 10.11 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 179.8 | 181.5 | 181.5 | 180.6 | 179.7 | 180.8 | 179.3 | 180.5 | 180.1 | 183.7 | 183.7 | 181.5 | 181.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 179.8 | 181.5 | 181.5 | 180.6 | 179.7 | 180.8 | 179.3 | 180.5 | 180.1 | 183.7 | 183.7 | 181.5 | 181.4 |
| CPU used with Omni's own (cores), mean | 2.024 | 2.024 | 2.147 | 2.149 | 2.012 | 2.014 | 1.988 | 1.984 | 1.991 | 2.008 | 2.343 | 2.355 | 2.116 | 2.12 |
| host CPU busy, the real machine under kind (%) | 59.8 | 60.25 | 63.64 | 63.79 | 59.43 | 59.79 | 58.91 | 59.05 | 59.16 | 59.76 | 68.86 | 69.4 | 62.83 | 63.13 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0.002857 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 6 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2145 | 1852 | -13.7% | -583 to -3.64 | GAIN |
| response time (ms), 99th percentile | 6050 | 5610 | -7.3% | -746.3 to -133.5 | GAIN |
| time over the response line (% of samples) | 20.09 | 15.68 | -22.0% | -5.509 to -3.33 | GAIN |
| failed requests (%) | 6.621 | 6.442 | -2.7% | -0.478 to +0.1206 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 13.52 | +40.8% | +3.211 to +4.627 | power given |
| pods started | 5.343 | 9.943 | +86.1% | +3.746 to +5.454 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.352e-16 to +1.276e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 179.8 | -0.6% | -1.595 to -0.7174 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 179.8 | -0.6% | -1.595 to -0.7174 | GAIN |
| CPU used with Omni's own (cores), mean | 2.024 | 2.024 | +0.0% | -0.01088 to +0.01136 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.8 | 60.25 | +0.7% | +0.145 to +0.7465 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +7.998e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.418e-05 to -9.39e-05 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1585 | 1549 | -2.3% | -239.4 to +167.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4821 | 5322 | +10.4% | -26.78 to +1028 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.87 | 20.56 | -26.2% | -9.329 to -5.302 | GAIN |
| failed requests (%) | 12.94 | 10.84 | -16.2% | -3.321 to -0.8741 | GAIN |
| HPA replicas, mean | 9.642 | 12.39 | +28.5% | +2.117 to +3.374 | power given |
| pods started | 5.371 | 9.743 | +81.4% | +3.669 to +5.074 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.662e-16 to +2.14e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.5 | +0.0% | -0.39 to +0.4732 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.5 | +0.0% | -0.39 to +0.4732 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.147 | 2.149 | +0.1% | -0.0139 to +0.01733 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.64 | 63.79 | +0.2% | -0.2484 to +0.5626 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2032 | 1887 | -7.1% | -552.7 to +264 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5574 | 5415 | -2.8% | -589 to +271.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20 | 14.98 | -25.1% | -6.233 to -3.821 | GAIN |
| failed requests (%) | 6.453 | 5.795 | -10.2% | -1.173 to -0.1431 | GAIN |
| HPA replicas, mean | 9.597 | 13.24 | +37.9% | +2.912 to +4.364 | power given |
| pods started | 5.343 | 9.6 | +79.7% | +3.382 to +5.132 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.652e-16 to +2.374e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.7 | -0.5% | -1.35 to -0.4304 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.7 | -0.5% | -1.35 to -0.4304 | GAIN |
| CPU used with Omni's own (cores), mean | 2.012 | 2.014 | +0.1% | -0.006998 to +0.01097 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.43 | 59.79 | +0.6% | +0.1001 to +0.6377 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1735 | 1776 | +2.3% | -255.3 to +336.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5165 | 5367 | +3.9% | -231.2 to +635.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 19.91 | 14.18 | -28.8% | -7.079 to -4.368 | GAIN |
| failed requests (%) | 7.099 | 6.193 | -12.8% | -1.36 to -0.4523 | GAIN |
| HPA replicas, mean | 9.62 | 13.31 | +38.4% | +2.88 to +4.504 | power given |
| pods started | 5.114 | 9.314 | +82.1% | +3.372 to +5.028 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.052e-16 to +3.022e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 179.3 | -0.8% | -1.829 to -1.041 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 179.3 | -0.8% | -1.829 to -1.041 | GAIN |
| CPU used with Omni's own (cores), mean | 1.988 | 1.984 | -0.2% | -0.01192 to +0.004098 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.91 | 59.05 | +0.2% | -0.09995 to +0.379 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1480 | 1270 | -14.2% | -413.8 to -7.624 | GAIN |
| response time (ms), 99th percentile | 4503 | 4433 | -1.5% | -480.7 to +342.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 21.5 | 15.72 | -26.9% | -7.49 to -4.061 | GAIN |
| failed requests (%) | 6.93 | 6.444 | -7.0% | -0.8518 to -0.1202 | GAIN |
| HPA replicas, mean | 9.557 | 12.9 | +35.0% | +2.602 to +4.091 | power given |
| pods started | 5.457 | 9.8 | +79.6% | +3.408 to +5.278 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.968e-16 to +4.506e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.1 | -0.2% | -0.8386 to +0.04213 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.1 | -0.2% | -0.8386 to +0.04213 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.991 | 2.008 | +0.9% | +0.007376 to +0.02648 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.16 | 59.76 | +1.0% | +0.3307 to +0.8701 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2276 | 2169 | -4.7% | -399.7 to +184.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5537 | 6062 | +9.5% | +37.28 to +1012 | LOSS |
| time over the response line (% of samples) | 36.54 | 27.41 | -25.0% | -11.22 to -7.025 | GAIN |
| failed requests (%) | 15.83 | 12.58 | -20.6% | -4.724 to -1.786 | GAIN |
| HPA replicas, mean | 9.67 | 13.87 | +43.4% | +3.653 to +4.743 | power given |
| pods started | 4.914 | 10.2 | +107.6% | +4.762 to +5.81 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004793 to +0.001631 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.7 | +0.0% | -0.4398 to +0.5014 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.7 | -0.0% | -0.4804 to +0.4777 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.343 | 2.355 | +0.5% | -0.002722 to +0.02524 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.86 | 69.4 | +0.8% | +0.1522 to +0.9338 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1671 | 1220 | -27.0% | -694.6 to -208.6 | GAIN |
| response time (ms), 99th percentile | 4801 | 4586 | -4.5% | -777.5 to +349.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.59 | 18.13 | -31.8% | -10.94 to -5.987 | GAIN |
| failed requests (%) | 11.38 | 9.452 | -16.9% | -3.13 to -0.7205 | GAIN |
| HPA replicas, mean | 9.644 | 12.5 | +29.6% | +2.232 to +3.47 | power given |
| pods started | 5.171 | 10.11 | +95.6% | +4.031 to +5.855 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001613 to +0.0005489 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.4 | -0.0% | -0.5289 to +0.4316 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.4 | -0.0% | -0.5496 to +0.4309 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.116 | 2.12 | +0.2% | -0.009429 to +0.01785 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.83 | 63.13 | +0.5% | -0.07784 to +0.6776 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.07143 | +0.0714 | +0.05569 to +0.08717 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
