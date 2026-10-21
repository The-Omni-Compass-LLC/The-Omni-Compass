# Kueue under the batch stream, the four ways: Omni-Compass on top of Kueue against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368387821 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368394823 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368401852 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -11.3% (-21.5 to -1.0) | -9.7% (-17.6 to -1.8) | -11.0% (-21.4 to -0.7) | **GAIN in all three of our runs** |
| node-hours | -11.5% (-21.5 to -1.4) | -9.7% (-17.8 to -1.6) | -11.1% (-21.4 to -0.8) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.5 to -0.0) | +0.1% (-0.2 to +0.4) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -8.1% (-15.1 to -1.1) | -6.6% (-12.2 to -1.0) | -7.7% (-14.8 to -0.5) | **GAIN in all three of our runs** |
| response time (ms), mean | -8.5% (-10.9 to -6.1) | -5.4% (-9.7 to -1.2) | -4.0% (-8.0 to +0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| response time (ms), 95th percentile | +9.5% (+1.9 to +17.1) | +13.4% (+3.4 to +23.4) | +15.4% (+7.8 to +22.9) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | +10.6% (-0.7 to +22.0) | +13.1% (+4.1 to +22.1) | +11.8% (+3.7 to +19.8) | EVEN, no difference beyond the noise (1 of 3 runs) |
| time over the response line (% of samples) | -2.4% (-6.5 to +1.7) | -2.0% (-4.7 to +0.7) | -0.0% (-3.4 to +3.3) | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | +0 (+0 to +0) | +0.009302 (-0.01174 to +0.03034) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +2.6% (-5.9 to +11.0) | +3.9% (-1.0 to +8.8) | +3.0% (-0.5 to +6.5) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +42 (+34.37 to +49.63) | +34.2 (+21.64 to +46.76) | +33.11 (+21.77 to +44.46) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.0% (-15.2 to +17.2) | -0.1% (-14.9 to +14.7) | +11.2% (-13.3 to +35.7) | shown, not judged |
| utilisation (used / allocatable) | +13.2% (+1.9 to +24.5) | +12.3% (+1.8 to +22.9) | +13.1% (+1.8 to +24.5) | shown, not judged |
| CPU used (cores), mean | -0.5% (-2.5 to +1.5) | +1.1% (-0.5 to +2.7) | -0.1% (-2.0 to +1.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01752 (+0.01459 to +0.02045) | +0.01711 (+0.01525 to +0.01897) | +0.01838 (+0.0172 to +0.01956) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.8% (-1.2 to +2.8) | +2.3% (+0.6 to +4.0) | +1.1% (-0.8 to +3.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -8.0% (-14.8 to -1.1) | -8.6% (-16.6 to -0.7) | -8.1% (-15.0 to -1.2) | shown, not judged |
| HPA replicas, mean | +3.4% (-3.6 to +10.4) | +5.9% (-1.8 to +13.6) | +1.5% (-9.0 to +12.0) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +0.1 (-0.1262 to +0.3262) | +0.2 (-0.1016 to +0.5016) | +0.5556 (-0.1223 to +1.233) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +0.1 (-0.1262 to +0.3262) | +0.3 (-0.1828 to +0.7828) | +1.222 (-0.3983 to +2.843) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +0.1 (-0.1262 to +0.3262) | +0.3 (-0.1828 to +0.7828) | +0.7222 (-0.1607 to +1.605) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +4.2% (+3.1 to +5.2) | +4.8% (+3.1 to +6.6) | +4.0% (+2.9 to +5.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +1.0% (+0.3 to +1.7) | +1.6% (+0.8 to +2.5) | +1.9% (+1.1 to +2.8) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -21.4% (-40.0 to -2.7) | -19.2% (-34.2 to -4.2) | -21.3% (-39.6 to -2.9) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +185.7% (-48.1 to +419.5) | +118.2% (+27.2 to +209.1) | +537.5% (+360.4 to +714.6) | EVEN, no difference beyond the noise (1 of 3 runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +100.0% (-15.2 to +215.2) | +0.0% (-42.1 to +42.1) | +800.0% (+569.4 to +1030.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job turnaround, submitted to done, mean (s) | +12.5% (+3.2 to +21.8) | +13.8% (+6.4 to +21.3) | +16.6% (+8.6 to +24.5) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 4 GAIN in all three of our runs, 3 LOSS in all three of our runs, 3 EVEN, no difference beyond the noise (1 of 3 runs), 2 EVEN, no difference beyond the noise (2 of 3 runs), 7 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
