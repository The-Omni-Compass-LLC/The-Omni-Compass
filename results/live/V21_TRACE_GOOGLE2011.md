# A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40232036723 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40252903510 | `babd7a2ceac0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40275448206 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.1 to +0.2) | =0.1% (−0.3 to +0.0) | =0.0% (−0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.3% (−0.6 to −0.1) | =0.4% (−0.6 to −0.2) | =0.3% (−0.5 to −0.1) | EVEN, under the floor (the three runs' mean 0.36%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.3% (−0.6 to −0.1) | =0.4% (−0.6 to −0.2) | =0.3% (−0.5 to −0.1) | EVEN, under the floor (the three runs' mean 0.36%) |
| response time (ms), mean | +50.3% (+33.1 to +67.4) | +50.2% (+26.9 to +73.5) | +50.3% (+43.5 to +57.2) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +61.7% (+43.2 to +80.2) | +63.7% (+37.1 to +90.4) | +59.3% (+52.8 to +65.9) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +52.7% (+36.6 to +68.7) | +56.2% (+27.2 to +85.1) | +47.5% (+37.6 to +57.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +77.4% (+38.5 to +116.4) | +80.4% (+20.2 to +140.5) | +75.2% (+56.8 to +93.5) | **GAIN in all three of our runs** |
| failed requests (%) | +18.3% (+3.5 to +33.0) | +10.4% (−3.2 to +24.0) | +13.0% (+3.1 to +22.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +61.2% (+35.8 to +86.6) | +72.4% (+23.4 to +121.4) | +67.4% (+56.6 to +78.2) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +50.0000 (+35.6780 to +64.3220) | +43.9000 (+29.5010 to +58.2990) | +60.3000 (+44.0057 to +76.5943) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +69.9% (−33.6 to +173.5) | +46.3% (−12.9 to +105.6) | +169.2% (+11.3 to +327.2) | shown, not judged |
| utilisation (used / allocatable) | −4.0% (−5.1 to −2.9) | −3.3% (−4.4 to −2.1) | −3.2% (−3.9 to −2.5) | shown, not judged |
| CPU used (cores), mean | −4.0% (−5.1 to −2.9) | −3.3% (−4.4 to −2.1) | −3.2% (−3.9 to −2.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0090 (+0.0072 to +0.0108) | +0.0080 (+0.0062 to +0.0098) | +0.0101 (+0.0086 to +0.0115) | shown, not judged |
| CPU used with Omni's own (cores), mean | −3.5% (−4.5 to −2.4) | −2.8% (−3.9 to −1.7) | −2.7% (−3.4 to −2.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +3.4% (+2.4 to +4.5) | +3.0% (+1.8 to +4.2) | +3.1% (+2.1 to +4.1) | shown, not judged |
| HPA replicas, mean | +15.5% (−2.8 to +33.8) | +2.3% (−14.6 to +19.2) | +18.9% (+6.5 to +31.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +108.2% (+54.5 to +161.8) | +79.5% (+39.5 to +119.4) | +234.8% (+163.0 to +306.5) | **power given in all three of our runs** |
| pod start wait, total (s) | −109.0% (−31.2 to −186.8) | −87.9% (−13.7 to −162.0) | −279.2% (−180.7 to −377.8) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | +1.1% (−19.0 to +21.1) | −5.0% (−33.4 to +23.4) | −11.2% (−29.1 to +6.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | −2.9% (−3.8 to −2.0) | −1.8% (−2.9 to −0.8) | −2.2% (−2.8 to −1.6) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 1 LOSS in all three of our runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
