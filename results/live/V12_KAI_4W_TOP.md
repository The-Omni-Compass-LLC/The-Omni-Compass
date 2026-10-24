# The KAI scheduler under the batch stream, the four ways: Omni-Compass on top of KAI against KAI as shipped (register row 91): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368344021 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368351097 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368358521 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +14.3% (+4.4 to +24.2) | +7.7% (+1.2 to +14.2) | +6.0% (−0.2 to +12.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| node-hours | +14.2% (+4.4 to +24.1) | +7.8% (+1.2 to +14.4) | +6.0% (−0.4 to +12.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.4 to +0.5) | =0.1% (−0.4 to +0.3) | =0.1% (−0.3 to +0.5) | EVEN, under the floor (the three runs' mean 0.02%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +9.9% (+3.0 to +16.8) | +5.3% (+0.8 to +9.9) | +4.0% (−0.4 to +8.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), mean | +11.1% (+2.1 to +20.1) | +7.5% (+3.2 to +11.8) | +9.7% (+2.7 to +16.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | −2.8% (−14.1 to +8.6) | −3.4% (−9.1 to +2.4) | −4.4% (−16.0 to +7.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 99th percentile | −3.7% (−12.0 to +4.5) | −3.4% (−10.3 to +3.5) | =0.5% (−9.2 to +10.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +3.5% (−6.0 to +13.1) | +3.0% (−5.3 to +11.4) | +1.0% (−11.7 to +13.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −1.1% (−5.8 to +3.5) | +2.4% (−3.1 to +7.9) | +0.9% (−2.6 to +4.4) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +35 (+27.73 to +42.27) | +31.7 (+28.19 to +35.21) | +30.8 (+25.73 to +35.87) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.2% (-18.8 to +21.1) | +6.8% (-14.6 to +28.3) | -0.6% (-11.6 to +10.3) | shown, not judged |
| utilisation (used / allocatable) | +15.5% (+4.5 to +26.5) | +8.8% (+1.4 to +16.3) | +7.4% (+0.5 to +14.4) | shown, not judged |
| CPU used (cores), mean | -0.6% (-3.2 to +2.1) | +0.4% (-0.6 to +1.5) | +0.7% (-0.7 to +2.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01869 (+0.01571 to +0.02167) | +0.01924 (+0.01699 to +0.02149) | +0.0184 (+0.01509 to +0.02171) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.8% (-1.8 to +3.4) | +1.7% (+0.5 to +2.8) | +1.9% (+0.6 to +3.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.2% (-17.8 to -2.6) | -6.0% (-11.8 to -0.3) | -5.3% (-10.2 to -0.3) | shown, not judged |
| HPA replicas, mean | +6.1% (−4.6 to +16.8) | +2.8% (−6.5 to +12.0) | +11.6% (+1.6 to +21.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +150.0% (−189.3 to +489.3) | +50.0% (−153.0 to +253.0) | +33.3% (−142.6 to +209.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −166.7% (−526.5 to +193.2) | −33.3% (−168.7 to +102.0) | +16.7% (−156.1 to +189.4) | **the runs disagree** |
| pod start wait, mean (s) | −433.3% (−984.6 to +117.9) | −166.7% (−369.3 to +36.0) | −25.0% (−221.8 to +171.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +2.6% (+1.9 to +3.4) | +2.6% (+1.8 to +3.4) | +2.4% (+1.3 to +3.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −0.8% (−0.1 to −1.6) | −1.1% (−0.3 to −1.9) | −0.6% (−1.4 to +0.3) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| batch: worker machines in service after the queue finished, mean | +26.3% (+9.4 to +43.2) | +15.7% (+3.2 to +28.3) | +11.6% (+0.8 to +22.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | −18.7% (−48.6 to +11.2) | −0.8% (−33.4 to +31.8) | +4.9% (−3.0 to +12.9) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −62.5% (−146.8 to +21.8) | −15.4% (−91.2 to +60.5) | −14.3% (−46.6 to +18.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job turnaround, submitted to done, mean (s) | −5.6% (−11.7 to +0.4) | −6.5% (−0.8 to −12.2) | −5.0% (−0.2 to −9.9) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 4 GAIN by the mean of our three runs, 2 GAIN in all three of our runs, 6 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
