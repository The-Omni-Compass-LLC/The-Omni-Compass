# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: The bin-packing profile as shipped against the organism alone (register row 88): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368428763 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368435483 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368442002 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.1% (-0.1 to +0.3) | -0.0% (-0.3 to +0.2) | -0.1% (-0.4 to +0.1) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.2 to +0.3) | +0.1% (-0.3 to +0.5) | -0.1% (-0.4 to +0.2) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.1% (-0.2 to +0.3) | +0.1% (-0.3 to +0.5) | -0.1% (-0.4 to +0.2) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), mean | -4.4% (-10.2 to +1.4) | -5.6% (-10.0 to -1.1) | -8.2% (-15.2 to -1.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| response time (ms), 95th percentile | +13.5% (+1.0 to +26.0) | +4.9% (-8.4 to +18.1) | -0.6% (-10.4 to +9.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), 99th percentile | +13.8% (-0.5 to +28.2) | +14.7% (-3.2 to +32.7) | +9.9% (-7.4 to +27.3) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -21.0% (-35.1 to -6.9) | -28.1% (-50.9 to -5.3) | -26.5% (-48.6 to -4.3) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -0.9% (-8.2 to +6.4) | -13.0% (-28.8 to +2.8) | -4.8% (-10.8 to +1.2) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +8.1% (-11.8 to +27.9) | +22.9% (+6.0 to +39.9) | +3.6% (-10.8 to +17.9) | shown, not judged |
| utilisation (used / allocatable) | -1.0% (-2.6 to +0.6) | +0.5% (-3.4 to +4.4) | -0.5% (-2.1 to +1.2) | shown, not judged |
| CPU used (cores), mean | -1.0% (-2.6 to +0.6) | +0.5% (-3.4 to +4.4) | -0.5% (-2.1 to +1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.0% (-2.6 to +0.6) | +0.5% (-3.4 to +4.4) | -0.5% (-2.1 to +1.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.2% (-0.6 to +3.0) | -2.2% (-9.3 to +4.9) | +0.5% (-1.1 to +2.1) | shown, not judged |
| HPA replicas, mean | +5.6% (-1.2 to +12.4) | +0.2% (-3.7 to +4.1) | +3.0% (-2.8 to +8.9) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +100.0% (-427.8 to +627.8) | +0.3 (-0.1828 to +0.7828) | -100.0% (-250.8 to +50.8) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +66.7% (-394.0 to +527.4) | +0.5 (-0.2726 to +1.273) | -100.0% (-252.7 to +52.7) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -16.7% (-326.8 to +293.5) | +0.4 (-0.2911 to +1.091) | -100.0% (-252.7 to +52.7) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -0.1% (-0.8 to +0.6) | +0.1% (-0.6 to +0.8) | -0.7% (-1.5 to +0.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.2% (-0.7 to +1.0) | -0.2% (-0.5 to +0.2) | -0.3% (-1.1 to +0.5) | EVEN, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | -27.8% (-74.6 to +19.1) | +33.3% (-56.4 to +123.1) | +90.0% (-8.0 to +188.0) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -50.0% (-107.6 to +7.6) | +33.3% (-102.0 to +168.7) | +200.0% (+15.3 to +384.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job turnaround, submitted to done, mean (s) | +3.7% (-2.2 to +9.6) | +0.3% (-3.1 to +3.7) | -0.7% (-7.4 to +6.0) | EVEN, no difference beyond the noise (all three runs) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 1 GAIN in all three of our runs, 1 EVEN, no difference beyond the noise (1 of 3 runs), 2 EVEN, no difference beyond the noise (2 of 3 runs), 12 EVEN, no difference beyond the noise (all three runs), 6 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
