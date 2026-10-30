# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1848 | 2914 | 2814 | 2515 | 2657 | 2711 | 2081 | 3427 |
| response time (ms), 99th percentile | 4068 | 5373 | 5227 | 5218 | 5236 | 5201 | 3844 | 5489 |
| time over the response line (% of samples) | 40.98 | 37.98 | 40.51 | 36.04 | 44.18 | 40.03 | 35.83 | 34.54 |
| failed requests (%) | 23.64 | 21.77 | 26.39 | 26.21 | 26.46 | 25.33 | 18.66 | 17.72 |
| HPA replicas, mean | 9.684 | 13.15 | 9.635 | 11.47 | 9.652 | 12.84 | 9.674 | 12.24 |
| pods started | 4.532 | 8.387 | 4.855 | 7.177 | 4.968 | 8.419 | 4.516 | 7.475 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | 183.8 | 184.2 | 183.8 | 184.1 | 183 | 183.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | 183.8 | 184.2 | 183.8 | 184.1 | 183 | 183.2 |
| CPU used with Omni's own (cores), mean | 2.332 | 2.346 | 2.339 | 2.352 | 2.345 | 2.349 | 2.269 | 2.288 |
| host CPU busy, the real machine under kind (%) | 68.62 | 69.89 | 69.24 | 70.12 | 68.79 | 69.72 | 68.02 | 70.92 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.0129 | 0.004839 | 0.009677 | 0.008065 | 0.009677 | 0.008065 | 0.1468 | 0.1672 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 0

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1848 | 2914 | +57.7% | +730.3 to +1401 | LOSS |
| response time (ms), 99th percentile | 4068 | 5373 | +32.1% | +804.8 to +1805 | LOSS |
| time over the response line (% of samples) | 40.98 | 37.98 | -7.3% | -4.361 to -1.643 | GAIN |
| failed requests (%) | 23.64 | 21.77 | -7.9% | -2.614 to -1.119 | GAIN |
| HPA replicas, mean | 9.684 | 13.15 | +35.8% | +2.919 to +4.02 | power given |
| pods started | 4.532 | 8.387 | +85.1% | +3.158 to +4.552 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.216e-16 to +1.924e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | +0.4% | +0.3441 to +1.046 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | +0.4% | +0.3441 to +1.046 | power given |
| CPU used with Omni's own (cores), mean | 2.332 | 2.346 | +0.6% | +0.008058 to +0.02064 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.62 | 69.89 | +1.8% | +1.077 to +1.454 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.0129 | 0.004839 | -62.5% | -0.0176 to +0.001471 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2814 | 2515 | -10.6% | -784.6 to +186.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5227 | 5218 | -0.2% | -441.8 to +422.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 40.51 | 36.04 | -11.0% | -5.687 to -3.262 | GAIN |
| failed requests (%) | 26.39 | 26.21 | -0.7% | -1.031 to +0.6683 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.635 | 11.47 | +19.1% | +1.24 to +2.434 | power given |
| pods started | 4.855 | 7.177 | +47.8% | +1.51 to +3.135 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.81e-16 to +3.529e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.2 | +0.2% | +0.02566 to +0.7009 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.2 | +0.2% | +0.02566 to +0.7009 | power given |
| CPU used with Omni's own (cores), mean | 2.339 | 2.352 | +0.5% | +0.003669 to +0.02199 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.24 | 70.12 | +1.3% | +0.6002 to +1.164 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.009677 | 0.008065 | -16.7% | -0.01239 to +0.009165 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2657 | 2711 | +2.0% | -328.8 to +437.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5236 | 5201 | -0.7% | -541.2 to +470.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 44.18 | 40.03 | -9.4% | -5.4 to -2.903 | GAIN |
| failed requests (%) | 26.46 | 25.33 | -4.3% | -1.775 to -0.4783 | GAIN |
| HPA replicas, mean | 9.652 | 12.84 | +33.1% | +2.555 to +3.83 | power given |
| pods started | 4.968 | 8.419 | +69.5% | +2.655 to +4.248 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.613e-16 to +2.181e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | +0.2% | -0.06382 to +0.6397 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | +0.2% | -0.06382 to +0.6397 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.345 | 2.349 | +0.2% | -0.004444 to +0.01293 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.79 | 69.72 | +1.4% | +0.6546 to +1.217 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.009677 | 0.008065 | -16.7% | -0.01136 to +0.008135 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

61 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2090 | 3427 | +64.0% | +861.3 to +1814 | LOSS |
| response time (ms), 99th percentile | 3856 | 5489 | +42.3% | +988.2 to +2277 | LOSS |
| time over the response line (% of samples) | 35.41 | 34.54 | -2.5% | -2.161 to +0.422 | EVEN, inside the noise (cut) |
| failed requests (%) | 18.34 | 17.72 | -3.4% | -1.83 to +0.5789 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.669 | 12.24 | +26.6% | +2.026 to +3.121 | power given |
| pods started | 4.59 | 7.475 | +62.9% | +2.244 to +3.526 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.211e-16 to +2.92e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.2 | +0.2% | -0.02842 to +0.6566 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.2 | +0.2% | -0.02842 to +0.6566 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.263 | 2.288 | +1.1% | +0.01962 to +0.03029 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.84 | 70.92 | +4.5% | +2.902 to +3.245 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1475 | 0.1672 | +13.3% | -0.00166 to +0.041 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
