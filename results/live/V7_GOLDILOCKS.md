# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v7)

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
| A | 38843260818 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38843263401 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38843266098 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.3% (-0.9 to +0.3) | -0.1% (-0.5 to +0.4) | +0.0% (-0.5 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.29%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.6% (+1.1 to +2.1) | +1.9% (+1.4 to +2.5) | +2.3% (+1.8 to +2.7) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.6% (+1.1 to +2.1) | +1.9% (+1.4 to +2.5) | +2.3% (+1.8 to +2.7) | **power given in all three of our runs** |
| response time (ms), mean | -45.0% (-58.3 to -31.8) | -46.6% (-60.2 to -33.1) | -46.5% (-57.5 to -35.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -60.1% (-72.9 to -47.3) | -61.5% (-73.8 to -49.2) | -61.9% (-74.5 to -49.2) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -67.0% (-78.5 to -55.5) | -67.0% (-80.6 to -53.4) | -68.9% (-81.7 to -56.0) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-175.2 to -24.8) | -100.0% (-174.4 to -25.6) | -100.0% (-163.3 to -36.7) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-206.6 to +6.6) | -100.0% (-216.8 to +16.8) | -100.0% (-165.9 to -34.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +17.8 (+15.4 to +20.2) | +16.6 (+13.7 to +19.5) | +14.1 (+12.77 to +15.43) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.135 (-0.0008654 to +0.2709) | +0.05333 (-0.02709 to +0.1338) | +106.5% (-126.3 to +339.3) | shown, not judged |
| utilisation (used / allocatable) | +41.0% (+31.0 to +51.1) | +43.3% (+31.9 to +54.7) | +46.3% (+36.6 to +56.0) | shown, not judged |
| CPU used (cores), mean | +41.0% (+31.0 to +51.1) | +43.3% (+31.9 to +54.7) | +46.3% (+36.6 to +56.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00796 (+0.006945 to +0.008975) | +0.00774 (+0.006612 to +0.008868) | +0.00839 (+0.007719 to +0.009061) | shown, not judged |
| CPU used with Omni's own (cores), mean | +42.0% (+31.9 to +52.2) | +44.3% (+32.8 to +55.8) | +47.3% (+37.6 to +57.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -26.8% (-30.8 to -22.7) | -27.7% (-32.3 to -23.0) | -29.4% (-33.6 to -25.2) | shown, not judged |
| HPA replicas, mean | +0.6% (-1.8 to +3.0) | +0.5% (-1.5 to +2.5) | +3.4% (+2.2 to +4.6) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| pods started | -27.3% (-83.0 to +28.4) | -38.1% (-97.7 to +21.6) | -88.6% (-106.5 to -70.7) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| pod start wait, total (s) | -10.3% (-70.8 to +50.1) | -34.6% (-109.6 to +40.4) | -88.0% (-116.8 to -59.2) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| pod start wait, mean (s) | +43.1% (-33.5 to +119.8) | -12.4% (-95.6 to +70.9) | -64.7% (-116.5 to -12.9) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +38.1% (+28.8 to +47.3) | +39.3% (+28.5 to +50.1) | +40.6% (+32.8 to +48.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 3 GAIN (the same way in all three runs; 1 of 3 clear of the noise), 2 power given in all three of our runs, 1 power given (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise), 1 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.29%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
