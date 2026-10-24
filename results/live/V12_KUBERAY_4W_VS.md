# KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on the organism alone against KubeRay as shipped (register row 92): the A/B/C three-run table (Omni v12)

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
| A | 39438462925 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438478652 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438494234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +18.6% (+5.1 to +32.1) | +19.3% (+6.0 to +32.7) | +14.0% (+2.6 to +25.3) | **GAIN in all three of our runs** |
| node-hours | +18.6% (+5.3 to +31.9) | +19.0% (+5.6 to +32.4) | +14.2% (+3.1 to +25.4) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | +4.9% (+3.8 to +6.0) | +4.1% (+3.3 to +4.9) | +4.5% (+3.6 to +5.4) | **GAIN in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +17.2% (+7.5 to +26.9) | +16.9% (+7.6 to +26.3) | +13.7% (+5.8 to +21.6) | **GAIN in all three of our runs** |
| response time (ms), mean | +52.0% (+39.0 to +65.0) | +51.3% (+38.1 to +64.5) | +45.6% (+33.7 to +57.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +7.8% (−31.4 to +46.9) | +8.3% (−31.0 to +47.6) | −8.0% (−51.6 to +35.5) | **the runs disagree** |
| response time (ms), 99th percentile | +4.8% (−36.2 to +45.8) | +4.3% (−39.1 to +47.6) | −19.4% (−69.6 to +30.8) | **the runs disagree** |
| time over the response line (% of samples) | +70.3% (+57.7 to +82.9) | +71.0% (+53.9 to +88.1) | +69.4% (+58.3 to +80.5) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +64.4% (+46.4 to +82.3) | +69.1% (+52.3 to +85.9) | +59.3% (+44.6 to +74.1) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +47.33 (+35.65 to +59.02) | +45.7 (+32.87 to +58.53) | +46.6 (+33.06 to +60.14) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +351.1% (+198.2 to +504.0) | +327.9% (+201.1 to +454.6) | +452.2% (+273.8 to +630.6) | shown, not judged |
| utilisation (used / allocatable) | -25.6% (-30.9 to -20.2) | -20.5% (-31.0 to -10.0) | -23.0% (-31.7 to -14.3) | shown, not judged |
| CPU used (cores), mean | -39.8% (-49.7 to -30.0) | -37.0% (-43.4 to -30.6) | -34.3% (-42.2 to -26.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0191 (+0.016 to +0.0222) | +0.01679 (+0.01549 to +0.01809) | +0.01724 (+0.01631 to +0.01817) | shown, not judged |
| CPU used with Omni's own (cores), mean | -39.0% (-48.9 to -29.1) | -36.2% (-42.7 to -29.8) | -33.5% (-41.5 to -25.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +38.2% (+31.3 to +45.0) | +31.5% (+21.9 to +41.2) | +32.3% (+22.9 to +41.7) | shown, not judged |
| HPA replicas, mean | +1.1% (−7.0 to +9.3) | +2.2% (−7.6 to +11.9) | +0.7% (−6.1 to +7.5) | **the runs disagree** |
| pods started | +100.0% (−315.7 to +515.7) | +33.3% (−102.0 to +168.7) | +50.0% (−213.9 to +313.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −150.0% (−639.2 to +339.2) | +37.5% (−74.4 to +149.4) | −100.0% (−438.1 to +238.1) | **the runs disagree** |
| pod start wait, mean (s) | −150.0% (−639.2 to +339.2) | +36.4% (−111.3 to +184.0) | −100.0% (−438.1 to +238.1) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -44.9% (-51.1 to -38.8) | -42.3% (-46.3 to -38.3) | -41.2% (-45.9 to -36.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +47.1% (+41.9 to +52.3) | +44.3% (+38.9 to +49.6) | +44.5% (+39.6 to +49.5) | **GAIN in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -66.7% (+nan to +nan) | -66.4% (-66.9 to -65.9) | -66.3% (-66.3 to -66.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| queue: job wait, submitted to its first pod running, mean (s) | +100.0% (+58.0 to +141.9) | +100.0% (+40.0 to +160.0) | +100.0% (+60.7 to +139.3) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +100.0% (+67.4 to +132.5) | +100.0% (+50.0 to +150.0) | +99.9% (+66.5 to +133.3) | **GAIN in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +90.9% (+75.3 to +106.4) | +89.8% (+70.6 to +108.9) | +87.9% (+74.2 to +101.7) | **GAIN in all three of our runs** |
| queue: jobs unfinished at the window's end | +100.0% (+57.3 to +142.7) | +100.0% (+33.8 to +166.2) | +100.0% (+59.0 to +141.0) | **GAIN in all three of our runs** |

Readings: 1 EVEN, no difference beyond the noise, 3 EVEN, the same, 12 GAIN in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
