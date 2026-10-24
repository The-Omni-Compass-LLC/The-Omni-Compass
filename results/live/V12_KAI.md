# The KAI scheduler under the batch stream: Omni-Compass on top of KAI's queues (register row 91): the A/B/C three-run table (Omni v12)

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
| A | 39350900880 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39350907916 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39350915166 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -16.2% (-24.1 to -8.3) | -14.7% (-24.2 to -5.1) | -11.1% (-20.8 to -1.5) | **GAIN in all three of our runs** |
| node-hours | -16.2% (-24.1 to -8.2) | -14.4% (-24.0 to -4.9) | -11.1% (-20.9 to -1.2) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.6 to +0.3) | +0.0% (-0.4 to +0.5) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -11.3% (-17.0 to -5.7) | -10.1% (-16.9 to -3.4) | -7.5% (-14.2 to -0.8) | **GAIN in all three of our runs** |
| response time (ms), mean | -22.9% (-26.7 to -19.1) | -20.6% (-25.2 to -16.1) | -21.5% (-27.9 to -15.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -1.3% (-5.7 to +3.1) | +9.9% (-5.7 to +25.4) | +0.1% (-16.7 to +16.9) | **the runs disagree** |
| response time (ms), 99th percentile | +0.7% (-3.4 to +4.7) | +9.7% (-2.4 to +21.7) | +5.7% (-11.8 to +23.3) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | +8.8% (-24.7 to +42.4) | +42.3% (-9.2 to +93.8) | +6.5% (-47.1 to +60.1) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +28.6% (-74.2 to +131.3) | +61.1% (-21.5 to +143.7) | +0.0% (-46.2 to +46.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +22.1 (+15.15 to +29.05) | +26.2 (+17.28 to +35.12) | +24.4 (+17.59 to +31.21) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +13.0% (+1.5 to +24.6) | -7.2% (-26.4 to +12.0) | +11.6% (-6.5 to +29.7) | shown, not judged |
| utilisation (used / allocatable) | +15.8% (+7.4 to +24.3) | +12.1% (+2.9 to +21.4) | +14.0% (-1.1 to +29.0) | shown, not judged |
| CPU used (cores), mean | -3.3% (-5.7 to -1.0) | -4.1% (-8.3 to +0.0) | +0.1% (-2.3 to +2.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02092 (+0.01957 to +0.02227) | +0.02089 (+0.01478 to +0.027) | +0.01945 (+0.01805 to +0.02085) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.9% (-4.3 to +0.5) | -2.7% (-6.6 to +1.2) | +1.4% (-1.0 to +3.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -8.5% (-13.5 to -3.5) | -7.1% (-13.8 to -0.4) | -8.8% (-18.6 to +1.0) | shown, not judged |
| HPA replicas, mean | -2.9% (-9.6 to +3.9) | +11.5% (-0.1 to +23.2) | +6.8% (-1.9 to +15.5) | **the runs disagree** |
| pods started | +0.2 (-0.1016 to +0.5016) | -100.0% (-260.9 to +60.9) | +0.0% (-292.0 to +292.0) | **the runs disagree** |
| pod start wait, total (s) | +0.5 (-0.2726 to +1.273) | -100.0% (-260.9 to +60.9) | -25.0% (-297.5 to +247.5) | **the runs disagree** |
| pod start wait, mean (s) | +0.5 (-0.2726 to +1.273) | -100.0% (-250.8 to +50.8) | +50.0% (-305.7 to +405.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.8% (+1.8 to +3.8) | +1.6% (-0.2 to +3.3) | +1.3% (+0.4 to +2.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.4% (+0.1 to +0.7) | +0.4% (+0.1 to +0.8) | +0.2% (-0.1 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.44%) |
| batch: worker machines in service after the queue finished, mean | -30.4% (-44.8 to -16.0) | -27.7% (-45.6 to -9.8) | -20.4% (-37.2 to -3.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -2.6% (-11.4 to +6.2) | -0.7% (-8.6 to +7.3) | +2.6% (-5.7 to +11.0) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +20.0% (-10.2 to +50.2) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | +1.5% (+0.4 to +2.5) | +5.3% (-2.4 to +13.1) | +2.2% (-5.4 to +9.9) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN in all three of our runs, 1 LOSS (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 6 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.14%), 1 EVEN, under the floor (every run under 0.5%; the largest 0.44%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
