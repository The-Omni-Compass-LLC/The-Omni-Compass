# Koordinator under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 89): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +22.8% (+11.5 to +34.0) | +17.5% (+3.6 to +31.4) | +14.6% (+6.8 to +22.4) | **GAIN in all three of our runs** |
| node-hours | +22.7% (+11.3 to +34.0) | +17.4% (+3.4 to +31.3) | +14.5% (+6.4 to +22.5) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.1 to +0.5) | =0.2% (−0.1 to +0.5) | =0.2% (−0.1 to +0.5) | EVEN, under the floor (the three runs' mean 0.20%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +15.8% (+7.9 to +23.7) | +11.9% (+2.2 to +21.6) | +10.0% (+4.3 to +15.6) | **GAIN in all three of our runs** |
| response time (ms), mean | +15.2% (+8.7 to +21.6) | +8.3% (+2.5 to +14.0) | +12.9% (+9.8 to +16.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | −5.8% (−1.6 to −9.9) | −6.9% (−15.1 to +1.2) | −5.8% (−12.8 to +1.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 99th percentile | −6.6% (−17.9 to +4.7) | −7.3% (−16.1 to +1.6) | −3.6% (−8.4 to +1.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +2.3% (−6.0 to +10.7) | +2.0% (−2.1 to +6.0) | +1.1% (−4.9 to +7.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +3.9% (−7.1 to +15.0) | −3.4% (−10.2 to +3.3) | −3.2% (−10.5 to +4.1) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +64 (+51.18 to +76.82) | +41.3 (+25.47 to +57.13) | +41.2 (+29.17 to +53.23) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +11.1% (-6.2 to +28.4) | +5.9% (-6.6 to +18.3) | -1.1% (-30.2 to +28.1) | shown, not judged |
| utilisation (used / allocatable) | +31.5% (+14.2 to +48.7) | +22.4% (+5.2 to +39.5) | +16.9% (+7.9 to +25.8) | shown, not judged |
| CPU used (cores), mean | +0.5% (-2.6 to +3.6) | -0.5% (-3.1 to +2.1) | -0.3% (-1.4 to +0.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01674 (+0.01529 to +0.01819) | +0.01829 (+0.01554 to +0.02104) | +0.01692 (+0.01504 to +0.0188) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.9% (-1.2 to +4.9) | +0.8% (-1.8 to +3.4) | +1.0% (-0.2 to +2.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -18.9% (-31.0 to -6.8) | -13.5% (-23.9 to -3.1) | -10.6% (-16.6 to -4.6) | shown, not judged |
| HPA replicas, mean | =0.0% (−6.1 to +6.2) | +1.9% (−7.7 to +11.5) | +0.9% (−7.9 to +9.6) | **the runs disagree** |
| pods started | +100.0% (−126.2 to +326.2) | +0.2000 (−0.1016 to +0.5016) | +100.0% (−427.8 to +627.8) | **the runs disagree** |
| pod start wait, total (s) | +100.0% (−126.2 to +326.2) | −0.2000 (−0.5016 to +0.1016) | −200.0% (−938.8 to +538.8) | **the runs disagree** |
| pod start wait, mean (s) | +100.0% (−126.2 to +326.2) | −0.2000 (−0.5016 to +0.1016) | −50.0% (−478.2 to +378.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.7% (+1.4 to +3.9) | +2.5% (+1.5 to +3.6) | +2.1% (+1.8 to +2.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.2% (−0.4 to +0.7) | −0.6% (−0.0 to −1.1) | =0.5% (+0.0 to +0.9) | EVEN, under the floor (the three runs' mean 0.40%) |
| batch: worker machines in service after the queue finished, mean | +40.5% (+21.4 to +59.5) | +29.6% (+7.8 to +51.3) | +28.5% (+13.8 to +43.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | −37.5% (−111.1 to +36.1) | −150.0% (−340.2 to +40.2) | +33.3% (−18.2 to +84.8) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +33.3% (−42.1 to +108.7) | −300.0% (−645.5 to +45.5) | +40.0% (−50.5 to +130.5) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −5.3% (−15.3 to +4.7) | −3.9% (−7.9 to +0.1) | −7.2% (−0.2 to −14.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 2 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 9 shown, not judged, 7 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
