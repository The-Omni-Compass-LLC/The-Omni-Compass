# Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 90): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438326588 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39438344234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438362894 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.0% (-0.4 to +0.3) | -0.2% (-0.7 to +0.4) | +0.2% (+0.0 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.0% (-0.4 to +0.4) | -0.2% (-0.7 to +0.4) | +0.3% (+0.0 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.0% (-0.4 to +0.4) | -0.2% (-0.7 to +0.4) | +0.3% (+0.0 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), mean | -2.1% (-4.3 to +0.1) | -0.0% (-2.8 to +2.7) | -1.7% (-3.2 to -0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), 95th percentile | -3.3% (-6.2 to -0.4) | -1.8% (-6.8 to +3.1) | -4.6% (-8.2 to -0.9) | EVEN, no difference beyond the noise (1 of 3 runs) |
| response time (ms), 99th percentile | -3.8% (-9.3 to +1.7) | +3.4% (+0.3 to +6.5) | -5.7% (-9.5 to -1.9) | **the runs disagree** |
| time over the response line (% of samples) | -22.2% (-69.0 to +24.6) | -26.8% (-73.8 to +20.3) | -23.8% (-55.3 to +7.7) | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -66.7% (-167.2 to +33.9) | +0 (+0 to +0) | -100.0% (-215.2 to +15.2) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +2.6 (+0.8414 to +4.359) | +1.2 (+0.2583 to +2.142) | +1.5 (+0.5315 to +2.469) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +11.1% (-98.8 to +121.1) | +99.1% (-51.3 to +249.6) | +37.0% (-57.8 to +131.8) | shown, not judged |
| utilisation (used / allocatable) | +0.9% (-0.9 to +2.7) | +0.1% (-1.5 to +1.8) | +1.7% (+0.1 to +3.2) | shown, not judged |
| CPU used (cores), mean | +0.9% (-0.9 to +2.7) | +0.1% (-1.5 to +1.8) | +1.7% (+0.1 to +3.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00617 (+0.005381 to +0.006959) | +0.00568 (+0.004916 to +0.006444) | +0.00596 (+0.005506 to +0.006414) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.6% (-0.3 to +3.4) | +0.8% (-0.9 to +2.4) | +2.3% (+0.7 to +3.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.6% (-2.5 to +1.2) | +0.0% (-1.6 to +1.6) | -1.5% (-2.9 to -0.1) | shown, not judged |
| HPA replicas, mean | +15.8% (+8.0 to +23.7) | +9.0% (+1.9 to +16.1) | +11.4% (+4.6 to +18.2) | **power given in all three of our runs** |
| pods started | +78.0% (+34.7 to +121.4) | +34.7% (-10.5 to +79.8) | +57.8% (+18.0 to +97.6) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, total (s) | +60.3% (+15.0 to +105.6) | +28.7% (-22.5 to +80.0) | +69.0% (+30.9 to +107.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, mean (s) | -10.0% (-35.1 to +15.1) | -5.9% (-21.7 to +10.0) | +7.8% (-10.1 to +25.7) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +1.9% (-0.1 to +3.9) | +1.9% (+0.1 to +3.6) | +2.7% (+1.1 to +4.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 1 power given in all three of our runs, 1 the runs disagree, 3 EVEN, no difference beyond the noise (1 of 3 runs), 4 EVEN, no difference beyond the noise (2 of 3 runs), 3 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
