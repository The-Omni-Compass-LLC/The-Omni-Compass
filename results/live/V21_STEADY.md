# Steady load: the same fixed-rate work sent to both arms: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40223431219 | `433bcf30d2ad` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40246652453 | `22138ecd5b5a` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40269968227 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.5 to +0.2) | =0.1% (−0.0 to +0.2) | =0.2% (−0.5 to +0.9) | EVEN, under the floor (the three runs' mean 0.04%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.4% (−0.8 to +0.1) | =0.1% (−0.3 to −0.0) | =0.0% (−0.7 to +0.7) | EVEN, under the floor (the three runs' mean 0.18%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.4% (−0.8 to +0.1) | =0.1% (−0.3 to −0.0) | =0.0% (−0.7 to +0.7) | EVEN, under the floor (the three runs' mean 0.18%) |
| response time (ms), mean | +48.5% (+30.9 to +66.1) | +48.1% (+30.2 to +66.0) | +48.7% (+32.0 to +65.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +65.8% (+43.3 to +88.3) | +65.8% (+42.8 to +88.8) | +66.3% (+46.3 to +86.3) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +71.7% (+49.1 to +94.2) | +72.7% (+43.2 to +102.1) | +73.5% (+47.4 to +99.7) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +100.0% (+27.1 to +172.9) | +100.0% (+24.9 to +175.1) | +100.0% (+31.6 to +168.4) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+22.7 to +177.3) | +100.0% (+17.8 to +182.2) | +100.0% (+27.4 to +172.6) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +15.5000 (+12.8395 to +18.1605) | +15.0000 (+12.5452 to +17.4548) | +17.2000 (+14.5707 to +19.8293) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | −14.9% (−136.2 to +106.4) | +75.0% (−72.2 to +222.2) | ±0.0% (−292.0 to +292.0) | shown, not judged |
| utilisation (used / allocatable) | −4.2% (−7.2 to −1.2) | −4.2% (−6.0 to −2.4) | −4.1% (−7.2 to −1.1) | shown, not judged |
| CPU used (cores), mean | −4.2% (−7.2 to −1.2) | −4.2% (−6.0 to −2.4) | −4.1% (−7.2 to −1.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0079 (+0.0066 to +0.0092) | +0.0078 (+0.0066 to +0.0090) | +0.0081 (+0.0069 to +0.0093) | shown, not judged |
| CPU used with Omni's own (cores), mean | −3.3% (−6.2 to −0.5) | −3.3% (−5.1 to −1.5) | −3.3% (−6.2 to −0.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.7% (−0.5 to +5.8) | +3.9% (+2.1 to +5.7) | +2.4% (−0.8 to +5.5) | shown, not judged |
| HPA replicas, mean | +5.2% (−3.6 to +13.9) | +6.3% (−1.7 to +14.2) | +4.1% (−2.4 to +10.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +42.3% (+23.1 to +61.5) | +49.1% (+40.3 to +57.9) | +20.4% (+3.3 to +37.4) | **GAIN in all three of our runs** |
| pod start wait, total (s) | +53.6% (+28.7 to +78.4) | +47.9% (+28.8 to +67.1) | +19.5% (−2.7 to +41.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, mean (s) | +21.2% (+4.8 to +37.6) | =0.2% (−17.5 to +17.9) | +2.2% (−16.0 to +20.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | −3.4% (−6.2 to −0.5) | −3.3% (−4.6 to −1.9) | −2.9% (−5.9 to +0.2) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 4 EVEN, the same, 3 EVEN, under the floor, 3 GAIN by the mean of our three runs, 6 GAIN in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
