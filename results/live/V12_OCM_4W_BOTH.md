# Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Open Cluster Management against the organism alone (register row 96): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39479807336 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39479824367 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39479840381 | `00ec0be44be7` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +1.9% (−0.3 to +4.1) | +7.4% (−3.8 to +18.5) | +7.1% (+0.5 to +13.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| node-hours | +2.1% (−0.1 to +4.4) | +7.5% (−3.6 to +18.6) | +7.0% (+0.4 to +13.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.5 to +0.4) | =0.3% (−0.1 to +0.7) | =0.4% (−0.0 to +0.9) | EVEN, under the floor (the three runs' mean 0.23%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.4% (−0.2 to +3.0) | +5.0% (−3.1 to +13.1) | +4.7% (+0.1 to +9.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), mean | −59.9% (−38.6 to −81.3) | −51.7% (−23.3 to −80.0) | −58.7% (−37.1 to −80.3) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | −51.5% (−36.6 to −66.4) | −55.2% (−22.4 to −88.0) | −55.0% (−29.0 to −81.1) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | −49.4% (−31.0 to −67.8) | −58.4% (−25.9 to −90.9) | −52.9% (−30.2 to −75.6) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | −55.9% (−30.2 to −81.5) | −23.9% (−11.2 to −36.5) | −75.5% (−53.5 to −97.5) | **LOSS in all three of our runs** |
| failed requests (%) | −1075.1% (−3104.7 to +954.5) | −1410.9% (−3307.7 to +485.9) | −41.3% (−301.7 to +219.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −24.8% (−18.0 to −31.6) | −26.6% (−20.5 to −32.7) | −74.3% (−40.2 to −108.3) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +48 (+41.77 to +54.23) | +57.4 (+34.35 to +80.45) | +43.8 (+33.04 to +54.56) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +166.1% (-31.6 to +363.8) | +70.8% (+13.4 to +128.3) | +116.9% (-44.4 to +278.1) | shown, not judged |
| utilisation (used / allocatable) | +6.4% (-5.2 to +18.1) | +17.3% (+7.7 to +26.9) | +14.3% (+1.5 to +27.2) | shown, not judged |
| CPU used (cores), mean | +4.6% (-6.3 to +15.5) | +9.0% (+3.8 to +14.1) | +6.4% (-2.1 to +14.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01277 (+0.01157 to +0.01397) | +0.01242 (+0.01188 to +0.01296) | +0.01188 (+0.01116 to +0.0126) | shown, not judged |
| CPU used with Omni's own (cores), mean | +5.3% (-5.6 to +16.2) | +9.7% (+4.5 to +14.9) | +7.1% (-1.4 to +15.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -5.5% (-16.4 to +5.4) | -13.7% (-22.1 to -5.3) | -11.6% (-23.0 to -0.3) | shown, not judged |
| HPA replicas, mean | +19.1% (−1.3 to +39.5) | +7.0% (−3.7 to +17.6) | +3.6% (−2.1 to +9.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +300.0% (−45.5 to +645.5) | +1300.0% (+470.6 to +2129.4) | +400.0% (+106.9 to +693.1) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, total (s) | −262.5% (−638.2 to +113.2) | −1350.0% (−337.7 to −2362.3) | −733.3% (−1506.4 to +39.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −181.8% (−456.0 to +92.4) | −708.3% (−164.7 to −1251.9) | −516.7% (−1102.4 to +69.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | +20.2% (+16.9 to +23.5) | +19.7% (+14.7 to +24.6) | +20.2% (+17.3 to +23.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −21.4% (−16.0 to −26.8) | −19.4% (−11.5 to −27.4) | −19.1% (−13.1 to −25.0) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +4.6% (−0.3 to +9.6) | +10.8% (−5.6 to +27.2) | +15.6% (+1.2 to +30.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: job wait, submitted to its first pod running, mean (s) | −14475.7% (−1985.4 to −26966.0) | −15860.7% (−1447.0 to −30274.5) | −17305.6% (−349.2 to −34262.0) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −22685.7% (−4894.5 to −40476.9) | −13100.0% (−1240.5 to −24959.5) | −16980.0% (−170.1 to −33789.9) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | −70.9% (−54.6 to −87.2) | −67.7% (−38.0 to −97.5) | −76.8% (−55.5 to −98.1) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 4 GAIN by the mean of our three runs, 3 LOSS by the mean of our three runs, 9 LOSS in all three of our runs, 2 power given by the mean of our three runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
