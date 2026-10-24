# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on the organism alone against the bin-packing profile as shipped (register row 88): the A/B/C three-run table (Omni v12)

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
| A | 39368428763 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368435483 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368442002 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -12.7% (-24.0 to -1.3) | -16.5% (-29.2 to -3.8) | -13.6% (-24.9 to -2.2) | **GAIN in all three of our runs** |
| node-hours | -12.8% (-24.1 to -1.5) | -16.5% (-29.2 to -3.7) | -13.5% (-24.7 to -2.2) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.3 to +0.2) | +0.0% (-0.4 to +0.4) | +0.1% (-0.4 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -8.8% (-16.6 to -1.0) | -11.4% (-20.5 to -2.4) | -9.3% (-17.2 to -1.5) | **GAIN in all three of our runs** |
| response time (ms), mean | -5.6% (-10.9 to -0.2) | -5.9% (-10.3 to -1.5) | -6.6% (-16.5 to +3.3) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| response time (ms), 95th percentile | -7.7% (-17.5 to +2.0) | +1.7% (-9.5 to +12.9) | +6.0% (-7.3 to +19.3) | **the runs disagree** |
| response time (ms), 99th percentile | -10.2% (-20.5 to +0.1) | -9.8% (-26.1 to +6.5) | -9.3% (-25.4 to +6.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| time over the response line (% of samples) | +21.1% (+5.3 to +36.8) | +37.2% (+12.4 to +61.9) | +29.8% (+1.0 to +58.6) | **LOSS in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +1.9% (-2.4 to +6.1) | +28.3% (-3.0 to +59.6) | +8.9% (-4.7 to +22.4) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | +44 (+30.47 to +57.53) | +55.5 (+41.92 to +69.08) | +47.4 (+31.46 to +63.34) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -4.2% (-24.0 to +15.6) | -5.8% (-21.7 to +10.2) | -10.3% (-33.2 to +12.7) | shown, not judged |
| utilisation (used / allocatable) | +17.4% (+2.0 to +32.8) | +21.3% (+6.3 to +36.2) | +18.5% (+2.7 to +34.2) | shown, not judged |
| CPU used (cores), mean | +1.2% (-1.1 to +3.5) | +0.5% (-2.2 to +3.1) | +0.1% (-2.4 to +2.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01881 (+0.0167 to +0.02092) | +0.01616 (+0.01481 to +0.01751) | +0.01653 (+0.01471 to +0.01835) | shown, not judged |
| CPU used with Omni's own (cores), mean | +2.5% (+0.2 to +4.7) | +1.7% (-1.0 to +4.4) | +1.3% (-1.2 to +3.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -11.0% (-20.7 to -1.3) | -13.1% (-22.1 to -4.0) | -9.9% (-18.4 to -1.5) | shown, not judged |
| HPA replicas, mean | -1.4% (-9.7 to +6.9) | +4.1% (-2.6 to +10.9) | +1.0% (-6.2 to +8.3) | **the runs disagree** |
| pods started | -50.0% (-313.9 to +213.9) | +0.0% (-112.4 to +112.4) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pod start wait, total (s) | -60.0% (-312.8 to +192.8) | +40.0% (-201.3 to +281.3) | +0 (+0 to +0) | **the runs disagree** |
| pod start wait, mean (s) | -20.0% (-325.0 to +285.0) | +0.0% (-223.0 to +223.0) | +0 (+0 to +0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU busy, the real machine under kind (%) | +2.3% (+1.3 to +3.4) | +2.8% (+1.7 to +3.8) | +2.4% (+1.3 to +3.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.4% (-0.7 to +1.4) | +0.6% (-0.2 to +1.4) | +0.8% (-0.2 to +1.7) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| batch: worker machines in service after the queue finished, mean | -22.1% (-39.3 to -5.0) | -28.4% (-49.0 to -7.8) | -24.1% (-42.5 to -5.7) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +53.8% (-124.1 to +231.8) | -43.8% (-116.9 to +29.4) | -52.6% (-96.1 to -9.2) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +33.3% (-142.6 to +209.3) | -50.0% (-163.1 to +63.1) | -50.0% (-130.5 to +30.5) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | +0.7% (-6.2 to +7.7) | +3.3% (-2.8 to +9.3) | +5.0% (-4.9 to +15.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 4 GAIN in all three of our runs, 2 GAIN (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 0 of 3 clear of the noise), 1 GAIN (the same way in all three runs; 2 of 3 clear of the noise), 1 LOSS in all three of our runs, 1 LOSS (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise), 2 LOSS (the same way in all three runs; 0 of 3 clear of the noise), 5 the runs disagree, 4 EVEN, the same, 1 EVEN, under the floor (every run under 0.5%; the largest 0.10%), 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
