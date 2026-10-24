# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on top of the bin-packing profile against the organism alone (register row 88): the A/B/C three-run table (Omni v12)

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
| A | 39368428763 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368435483 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368442002 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +9.1% (+0.4 to +17.8) | +21.7% (+8.2 to +35.3) | +16.7% (+3.3 to +30.0) | **GAIN in all three of our runs** |
| node-hours | +9.0% (+0.2 to +17.8) | +21.8% (+8.2 to +35.3) | +16.7% (+3.3 to +30.1) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.0 to +0.4) | =0.1% (−0.2 to +0.4) | =0.1% (−0.4 to +0.3) | EVEN, under the floor (the three runs' mean 0.08%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +6.1% (+0.1 to +12.1) | +15.0% (+5.7 to +24.4) | +11.6% (+2.3 to +20.9) | **GAIN in all three of our runs** |
| response time (ms), mean | +18.0% (+11.5 to +24.6) | +22.8% (+14.4 to +31.1) | +21.5% (+15.5 to +27.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | −10.5% (−21.8 to +0.8) | −1.0% (−12.1 to +10.2) | −7.2% (−17.7 to +3.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 99th percentile | −14.2% (−31.2 to +2.7) | −7.9% (−19.0 to +3.3) | −12.7% (−29.1 to +3.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +27.6% (+11.5 to +43.6) | +31.5% (+4.5 to +58.5) | +28.3% (+6.7 to +50.0) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −2.8% (−7.2 to +1.7) | +15.9% (−0.6 to +32.5) | +6.0% (−1.3 to +13.3) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +35 (+26.76 to +43.24) | +46.3 (+35.52 to +57.08) | +42.1 (+32.08 to +52.12) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +9.5% (-15.8 to +34.8) | +33.6% (+13.8 to +53.5) | +10.7% (-5.1 to +26.6) | shown, not judged |
| utilisation (used / allocatable) | +10.0% (+0.3 to +19.8) | +29.4% (+9.1 to +49.8) | +22.1% (+3.0 to +41.1) | shown, not judged |
| CPU used (cores), mean | -0.3% (-1.6 to +1.0) | -0.5% (-4.1 to +3.1) | -1.5% (-3.0 to -0.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01715 (+0.0159 to +0.0184) | +0.01651 (+0.01459 to +0.01843) | +0.01685 (+0.01557 to +0.01813) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.8% (-0.4 to +2.1) | +0.8% (-2.8 to +4.3) | -0.3% (-1.8 to +1.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -6.8% (-13.9 to +0.2) | -17.7% (-32.5 to -3.0) | -11.1% (-20.6 to -1.5) | shown, not judged |
| HPA replicas, mean | +18.5% (+9.5 to +27.6) | +7.1% (−3.9 to +18.1) | +11.5% (+2.4 to +20.7) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +500.0% (+123.0 to +877.0) | +0.3000 (−0.1828 to +0.7828) | +100.0% (−126.2 to +326.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −200.0% (−501.6 to +101.6) | −1.0000 (−2.6519 to +0.6519) | +14.3% (−168.8 to +197.4) | **the runs disagree** |
| pod start wait, mean (s) | −200.0% (−501.6 to +101.6) | −0.6500 (−1.6338 to +0.3338) | +14.3% (−168.8 to +197.4) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +1.8% (+1.0 to +2.6) | +2.2% (+1.1 to +3.4) | +1.7% (+0.8 to +2.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −0.5% (−1.3 to +0.2) | =0.1% (−0.4 to +0.5) | =0.1% (−0.5 to +0.4) | EVEN, under the floor (the three runs' mean 0.18%) |
| batch: worker machines in service after the queue finished, mean | +16.9% (+1.5 to +32.2) | +36.1% (+15.3 to +56.8) | +27.6% (+7.0 to +48.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +50.0% (−10.6 to +110.6) | −58.3% (−151.7 to +35.1) | −40.0% (−142.3 to +62.3) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +50.0% (−30.5 to +130.5) | −66.7% (−217.5 to +84.1) | −100.0% (−326.2 to +126.2) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −5.9% (−12.0 to +0.1) | −2.7% (−5.8 to +0.5) | −4.4% (−10.0 to +1.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 2 EVEN, under the floor, 6 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
