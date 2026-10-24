# KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 92): the A/B/C three-run table (Omni v12)

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
| A | 39438462925 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438478652 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438494234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +18.6% (+5.1 to +32.1) | +19.3% (+6.0 to +32.7) | +14.0% (+2.6 to +25.3) | **GAIN in all three of our runs** |
| node-hours | +18.4% (+5.0 to +31.9) | +19.1% (+5.7 to +32.6) | +14.1% (+2.8 to +25.4) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.3% (−0.2 to +0.9) | =0.2% (−0.1 to +0.5) | =0.1% (−0.5 to +0.3) | EVEN, under the floor (the three runs' mean 0.15%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +12.6% (+3.4 to +21.8) | +13.2% (+3.8 to +22.5) | +9.7% (+1.9 to +17.5) | **GAIN in all three of our runs** |
| response time (ms), mean | +9.8% (+4.7 to +14.9) | +9.1% (+6.0 to +12.1) | +7.2% (+4.5 to +9.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | −6.3% (−13.4 to +0.8) | −7.0% (−2.5 to −11.4) | −3.4% (−7.4 to +0.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 99th percentile | −9.8% (−1.5 to −18.0) | −4.4% (−0.1 to −8.7) | −13.0% (−4.7 to −21.2) | **LOSS in all three of our runs** |
| time over the response line (% of samples) | +4.5% (−1.1 to +10.1) | +3.1% (−1.4 to +7.5) | +2.8% (−2.2 to +7.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −8.3% (−17.9 to +1.3) | +1.4% (−5.9 to +8.6) | −5.4% (−13.7 to +2.9) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +47.33 (+35.65 to +59.02) | +45.7 (+32.87 to +58.53) | +46.6 (+33.06 to +60.14) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -4.3% (-27.2 to +18.6) | -4.9% (-17.7 to +8.0) | +22.5% (+4.1 to +40.9) | shown, not judged |
| utilisation (used / allocatable) | +24.7% (+5.7 to +43.8) | +25.3% (+7.2 to +43.3) | +16.8% (+3.6 to +30.0) | shown, not judged |
| CPU used (cores), mean | +0.8% (-3.2 to +4.8) | -0.7% (-2.2 to +0.9) | -0.3% (-2.2 to +1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0191 (+0.016 to +0.0222) | +0.01679 (+0.01549 to +0.01809) | +0.01724 (+0.01631 to +0.01817) | shown, not judged |
| CPU used with Omni's own (cores), mean | +2.2% (-1.9 to +6.2) | +0.5% (-1.1 to +2.0) | +0.9% (-1.1 to +2.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -16.3% (-31.9 to -0.8) | -14.3% (-24.1 to -4.5) | -10.4% (-18.2 to -2.5) | shown, not judged |
| HPA replicas, mean | +4.8% (−2.5 to +12.1) | +6.3% (−4.1 to +16.6) | +9.0% (+2.4 to +15.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +0.2222 (−0.1167 to +0.5612) | +0.4000 (−0.1001 to +0.9001) | +0.3000 (−0.0455 to +0.6455) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −0.5556 (−1.4244 to +0.3133) | −0.5000 (−1.1952 to +0.1952) | −0.6000 (−1.3689 to +0.1689) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | −0.5556 (−1.4244 to +0.3133) | −0.3500 (−0.7647 to +0.0647) | −0.6000 (−1.3689 to +0.1689) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +3.2% (+1.8 to +4.7) | +2.1% (+0.8 to +3.3) | +2.3% (+1.3 to +3.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −0.8% (−0.1 to −1.5) | −0.7% (−0.2 to −1.2) | −0.6% (−0.2 to −1.1) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | +32.7% (+11.3 to +54.1) | +33.0% (+11.3 to +54.7) | +25.4% (+6.2 to +44.5) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | −57.1% (−168.9 to +54.6) | −120.0% (−301.0 to +61.0) | −76.9% (−219.0 to +65.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −200.0% (−505.1 to +105.1) | =0.0% (−119.2 to +119.2) | −50.0% (−125.4 to +25.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job turnaround, submitted to done, mean (s) | −6.8% (−14.2 to +0.6) | −5.0% (−10.2 to +0.2) | −6.1% (−1.9 to −10.4) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 6 LOSS by the mean of our three runs, 2 LOSS in all three of our runs, 2 power given by the mean of our three runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
