# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39173411511 | `8de24035ac07` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| B | 39176842679 | `2a2cfc67147e` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| C | 39180252225 | `7b7dd69870e7` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| node-hours | -0.4% (-0.9 to +0.1) | +0.3% (-0.3 to +0.9) | -0.4% (-0.7 to -0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.1% (+0.3 to +1.8) | +1.8% (+1.1 to +2.6) | +1.1% (+0.6 to +1.7) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.1% (+0.3 to +1.8) | +1.8% (+1.1 to +2.6) | +1.1% (+0.6 to +1.7) | **power given in all three of our runs** |
| response time (ms), mean | -35.6% (-48.7 to -22.5) | -37.1% (-49.1 to -25.0) | -37.5% (-47.6 to -27.3) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -51.7% (-63.2 to -40.1) | -53.3% (-64.9 to -41.6) | -53.2% (-64.2 to -42.2) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -58.4% (-71.4 to -45.4) | -60.6% (-70.8 to -50.4) | -57.1% (-66.2 to -48.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-180.9 to -19.1) | -96.9% (-175.6 to -18.1) | -100.0% (-179.2 to -20.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | -100.0% (-326.2 to +126.2) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +18 (+17.17 to +18.83) | +18 (+17.11 to +18.89) | +17.7 (+16.94 to +18.46) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +36.2% (-95.4 to +167.9) | -63.2% (-173.2 to +46.8) | +196.9% (-144.6 to +538.3) | shown, not judged |
| utilisation (used / allocatable) | +27.8% (+18.7 to +37.0) | +28.8% (+20.1 to +37.5) | +29.9% (+22.9 to +36.9) | shown, not judged |
| CPU used (cores), mean | +27.8% (+18.7 to +37.0) | +28.8% (+20.1 to +37.5) | +29.9% (+22.9 to +36.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01129 (+0.00977 to +0.01281) | +0.01166 (+0.01007 to +0.01325) | +0.01196 (+0.01064 to +0.01328) | shown, not judged |
| CPU used with Omni's own (cores), mean | +29.2% (+19.9 to +38.5) | +30.2% (+21.3 to +39.0) | +31.3% (+24.1 to +38.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -19.4% (-23.7 to -15.1) | -20.1% (-24.5 to -15.7) | -21.0% (-24.2 to -17.8) | shown, not judged |
| HPA replicas, mean | +1.8% (+0.5 to +3.1) | +2.6% (+1.5 to +3.8) | +3.1% (+1.9 to +4.2) | **power given in all three of our runs** |
| pods started | +6.2% (-3.8 to +16.3) | +0.0% (-14.0 to +14.0) | -9.6% (-24.5 to +5.2) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +11.9% (-20.5 to +44.2) | -22.1% (-44.8 to +0.6) | -2.7% (-24.8 to +19.3) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +6.8% (-21.8 to +35.5) | -21.3% (-38.0 to -4.5) | +4.3% (-14.0 to +22.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy, the real machine under kind (%) | +26.6% (+17.7 to +35.5) | +27.8% (+20.2 to +35.3) | +29.9% (+23.4 to +36.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 3 power given in all three of our runs, 2 EVEN, no difference beyond the noise (2 of 3 runs), 4 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
