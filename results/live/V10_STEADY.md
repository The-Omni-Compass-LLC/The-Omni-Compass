# Steady load: the same fixed-rate work sent to both arms: the A/B/C three-run table (Omni v10)

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
| A | 39107180703 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39114207589 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39121472594 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.0% (-0.1 to +0.1) | -0.1% (-0.4 to +0.2) | +0.2% (-0.2 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.4 to -0.0) | -0.5% (-0.8 to -0.1) | -0.1% (-0.6 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.45%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.2% (-0.4 to -0.0) | -0.5% (-0.8 to -0.1) | -0.1% (-0.6 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.45%) |
| response time (ms), mean | -48.2% (-62.7 to -33.6) | -48.8% (-59.1 to -38.6) | -48.5% (-66.0 to -30.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -64.7% (-82.0 to -47.4) | -64.3% (-76.3 to -52.3) | -65.2% (-86.1 to -44.4) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -72.6% (-93.8 to -51.4) | -68.8% (-87.3 to -50.2) | -69.8% (-91.1 to -48.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -99.5% (-158.1 to -40.8) | -98.4% (-134.7 to -62.1) | -100.0% (-160.6 to -39.4) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-160.9 to -39.1) | -100.0% (-141.4 to -58.6) | -100.0% (-163.1 to -36.9) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +18.6 (+15.45 to +21.75) | +18.8 (+15.5 to +22.1) | +18.3 (+15.82 to +20.78) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -22.5% (-85.5 to +40.4) | -11.9% (-76.5 to +52.7) | +47.5% (-62.2 to +157.2) | shown, not judged |
| utilisation (used / allocatable) | -5.2% (-7.8 to -2.6) | -6.1% (-7.9 to -4.3) | -5.4% (-8.3 to -2.4) | shown, not judged |
| CPU used (cores), mean | -5.2% (-7.8 to -2.6) | -6.1% (-7.9 to -4.3) | -5.4% (-8.3 to -2.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00807 (+0.006859 to +0.009281) | +0.00866 (+0.007512 to +0.009808) | +0.00787 (+0.006607 to +0.009133) | shown, not judged |
| CPU used with Omni's own (cores), mean | -4.3% (-6.8 to -1.8) | -5.2% (-7.0 to -3.5) | -4.5% (-7.4 to -1.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +4.4% (+2.7 to +6.1) | +6.2% (+3.8 to +8.6) | +4.1% (+2.4 to +5.8) | shown, not judged |
| HPA replicas, mean | -6.7% (-12.8 to -0.7) | -5.9% (-12.5 to +0.6) | -2.5% (-5.8 to +0.7) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| pods started | -27.7% (-59.8 to +4.5) | -16.7% (-52.0 to +18.6) | -17.0% (-41.7 to +7.6) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -29.3% (-86.9 to +28.4) | -9.1% (-51.9 to +33.7) | -2.1% (-51.2 to +46.9) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -11.8% (-56.3 to +32.7) | +13.1% (-37.6 to +63.8) | +5.0% (-34.8 to +44.8) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -3.7% (-5.8 to -1.7) | -4.2% (-5.6 to -2.7) | -3.8% (-5.9 to -1.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 GAIN in all three of our runs, 2 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 1 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.15%), 2 EVEN, under the floor (every run under 0.5%; the largest 0.45%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
