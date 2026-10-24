# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38096663118 | `175cc0feda00` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 9 |
| B | 38099655092 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38099656930 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.6% (-1.2 to +0.1) | -0.6% (-1.2 to +0.1) | -0.7% (-1.4 to -0.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| node-hours | -0.8% (-1.3 to -0.3) | -0.4% (-1.3 to +0.5) | -0.9% (-1.4 to -0.5) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.4% (+1.0 to +1.8) | +1.6% (+0.9 to +2.4) | +1.0% (+0.2 to +1.8) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.0% (+0.4 to +1.7) | +1.2% (+0.1 to +2.3) | +0.5% (-0.3 to +1.4) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | -38.5% (-47.3 to -29.7) | -35.8% (-49.1 to -22.5) | -36.2% (-51.2 to -21.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -53.4% (-62.6 to -44.3) | -50.8% (-62.3 to -39.4) | -52.9% (-66.2 to -39.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -62.3% (-69.9 to -54.7) | -60.3% (-73.0 to -47.5) | -60.0% (-73.1 to -46.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -97.2% (-159.4 to -35.0) | -100.0% (-172.1 to -27.9) | -100.0% (-173.6 to -26.4) | **GAIN in all three of our runs** |
| failed requests (%) | -0.6% (-345.5 to +344.2) | +0 (+0 to +0) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +141.1% (-70.0 to +352.2) | +27.3% (-180.3 to +235.0) | -76.2% (-125.3 to -27.1) | shown, not judged |
| utilisation (used / allocatable) | +32.7% (+24.8 to +40.7) | +28.2% (+20.6 to +35.8) | +25.2% (+15.6 to +34.9) | shown, not judged |
| CPU used (cores), mean | +32.0% (+23.6 to +40.5) | +27.6% (+19.4 to +35.7) | +24.4% (+14.5 to +34.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01499 (+0.0133 to +0.01668) | +0.01517 (+0.01309 to +0.01725) | +0.01432 (+0.01217 to +0.01647) | shown, not judged |
| CPU used with Omni's own (cores), mean | +33.7% (+25.2 to +42.3) | +29.3% (+20.9 to +37.7) | +26.0% (+15.9 to +36.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -22.5% (-26.7 to -18.2) | -19.8% (-23.2 to -16.3) | -17.6% (-22.5 to -12.7) | shown, not judged |
| HPA replicas, mean | +3.1% (+0.9 to +5.2) | +1.3% (-1.9 to +4.4) | +0.3% (-2.9 to +3.6) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| pods started | +0.0% (-16.1 to +16.1) | +4.3% (-13.0 to +21.5) | +4.1% (-2.1 to +10.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -13.6% (-48.1 to +20.9) | +21.6% (-36.1 to +79.2) | +14.5% (-1.0 to +30.0) | **the runs disagree** |
| pod start wait, mean (s) | -17.0% (-41.8 to +7.7) | +12.3% (-31.7 to +56.3) | +10.8% (-6.1 to +27.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +31.2% (+24.3 to +38.1) | +28.3% (+20.2 to +36.5) | +23.9% (+14.9 to +33.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 1 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 GAIN (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 1 power given in all three of our runs, 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise), 1 power given (the same way in all three runs; 2 of 3 clear of the noise), 2 the runs disagree, 2 EVEN, the same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
