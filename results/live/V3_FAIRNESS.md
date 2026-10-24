# Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013235441 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013239864 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013244591 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.0% (-0.2 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.3 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.3 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| response time (ms), mean | -4.1% (-10.7 to +2.6) | -5.4% (-13.8 to +2.9) | -3.8% (-12.2 to +4.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| response time (ms), 95th percentile | +17.9% (+3.7 to +32.1) | +6.8% (-12.1 to +25.6) | +8.1% (-9.1 to +25.3) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 99th percentile | +8.2% (-7.3 to +23.7) | +8.9% (-6.0 to +23.8) | +6.7% (-14.5 to +27.9) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | -4.2% (-12.5 to +4.1) | -5.5% (-12.1 to +1.0) | -2.9% (-6.6 to +0.9) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | -5.3% (-17.9 to +7.4) | -16.2% (-30.7 to -1.8) | -29.5% (-51.3 to -7.7) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -21.7% (-85.0 to +41.6) | +96.6% (-11.3 to +204.4) | +43.3% (+6.2 to +80.4) | shown, not judged |
| utilisation (used / allocatable) | -0.6% (-1.4 to +0.2) | -0.9% (-1.6 to -0.2) | -0.1% (-1.1 to +0.9) | shown, not judged |
| CPU used (cores), mean | -0.6% (-1.4 to +0.2) | -0.9% (-1.6 to -0.2) | -0.1% (-1.1 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01376 (+0.01158 to +0.01594) | +0.0142 (+0.01175 to +0.01665) | +0.01438 (+0.01232 to +0.01644) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.0% (-0.8 to +0.8) | -0.3% (-1.0 to +0.4) | +0.5% (-0.4 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.7% (-0.5 to +1.9) | +1.0% (+0.1 to +1.9) | -0.1% (-1.3 to +1.0) | shown, not judged |
| HPA replicas, mean | +0.5% (-1.8 to +2.8) | +0.2% (-2.0 to +2.3) | +0.5% (-1.2 to +2.3) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pods started | -10.9% (-41.3 to +19.6) | -15.4% (-40.1 to +9.4) | -13.0% (-40.7 to +14.6) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +17.0% (-38.9 to +73.0) | +8.8% (-41.1 to +58.7) | +2.3% (-46.5 to +51.1) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | +15.4% (-29.4 to +60.2) | +3.5% (-29.3 to +36.2) | +16.2% (-17.0 to +49.3) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +1.0% (+0.2 to +1.8) | +0.0% (-0.6 to +0.7) | +0.4% (-0.2 to +1.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | -7.3% (-25.7 to +11.1) | +6.3% (-5.0 to +17.7) | -1.3% (-21.0 to +18.5) | **the runs disagree** |
| second app: response time (ms), 99th percentile | -25.2% (-74.5 to +24.0) | -28.7% (-80.8 to +23.5) | -16.7% (-53.6 to +20.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| second app: time over the response line (% of samples) | -3.6% (-7.4 to +0.1) | -1.2% (-3.4 to +1.1) | +0.5% (-4.5 to +5.6) | **the runs disagree** |
| second app: failed requests (%) | +1.8% (-3.5 to +7.1) | -0.7% (-3.9 to +2.6) | +3.9% (-0.2 to +8.1) | **the runs disagree** |

Readings: 4 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 3 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 3 the runs disagree, 3 EVEN, the same, 3 EVEN, under the floor (every run under 0.5%; the largest 0.15%), 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
