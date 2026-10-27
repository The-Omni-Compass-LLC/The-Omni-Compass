# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3681 | 4139 | 3622 | 2450 | 4115 | 2995 | 4657 | 2893 | 2573 | 2594 |
| response time (ms), 99th percentile | 5821 | 6367 | 5753 | 4768 | 6335 | 5475 | 7082 | 5954 | 4731 | 4623 |
| time over the response line (% of samples) | 55.45 | 53.07 | 54.14 | 52.35 | 55.86 | 53.8 | 62.69 | 60.18 | 49.16 | 48.1 |
| failed requests (%) | 41.31 | 42.93 | 41.45 | 45.44 | 39.82 | 44.77 | 46.56 | 51.33 | 40.28 | 41.36 |
| HPA replicas, mean | 9.801 | 13.17 | 9.79 | 11.85 | 9.789 | 11.46 | 9.818 | 11.87 | 9.783 | 12.02 |
| pods started | 4.275 | 7.949 | 4.625 | 6.625 | 4.475 | 6.725 | 4.25 | 6.225 | 4.525 | 7.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.998 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 277 | 276.3 | 276.6 | 277.1 | 277.3 | 278.2 | 278 | 275.3 | 276.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 277 | 276.3 | 276.6 | 277.1 | 277.2 | 278.2 | 278 | 275.3 | 276.1 |
| CPU used with Omni's own (cores), mean | 2.454 | 2.479 | 2.414 | 2.458 | 2.46 | 2.48 | 2.526 | 2.555 | 2.366 | 2.409 |
| host CPU busy, the real machine under kind (%) | 72.85 | 76.61 | 73.33 | 80.93 | 75.22 | 80.11 | 77.73 | 83.48 | 71.92 | 79.03 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.4225 | 0.5641 | 0.9475 | 1.328 | 0.59 | 0.435 | 0.7825 | 1.315 | 0.51 | 1.12 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

39 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3690 | 4139 | +12.1% | -269.3 to +1166 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5803 | 6367 | +9.7% | -81.39 to +1209 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.83 | 53.07 | -3.2% | -2.805 to -0.7237 | GAIN |
| failed requests (%) | 40.76 | 42.93 | +5.3% | -0.2809 to +4.62 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.801 | 13.17 | +34.3% | +2.612 to +4.117 | power given |
| pods started | 4.256 | 7.949 | +86.7% | +2.662 to +4.723 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.755e-16 to +3.289e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 277 | +0.1% | -0.05586 to +0.622 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 277 | +0.1% | -0.05586 to +0.622 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.449 | 2.479 | +1.2% | +0.02203 to +0.03736 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.7 | 76.61 | +5.4% | +3.645 to +4.175 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4256 | 0.5641 | +32.5% | +0.07687 to +0.2001 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3622 | 2450 | -32.4% | -1748 to -595.5 | GAIN |
| response time (ms), 99th percentile | 5753 | 4768 | -17.1% | -1609 to -361.8 | GAIN |
| time over the response line (% of samples) | 54.14 | 52.35 | -3.3% | -2.942 to -0.6313 | GAIN |
| failed requests (%) | 41.45 | 45.44 | +9.6% | +2.47 to +5.518 | LOSS |
| HPA replicas, mean | 9.79 | 11.85 | +21.0% | +1.519 to +2.599 | power given |
| pods started | 4.625 | 6.625 | +43.2% | +0.9807 to +3.019 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.841e-16 to +3.845e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.6 | +0.1% | -0.2556 to +0.8502 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.6 | +0.1% | -0.2556 to +0.8502 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.414 | 2.458 | +1.8% | +0.02702 to +0.06225 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.33 | 80.93 | +10.4% | +7.16 to +8.043 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.9475 | 1.328 | +40.1% | +0.2514 to +0.5086 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4115 | 2995 | -27.2% | -1995 to -244.5 | GAIN |
| response time (ms), 99th percentile | 6335 | 5475 | -13.6% | -1727 to +7.79 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.86 | 53.8 | -3.7% | -3.604 to -0.5194 | GAIN |
| failed requests (%) | 39.82 | 44.77 | +12.4% | +2.106 to +7.788 | LOSS |
| HPA replicas, mean | 9.789 | 11.46 | +17.0% | +1.024 to +2.313 | power given |
| pods started | 4.475 | 6.725 | +50.3% | +1.257 to +3.243 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005729 to +0.001939 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 277.3 | +0.1% | -0.241 to +0.5294 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.1 | 277.2 | +0.0% | -0.3315 to +0.5053 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.46 | 2.48 | +0.8% | +0.003833 to +0.03514 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.22 | 80.11 | +6.5% | +4.586 to +5.198 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.59 | 0.435 | -26.3% | -0.2363 to -0.07371 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4657 | 2893 | -37.9% | -2616 to -912 | GAIN |
| response time (ms), 99th percentile | 7082 | 5954 | -15.9% | -1865 to -391 | GAIN |
| time over the response line (% of samples) | 62.69 | 60.18 | -4.0% | -3.585 to -1.44 | GAIN |
| failed requests (%) | 46.56 | 51.33 | +10.2% | +2.598 to +6.937 | LOSS |
| HPA replicas, mean | 9.818 | 11.87 | +20.9% | +1.394 to +2.713 | power given |
| pods started | 4.25 | 6.225 | +46.5% | +0.7383 to +3.212 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002822 to +0.0009551 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.2 | 278 | -0.1% | -0.6685 to +0.2614 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.2 | 278 | -0.1% | -0.7076 to +0.2442 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.526 | 2.555 | +1.2% | +0.01774 to +0.04047 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.73 | 83.48 | +7.4% | +5.407 to +6.09 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7825 | 1.315 | +68.1% | -1.206 to +2.271 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2573 | 2594 | +0.8% | -606.7 to +647.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4731 | 4623 | -2.3% | -771.8 to +555.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 49.16 | 48.1 | -2.1% | -2.222 to +0.1137 | EVEN, inside the noise (cut) |
| failed requests (%) | 40.28 | 41.36 | +2.7% | -0.3384 to +2.502 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.783 | 12.02 | +22.9% | +1.597 to +2.88 | power given |
| pods started | 4.525 | 7.1 | +56.9% | +1.559 to +3.591 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004626 to +0.001132 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 276.2 | +0.3% | +0.3645 to +1.368 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 276.1 | +0.3% | +0.321 to +1.306 | power given |
| CPU used with Omni's own (cores), mean | 2.366 | 2.409 | +1.8% | +0.02725 to +0.0582 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.92 | 79.03 | +9.9% | +6.77 to +7.449 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.51 | 1.12 | +119.6% | +0.5272 to +0.6928 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
