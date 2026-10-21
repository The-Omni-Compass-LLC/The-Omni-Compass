# Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Karmada against the organism alone (register row 95): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438525862 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438541616 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438559009 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -8.9% (-19.0 to +1.3) | -8.8% (-19.3 to +1.7) | -15.3% (-29.5 to -1.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| node-hours | -8.7% (-18.7 to +1.3) | -8.9% (-19.2 to +1.5) | -15.0% (-29.3 to -0.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.6% (+0.2 to +1.0) | +0.1% (-0.4 to +0.6) | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -5.8% (-13.1 to +1.5) | -6.3% (-13.6 to +1.1) | -10.8% (-21.0 to -0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), mean | +45.7% (+15.8 to +75.5) | +33.1% (+14.0 to +52.3) | +25.0% (+7.6 to +42.4) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | +81.3% (+33.4 to +129.1) | +62.1% (+27.0 to +97.3) | +38.8% (+13.8 to +63.9) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | +73.4% (+34.4 to +112.5) | +64.1% (+30.5 to +97.7) | +36.5% (+13.7 to +59.4) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | +17.9% (+8.8 to +27.1) | +12.6% (+0.3 to +25.0) | +22.4% (+7.1 to +37.8) | **LOSS in all three of our runs** |
| failed requests (%) | +912.6% (+76.0 to +1749.3) | +0.1452 (-0.008503 to +0.299) | +1119.8% (-207.1 to +2446.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +45.1% (+21.3 to +68.9) | +34.5% (+21.0 to +48.0) | +30.8% (+18.3 to +43.2) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +43.11 (+37.35 to +48.87) | +44.3 (+31.46 to +57.14) | +48.2 (+35.57 to +60.83) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +72.7% (+3.8 to +141.5) | +168.6% (-66.5 to +403.7) | +214.1% (+36.2 to +392.0) | shown, not judged |
| utilisation (used / allocatable) | +16.5% (+7.6 to +25.4) | +11.8% (-2.4 to +25.9) | +13.7% (-5.0 to +32.3) | shown, not judged |
| CPU used (cores), mean | +6.4% (+0.6 to +12.2) | +1.4% (-6.5 to +9.3) | -4.6% (-11.0 to +1.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0099 (+0.008994 to +0.01081) | +0.00974 (+0.008487 to +0.01099) | +0.0097 (+0.008547 to +0.01085) | shown, not judged |
| CPU used with Omni's own (cores), mean | +7.0% (+1.2 to +12.8) | +2.0% (-5.9 to +9.9) | -4.0% (-10.4 to +2.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -11.6% (-17.2 to -5.9) | -8.9% (-19.1 to +1.4) | -9.4% (-23.0 to +4.2) | shown, not judged |
| HPA replicas, mean | +15.7% (+6.2 to +25.3) | +10.2% (+0.6 to +19.9) | +17.6% (+8.3 to +26.8) | **power given in all three of our runs** |
| pods started | +700.0% (-131.4 to +1531.4) | +1.1 (+0.3128 to +1.887) | +1 (+0.1079 to +1.892) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, total (s) | +600.0% (-258.5 to +1458.5) | +1.9 (+0.4914 to +3.309) | +2.2 (-0.08202 to +4.482) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, mean (s) | +98.1% (-145.9 to +342.1) | +1.033 (+0.3341 to +1.733) | +1.225 (+0.2048 to +2.245) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU busy, the real machine under kind (%) | +16.9% (+11.3 to +22.4) | +17.4% (+13.8 to +21.0) | +15.7% (+11.1 to +20.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +16.5% (+7.4 to +25.6) | +15.7% (+8.5 to +23.0) | +14.3% (+5.7 to +22.9) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -16.5% (-34.4 to +1.4) | -16.1% (-33.9 to +1.7) | -25.3% (-48.7 to -1.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job wait, submitted to its first pod running, mean (s) | +2550.0% (-2197.6 to +7297.6) | +3040.0% (-1048.9 to +7128.9) | +18419.0% (+3305.6 to +33532.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +180.0% (+82.2 to +277.8) | +183.3% (+52.1 to +314.5) | +24360.0% (+1893.1 to +46826.9) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +83.0% (+40.0 to +126.1) | +78.2% (+42.6 to +113.8) | +57.9% (+24.1 to +91.8) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 8 LOSS in all three of our runs, 1 power given in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 8 EVEN, no difference beyond the noise (2 of 3 runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
