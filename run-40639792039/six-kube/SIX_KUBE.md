# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2813 | 1650 | 2368 | 4261 | 2560 | 2188 |
| response time (ms), 99th percentile | 6286 | 4195 | 5264 | 6646 | 4586 | 4032 |
| time over the response line (% of samples) | 67.99 | 47.93 | 53.11 | 56.91 | 55.22 | 40.67 |
| failed requests (%) | 58.3 | 44.32 | 41.48 | 46.84 | 45.41 | 34.88 |
| HPA replicas, mean | 9.921 | 10.08 | 9.899 | 11.61 | 9.9 | 11.02 |
| pods started | 5 | 5.444 | 5.778 | 7.222 | 5.556 | 7.444 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1371 | 1382 | 1381 | 1377 | 1370 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1371 | 1382 | 1381 | 1377 | 1370 |
| CPU used with Omni's own (cores), mean | 2.631 | 2.401 | 2.515 | 2.514 | 2.456 | 2.368 |
| host CPU busy, the real machine under kind (%) | 77.81 | 73.99 | 75.04 | 82.08 | 75.22 | 75.37 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 |
| organism behind its window (s) | 2.189 | 2.667 | 4.378 | 5.5 | 3.133 | 3.744 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 8

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2813 | 1650 | -41.3% | -3889 to +1563 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6286 | 4195 | -33.3% | -6029 to +1845 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 67.99 | 47.93 | -29.5% | -56.77 to +16.67 | EVEN, inside the noise (cut) |
| failed requests (%) | 58.3 | 44.32 | -24.0% | -48.42 to +20.48 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.921 | 10.08 | +1.6% | -0.2434 to +0.5514 | EVEN, inside the noise (up) |
| pods started | 5 | 5.444 | +8.9% | -0.8367 to +1.726 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.904e-16 to +1.775e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1371 | -1.4% | -42.49 to +3.685 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1371 | -1.4% | -42.49 to +3.685 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.631 | 2.401 | -8.7% | -0.5421 to +0.08292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.81 | 73.99 | -4.9% | -14.21 to +6.566 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.189 | 2.667 | +21.8% | +0.09387 to +0.8617 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2368 | 4261 | +79.9% | -843.3 to +4629 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5264 | 6646 | +26.2% | -2523 to +5286 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.11 | 56.91 | +7.2% | -26.74 to +34.33 | EVEN, inside the noise (up) |
| failed requests (%) | 41.48 | 46.84 | +12.9% | -25.74 to +36.47 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.899 | 11.61 | +17.2% | +0.43 to +2.984 | power given |
| pods started | 5.778 | 7.222 | +25.0% | +0.1069 to +2.782 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003465 to +0.001369 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1382 | 1381 | -0.1% | -22.56 to +20.9 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1382 | 1381 | -0.1% | -22.73 to +20.75 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.515 | 2.514 | -0.0% | -0.2925 to +0.2907 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.04 | 82.08 | +9.4% | -2.409 to +16.49 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.378 | 5.5 | +25.6% | +0.6744 to +1.57 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), EVEN (inside the noise) on 8

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2560 | 2188 | -14.5% | -3233 to +2489 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4586 | 4032 | -12.1% | -4772 to +3665 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.22 | 40.67 | -26.3% | -66.09 to +37 | EVEN, inside the noise (cut) |
| failed requests (%) | 45.41 | 34.88 | -23.2% | -58.8 to +37.73 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.9 | 11.02 | +11.3% | -0.1853 to +2.419 | EVEN, inside the noise (up) |
| pods started | 5.556 | 7.444 | +34.0% | -0.2317 to +4.01 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.182e-15 to +1.182e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1370 | -0.5% | -42.32 to +27.61 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1370 | -0.5% | -42.32 to +27.61 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.456 | 2.368 | -3.6% | -0.5563 to +0.3809 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.22 | 75.37 | +0.2% | -15.62 to +15.91 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.133 | 3.744 | +19.5% | +0.2072 to +1.015 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
