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
| response time (ms), 95th percentile | 1630 | 1505 | 1329 | 1220 | 1569 | 1274 | 2066 | 2033 | 1748 | 1508 | 1674 | 1529 | 1253 | 1063 |
| response time (ms), 99th percentile | 4948 | 4999 | 3983 | 4632 | 4520 | 4273 | 6215 | 6113 | 4561 | 3932 | 4275 | 4579 | 4510 | 4433 |
| time over the response line (% of samples) | 17.53 | 13.43 | 20.72 | 15.24 | 14.8 | 10.91 | 22.05 | 16.54 | 23.25 | 17.83 | 25.46 | 18.56 | 18.34 | 13.87 |
| failed requests (%) | 6.099 | 5.734 | 8.692 | 7.557 | 4.934 | 4.502 | 7.889 | 6.807 | 7.748 | 7.514 | 9.92 | 8.164 | 7.476 | 6.676 |
| HPA replicas, mean | 9.57 | 13.34 | 9.613 | 12.49 | 9.56 | 13 | 9.645 | 13.73 | 9.546 | 12.91 | 9.564 | 12.74 | 9.609 | 12.15 |
| pods started | 5.657 | 10.23 | 5.514 | 10.89 | 5.486 | 10.17 | 4.943 | 9.829 | 5.429 | 9.2 | 5.457 | 10.03 | 5.429 | 9.743 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179 | 180.2 | 180.5 | 179.1 | 178.5 | 181.7 | 180.5 | 180.4 | 180.6 | 180.4 | 180.7 | 179.6 | 180 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179 | 180.2 | 180.5 | 179.1 | 178.5 | 181.7 | 180.5 | 180.4 | 180.6 | 180.4 | 180.7 | 179.6 | 180 |
| CPU used with Omni's own (cores), mean | 1.925 | 1.93 | 2.007 | 2.007 | 1.849 | 1.855 | 2.1 | 2.091 | 2.014 | 2.03 | 2.043 | 2.041 | 1.954 | 1.957 |
| host CPU busy, the real machine under kind (%) | 56.98 | 57.51 | 59.6 | 59.81 | 54.89 | 55.32 | 61.85 | 62.1 | 59.91 | 60.51 | 60.28 | 60.7 | 58.01 | 58.47 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08286 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1630 | 1505 | -7.7% | -452.1 to +200.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4948 | 4999 | +1.0% | -289.8 to +391.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.53 | 13.43 | -23.4% | -5.105 to -3.092 | GAIN |
| failed requests (%) | 6.099 | 5.734 | -6.0% | -0.8598 to +0.1304 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.57 | 13.34 | +39.4% | +3.096 to +4.438 | power given |
| pods started | 5.657 | 10.23 | +80.8% | +3.919 to +5.224 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.139e-16 to +3.139e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179 | -0.5% | -1.433 to -0.4177 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179 | -0.5% | -1.433 to -0.4177 | GAIN |
| CPU used with Omni's own (cores), mean | 1.925 | 1.93 | +0.3% | -0.004964 to +0.01472 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.98 | 57.51 | +0.9% | +0.319 to +0.7454 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +7.989e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.407e-05 to -9.395e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1329 | 1220 | -8.2% | -311 to +93.07 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3983 | 4632 | +16.3% | +124.9 to +1174 | LOSS |
| time over the response line (% of samples) | 20.72 | 15.24 | -26.5% | -7.087 to -3.881 | GAIN |
| failed requests (%) | 8.692 | 7.557 | -13.1% | -1.767 to -0.5027 | GAIN |
| HPA replicas, mean | 9.613 | 12.49 | +29.9% | +2.315 to +3.432 | power given |
| pods started | 5.514 | 10.89 | +97.4% | +4.559 to +6.184 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.431e-16 to +3.408e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.5 | +0.2% | -0.07402 to +0.6169 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.5 | +0.2% | -0.07402 to +0.6169 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.007 | 2.007 | +0.0% | -0.01256 to +0.01282 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.6 | 59.81 | +0.3% | -0.1993 to +0.6082 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1569 | 1274 | -18.8% | -535.9 to -54.51 | GAIN |
| response time (ms), 99th percentile | 4520 | 4273 | -5.5% | -502.3 to +8.635 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.8 | 10.91 | -26.3% | -5.126 to -2.659 | GAIN |
| failed requests (%) | 4.934 | 4.502 | -8.8% | -0.7956 to -0.06826 | GAIN |
| HPA replicas, mean | 9.56 | 13 | +36.0% | +2.698 to +4.178 | power given |
| pods started | 5.486 | 10.17 | +85.4% | +3.821 to +5.551 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.962e-16 to +1.379e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 178.5 | -0.4% | -1.1 to -0.1609 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 178.5 | -0.4% | -1.1 to -0.1609 | GAIN |
| CPU used with Omni's own (cores), mean | 1.849 | 1.855 | +0.3% | -0.003661 to +0.01527 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.89 | 55.32 | +0.8% | +0.2049 to +0.6625 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2066 | 2033 | -1.6% | -353.4 to +287.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6215 | 6113 | -1.6% | -421.4 to +217.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.05 | 16.54 | -25.0% | -6.556 to -4.477 | GAIN |
| failed requests (%) | 7.889 | 6.807 | -13.7% | -1.522 to -0.6417 | GAIN |
| HPA replicas, mean | 9.645 | 13.73 | +42.4% | +3.476 to +4.694 | power given |
| pods started | 4.943 | 9.829 | +98.8% | +4.079 to +5.692 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.761e-16 to -8.825e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.5 | -0.7% | -1.737 to -0.6825 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.5 | -0.7% | -1.737 to -0.6825 | GAIN |
| CPU used with Omni's own (cores), mean | 2.1 | 2.091 | -0.4% | -0.01557 to -0.00158 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.85 | 62.1 | +0.4% | +0.05373 to +0.4411 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1748 | 1508 | -13.8% | -436.2 to -44.62 | GAIN |
| response time (ms), 99th percentile | 4561 | 3932 | -13.8% | -953.6 to -303.5 | GAIN |
| time over the response line (% of samples) | 23.25 | 17.83 | -23.3% | -7.185 to -3.656 | GAIN |
| failed requests (%) | 7.748 | 7.514 | -3.0% | -0.5527 to +0.08542 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.546 | 12.91 | +35.3% | +2.585 to +4.149 | power given |
| pods started | 5.429 | 9.2 | +69.5% | +2.84 to +4.703 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.589e-16 to +4.988e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.6 | +0.1% | -0.3242 to +0.6027 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.6 | +0.1% | -0.3242 to +0.6027 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.014 | 2.03 | +0.8% | +0.004527 to +0.02642 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.91 | 60.51 | +1.0% | +0.1956 to +0.9916 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1674 | 1529 | -8.6% | -351.1 to +62.38 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4275 | 4579 | +7.1% | -242.7 to +852.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 25.46 | 18.56 | -27.1% | -9.098 to -4.709 | GAIN |
| failed requests (%) | 9.92 | 8.164 | -17.7% | -2.609 to -0.9039 | GAIN |
| HPA replicas, mean | 9.564 | 12.74 | +33.2% | +2.44 to +3.918 | power given |
| pods started | 5.457 | 10.03 | +83.8% | +3.858 to +5.285 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.999e-16 to -9.092e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.7 | +0.2% | -0.01312 to +0.6234 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.7 | +0.2% | -0.01312 to +0.6234 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.043 | 2.041 | -0.1% | -0.009604 to +0.006424 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.28 | 60.7 | +0.7% | +0.2397 to +0.6117 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1253 | 1063 | -15.2% | -426.8 to +46.85 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4510 | 4433 | -1.7% | -591.1 to +437 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.34 | 13.87 | -24.4% | -6.122 to -2.825 | GAIN |
| failed requests (%) | 7.476 | 6.676 | -10.7% | -1.438 to -0.1601 | GAIN |
| HPA replicas, mean | 9.609 | 12.15 | +26.5% | +1.886 to +3.202 | power given |
| pods started | 5.429 | 9.743 | +79.5% | +3.512 to +5.117 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.589e-16 to +4.988e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 180 | +0.3% | +0.1243 to +0.8282 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 180 | +0.3% | +0.1243 to +0.8282 | power given |
| CPU used with Omni's own (cores), mean | 1.954 | 1.957 | +0.1% | -0.009306 to +0.01411 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.01 | 58.47 | +0.8% | +0.1302 to +0.802 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08286 | +0.0829 | +0.06972 to +0.09599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
