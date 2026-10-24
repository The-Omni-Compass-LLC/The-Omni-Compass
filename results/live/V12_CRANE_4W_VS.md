# Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on the organism alone against Crane as shipped (register row 90): the A/B/C three-run table (Omni v12)

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
| A | 39438326588 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39438344234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438362894 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.0% (-0.6 to +0.6) | +0.5% (-0.2 to +1.1) | +0.4% (-0.1 to +1.0) | EVEN, under the floor (every run under 0.5%; the largest 0.46%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.6% (-1.2 to +0.1) | -0.1% (-0.8 to +0.6) | -0.1% (-0.7 to +0.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.6% (-1.2 to +0.1) | -0.1% (-0.8 to +0.6) | -0.1% (-0.7 to +0.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| response time (ms), mean | -4.6% (-6.7 to -2.4) | -3.1% (-5.7 to -0.6) | -4.6% (-6.6 to -2.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -6.4% (-9.9 to -2.8) | -3.0% (-5.7 to -0.3) | -2.7% (-5.4 to +0.0) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 99th percentile | +0.0% (-4.0 to +4.0) | -3.1% (-9.4 to +3.3) | -2.8% (-5.8 to +0.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | +6.2% (-41.2 to +53.5) | -29.7% (-72.7 to +13.4) | -3.8% (-38.4 to +30.9) | **the runs disagree** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0.0% (-238.4 to +238.4) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +2.6 (+0.8414 to +4.359) | +1.2 (+0.2583 to +2.142) | +1.5 (+0.5315 to +2.469) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +175.0% (-6.6 to +356.6) | +246.2% (+43.8 to +448.5) | +152.2% (-3.4 to +307.8) | shown, not judged |
| utilisation (used / allocatable) | -10.0% (-11.5 to -8.5) | -9.8% (-11.7 to -7.9) | -9.2% (-10.4 to -8.1) | shown, not judged |
| CPU used (cores), mean | -10.0% (-11.5 to -8.5) | -9.8% (-11.7 to -7.9) | -9.2% (-10.4 to -8.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00617 (+0.005381 to +0.006959) | +0.00568 (+0.004916 to +0.006444) | +0.00596 (+0.005506 to +0.006414) | shown, not judged |
| CPU used with Omni's own (cores), mean | -9.4% (-10.9 to -7.9) | -9.2% (-11.2 to -7.3) | -8.7% (-9.8 to -7.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +10.6% (+8.6 to +12.6) | +10.3% (+8.2 to +12.3) | +9.5% (+8.4 to +10.7) | shown, not judged |
| HPA replicas, mean | +17.6% (+9.5 to +25.7) | +9.8% (+2.5 to +17.1) | +12.1% (+4.8 to +19.4) | **power given in all three of our runs** |
| pods started | +58.7% (+21.3 to +96.1) | +34.7% (-4.9 to +74.3) | +42.0% (+10.8 to +73.2) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pod start wait, total (s) | +60.3% (+28.4 to +92.2) | +56.1% (+0.6 to +111.6) | +51.9% (+20.4 to +83.4) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | +1.6% (-21.9 to +25.0) | +16.8% (-11.2 to +44.7) | +7.8% (-8.6 to +24.3) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | -11.1% (-12.3 to -9.8) | -10.7% (-12.3 to -9.2) | -10.6% (-11.7 to -9.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 1 GAIN in all three of our runs, 3 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 GAIN (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS in all three of our runs, 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 power given in all three of our runs, 1 power given (the same way in all three runs; 2 of 3 clear of the noise), 1 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.46%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
