# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3465 | 4406 |
| response time (ms), 99th percentile | 6101 | 6948 |
| time over the response line (% of samples) | 52.2 | 47.98 |
| failed requests (%) | 31.91 | 29.12 |
| HPA replicas, mean | 9.706 | 13.59 |
| pods started | 4.271 | 8.647 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.6 |
| CPU used with Omni's own (cores), mean | 2.466 | 2.48 |
| host CPU busy, the real machine under kind (%) | 73.18 | 74.8 |
| organism work | 6.905e+11 | 6.905e+11 |
| organism energy (J) | 1.108e+14 | 1.108e+14 |
| organism time over the line (% of steps) | 2.707 | 2.671 |
| organism work per energy | 0.006233 | 0.006233 |
| organism behind its window (s) | 0.1012 | 0.2235 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 0

85 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3465 | 4406 | +27.2% | +524.2 to +1358 | LOSS |
| response time (ms), 99th percentile | 6101 | 6948 | +13.9% | +440.3 to +1254 | LOSS |
| time over the response line (% of samples) | 52.2 | 47.98 | -8.1% | -5.357 to -3.095 | GAIN |
| failed requests (%) | 31.91 | 29.12 | -8.8% | -3.698 to -1.888 | GAIN |
| HPA replicas, mean | 9.706 | 13.59 | +40.0% | +3.531 to +4.232 | power given |
| pods started | 4.271 | 8.647 | +102.5% | +3.86 to +4.893 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.249e-16 to +1.577e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.6 | +0.3% | +0.1847 to +0.7995 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.6 | +0.3% | +0.1847 to +0.7995 | power given |
| CPU used with Omni's own (cores), mean | 2.466 | 2.48 | +0.5% | +0.007999 to +0.01873 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.18 | 74.8 | +2.2% | +1.476 to +1.765 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1012 | 0.2235 | +120.9% | +0.1081 to +0.1366 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
