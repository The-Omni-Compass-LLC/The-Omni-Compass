# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 88): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368428763 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368435483 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368442002 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +12.7% (+1.3 to +24.0) | +16.5% (+3.8 to +29.2) | +13.6% (+2.2 to +24.9) | **GAIN in all three of our runs** |
| node-hours | +12.7% (+1.4 to +24.0) | +16.5% (+3.6 to +29.3) | +13.6% (+2.4 to +24.7) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.3 to +0.3) | =0.1% (−0.2 to +0.4) | =0.0% (−0.4 to +0.3) | EVEN, under the floor (the three runs' mean 0.04%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +8.7% (+0.9 to +16.5) | +11.3% (+2.4 to +20.2) | +9.4% (+1.7 to +17.2) | **GAIN in all three of our runs** |
| response time (ms), mean | +9.7% (+4.9 to +14.5) | +11.1% (+5.2 to +17.0) | +14.3% (+8.6 to +20.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | −4.7% (−11.2 to +1.7) | −6.7% (−15.0 to +1.7) | −5.4% (−12.4 to +1.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 99th percentile | −2.3% (−10.6 to +6.1) | −3.5% (−9.6 to +2.6) | =0.3% (−11.9 to +11.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +4.4% (−0.2 to +9.0) | +1.4% (−6.3 to +9.1) | +4.6% (−6.0 to +15.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −0.9% (−4.7 to +2.8) | −11.6% (−25.2 to +2.1) | −3.6% (−11.8 to +4.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +44 (+30.47 to +57.53) | +55.5 (+41.92 to +69.08) | +47.4 (+31.46 to +63.34) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +3.5% (-16.3 to +23.3) | +15.9% (-2.2 to +34.0) | -7.1% (-21.4 to +7.2) | shown, not judged |
| utilisation (used / allocatable) | +16.2% (+1.5 to +30.9) | +21.9% (+4.9 to +38.8) | +17.9% (+2.6 to +33.2) | shown, not judged |
| CPU used (cores), mean | +0.2% (-1.2 to +1.6) | +1.0% (-0.9 to +2.9) | -0.4% (-2.1 to +1.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01881 (+0.0167 to +0.02092) | +0.01616 (+0.01481 to +0.01751) | +0.01653 (+0.01471 to +0.01835) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.4% (+0.0 to +2.8) | +2.2% (+0.3 to +4.1) | +0.8% (-1.0 to +2.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -9.9% (-18.7 to -1.2) | -15.0% (-28.4 to -1.6) | -9.5% (-17.4 to -1.5) | shown, not judged |
| HPA replicas, mean | +4.1% (−3.6 to +11.8) | +4.3% (−2.0 to +10.7) | +4.1% (−4.9 to +13.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | =0.0% (−337.2 to +337.2) | +0.3000 (−0.1828 to +0.7828) | +100.0% (−50.8 to +250.8) | **the runs disagree** |
| pod start wait, total (s) | +33.3% (−252.1 to +318.8) | −0.7000 (−2.0509 to +0.6509) | +100.0% (−52.7 to +252.7) | **the runs disagree** |
| pod start wait, mean (s) | +33.3% (−252.1 to +318.8) | −0.4000 (−1.0911 to +0.2911) | +100.0% (−52.7 to +252.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.2% (+1.5 to +2.9) | +2.8% (+1.7 to +4.0) | +1.7% (+0.6 to +2.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −0.6% (−1.3 to +0.2) | =0.5% (−0.3 to +1.2) | =0.5% (−0.1 to +1.0) | EVEN, under the floor (the three runs' mean 0.49%) |
| batch: worker machines in service after the queue finished, mean | +22.1% (+5.0 to +39.3) | +28.4% (+7.8 to +49.0) | +24.1% (+5.7 to +42.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | −11.1% (−121.6 to +99.4) | +25.0% (−64.1 to +114.1) | +10.0% (−109.0 to +129.0) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +33.3% (−42.1 to +108.7) | +33.3% (−142.6 to +209.3) | −50.0% (−313.9 to +213.9) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −4.4% (−10.5 to +1.7) | −3.6% (−10.3 to +3.2) | −4.3% (−10.9 to +2.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 2 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 4 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
