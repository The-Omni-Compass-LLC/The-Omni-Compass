# The KAI scheduler under the batch stream, the four ways: Omni-Compass on the organism alone against KAI as shipped (register row 91): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the orchestrator as shipped: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368344021 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368351097 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368358521 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -16.7% (-28.4 to -4.9) | -11.1% (-18.0 to -4.2) | -13.2% (-22.6 to -3.8) | **GAIN in all three of our runs** |
| node-hours | -16.7% (-28.5 to -4.9) | -11.2% (-18.1 to -4.3) | -13.1% (-22.6 to -3.6) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.4 to +0.1) | -0.2% (-0.6 to +0.1) | +0.1% (-0.2 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.23%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -11.7% (-19.9 to -3.5) | -7.9% (-12.6 to -3.1) | -9.0% (-15.5 to -2.5) | **GAIN in all three of our runs** |
| response time (ms), mean | -22.5% (-36.3 to -8.7) | -21.6% (-27.8 to -15.3) | -27.9% (-40.0 to -15.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -25.9% (-48.4 to -3.3) | -24.8% (-38.9 to -10.7) | -32.8% (-52.7 to -13.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -28.8% (-51.9 to -5.6) | -24.9% (-36.8 to -13.0) | -38.5% (-57.3 to -19.8) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +16.2% (+5.8 to +26.6) | +5.0% (-12.2 to +22.3) | +8.2% (-2.0 to +18.5) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -3.4% (-11.2 to +4.4) | -6.5% (-11.0 to -1.9) | -5.2% (-9.5 to -0.9) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +46.9 (+30.23 to +63.57) | +47.1 (+30.24 to +63.96) | +43.6 (+31.77 to +55.43) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -47.3% (-74.6 to -20.1) | -48.6% (-77.3 to -20.0) | -41.2% (-50.8 to -31.6) | shown, not judged |
| utilisation (used / allocatable) | +18.4% (+4.4 to +32.5) | +11.7% (+4.2 to +19.2) | +15.5% (+2.3 to +28.7) | shown, not judged |
| CPU used (cores), mean | -1.8% (-4.0 to +0.5) | -0.4% (-1.4 to +0.5) | -0.9% (-2.0 to +0.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.017 (+0.01555 to +0.01845) | +0.01824 (+0.01718 to +0.0193) | +0.01791 (+0.01675 to +0.01907) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.6% (-2.8 to +1.7) | +0.7% (-0.2 to +1.7) | +0.3% (-0.9 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -11.4% (-20.6 to -2.2) | -8.1% (-13.7 to -2.5) | -9.0% (-16.5 to -1.4) | shown, not judged |
| HPA replicas, mean | -2.1% (-7.1 to +2.9) | +0.2% (-7.8 to +8.2) | +1.7% (-4.0 to +7.3) | **the runs disagree** |
| pods started | -100.0% (-326.2 to +126.2) | +0.0% (-292.0 to +292.0) | -100.0% (-260.9 to +60.9) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -100.0% (-326.2 to +126.2) | -33.3% (-295.7 to +229.1) | -100.0% (-260.9 to +60.9) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -100.0% (-326.2 to +126.2) | +33.3% (-293.4 to +360.1) | -100.0% (-250.8 to +50.8) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -3.5% (-5.0 to -2.0) | -3.9% (-5.3 to -2.5) | -3.6% (-4.8 to -2.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | -3.6% (-5.8 to -1.3) | -4.5% (-6.6 to -2.4) | -4.3% (-6.0 to -2.6) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -29.9% (-49.2 to -10.7) | -21.8% (-34.8 to -8.7) | -24.2% (-38.3 to -10.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -98.0% (-120.0 to -76.1) | -93.0% (-121.5 to -64.4) | -91.6% (-105.0 to -78.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -100.0% (-156.5 to -43.5) | -84.6% (-142.3 to -26.9) | -64.3% (-93.3 to -35.3) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | -25.8% (-41.5 to -10.1) | -23.9% (-33.7 to -14.0) | -31.1% (-43.6 to -18.6) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 11 GAIN in all three of our runs, 1 GAIN (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 2 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.23%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
