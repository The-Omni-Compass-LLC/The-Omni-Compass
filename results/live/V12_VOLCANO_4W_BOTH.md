# Volcano under the batch stream, the four ways: Omni-Compass on top of Volcano against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -12.4% (-24.7 to -0.2) | -17.5% (-31.0 to -4.0) | -15.2% (-27.0 to -3.3) | **GAIN in all three of our runs** |
| node-hours | -12.5% (-24.9 to -0.1) | -17.5% (-31.1 to -3.9) | -15.2% (-27.1 to -3.3) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.5 to +0.2) | -0.0% (-0.3 to +0.3) | -0.1% (-0.4 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -8.7% (-17.4 to +0.0) | -12.2% (-21.7 to -2.6) | -10.5% (-18.9 to -2.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | -41.0% (-54.6 to -27.4) | -29.4% (-44.0 to -14.8) | -28.8% (-40.7 to -17.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -44.0% (-65.6 to -22.3) | -11.5% (-33.2 to +10.2) | -21.2% (-36.3 to -6.1) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 99th percentile | -38.3% (-55.8 to -20.8) | -3.7% (-24.8 to +17.5) | -4.8% (-27.3 to +17.8) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | -58.8% (-93.4 to -24.3) | -43.0% (-79.6 to -6.3) | -42.4% (-72.9 to -11.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -18.4% (-30.1 to -6.6) | -21.5% (-38.6 to -4.4) | -16.1% (-35.2 to +3.0) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +35.2 (+21.52 to +48.88) | +32.1 (+26.23 to +37.97) | +38.3 (+22.68 to +53.92) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +45.3% (+22.2 to +68.5) | +69.3% (+31.7 to +106.9) | +49.0% (+16.4 to +81.6) | shown, not judged |
| utilisation (used / allocatable) | +15.5% (+1.0 to +30.1) | +20.9% (+5.0 to +36.9) | +18.3% (+5.0 to +31.6) | shown, not judged |
| CPU used (cores), mean | -0.5% (-2.4 to +1.5) | -1.6% (-4.2 to +1.0) | -0.8% (-3.3 to +1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01708 (+0.01579 to +0.01837) | +0.01657 (+0.01502 to +0.01812) | +0.01846 (+0.01514 to +0.02178) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.7% (-1.2 to +2.7) | -0.5% (-3.1 to +2.2) | +0.5% (-2.1 to +3.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -9.1% (-17.4 to -0.9) | -11.9% (-20.9 to -3.0) | -10.5% (-18.2 to -2.9) | shown, not judged |
| HPA replicas, mean | -0.5% (-8.5 to +7.4) | +4.1% (-7.3 to +15.5) | +8.0% (-0.2 to +16.2) | **the runs disagree** |
| pods started | +0.0% (-168.6 to +168.6) | +100.0% (-306.0 to +506.0) | +200.0% (-252.4 to +652.4) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +0.0% (-168.6 to +168.6) | +366.7% (-477.8 to +1211.2) | +500.0% (-326.0 to +1326.0) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | +100.0% (-126.2 to +326.2) | +366.7% (-477.8 to +1211.2) | +500.0% (-326.0 to +1326.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +4.8% (+4.4 to +5.3) | +5.0% (+4.0 to +5.9) | +4.9% (+3.7 to +6.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +1.8% (+0.8 to +2.8) | +1.7% (+0.4 to +2.9) | +1.8% (+0.4 to +3.2) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -22.0% (-43.0 to -0.9) | -29.5% (-51.7 to -7.4) | -27.2% (-45.9 to -8.4) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +1126.7% (+1020.2 to +1233.2) | +1088.9% (+690.1 to +1487.7) | +1416.7% (+986.8 to +1846.5) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +333.3% (+174.4 to +492.3) | +450.0% (+38.7 to +861.3) | +550.0% (+436.9 to +663.1) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +32.1% (+13.4 to +50.8) | +19.7% (+5.5 to +33.9) | +26.0% (+8.1 to +43.9) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN in all three of our runs, 1 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 3 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 4 LOSS in all three of our runs, 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.11%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
