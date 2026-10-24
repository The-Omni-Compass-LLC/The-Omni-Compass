# Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 94): the A/B/C three-run table (Omni v12)

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
| A | 39482335827 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39482351075 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39482365814 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -10.4% (-24.5 to +3.7) | -6.2% (-15.6 to +3.3) | -24.5% (-38.5 to -10.6) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| node-hours | -10.4% (-24.4 to +3.6) | -6.4% (-15.9 to +3.1) | -24.3% (-38.3 to -10.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.4 to +0.2) | -0.3% (-0.8 to +0.1) | +0.2% (-0.1 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.33%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -7.5% (-17.6 to +2.5) | -4.7% (-11.6 to +2.1) | -17.5% (-27.6 to -7.4) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), mean | -5.0% (-7.2 to -2.9) | -2.2% (-6.9 to +2.6) | -1.5% (-6.8 to +3.7) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 95th percentile | +2.4% (-2.1 to +6.9) | +6.5% (-3.8 to +16.7) | +7.7% (+1.4 to +14.1) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 99th percentile | +3.2% (-1.9 to +8.3) | +6.3% (-5.8 to +18.3) | +9.7% (+3.3 to +16.0) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | -1.1% (-4.1 to +2.0) | +1.7% (-2.6 to +6.1) | +10.7% (+1.7 to +19.7) | **the runs disagree** |
| failed requests (%) | +12.0% (-355.1 to +379.2) | +0 (+0 to +0) | +0 (+0 to +0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +2.8% (-0.4 to +6.0) | +7.7% (-2.4 to +17.7) | +20.6% (+0.0 to +41.2) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +58.22 (+33.72 to +82.73) | +49.2 (+25.32 to +73.08) | +87.9 (+55.37 to +120.4) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +26.4% (-27.5 to +80.3) | +78.5% (-21.2 to +178.1) | +14.1% (-1.1 to +29.3) | shown, not judged |
| utilisation (used / allocatable) | +11.0% (-4.4 to +26.4) | +5.2% (-6.4 to +16.9) | +29.7% (+11.1 to +48.2) | shown, not judged |
| CPU used (cores), mean | -0.8% (-3.3 to +1.8) | -1.6% (-6.9 to +3.7) | -3.5% (-7.1 to +0.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01219 (+0.01103 to +0.01334) | +0.01249 (+0.01167 to +0.01331) | +0.01309 (+0.01213 to +0.01405) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.0% (-2.5 to +2.5) | -0.9% (-6.1 to +4.4) | -2.6% (-6.2 to +1.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -9.7% (-23.8 to +4.4) | -4.4% (-13.3 to +4.4) | -16.7% (-27.2 to -6.1) | shown, not judged |
| HPA replicas, mean | +2.1% (-7.2 to +11.4) | +7.5% (+2.6 to +12.4) | +1.1% (-5.2 to +7.5) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| pods started | +200.0% (+17.7 to +382.3) | +1100.0% (+312.8 to +1887.2) | +200.0% (-219.8 to +619.8) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pod start wait, total (s) | +125.0% (-50.3 to +300.3) | +666.7% (+151.6 to +1181.7) | +233.3% (-257.2 to +723.9) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| pod start wait, mean (s) | +275.0% (-46.0 to +596.0) | +261.1% (+52.5 to +469.8) | +333.3% (-217.3 to +884.0) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.9% (+2.0 to +3.8) | +4.1% (+3.1 to +5.0) | +4.2% (+3.2 to +5.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +1.4% (+0.4 to +2.4) | +2.3% (+1.0 to +3.5) | +1.6% (-0.1 to +3.2) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -16.8% (-38.6 to +5.0) | -10.7% (-26.1 to +4.7) | -40.5% (-61.8 to -19.2) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, mean (s) | -19.0% (-68.8 to +30.7) | +64.7% (+18.4 to +111.0) | -47.6% (-122.9 to +27.7) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +16.7% (-21.8 to +55.1) | +50.0% (-7.6 to +107.6) | -66.7% (-128.2 to -5.1) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | +5.1% (+1.9 to +8.3) | +8.9% (+4.9 to +12.9) | +9.1% (+0.9 to +17.3) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 1 LOSS in all three of our runs, 1 LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 5 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given (the same way in all three runs; 1 of 3 clear of the noise), 1 power given (the same way in all three runs; 2 of 3 clear of the noise), 3 the runs disagree, 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.33%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
