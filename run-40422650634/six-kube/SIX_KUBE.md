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
| response time (ms), 95th percentile | 1943 | 1682 | 1820 | 1643 | 1341 | 1251 | 1698 | 1493 | 1533 | 1404 | 2265 | 2024 | 1546 | 1382 |
| response time (ms), 99th percentile | 5225 | 5178 | 5277 | 5274 | 4522 | 4571 | 4976 | 4866 | 4163 | 4169 | 5195 | 5524 | 4219 | 4436 |
| time over the response line (% of samples) | 19.22 | 14.61 | 32.49 | 22.69 | 15.74 | 11.59 | 16.46 | 12.84 | 22.07 | 15.38 | 34.24 | 26.37 | 26.3 | 18.72 |
| failed requests (%) | 6.729 | 6.492 | 14.73 | 11.96 | 5.302 | 4.781 | 5.565 | 5.296 | 7.271 | 6.497 | 15.75 | 13.13 | 11.46 | 9.918 |
| HPA replicas, mean | 9.614 | 13.35 | 9.678 | 12.98 | 9.559 | 12.67 | 9.569 | 13 | 9.564 | 12.61 | 9.654 | 13.27 | 9.647 | 12.39 |
| pods started | 5.086 | 10.26 | 4.914 | 10.6 | 5.571 | 9.8 | 5.543 | 9.629 | 5.314 | 9.4 | 4.571 | 9.914 | 5.171 | 9.714 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.9 | 182.5 | 182.1 | 178.9 | 178.2 | 179.4 | 178.8 | 179.7 | 180 | 182.2 | 182.4 | 181 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.9 | 182.5 | 182.1 | 178.9 | 178.2 | 179.4 | 178.8 | 179.7 | 180 | 182.2 | 182.4 | 181 | 181 |
| CPU used with Omni's own (cores), mean | 1.987 | 1.996 | 2.228 | 2.225 | 1.852 | 1.851 | 1.893 | 1.898 | 1.974 | 1.987 | 2.211 | 2.224 | 2.081 | 2.076 |
| host CPU busy, the real machine under kind (%) | 58.57 | 59.23 | 65.66 | 65.67 | 54.86 | 55.11 | 56.11 | 56.46 | 58.71 | 59.17 | 65.16 | 65.65 | 61.58 | 61.91 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1943 | 1682 | -13.4% | -654.6 to +132.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5225 | 5178 | -0.9% | -507.2 to +413.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.22 | 14.61 | -24.0% | -5.962 to -3.257 | GAIN |
| failed requests (%) | 6.729 | 6.492 | -3.5% | -0.7297 to +0.2564 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.614 | 13.35 | +38.9% | +3.028 to +4.45 | power given |
| pods started | 5.086 | 10.26 | +101.7% | +4.415 to +5.928 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.286e-16 to +2.226e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.9 | -0.4% | -1.142 to -0.2357 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.9 | -0.4% | -1.142 to -0.2357 | GAIN |
| CPU used with Omni's own (cores), mean | 1.987 | 1.996 | +0.4% | -0.0005645 to +0.01773 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.57 | 59.23 | +1.1% | +0.3821 to +0.9361 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +7.991e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.409e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1820 | 1643 | -9.7% | -473.9 to +119.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5277 | 5274 | -0.1% | -504.8 to +498.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 32.49 | 22.69 | -30.2% | -12.2 to -7.403 | GAIN |
| failed requests (%) | 14.73 | 11.96 | -18.8% | -3.974 to -1.575 | GAIN |
| HPA replicas, mean | 9.678 | 12.98 | +34.1% | +2.751 to +3.853 | power given |
| pods started | 4.914 | 10.6 | +115.7% | +5.064 to +6.308 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005776 to +0.001697 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.1 | -0.2% | -0.8258 to -0.03402 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.1 | -0.2% | -0.8165 to -0.02069 | GAIN |
| CPU used with Omni's own (cores), mean | 2.228 | 2.225 | -0.1% | -0.01578 to +0.01003 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.66 | 65.67 | +0.0% | -0.3411 to +0.3739 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1341 | 1251 | -6.7% | -427.4 to +247.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4522 | 4571 | +1.1% | -223.6 to +320.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.74 | 11.59 | -26.4% | -5.5 to -2.805 | GAIN |
| failed requests (%) | 5.302 | 4.781 | -9.8% | -0.946 to -0.09638 | GAIN |
| HPA replicas, mean | 9.559 | 12.67 | +32.5% | +2.309 to +3.904 | power given |
| pods started | 5.571 | 9.8 | +75.9% | +3.308 to +5.149 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.399e-16 to +8.16e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 178.2 | -0.4% | -1.12 to -0.2297 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 178.2 | -0.4% | -1.12 to -0.2297 | GAIN |
| CPU used with Omni's own (cores), mean | 1.852 | 1.851 | -0.1% | -0.01017 to +0.007464 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.86 | 55.11 | +0.5% | +0.02696 to +0.4822 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1698 | 1493 | -12.1% | -443.4 to +33.58 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4976 | 4866 | -2.2% | -361.2 to +141.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 16.46 | 12.84 | -22.0% | -4.774 to -2.462 | GAIN |
| failed requests (%) | 5.565 | 5.296 | -4.8% | -0.7558 to +0.2172 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.569 | 13 | +35.9% | +2.658 to +4.21 | power given |
| pods started | 5.543 | 9.629 | +73.7% | +3.231 to +4.941 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.622e-16 to +2.592e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.8 | -0.3% | -0.9906 to -0.07386 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.8 | -0.3% | -0.9906 to -0.07386 | GAIN |
| CPU used with Omni's own (cores), mean | 1.893 | 1.898 | +0.3% | -0.005661 to +0.01622 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.11 | 56.46 | +0.6% | +0.02166 to +0.6896 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1533 | 1404 | -8.4% | -297.8 to +38.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4163 | 4169 | +0.2% | -348.7 to +361.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.07 | 15.38 | -30.3% | -8.798 to -4.586 | GAIN |
| failed requests (%) | 7.271 | 6.497 | -10.6% | -1.184 to -0.3645 | GAIN |
| HPA replicas, mean | 9.564 | 12.61 | +31.9% | +2.229 to +3.872 | power given |
| pods started | 5.314 | 9.4 | +76.9% | +3.149 to +5.022 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.951e-16 to +1.413e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 180 | +0.1% | -0.1606 to +0.678 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 180 | +0.1% | -0.1606 to +0.678 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.974 | 1.987 | +0.7% | +0.002392 to +0.02441 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.71 | 59.17 | +0.8% | +0.2241 to +0.7037 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2265 | 2024 | -10.6% | -547.9 to +66.16 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5195 | 5524 | +6.3% | -169.7 to +827.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 34.24 | 26.37 | -23.0% | -9.689 to -6.046 | GAIN |
| failed requests (%) | 15.75 | 13.13 | -16.6% | -3.768 to -1.469 | GAIN |
| HPA replicas, mean | 9.654 | 13.27 | +37.5% | +2.917 to +4.324 | power given |
| pods started | 4.571 | 9.914 | +116.9% | +4.661 to +6.024 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.891e-16 to -7.371e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.4 | +0.1% | -0.1964 to +0.6636 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.4 | +0.1% | -0.1964 to +0.6636 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.211 | 2.224 | +0.6% | +0.00499 to +0.02107 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.16 | 65.65 | +0.7% | +0.2863 to +0.6844 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1546 | 1382 | -10.6% | -387 to +58 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4219 | 4436 | +5.1% | -254.7 to +687.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 26.3 | 18.72 | -28.8% | -9.901 to -5.255 | GAIN |
| failed requests (%) | 11.46 | 9.918 | -13.5% | -2.366 to -0.7225 | GAIN |
| HPA replicas, mean | 9.647 | 12.39 | +28.4% | +2.082 to +3.4 | power given |
| pods started | 5.171 | 9.714 | +87.8% | +3.668 to +5.418 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.012e-16 to +3.52e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 181 | -0.0% | -0.469 to +0.3305 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 181 | -0.0% | -0.469 to +0.3305 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.081 | 2.076 | -0.2% | -0.01351 to +0.004222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.58 | 61.91 | +0.5% | +0.05386 to +0.6185 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.1 | +0.1 | +0.08557 to +0.1144 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
