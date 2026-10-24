# Kueue under the batch stream, the four ways: Omni-Compass on top of Kueue against Kueue as shipped (register row 63): the A/B/C three-run table (Omni v12)

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
| A | 39368387821 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368394823 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368401852 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -11.3% (-21.5 to -1.0) | -9.7% (-17.6 to -1.8) | -11.0% (-21.4 to -0.7) | **GAIN in all three of our runs** |
| node-hours | -11.3% (-21.6 to -1.0) | -9.8% (-17.9 to -1.8) | -11.1% (-21.5 to -0.7) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.0% (-0.4 to +0.4) | -0.0% (-0.5 to +0.4) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -7.8% (-15.0 to -0.7) | -6.7% (-12.1 to -1.3) | -7.7% (-14.9 to -0.5) | **GAIN in all three of our runs** |
| response time (ms), mean | -14.7% (-20.2 to -9.2) | -11.1% (-16.4 to -5.8) | -11.8% (-17.4 to -6.2) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -2.9% (-9.4 to +3.6) | +3.1% (-7.5 to +13.7) | +4.7% (-2.5 to +11.9) | **the runs disagree** |
| response time (ms), 99th percentile | -2.3% (-6.6 to +2.0) | +5.7% (-3.7 to +15.1) | +0.6% (-6.7 to +7.9) | **the runs disagree** |
| time over the response line (% of samples) | -7.2% (-13.4 to -1.0) | -5.6% (-10.6 to -0.7) | -6.7% (-11.6 to -1.9) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0.009302 (-0.01174 to +0.03034) | +0 (+0 to +0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +2.6% (-8.7 to +13.8) | +2.9% (-1.8 to +7.6) | +2.0% (-1.1 to +5.1) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +42 (+34.37 to +49.63) | +34.2 (+21.64 to +46.76) | +33.11 (+21.77 to +44.46) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.4% (-7.9 to +10.7) | +7.0% (-5.6 to +19.5) | +5.4% (-12.7 to +23.5) | shown, not judged |
| utilisation (used / allocatable) | +12.5% (+0.3 to +24.7) | +12.7% (+1.2 to +24.3) | +13.0% (+0.2 to +25.9) | shown, not judged |
| CPU used (cores), mean | -1.1% (-2.3 to +0.2) | +1.5% (-1.3 to +4.2) | -0.2% (-1.6 to +1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01752 (+0.01459 to +0.02045) | +0.01711 (+0.01525 to +0.01897) | +0.01838 (+0.0172 to +0.01956) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.2% (-1.1 to +1.5) | +2.6% (-0.2 to +5.4) | +1.0% (-0.4 to +2.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -7.7% (-15.7 to +0.3) | -9.3% (-18.8 to +0.2) | -8.3% (-17.0 to +0.4) | shown, not judged |
| HPA replicas, mean | +2.8% (-2.9 to +8.6) | +5.8% (-1.0 to +12.7) | -1.2% (-13.4 to +11.0) | **the runs disagree** |
| pods started | +0.0% (-337.2 to +337.2) | +100.0% (-126.2 to +326.2) | +400.0% (-301.3 to +1101.3) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -75.0% (-314.2 to +164.2) | -25.0% (-156.9 to +106.9) | +266.7% (-314.9 to +848.3) | **the runs disagree** |
| pod start wait, mean (s) | -75.0% (-314.2 to +164.2) | -25.0% (-156.9 to +106.9) | +116.7% (-273.4 to +506.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +1.7% (+0.9 to +2.5) | +3.0% (+1.4 to +4.6) | +2.8% (+1.2 to +4.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.1% (-0.6 to +0.7) | +0.5% (-0.0 to +1.1) | +0.5% (-0.1 to +1.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -21.4% (-40.0 to -2.7) | -19.2% (-34.2 to -4.2) | -21.3% (-39.6 to -2.9) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +2.6% (-75.0 to +80.1) | -0.0% (-63.2 to +63.2) | -0.0% (-17.9 to +17.9) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -40.0% (-90.0 to +10.0) | -20.0% (-50.2 to +10.2) | +12.5% (-16.3 to +41.3) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | +0.9% (-5.4 to +7.3) | +4.2% (-2.2 to +10.6) | +3.5% (-2.7 to +9.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 6 GAIN in all three of our runs, 3 LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 6 the runs disagree, 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.10%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
