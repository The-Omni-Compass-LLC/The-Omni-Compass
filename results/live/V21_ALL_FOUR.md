# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40227146512 | `433bcf30d2ad` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40250382783 | `ddc44f445d06` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40272629580 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge) | +30.0% (+22.5 to +37.5) | +51.5% (+36.9 to +66.1) | +40.6% (+29.8 to +51.4) | **GAIN in all three of our runs** |
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to −0.0) | EVEN, the same |
| node-hours | =0.0% (−0.2 to +0.1) | =0.0% (−0.1 to +0.2) | =0.1% (−0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.3 to +0.1) | =0.1% (−0.4 to +0.1) | =0.1% (−0.4 to +0.1) | EVEN, under the floor (the three runs' mean 0.11%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.1% (−0.3 to +0.1) | =0.1% (−0.4 to +0.1) | =0.1% (−0.4 to +0.1) | EVEN, under the floor (the three runs' mean 0.11%) |
| response time (ms), mean | +36.0% (+23.6 to +48.4) | +43.2% (+30.8 to +55.6) | +41.4% (+27.3 to +55.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +51.5% (+35.5 to +67.5) | +59.5% (+41.7 to +77.3) | +56.2% (+38.4 to +74.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | −5.5% (−60.2 to +49.2) | +29.1% (−12.0 to +70.3) | +23.9% (−19.7 to +67.5) | **the runs disagree** |
| time over the response line (% of samples) | +31.8% (+17.0 to +46.6) | +36.5% (+24.6 to +48.5) | +33.7% (+20.1 to +47.3) | **GAIN in all three of our runs** |
| failed requests (%) | +5.3% (−1.7 to +12.3) | +5.1% (+0.1 to +10.1) | +5.4% (−0.2 to +11.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +20.3% (+11.7 to +28.8) | +23.6% (+16.6 to +30.7) | +15.8% (+8.1 to +23.6) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +30.9000 (+23.7354 to +38.0646) | +37.0000 (+28.1618 to +45.8382) | +36.1000 (+26.1916 to +46.0084) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +31.9% (−65.0 to +128.8) | +4.9% (−136.5 to +146.2) | −23.8% (−138.1 to +90.5) | shown, not judged |
| utilisation (used / allocatable) | −0.4% (−1.7 to +0.9) | −1.4% (−3.5 to +0.7) | −0.7% (−1.9 to +0.6) | shown, not judged |
| CPU used (cores), mean | −0.4% (−1.7 to +0.9) | −1.4% (−3.5 to +0.7) | −0.7% (−1.9 to +0.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0082 (+0.0067 to +0.0096) | +0.0086 (+0.0073 to +0.0099) | +0.0087 (+0.0072 to +0.0102) | shown, not judged |
| CPU used with Omni's own (cores), mean | −0.1% (−1.4 to +1.3) | −1.1% (−3.2 to +1.1) | −0.3% (−1.6 to +0.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.1% (−0.4 to +2.6) | +3.1% (−0.8 to +6.9) | +1.3% (−0.4 to +3.1) | shown, not judged |
| HPA replicas, mean | +1.2% (−10.2 to +12.5) | +9.1% (−4.7 to +22.9) | +3.8% (−5.3 to +12.8) | **the runs disagree** |
| pods started | +17.5% (−10.2 to +45.3) | +37.0% (−7.6 to +81.6) | +7.5% (−15.6 to +30.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −15.7% (−51.1 to +19.6) | −42.2% (−100.6 to +16.2) | −19.2% (−61.4 to +23.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | +1.2% (−16.8 to +19.2) | =0.4% (−14.8 to +14.0) | −10.5% (−32.8 to +11.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +0.4% (−0.8 to +1.6) | −1.1% (−3.1 to +1.0) | −0.0% (−1.2 to +1.2) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
