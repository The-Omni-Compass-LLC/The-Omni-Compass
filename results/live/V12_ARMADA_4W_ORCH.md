# Armada on the group of two clusters under the batch stream, the four ways: Armada as shipped against the organism alone (register row 94): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39482335827 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39482351075 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39482365814 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to -0.0) | EVEN, the same |
| node-hours | -0.0% (-0.4 to +0.4) | -0.3% (-0.6 to +0.0) | +0.1% (-0.2 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.30%) |
| energy, parked workers still on at idle power (Wh, declared model) | -4.0% (-5.0 to -3.0) | -4.4% (-5.0 to -3.8) | -3.5% (-4.2 to -2.9) | **GAIN in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -4.0% (-5.0 to -3.0) | -4.4% (-5.0 to -3.8) | -3.5% (-4.2 to -2.9) | **GAIN in all three of our runs** |
| response time (ms), mean | -79.6% (-122.5 to -36.7) | -79.9% (-116.8 to -43.0) | -73.5% (-143.2 to -3.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -93.0% (-143.8 to -42.2) | -93.1% (-135.3 to -50.8) | -90.1% (-177.4 to -2.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -94.2% (-144.9 to -43.6) | -94.5% (-135.3 to -53.7) | -91.8% (-176.5 to -7.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-146.0 to -53.9) | -100.0% (-137.4 to -62.6) | -100.0% (-192.2 to -7.8) | **GAIN in all three of our runs** |
| failed requests (%) | -100.0% (-330.6 to +130.6) | +0 (+0 to +0) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-144.3 to -55.7) | -100.0% (-133.6 to -66.4) | -100.0% (-181.0 to -19.0) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -100.0% (-132.2 to -67.8) | -100.0% (-133.5 to -66.5) | -99.8% (-178.1 to -21.5) | shown, not judged |
| utilisation (used / allocatable) | -82.2% (-96.2 to -68.2) | -82.0% (-91.6 to -72.4) | -82.4% (-93.8 to -71.0) | shown, not judged |
| CPU used (cores), mean | -82.2% (-96.2 to -68.2) | -82.0% (-91.6 to -72.4) | -82.4% (-93.8 to -71.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | -82.2% (-96.2 to -68.2) | -82.0% (-91.6 to -72.4) | -82.4% (-93.8 to -71.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +423.4% (+375.5 to +471.4) | +425.5% (+399.9 to +451.1) | +448.2% (+390.6 to +505.8) | shown, not judged |
| HPA replicas, mean | +2.0% (-4.6 to +8.5) | -0.3% (-3.1 to +2.6) | -0.2% (-5.2 to +4.8) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pods started | +0.0% (-345.9 to +345.9) | -100.0% (-326.2 to +126.2) | +250.0% (-2.9 to +502.9) | **the runs disagree** |
| pod start wait, total (s) | +0.0% (-345.9 to +345.9) | -100.0% (-326.2 to +126.2) | +400.0% (+13.9 to +786.1) | **the runs disagree** |
| pod start wait, mean (s) | +0.0% (-345.9 to +345.9) | -100.0% (-326.2 to +126.2) | +500.0% (-42.0 to +1042.0) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -71.9% (-83.4 to -60.4) | -71.3% (-79.9 to -62.7) | -70.9% (-82.5 to -59.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +72.6% (+62.2 to +83.1) | +68.4% (+58.3 to +78.6) | +86.7% (+75.4 to +98.1) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +1193142.9% (+1189052.7 to +1197233.0) | +1632935.3% (+1629797.0 to +1636073.6) | +1323895.2% (+1320577.4 to +1327213.0) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +221366.7% (+220793.7 to +221939.6) | +245383.3% (+244977.9 to +245788.8) | +245666.7% (+245189.8 to +246143.5) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +529.1% (+479.5 to +578.7) | +469.3% (+425.4 to +513.1) | +904.5% (+823.7 to +985.2) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +24 (+24 to +24) | +24 (+24 to +24) | +24 (+24 to +24) | **LOSS in all three of our runs** |

Readings: 7 GAIN in all three of our runs, 1 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 5 LOSS in all three of our runs, 1 power given (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 3 the runs disagree, 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.30%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
