# CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38695794476 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38708509996 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38721988615 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | -0.2% (-0.6 to +0.2) | -2.1% (-6.9 to +2.7) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| node-hours | -0.1% (-0.8 to +0.5) | +0.5% (+0.2 to +0.9) | -2.3% (-7.3 to +2.7) | **the runs disagree** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.4) | +0.7% (+0.3 to +1.1) | +0.5% (-1.1 to +2.1) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.2% (-0.7 to +0.4) | +0.6% (+0.4 to +0.8) | -1.0% (-3.0 to +1.0) | **the runs disagree** |
| response time (ms), mean | -1.6% (-3.6 to +0.3) | +0.3% (-1.0 to +1.6) | +1.1% (-0.5 to +2.7) | **the runs disagree** |
| response time (ms), 95th percentile | -1.9% (-3.9 to +0.2) | +0.7% (-1.0 to +2.4) | +1.7% (-0.3 to +3.7) | **the runs disagree** |
| response time (ms), 99th percentile | -3.8% (-9.9 to +2.2) | -5.6% (-15.9 to +4.7) | +6.0% (-4.0 to +16.1) | **the runs disagree** |
| time over the response line (% of samples) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0.1 (-0.1262 to +0.3262) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +70.8% (-151.2 to +292.9) | -69.7% (-145.9 to +6.5) | +658.8% (-45.8 to +1363.4) | shown, not judged |
| utilisation (used / allocatable) | -0.4% (-2.4 to +1.7) | -1.6% (-3.5 to +0.2) | +0.9% (-3.6 to +5.3) | shown, not judged |
| CPU used (cores), mean | -0.4% (-2.4 to +1.7) | -1.8% (-3.6 to -0.1) | -2.0% (-4.8 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00848 (+0.007386 to +0.009574) | +0.00834 (+0.007285 to +0.009395) | +0.00828 (+0.006583 to +0.009977) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.3% (-1.7 to +2.4) | -1.1% (-2.9 to +0.6) | -1.2% (-4.0 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.6% (-1.7 to +3.0) | +1.8% (-0.3 to +3.8) | +1.1% (-1.0 to +3.1) | shown, not judged |
| HPA replicas, mean | -2.8% (-9.8 to +4.1) | -4.7% (-12.7 to +3.3) | +1.9% (-5.3 to +9.0) | **the runs disagree** |
| pods started | -7.7% (-78.5 to +63.1) | -25.0% (-62.7 to +12.7) | +14.3% (-43.7 to +72.3) | **the runs disagree** |
| pod start wait, total (s) | +15.2% (-151.6 to +181.9) | -58.7% (-144.0 to +26.6) | +44.4% (-89.1 to +178.0) | **the runs disagree** |
| pod start wait, mean (s) | +16.1% (-94.9 to +127.1) | -48.5% (-119.2 to +22.1) | +27.6% (-68.9 to +124.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +0.5% (-1.3 to +2.4) | +1.3% (-0.1 to +2.8) | +1.1% (-1.6 to +3.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 power given (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise), 9 the runs disagree, 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
