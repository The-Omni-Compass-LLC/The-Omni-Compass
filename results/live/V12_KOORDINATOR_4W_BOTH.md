# Koordinator under the batch stream, the four ways: Omni-Compass on top of Koordinator against the organism alone (register row 89): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -2.5% (-6.2 to +1.1) | -0.4% (-1.2 to +0.3) | -1.4% (-4.6 to +1.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| node-hours | -2.4% (-6.2 to +1.4) | -0.2% (-0.9 to +0.5) | -1.4% (-4.6 to +1.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.6% (+0.2 to +1.1) | +0.0% (-0.8 to +0.8) | +0.1% (-0.4 to +0.7) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.1% (-3.7 to +1.4) | -0.3% (-1.0 to +0.4) | -0.9% (-3.1 to +1.4) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| response time (ms), mean | -56.0% (-88.7 to -23.2) | -72.2% (-111.7 to -32.6) | -62.8% (-92.6 to -32.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -66.9% (-111.9 to -21.9) | -82.8% (-133.7 to -31.8) | -74.4% (-117.2 to -31.5) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -64.2% (-105.2 to -23.2) | -82.3% (-131.4 to -33.1) | -73.0% (-114.6 to -31.3) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -98.5% (-198.8 to +1.8) | -98.4% (-157.8 to -39.1) | -98.4% (-154.5 to -42.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-182.2 to -17.8) | -97.7% (-151.9 to -43.5) | -98.9% (-138.1 to -59.7) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +14.2 (+11.13 to +17.27) | +12.5 (+10.84 to +14.16) | +11.4 (+8.555 to +14.25) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +10306.6% (+6365.4 to +14247.8) | +11253.2% (+8243.7 to +14262.8) | +11685.6% (+8482.7 to +14888.5) | shown, not judged |
| utilisation (used / allocatable) | +13.2% (+1.9 to +24.6) | -1.4% (-12.3 to +9.4) | +4.3% (-4.3 to +13.0) | shown, not judged |
| CPU used (cores), mean | +10.7% (+1.4 to +19.9) | -1.8% (-12.4 to +8.7) | +3.1% (-5.1 to +11.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01124 (+0.01006 to +0.01242) | +0.01219 (+0.01113 to +0.01325) | +0.01196 (+0.01105 to +0.01287) | shown, not judged |
| CPU used with Omni's own (cores), mean | +11.6% (+2.4 to +20.8) | -1.0% (-11.5 to +9.5) | +4.0% (-4.1 to +12.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -13.7% (-25.7 to -1.7) | -1.1% (-11.6 to +9.5) | -5.1% (-13.0 to +2.8) | shown, not judged |
| HPA replicas, mean | -3.7% (-9.3 to +1.8) | +0.3% (-9.0 to +9.6) | -1.4% (-11.7 to +8.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pods started | +100.0% (-126.2 to +326.2) | +0.3 (-0.04553 to +0.6455) | +0.0% (-337.2 to +337.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | +50.0% (-63.1 to +163.1) | +0.7 (-0.1294 to +1.529) | +0.0% (-337.2 to +337.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pod start wait, mean (s) | -25.0% (-81.5 to +31.5) | +0.7 (-0.1294 to +1.529) | +0.0% (-337.2 to +337.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +19.0% (+13.1 to +24.8) | +8.4% (+0.3 to +16.5) | +13.4% (+7.4 to +19.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +79.6% (+57.4 to +101.8) | +82.5% (+72.2 to +92.7) | +90.2% (+71.9 to +108.5) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -9.7% (-23.5 to +4.1) | -6.2% (-23.8 to +11.3) | -11.0% (-58.2 to +36.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: job wait, submitted to its first pod running, mean (s) | +332575.0% (+204178.2 to +460971.8) | +701433.3% (+502619.2 to +900247.5) | +227980.0% (+149811.1 to +306148.9) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +172733.3% (+104746.8 to +240719.9) | +763800.0% (+530043.0 to +997557.0) | +136780.0% (+86044.3 to +187515.7) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +1607.8% (+1081.3 to +2134.4) | +849.4% (+675.6 to +1023.2) | +1322.9% (+1027.8 to +1618.1) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +5.3 (-0.8906 to +11.49) | +10.7 (+4.049 to +17.35) | +8.8 (+3.261 to +14.34) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |

Readings: 4 GAIN in all three of our runs, 4 GAIN (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 4 LOSS in all three of our runs, 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 LOSS (the same way in all three runs; 2 of 3 clear of the noise), 1 power given (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise), 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 1 the runs disagree, 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
