# Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1): the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40227141899 | `433bcf30d2ad` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40250378687 | `ddc44f445d06` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40271292066 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.3 to +0.1) | =0.0% (−0.1 to +0.1) | =0.0% (−0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.03%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.4% (−0.6 to −0.2) | =0.3% (−0.4 to −0.2) | =0.3% (−0.4 to −0.1) | EVEN, under the floor (the three runs' mean 0.32%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.4% (−0.6 to −0.2) | =0.3% (−0.4 to −0.2) | =0.3% (−0.4 to −0.1) | EVEN, under the floor (the three runs' mean 0.32%) |
| response time (ms), mean | +40.4% (+27.4 to +53.4) | +40.9% (+32.4 to +49.5) | +45.1% (+30.7 to +59.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +59.0% (+40.7 to +77.2) | +56.4% (+47.8 to +64.9) | +58.8% (+41.6 to +76.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +11.5% (−34.3 to +57.2) | +23.6% (−19.8 to +67.0) | +34.7% (+2.6 to +66.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| time over the response line (% of samples) | +40.4% (+23.5 to +57.3) | +37.7% (+27.3 to +48.2) | +34.8% (+21.6 to +48.0) | **GAIN in all three of our runs** |
| failed requests (%) | +13.9% (+3.6 to +24.2) | +14.9% (+6.2 to +23.5) | +12.2% (+5.1 to +19.2) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +29.0% (+22.1 to +35.9) | +27.0% (+19.9 to +34.1) | +22.4% (+18.4 to +26.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +38.1000 (+29.4277 to +46.7723) | +39.8000 (+30.4565 to +49.1435) | +34.2000 (+26.8835 to +41.5165) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +85.4% (−16.2 to +187.1) | +167.0% (−36.0 to +370.1) | −1.6% (−84.6 to +81.5) | shown, not judged |
| utilisation (used / allocatable) | −2.7% (−3.4 to −2.1) | −2.0% (−2.6 to −1.5) | −2.1% (−3.1 to −1.2) | shown, not judged |
| CPU used (cores), mean | −2.7% (−3.4 to −2.1) | −2.0% (−2.6 to −1.5) | −2.1% (−3.1 to −1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0087 (+0.0074 to +0.0099) | +0.0093 (+0.0084 to +0.0102) | +0.0087 (+0.0074 to +0.0100) | shown, not judged |
| CPU used with Omni's own (cores), mean | −2.3% (−3.0 to −1.6) | −1.6% (−2.2 to −1.1) | −1.8% (−2.8 to −0.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +3.5% (+1.2 to +5.9) | +1.8% (+1.2 to +2.5) | +2.3% (−0.3 to +4.9) | shown, not judged |
| HPA replicas, mean | +1.5% (−9.3 to +12.2) | +2.9% (−1.9 to +7.8) | =0.1% (−3.4 to +3.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +14.5% (−24.6 to +53.7) | +11.1% (−36.9 to +59.2) | +9.8% (−26.6 to +46.2) | **the runs disagree** |
| pod start wait, total (s) | −23.5% (−83.3 to +36.2) | −5.7% (−57.0 to +45.6) | +16.9% (−26.0 to +59.8) | **the runs disagree** |
| pod start wait, mean (s) | =0.5% (−22.5 to +21.5) | +4.1% (−21.8 to +29.9) | +9.9% (−9.2 to +29.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | −1.9% (−2.7 to −1.2) | −1.6% (−2.1 to −1.2) | −1.4% (−2.4 to −0.4) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 2 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
