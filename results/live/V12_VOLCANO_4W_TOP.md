# Volcano under the batch stream, the four ways: Omni-Compass on top of Volcano against Volcano as shipped (register row 63): the A/B/C three-run table (Omni v12)

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
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -12.4% (-24.7 to -0.2) | -17.5% (-31.0 to -4.0) | -15.2% (-27.0 to -3.3) | **GAIN in all three of our runs** |
| node-hours | -12.5% (-24.9 to -0.1) | -17.5% (-30.9 to -4.1) | -15.0% (-26.8 to -3.2) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.5 to +0.3) | -0.0% (-0.2 to +0.2) | +0.2% (-0.2 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -8.7% (-17.4 to +0.0) | -12.1% (-21.5 to -2.8) | -10.4% (-18.5 to -2.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | -19.8% (-29.9 to -9.7) | -10.9% (-20.7 to -1.1) | -12.0% (-20.2 to -3.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +0.3% (-21.7 to +22.3) | +13.4% (-8.4 to +35.1) | +10.6% (-7.0 to +28.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| response time (ms), 99th percentile | -2.5% (-29.8 to +24.9) | +6.0% (-4.9 to +16.9) | +6.6% (-5.2 to +18.4) | **the runs disagree** |
| time over the response line (% of samples) | -5.3% (-46.0 to +35.3) | -10.2% (-30.5 to +10.0) | -7.3% (-23.3 to +8.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -6.6% (-22.1 to +8.9) | -12.7% (-26.5 to +1.1) | +5.8% (-5.3 to +16.9) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +35.2 (+21.52 to +48.88) | +32.1 (+26.23 to +37.97) | +38.3 (+22.68 to +53.92) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +6.8% (-8.0 to +21.5) | +1.3% (-9.9 to +12.6) | +0.4% (-18.6 to +19.5) | shown, not judged |
| utilisation (used / allocatable) | +15.4% (+1.0 to +29.7) | +20.5% (+4.7 to +36.4) | +18.0% (+3.9 to +32.0) | shown, not judged |
| CPU used (cores), mean | -0.6% (-2.7 to +1.5) | -2.0% (-4.2 to +0.3) | -1.1% (-3.0 to +0.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01708 (+0.01579 to +0.01837) | +0.01657 (+0.01502 to +0.01812) | +0.01846 (+0.01514 to +0.02178) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.6% (-1.5 to +2.7) | -0.8% (-3.1 to +1.5) | +0.2% (-1.8 to +2.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -9.0% (-16.9 to -1.0) | -11.7% (-20.7 to -2.7) | -10.7% (-19.2 to -2.2) | shown, not judged |
| HPA replicas, mean | -2.4% (-10.5 to +5.6) | +4.7% (-5.7 to +15.1) | +4.1% (-3.7 to +12.0) | **the runs disagree** |
| pods started | +100.0% (-306.0 to +506.0) | +300.0% (-378.6 to +978.6) | +0.3 (-0.04553 to +0.6455) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +100.0% (-306.0 to +506.0) | +1300.0% (-1085.5 to +3685.5) | +1.2 (-0.3004 to +2.7) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | +100.0% (-306.0 to +506.0) | +600.0% (-625.1 to +1825.1) | +1.2 (-0.3004 to +2.7) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.3% (+1.7 to +2.9) | +1.9% (+0.9 to +2.9) | +2.3% (+1.4 to +3.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.6% (+0.1 to +1.1) | +0.3% (-0.4 to +0.9) | +0.4% (-0.2 to +0.9) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -22.0% (-43.0 to -0.9) | -29.5% (-51.7 to -7.4) | -27.2% (-45.9 to -8.4) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +6.4% (-9.5 to +22.2) | +23.0% (-8.0 to +53.9) | -4.7% (-18.9 to +9.5) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -7.1% (-36.1 to +21.9) | +46.7% (-28.1 to +121.4) | +8.3% (-25.5 to +42.2) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | +6.4% (+0.7 to +12.1) | +1.8% (-4.5 to +8.1) | +2.3% (-2.1 to +6.8) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 4 GAIN in all three of our runs, 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 1 power given (the same way in all three runs; 0 of 3 clear of the noise), 5 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.15%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
