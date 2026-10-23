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
| response time (ms), 95th percentile | 1608 | 1345 | 1791 | 1472 | 1814 | 1579 | 2040 | 1616 | 1684 | 1686 | 2073 | 2113 | 1461 | 1457 |
| response time (ms), 99th percentile | 5224 | 5058 | 4687 | 4820 | 5929 | 5563 | 6153 | 5964 | 4391 | 4542 | 4868 | 5222 | 4115 | 4501 |
| time over the response line (% of samples) | 18.2 | 13.6 | 29.35 | 21.17 | 20.34 | 15.45 | 21.85 | 16.77 | 24.34 | 19.8 | 33.49 | 25.64 | 24.12 | 16.98 |
| failed requests (%) | 5.887 | 5.845 | 12.78 | 11.57 | 6.784 | 6.462 | 7.561 | 7.386 | 8.146 | 7.993 | 13.89 | 12.13 | 10.64 | 8.797 |
| HPA replicas, mean | 9.612 | 14.25 | 9.668 | 13.77 | 9.641 | 14.28 | 9.657 | 14.44 | 9.554 | 13.92 | 9.645 | 14.12 | 9.644 | 13.77 |
| pods started | 5.029 | 11.17 | 4.943 | 12.41 | 4.886 | 10.91 | 4.8 | 10.54 | 5.514 | 11.29 | 4.8 | 10.66 | 5.229 | 12.31 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.8 | 181.5 | 181.6 | 181.2 | 180.5 | 181.7 | 180.7 | 180.7 | 181.1 | 182.5 | 182.8 | 180.8 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.8 | 181.5 | 181.6 | 181.2 | 180.5 | 181.7 | 180.7 | 180.7 | 181.1 | 182.5 | 182.8 | 180.8 | 181 |
| CPU used with Omni's own (cores), mean | 1.968 | 1.997 | 2.122 | 2.148 | 2.059 | 2.084 | 2.093 | 2.125 | 2.053 | 2.09 | 2.249 | 2.268 | 2.057 | 2.074 |
| host CPU busy, the real machine under kind (%) | 58.21 | 59.49 | 62.5 | 63.79 | 60.76 | 61.86 | 61.63 | 63.01 | 60.89 | 62.29 | 66.1 | 67.2 | 61.19 | 62.12 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1608 | 1345 | -16.3% | -510.2 to -15.48 | GAIN |
| response time (ms), 99th percentile | 5224 | 5058 | -3.2% | -587.2 to +255.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.2 | 13.6 | -25.3% | -5.721 to -3.479 | GAIN |
| failed requests (%) | 5.887 | 5.845 | -0.7% | -0.3202 to +0.2356 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.612 | 14.25 | +48.2% | +4.226 to +5.042 | power given |
| pods started | 5.029 | 11.17 | +122.2% | +5.725 to +6.561 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.56e-16 to +4.022e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.8 | -0.3% | -0.9584 to -0.1152 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.8 | -0.3% | -0.9584 to -0.1152 | GAIN |
| CPU used with Omni's own (cores), mean | 1.968 | 1.997 | +1.5% | +0.02092 to +0.03748 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.21 | 59.49 | +2.2% | +1.073 to +1.494 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.96e+05 to +7.986e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.404e-05 to -9.373e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1582 | 1472 | -6.9% | -444.3 to +224.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4551 | 4820 | +5.9% | -266.7 to +804.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.27 | 21.17 | -22.4% | -8.66 to -3.541 | GAIN |
| failed requests (%) | 12.28 | 11.57 | -5.8% | -1.717 to +0.3016 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.658 | 13.77 | +42.6% | +3.652 to +4.567 | power given |
| pods started | 5.088 | 12.41 | +143.9% | +6.803 to +7.844 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.115e-16 to +8.001e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.6 | +0.0% | -0.3942 to +0.57 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.6 | +0.0% | -0.3942 to +0.57 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.118 | 2.148 | +1.4% | +0.01603 to +0.04336 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.61 | 63.79 | +1.9% | +0.7701 to +1.593 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1814 | 1579 | -13.0% | -453.2 to -16.64 | GAIN |
| response time (ms), 99th percentile | 5929 | 5563 | -6.2% | -816.1 to +84.49 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.34 | 15.45 | -24.0% | -5.884 to -3.893 | GAIN |
| failed requests (%) | 6.784 | 6.462 | -4.7% | -0.7428 to +0.1 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.641 | 14.28 | +48.1% | +4.183 to +5.094 | power given |
| pods started | 4.886 | 10.91 | +123.4% | +5.492 to +6.565 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.278e-16 to +1.695e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.5 | -0.4% | -1.187 to -0.1649 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.5 | -0.4% | -1.187 to -0.1649 | GAIN |
| CPU used with Omni's own (cores), mean | 2.059 | 2.084 | +1.2% | +0.01585 to +0.03412 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.76 | 61.86 | +1.8% | +0.8747 to +1.333 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2040 | 1616 | -20.8% | -696.5 to -151.5 | GAIN |
| response time (ms), 99th percentile | 6153 | 5964 | -3.1% | -538.5 to +162.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 21.85 | 16.77 | -23.2% | -6.174 to -3.975 | GAIN |
| failed requests (%) | 7.561 | 7.386 | -2.3% | -0.5698 to +0.2214 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.657 | 14.44 | +49.6% | +4.402 to +5.171 | power given |
| pods started | 4.8 | 10.54 | +119.6% | +5.069 to +6.416 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.067e-16 to +6.113e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.7 | -0.5% | -1.452 to -0.5017 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.7 | -0.5% | -1.452 to -0.5017 | GAIN |
| CPU used with Omni's own (cores), mean | 2.093 | 2.125 | +1.5% | +0.01971 to +0.04342 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.63 | 63.01 | +2.2% | +1.102 to +1.657 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1684 | 1686 | +0.1% | -204.5 to +207.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4391 | 4542 | +3.4% | -275.5 to +577.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 24.34 | 19.8 | -18.6% | -5.988 to -3.093 | GAIN |
| failed requests (%) | 8.146 | 7.993 | -1.9% | -0.498 to +0.1912 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.554 | 13.92 | +45.7% | +3.834 to +4.895 | power given |
| pods started | 5.514 | 11.29 | +104.7% | +5.084 to +6.459 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.266e-16 to -3.315e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 181.1 | +0.2% | +0.0427 to +0.7793 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 181.1 | +0.2% | +0.0427 to +0.7793 | power given |
| CPU used with Omni's own (cores), mean | 2.053 | 2.09 | +1.8% | +0.02642 to +0.04744 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.89 | 62.29 | +2.3% | +1.15 to +1.65 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2073 | 2113 | +1.9% | -196.4 to +277 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4868 | 5222 | +7.3% | -130.2 to +837.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 33.49 | 25.64 | -23.4% | -9.861 to -5.843 | GAIN |
| failed requests (%) | 13.89 | 12.13 | -12.7% | -2.63 to -0.8914 | GAIN |
| HPA replicas, mean | 9.645 | 14.12 | +46.4% | +4.015 to +4.928 | power given |
| pods started | 4.8 | 10.66 | +122.0% | +5.316 to +6.398 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.339e-16 to +3.831e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.8 | +0.2% | -0.06915 to +0.8129 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.8 | +0.2% | -0.06915 to +0.8129 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.249 | 2.268 | +0.8% | +0.008315 to +0.02987 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.1 | 67.2 | +1.7% | +0.8009 to +1.405 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1461 | 1457 | -0.2% | -225.9 to +219.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4115 | 4501 | +9.4% | -108 to +880.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 24.12 | 16.98 | -29.6% | -9.375 to -4.887 | GAIN |
| failed requests (%) | 10.64 | 8.797 | -17.3% | -2.635 to -1.048 | GAIN |
| HPA replicas, mean | 9.644 | 13.77 | +42.8% | +3.703 to +4.554 | power given |
| pods started | 5.229 | 12.31 | +135.5% | +6.339 to +7.833 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.47e-16 to +3.47e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 181 | +0.1% | -0.1946 to +0.6188 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 181 | +0.1% | -0.1946 to +0.6188 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.057 | 2.074 | +0.8% | +0.005322 to +0.0284 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.19 | 62.12 | +1.5% | +0.6374 to +1.225 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.08857 | +0.0886 | +0.0747 to +0.1024 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
