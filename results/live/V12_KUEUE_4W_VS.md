# Kueue under the batch stream, the four ways: Omni-Compass on the organism alone against Kueue as shipped (register row 63): the A/B/C three-run table (Omni v12)

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
| A | 39368387821 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368394823 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368401852 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +14.5% (+3.9 to +25.2) | +9.8% (+3.5 to +16.0) | +13.8% (+3.9 to +23.7) | **GAIN in all three of our runs** |
| node-hours | +14.4% (+3.5 to +25.2) | +9.7% (+3.5 to +15.8) | +14.0% (+4.1 to +23.9) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.2 to +0.5) | =0.2% (−0.2 to +0.6) | =0.2% (−0.4 to −0.0) | EVEN, under the floor (the three runs' mean 0.06%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +9.9% (+2.3 to +17.5) | +6.5% (+2.4 to +10.7) | +9.7% (+2.8 to +16.6) | **GAIN in all three of our runs** |
| response time (ms), mean | +17.4% (+8.7 to +26.2) | +17.7% (+12.5 to +22.9) | +17.5% (+11.0 to +23.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +7.9% (−4.4 to +20.3) | +7.6% (+1.6 to +13.7) | +5.3% (−4.1 to +14.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 99th percentile | +2.8% (−7.3 to +12.8) | +8.3% (−0.9 to +17.5) | +7.0% (+0.3 to +13.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| time over the response line (% of samples) | +10.8% (+1.5 to +20.0) | +8.9% (+3.4 to +14.4) | +10.8% (+4.7 to +16.9) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +1.3% (−3.9 to +6.5) | =0.0% (−5.7 to +5.7) | +1.0% (−3.2 to +5.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +46.1 (+34.95 to +57.25) | +39.9 (+29.63 to +50.17) | +41.89 (+29.46 to +54.32) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +15.8% (+0.4 to +31.2) | -9.9% (-24.7 to +4.8) | -5.2% (-24.4 to +14.0) | shown, not judged |
| utilisation (used / allocatable) | +16.0% (+3.7 to +28.3) | +11.4% (+4.4 to +18.4) | +15.6% (+3.9 to +27.3) | shown, not judged |
| CPU used (cores), mean | -1.3% (-3.6 to +1.0) | +0.5% (-0.9 to +1.9) | -0.9% (-2.3 to +0.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01696 (+0.01582 to +0.0181) | +0.01666 (+0.01502 to +0.0183) | +0.01814 (+0.01706 to +0.01923) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.1% (-2.4 to +2.1) | +1.6% (+0.3 to +3.0) | +0.3% (-1.2 to +1.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.1% (-17.9 to -2.3) | -7.9% (-14.1 to -1.7) | -9.5% (-17.2 to -1.9) | shown, not judged |
| HPA replicas, mean | =0.2% (−6.6 to +7.0) | +0.9% (−3.1 to +5.0) | +4.6% (−3.4 to +12.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | =0.0% (−337.2 to +337.2) | =0.0% (−337.2 to +337.2) | +100.0% (−130.6 to +330.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | +100.0% (−126.2 to +326.2) | +25.0% (−272.4 to +322.4) | +100.0% (−130.6 to +330.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | +100.0% (−126.2 to +326.2) | +25.0% (−272.4 to +322.4) | +100.0% (−130.6 to +330.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +0.1% (-0.9 to +1.1) | -0.1% (-0.9 to +0.8) | +0.4% (-0.4 to +1.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.5% (−1.3 to +0.4) | +0.8% (+0.2 to +1.4) | +0.8% (−0.1 to +1.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| batch: worker machines in service after the queue finished, mean | +27.0% (+7.9 to +46.1) | +19.7% (+7.6 to +31.7) | +26.2% (+10.5 to +41.8) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +74.4% (+49.2 to +99.5) | +72.9% (+24.6 to +121.2) | +88.2% (+49.3 to +127.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +70.0% (+35.4 to +104.6) | +70.0% (+35.4 to +104.6) | +100.0% (+71.2 to +128.8) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +3.0% (−5.9 to +11.9) | +5.5% (+0.1 to +10.9) | +6.6% (+0.5 to +12.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 9 GAIN by the mean of our three runs, 8 GAIN in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
