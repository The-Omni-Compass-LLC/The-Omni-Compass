# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 500 copies: native | The whole tower, every muscle once, 500 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 1354 | 2371 |
| response time (ms), 99th percentile | 3897 | 6180 |
| time over the response line (% of samples) | 44.14 | 61.73 |
| failed requests (%) | 36.56 | 57.92 |
| HPA replicas, mean | 9.926 | 13.18 |
| pods started | 5.8 | 8.7 |
| worker nodes in service, mean | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 2287 | 2302 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2287 | 2301 |
| CPU used with Omni's own (cores), mean | 2.402 | 2.527 |
| host CPU busy, the real machine under kind (%) | 74.52 | 86.47 |
| organism work | 3.431e+13 | 3.431e+13 |
| organism energy (J) | 5.537e+15 | 5.537e+15 |
| organism time over the line (% of steps) | 2.604 | 2.567 |
| organism work per energy | 0.006197 | 0.006197 |
| organism behind its window (s) | 7.27 | 10.98 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1354 | 2371 | +75.0% | +55.83 to +1977 | LOSS |
| response time (ms), 99th percentile | 3897 | 6180 | +58.6% | -681.2 to +5248 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 44.14 | 61.73 | +39.8% | -17.14 to +52.32 | EVEN, inside the noise (up) |
| failed requests (%) | 36.56 | 57.92 | +58.4% | -15.46 to +58.18 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.926 | 13.18 | +32.8% | +2.006 to +4.509 | power given |
| pods started | 5.8 | 8.7 | +50.0% | +1.71 to +4.09 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004457 to -5.551e-05 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 2287 | 2302 | +0.6% | -22.15 to +50.49 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2287 | 2301 | +0.6% | -22.66 to +49.87 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.402 | 2.527 | +5.2% | -0.1618 to +0.4119 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.52 | 86.47 | +16.0% | +1.448 to +22.45 | shown, not judged |
| organism work | 3.431e+13 | 3.431e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.537e+15 | 5.537e+15 | +0.0% | +4.35e+09 to +4.35e+09 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.604 | 2.567 | -1.4% | -0.03767 to -0.03767 | GAIN |
| organism work per energy | 0.006197 | 0.006197 | -0.0% | -4.868e-09 to -4.868e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 7.27 | 10.98 | +51.0% | +2.582 to +4.838 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
