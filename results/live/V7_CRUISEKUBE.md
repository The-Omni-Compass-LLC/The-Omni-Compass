# CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38843284578 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38843287341 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38843289946 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.5% (-0.7 to +1.7) | -0.7% (-2.2 to +0.9) | EVEN, no difference beyond the noise (all three runs) |
| node-hours | +0.2% (-0.5 to +0.8) | +1.0% (+0.2 to +1.8) | -0.1% (-1.6 to +1.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.2% (-0.4 to +0.9) | +0.1% (-1.2 to +1.3) | +1.2% (-0.1 to +2.4) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.2% (-0.4 to +0.9) | +0.4% (-0.1 to +0.9) | +0.7% (+0.2 to +1.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| response time (ms), mean | +1.5% (-0.2 to +3.1) | +0.1% (-1.6 to +1.7) | +0.8% (-1.0 to +2.5) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 95th percentile | +0.3% (-1.1 to +1.8) | -0.1% (-2.3 to +2.2) | -0.1% (-1.7 to +1.5) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +3.1% (+0.6 to +5.7) | +0.0% (-4.1 to +4.2) | -0.1% (-4.7 to +4.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| time over the response line (% of samples) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +2.1% (-156.9 to +161.1) | -57.8% (-178.1 to +62.6) | -80.2% (-152.5 to -8.0) | shown, not judged |
| utilisation (used / allocatable) | +0.9% (-0.6 to +2.3) | -0.7% (-2.3 to +0.8) | +1.1% (-0.5 to +2.6) | shown, not judged |
| CPU used (cores), mean | +0.9% (-0.6 to +2.3) | -0.1% (-1.8 to +1.5) | +0.4% (-1.1 to +1.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00953 (+0.008894 to +0.01017) | +0.00853 (+0.007232 to +0.009828) | +0.00964 (+0.008849 to +0.01043) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.6% (+0.2 to +3.1) | +0.6% (-1.0 to +2.3) | +1.2% (-0.3 to +2.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.7% (-2.0 to +0.6) | +0.3% (-1.0 to +1.5) | -0.2% (-1.5 to +1.1) | shown, not judged |
| HPA replicas, mean | +3.2% (-9.1 to +15.5) | +0.7% (-6.5 to +7.9) | +1.9% (-6.7 to +10.4) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +45.5% (-37.1 to +128.0) | -18.8% (-66.1 to +28.6) | -7.7% (-38.9 to +23.5) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +117.6% (-83.9 to +319.2) | -8.3% (-88.3 to +71.6) | -15.9% (-108.5 to +76.7) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +120.9% (-37.5 to +279.2) | +24.7% (-68.6 to +118.0) | -14.0% (-82.2 to +54.1) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +2.0% (+0.8 to +3.3) | +0.2% (-1.4 to +1.8) | +1.6% (+0.5 to +2.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, no difference beyond the noise (2 of 3 runs), 8 EVEN, no difference beyond the noise (all three runs), 5 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
