# Kueue under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368387821 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368394823 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368401852 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -14.5% (-25.2 to -3.9) | -9.8% (-16.0 to -3.5) | -13.8% (-23.7 to -3.9) | **GAIN in all three of our runs** |
| node-hours | -14.6% (-25.1 to -4.0) | -9.5% (-15.8 to -3.3) | -13.9% (-23.7 to -4.1) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.3 to +0.2) | +0.3% (+0.0 to +0.7) | -0.2% (-0.4 to +0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -10.2% (-17.5 to -2.8) | -6.4% (-10.7 to -2.1) | -9.7% (-16.5 to -2.8) | **GAIN in all three of our runs** |
| response time (ms), mean | -11.4% (-14.7 to -8.2) | -12.5% (-15.5 to -9.4) | -10.1% (-16.0 to -4.3) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +3.8% (-2.2 to +9.8) | +1.6% (-5.0 to +8.2) | +4.4% (-5.1 to +13.8) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +10.1% (-1.7 to +22.0) | -1.9% (-8.1 to +4.4) | +3.3% (-4.9 to +11.5) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -6.1% (-12.9 to +0.6) | -5.3% (-8.4 to -2.2) | -4.5% (-10.0 to +1.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -1.3% (-6.5 to +3.9) | +1.0% (-1.2 to +3.2) | +0.0% (-3.5 to +3.5) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +46.1 (+34.95 to +57.25) | +39.9 (+29.63 to +50.17) | +41.89 (+29.46 to +54.32) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +15.3% (-5.4 to +35.9) | -15.9% (-24.9 to -6.9) | +0.1% (-23.4 to +23.6) | shown, not judged |
| utilisation (used / allocatable) | +16.7% (+4.8 to +28.5) | +11.0% (+5.1 to +17.0) | +15.7% (+5.3 to +26.1) | shown, not judged |
| CPU used (cores), mean | -0.7% (-2.7 to +1.2) | +0.1% (-1.2 to +1.4) | -0.8% (-3.8 to +2.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01696 (+0.01582 to +0.0181) | +0.01666 (+0.01502 to +0.0183) | +0.01814 (+0.01706 to +0.01923) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.5% (-1.5 to +2.4) | +1.3% (+0.0 to +2.5) | +0.4% (-2.7 to +3.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.3% (-17.4 to -3.3) | -7.2% (-11.7 to -2.7) | -9.3% (-15.5 to -3.2) | shown, not judged |
| HPA replicas, mean | +0.8% (-6.8 to +8.4) | -0.9% (-6.5 to +4.7) | -2.0% (-10.3 to +6.3) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +0.1 (-0.1262 to +0.3262) | +0.1 (-0.1262 to +0.3262) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +0 (+0 to +0) | +0.3 (-0.3786 to +0.9786) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +0 (+0 to +0) | +0.3 (-0.3786 to +0.9786) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +2.5% (+1.4 to +3.6) | +1.7% (+1.1 to +2.3) | +1.5% (-0.7 to +3.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.5% (-0.1 to +1.0) | +0.3% (-0.2 to +0.8) | +0.6% (-0.4 to +1.6) | EVEN, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | -27.0% (-46.1 to -7.9) | -19.7% (-31.7 to -7.6) | -26.2% (-41.8 to -10.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -28.6% (-101.6 to +44.5) | -40.9% (-99.2 to +17.4) | -25.0% (-97.1 to +47.1) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +0.0% (-159.0 to +159.0) | -62.5% (-109.6 to -15.4) | -100.0% (-330.6 to +130.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job turnaround, submitted to done, mean (s) | +8.2% (+0.2 to +16.1) | +3.3% (-1.2 to +7.8) | +5.3% (-2.3 to +12.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN in all three of our runs, 4 EVEN, no difference beyond the noise (2 of 3 runs), 9 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
