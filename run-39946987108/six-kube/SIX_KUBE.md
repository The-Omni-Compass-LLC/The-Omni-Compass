# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3880 | 2252 | 3480 | 2430 | 3345 | 1792 | 3924 | 3500 | 3471 | 3184 |
| response time (ms), 99th percentile | 5808 | 5300 | 5497 | 4677 | 5295 | 4332 | 6136 | 6006 | 5742 | 5601 |
| time over the response line (% of samples) | 57 | 55.35 | 53.28 | 52.33 | 53.57 | 51.39 | 62.19 | 60.68 | 53.41 | 53.84 |
| failed requests (%) | 43.39 | 48.4 | 41.33 | 44.51 | 41.95 | 45.4 | 47.7 | 48.42 | 42.09 | 43.18 |
| HPA replicas, mean | 9.821 | 12.81 | 9.802 | 11.46 | 9.809 | 11.87 | 9.83 | 11.27 | 9.805 | 11.68 |
| pods started | 3.86 | 9.84 | 4.5 | 7.7 | 4.1 | 9.28 | 3.78 | 8.3 | 4.22 | 7.58 |
| worker nodes in service, mean | 6 | 5.996 | 6 | 6 | 5.999 | 6 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.9 | 276.3 | 277 | 275.9 | 276.3 | 277.8 | 277.7 | 276.2 | 276.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.8 | 276.3 | 277 | 275.8 | 276.3 | 277.8 | 277.7 | 276.2 | 276.5 |
| CPU used with Omni's own (cores), mean | 2.441 | 2.493 | 2.424 | 2.48 | 2.395 | 2.445 | 2.504 | 2.552 | 2.423 | 2.487 |
| host CPU busy, the real machine under kind (%) | 72.76 | 77.41 | 73.74 | 81.96 | 73.77 | 79.52 | 77.47 | 83.86 | 74.09 | 81.97 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.454 | 0.508 | 0.914 | 1.188 | 0.57 | 0.42 | 0.764 | 0.508 | 0.512 | 1.066 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3880 | 2252 | -42.0% | -2306 to -950.3 | GAIN |
| response time (ms), 99th percentile | 5808 | 5300 | -8.7% | -1021 to +5.291 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 57 | 55.35 | -2.9% | -2.552 to -0.7409 | GAIN |
| failed requests (%) | 43.39 | 48.4 | +11.5% | +3.668 to +6.349 | LOSS |
| HPA replicas, mean | 9.821 | 12.81 | +30.5% | +2.627 to +3.357 | power given |
| pods started | 3.86 | 9.84 | +154.9% | +4.952 to +7.008 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.008889 to +0.001669 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.9 | +0.2% | -0.03109 to +0.8623 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.8 | +0.1% | -0.2141 to +0.8269 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.441 | 2.493 | +2.1% | +0.04107 to +0.06304 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.76 | 77.41 | +6.4% | +4.426 to +4.876 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.454 | 0.508 | +11.9% | -0.008174 to +0.1162 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3480 | 2430 | -30.2% | -1573 to -526.8 | GAIN |
| response time (ms), 99th percentile | 5497 | 4677 | -14.9% | -1408 to -231.3 | GAIN |
| time over the response line (% of samples) | 53.28 | 52.33 | -1.8% | -2.621 to +0.7118 | EVEN, inside the noise (cut) |
| failed requests (%) | 41.33 | 44.51 | +7.7% | +1.64 to +4.729 | LOSS |
| HPA replicas, mean | 9.802 | 11.46 | +16.9% | +0.9992 to +2.318 | power given |
| pods started | 4.5 | 7.7 | +71.1% | +2.287 to +4.113 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.686e-16 to +3.422e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 277 | +0.3% | +0.3061 to +1.119 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 277 | +0.3% | +0.3061 to +1.119 | power given |
| CPU used with Omni's own (cores), mean | 2.424 | 2.48 | +2.3% | +0.03901 to +0.07332 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.74 | 81.96 | +11.1% | +7.801 to +8.629 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.914 | 1.188 | +30.0% | +0.1892 to +0.3588 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3345 | 1792 | -46.4% | -2104 to -1002 | GAIN |
| response time (ms), 99th percentile | 5295 | 4332 | -18.2% | -1547 to -378.9 | GAIN |
| time over the response line (% of samples) | 53.57 | 51.39 | -4.1% | -3.102 to -1.26 | GAIN |
| failed requests (%) | 41.95 | 45.4 | +8.2% | +1.951 to +4.933 | LOSS |
| HPA replicas, mean | 9.809 | 11.87 | +21.0% | +1.527 to +2.593 | power given |
| pods started | 4.1 | 9.28 | +126.3% | +3.865 to +6.495 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0008941 to +0.002664 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 276.3 | +0.1% | -0.0499 to +0.8634 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 276.3 | +0.2% | -0.03706 to +0.9039 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.395 | 2.445 | +2.1% | +0.03669 to +0.06354 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.77 | 79.52 | +7.8% | +5.445 to +6.045 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.57 | 0.42 | -26.3% | -0.2046 to -0.09544 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3924 | 3500 | -10.8% | -926.4 to +79.48 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6136 | 6006 | -2.1% | -678.6 to +418.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 62.19 | 60.68 | -2.4% | -2.652 to -0.3746 | GAIN |
| failed requests (%) | 47.7 | 48.42 | +1.5% | -0.376 to +1.814 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.83 | 11.27 | +14.7% | +0.8536 to +2.028 | power given |
| pods started | 3.78 | 8.3 | +119.6% | +3.188 to +5.852 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003671 to +0.0007745 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 277.7 | -0.0% | -0.4627 to +0.3617 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 277.7 | -0.0% | -0.5162 to +0.3277 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.504 | 2.552 | +1.9% | +0.03154 to +0.06378 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.47 | 83.86 | +8.3% | +5.972 to +6.811 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.764 | 0.508 | -33.5% | -0.3375 to -0.1745 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 7

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3471 | 3184 | -8.3% | -907.9 to +334.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5742 | 5601 | -2.5% | -726.3 to +443.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 53.41 | 53.84 | +0.8% | -1.348 to +2.206 | EVEN, inside the noise (up) |
| failed requests (%) | 42.09 | 43.18 | +2.6% | -0.3947 to +2.579 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.805 | 11.68 | +19.1% | +1.21 to +2.532 | power given |
| pods started | 4.22 | 7.58 | +79.6% | +2.398 to +4.322 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005181 to +0.001739 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.6 | +0.1% | -0.01457 to +0.8206 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 276.5 | +0.1% | -0.04364 to +0.7455 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.423 | 2.487 | +2.6% | +0.04665 to +0.0805 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.09 | 81.97 | +10.6% | +7.453 to +8.296 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.512 | 1.066 | +108.2% | +0.4841 to +0.6239 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
