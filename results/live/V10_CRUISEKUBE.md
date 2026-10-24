# CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v10)

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
| A | 39102512170 | `959cb4725a7e` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39113183694 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39120444653 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.2% (-0.8 to +0.4) | +0.2% (-0.5 to +0.8) | +0.5% (-0.0 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.45%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.8 to +0.5) | +0.2% (-0.5 to +0.8) | +0.4% (-0.0 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.45%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.8 to +0.5) | +0.2% (-0.5 to +0.8) | +0.4% (-0.0 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.45%) |
| response time (ms), mean | +1.4% (-0.8 to +3.6) | +0.9% (-0.9 to +2.7) | +1.4% (+0.3 to +2.5) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| response time (ms), 95th percentile | +1.5% (-0.8 to +3.9) | +3.0% (-1.7 to +7.8) | +0.5% (-1.1 to +2.2) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| response time (ms), 99th percentile | +1.3% (-5.2 to +7.9) | +3.1% (-5.1 to +11.2) | +2.7% (+0.0 to +5.3) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| time over the response line (% of samples) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.2% (-148.7 to +151.2) | +712.5% (+30.2 to +1394.8) | -41.6% (-169.2 to +86.0) | shown, not judged |
| utilisation (used / allocatable) | +1.1% (-0.4 to +2.6) | -0.2% (-2.3 to +1.9) | -0.2% (-1.6 to +1.2) | shown, not judged |
| CPU used (cores), mean | +1.1% (-0.4 to +2.6) | -0.2% (-2.3 to +1.9) | -0.2% (-1.6 to +1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00905 (+0.007927 to +0.01017) | +0.00796 (+0.006878 to +0.009042) | +0.00958 (+0.008902 to +0.01026) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.9% (+0.4 to +3.4) | +0.5% (-1.5 to +2.6) | +0.6% (-0.8 to +2.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -1.2% (-2.8 to +0.5) | -0.2% (-2.1 to +1.8) | +0.2% (-1.1 to +1.5) | shown, not judged |
| HPA replicas, mean | -0.2% (-9.1 to +8.6) | +4.3% (-3.6 to +12.2) | +1.9% (-4.3 to +8.0) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pods started | -25.0% (-62.7 to +12.7) | +9.1% (-38.9 to +57.1) | -31.2% (-83.9 to +21.4) | **the runs disagree** |
| pod start wait, total (s) | -44.9% (-143.9 to +54.1) | +105.6% (-89.5 to +300.6) | -25.8% (-121.4 to +69.8) | **the runs disagree** |
| pod start wait, mean (s) | -8.3% (-123.9 to +107.4) | +124.0% (-126.3 to +374.3) | -26.4% (-101.0 to +48.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.1% (+1.2 to +3.0) | +1.9% (+0.7 to +3.1) | +1.2% (-0.1 to +2.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 2 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 1 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 3 the runs disagree, 4 EVEN, the same, 3 EVEN, under the floor (every run under 0.5%; the largest 0.45%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
