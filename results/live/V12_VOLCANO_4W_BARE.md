# Volcano under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -14.6% (-21.6 to -7.6) | -19.2% (-31.0 to -7.4) | -11.8% (-23.7 to +0.1) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| node-hours | -14.5% (-21.5 to -7.6) | -19.1% (-31.0 to -7.2) | -11.8% (-23.7 to +0.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.2 to +0.4) | -0.0% (-0.4 to +0.3) | +0.1% (-0.2 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -10.0% (-14.8 to -5.2) | -13.3% (-21.7 to -4.9) | -8.1% (-16.4 to +0.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | -11.7% (-15.0 to -8.4) | -11.7% (-17.3 to -6.1) | -8.6% (-13.0 to -4.2) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +7.6% (+0.8 to +14.5) | +2.9% (-2.9 to +8.8) | +7.5% (-0.1 to +15.1) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 99th percentile | +9.7% (+1.9 to +17.5) | -0.4% (-10.6 to +9.7) | +10.4% (-0.9 to +21.7) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | -2.6% (-8.1 to +2.9) | -4.5% (-13.6 to +4.5) | -3.8% (-7.8 to +0.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +13.8% (-1.1 to +28.7) | +0.0% (-8.5 to +8.5) | -2.3% (-15.0 to +10.4) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +40.2 (+31.7 to +48.7) | +55.7 (+35.95 to +75.45) | +49.7 (+37.2 to +62.2) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +4.6% (-12.0 to +21.2) | +9.8% (-12.2 to +31.9) | +2.6% (-13.6 to +18.9) | shown, not judged |
| utilisation (used / allocatable) | +17.3% (+9.4 to +25.3) | +22.6% (+7.2 to +37.9) | +14.1% (+0.6 to +27.6) | shown, not judged |
| CPU used (cores), mean | -0.2% (-1.2 to +0.8) | -2.3% (-4.1 to -0.6) | -0.5% (-3.3 to +2.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01732 (+0.01601 to +0.01863) | +0.01773 (+0.01636 to +0.0191) | +0.01698 (+0.0147 to +0.01926) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.0% (-0.0 to +2.1) | -1.1% (-2.9 to +0.7) | +0.7% (-2.2 to +3.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.2% (-15.4 to -5.1) | -12.2% (-20.8 to -3.7) | -8.4% (-16.3 to -0.5) | shown, not judged |
| HPA replicas, mean | -0.3% (-9.9 to +9.3) | +5.4% (-6.7 to +17.4) | +0.9% (-6.0 to +7.7) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pods started | -100.0% (-326.2 to +126.2) | +0.0% (-337.2 to +337.2) | +0.0% (-337.2 to +337.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -100.0% (-326.2 to +126.2) | +0.0% (-337.2 to +337.2) | +0.0% (-337.2 to +337.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -100.0% (-326.2 to +126.2) | +0.0% (-337.2 to +337.2) | +0.0% (-337.2 to +337.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.4% (+1.9 to +2.9) | +2.1% (+1.5 to +2.6) | +2.1% (+0.8 to +3.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.4% (-0.1 to +1.0) | +0.2% (-0.2 to +0.6) | +0.6% (+0.0 to +1.1) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -29.0% (-42.4 to -15.7) | -33.8% (-51.4 to -16.2) | -20.5% (-40.2 to -0.9) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -13.3% (-80.0 to +53.4) | -11.1% (-63.4 to +41.2) | +16.7% (-91.4 to +124.8) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +0.0% (-159.0 to +159.0) | +25.0% (-76.5 to +126.5) | +150.0% (-91.4 to +391.4) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | +7.3% (+1.1 to +13.4) | +1.5% (-1.8 to +4.8) | +9.0% (+1.5 to +16.5) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 2 GAIN in all three of our runs, 3 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 3 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 2 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.12%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
