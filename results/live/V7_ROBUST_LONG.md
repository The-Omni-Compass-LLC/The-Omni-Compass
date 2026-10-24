# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38937561382 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| B | 38949637918 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| C | 38961359324 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.1% (-0.1 to +0.2) | -0.0% (-0.3 to +0.3) | -0.0% (-0.3 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.3 to -0.0) | -0.4% (-1.0 to +0.2) | -0.4% (-2.0 to +1.2) | EVEN, under the floor (every run under 0.5%; the largest 0.40%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.3 to -0.0) | -0.4% (-1.0 to +0.2) | -0.4% (-2.0 to +1.2) | EVEN, under the floor (every run under 0.5%; the largest 0.40%) |
| response time (ms), mean | -39.1% (-77.2 to -1.0) | -40.2% (-109.3 to +28.8) | -46.7% (-89.6 to -3.7) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 95th percentile | -43.2% (-89.0 to +2.6) | -44.3% (-128.6 to +39.9) | -54.1% (-124.0 to +15.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| response time (ms), 99th percentile | -26.2% (-48.6 to -3.9) | -18.1% (-47.3 to +11.2) | -38.0% (-122.5 to +46.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | -33.3% (-76.5 to +9.9) | -33.8% (-106.6 to +39.0) | -61.5% (-142.1 to +19.1) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | -16.8% (-54.2 to +20.7) | -17.3% (-59.9 to +25.4) | -47.9% (-230.2 to +134.4) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -19.7% (-34.5 to -4.9) | -19.8% (-23.2 to -16.3) | -39.6% (-100.4 to +21.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +164.7 (-120.1 to +449.4) | +102 (+89.58 to +114.4) | +232.7 (+142.7 to +322.7) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -5.6% (-229.8 to +218.6) | -27.2% (-83.1 to +28.7) | +16.3% (-412.0 to +444.7) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-2.3 to -1.1) | -2.8% (-4.7 to -0.9) | -2.7% (-14.0 to +8.5) | shown, not judged |
| CPU used (cores), mean | -1.7% (-2.3 to -1.1) | -2.8% (-4.7 to -0.9) | -2.7% (-14.0 to +8.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0109 (+0.009349 to +0.01245) | +0.009233 (+0.004207 to +0.01426) | +0.0097 (+0.008562 to +0.01084) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.3% (-2.0 to -0.7) | -2.4% (-4.2 to -0.6) | -2.3% (-13.6 to +8.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.6% (-0.3 to +3.5) | +3.1% (-3.6 to +9.8) | +2.4% (-7.3 to +12.1) | shown, not judged |
| HPA replicas, mean | +50.8% (+46.0 to +55.6) | +33.1% (-48.4 to +114.6) | +49.5% (+47.8 to +51.2) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pods started | +206.2% (-479.9 to +892.4) | +83.3% (+11.6 to +155.1) | +300.0% (+53.5 to +546.5) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pod start wait, total (s) | +94.6% (-381.9 to +571.2) | +9.8% (-90.2 to +109.8) | +162.1% (-275.8 to +600.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -40.5% (-67.4 to -13.7) | -31.9% (-124.6 to +60.9) | -35.5% (-177.3 to +106.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | -0.5% (-1.5 to +0.5) | -1.5% (-2.9 to -0.2) | -2.0% (-12.7 to +8.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.038 | 1.043 | 1.036 | no leak (every repetition under 1.25) |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 97.5% | 97.5% | 99.2% | valid (every repetition at 95% of the expected or more) |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 0 | 0 | 0 | none in any repetition |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 0.89 | 1.17 | 0.80 | no growth beyond the limit (every repetition under 1.5) |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **every setting handed back at the end of every repetition, in all three of our runs** |

Readings: 3 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 every setting handed back at the end of every repetition, in all three of our runs, 2 power given (the same way in all three runs; 2 of 3 clear of the noise), 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.08%), 2 EVEN, under the floor (every run under 0.5%; the largest 0.40%), 1 no growth beyond the limit (every repetition under 1.5), 1 no leak (every repetition under 1.25), 1 none in any repetition, 9 shown, not judged, 1 valid (every repetition at 95% of the expected or more).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
