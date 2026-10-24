# The KAI scheduler under the batch stream, the four ways: Omni-Compass on top of KAI against KAI as shipped (register row 91): the A/B/C three-run table (Omni v12)

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
| A | 39368344021 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368351097 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368358521 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -14.3% (-24.2 to -4.4) | -7.7% (-14.2 to -1.2) | -6.0% (-12.2 to +0.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| node-hours | -14.2% (-24.1 to -4.4) | -7.8% (-14.4 to -1.2) | -6.0% (-12.3 to +0.4) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.0% (-0.4 to +0.5) | -0.1% (-0.4 to +0.3) | +0.1% (-0.3 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -9.9% (-16.8 to -3.0) | -5.3% (-9.9 to -0.8) | -4.0% (-8.5 to +0.4) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | -11.1% (-20.1 to -2.1) | -7.5% (-11.8 to -3.2) | -9.7% (-16.6 to -2.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +2.8% (-8.6 to +14.1) | +3.4% (-2.4 to +9.1) | +4.4% (-7.1 to +16.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| response time (ms), 99th percentile | +3.7% (-4.5 to +12.0) | +3.4% (-3.5 to +10.3) | +0.5% (-9.2 to +10.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | -3.5% (-13.1 to +6.0) | -3.0% (-11.4 to +5.3) | -1.0% (-13.6 to +11.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +1.1% (-3.5 to +5.8) | -2.4% (-7.9 to +3.1) | -0.9% (-4.4 to +2.6) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +35 (+27.73 to +42.27) | +31.7 (+28.19 to +35.21) | +30.8 (+25.73 to +35.87) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.2% (-18.8 to +21.1) | +6.8% (-14.6 to +28.3) | -0.6% (-11.6 to +10.3) | shown, not judged |
| utilisation (used / allocatable) | +15.5% (+4.5 to +26.5) | +8.8% (+1.4 to +16.3) | +7.4% (+0.5 to +14.4) | shown, not judged |
| CPU used (cores), mean | -0.6% (-3.2 to +2.1) | +0.4% (-0.6 to +1.5) | +0.7% (-0.7 to +2.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01869 (+0.01571 to +0.02167) | +0.01924 (+0.01699 to +0.02149) | +0.0184 (+0.01509 to +0.02171) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.8% (-1.8 to +3.4) | +1.7% (+0.5 to +2.8) | +1.9% (+0.6 to +3.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.2% (-17.8 to -2.6) | -6.0% (-11.8 to -0.3) | -5.3% (-10.2 to -0.3) | shown, not judged |
| HPA replicas, mean | +6.1% (-4.6 to +16.8) | +2.8% (-6.5 to +12.0) | +11.6% (+1.6 to +21.5) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| pods started | +150.0% (-189.3 to +489.3) | +50.0% (-153.0 to +253.0) | +33.3% (-142.6 to +209.3) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +166.7% (-193.2 to +526.5) | +33.3% (-102.0 to +168.7) | -16.7% (-189.4 to +156.1) | **the runs disagree** |
| pod start wait, mean (s) | +433.3% (-117.9 to +984.6) | +166.7% (-36.0 to +369.3) | +25.0% (-171.8 to +221.8) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.6% (+1.9 to +3.4) | +2.6% (+1.8 to +3.4) | +2.4% (+1.3 to +3.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.8% (+0.1 to +1.6) | +1.1% (+0.3 to +1.9) | +0.6% (-0.3 to +1.4) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -26.3% (-43.2 to -9.4) | -15.7% (-28.3 to -3.2) | -11.6% (-22.5 to -0.8) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +18.7% (-11.2 to +48.6) | +0.8% (-31.8 to +33.4) | -4.9% (-12.9 to +3.0) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +62.5% (-21.8 to +146.8) | +15.4% (-60.5 to +91.2) | +14.3% (-18.0 to +46.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | +5.6% (-0.4 to +11.7) | +6.5% (+0.8 to +12.2) | +5.0% (+0.2 to +9.9) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 2 GAIN in all three of our runs, 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 3 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 3 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given (the same way in all three runs; 0 of 3 clear of the noise), 1 power given (the same way in all three runs; 1 of 3 clear of the noise), 3 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.10%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
