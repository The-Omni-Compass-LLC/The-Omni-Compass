# Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against Open Cluster Management as shipped (register row 96): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the orchestrator as shipped: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39479807336 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39479824367 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39479840381 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +5.5% (+0.4 to +10.7) | +9.9% (−2.7 to +22.6) | +15.9% (+1.7 to +30.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| node-hours | +5.6% (+0.5 to +10.7) | +10.0% (−2.7 to +22.7) | +15.8% (+1.3 to +30.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.7 to +0.3) | =0.3% (−0.6 to +0.1) | +0.6% (−0.7 to +2.0) | EVEN, under the floor (the three runs' mean 0.06%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +4.1% (+0.5 to +7.8) | +7.4% (−1.7 to +16.4) | +10.8% (−0.2 to +21.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), mean | +32.0% (+19.1 to +44.8) | +38.3% (+22.8 to +53.9) | +19.0% (−22.4 to +60.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 95th percentile | +24.8% (+11.7 to +37.9) | +32.0% (+16.7 to +47.3) | +7.3% (−40.0 to +54.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | +21.8% (+9.0 to +34.6) | +29.1% (+15.8 to +42.5) | +7.0% (−41.3 to +55.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | +27.0% (+18.3 to +35.7) | +22.2% (+11.4 to +32.9) | +13.0% (−31.4 to +57.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | +89.1% (−79.5 to +257.7) | +100.0% (−52.6 to +252.6) | +100.0% (−126.2 to +326.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +13.1% (+8.8 to +17.4) | +14.2% (+8.0 to +20.4) | +7.4% (−35.1 to +50.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +51 (+36.12 to +65.88) | +56.2 (+28.28 to +84.12) | +63.9 (+38.85 to +88.95) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -40.4% (-95.4 to +14.6) | -46.3% (-128.2 to +35.5) | -53.2% (-134.3 to +27.8) | shown, not judged |
| utilisation (used / allocatable) | +2.2% (-5.1 to +9.6) | +6.4% (-9.5 to +22.4) | +33.7% (+7.0 to +60.4) | shown, not judged |
| CPU used (cores), mean | -3.1% (-9.0 to +2.8) | -4.9% (-10.9 to +1.2) | +11.1% (-16.2 to +38.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0124 (+0.01164 to +0.01316) | +0.01182 (+0.01146 to +0.01218) | +0.01275 (+0.01191 to +0.01359) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.4% (-8.3 to +3.5) | -4.2% (-10.3 to +1.9) | +12.0% (-15.4 to +39.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -1.3% (-7.6 to +5.0) | -4.7% (-17.6 to +8.3) | -36.0% (-93.7 to +21.6) | shown, not judged |
| HPA replicas, mean | +10.4% (+3.8 to +17.0) | +10.1% (+1.6 to +18.5) | +3.9% (−2.2 to +10.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +1000.0% (+416.0 to +1584.0) | +1.5000 (+0.8048 to +2.1952) | +1.0000 (+0.3256 to +1.6744) | **power given in all three of our runs** |
| pod start wait, total (s) | −466.7% (−186.8 to −746.5) | −2.4000 (−0.9225 to −3.8775) | −1.3000 (−0.4047 to −2.1953) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | −266.7% (−26.9 to −506.4) | −1.2500 (−0.6136 to −1.8864) | −0.8000 (−0.2615 to −1.3385) | **LOSS in all three of our runs** |
| host CPU busy, the real machine under kind (%) | -8.9% (-11.4 to -6.4) | -10.4% (-14.0 to -6.8) | -0.6% (-21.8 to +20.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +11.1% (+6.8 to +15.3) | +12.5% (+7.4 to +17.6) | +13.0% (+3.8 to +22.1) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +11.3% (+1.1 to +21.6) | +16.4% (−2.8 to +35.7) | +29.3% (+4.2 to +54.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| queue: job wait, submitted to its first pod running, mean (s) | +98.2% (−70.9 to +267.2) | +98.8% (+6.1 to +191.5) | +98.1% (−55.5 to +251.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +98.5% (−64.4 to +261.3) | +99.1% (−2.5 to +200.7) | +94.7% (−70.2 to +259.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job turnaround, submitted to done, mean (s) | +28.0% (+15.9 to +40.0) | +33.2% (+18.9 to +47.4) | +31.6% (+12.5 to +50.7) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 12 GAIN by the mean of our three runs, 2 GAIN in all three of our runs, 2 LOSS in all three of our runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
