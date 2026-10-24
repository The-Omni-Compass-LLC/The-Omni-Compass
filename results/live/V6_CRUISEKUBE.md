# CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38695794476 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38708509996 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38721988615 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.2% (−0.6 to +0.2) | +2.1% (−2.7 to +6.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| node-hours | =0.1% (−0.8 to +0.5) | +0.5% (+0.2 to +0.9) | +2.3% (−2.7 to +7.3) | **the runs disagree** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.7 to +0.4) | +0.7% (+0.3 to +1.1) | =0.5% (−1.1 to +2.1) | EVEN, under the floor (the three runs' mean 0.35%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.2% (−0.7 to +0.4) | +0.6% (+0.4 to +0.8) | +1.0% (−1.0 to +3.0) | **the runs disagree** |
| response time (ms), mean | +1.6% (−0.3 to +3.6) | =0.3% (−1.0 to +1.6) | −1.1% (−2.7 to +0.5) | **the runs disagree** |
| response time (ms), 95th percentile | +1.9% (−0.2 to +3.9) | −0.7% (−2.4 to +1.0) | −1.7% (−3.7 to +0.3) | **the runs disagree** |
| response time (ms), 99th percentile | +3.8% (−2.2 to +9.9) | +5.6% (−4.7 to +15.9) | −6.0% (−16.1 to +4.0) | **the runs disagree** |
| time over the response line (% of samples) | =0.0000 (±0.0000 to ±0.0000) | +100.0% (−126.2 to +326.2) | =0.0000 (±0.0000 to ±0.0000) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | +100.0% (−126.2 to +326.2) | =0.0000 (±0.0000 to ±0.0000) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0.1 (-0.1262 to +0.3262) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +70.8% (-151.2 to +292.9) | -69.7% (-145.9 to +6.5) | +658.8% (-45.8 to +1363.4) | shown, not judged |
| utilisation (used / allocatable) | -0.4% (-2.4 to +1.7) | -1.6% (-3.5 to +0.2) | +0.9% (-3.6 to +5.3) | shown, not judged |
| CPU used (cores), mean | -0.4% (-2.4 to +1.7) | -1.8% (-3.6 to -0.1) | -2.0% (-4.8 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00848 (+0.007386 to +0.009574) | +0.00834 (+0.007285 to +0.009395) | +0.00828 (+0.006583 to +0.009977) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.3% (-1.7 to +2.4) | -1.1% (-2.9 to +0.6) | -1.2% (-4.0 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.6% (-1.7 to +3.0) | +1.8% (-0.3 to +3.8) | +1.1% (-1.0 to +3.1) | shown, not judged |
| HPA replicas, mean | +2.8% (−4.1 to +9.8) | +4.7% (−3.3 to +12.7) | +1.9% (−5.3 to +9.0) | **the runs disagree** |
| pods started | +7.7% (−63.1 to +78.5) | +25.0% (−12.7 to +62.7) | +14.3% (−43.7 to +72.3) | **the runs disagree** |
| pod start wait, total (s) | −15.2% (−181.9 to +151.6) | +58.7% (−26.6 to +144.0) | −44.4% (−178.0 to +89.1) | **the runs disagree** |
| pod start wait, mean (s) | −16.1% (−127.1 to +94.9) | +48.5% (−22.1 to +119.2) | −27.6% (−124.2 to +68.9) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +0.5% (-1.3 to +2.4) | +1.3% (-0.1 to +2.8) | +1.1% (-1.6 to +3.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 3 GAIN by the mean of our three runs, 9 shown, not judged, 9 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
