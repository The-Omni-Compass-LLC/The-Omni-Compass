# The KAI scheduler under the batch stream, the four ways: KAI as shipped against the organism alone (register row 91): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368344021 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368351097 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368358521 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.0% (-0.3 to +0.4) | +0.1% (-0.1 to +0.4) | -0.1% (-0.5 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.0% (-0.3 to +0.4) | +0.2% (-0.0 to +0.4) | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.0% (-0.3 to +0.4) | +0.2% (-0.0 to +0.4) | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), mean | +13.2% (+1.6 to +24.8) | +15.8% (+8.1 to +23.5) | +18.3% (+7.5 to +29.1) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | +38.1% (+7.2 to +69.0) | +41.1% (+19.5 to +62.6) | +50.8% (+22.6 to +79.0) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | +39.9% (+7.8 to +72.1) | +44.0% (+23.2 to +64.9) | +61.3% (+30.8 to +91.7) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | -18.7% (-30.5 to -6.9) | -7.5% (-23.7 to +8.7) | -14.4% (-26.2 to -2.6) | EVEN, no difference beyond the noise (1 of 3 runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +1.2% (-11.5 to +13.8) | +6.9% (+4.3 to +9.5) | +6.4% (+2.0 to +10.9) | EVEN, no difference beyond the noise (1 of 3 runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +104.5% (+52.4 to +156.5) | +89.9% (+38.8 to +141.0) | +57.8% (+38.7 to +76.8) | shown, not judged |
| utilisation (used / allocatable) | +0.1% (-2.0 to +2.1) | +0.8% (-0.7 to +2.4) | +0.3% (-1.6 to +2.1) | shown, not judged |
| CPU used (cores), mean | +0.1% (-2.0 to +2.1) | +0.8% (-0.7 to +2.4) | +0.3% (-1.6 to +2.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.1% (-2.0 to +2.1) | +0.8% (-0.7 to +2.4) | +0.3% (-1.6 to +2.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.6% (-1.7 to +2.8) | -0.6% (-2.3 to +1.2) | -0.0% (-1.9 to +1.8) | shown, not judged |
| HPA replicas, mean | +2.4% (-3.7 to +8.4) | +5.2% (-1.6 to +12.0) | -5.2% (-17.0 to +6.5) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +0.0% (-337.2 to +337.2) | +0.2 (-0.2524 to +0.6524) | +0.3 (-0.1828 to +0.7828) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -25.0% (-322.4 to +272.4) | +0.3 (-0.3786 to +0.9786) | +0.6 (-0.3656 to +1.566) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -25.0% (-322.4 to +272.4) | +0.15 (-0.1893 to +0.4893) | +0.4 (-0.2032 to +1.003) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +6.4% (+4.8 to +7.9) | +6.9% (+5.3 to +8.5) | +5.6% (+4.6 to +6.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +4.2% (+1.6 to +6.9) | +5.7% (+2.8 to +8.6) | +4.6% (+2.7 to +6.4) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | +1461.5% (+1162.4 to +1760.7) | +1613.3% (+1157.7 to +2069.0) | +968.4% (+828.5 to +1108.4) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +300.0% (+115.3 to +484.7) | +550.0% (+225.7 to +874.3) | +100.0% (+31.0 to +169.0) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +40.1% (+16.1 to +64.0) | +42.1% (+24.1 to +60.0) | +45.2% (+26.8 to +63.6) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 7 LOSS in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 7 EVEN, no difference beyond the noise (all three runs), 6 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
