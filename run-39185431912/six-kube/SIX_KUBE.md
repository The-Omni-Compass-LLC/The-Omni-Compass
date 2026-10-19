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
| response time (ms), 95th percentile | 2006 | 2275 | 1680 | 1731 | 1657 | 1585 | 1704 | 1984 | 1786 | 1900 | 1408 | 1438 | 1591 | 1336 |
| response time (ms), 99th percentile | 5899 | 6347 | 4972 | 6127 | 4415 | 4745 | 5446 | 5600 | 4533 | 5449 | 3846 | 4498 | 4295 | 4262 |
| time over the response line (% of samples) | 22.23 | 16.25 | 33.29 | 23.55 | 16.79 | 12.19 | 18.95 | 14.62 | 28.27 | 20.2 | 21.84 | 16.63 | 27.45 | 18.42 |
| failed requests (%) | 7.853 | 6.427 | 14.83 | 12.53 | 5.299 | 5.141 | 6.626 | 5.921 | 9.733 | 8.149 | 7.769 | 7.746 | 12.14 | 9.697 |
| HPA replicas, mean | 9.639 | 14.08 | 9.731 | 13.98 | 9.578 | 13.03 | 9.625 | 13.65 | 9.584 | 13.53 | 9.597 | 12.3 | 9.636 | 12.32 |
| pods started | 5.3 | 10.7 | 4.5 | 11.1 | 5.5 | 9.7 | 4.9 | 9.6 | 5.4 | 9.6 | 5.5 | 10.8 | 5.5 | 9.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.1 | 184.1 | 183.9 | 179.7 | 179.4 | 180.8 | 180 | 182.7 | 181.8 | 180.3 | 180.3 | 181.3 | 180.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.1 | 184.1 | 183.9 | 179.7 | 179.4 | 180.8 | 180 | 182.7 | 181.8 | 180.3 | 180.3 | 181.3 | 180.7 |
| CPU used with Omni's own (cores), mean | 2.136 | 2.131 | 2.339 | 2.349 | 1.906 | 1.918 | 2.006 | 2.017 | 2.173 | 2.188 | 2.012 | 2.023 | 2.09 | 2.068 |
| host CPU busy, the real machine under kind (%) | 63.03 | 63.34 | 68.96 | 69.36 | 56.47 | 56.96 | 59.55 | 60.15 | 64.19 | 64.68 | 59.64 | 60.16 | 62.12 | 61.61 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2006 | 2275 | +13.4% | -360.8 to +897.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5899 | 6347 | +7.6% | -117.9 to +1015 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.23 | 16.25 | -26.9% | -8.05 to -3.908 | GAIN |
| failed requests (%) | 7.853 | 6.427 | -18.2% | -2.257 to -0.5947 | GAIN |
| HPA replicas, mean | 9.639 | 14.08 | +46.0% | +3.31 to +5.565 | power given |
| pods started | 5.3 | 10.7 | +101.9% | +4.631 to +6.169 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.661e-15 to +4.179e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.1 | -0.7% | -2.241 to -0.2401 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.1 | -0.7% | -2.241 to -0.2401 | GAIN |
| CPU used with Omni's own (cores), mean | 2.136 | 2.131 | -0.2% | -0.02328 to +0.01275 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.03 | 63.34 | +0.5% | +0.08527 to +0.5419 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.97e+05 to +7.986e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.404e-05 to -9.385e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1680 | 1731 | +3.0% | -373.8 to +475.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4972 | 6127 | +23.2% | +141 to +2168 | LOSS |
| time over the response line (% of samples) | 33.29 | 23.55 | -29.3% | -13.69 to -5.799 | GAIN |
| failed requests (%) | 14.83 | 12.53 | -15.5% | -3.267 to -1.325 | GAIN |
| HPA replicas, mean | 9.731 | 13.98 | +43.6% | +3.635 to +4.855 | power given |
| pods started | 4.5 | 11.1 | +146.7% | +5.329 to +7.871 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.213e-15 to +5.023e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 183.9 | -0.1% | -1.284 to +0.8837 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 183.9 | -0.1% | -1.284 to +0.8837 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.339 | 2.349 | +0.4% | -0.009286 to +0.02949 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.96 | 69.36 | +0.6% | -0.1447 to +0.9515 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.629e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.153e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1657 | 1585 | -4.3% | -452.2 to +309.5 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4415 | 4745 | +7.5% | -332.2 to +992.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 16.79 | 12.19 | -27.4% | -7.16 to -2.048 | GAIN |
| failed requests (%) | 5.299 | 5.141 | -3.0% | -1.272 to +0.9552 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.578 | 13.03 | +36.1% | +1.767 to +5.147 | power given |
| pods started | 5.5 | 9.7 | +76.4% | +2.422 to +5.978 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.69e-16 to +2.585e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.4 | -0.1% | -1.316 to +0.8295 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.4 | -0.1% | -1.316 to +0.8295 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.906 | 1.918 | +0.6% | -0.004545 to +0.02827 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.47 | 56.96 | +0.9% | +0.009938 to +0.9776 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1704 | 1984 | +16.5% | -330.5 to +891.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5446 | 5600 | +2.8% | -361.9 to +669.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 18.95 | 14.62 | -22.9% | -6.267 to -2.402 | GAIN |
| failed requests (%) | 6.626 | 5.921 | -10.6% | -1.528 to +0.1172 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.625 | 13.65 | +41.8% | +2.478 to +5.575 | power given |
| pods started | 4.9 | 9.6 | +95.9% | +2.946 to +6.454 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180 | -0.4% | -1.866 to +0.3103 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180 | -0.4% | -1.866 to +0.3103 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.006 | 2.017 | +0.5% | -0.006127 to +0.02768 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.55 | 60.15 | +1.0% | +0.1296 to +1.063 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1786 | 1900 | +6.4% | -274.6 to +503.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4533 | 5449 | +20.2% | +164.3 to +1669 | LOSS |
| time over the response line (% of samples) | 28.27 | 20.2 | -28.6% | -12.25 to -3.898 | GAIN |
| failed requests (%) | 9.733 | 8.149 | -16.3% | -2.486 to -0.6816 | GAIN |
| HPA replicas, mean | 9.584 | 13.53 | +41.2% | +2.403 to +5.488 | power given |
| pods started | 5.4 | 9.6 | +77.8% | +2.487 to +5.913 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.395e-16 to +4.066e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 181.8 | -0.5% | -1.956 to +0.0704 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 181.8 | -0.5% | -1.956 to +0.0704 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.173 | 2.188 | +0.7% | +0.001425 to +0.02891 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.19 | 64.68 | +0.8% | +0.0319 to +0.9501 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1408 | 1438 | +2.1% | -223 to +282.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3846 | 4498 | +17.0% | -559 to +1864 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 21.84 | 16.63 | -23.9% | -8.22 to -2.217 | GAIN |
| failed requests (%) | 7.769 | 7.746 | -0.3% | -0.5651 to +0.5197 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.597 | 12.3 | +28.1% | +1.136 to +4.262 | power given |
| pods started | 5.5 | 10.8 | +96.4% | +3.248 to +7.352 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +6.104e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180.3 | -0.0% | -0.6666 to +0.5521 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180.3 | -0.0% | -0.6666 to +0.5521 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.012 | 2.023 | +0.5% | -0.01198 to +0.03232 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.64 | 60.16 | +0.9% | -0.04237 to +1.088 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1591 | 1336 | -16.0% | -475.7 to -33.12 | GAIN |
| response time (ms), 99th percentile | 4295 | 4262 | -0.8% | -1515 to +1450 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 27.45 | 18.42 | -32.9% | -13.77 to -4.28 | GAIN |
| failed requests (%) | 12.14 | 9.697 | -20.2% | -4.049 to -0.8462 | GAIN |
| HPA replicas, mean | 9.636 | 12.32 | +27.8% | +1.15 to +4.216 | power given |
| pods started | 5.5 | 9.1 | +65.5% | +2.084 to +5.116 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.7 | -0.3% | -1.439 to +0.3178 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.7 | -0.3% | -1.439 to +0.3178 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.09 | 2.068 | -1.0% | -0.03616 to -0.006768 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.12 | 61.61 | -0.8% | -0.9626 to -0.06924 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.1 | +0.1 | +0.05231 to +0.1477 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
