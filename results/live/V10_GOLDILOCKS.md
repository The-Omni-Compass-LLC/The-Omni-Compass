# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v10)

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
| A | 39106189778 | `0454fdb0089f` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39113187123 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39120448390 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.4% (-0.9 to +0.2) | +0.3% (-0.1 to +0.6) | -0.1% (-0.6 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.35%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.8% (+1.4 to +2.3) | +2.4% (+1.8 to +2.9) | +1.8% (+1.3 to +2.3) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.8% (+1.4 to +2.3) | +2.4% (+1.8 to +2.9) | +1.8% (+1.3 to +2.3) | **power given in all three of our runs** |
| response time (ms), mean | -46.1% (-59.0 to -33.2) | -47.3% (-60.4 to -34.2) | -46.6% (-59.5 to -33.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -60.1% (-72.7 to -47.6) | -60.1% (-72.2 to -48.0) | -61.3% (-74.0 to -48.6) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -65.3% (-75.5 to -55.0) | -66.2% (-78.8 to -53.6) | -66.5% (-79.3 to -53.6) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-162.2 to -37.8) | -99.1% (-153.4 to -44.7) | -100.0% (-160.9 to -39.1) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-175.4 to -24.6) | -100.0% (-178.7 to -21.3) | -100.0% (-175.4 to -24.6) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +16 (+13.89 to +18.11) | +13.8 (+12.46 to +15.14) | +16.2 (+13.11 to +19.29) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.02667 (-0.03365 to +0.08699) | +326.7% (-178.7 to +832.1) | +0.0% (-337.2 to +337.2) | shown, not judged |
| utilisation (used / allocatable) | +44.9% (+34.3 to +55.6) | +43.7% (+33.6 to +53.7) | +41.1% (+30.5 to +51.7) | shown, not judged |
| CPU used (cores), mean | +44.9% (+34.3 to +55.6) | +43.7% (+33.6 to +53.7) | +41.1% (+30.5 to +51.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00832 (+0.007486 to +0.009154) | +0.00806 (+0.007076 to +0.009044) | +0.00769 (+0.006753 to +0.008627) | shown, not judged |
| CPU used with Omni's own (cores), mean | +46.0% (+35.2 to +56.7) | +44.7% (+34.5 to +54.9) | +42.1% (+31.4 to +52.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -28.5% (-33.0 to -24.0) | -28.1% (-32.6 to -23.6) | -26.7% (-31.2 to -22.3) | shown, not judged |
| HPA replicas, mean | +1.1% (-0.3 to +2.5) | +1.9% (+0.7 to +3.0) | +0.6% (-2.0 to +3.2) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| pods started | -54.5% (-104.9 to -4.2) | -91.3% (-125.5 to -57.1) | -42.9% (-120.6 to +34.9) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| pod start wait, total (s) | -45.5% (-102.6 to +11.7) | -94.7% (-139.3 to -50.2) | -42.9% (-139.8 to +54.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| pod start wait, mean (s) | -19.0% (-75.2 to +37.1) | -93.1% (-131.8 to -54.5) | -35.6% (-98.5 to +27.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +40.9% (+31.9 to +49.9) | +39.7% (+30.6 to +48.8) | +38.0% (+28.4 to +47.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 GAIN in all three of our runs, 2 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 2 power given in all three of our runs, 1 power given (the same way in all three runs; 1 of 3 clear of the noise), 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.35%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
