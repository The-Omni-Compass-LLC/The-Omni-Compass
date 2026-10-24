# Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Open Cluster Management against Open Cluster Management as shipped (register row 96): the A/B/C three-run table (Omni v12)

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
| A | 39479807336 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39479824367 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39479840381 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -1.9% (-4.1 to +0.3) | -7.4% (-18.5 to +3.8) | -7.1% (-13.7 to -0.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| node-hours | -2.1% (-4.3 to +0.2) | -7.5% (-18.6 to +3.6) | -7.2% (-13.9 to -0.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.0% (-0.7 to +0.7) | +0.1% (-0.3 to +0.5) | +0.8% (+0.0 to +1.7) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.4% (-3.1 to +0.3) | -5.2% (-13.3 to +2.9) | -4.3% (-9.4 to +0.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| response time (ms), mean | +11.4% (-0.3 to +23.1) | -3.0% (-16.3 to +10.2) | +37.2% (+0.3 to +74.0) | **the runs disagree** |
| response time (ms), 95th percentile | +9.2% (-1.6 to +20.0) | +1.6% (-12.0 to +15.2) | +41.2% (+1.6 to +80.7) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 99th percentile | +11.2% (-2.0 to +24.3) | +6.9% (-7.7 to +21.4) | +38.0% (+0.1 to +76.0) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | +12.6% (-2.4 to +27.6) | -2.1% (-5.9 to +1.6) | +49.2% (+0.1 to +98.3) | **the runs disagree** |
| failed requests (%) | +39.5% (-46.7 to +125.8) | +123.7% (-203.3 to +450.7) | +207.5% (-260.7 to +675.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +5.7% (+1.4 to +10.0) | +6.1% (+0.8 to +11.4) | +45.5% (+5.7 to +85.2) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +48 (+41.77 to +54.23) | +57.4 (+34.35 to +80.45) | +43.8 (+33.04 to +54.56) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +15.5% (-89.1 to +120.2) | -19.7% (-76.5 to +37.1) | -9.0% (-144.7 to +126.6) | shown, not judged |
| utilisation (used / allocatable) | +4.4% (-8.0 to +16.8) | +12.3% (+2.7 to +21.9) | +29.1% (+13.7 to +44.5) | shown, not judged |
| CPU used (cores), mean | +2.5% (-9.4 to +14.4) | +4.4% (+0.9 to +7.8) | +20.1% (+4.0 to +36.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01277 (+0.01157 to +0.01397) | +0.01242 (+0.01188 to +0.01296) | +0.01188 (+0.01116 to +0.0126) | shown, not judged |
| CPU used with Omni's own (cores), mean | +3.2% (-8.6 to +15.1) | +5.1% (+1.6 to +8.5) | +20.9% (+4.8 to +37.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -3.5% (-14.7 to +7.7) | -10.2% (-18.9 to -1.5) | -36.0% (-88.8 to +16.8) | shown, not judged |
| HPA replicas, mean | +19.6% (-3.9 to +43.0) | +10.2% (+2.2 to +18.3) | +3.7% (-1.4 to +8.8) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| pods started | +1100.0% (+388.7 to +1811.3) | +1.4 (+0.7089 to +2.091) | +1.5 (+0.657 to +2.343) | **power given in all three of our runs** |
| pod start wait, total (s) | +866.7% (+127.9 to +1605.4) | +2.9 (+1.101 to +4.699) | +5 (-0.4892 to +10.49) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| pod start wait, mean (s) | +416.7% (+69.1 to +764.2) | +1.617 (+0.8358 to +2.398) | +2.467 (-0.2772 to +5.211) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +5.6% (+3.0 to +8.2) | +3.8% (+2.8 to +4.9) | +16.3% (-4.6 to +37.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +5.5% (+2.2 to +8.9) | +3.0% (+1.0 to +5.0) | +2.6% (-4.4 to +9.5) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -4.6% (-9.6 to +0.3) | -10.8% (-27.2 to +5.6) | -17.4% (-33.2 to -1.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, mean (s) | +210.8% (-13.9 to +435.5) | +168.7% (-49.3 to +386.7) | +358.1% (-20.3 to +736.6) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +304.8% (-8.1 to +617.8) | +88.9% (-32.2 to +210.0) | +1389.5% (-119.4 to +2898.4) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | +15.6% (+2.8 to +28.4) | +6.9% (-5.0 to +18.7) | +19.6% (+8.1 to +31.0) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 3 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 1 LOSS in all three of our runs, 3 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 4 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given in all three of our runs, 1 power given (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise), 1 power given (the same way in all three runs; 1 of 3 clear of the noise), 2 the runs disagree, 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
