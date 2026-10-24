# Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against Open Cluster Management as shipped (register row 96): the A/B/C three-run table (Omni v12)

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
| A | 39479807336 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39479824367 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39479840381 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -5.5% (-10.7 to -0.4) | -9.9% (-22.6 to +2.7) | -15.9% (-30.0 to -1.7) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| node-hours | -5.6% (-10.7 to -0.5) | -10.0% (-22.7 to +2.7) | -15.8% (-30.2 to -1.3) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.3) | -0.3% (-0.6 to +0.1) | +0.6% (-0.7 to +2.0) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -4.1% (-7.8 to -0.5) | -7.4% (-16.4 to +1.7) | -10.8% (-21.7 to +0.2) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), mean | -32.0% (-44.8 to -19.1) | -38.3% (-53.9 to -22.8) | -19.0% (-60.4 to +22.4) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 95th percentile | -24.8% (-37.9 to -11.7) | -32.0% (-47.3 to -16.7) | -7.3% (-54.6 to +40.0) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 99th percentile | -21.8% (-34.6 to -9.0) | -29.1% (-42.5 to -15.8) | -7.0% (-55.3 to +41.3) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| time over the response line (% of samples) | -27.0% (-35.7 to -18.3) | -22.2% (-32.9 to -11.4) | -13.0% (-57.3 to +31.4) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| failed requests (%) | -89.1% (-257.7 to +79.5) | -100.0% (-252.6 to +52.6) | -100.0% (-326.2 to +126.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -13.1% (-17.4 to -8.8) | -14.2% (-20.4 to -8.0) | -7.4% (-50.0 to +35.1) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +51 (+36.12 to +65.88) | +56.2 (+28.28 to +84.12) | +63.9 (+38.85 to +88.95) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -40.4% (-95.4 to +14.6) | -46.3% (-128.2 to +35.5) | -53.2% (-134.3 to +27.8) | shown, not judged |
| utilisation (used / allocatable) | +2.2% (-5.1 to +9.6) | +6.4% (-9.5 to +22.4) | +33.7% (+7.0 to +60.4) | shown, not judged |
| CPU used (cores), mean | -3.1% (-9.0 to +2.8) | -4.9% (-10.9 to +1.2) | +11.1% (-16.2 to +38.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0124 (+0.01164 to +0.01316) | +0.01182 (+0.01146 to +0.01218) | +0.01275 (+0.01191 to +0.01359) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.4% (-8.3 to +3.5) | -4.2% (-10.3 to +1.9) | +12.0% (-15.4 to +39.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -1.3% (-7.6 to +5.0) | -4.7% (-17.6 to +8.3) | -36.0% (-93.7 to +21.6) | shown, not judged |
| HPA replicas, mean | +10.4% (+3.8 to +17.0) | +10.1% (+1.6 to +18.5) | +3.9% (-2.2 to +10.0) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pods started | +1000.0% (+416.0 to +1584.0) | +1.5 (+0.8048 to +2.195) | +1 (+0.3256 to +1.674) | **power given in all three of our runs** |
| pod start wait, total (s) | +466.7% (+186.8 to +746.5) | +2.4 (+0.9225 to +3.878) | +1.3 (+0.4047 to +2.195) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | +266.7% (+26.9 to +506.4) | +1.25 (+0.6136 to +1.886) | +0.8 (+0.2615 to +1.338) | **LOSS in all three of our runs** |
| host CPU busy, the real machine under kind (%) | -8.9% (-11.4 to -6.4) | -10.4% (-14.0 to -6.8) | -0.6% (-21.8 to +20.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | -11.1% (-15.3 to -6.8) | -12.5% (-17.6 to -7.4) | -13.0% (-22.1 to -3.8) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -11.3% (-21.6 to -1.1) | -16.4% (-35.7 to +2.8) | -29.3% (-54.4 to -4.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, mean (s) | -98.2% (-267.2 to +70.9) | -98.8% (-191.5 to -6.1) | -98.1% (-251.6 to +55.5) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | -98.5% (-261.3 to +64.4) | -99.1% (-200.7 to +2.5) | -94.7% (-259.7 to +70.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job turnaround, submitted to done, mean (s) | -28.0% (-40.0 to -15.9) | -33.2% (-47.4 to -18.9) | -31.6% (-50.7 to -12.5) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 2 GAIN in all three of our runs, 2 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 2 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 8 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 2 LOSS in all three of our runs, 1 power given in all three of our runs, 1 power given (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 power given (the same way in all three runs; 2 of 3 clear of the noise), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
