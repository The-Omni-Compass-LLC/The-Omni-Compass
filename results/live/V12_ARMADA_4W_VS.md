# Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against Armada as shipped (register row 94): the A/B/C three-run table (Omni v12)

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
| A | 39482335827 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39482351075 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39482365814 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +10.4% (−3.7 to +24.5) | +6.2% (−3.3 to +15.6) | +24.5% (+10.6 to +38.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| node-hours | +10.4% (−3.8 to +24.6) | +6.2% (−3.4 to +15.7) | +24.4% (+10.3 to +38.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | +4.1% (+3.2 to +4.9) | +4.3% (+3.7 to +4.8) | +3.9% (+3.1 to +4.6) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +3.7% (−7.6 to +14.9) | =0.3% (−7.9 to +7.2) | +14.5% (+3.5 to +25.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), mean | −365.9% (−157.4 to −574.3) | −387.2% (−211.6 to −562.8) | −271.6% (−1.7 to −541.5) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | −1362.7% (−633.9 to −2091.4) | −1439.3% (−847.3 to −2031.3) | −986.8% (−75.2 to −1898.5) | **LOSS in all three of our runs** |
| response time (ms), 99th percentile | −1691.7% (−817.5 to −2565.8) | −1837.8% (−1123.2 to −2552.5) | −1233.4% (−145.9 to −2320.8) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | −583748.7% (−317248.1 to −850249.4) | −27.7590 (−17.8729 to −37.6451) | −13.9600 (−2.2913 to −25.6287) | **LOSS in all three of our runs** |
| failed requests (%) | −0.0076 (−0.0252 to +0.0100) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −12.3333 (−7.0357 to −17.6310) | −14.0000 (−10.0676 to −17.9324) | −8.2000 (−2.5094 to −13.8906) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +58.22 (+33.72 to +82.73) | +49.2 (+25.32 to +73.08) | +87.9 (+55.37 to +120.4) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +18.61 (+7.395 to +29.82) | +26.96 (+7.469 to +46.45) | +61186.7% (+14331.4 to +108041.9) | shown, not judged |
| utilisation (used / allocatable) | +523.1% (+474.3 to +572.0) | +484.4% (+458.4 to +510.4) | +638.0% (+587.3 to +688.8) | shown, not judged |
| CPU used (cores), mean | +457.0% (+377.1 to +536.9) | +446.5% (+398.6 to +494.5) | +449.3% (+379.8 to +518.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01219 (+0.01103 to +0.01334) | +0.01249 (+0.01167 to +0.01331) | +0.01309 (+0.01213 to +0.01405) | shown, not judged |
| CPU used with Omni's own (cores), mean | +461.1% (+381.1 to +541.2) | +450.6% (+402.8 to +498.3) | +454.3% (+384.7 to +523.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -82.7% (-94.4 to -71.1) | -81.8% (-88.0 to -75.6) | -84.8% (-96.9 to -72.7) | shown, not judged |
| HPA replicas, mean | =0.1% (−6.6 to +6.8) | +7.8% (+2.2 to +13.4) | +1.3% (−5.3 to +7.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +200.0% (−105.1 to +505.1) | +1.2000 (+0.3207 to +2.0793) | +14.3% (−141.4 to +170.0) | **the runs disagree** |
| pod start wait, total (s) | −125.0% (−371.3 to +121.3) | −2.3000 (−0.2475 to −4.3525) | +33.3% (−116.2 to +182.9) | **the runs disagree** |
| pod start wait, mean (s) | −275.0% (−4.6 to −545.4) | −1.0833 (−0.3184 to −1.8483) | +27.8% (−114.0 to +169.5) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +266.5% (+223.3 to +309.7) | +262.2% (+232.1 to +292.2) | +258.6% (+216.7 to +300.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +41.3% (+34.7 to +47.8) | +39.3% (+33.0 to +45.6) | +45.6% (+38.7 to +52.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +100.0% (+99.7 to +100.3) | +100.0% (+99.8 to +100.2) | +100.0% (+99.7 to +100.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +99.9% (+99.7 to +100.2) | +99.9% (+99.8 to +100.1) | +100.0% (+99.8 to +100.2) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +83.3% (+75.0 to +91.6) | +80.9% (+72.7 to +89.0) | +89.1% (+80.3 to +97.9) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | **GAIN in all three of our runs** |

Readings: 2 EVEN, the same, 3 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 5 LOSS in all three of our runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
