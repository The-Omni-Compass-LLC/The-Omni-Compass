# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40222183655 | `f0c1c431231c` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40245490699 | `22138ecd5b5a` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40267231266 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.3% (−0.8 to +0.2) | =0.2% (−0.8 to +0.3) | +0.6% (+0.0 to +1.3) | EVEN, under the floor (the three runs' mean 0.39%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.8% (+1.3 to +2.4) | +1.5% (+0.9 to +2.0) | +1.7% (+1.0 to +2.4) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.8% (+1.3 to +2.4) | +1.5% (+0.9 to +2.0) | +1.7% (+1.0 to +2.4) | **power given in all three of our runs** |
| response time (ms), mean | +45.4% (+31.9 to +58.9) | +44.9% (+30.1 to +59.8) | +47.1% (+39.8 to +54.3) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +59.2% (+46.6 to +71.8) | +60.7% (+48.0 to +73.5) | +59.2% (+52.3 to +66.1) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +62.1% (+50.7 to +73.5) | +64.7% (+53.0 to +76.4) | +63.3% (+56.0 to +70.6) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +98.9% (+43.4 to +154.4) | +96.2% (+6.3 to +186.0) | +100.0% (+59.7 to +140.3) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+22.1 to +177.9) | +100.0% (−126.2 to +326.2) | +100.0% (+21.0 to +179.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +35.6000 (+26.8575 to +44.3425) | +37.1000 (+26.2129 to +47.9871) | +41.3000 (+32.1269 to +50.4731) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | −58.0% (−188.2 to +72.1) | −59.0% (−180.6 to +62.6) | −22.5% (−227.0 to +182.0) | shown, not judged |
| utilisation (used / allocatable) | +43.2% (+34.3 to +52.1) | +36.6% (+25.0 to +48.2) | +49.2% (+43.4 to +55.1) | shown, not judged |
| CPU used (cores), mean | +43.2% (+34.3 to +52.1) | +36.6% (+25.0 to +48.2) | +49.2% (+43.4 to +55.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0108 (+0.0089 to +0.0126) | +0.0092 (+0.0070 to +0.0115) | +0.0112 (+0.0097 to +0.0128) | shown, not judged |
| CPU used with Omni's own (cores), mean | +44.5% (+35.5 to +53.6) | +37.8% (+26.0 to +49.7) | +50.6% (+44.6 to +56.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | −28.0% (−32.2 to −23.9) | −24.4% (−29.9 to −18.8) | −31.2% (−33.6 to −28.7) | shown, not judged |
| HPA replicas, mean | +20.3% (+10.1 to +30.5) | +19.7% (+7.2 to +32.2) | +28.7% (+18.7 to +38.7) | **power given in all three of our runs** |
| pods started | +44.1% (+19.3 to +68.9) | +55.9% (+20.9 to +90.9) | +103.1% (+50.4 to +155.9) | **power given in all three of our runs** |
| pod start wait, total (s) | −75.0% (−27.8 to −122.2) | −102.3% (−38.5 to −166.1) | −137.0% (−32.0 to −241.9) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | −19.4% (−44.9 to +6.1) | −32.1% (−7.0 to −57.2) | −11.2% (−49.8 to +27.5) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | +42.3% (+33.3 to +51.4) | +35.4% (+24.1 to +46.8) | +46.9% (+40.9 to +53.0) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 1 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 LOSS in all three of our runs, 4 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
