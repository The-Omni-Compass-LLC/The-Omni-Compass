# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4166 | 5727 | 4859 | 3178 | 3141 | 4357 | 4798 | 4374 | 3388 | 2852 |
| response time (ms), 99th percentile | 6604 | 7464 | 7366 | 6485 | 5278 | 6325 | 7600 | 6969 | 5314 | 5033 |
| time over the response line (% of samples) | 59.77 | 62.47 | 68.42 | 67.08 | 60.68 | 59.93 | 68.02 | 66.72 | 48.39 | 48.69 |
| failed requests (%) | 40.99 | 45.41 | 51.65 | 57.85 | 48.16 | 47.93 | 51.39 | 55.33 | 37.04 | 40.99 |
| HPA replicas, mean | 9.828 | 11.7 | 9.838 | 11.59 | 9.835 | 12.16 | 9.816 | 11.65 | 9.785 | 12.42 |
| pods started | 3.7 | 6 | 3.8 | 5.1 | 3.7 | 6.3 | 4.1 | 4.4 | 4.8 | 7.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 278.3 | 278 | 278.4 | 277 | 276.8 | 278.4 | 278.1 | 276.3 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 278.3 | 278 | 278.4 | 277 | 276.8 | 278.4 | 278.1 | 276.3 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.54 | 2.565 | 2.565 | 2.582 | 2.459 | 2.46 | 2.535 | 2.542 | 2.408 | 2.45 |
| host CPU busy, the real machine under kind (%) | 74.96 | 78.78 | 78.23 | 85.48 | 75.46 | 79.42 | 78.26 | 83.23 | 72.75 | 79.63 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.43 | 0.52 | 0.91 | 1.14 | 0.63 | 0.48 | 0.78 | 0.57 | 0.55 | 1.03 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; time over the response line (% of samples)), power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4166 | 5727 | +37.5% | +515 to +2607 | LOSS |
| response time (ms), 99th percentile | 6604 | 7464 | +13.0% | -255.3 to +1975 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.77 | 62.47 | +4.5% | +0.07542 to +5.321 | LOSS |
| failed requests (%) | 40.99 | 45.41 | +10.8% | -4.117 to +12.96 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.828 | 11.7 | +19.0% | +0.1502 to +3.585 | power given |
| pods started | 3.7 | 6 | +62.2% | -0.3347 to +4.935 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.702e-16 to +1.503e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 278.3 | +0.2% | -0.1205 to +1.469 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 278.3 | +0.2% | -0.1205 to +1.469 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.54 | 2.565 | +1.0% | +0.006632 to +0.04343 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.96 | 78.78 | +5.1% | +3.487 to +4.173 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.43 | 0.52 | +20.9% | +0.02737 to +0.1526 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4859 | 3178 | -34.6% | -3062 to -300.3 | GAIN |
| response time (ms), 99th percentile | 7366 | 6485 | -12.0% | -2706 to +944.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 68.42 | 67.08 | -2.0% | -3.052 to +0.3605 | EVEN, inside the noise (cut) |
| failed requests (%) | 51.65 | 57.85 | +12.0% | +2.368 to +10.03 | LOSS |
| HPA replicas, mean | 9.838 | 11.59 | +17.8% | +0.6628 to +2.843 | power given |
| pods started | 3.8 | 5.1 | +34.2% | -0.9124 to +3.512 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.757e-16 to +2.63e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278 | 278.4 | +0.1% | -0.658 to +1.492 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278 | 278.4 | +0.1% | -0.658 to +1.492 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.565 | 2.582 | +0.7% | -0.01569 to +0.0494 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.23 | 85.48 | +9.3% | +6.444 to +8.051 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.91 | 1.14 | +25.3% | +0.1405 to +0.3195 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3141 | 4357 | +38.7% | -642.5 to +3074 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5278 | 6325 | +19.8% | -746.5 to +2840 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 60.68 | 59.93 | -1.2% | -2.127 to +0.6284 | EVEN, inside the noise (cut) |
| failed requests (%) | 48.16 | 47.93 | -0.5% | -3.746 to +3.272 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.835 | 12.16 | +23.7% | +0.8463 to +3.807 | power given |
| pods started | 3.7 | 6.3 | +70.3% | +0.9758 to +4.224 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.89e-17 to +1.835e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 276.8 | -0.1% | -1.304 to +0.9377 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 276.8 | -0.1% | -1.304 to +0.9377 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.459 | 2.46 | +0.0% | -0.02168 to +0.02396 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.46 | 79.42 | +5.2% | +3.05 to +4.853 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.63 | 0.48 | -23.8% | -0.2941 to -0.005949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 1 (HPA replicas, mean), EVEN (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4798 | 4374 | -8.8% | -2141 to +1294 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 7600 | 6969 | -8.3% | -1831 to +568.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 68.02 | 66.72 | -1.9% | -3.997 to +1.397 | EVEN, inside the noise (cut) |
| failed requests (%) | 51.39 | 55.33 | +7.7% | +0.6953 to +7.182 | LOSS |
| HPA replicas, mean | 9.816 | 11.65 | +18.7% | +0.4782 to +3.195 | power given |
| pods started | 4.1 | 4.4 | +7.3% | -1.609 to +2.209 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003822 to +0.001479 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.4 | 278.1 | -0.1% | -1.209 to +0.6494 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.4 | 278.1 | -0.1% | -1.26 to +0.6301 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.535 | 2.542 | +0.3% | -0.007914 to +0.0222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.26 | 83.23 | +6.3% | +4.556 to +5.375 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.78 | 0.57 | -26.9% | -0.4271 to +0.007094 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3388 | 2852 | -15.8% | -1897 to +824.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5314 | 5033 | -5.3% | -1762 to +1201 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 48.39 | 48.69 | +0.6% | -3.879 to +4.488 | EVEN, inside the noise (up) |
| failed requests (%) | 37.04 | 40.99 | +10.7% | -2.725 to +10.64 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.785 | 12.42 | +26.9% | +1.073 to +4.188 | power given |
| pods started | 4.8 | 7.8 | +62.5% | +0.02194 to +5.978 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.349e-16 to +1.29e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.8 | +0.2% | -0.2692 to +1.286 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.8 | +0.2% | -0.2692 to +1.286 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.45 | +1.8% | +0.01518 to +0.06928 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.75 | 79.63 | +9.4% | +6.319 to +7.43 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.55 | 1.03 | +87.3% | +0.27 to +0.69 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
