# Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107196814 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115235566 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122536157 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +9.4% (+1.7 to +17.0) | +6.2% (+1.0 to +11.4) | +13.8% (+6.4 to +21.1) | **GAIN in all three of our runs** |
| node-hours | +9.3% (+1.6 to +17.0) | +6.2% (+1.1 to +11.4) | +13.8% (+6.5 to +21.0) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.3 to +0.6) | =0.0% (−0.2 to +0.3) | =0.0% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.07%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +6.3% (+1.0 to +11.6) | +4.3% (+0.7 to +7.8) | +9.5% (+4.5 to +14.5) | **GAIN in all three of our runs** |
| response time (ms), mean | +9.8% (+7.2 to +12.5) | +12.3% (+9.7 to +14.8) | +11.6% (+7.8 to +15.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +1.7% (−3.1 to +6.4) | +3.5% (−1.0 to +7.9) | +3.8% (−1.0 to +8.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 99th percentile | −1.2% (−7.6 to +5.2) | +0.8% (−3.9 to +5.5) | +2.7% (−1.9 to +7.2) | **the runs disagree** |
| time over the response line (% of samples) | +3.7% (+0.7 to +6.7) | +3.2% (−0.2 to +6.5) | +3.2% (+0.5 to +6.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | +100.0% (−126.2 to +326.2) | =0.0000 (±0.0000 to ±0.0000) | +100.0% (−126.2 to +326.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0% (±0.0 to ±0.0) | −0.9% (−3.1 to +1.2) | =0.0% (±0.0 to ±0.0) | EVEN, under the floor (the three runs' mean 0.31%) |
| settings commands the governor wrote on its own (no person touched either arm) | +11.8 (+11.06 to +12.54) | +11.4 (+10.9 to +11.9) | +11.8 (+10.92 to +12.68) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.0% (-1.7 to +3.7) | +1.8% (+0.5 to +3.0) | -0.3% (-2.6 to +2.0) | shown, not judged |
| utilisation (used / allocatable) | +10.3% (+0.7 to +19.9) | +6.4% (+0.3 to +12.5) | +14.1% (+5.9 to +22.4) | shown, not judged |
| CPU used (cores), mean | -0.3% (-3.1 to +2.6) | -0.5% (-2.8 to +1.8) | -1.7% (-4.4 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02042 (+0.01631 to +0.02453) | +0.02104 (+0.01742 to +0.02466) | +0.02398 (+0.01961 to +0.02835) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.1% (-1.7 to +3.9) | +0.8% (-1.5 to +3.1) | -0.1% (-2.8 to +2.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -6.5% (-13.8 to +0.7) | -3.9% (-8.3 to +0.5) | -8.7% (-14.9 to -2.5) | shown, not judged |
| HPA replicas, mean | +10.0% (−6.2 to +26.2) | +18.7% (+5.2 to +32.2) | +3.5% (−12.8 to +19.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +500.0% (−107.9 to +1107.9) | +0.9000 (+0.3722 to +1.4278) | =0.0% (−337.2 to +337.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −142.4% (−731.5 to +446.7) | −18.0000 (−1.9839 to −34.0161) | =0.0% (−337.2 to +337.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −27.3% (−390.6 to +336.1) | −13.1000 (−1.3938 to −24.8062) | =0.0% (−337.2 to +337.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | +1.5% (+0.9 to +2.2) | +2.0% (+1.0 to +3.0) | +2.0% (+1.3 to +2.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −0.5% (−1.2 to +0.1) | −0.9% (−0.2 to −1.6) | −0.8% (−0.2 to −1.4) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| batch: worker machines in service after the queue finished, mean | +14.6% (+3.5 to +25.7) | +10.4% (+2.1 to +18.8) | +22.2% (+11.1 to +33.3) | **GAIN in all three of our runs** |

Readings: 2 EVEN, the same, 2 EVEN, under the floor, 3 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
