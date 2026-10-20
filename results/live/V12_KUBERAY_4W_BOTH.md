# KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on top of KubeRay against the organism alone (register row 92): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438462925 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438478652 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438494234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.9% (-2.9 to +1.1) | -1.8% (-3.5 to -0.1) | -1.2% (-3.0 to +0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| node-hours | -0.7% (-2.7 to +1.3) | -1.8% (-3.5 to +0.0) | -1.2% (-3.0 to +0.6) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +5.5% (+4.0 to +7.0) | +4.7% (+3.8 to +5.6) | +4.5% (+3.5 to +5.5) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +4.9% (+2.8 to +7.0) | +3.5% (+2.1 to +4.8) | +3.7% (+2.2 to +5.1) | **power given in all three of our runs** |
| response time (ms), mean | +85.7% (+68.2 to +103.3) | +85.1% (+68.5 to +101.7) | +67.0% (+49.1 to +84.9) | **LOSS in all three of our runs** |
| response time (ms), 95th percentile | +19.8% (-21.8 to +61.3) | +23.3% (-13.8 to +60.3) | -3.8% (-43.1 to +35.5) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +15.1% (-31.0 to +61.2) | +8.9% (-32.1 to +50.0) | -5.6% (-46.4 to +35.2) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | +212.8% (+175.6 to +250.1) | +223.2% (+172.9 to +273.6) | +207.9% (+172.9 to +243.0) | **LOSS in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +202.8% (+146.0 to +259.6) | +216.4% (+168.3 to +264.6) | +157.0% (+115.5 to +198.5) | **LOSS in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +15.33 (+12.14 to +18.53) | +16.5 (+11.85 to +21.15) | +15.6 (+12.13 to +19.07) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -78.4% (-111.6 to -45.1) | -79.9% (-105.2 to -54.6) | -79.9% (-104.3 to -55.4) | shown, not judged |
| utilisation (used / allocatable) | +67.9% (+49.7 to +86.1) | +60.0% (+49.1 to +71.0) | +53.8% (+42.5 to +65.0) | shown, not judged |
| CPU used (cores), mean | +66.6% (+48.3 to +84.8) | +57.2% (+47.2 to +67.3) | +52.0% (+41.4 to +62.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.008756 (+0.007947 to +0.009564) | +0.00896 (+0.008399 to +0.009521) | +0.00909 (+0.008394 to +0.009786) | shown, not judged |
| CPU used with Omni's own (cores), mean | +67.2% (+49.0 to +85.4) | +57.9% (+47.9 to +67.9) | +52.6% (+42.1 to +63.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -39.5% (-57.6 to -21.4) | -35.5% (-45.4 to -25.6) | -32.9% (-42.7 to -23.1) | shown, not judged |
| HPA replicas, mean | +8.1% (+0.5 to +15.7) | +3.4% (-4.4 to +11.1) | +7.9% (+3.6 to +12.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pods started | +0.5556 (-0.2237 to +1.335) | +0.1 (-0.1262 to +0.3262) | +0.4 (+0.03062 to +0.7694) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, total (s) | +1.111 (-0.2981 to +2.52) | +0.2 (-0.2524 to +0.6524) | +0.8 (-0.01208 to +1.612) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +0.7407 (-0.154 to +1.635) | +0.2 (-0.2524 to +0.6524) | +0.8 (-0.01208 to +1.612) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +87.3% (+75.9 to +98.7) | +76.9% (+69.8 to +84.0) | +74.4% (+66.3 to +82.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +89.3% (+79.7 to +98.9) | +80.1% (+69.7 to +90.5) | +80.8% (+71.6 to +90.1) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | -18.3% (-250.2 to +213.7) | -24.7% (-31.9 to -17.5) | -31.6% (-75.2 to +12.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: job wait, submitted to its first pod running, mean (s) | +1967119.6% (+1111934.3 to +2822304.9) | +1287745.8% (+521467.2 to +2054024.4) | +1250833.4% (+747221.5 to +1754445.3) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +1001696.3% (+623421.0 to +1379971.7) | +230987.0% (+116467.0 to +345506.9) | +285052.5% (+193399.9 to +376705.2) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +1067.6% (+891.6 to +1243.7) | +910.0% (+690.2 to +1129.8) | +774.9% (+649.7 to +900.2) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +13.44 (+7.163 to +19.73) | +11.3 (+3.858 to +18.74) | +14.5 (+8.326 to +20.67) | **LOSS in all three of our runs** |

Readings: 8 LOSS in all three of our runs, 2 power given in all three of our runs, 1 EVEN, no difference beyond the noise (1 of 3 runs), 3 EVEN, no difference beyond the noise (2 of 3 runs), 5 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
