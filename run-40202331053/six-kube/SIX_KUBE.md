# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1816 | 1773 | 1449 | 1263 | 1441 | 1180 | 1587 | 1307 | 2075 | 2014 |
| response time (ms), 99th percentile | 5937 | 5565 | 4965 | 4921 | 4236 | 4155 | 4359 | 4157 | 5143 | 5186 |
| time over the response line (% of samples) | 20.61 | 15.3 | 23.06 | 16.35 | 14.89 | 10.43 | 21.66 | 15.32 | 30.8 | 24.16 |
| failed requests (%) | 6.773 | 6.134 | 9.188 | 8.106 | 5.277 | 4.251 | 6.45 | 6.056 | 12.91 | 10.73 |
| HPA replicas, mean | 9.633 | 13.83 | 9.624 | 13.08 | 9.57 | 12.82 | 9.564 | 13.15 | 9.64 | 12.89 |
| pods started | 5.1 | 10.1 | 5.5 | 11.65 | 5.3 | 9.65 | 5.65 | 9.9 | 4.65 | 9.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180 | 181.4 | 181 | 178.4 | 177.9 | 180.1 | 180.7 | 181.4 | 182.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180 | 181.4 | 181 | 178.4 | 177.9 | 180.1 | 180.7 | 181.4 | 182.1 |
| CPU used with Omni's own (cores), mean | 2.062 | 2.052 | 2.077 | 2.074 | 1.812 | 1.798 | 2.024 | 2.043 | 2.171 | 2.185 |
| host CPU busy, the real machine under kind (%) | 60.71 | 60.97 | 61.32 | 61.65 | 53.91 | 53.87 | 59.85 | 60.61 | 64.11 | 64.77 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1816 | 1773 | -2.4% | -487 to +400 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5937 | 5565 | -6.3% | -822.9 to +77.85 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.61 | 15.3 | -25.8% | -6.77 to -3.867 | GAIN |
| failed requests (%) | 6.773 | 6.134 | -9.4% | -1.261 to -0.01644 | GAIN |
| HPA replicas, mean | 9.633 | 13.83 | +43.5% | +3.416 to +4.973 | power given |
| pods started | 5.1 | 10.1 | +98.0% | +3.981 to +6.019 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.947e-16 to +4.506e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180 | -0.7% | -1.925 to -0.6226 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180 | -0.7% | -1.925 to -0.6226 | GAIN |
| CPU used with Omni's own (cores), mean | 2.062 | 2.052 | -0.5% | -0.01928 to -0.001567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.71 | 60.97 | +0.4% | -0.03407 to +0.5576 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +7.984e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.401e-05 to -9.389e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1449 | 1263 | -12.9% | -331.7 to -41.8 | GAIN |
| response time (ms), 99th percentile | 4965 | 4921 | -0.9% | -546.8 to +459 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 23.06 | 16.35 | -29.1% | -9.317 to -4.107 | GAIN |
| failed requests (%) | 9.188 | 8.106 | -11.8% | -2.049 to -0.1163 | GAIN |
| HPA replicas, mean | 9.624 | 13.08 | +35.9% | +2.728 to +4.187 | power given |
| pods started | 5.5 | 11.65 | +111.8% | +5.417 to +6.883 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.76e-16 to +7.666e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181 | -0.2% | -0.9721 to +0.1611 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181 | -0.2% | -0.9721 to +0.1611 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.077 | 2.074 | -0.1% | -0.0163 to +0.01029 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.32 | 61.65 | +0.5% | +0.01211 to +0.6559 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1441 | 1180 | -18.1% | -708.7 to +186.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4236 | 4155 | -1.9% | -648.5 to +486 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.89 | 10.43 | -29.9% | -7.664 to -1.249 | GAIN |
| failed requests (%) | 5.277 | 4.251 | -19.4% | -2.454 to +0.4009 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.57 | 12.82 | +33.9% | +2.179 to +4.318 | power given |
| pods started | 5.3 | 9.65 | +82.1% | +2.755 to +5.945 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.947e-16 to +9.538e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 177.9 | -0.3% | -1.042 to -0.01515 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 177.9 | -0.3% | -1.042 to -0.01515 | GAIN |
| CPU used with Omni's own (cores), mean | 1.812 | 1.798 | -0.8% | -0.03614 to +0.007902 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.91 | 53.87 | -0.1% | -0.6051 to +0.5079 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1587 | 1307 | -17.6% | -524.5 to -35.32 | GAIN |
| response time (ms), 99th percentile | 4359 | 4157 | -4.6% | -774.5 to +371.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 21.66 | 15.32 | -29.3% | -8.904 to -3.774 | GAIN |
| failed requests (%) | 6.45 | 6.056 | -6.1% | -0.9817 to +0.1929 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.564 | 13.15 | +37.4% | +2.683 to +4.48 | power given |
| pods started | 5.65 | 9.9 | +75.2% | +3.135 to +5.365 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.103e-16 to +3.55e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 180.7 | +0.3% | +0.1498 to +1.087 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 180.7 | +0.3% | +0.1498 to +1.087 | power given |
| CPU used with Omni's own (cores), mean | 2.024 | 2.043 | +0.9% | +0.006884 to +0.0312 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.85 | 60.61 | +1.3% | +0.3798 to +1.134 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2075 | 2014 | -3.0% | -369.6 to +246.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5143 | 5186 | +0.8% | -595.1 to +680.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 30.8 | 24.16 | -21.6% | -9.412 to -3.871 | GAIN |
| failed requests (%) | 12.91 | 10.73 | -16.9% | -4.176 to -0.1947 | GAIN |
| HPA replicas, mean | 9.64 | 12.89 | +33.7% | +2.271 to +4.221 | power given |
| pods started | 4.65 | 9.8 | +110.8% | +4.287 to +6.013 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.194e-16 to +6.082e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 182.1 | +0.4% | +0.3854 to +1.028 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 182.1 | +0.4% | +0.3854 to +1.028 | power given |
| CPU used with Omni's own (cores), mean | 2.171 | 2.185 | +0.7% | +0.0001071 to +0.02825 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.11 | 64.77 | +1.0% | +0.3374 to +0.9869 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Physics / Robotics / Autonomous
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
