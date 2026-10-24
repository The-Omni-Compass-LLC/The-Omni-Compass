# Volcano under the batch stream, the four ways: Volcano as shipped against the organism alone (register row 63): the A/B/C three-run table (Omni v12)

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
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.0% (-0.4 to +0.3) | -0.0% (-0.3 to +0.3) | -0.2% (-0.6 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.25%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.0% (-0.4 to +0.3) | -0.0% (-0.3 to +0.3) | -0.2% (-0.6 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.21%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.0% (-0.4 to +0.3) | -0.0% (-0.3 to +0.3) | -0.2% (-0.6 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.21%) |
| response time (ms), mean | -26.5% (-40.6 to -12.3) | -20.8% (-37.6 to -3.9) | -19.2% (-28.9 to -9.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -44.1% (-67.9 to -20.4) | -22.0% (-39.2 to -4.7) | -28.8% (-42.9 to -14.6) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -36.7% (-58.6 to -14.9) | -9.1% (-28.3 to +10.1) | -10.6% (-29.5 to +8.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | -56.5% (-90.7 to -22.3) | -36.4% (-70.5 to -2.4) | -37.8% (-61.6 to -14.1) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -12.6% (-20.8 to -4.5) | -10.1% (-21.3 to +1.0) | -20.7% (-44.8 to +3.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +36.1% (+9.1 to +63.2) | +67.1% (+34.2 to +100.0) | +48.4% (+36.7 to +60.0) | shown, not judged |
| utilisation (used / allocatable) | +0.2% (-0.8 to +1.2) | +0.3% (-1.3 to +2.0) | +0.2% (-1.2 to +1.7) | shown, not judged |
| CPU used (cores), mean | +0.2% (-0.8 to +1.2) | +0.3% (-1.3 to +2.0) | +0.2% (-1.2 to +1.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.2% (-0.8 to +1.2) | +0.3% (-1.3 to +2.0) | +0.2% (-1.2 to +1.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.2% (-1.2 to +0.8) | -0.3% (-2.1 to +1.5) | +0.2% (-1.3 to +1.7) | shown, not judged |
| HPA replicas, mean | +1.9% (-6.8 to +10.7) | -0.6% (-8.5 to +7.4) | +3.8% (-1.1 to +8.6) | **the runs disagree** |
| pods started | -50.0% (-313.9 to +213.9) | -50.0% (-313.9 to +213.9) | -100.0% (-326.2 to +126.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -50.0% (-313.9 to +213.9) | -66.7% (-312.9 to +179.6) | -100.0% (-326.2 to +126.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | +0.0% (-337.2 to +337.2) | -33.3% (-318.8 to +252.1) | -100.0% (-326.2 to +126.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.5% (+1.9 to +3.1) | +3.0% (+2.4 to +3.6) | +2.5% (+1.8 to +3.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +1.2% (+0.6 to +1.8) | +1.4% (+0.4 to +2.5) | +1.4% (+0.3 to +2.6) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | +1053.3% (+883.9 to +1222.8) | +866.7% (+664.7 to +1068.6) | +1491.7% (+1085.0 to +1898.3) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +366.7% (+231.3 to +502.0) | +275.0% (+78.2 to +471.8) | +500.0% (+331.4 to +668.6) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +24.2% (+10.9 to +37.5) | +17.6% (+5.6 to +29.5) | +23.2% (+6.9 to +39.4) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 3 GAIN in all three of our runs, 1 GAIN (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 4 LOSS in all three of our runs, 1 the runs disagree, 6 EVEN, the same, 2 EVEN, under the floor (every run under 0.5%; the largest 0.21%), 1 EVEN, under the floor (every run under 0.5%; the largest 0.25%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
