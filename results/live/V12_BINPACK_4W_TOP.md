# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on top of the bin-packing profile against the bin-packing profile as shipped (register row 88): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368428763 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368435483 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368442002 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +9.1% (+0.4 to +17.8) | +21.7% (+8.2 to +35.3) | +16.7% (+3.3 to +30.0) | **GAIN in all three of our runs** |
| node-hours | +9.1% (+0.3 to +17.9) | +21.7% (+8.2 to +35.3) | +16.6% (+3.1 to +30.0) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.1 to +0.4) | =0.0% (−0.3 to +0.3) | =0.1% (−0.3 to +0.5) | EVEN, under the floor (the three runs' mean 0.06%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +6.2% (+0.2 to +12.2) | +15.1% (+5.7 to +24.6) | +11.5% (+2.2 to +20.9) | **GAIN in all three of our runs** |
| response time (ms), mean | +14.3% (+9.6 to +19.0) | +18.2% (+13.3 to +23.1) | +14.5% (+11.1 to +17.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +2.7% (−4.2 to +9.6) | +3.7% (−2.2 to +9.6) | −7.8% (−17.6 to +1.9) | **the runs disagree** |
| response time (ms), 99th percentile | =0.4% (−8.2 to +8.9) | +6.0% (−0.5 to +12.5) | −2.5% (−5.7 to +0.6) | **the runs disagree** |
| time over the response line (% of samples) | +8.3% (+4.3 to +12.2) | +4.7% (−6.9 to +16.4) | +2.5% (−4.6 to +9.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −3.7% (−8.4 to +0.9) | +3.3% (−1.7 to +8.4) | +1.3% (−3.9 to +6.4) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +35 (+26.76 to +43.24) | +46.3 (+35.52 to +57.08) | +42.1 (+32.08 to +52.12) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.4% (-18.1 to +20.8) | +8.7% (-9.8 to +27.2) | +6.9% (-3.6 to +17.4) | shown, not judged |
| utilisation (used / allocatable) | +11.1% (+0.6 to +21.6) | +28.8% (+10.0 to +47.5) | +22.6% (+3.0 to +42.3) | shown, not judged |
| CPU used (cores), mean | +0.7% (-1.0 to +2.4) | -1.0% (-2.5 to +0.6) | -1.1% (-2.7 to +0.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01715 (+0.0159 to +0.0184) | +0.01651 (+0.01459 to +0.01843) | +0.01685 (+0.01557 to +0.01813) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.8% (+0.2 to +3.5) | +0.3% (-1.4 to +1.9) | +0.1% (-1.5 to +1.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -7.9% (-15.9 to +0.1) | -15.9% (-26.3 to -5.5) | -11.5% (-21.7 to -1.3) | shown, not judged |
| HPA replicas, mean | +12.2% (+3.2 to +21.3) | +6.9% (−3.3 to +17.0) | +8.3% (+0.4 to +16.1) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +200.0% (−50.1 to +450.1) | =0.0% (−251.3 to +251.3) | +0.4000 (+0.0306 to +0.7694) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −80.0% (−284.6 to +124.6) | −100.0% (−494.7 to +294.7) | −0.6000 (−1.2032 to +0.0032) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | −260.0% (−7.2 to −512.8) | −62.5% (−392.4 to +267.4) | −0.6000 (−1.2032 to +0.0032) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | +1.9% (+1.3 to +2.6) | +2.1% (+1.4 to +2.9) | +2.4% (+2.1 to +2.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.4% (−0.3 to +1.0) | =0.2% (−0.3 to +0.7) | =0.3% (−0.2 to +0.7) | EVEN, under the floor (the three runs' mean 0.29%) |
| batch: worker machines in service after the queue finished, mean | +16.9% (+1.5 to +32.2) | +36.1% (+15.3 to +56.8) | +27.6% (+7.0 to +48.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +30.8% (−43.5 to +105.0) | −18.8% (−88.8 to +51.3) | +26.3% (−10.3 to +62.9) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | =0.0% (−159.0 to +159.0) | −25.0% (−126.5 to +76.5) | +33.3% (−16.9 to +83.6) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −2.2% (−6.7 to +2.3) | −2.4% (−6.0 to +1.2) | −5.2% (−0.9 to −9.5) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 2 EVEN, under the floor, 1 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
