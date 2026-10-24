# Volcano under the batch stream, the four ways: Omni-Compass on the organism alone against Volcano as shipped (register row 63): the A/B/C three-run table (Omni v12)

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
| A | 39368409208 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368415819 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368422189 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +14.6% (+7.6 to +21.6) | +19.2% (+7.4 to +31.0) | +11.8% (−0.1 to +23.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| node-hours | +14.5% (+7.5 to +21.5) | +19.1% (+7.3 to +30.9) | +11.6% (−0.2 to +23.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.2 to +0.5) | =0.0% (−0.4 to +0.3) | =0.3% (+0.0 to +0.6) | EVEN, under the floor (the three runs' mean 0.15%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +10.0% (+5.1 to +14.8) | +13.3% (+5.1 to +21.5) | +7.9% (−0.2 to +16.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), mean | −20.0% (−0.7 to −39.3) | −11.4% (−29.2 to +6.3) | −13.1% (−27.6 to +1.5) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 95th percentile | −92.6% (−46.7 to −138.5) | −31.9% (−10.8 to −53.0) | −50.9% (−23.2 to −78.6) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | −73.3% (−31.5 to −115.1) | −9.6% (−27.4 to +8.3) | −23.6% (−1.1 to −46.0) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | −124.1% (−51.4 to −196.7) | −50.2% (−5.7 to −94.8) | −54.8% (−19.1 to −90.4) | **LOSS in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −30.3% (−6.8 to −53.8) | −11.3% (−26.1 to +3.6) | −23.2% (−48.2 to +1.8) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +40.2 (+31.7 to +48.7) | +55.7 (+35.95 to +75.45) | +49.7 (+37.2 to +62.2) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -23.2% (-41.4 to -4.9) | -34.3% (-51.1 to -17.4) | -30.8% (-43.6 to -18.0) | shown, not judged |
| utilisation (used / allocatable) | +17.1% (+8.6 to +25.7) | +22.1% (+6.3 to +37.9) | +13.8% (-0.7 to +28.3) | shown, not judged |
| CPU used (cores), mean | -0.4% (-1.5 to +0.7) | -2.7% (-5.0 to -0.3) | -0.8% (-2.7 to +1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01732 (+0.01601 to +0.01863) | +0.01773 (+0.01636 to +0.0191) | +0.01698 (+0.0147 to +0.01926) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.9% (-0.3 to +2.0) | -1.5% (-3.8 to +0.9) | +0.4% (-1.6 to +2.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.0% (-15.8 to -4.3) | -12.0% (-21.2 to -2.8) | -8.6% (-17.7 to +0.4) | shown, not judged |
| HPA replicas, mean | +2.2% (−7.8 to +12.2) | +6.0% (−5.7 to +17.7) | +2.8% (−3.5 to +9.1) | **the runs disagree** |
| pods started | +100.0% (−126.2 to +326.2) | +100.0% (−427.8 to +627.8) | +0.1000 (−0.1262 to +0.3262) | **the runs disagree** |
| pod start wait, total (s) | +100.0% (−126.2 to +326.2) | −200.0% (−938.8 to +538.8) | −0.2000 (−0.6524 to +0.2524) | **the runs disagree** |
| pod start wait, mean (s) | +100.0% (−126.2 to +326.2) | −50.0% (−478.2 to +378.2) | −0.2000 (−0.6524 to +0.2524) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -0.1% (-0.7 to +0.6) | -1.0% (-1.5 to -0.4) | -0.4% (-1.3 to +0.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.7% (+0.3 to +1.2) | +1.2% (+0.1 to +2.2) | +0.8% (+0.2 to +1.5) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +29.0% (+15.7 to +42.4) | +33.8% (+16.2 to +51.4) | +20.5% (+0.9 to +40.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +92.5% (+79.4 to +105.6) | +90.8% (+71.0 to +110.6) | +92.7% (+71.8 to +113.6) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +78.6% (+49.6 to +107.6) | +66.7% (+11.6 to +121.7) | +58.3% (+29.5 to +87.1) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +13.6% (+6.1 to +21.2) | +13.7% (+3.7 to +23.7) | +11.5% (+4.0 to +19.1) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 3 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 2 LOSS in all three of our runs, 9 shown, not judged, 4 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
