# Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1): the A/B/C three-run table (Omni v10)

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
| A | 39107183748 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39114211206 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122521784 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.2% (-0.3 to -0.0) | -0.0% (-0.3 to +0.2) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.19%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.4% (-0.5 to -0.3) | -0.3% (-0.5 to -0.1) | -0.4% (-0.6 to -0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.42%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.4% (-0.5 to -0.3) | -0.3% (-0.5 to -0.1) | -0.4% (-0.6 to -0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.42%) |
| response time (ms), mean | -45.1% (-54.3 to -36.0) | -45.5% (-52.7 to -38.4) | -50.1% (-76.8 to -23.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -57.2% (-67.4 to -46.9) | -59.0% (-64.2 to -53.8) | -65.5% (-116.3 to -14.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -43.0% (-71.1 to -14.8) | -34.4% (-58.0 to -10.8) | -45.6% (-75.8 to -15.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -38.2% (-48.0 to -28.3) | -38.2% (-42.3 to -34.1) | -44.9% (-74.1 to -15.7) | **GAIN in all three of our runs** |
| failed requests (%) | -11.6% (-16.7 to -6.6) | -12.2% (-16.7 to -7.7) | -21.0% (-48.0 to +6.0) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -24.1% (-33.2 to -15.0) | -20.7% (-25.9 to -15.5) | -31.8% (-44.7 to -18.8) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +43.4 (+35.07 to +51.73) | +47.6 (+39.44 to +55.76) | +37.5 (+27.96 to +47.04) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +85.2% (-44.6 to +214.9) | -34.1% (-99.5 to +31.4) | +11.7% (-51.0 to +74.4) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-2.0 to -1.4) | -1.9% (-2.5 to -1.4) | -2.5% (-4.5 to -0.6) | shown, not judged |
| CPU used (cores), mean | -1.7% (-2.0 to -1.4) | -1.9% (-2.5 to -1.4) | -2.5% (-4.5 to -0.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0095 (+0.008263 to +0.01074) | +0.00971 (+0.009031 to +0.01039) | +0.00804 (+0.006495 to +0.009585) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.3% (-1.6 to -1.0) | -1.6% (-2.1 to -1.0) | -2.1% (-4.0 to -0.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.8% (+0.8 to +2.7) | +1.6% (+1.2 to +2.1) | +1.8% (+0.2 to +3.4) | shown, not judged |
| HPA replicas, mean | +5.0% (-0.1 to +10.0) | +8.2% (+0.3 to +16.1) | -0.9% (-6.4 to +4.5) | **the runs disagree** |
| pods started | +47.5% (-8.7 to +103.7) | +22.5% (-48.8 to +93.8) | +20.4% (-13.3 to +54.1) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +32.8% (-23.9 to +89.4) | +4.5% (-82.1 to +91.1) | +14.7% (-27.6 to +57.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -2.2% (-29.7 to +25.3) | -32.0% (-71.1 to +7.0) | +0.7% (-27.8 to +29.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -1.4% (-1.7 to -1.0) | -1.4% (-1.9 to -0.9) | -1.7% (-3.3 to +0.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 GAIN in all three of our runs, 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 1 power given (the same way in all three runs; 0 of 3 clear of the noise), 2 the runs disagree, 3 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.19%), 2 EVEN, under the floor (every run under 0.5%; the largest 0.42%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
