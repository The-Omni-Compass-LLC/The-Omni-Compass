# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40229598467 | `277a6f3e33c0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40250391552 | `ddc44f445d06` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40272639170 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.1% (−0.2 to +0.0) | =0.0% (−0.1 to +0.1) | =0.0% (−0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| node-hours | +0.8% (+0.3 to +1.4) | =0.3% (−0.8 to +0.2) | =0.2% (−0.7 to +0.3) | EVEN, under the floor (the three runs' mean 0.46%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.0% (+0.3 to +1.6) | =0.4% (−0.9 to +0.1) | =0.3% (−0.8 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.0% (+0.4 to +1.7) | =0.4% (−0.9 to +0.1) | =0.3% (−0.8 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), mean | +48.5% (+32.5 to +64.4) | +37.7% (+14.3 to +61.1) | +48.4% (+23.4 to +73.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +51.0% (+39.3 to +62.6) | +57.8% (+47.9 to +67.6) | +54.5% (+35.9 to +73.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +59.5% (+10.9 to +108.2) | +20.5% (−38.3 to +79.3) | +60.0% (+17.0 to +103.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | +33.6% (+23.4 to +43.9) | +28.3% (+13.6 to +43.0) | +34.3% (+18.3 to +50.3) | **GAIN in all three of our runs** |
| failed requests (%) | +18.2% (+9.1 to +27.2) | +14.3% (−0.8 to +29.5) | +10.7% (+0.9 to +20.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +22.4% (+10.9 to +33.9) | +22.1% (+5.7 to +38.5) | +14.3% (+1.1 to +27.5) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +29.9000 (+25.2957 to +34.5043) | +27.9000 (+25.1513 to +30.6487) | +25.9000 (+20.2631 to +31.5369) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +213.6% (+56.0 to +371.3) | +83.9% (−100.6 to +268.3) | +75.7% (−88.8 to +240.2) | shown, not judged |
| utilisation (used / allocatable) | −2.2% (−5.8 to +1.4) | −1.4% (−5.3 to +2.4) | −1.1% (−2.8 to +0.6) | shown, not judged |
| CPU used (cores), mean | −2.3% (−5.9 to +1.3) | −1.5% (−5.3 to +2.4) | −1.1% (−2.8 to +0.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0099 (+0.0081 to +0.0117) | +0.0103 (+0.0089 to +0.0118) | +0.0086 (+0.0067 to +0.0104) | shown, not judged |
| CPU used with Omni's own (cores), mean | −1.7% (−5.2 to +1.8) | −0.9% (−4.7 to +2.9) | −0.5% (−2.2 to +1.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.7% (−2.8 to +4.3) | +0.6% (−2.6 to +3.8) | +1.2% (−0.1 to +2.6) | shown, not judged |
| HPA replicas, mean | +20.3% (+6.7 to +34.0) | +9.8% (−1.7 to +21.2) | +12.5% (−4.8 to +29.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +21.8% (−4.8 to +48.4) | +11.8% (−3.3 to +26.8) | +17.5% (+0.8 to +34.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −22.5% (−189.1 to +144.1) | −23.9% (−205.8 to +158.1) | +48.8% (−53.8 to +151.5) | **the runs disagree** |
| pod start wait, mean (s) | +5.4% (−144.3 to +155.0) | −9.1% (−180.9 to +162.7) | +50.2% (−43.3 to +143.8) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | −0.9% (−3.3 to +1.5) | −1.0% (−3.9 to +1.9) | −0.4% (−1.9 to +1.1) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 2 EVEN, the same, 2 EVEN, under the floor, 4 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 2 power given by the mean of our three runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
