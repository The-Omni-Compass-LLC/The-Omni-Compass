# Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40240618830 | `4a294bb71d0f` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40261931876 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40286252440 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.4 to +0.4) | =0.1% (−0.2 to +0.3) | =0.2% (+0.0 to +0.3) | EVEN, under the floor (the three runs' mean 0.09%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.6 to +0.3) | =0.2% (−0.5 to +0.1) | =0.0% (−0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.14%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.2% (−0.6 to +0.3) | =0.2% (−0.5 to +0.1) | =0.0% (−0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.14%) |
| response time (ms), mean | +35.6% (+20.1 to +51.1) | +39.5% (+16.2 to +62.9) | +30.3% (+18.6 to +42.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +38.9% (+17.8 to +60.1) | +48.3% (+9.6 to +87.0) | +27.6% (+17.3 to +37.8) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | −6.2% (−45.0 to +32.6) | +17.7% (−24.8 to +60.2) | +5.6% (−34.8 to +46.0) | **the runs disagree** |
| time over the response line (% of samples) | +32.9% (+19.8 to +45.9) | +34.2% (+21.3 to +47.1) | +34.6% (+14.7 to +54.6) | **GAIN in all three of our runs** |
| failed requests (%) | +12.4% (+7.6 to +17.2) | +9.4% (+3.2 to +15.7) | +12.8% (−1.6 to +27.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +17.9% (+13.3 to +22.5) | +19.5% (+13.7 to +25.3) | +25.3% (+12.2 to +38.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +42.7000 (+36.4636 to +48.9364) | +48.0000 (+37.5959 to +58.4041) | +51.9000 (+44.5707 to +59.2293) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +112.9% (−189.6 to +415.4) | +103.1% (−81.8 to +288.1) | +68.8% (−84.2 to +221.7) | shown, not judged |
| utilisation (used / allocatable) | −1.6% (−2.4 to −0.8) | −1.9% (−2.7 to −1.1) | −1.6% (−2.3 to −1.0) | shown, not judged |
| CPU used (cores), mean | −1.6% (−2.4 to −0.8) | −1.9% (−2.7 to −1.1) | −1.6% (−2.3 to −1.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0130 (+0.0113 to +0.0147) | +0.0128 (+0.0115 to +0.0140) | +0.0135 (+0.0115 to +0.0154) | shown, not judged |
| CPU used with Omni's own (cores), mean | −1.1% (−1.9 to −0.4) | −1.4% (−2.2 to −0.6) | −1.0% (−1.7 to −0.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.0% (−0.3 to +2.2) | +1.5% (+0.5 to +2.5) | +1.5% (+0.9 to +2.1) | shown, not judged |
| HPA replicas, mean | +2.3% (−0.8 to +5.4) | +7.3% (+2.4 to +12.2) | +6.5% (+2.2 to +10.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +7.7% (−29.1 to +44.5) | +13.7% (−51.1 to +78.5) | +46.7% (+10.3 to +83.0) | **the runs disagree** |
| pod start wait, total (s) | −10.1% (−57.3 to +37.0) | −24.4% (−111.9 to +63.1) | −78.6% (−16.2 to −140.9) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −16.1% (−43.4 to +11.2) | +1.0% (−23.1 to +25.1) | −19.9% (−47.0 to +7.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | −0.6% (−1.1 to −0.1) | −0.6% (−1.3 to +0.1) | −0.4% (−0.9 to −0.0) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |
| robust: failed requests in the 300 s after the kill (%) | +4.0% (−5.6 to +13.6) | +4.3% (−5.9 to +14.6) | +3.7% (−3.4 to +10.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| robust: time over the line in the 300 s after the kill (% of samples) | =0.5% (−2.2 to +1.2) | +2.6% (−1.2 to +6.4) | +0.7% (−2.9 to +4.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| robust: every setting back at the operator's within 60 s of the kill, every repetition (the governor killed outright; the watchdog's hand-back) | yes (10 reps; mean 9 s, max 10 s) | yes (10 reps; mean 9 s, max 11 s) | yes (10 reps; mean 8 s, max 10 s) | **handed back within the allowance in every repetition, in all three of our runs** |
| robust: a second governor started after the hand-back and governed to the end, every repetition | yes | yes | yes | **the same in all three of our runs** |

Readings: 1 handed back within the allowance in every repetition, in all three of our runs, 1 the same in all three of our runs, 3 EVEN, the same, 3 EVEN, under the floor, 3 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
