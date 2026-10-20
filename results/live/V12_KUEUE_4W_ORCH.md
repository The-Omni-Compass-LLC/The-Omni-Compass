# Kueue under the batch stream, the four ways: Kueue as shipped against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368387821 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368394823 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368401852 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.2% (-0.6 to +0.1) | +0.1% (-0.2 to +0.5) | +0.1% (-0.2 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.6 to +0.1) | +0.1% (-0.4 to +0.6) | +0.1% (-0.2 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.3% (-0.6 to +0.1) | +0.1% (-0.4 to +0.6) | +0.1% (-0.2 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), mean | +7.3% (+0.0 to +14.5) | +6.4% (+1.8 to +11.0) | +8.9% (+3.7 to +14.1) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | +12.8% (+0.3 to +25.2) | +10.0% (+1.4 to +18.7) | +10.2% (+2.9 to +17.5) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | +13.2% (-1.3 to +27.7) | +7.0% (+0.4 to +13.6) | +11.1% (+5.0 to +17.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| time over the response line (% of samples) | +5.2% (-0.2 to +10.5) | +3.9% (-0.7 to +8.5) | +7.2% (+2.9 to +11.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0.0% (-6.1 to +6.1) | +1.0% (-6.0 to +8.0) | +1.0% (-1.3 to +3.3) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -0.5% (-14.5 to +13.5) | -6.7% (-20.7 to +7.4) | +5.5% (-13.3 to +24.4) | shown, not judged |
| utilisation (used / allocatable) | +0.6% (-1.4 to +2.6) | -0.3% (-1.9 to +1.2) | +0.1% (-1.7 to +1.9) | shown, not judged |
| CPU used (cores), mean | +0.6% (-1.4 to +2.6) | -0.3% (-1.9 to +1.2) | +0.1% (-1.7 to +1.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.6% (-1.4 to +2.6) | -0.3% (-1.9 to +1.2) | +0.1% (-1.7 to +1.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.3% (-2.6 to +2.1) | +0.7% (-1.4 to +2.8) | +0.2% (-1.9 to +2.4) | shown, not judged |
| HPA replicas, mean | +0.6% (-4.4 to +5.5) | +0.0% (-6.4 to +6.5) | +2.7% (-2.9 to +8.4) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +0.1 (-0.1262 to +0.3262) | +0.1 (-0.1262 to +0.3262) | +0.1111 (-0.1451 to +0.3673) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +0.4 (-0.5048 to +1.305) | +0.4 (-0.5048 to +1.305) | +0.3333 (-0.4353 to +1.102) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +0.4 (-0.5048 to +1.305) | +0.4 (-0.5048 to +1.305) | +0.3333 (-0.4353 to +1.102) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +2.4% (+1.1 to +3.7) | +1.8% (+1.2 to +2.4) | +1.1% (-1.1 to +3.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.9% (-0.1 to +1.9) | +1.1% (+0.3 to +1.8) | +1.4% (+0.6 to +2.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | +178.6% (+75.7 to +281.5) | +118.2% (+22.2 to +214.1) | +537.5% (+313.8 to +761.2) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +233.3% (+118.2 to +348.5) | +25.0% (-12.7 to +62.7) | +700.0% (+394.9 to +1005.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| queue: job turnaround, submitted to done, mean (s) | +11.5% (+0.3 to +22.7) | +9.3% (+2.0 to +16.5) | +12.7% (+5.4 to +19.9) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 4 LOSS in all three of our runs, 3 EVEN, no difference beyond the noise (1 of 3 runs), 1 EVEN, no difference beyond the noise (2 of 3 runs), 8 EVEN, no difference beyond the noise (all three runs), 6 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
