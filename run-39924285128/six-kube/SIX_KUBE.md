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
| response time (ms), 95th percentile | 1584 | 1492 | 1015 | 868.5 | 1467 | 1258 | 1270 | 1133 | 1574 | 1806 | 1862 | 1915 | 1631 | 1529 |
| response time (ms), 99th percentile | 4849 | 4946 | 2982 | 3071 | 4177 | 3973 | 4455 | 4387 | 4751 | 5346 | 3965 | 4494 | 4468 | 4955 |
| time over the response line (% of samples) | 18.13 | 13.96 | 15.42 | 11.16 | 15.42 | 12.11 | 15.2 | 11.75 | 25.81 | 19.83 | 27.39 | 21.55 | 27.48 | 21.76 |
| failed requests (%) | 5.774 | 5.597 | 6.526 | 5.71 | 5.503 | 5.797 | 5.023 | 4.949 | 8.221 | 7.784 | 11.82 | 10.42 | 12.19 | 11.06 |
| HPA replicas, mean | 9.613 | 13.98 | 9.561 | 13.1 | 9.545 | 13.19 | 9.558 | 13.77 | 9.587 | 14.19 | 9.593 | 13.75 | 9.662 | 14.21 |
| pods started | 5.1 | 10.25 | 5.65 | 13.2 | 5.5 | 10.65 | 5.5 | 11.45 | 5.45 | 10.2 | 5.05 | 11.2 | 5.05 | 11.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.6 | 178.4 | 178.5 | 178.5 | 177.7 | 178.5 | 178.3 | 181.2 | 181.9 | 180.3 | 181.1 | 181.5 | 182.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.6 | 178.4 | 178.5 | 178.5 | 177.7 | 178.5 | 178.3 | 181.2 | 181.9 | 180.3 | 181.1 | 181.5 | 182.1 |
| CPU used with Omni's own (cores), mean | 1.955 | 1.982 | 1.794 | 1.822 | 1.787 | 1.812 | 1.831 | 1.866 | 2.13 | 2.181 | 2.046 | 2.083 | 2.137 | 2.17 |
| host CPU busy, the real machine under kind (%) | 57.66 | 58.96 | 53.34 | 54.65 | 53.08 | 54.33 | 54.38 | 55.72 | 62.99 | 64.45 | 60.69 | 62.05 | 64.58 | 66.07 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1584 | 1492 | -5.8% | -608.6 to +425.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4849 | 4946 | +2.0% | -387.5 to +580.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 18.13 | 13.96 | -23.0% | -5.511 to -2.836 | GAIN |
| failed requests (%) | 5.774 | 5.597 | -3.1% | -0.7164 to +0.3633 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.613 | 13.98 | +45.4% | +3.493 to +5.237 | power given |
| pods started | 5.1 | 10.25 | +101.0% | +4.211 to +6.089 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.811e-16 to -7.083e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.6 | -0.2% | -1.075 to +0.3282 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.6 | -0.2% | -1.075 to +0.3282 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.955 | 1.982 | +1.4% | +0.01449 to +0.03942 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.66 | 58.96 | +2.3% | +1.025 to +1.583 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.966e+05 to +7.991e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.41e-05 to -9.38e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1015 | 868.5 | -14.4% | -325.2 to +32.67 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 2982 | 3071 | +3.0% | -464.4 to +642.8 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.42 | 11.16 | -27.6% | -6.974 to -1.54 | GAIN |
| failed requests (%) | 6.526 | 5.71 | -12.5% | -1.479 to -0.1511 | GAIN |
| HPA replicas, mean | 9.561 | 13.1 | +37.0% | +2.826 to +4.258 | power given |
| pods started | 5.65 | 13.2 | +133.6% | +6.671 to +8.429 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.775e-16 to +5.44e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 178.5 | +0.1% | -0.4424 to +0.6982 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 178.5 | +0.1% | -0.4424 to +0.6982 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.794 | 1.822 | +1.5% | +0.01482 to +0.03988 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.34 | 54.65 | +2.5% | +1.006 to +1.617 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1467 | 1258 | -14.3% | -408.1 to -11.23 | GAIN |
| response time (ms), 99th percentile | 4177 | 3973 | -4.9% | -424.4 to +14.57 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 15.42 | 12.11 | -21.4% | -4.978 to -1.629 | GAIN |
| failed requests (%) | 5.503 | 5.797 | +5.3% | -0.186 to +0.7748 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.545 | 13.19 | +38.2% | +2.745 to +4.55 | power given |
| pods started | 5.5 | 10.65 | +93.6% | +4.301 to +5.999 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.494e-16 to +1.942e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 177.7 | -0.5% | -1.454 to -0.2872 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 177.7 | -0.5% | -1.454 to -0.2872 | GAIN |
| CPU used with Omni's own (cores), mean | 1.787 | 1.812 | +1.4% | +0.009871 to +0.03888 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.08 | 54.33 | +2.3% | +0.8423 to +1.646 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.243e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1270 | 1133 | -10.7% | -327.6 to +54.97 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4455 | 4387 | -1.5% | -613.9 to +478.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 15.2 | 11.75 | -22.7% | -4.778 to -2.131 | GAIN |
| failed requests (%) | 5.023 | 4.949 | -1.5% | -0.4289 to +0.2804 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.558 | 13.77 | +44.0% | +3.471 to +4.949 | power given |
| pods started | 5.5 | 11.45 | +108.2% | +5.154 to +6.746 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.405e-16 to +4.74e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 178.3 | -0.1% | -0.8672 to +0.5201 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 178.3 | -0.1% | -0.8672 to +0.5201 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.831 | 1.866 | +1.9% | +0.01789 to +0.05167 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.38 | 55.72 | +2.5% | +0.8278 to +1.843 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1574 | 1806 | +14.8% | -54.85 to +520.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4751 | 5346 | +12.5% | -115.4 to +1306 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 25.81 | 19.83 | -23.2% | -7.994 to -3.96 | GAIN |
| failed requests (%) | 8.221 | 7.784 | -5.3% | -1.07 to +0.1966 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.587 | 14.19 | +48.0% | +3.853 to +5.359 | power given |
| pods started | 5.45 | 10.2 | +87.2% | +3.803 to +5.697 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.135e-16 to +4.912e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181.9 | +0.4% | +0.1315 to +1.324 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181.9 | +0.4% | +0.1315 to +1.324 | power given |
| CPU used with Omni's own (cores), mean | 2.13 | 2.181 | +2.4% | +0.03983 to +0.06099 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.99 | 64.45 | +2.3% | +1.15 to +1.763 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1862 | 1915 | +2.9% | -197.9 to +305.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3965 | 4494 | +13.4% | -4.885 to +1064 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.39 | 21.55 | -21.3% | -8.294 to -3.384 | GAIN |
| failed requests (%) | 11.82 | 10.42 | -11.8% | -2.536 to -0.2656 | GAIN |
| HPA replicas, mean | 9.593 | 13.75 | +43.4% | +3.454 to +4.869 | power given |
| pods started | 5.05 | 11.2 | +121.8% | +5.301 to +6.999 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.411e-16 to -2.136e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 181.1 | +0.4% | +0.1929 to +1.367 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 181.1 | +0.4% | +0.1929 to +1.367 | power given |
| CPU used with Omni's own (cores), mean | 2.046 | 2.083 | +1.8% | +0.02661 to +0.04734 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.69 | 62.05 | +2.3% | +1.076 to +1.66 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1631 | 1529 | -6.2% | -503.1 to +299.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4468 | 4955 | +10.9% | -344.1 to +1319 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.48 | 21.76 | -20.8% | -8.634 to -2.8 | GAIN |
| failed requests (%) | 12.19 | 11.06 | -9.3% | -2.264 to -0.008246 | GAIN |
| HPA replicas, mean | 9.662 | 14.21 | +47.1% | +4.099 to +5.005 | power given |
| pods started | 5.05 | 11.8 | +133.7% | +6.108 to +7.392 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.022e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 182.1 | +0.3% | +0.07731 to +1.055 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 182.1 | +0.3% | +0.07731 to +1.055 | power given |
| CPU used with Omni's own (cores), mean | 2.137 | 2.17 | +1.5% | +0.01852 to +0.04567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.58 | 66.07 | +2.3% | +1.182 to +1.81 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4.001e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.986e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.085 | +0.085 | +0.06785 to +0.1021 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
