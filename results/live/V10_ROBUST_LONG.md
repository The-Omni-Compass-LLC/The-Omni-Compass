# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v10)

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
| A | 39111154503 | `13f22e8141c4` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| B | 39119406616 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| C | 39126745660 | `56e00223da79` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.0% (-0.4 to +0.4) | -0.1% (-0.3 to -0.0) | -0.0% (-0.5 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.13%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.4 to +0.1) | -0.3% (-0.4 to -0.1) | -0.2% (-0.4 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.27%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.4 to +0.1) | -0.3% (-0.4 to -0.1) | -0.2% (-0.4 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.27%) |
| response time (ms), mean | -33.6% (-48.7 to -18.6) | -32.6% (-64.5 to -0.7) | -35.1% (-66.4 to -3.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -35.5% (-59.7 to -11.3) | -31.6% (-52.1 to -11.1) | -41.8% (-93.4 to +9.7) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 99th percentile | -9.1% (-39.3 to +21.2) | -4.9% (-44.5 to +34.7) | -0.6% (-35.5 to +34.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | -32.2% (-57.8 to -6.7) | -33.3% (-72.6 to +6.1) | -34.9% (-62.2 to -7.6) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| failed requests (%) | -13.2% (-32.2 to +5.8) | -12.6% (-37.6 to +12.4) | -14.8% (-47.0 to +17.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -19.8% (-34.6 to -5.0) | -21.5% (-36.0 to -7.1) | -19.3% (-33.1 to -5.5) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +161 (-86.58 to +408.6) | +168.7 (-101 to +438.4) | +163.3 (-31.74 to +358.4) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +33.5% (-56.8 to +123.8) | +31.7% (-75.0 to +138.4) | +18.3% (-62.1 to +98.7) | shown, not judged |
| utilisation (used / allocatable) | -1.2% (-2.1 to -0.3) | -1.0% (-2.6 to +0.5) | -1.2% (-3.7 to +1.4) | shown, not judged |
| CPU used (cores), mean | -1.2% (-2.1 to -0.3) | -1.0% (-2.6 to +0.5) | -1.2% (-3.7 to +1.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01027 (+0.00975 to +0.01078) | +0.01117 (+0.008716 to +0.01362) | +0.0107 (+0.01004 to +0.01136) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.8% (-1.8 to +0.1) | -0.6% (-2.2 to +1.0) | -0.8% (-3.3 to +1.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.2% (-0.8 to +3.1) | +0.8% (+0.1 to +1.6) | +0.9% (-0.6 to +2.5) | shown, not judged |
| HPA replicas, mean | +49.3% (+42.6 to +56.1) | +49.6% (+40.7 to +58.5) | +49.2% (+39.3 to +59.0) | **power given in all three of our runs** |
| pods started | +178.6% (-94.6 to +451.8) | +200.0% (-294.6 to +694.6) | +173.3% (-100.3 to +447.0) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +172.7% (-137.8 to +483.2) | +98.0% (-228.8 to +424.9) | +81.2% (-150.6 to +313.1) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -2.5% (-60.5 to +55.4) | -33.0% (-134.4 to +68.4) | -33.7% (-86.1 to +18.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | -0.4% (-1.5 to +0.8) | -0.0% (-0.9 to +0.8) | -0.0% (-2.3 to +2.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.034 | 1.037 | 1.041 | no leak (every repetition under 1.25) |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 97.5% | 97.5% | 97.5% | valid (every repetition at 95% of the expected or more) |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 0 | 0 | 0 | none in any repetition |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 0.97 | 0.96 | 0.93 | no growth beyond the limit (every repetition under 1.5) |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **every setting handed back at the end of every repetition, in all three of our runs** |

Readings: 2 GAIN in all three of our runs, 3 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 every setting handed back at the end of every repetition, in all three of our runs, 1 power given in all three of our runs, 1 power given (the same way in all three runs; 0 of 3 clear of the noise), 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.13%), 2 EVEN, under the floor (every run under 0.5%; the largest 0.27%), 1 no growth beyond the limit (every repetition under 1.5), 1 no leak (every repetition under 1.25), 1 none in any repetition, 9 shown, not judged, 1 valid (every repetition at 95% of the expected or more).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
