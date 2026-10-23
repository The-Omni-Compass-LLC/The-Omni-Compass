# Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against Karmada as shipped (register row 95): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the orchestrator as shipped: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438525862 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438541616 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438559009 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -9.1% (-19.2 to +0.9) | -12.4% (-24.8 to +0.0) | -16.6% (-31.8 to -1.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| node-hours | -9.2% (-19.3 to +1.0) | -12.3% (-24.7 to +0.1) | -16.4% (-31.9 to -0.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.0% (-0.2 to +0.2) | +0.1% (-0.2 to +0.4) | +0.1% (-0.5 to +0.6) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -6.5% (-13.8 to +0.7) | -8.8% (-17.7 to +0.2) | -11.8% (-23.1 to -0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), mean | -20.7% (-30.9 to -10.4) | -21.1% (-30.5 to -11.6) | -20.7% (-33.6 to -7.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -25.4% (-43.1 to -7.7) | -24.7% (-41.7 to -7.6) | -23.2% (-39.4 to -7.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -25.8% (-41.3 to -10.3) | -27.2% (-42.4 to -12.1) | -19.5% (-33.7 to -5.3) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -5.0% (-13.9 to +3.9) | -7.6% (-15.1 to -0.1) | -9.3% (-16.3 to -2.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| failed requests (%) | -100.0% (-241.3 to +41.3) | -100.0% (-267.8 to +67.8) | -66.4% (-208.7 to +76.0) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -14.6% (-23.6 to -5.6) | -10.9% (-17.0 to -4.8) | -20.4% (-38.5 to -2.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +68.22 (+39.17 to +97.28) | +64.7 (+36.32 to +93.08) | +74.1 (+40.94 to +107.3) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -51.1% (-108.0 to +5.7) | -56.8% (-130.4 to +16.7) | -29.6% (-75.8 to +16.7) | shown, not judged |
| utilisation (used / allocatable) | +10.7% (-3.3 to +24.7) | +15.3% (-0.6 to +31.3) | +15.9% (-2.2 to +34.0) | shown, not judged |
| CPU used (cores), mean | +0.2% (-5.1 to +5.5) | +0.1% (-8.3 to +8.5) | -4.3% (-12.8 to +4.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0133 (+0.01188 to +0.01472) | +0.01306 (+0.01216 to +0.01396) | +0.01268 (+0.01201 to +0.01335) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.0% (-4.3 to +6.3) | +0.9% (-7.6 to +9.3) | -3.6% (-12.0 to +4.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -7.7% (-17.7 to +2.2) | -9.8% (-20.3 to +0.7) | -9.9% (-21.8 to +2.1) | shown, not judged |
| HPA replicas, mean | +10.1% (+5.2 to +15.0) | +4.9% (-3.9 to +13.6) | +3.3% (-5.7 to +12.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pods started | +175.0% (-14.0 to +364.0) | +60.0% (-142.9 to +262.9) | +100.0% (-50.8 to +250.8) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +100.0% (-48.6 to +248.6) | +9.1% (-162.8 to +181.0) | +72.7% (-105.5 to +250.9) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +66.7% (-35.0 to +168.4) | +46.2% (-124.3 to +216.6) | +47.1% (-53.7 to +147.8) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -6.6% (-9.0 to -4.1) | -7.7% (-9.6 to -5.7) | -8.3% (-11.0 to -5.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | -8.0% (-12.5 to -3.5) | -9.0% (-12.9 to -5.0) | -8.1% (-12.4 to -3.8) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -17.3% (-35.2 to +0.6) | -20.9% (-39.6 to -2.2) | -26.2% (-49.8 to -2.5) | EVEN, no difference beyond the noise (1 of 3 runs) |
| queue: job wait, submitted to its first pod running, mean (s) | -97.0% (-300.9 to +106.8) | -94.2% (-261.5 to +73.1) | -99.0% (-201.5 to +3.6) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -98.2% (-322.3 to +125.9) | -46.7% (-97.2 to +3.9) | -99.2% (-245.5 to +47.0) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | -29.5% (-44.7 to -14.2) | -34.5% (-50.2 to -18.9) | -26.6% (-41.0 to -12.2) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 6 GAIN in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 4 EVEN, no difference beyond the noise (2 of 3 runs), 7 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
