# Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 95): the A/B/C three-run table (Omni v12)

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
| A | 39438525862 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438541616 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438559009 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -9.1% (-19.2 to +0.9) | -12.4% (-24.8 to +0.0) | -16.6% (-31.8 to -1.4) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| node-hours | -9.1% (-19.1 to +0.9) | -12.6% (-24.9 to -0.3) | -16.3% (-31.6 to -0.9) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.2% (-0.1 to +0.5) | -0.1% (-0.4 to +0.2) | +0.2% (-0.1 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.21%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -6.4% (-13.6 to +0.8) | -9.0% (-17.9 to -0.2) | -11.7% (-22.7 to -0.7) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), mean | +1.5% (-2.6 to +5.6) | -5.0% (-9.0 to -0.9) | -3.5% (-7.7 to +0.7) | **the runs disagree** |
| response time (ms), 95th percentile | +12.7% (+5.9 to +19.5) | +4.6% (-3.6 to +12.9) | +4.0% (-2.0 to +10.0) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 99th percentile | +15.0% (+3.5 to +26.5) | +7.4% (-0.4 to +15.3) | +5.7% (-5.3 to +16.8) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | +6.7% (-0.5 to +14.0) | -1.3% (-9.9 to +7.4) | +2.5% (-1.6 to +6.7) | **the runs disagree** |
| failed requests (%) | -100.0% (-330.6 to +130.6) | +0 (+0 to +0) | +42.8% (-153.3 to +239.0) | **the runs disagree** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +14.7% (-2.6 to +32.0) | +8.8% (-2.7 to +20.4) | +4.8% (+1.2 to +8.4) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +68.22 (+39.17 to +97.28) | +64.7 (+36.32 to +93.08) | +74.1 (+40.94 to +107.3) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +9.5% (-13.8 to +32.9) | +3.5% (-10.6 to +17.5) | +56.4% (-15.5 to +128.3) | shown, not judged |
| utilisation (used / allocatable) | +12.4% (+0.4 to +24.5) | +15.0% (+0.5 to +29.4) | +15.3% (-3.6 to +34.1) | shown, not judged |
| CPU used (cores), mean | +1.7% (-1.0 to +4.5) | -0.3% (-2.7 to +2.2) | -4.8% (-10.1 to +0.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0133 (+0.01188 to +0.01472) | +0.01306 (+0.01216 to +0.01396) | +0.01268 (+0.01201 to +0.01335) | shown, not judged |
| CPU used with Omni's own (cores), mean | +2.5% (-0.2 to +5.3) | +0.5% (-2.0 to +3.0) | -4.1% (-9.4 to +1.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -8.8% (-16.7 to -0.9) | -9.9% (-19.1 to -0.8) | -10.1% (-23.0 to +2.9) | shown, not judged |
| HPA replicas, mean | +14.1% (+8.1 to +20.1) | +6.6% (+0.7 to +12.5) | +5.6% (-0.7 to +11.9) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pods started | +450.0% (+26.4 to +873.6) | +0.8 (+0.2358 to +1.364) | +0.8 (+0.2358 to +1.364) | **power given in all three of our runs** |
| pod start wait, total (s) | +300.0% (-72.5 to +672.5) | +1.2 (+0.3879 to +2.012) | +1.9 (-0.1077 to +3.908) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| pod start wait, mean (s) | +150.0% (-99.4 to +399.4) | +0.95 (+0.3091 to +1.591) | +1.25 (+0.221 to +2.279) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +4.3% (+2.9 to +5.8) | +3.4% (+2.4 to +4.5) | +3.6% (+2.1 to +5.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +2.7% (+1.0 to +4.5) | +1.2% (-0.1 to +2.6) | +2.0% (+0.7 to +3.3) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -17.3% (-35.2 to +0.6) | -20.9% (-39.6 to -2.2) | -26.2% (-49.8 to -2.5) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, mean (s) | +37.5% (-30.9 to +105.9) | +4.0% (-58.5 to +66.5) | +14.3% (-43.7 to +72.3) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +20.0% (-63.1 to +103.1) | +33.3% (-16.9 to +83.6) | +0.0% (+0.0 to +0.0) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | +11.6% (+4.9 to +18.2) | +2.2% (-1.7 to +6.0) | +5.8% (+1.3 to +10.4) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 1 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 3 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 4 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 3 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given in all three of our runs, 1 power given (the same way in all three runs; 2 of 3 clear of the noise), 3 the runs disagree, 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.21%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
