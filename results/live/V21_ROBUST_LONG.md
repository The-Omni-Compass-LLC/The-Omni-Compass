# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40240697625 | `4a294bb71d0f` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| B | 40261936964 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| C | 40286258686 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.2 to +0.3) | =0.0% (−0.2 to +0.1) | =0.0% (−0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.01%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.6 to +0.2) | =0.2% (−0.7 to +0.3) | =0.2% (−0.5 to +0.0) | EVEN, under the floor (the three runs' mean 0.20%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.2% (−0.6 to +0.2) | =0.2% (−0.7 to +0.3) | =0.2% (−0.5 to +0.0) | EVEN, under the floor (the three runs' mean 0.20%) |
| response time (ms), mean | +43.2% (−41.8 to +128.3) | +28.9% (−8.5 to +66.3) | +39.9% (−24.8 to +104.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 95th percentile | +56.6% (−64.3 to +177.5) | +25.0% (−45.3 to +95.3) | +40.7% (−9.6 to +90.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 99th percentile | +24.7% (−31.2 to +80.7) | −6.8% (−84.0 to +70.4) | +11.1% (−0.7 to +23.0) | **the runs disagree** |
| time over the response line (% of samples) | +41.3% (−47.8 to +130.5) | +30.1% (−2.5 to +62.7) | +40.5% (−38.2 to +119.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | +14.5% (−37.6 to +66.7) | +9.5% (−7.2 to +26.2) | +12.6% (−29.6 to +54.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +25.5% (−24.9 to +75.9) | +21.2% (+1.3 to +41.1) | +28.0% (−17.6 to +73.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +130.6667 (+90.4286 to +170.9048) | +150.0000 (−37.2176 to +337.2176) | +176.3333 (−6.4021 to +359.0688) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +26.1% (−14.7 to +67.0) | +42.7% (−95.9 to +181.2) | −24.0% (−208.0 to +160.0) | shown, not judged |
| utilisation (used / allocatable) | −2.0% (−4.2 to +0.2) | −1.2% (−4.6 to +2.3) | −1.9% (−3.8 to −0.1) | shown, not judged |
| CPU used (cores), mean | −2.0% (−4.2 to +0.2) | −1.2% (−4.6 to +2.3) | −1.9% (−3.8 to −0.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0087 (+0.0031 to +0.0143) | +0.0111 (+0.0099 to +0.0124) | +0.0094 (+0.0055 to +0.0133) | shown, not judged |
| CPU used with Omni's own (cores), mean | −1.6% (−3.6 to +0.4) | −0.8% (−4.2 to +2.7) | −1.5% (−3.5 to +0.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.7% (+0.1 to +3.4) | +1.3% (−2.6 to +5.3) | +2.6% (−4.2 to +9.5) | shown, not judged |
| HPA replicas, mean | +28.6% (−75.7 to +132.9) | +50.1% (+42.5 to +57.7) | +34.7% (−41.0 to +110.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +68.2% (+9.5 to +126.9) | +162.5% (−297.1 to +622.1) | +226.3% (−185.7 to +638.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −90.0% (−198.3 to +18.3) | −221.7% (−761.1 to +317.6) | −324.0% (−892.8 to +244.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | −24.5% (−118.6 to +69.7) | −27.0% (−154.0 to +100.1) | −25.6% (−83.7 to +32.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | −0.9% (−1.5 to −0.4) | −0.1% (−2.6 to +2.5) | −0.7% (−3.2 to +1.8) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.035 | 1.026 | 1.039 | no leak (every repetition under 1.25) |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 100.0% | 100.0% | 100.0% | valid (every repetition at 95% of the expected or more) |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 0 | 0 | 0 | none in any repetition |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 1.23 | 1.26 | 1.12 | no growth beyond the limit (every repetition under 1.5) |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **every setting handed back at the end of every repetition, in all three of our runs** |

Readings: 1 every setting handed back at the end of every repetition, in all three of our runs, 3 EVEN, the same, 3 EVEN, under the floor, 5 GAIN by the mean of our three runs, 2 LOSS by the mean of our three runs, 1 no growth beyond the limit (every repetition under 1.5), 1 no leak (every repetition under 1.25), 1 none in any repetition, 2 power given by the mean of our three runs, 9 shown, not judged, 1 the runs disagree, 1 valid (every repetition at 95% of the expected or more).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
