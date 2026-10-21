# Koordinator under the batch stream: Omni-Compass on top of its colocation (register row 89): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39359085965 | `28a65e160d68` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39359094679 | `28a65e160d68` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39359103518 | `28a65e160d68` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.9% (-2.3 to +0.5) | -0.4% (-1.1 to +0.4) | -0.1% (-0.2 to +0.0) | EVEN, no difference beyond the noise (all three runs) |
| node-hours | -0.8% (-2.4 to +0.7) | -0.6% (-1.5 to +0.4) | -0.3% (-0.7 to +0.1) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.3 to +0.4) | -0.2% (-0.8 to +0.4) | -0.3% (-0.7 to +0.1) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.5% (-1.7 to +0.6) | -0.5% (-1.2 to +0.3) | -0.3% (-0.8 to +0.1) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), mean | -37.1% (-45.8 to -28.4) | -36.0% (-43.9 to -28.2) | -37.1% (-44.9 to -29.3) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -23.7% (-29.2 to -18.2) | -22.1% (-24.8 to -19.3) | -24.9% (-29.2 to -20.6) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -8.3% (-13.7 to -2.8) | -9.5% (-12.5 to -6.5) | -15.0% (-23.2 to -6.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -35.9% (-144.5 to +72.7) | -32.2% (-124.8 to +60.5) | +26.9% (-172.5 to +226.3) | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +13.2 (+11.59 to +14.81) | +12.9 (+11.86 to +13.94) | +13.2 (+11.36 to +15.04) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -0.2% (-5.3 to +4.8) | +1.4% (-4.5 to +7.2) | +5.1% (-5.4 to +15.5) | shown, not judged |
| utilisation (used / allocatable) | +1.2% (-1.1 to +3.4) | -0.2% (-3.2 to +2.8) | -0.5% (-2.9 to +2.0) | shown, not judged |
| CPU used (cores), mean | +0.4% (-1.5 to +2.2) | -0.5% (-3.1 to +2.1) | -0.5% (-3.0 to +1.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01274 (+0.01182 to +0.01366) | +0.0131 (+0.01201 to +0.01419) | +0.01189 (+0.0108 to +0.01298) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.2% (-0.6 to +3.1) | +0.4% (-2.2 to +2.9) | +0.3% (-2.1 to +2.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -1.0% (-2.9 to +1.0) | +0.1% (-2.7 to +2.9) | +0.4% (-1.8 to +2.5) | shown, not judged |
| HPA replicas, mean | +4.0% (-5.8 to +13.9) | +3.8% (-7.7 to +15.2) | +0.2% (-5.6 to +6.1) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +400.0% (-203.2 to +1003.2) | +150.0% (-91.4 to +391.4) | +400.0% (-203.2 to +1003.2) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +300.0% (-264.2 to +864.2) | +300.0% (-45.5 to +645.5) | +350.0% (-304.1 to +1004.1) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +200.0% (-219.8 to +619.8) | +300.0% (-45.5 to +645.5) | +225.0% (-224.6 to +674.6) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +0.7% (-1.4 to +2.9) | +1.2% (-0.0 to +2.4) | +0.1% (-1.7 to +2.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | -1.3% (-3.4 to +0.7) | -1.4% (-4.2 to +1.3) | -1.2% (-5.6 to +3.2) | EVEN, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | -17.2% (-69.9 to +35.5) | -5.0% (-22.5 to +12.4) | -1.4% (-4.4 to +1.6) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, mean (s) | -4.7% (-25.0 to +15.6) | -7.5% (-36.1 to +21.0) | -12.6% (-29.8 to +4.6) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +3.7% (-26.5 to +33.9) | -3.7% (-23.9 to +16.4) | -15.3% (-43.3 to +12.8) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | -3.1% (-8.7 to +2.4) | +0.7% (-5.6 to +6.9) | +5.5% (-2.9 to +14.0) | EVEN, no difference beyond the noise (all three runs) |
| queue: jobs unfinished at the window's end | -1.9% (-13.4 to +9.6) | +4.0% (-30.4 to +38.4) | +36.0% (-6.5 to +78.5) | EVEN, no difference beyond the noise (all three runs) |

Readings: 3 GAIN in all three of our runs, 15 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
