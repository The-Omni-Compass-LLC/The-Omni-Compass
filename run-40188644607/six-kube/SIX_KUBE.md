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
| response time (ms), 95th percentile | 1436 | 1516 | 1649 | 1536 | 1291 | 1175 | 1357 | 1614 | 1636 | 1352 | 1655 | 1507 | 1439 | 1225 |
| response time (ms), 99th percentile | 4763 | 4686 | 5174 | 5220 | 4695 | 4300 | 4790 | 4754 | 4230 | 3846 | 4226 | 4435 | 4694 | 4785 |
| time over the response line (% of samples) | 15.71 | 11.5 | 26.53 | 19.71 | 13.65 | 9.537 | 17.07 | 13.03 | 23.08 | 16.82 | 25.69 | 18.68 | 22.08 | 15.64 |
| failed requests (%) | 5.127 | 4.415 | 11.65 | 10.31 | 3.318 | 2.876 | 6.621 | 5.765 | 7.516 | 6.908 | 10.06 | 8.221 | 9.65 | 7.957 |
| HPA replicas, mean | 9.585 | 13.23 | 9.665 | 13.34 | 9.578 | 13.45 | 9.566 | 12.58 | 9.549 | 12.68 | 9.584 | 12.92 | 9.629 | 12.76 |
| pods started | 5.286 | 10.51 | 5.029 | 11.06 | 5.618 | 10.65 | 5.4 | 9.057 | 5.4 | 9.229 | 5.486 | 10.6 | 5.294 | 10.68 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.8 | 181.8 | 181.7 | 178.8 | 178.7 | 179.4 | 178.5 | 180.3 | 180 | 180.6 | 180.9 | 180.1 | 180.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.8 | 181.8 | 181.7 | 178.8 | 178.7 | 179.4 | 178.5 | 180.3 | 180 | 180.6 | 180.9 | 180.1 | 180.5 |
| CPU used with Omni's own (cores), mean | 1.894 | 1.899 | 2.152 | 2.145 | 1.869 | 1.871 | 1.879 | 1.874 | 1.982 | 1.993 | 2.066 | 2.076 | 2.013 | 2.014 |
| host CPU busy, the real machine under kind (%) | 56.26 | 56.69 | 63.52 | 63.84 | 55.57 | 55.69 | 55.83 | 55.96 | 58.77 | 59.22 | 61.06 | 61.51 | 59.84 | 60.17 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08235 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1436 | 1516 | +5.5% | -236 to +394.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4763 | 4686 | -1.6% | -463.9 to +310.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 15.71 | 11.5 | -26.8% | -5.22 to -3.183 | GAIN |
| failed requests (%) | 5.127 | 4.415 | -13.9% | -1.159 to -0.2646 | GAIN |
| HPA replicas, mean | 9.585 | 13.23 | +38.0% | +3.066 to +4.229 | power given |
| pods started | 5.286 | 10.51 | +98.9% | +4.562 to +5.895 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.33e-16 to +2.285e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 178.8 | -0.3% | -0.9483 to -0.04498 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 178.8 | -0.3% | -0.9483 to -0.04498 | GAIN |
| CPU used with Omni's own (cores), mean | 1.894 | 1.899 | +0.3% | -0.004853 to +0.01482 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.26 | 56.69 | +0.8% | +0.1811 to +0.6755 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.979e+05 to +7.988e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.407e-05 to -9.396e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1649 | 1536 | -6.9% | -307.8 to +80.53 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5174 | 5220 | +0.9% | -456.6 to +547.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 26.53 | 19.71 | -25.7% | -8.807 to -4.825 | GAIN |
| failed requests (%) | 11.65 | 10.31 | -11.5% | -2.25 to -0.4221 | GAIN |
| HPA replicas, mean | 9.665 | 13.34 | +38.1% | +3.129 to +4.226 | power given |
| pods started | 5.029 | 11.06 | +119.9% | +5.419 to +6.638 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.809e-16 to +1.749e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.7 | -0.0% | -0.5974 to +0.4243 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.7 | -0.0% | -0.5974 to +0.4243 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.152 | 2.145 | -0.3% | -0.01903 to +0.00626 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.52 | 63.84 | +0.5% | -0.04278 to +0.6933 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1291 | 1175 | -8.9% | -410.5 to +180.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4695 | 4300 | -8.4% | -866.7 to +78.53 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 13.65 | 9.537 | -30.1% | -5.237 to -2.995 | GAIN |
| failed requests (%) | 3.318 | 2.876 | -13.3% | -0.7286 to -0.1551 | GAIN |
| HPA replicas, mean | 9.578 | 13.45 | +40.4% | +3.298 to +4.444 | power given |
| pods started | 5.618 | 10.65 | +89.5% | +4.226 to +5.833 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.881e-16 to +5.448e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 178.7 | -0.1% | -0.5122 to +0.3295 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 178.7 | -0.1% | -0.5122 to +0.3295 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.869 | 1.871 | +0.1% | -0.007286 to +0.01204 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.57 | 55.69 | +0.2% | -0.1895 to +0.4193 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1357 | 1614 | +19.0% | -87.33 to +601.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4790 | 4754 | -0.8% | -388.6 to +315.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 17.07 | 13.03 | -23.7% | -5.222 to -2.861 | GAIN |
| failed requests (%) | 6.621 | 5.765 | -12.9% | -1.395 to -0.317 | GAIN |
| HPA replicas, mean | 9.566 | 12.58 | +31.5% | +2.193 to +3.826 | power given |
| pods started | 5.4 | 9.057 | +67.7% | +2.661 to +4.653 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.5 | -0.5% | -1.303 to -0.4835 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.5 | -0.5% | -1.303 to -0.4835 | GAIN |
| CPU used with Omni's own (cores), mean | 1.879 | 1.874 | -0.3% | -0.01457 to +0.004996 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.83 | 55.96 | +0.2% | -0.2076 to +0.4671 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1636 | 1352 | -17.4% | -457.8 to -110.1 | GAIN |
| response time (ms), 99th percentile | 4230 | 3846 | -9.1% | -847 to +78.48 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.08 | 16.82 | -27.1% | -8.251 to -4.283 | GAIN |
| failed requests (%) | 7.516 | 6.908 | -8.1% | -1.021 to -0.1938 | GAIN |
| HPA replicas, mean | 9.549 | 12.68 | +32.8% | +2.323 to +3.939 | power given |
| pods started | 5.4 | 9.229 | +70.9% | +2.777 to +4.881 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.538e-16 to +9.702e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180 | -0.2% | -0.7023 to +0.1423 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180 | -0.2% | -0.7023 to +0.1423 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.982 | 1.993 | +0.6% | +0.001465 to +0.02123 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.77 | 59.22 | +0.8% | +0.152 to +0.7423 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1655 | 1507 | -9.0% | -387.7 to +90.76 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4226 | 4435 | +4.9% | -291.2 to +708.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 25.69 | 18.68 | -27.3% | -9.309 to -4.719 | GAIN |
| failed requests (%) | 10.06 | 8.221 | -18.3% | -2.954 to -0.7217 | GAIN |
| HPA replicas, mean | 9.584 | 12.92 | +34.8% | +2.763 to +3.901 | power given |
| pods started | 5.486 | 10.6 | +93.2% | +4.366 to +5.863 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.695e-16 to +4.203e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.9 | +0.1% | -0.079 to +0.6055 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.9 | +0.1% | -0.079 to +0.6055 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.066 | 2.076 | +0.5% | +0.0009367 to +0.01975 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.06 | 61.51 | +0.7% | +0.1286 to +0.7563 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 1

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1439 | 1225 | -14.9% | -414.2 to -14.29 | GAIN |
| response time (ms), 99th percentile | 4694 | 4785 | +1.9% | -373.4 to +555.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.08 | 15.64 | -29.2% | -8.7 to -4.193 | GAIN |
| failed requests (%) | 9.65 | 7.957 | -17.6% | -2.619 to -0.7688 | GAIN |
| HPA replicas, mean | 9.629 | 12.76 | +32.6% | +2.508 to +3.763 | power given |
| pods started | 5.294 | 10.68 | +101.7% | +4.536 to +6.229 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.274e-16 to +2.094e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 180.5 | +0.2% | +0.132 to +0.6532 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 180.5 | +0.2% | +0.132 to +0.6532 | power given |
| CPU used with Omni's own (cores), mean | 2.013 | 2.014 | +0.1% | -0.009943 to +0.01287 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.84 | 60.17 | +0.6% | +0.04368 to +0.6245 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08235 | +0.0824 | +0.06885 to +0.09586 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
