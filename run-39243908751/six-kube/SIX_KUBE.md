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
| response time (ms), 95th percentile | 4016 | 4752 | 4550 | 3017 | 4196 | 3348 | 4001 | 2807 | 3715 | 2501 |
| response time (ms), 99th percentile | 6504 | 6815 | 6767 | 5723 | 6524 | 5737 | 6694 | 5648 | 6252 | 5472 |
| time over the response line (% of samples) | 55.17 | 55.38 | 62.47 | 61.34 | 58.6 | 57.66 | 54.81 | 54.8 | 60.88 | 59.35 |
| failed requests (%) | 39.69 | 42.93 | 46.78 | 51.92 | 43.53 | 48.45 | 38.9 | 44.9 | 48.5 | 52.18 |
| HPA replicas, mean | 9.816 | 13.25 | 9.808 | 12.27 | 9.812 | 12.61 | 9.799 | 12.33 | 9.822 | 12.08 |
| pods started | 4.05 | 7.85 | 4.325 | 6.9 | 4.275 | 7 | 4.5 | 7.475 | 4.125 | 6.35 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.998 | 5.997 | 6 | 6 | 6 | 6 | 5.994 |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.8 | 277.8 | 278.5 | 277.5 | 277.6 | 277.3 | 277.8 | 277.7 | 278 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.7 | 277.8 | 278.4 | 277.4 | 277.6 | 277.3 | 277.8 | 277.7 | 277.8 |
| CPU used with Omni's own (cores), mean | 2.468 | 2.509 | 2.522 | 2.562 | 2.494 | 2.523 | 2.479 | 2.513 | 2.513 | 2.546 |
| host CPU busy, the real machine under kind (%) | 73.42 | 77.42 | 76.5 | 84.21 | 76.39 | 81.19 | 76.03 | 81.81 | 76.4 | 83.31 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.4175 | 0.535 | 0.92 | 1.283 | 0.5675 | 0.47 | 0.715 | 0.4525 | 0.5425 | 1.155 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4016 | 4752 | +18.3% | +159.2 to +1312 | LOSS |
| response time (ms), 99th percentile | 6504 | 6815 | +4.8% | -147.2 to +769 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.17 | 55.38 | +0.4% | -0.8654 to +1.29 | EVEN, inside the noise (up) |
| failed requests (%) | 39.69 | 42.93 | +8.2% | +1.271 to +5.218 | LOSS |
| HPA replicas, mean | 9.816 | 13.25 | +35.0% | +2.747 to +4.119 | power given |
| pods started | 4.05 | 7.85 | +93.8% | +2.901 to +4.699 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002801 to +0.0009479 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.8 | +0.3% | +0.1904 to +1.366 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.7 | +0.3% | +0.1836 to +1.315 | power given |
| CPU used with Omni's own (cores), mean | 2.468 | 2.509 | +1.7% | +0.03044 to +0.05205 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.42 | 77.42 | +5.4% | +3.742 to +4.252 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4175 | 0.535 | +28.1% | +0.06006 to +0.1749 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4550 | 3017 | -33.7% | -2214 to -851.7 | GAIN |
| response time (ms), 99th percentile | 6767 | 5723 | -15.4% | -1646 to -440.1 | GAIN |
| time over the response line (% of samples) | 62.47 | 61.34 | -1.8% | -2.361 to +0.1057 | EVEN, inside the noise (cut) |
| failed requests (%) | 46.78 | 51.92 | +11.0% | +3.706 to +6.573 | LOSS |
| HPA replicas, mean | 9.808 | 12.27 | +25.1% | +1.88 to +3.053 | power given |
| pods started | 4.325 | 6.9 | +59.5% | +1.731 to +3.419 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.006144 to +0.001401 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 278.5 | +0.3% | +0.1828 to +1.306 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 278.4 | +0.2% | +0.09158 to +1.253 | power given |
| CPU used with Omni's own (cores), mean | 2.522 | 2.562 | +1.6% | +0.02363 to +0.05619 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.5 | 84.21 | +10.1% | +7.249 to +8.184 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.92 | 1.283 | +39.4% | +0.2625 to +0.4625 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4196 | 3348 | -20.2% | -1547 to -150.8 | GAIN |
| response time (ms), 99th percentile | 6524 | 5737 | -12.1% | -1327 to -246.3 | GAIN |
| time over the response line (% of samples) | 58.6 | 57.66 | -1.6% | -1.98 to +0.1021 | EVEN, inside the noise (cut) |
| failed requests (%) | 43.53 | 48.45 | +11.3% | +2.887 to +6.957 | LOSS |
| HPA replicas, mean | 9.812 | 12.61 | +28.5% | +2.191 to +3.403 | power given |
| pods started | 4.275 | 7 | +63.7% | +1.786 to +3.664 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.0% | -0.001936 to +0.007406 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.6 | +0.1% | -0.2263 to +0.562 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.4 | 277.6 | +0.1% | -0.1751 to +0.6764 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.494 | 2.523 | +1.2% | +0.01794 to +0.0398 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.39 | 81.19 | +6.3% | +4.542 to +5.067 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5675 | 0.47 | -17.2% | -0.1729 to -0.02205 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4001 | 2807 | -29.8% | -2006 to -382.3 | GAIN |
| response time (ms), 99th percentile | 6694 | 5648 | -15.6% | -1745 to -346.2 | GAIN |
| time over the response line (% of samples) | 54.81 | 54.8 | -0.0% | -1.384 to +1.364 | EVEN, inside the noise (cut) |
| failed requests (%) | 38.9 | 44.9 | +15.4% | +4.135 to +7.857 | LOSS |
| HPA replicas, mean | 9.799 | 12.33 | +25.9% | +1.918 to +3.15 | power given |
| pods started | 4.5 | 7.475 | +66.1% | +2.083 to +3.867 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.599e-16 to +4.823e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.8 | +0.2% | -0.01314 to +0.8956 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.8 | +0.2% | -0.01314 to +0.8956 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.479 | 2.513 | +1.4% | +0.02183 to +0.04661 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.03 | 81.81 | +7.6% | +5.412 to +6.146 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.715 | 0.4525 | -36.7% | -0.3299 to -0.1951 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3715 | 2501 | -32.7% | -1853 to -575.7 | GAIN |
| response time (ms), 99th percentile | 6252 | 5472 | -12.5% | -1567 to +6.096 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 60.88 | 59.35 | -2.5% | -2.867 to -0.1828 | GAIN |
| failed requests (%) | 48.5 | 52.18 | +7.6% | +1.801 to +5.558 | LOSS |
| HPA replicas, mean | 9.822 | 12.08 | +23.0% | +1.612 to +2.905 | power given |
| pods started | 4.125 | 6.35 | +53.9% | +1.31 to +3.14 | power given |
| worker nodes in service, mean | 6 | 5.994 | -0.1% | -0.01668 to +0.004522 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 278 | +0.1% | -0.1911 to +0.8537 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 277.8 | +0.1% | -0.5384 to +0.8344 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.513 | 2.546 | +1.3% | +0.01825 to +0.04736 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.4 | 83.31 | +9.0% | +6.567 to +7.245 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5425 | 1.155 | +112.9% | +0.5172 to +0.7078 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
