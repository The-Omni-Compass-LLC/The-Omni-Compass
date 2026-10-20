# Volcano under the batch stream, the four ways: Omni-Compass on the organism alone against Volcano as shipped (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the orchestrator as shipped: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -14.6% (-21.6 to -7.6) | -19.2% (-31.0 to -7.4) | -11.8% (-23.7 to +0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| node-hours | -14.5% (-21.5 to -7.5) | -19.1% (-30.9 to -7.3) | -11.6% (-23.3 to +0.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.2 to +0.5) | -0.0% (-0.4 to +0.3) | +0.3% (+0.0 to +0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -10.0% (-14.8 to -5.1) | -13.3% (-21.5 to -5.1) | -7.9% (-16.0 to +0.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| response time (ms), mean | +20.0% (+0.7 to +39.3) | +11.4% (-6.3 to +29.2) | +13.1% (-1.5 to +27.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), 95th percentile | +92.6% (+46.7 to +138.5) | +31.9% (+10.8 to +53.0) | +50.9% (+23.2 to +78.6) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | +73.3% (+31.5 to +115.1) | +9.6% (-8.3 to +27.4) | +23.6% (+1.1 to +46.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| time over the response line (% of samples) | +124.1% (+51.4 to +196.7) | +50.2% (+5.7 to +94.8) | +54.8% (+19.1 to +90.4) | **LOSS in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +30.3% (+6.8 to +53.8) | +11.3% (-3.6 to +26.1) | +23.2% (-1.8 to +48.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +40.2 (+31.7 to +48.7) | +55.7 (+35.95 to +75.45) | +49.7 (+37.2 to +62.2) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -23.2% (-41.4 to -4.9) | -34.3% (-51.1 to -17.4) | -30.8% (-43.6 to -18.0) | shown, not judged |
| utilisation (used / allocatable) | +17.1% (+8.6 to +25.7) | +22.1% (+6.3 to +37.9) | +13.8% (-0.7 to +28.3) | shown, not judged |
| CPU used (cores), mean | -0.4% (-1.5 to +0.7) | -2.7% (-5.0 to -0.3) | -0.8% (-2.7 to +1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01732 (+0.01601 to +0.01863) | +0.01773 (+0.01636 to +0.0191) | +0.01698 (+0.0147 to +0.01926) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.9% (-0.3 to +2.0) | -1.5% (-3.8 to +0.9) | +0.4% (-1.6 to +2.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.0% (-15.8 to -4.3) | -12.0% (-21.2 to -2.8) | -8.6% (-17.7 to +0.4) | shown, not judged |
| HPA replicas, mean | -2.2% (-12.2 to +7.8) | +6.0% (-5.7 to +17.7) | -2.8% (-9.1 to +3.5) | EVEN, no difference beyond the noise (all three runs) |
| pods started | -100.0% (-326.2 to +126.2) | +100.0% (-427.8 to +627.8) | +0.1 (-0.1262 to +0.3262) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -100.0% (-326.2 to +126.2) | +200.0% (-538.8 to +938.8) | +0.2 (-0.2524 to +0.6524) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -100.0% (-326.2 to +126.2) | +50.0% (-378.2 to +478.2) | +0.2 (-0.2524 to +0.6524) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -0.1% (-0.7 to +0.6) | -1.0% (-1.5 to -0.4) | -0.4% (-1.3 to +0.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | -0.7% (-1.2 to -0.3) | -1.2% (-2.2 to -0.1) | -0.8% (-1.5 to -0.2) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -29.0% (-42.4 to -15.7) | -33.8% (-51.4 to -16.2) | -20.5% (-40.2 to -0.9) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -92.5% (-105.6 to -79.4) | -90.8% (-110.6 to -71.0) | -92.7% (-113.6 to -71.8) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -78.6% (-107.6 to -49.6) | -66.7% (-121.7 to -11.6) | -58.3% (-87.1 to -29.5) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | -13.6% (-21.2 to -6.1) | -13.7% (-23.7 to -3.7) | -11.5% (-19.1 to -4.0) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN in all three of our runs, 2 LOSS in all three of our runs, 4 EVEN, no difference beyond the noise (1 of 3 runs), 3 EVEN, no difference beyond the noise (2 of 3 runs), 4 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
