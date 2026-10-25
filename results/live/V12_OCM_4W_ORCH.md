# Open Cluster Management on the group of two clusters under the batch stream, the four ways: Open Cluster Management as shipped against the organism alone (register row 96): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39479807336 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39479824367 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39479840381 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.4 to +0.2) | =0.0% (−0.3 to +0.3) | =0.1% (−0.2 to +0.4) | EVEN, under the floor (the three runs' mean 0.02%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.4 to +0.4) | =0.2% (−0.1 to +0.5) | =0.4% (−1.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.07%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.0% (−0.4 to +0.4) | =0.2% (−0.1 to +0.5) | =0.4% (−1.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.07%) |
| response time (ms), mean | −43.6% (−24.2 to −62.9) | −56.4% (−31.6 to −81.2) | −15.7% (−63.5 to +32.1) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 95th percentile | −38.7% (−19.4 to −58.1) | −52.7% (−28.2 to −77.2) | −9.8% (−62.5 to +42.8) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | −34.4% (−13.7 to −55.0) | −48.2% (−27.5 to −69.0) | −10.8% (−62.1 to +40.6) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | −38.4% (−26.1 to −50.6) | −26.6% (−12.2 to −41.0) | −17.6% (−69.8 to +34.5) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | −742.2% (−2067.9 to +583.6) | −575.3% (−1442.9 to +292.3) | +54.0% (−205.2 to +313.3) | **the runs disagree** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −18.1% (−12.6 to −23.7) | −19.4% (−10.7 to −28.0) | −19.8% (−73.8 to +34.2) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +130.3% (-4.7 to +265.3) | +112.7% (-51.4 to +276.8) | +138.4% (-81.5 to +358.4) | shown, not judged |
| utilisation (used / allocatable) | +2.0% (-3.6 to +7.6) | +4.4% (-0.7 to +9.5) | -11.4% (-33.2 to +10.3) | shown, not judged |
| CPU used (cores), mean | +2.0% (-3.6 to +7.6) | +4.4% (-0.7 to +9.5) | -11.4% (-33.2 to +10.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | +2.0% (-3.6 to +7.6) | +4.4% (-0.7 to +9.5) | -11.4% (-33.2 to +10.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -2.0% (-6.7 to +2.6) | -3.9% (-7.6 to -0.2) | +38.1% (-42.8 to +118.9) | shown, not judged |
| HPA replicas, mean | =0.4% (−6.1 to +5.3) | +3.0% (−3.7 to +9.6) | =0.1% (−3.4 to +3.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +66.7% (−121.4 to +254.7) | +100.0% (−126.2 to +326.2) | +100.0% (−60.9 to +260.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | +62.5% (−127.2 to +252.2) | +100.0% (−126.2 to +326.2) | +100.0% (−60.9 to +260.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | +45.5% (−165.3 to +256.2) | +100.0% (−126.2 to +326.2) | +100.0% (−50.8 to +250.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +13.8% (+10.3 to +17.3) | +15.2% (+10.6 to +19.9) | +3.3% (-18.7 to +25.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −15.0% (−9.3 to −20.7) | −15.9% (−9.3 to −22.6) | −16.1% (−4.7 to −27.4) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | −4589.2% (−12556.0 to +3377.6) | −5839.3% (−343.3 to −11335.2) | −4080.2% (−10503.3 to +2342.8) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −5528.6% (−14699.6 to +3642.5) | −6887.5% (−13992.2 to +217.2) | −1177.8% (−3216.5 to +860.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job turnaround, submitted to done, mean (s) | −47.9% (−27.4 to −68.3) | −57.0% (−30.7 to −83.2) | −46.0% (−18.7 to −73.3) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 5 EVEN, the same, 3 EVEN, under the floor, 4 GAIN by the mean of our three runs, 7 LOSS by the mean of our three runs, 2 LOSS in all three of our runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
