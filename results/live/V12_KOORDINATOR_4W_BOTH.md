# Koordinator under the batch stream, the four ways: Omni-Compass on top of Koordinator against the organism alone (register row 89): the A/B/C three-run table (Omni v12)

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
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +2.5% (−1.1 to +6.2) | =0.4% (−1.2 to +0.3) | +1.4% (−1.8 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| node-hours | +2.4% (−1.4 to +6.2) | =0.2% (−0.9 to +0.5) | +1.4% (−1.8 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | +0.6% (+0.2 to +1.1) | =0.0% (−0.8 to +0.8) | =0.1% (−0.4 to +0.7) | EVEN, under the floor (the three runs' mean 0.27%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.1% (−1.4 to +3.7) | =0.3% (−1.0 to +0.4) | +0.9% (−1.4 to +3.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), mean | +56.0% (+23.2 to +88.7) | +72.2% (+32.6 to +111.7) | +62.8% (+32.9 to +92.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +66.9% (+21.9 to +111.9) | +82.8% (+31.8 to +133.7) | +74.4% (+31.5 to +117.2) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +64.2% (+23.2 to +105.2) | +82.3% (+33.1 to +131.4) | +73.0% (+31.3 to +114.6) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +98.5% (−1.8 to +198.8) | +98.4% (+39.1 to +157.8) | +98.4% (+42.2 to +154.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+17.8 to +182.2) | +97.7% (+43.5 to +151.9) | +98.9% (+59.7 to +138.1) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +14.2 (+11.13 to +17.27) | +12.5 (+10.84 to +14.16) | +11.4 (+8.555 to +14.25) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +10306.6% (+6365.4 to +14247.8) | +11253.2% (+8243.7 to +14262.8) | +11685.6% (+8482.7 to +14888.5) | shown, not judged |
| utilisation (used / allocatable) | +13.2% (+1.9 to +24.6) | -1.4% (-12.3 to +9.4) | +4.3% (-4.3 to +13.0) | shown, not judged |
| CPU used (cores), mean | +10.7% (+1.4 to +19.9) | -1.8% (-12.4 to +8.7) | +3.1% (-5.1 to +11.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01124 (+0.01006 to +0.01242) | +0.01219 (+0.01113 to +0.01325) | +0.01196 (+0.01105 to +0.01287) | shown, not judged |
| CPU used with Omni's own (cores), mean | +11.6% (+2.4 to +20.8) | -1.0% (-11.5 to +9.5) | +4.0% (-4.1 to +12.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -13.7% (-25.7 to -1.7) | -1.1% (-11.6 to +9.5) | -5.1% (-13.0 to +2.8) | shown, not judged |
| HPA replicas, mean | +3.7% (−1.8 to +9.3) | =0.3% (−9.0 to +9.6) | +1.4% (−8.8 to +11.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +100.0% (−126.2 to +326.2) | +0.3000 (−0.0455 to +0.6455) | =0.0% (−337.2 to +337.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −50.0% (−163.1 to +63.1) | −0.7000 (−1.5294 to +0.1294) | =0.0% (−337.2 to +337.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | +25.0% (−31.5 to +81.5) | −0.7000 (−1.5294 to +0.1294) | =0.0% (−337.2 to +337.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +19.0% (+13.1 to +24.8) | +8.4% (+0.3 to +16.5) | +13.4% (+7.4 to +19.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −79.6% (−57.4 to −101.8) | −82.5% (−72.2 to −92.7) | −90.2% (−71.9 to −108.5) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +9.7% (−4.1 to +23.5) | +6.2% (−11.3 to +23.8) | +11.0% (−36.2 to +58.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job wait, submitted to its first pod running, mean (s) | −332575.0% (−204178.2 to −460971.8) | −701433.3% (−502619.2 to −900247.5) | −227980.0% (−149811.1 to −306148.9) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −172733.3% (−104746.8 to −240719.9) | −763800.0% (−530043.0 to −997557.0) | −136780.0% (−86044.3 to −187515.7) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | −1607.8% (−1081.3 to −2134.4) | −849.4% (−675.6 to −1023.2) | −1322.9% (−1027.8 to −1618.1) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | −5.3000 (−11.4906 to +0.8906) | −10.7000 (−4.0490 to −17.3510) | −8.8000 (−3.2613 to −14.3387) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 6 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 2 LOSS by the mean of our three runs, 4 LOSS in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
