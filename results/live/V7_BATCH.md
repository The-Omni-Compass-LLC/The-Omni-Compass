# Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38933427756 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38943582904 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38955582904 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -11.5% (-19.1 to -3.8) | -13.6% (-22.9 to -4.3) | -15.1% (-26.2 to -4.0) | **GAIN in all three of our runs** |
| node-hours | -11.5% (-19.1 to -3.9) | -13.6% (-22.7 to -4.6) | -15.2% (-26.3 to -4.2) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.3 to +0.5) | +0.0% (-0.3 to +0.4) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -7.8% (-13.2 to -2.5) | -9.4% (-15.5 to -3.3) | -10.5% (-18.1 to -2.8) | **GAIN in all three of our runs** |
| response time (ms), mean | -10.7% (-12.8 to -8.7) | -11.4% (-15.3 to -7.5) | -9.4% (-14.0 to -4.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +2.2% (-1.0 to +5.5) | -1.9% (-5.2 to +1.4) | +0.9% (-5.5 to +7.3) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +3.1% (-1.3 to +7.5) | -0.5% (-4.8 to +3.7) | +0.1% (-4.7 to +4.8) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -5.1% (-8.9 to -1.4) | -3.1% (-6.6 to +0.3) | -4.4% (-7.5 to -1.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | -100.0% (-250.8 to +50.8) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +11.6 (+11.1 to +12.1) | +12.6 (+11.58 to +13.62) | +11.6 (+10.52 to +12.68) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.3% (-1.5 to +2.1) | +0.5% (-1.6 to +2.6) | +1.1% (-1.8 to +4.0) | shown, not judged |
| utilisation (used / allocatable) | +13.6% (+5.7 to +21.4) | +14.4% (+2.7 to +26.2) | +18.6% (+4.7 to +32.4) | shown, not judged |
| CPU used (cores), mean | +0.1% (-1.6 to +1.8) | -1.3% (-4.3 to +1.6) | -0.0% (-1.4 to +1.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02086 (+0.01601 to +0.02571) | +0.02075 (+0.01721 to +0.02429) | +0.01905 (+0.01556 to +0.02254) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.4% (-0.3 to +3.2) | +0.1% (-2.9 to +3.1) | +1.3% (-0.1 to +2.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -8.3% (-13.5 to -3.1) | -9.1% (-17.0 to -1.2) | -11.7% (-20.7 to -2.6) | shown, not judged |
| HPA replicas, mean | -3.2% (-18.4 to +12.0) | +8.9% (-3.0 to +20.8) | +7.6% (-7.5 to +22.6) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +500.0% (-107.9 to +1107.9) | +0.5 (+0.123 to +0.877) | +300.0% (-45.5 to +645.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, total (s) | +47.9% (-352.1 to +448.0) | +0.6 (+0.09985 to +1.1) | -87.8% (-311.3 to +135.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, mean (s) | -19.8% (-307.8 to +268.2) | +0.6 (+0.09985 to +1.1) | -87.8% (-311.3 to +135.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy, the real machine under kind (%) | +1.4% (+0.6 to +2.1) | +1.9% (+1.1 to +2.7) | +2.3% (+0.9 to +3.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.1% (-0.6 to +0.8) | +0.7% (-0.2 to +1.6) | +1.2% (-0.5 to +2.8) | EVEN, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | -18.6% (-30.3 to -7.0) | -20.5% (-34.0 to -7.0) | -22.4% (-38.4 to -6.4) | **GAIN in all three of our runs** |

Readings: 5 GAIN in all three of our runs, 1 EVEN, no difference beyond the noise (1 of 3 runs), 3 EVEN, no difference beyond the noise (2 of 3 runs), 6 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
