# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v10)

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
| A | 39107193417 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115232348 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122532509 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.1% (-0.2 to +0.0) | +0.1% (-0.0 to +0.2) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| node-hours | -0.2% (-0.8 to +0.4) | +0.1% (-0.4 to +0.6) | -0.3% (-0.8 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.32%) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.8 to +0.3) | -0.3% (-0.9 to +0.2) | -0.4% (-0.9 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.43%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.3% (-0.9 to +0.3) | -0.3% (-0.8 to +0.2) | -0.4% (-0.9 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.44%) |
| response time (ms), mean | -33.0% (-50.2 to -15.7) | -32.7% (-57.5 to -7.9) | -40.5% (-70.0 to -11.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -56.4% (-64.0 to -48.8) | -63.2% (-77.5 to -48.9) | -54.0% (-68.3 to -39.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -48.6% (-89.6 to -7.7) | -43.0% (-79.3 to -6.8) | -51.2% (-98.8 to -3.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -26.4% (-43.0 to -9.9) | -31.5% (-48.2 to -14.7) | -26.9% (-41.7 to -12.1) | **GAIN in all three of our runs** |
| failed requests (%) | -8.2% (-18.7 to +2.4) | -14.5% (-23.3 to -5.7) | -15.0% (-27.9 to -2.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -12.5% (-26.2 to +1.2) | -19.7% (-34.1 to -5.3) | -20.3% (-36.2 to -4.5) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +32.5 (+27.06 to +37.94) | +27.7 (+24.36 to +31.04) | +29.4 (+24.85 to +33.95) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +220.1% (+31.0 to +409.3) | -44.9% (-94.8 to +5.1) | -20.2% (-109.6 to +69.3) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-3.5 to +0.0) | -3.7% (-7.1 to -0.3) | -1.2% (-4.0 to +1.6) | shown, not judged |
| CPU used (cores), mean | -1.8% (-3.5 to -0.0) | -3.6% (-7.0 to -0.3) | -1.2% (-4.0 to +1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00972 (+0.008402 to +0.01104) | +0.01012 (+0.009436 to +0.0108) | +0.00935 (+0.008016 to +0.01068) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.2% (-2.9 to +0.5) | -3.1% (-6.4 to +0.3) | -0.6% (-3.4 to +2.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.1% (-0.3 to +2.6) | +3.0% (+0.2 to +5.8) | +0.2% (-3.4 to +3.7) | shown, not judged |
| HPA replicas, mean | +20.4% (+10.5 to +30.3) | +15.1% (+7.1 to +23.0) | +13.6% (+0.5 to +26.7) | **power given in all three of our runs** |
| pods started | +52.0% (+20.2 to +83.8) | -12.0% (-40.8 to +16.8) | +17.3% (-8.2 to +42.8) | **the runs disagree** |
| pod start wait, total (s) | +89.7% (-35.6 to +214.9) | -50.4% (-109.8 to +9.0) | -35.6% (-103.6 to +32.3) | **the runs disagree** |
| pod start wait, mean (s) | +39.6% (-51.6 to +130.7) | -50.5% (-108.3 to +7.2) | -45.8% (-122.7 to +31.0) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -0.5% (-1.8 to +0.8) | -2.8% (-5.4 to -0.2) | -0.5% (-2.7 to +1.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 2 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 power given in all three of our runs, 3 the runs disagree, 2 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.07%), 1 EVEN, under the floor (every run under 0.5%; the largest 0.32%), 1 EVEN, under the floor (every run under 0.5%; the largest 0.43%), 1 EVEN, under the floor (every run under 0.5%; the largest 0.44%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
