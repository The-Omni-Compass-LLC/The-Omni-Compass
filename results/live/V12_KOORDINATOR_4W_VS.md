# Koordinator under the batch stream, the four ways: Omni-Compass on the organism alone against Koordinator as shipped (register row 89): the A/B/C three-run table (Omni v12)

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
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +22.8% (+11.5 to +34.0) | +17.5% (+3.6 to +31.4) | +14.6% (+6.8 to +22.4) | **GAIN in all three of our runs** |
| node-hours | +22.7% (+11.5 to +33.9) | +17.7% (+3.9 to +31.5) | +14.5% (+6.7 to +22.4) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.4% (−0.9 to −0.0) | =0.1% (−0.8 to +0.9) | =0.0% (−0.6 to +0.6) | EVEN, under the floor (the three runs' mean 0.13%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +16.3% (+8.3 to +24.4) | +12.0% (+1.7 to +22.4) | +10.2% (+4.3 to +16.0) | **GAIN in all three of our runs** |
| response time (ms), mean | −40.4% (−83.9 to +3.0) | −148.2% (−55.6 to −240.8) | −71.4% (−13.0 to −129.9) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 95th percentile | −191.2% (−63.6 to −318.8) | −485.5% (−212.9 to −758.0) | −285.6% (−106.4 to −464.8) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | −181.3% (−56.9 to −305.8) | −481.6% (−212.0 to −751.1) | −285.0% (−116.9 to −453.1) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | −4381.5% (−8894.3 to +131.3) | −7419.5% (−3065.0 to −11774.0) | −8073.6% (−3500.6 to −12646.7) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −4.9000 (−0.7503 to −9.0497) | −8900.0% (−4446.3 to −13353.7) | −9500.0% (−6140.7 to −12859.3) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +64 (+51.18 to +76.82) | +41.3 (+25.47 to +57.13) | +41.2 (+29.17 to +53.23) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -98.8% (-134.9 to -62.8) | -99.1% (-123.2 to -74.9) | -99.1% (-126.6 to -71.6) | shown, not judged |
| utilisation (used / allocatable) | +16.5% (+5.3 to +27.7) | +24.8% (+15.5 to +34.1) | +13.0% (+7.6 to +18.5) | shown, not judged |
| CPU used (cores), mean | -11.0% (-17.5 to -4.4) | +1.5% (-11.0 to +14.0) | -3.5% (-10.5 to +3.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01674 (+0.01529 to +0.01819) | +0.01829 (+0.01554 to +0.02104) | +0.01692 (+0.01504 to +0.0188) | shown, not judged |
| CPU used with Omni's own (cores), mean | -9.8% (-16.3 to -3.2) | +2.8% (-9.8 to +15.3) | -2.3% (-9.4 to +4.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -6.2% (-11.8 to -0.6) | -12.9% (-16.5 to -9.2) | -6.7% (-10.3 to -3.1) | shown, not judged |
| HPA replicas, mean | +2.1% (−5.4 to +9.6) | +4.7% (−2.9 to +12.2) | +1.7% (−6.3 to +9.6) | **the runs disagree** |
| pods started | +100.0% (−21.6 to +221.6) | +100.0% (−306.0 to +506.0) | +0.2000 (−0.2524 to +0.6524) | **the runs disagree** |
| pod start wait, total (s) | +100.0% (−24.3 to +224.3) | +33.3% (−229.1 to +295.7) | −0.6000 (−1.9572 to +0.7572) | **the runs disagree** |
| pod start wait, mean (s) | +100.0% (−16.1 to +216.1) | +33.3% (−229.1 to +295.7) | −0.3000 (−0.9786 to +0.3786) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -13.3% (-17.2 to -9.3) | -4.7% (-12.5 to +3.2) | -9.3% (-13.5 to -5.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +43.3% (+30.6 to +55.9) | +44.9% (+39.7 to +50.1) | +46.2% (+36.4 to +56.1) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +53.9% (+37.8 to +70.1) | +64.5% (+60.5 to +68.5) | +49.2% (+34.0 to +64.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +100.0% (+53.7 to +146.2) | +100.0% (+64.0 to +136.0) | +100.0% (+69.3 to +130.7) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +100.0% (+53.2 to +146.7) | +99.9% (+68.3 to +131.6) | +100.0% (+72.9 to +127.0) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +93.5% (+62.6 to +124.3) | +88.9% (+74.0 to +103.7) | +92.2% (+70.9 to +113.5) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +100.0% (−16.3 to +216.3) | +100.0% (+37.3 to +162.7) | +100.0% (+36.5 to +163.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 1 GAIN by the mean of our three runs, 8 GAIN in all three of our runs, 2 LOSS by the mean of our three runs, 3 LOSS in all three of our runs, 9 shown, not judged, 4 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
