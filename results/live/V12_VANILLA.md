# The Kubernetes scheduler as shipped under the batch stream: Omni-Compass on top of the default scheduler alone (register row 88): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39356571014 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39356586356 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39356601235 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +12.0% (+4.6 to +19.4) | +18.9% (+6.2 to +31.6) | +15.0% (+4.4 to +25.6) | **GAIN in all three of our runs** |
| node-hours | +12.0% (+4.5 to +19.4) | +18.9% (+6.1 to +31.7) | +15.2% (+4.6 to +25.7) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.7 to +0.4) | =0.1% (−0.4 to +0.5) | =0.4% (−0.9 to +0.2) | EVEN, under the floor (the three runs' mean 0.15%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +8.4% (+2.9 to +13.9) | +13.1% (+4.0 to +22.2) | +10.7% (+3.1 to +18.3) | **GAIN in all three of our runs** |
| response time (ms), mean | +24.5% (+20.1 to +28.8) | +21.4% (+17.1 to +25.7) | +20.8% (+17.5 to +24.2) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | =0.2% (−5.3 to +4.9) | −9.1% (−3.9 to −14.2) | −5.3% (−11.9 to +1.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 99th percentile | −1.0% (−4.6 to +2.6) | −5.7% (−1.0 to −10.4) | −4.5% (−1.1 to −8.0) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | +6.6% (−6.5 to +19.6) | −13.3% (−28.1 to +1.5) | −7.8% (−31.9 to +16.3) | **the runs disagree** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0% (−4.9 to +4.9) | −28.9% (−61.6 to +3.8) | −22.1% (−49.8 to +5.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +38.3 (+23.57 to +53.03) | +60.2 (+42.77 to +77.63) | +41.2 (+24.73 to +57.67) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +6.4% (-18.7 to +31.6) | +8.1% (-32.7 to +48.9) | -6.6% (-31.0 to +17.8) | shown, not judged |
| utilisation (used / allocatable) | +11.3% (+4.8 to +17.8) | +24.3% (+8.5 to +40.2) | +15.5% (+5.0 to +26.0) | shown, not judged |
| CPU used (cores), mean | -1.8% (-7.0 to +3.5) | -1.4% (-7.9 to +5.2) | -2.5% (-9.5 to +4.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02202 (+0.01899 to +0.02505) | +0.01929 (+0.01724 to +0.02134) | +0.01963 (+0.01703 to +0.02223) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.3% (-5.6 to +5.0) | +0.1% (-6.5 to +6.6) | -1.1% (-8.2 to +6.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -6.5% (-11.8 to -1.2) | -13.5% (-22.9 to -4.2) | -8.6% (-15.7 to -1.4) | shown, not judged |
| HPA replicas, mean | +2.5% (−2.5 to +7.5) | +5.5% (−3.0 to +14.0) | +8.6% (−2.0 to +19.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +100.0% (−15.2 to +215.2) | =0.0% (−238.4 to +238.4) | +150.0% (−144.4 to +444.4) | **the runs disagree** |
| pod start wait, total (s) | +100.0% (−16.1 to +216.1) | +20.0% (−198.0 to +238.0) | −100.0% (−371.9 to +171.9) | **the runs disagree** |
| pod start wait, mean (s) | +100.0% (−16.1 to +216.1) | +20.0% (−198.0 to +238.0) | −50.0% (−238.5 to +138.5) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.3% (+1.9 to +2.7) | +2.5% (+2.0 to +3.1) | +2.7% (+2.2 to +3.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.2% (+0.0 to +0.4) | =0.0% (−0.0 to +0.1) | =0.1% (−0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.12%) |
| batch: worker machines in service after the queue finished, mean | +22.0% (+9.2 to +34.9) | +30.2% (+9.9 to +50.6) | +26.4% (+9.4 to +43.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +25.0% (−106.9 to +156.9) | −60.0% (−177.8 to +57.8) | −33.3% (−168.7 to +102.0) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | =0.0000 (±0.0000 to ±0.0000) | =0.0% (−337.2 to +337.2) | =0.0% (−337.2 to +337.2) | EVEN, the same |
| queue: job turnaround, submitted to done, mean (s) | −0.9% (−0.2 to −1.7) | −0.9% (−0.1 to −1.6) | −1.2% (−0.6 to −1.8) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 5 EVEN, the same, 2 EVEN, under the floor, 5 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 1 LOSS in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
