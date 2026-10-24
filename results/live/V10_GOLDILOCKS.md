# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39106189778 | `0454fdb0089f` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39113187123 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39120448390 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (+0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.4% (−0.9 to +0.2) | =0.3% (−0.1 to +0.6) | =0.1% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.07%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.8% (+1.4 to +2.3) | +2.4% (+1.8 to +2.9) | +1.8% (+1.3 to +2.3) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.8% (+1.4 to +2.3) | +2.4% (+1.8 to +2.9) | +1.8% (+1.3 to +2.3) | **power given in all three of our runs** |
| response time (ms), mean | +46.1% (+33.2 to +59.0) | +47.3% (+34.2 to +60.4) | +46.6% (+33.6 to +59.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +60.1% (+47.6 to +72.7) | +60.1% (+48.0 to +72.2) | +61.3% (+48.6 to +74.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +65.3% (+55.0 to +75.5) | +66.2% (+53.6 to +78.8) | +66.5% (+53.6 to +79.3) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +100.0% (+37.8 to +162.2) | +99.1% (+44.7 to +153.4) | +100.0% (+39.1 to +160.9) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+24.6 to +175.4) | +100.0% (+21.3 to +178.7) | +100.0% (+24.6 to +175.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +16 (+13.89 to +18.11) | +13.8 (+12.46 to +15.14) | +16.2 (+13.11 to +19.29) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.02667 (-0.03365 to +0.08699) | +326.7% (-178.7 to +832.1) | +0.0% (-337.2 to +337.2) | shown, not judged |
| utilisation (used / allocatable) | +44.9% (+34.3 to +55.6) | +43.7% (+33.6 to +53.7) | +41.1% (+30.5 to +51.7) | shown, not judged |
| CPU used (cores), mean | +44.9% (+34.3 to +55.6) | +43.7% (+33.6 to +53.7) | +41.1% (+30.5 to +51.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00832 (+0.007486 to +0.009154) | +0.00806 (+0.007076 to +0.009044) | +0.00769 (+0.006753 to +0.008627) | shown, not judged |
| CPU used with Omni's own (cores), mean | +46.0% (+35.2 to +56.7) | +44.7% (+34.5 to +54.9) | +42.1% (+31.4 to +52.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -28.5% (-33.0 to -24.0) | -28.1% (-32.6 to -23.6) | -26.7% (-31.2 to -22.3) | shown, not judged |
| HPA replicas, mean | +1.1% (−0.3 to +2.5) | +1.9% (+0.7 to +3.0) | +0.6% (−2.0 to +3.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +54.5% (+4.2 to +104.9) | +91.3% (+57.1 to +125.5) | +42.9% (−34.9 to +120.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, total (s) | +45.5% (−11.7 to +102.6) | +94.7% (+50.2 to +139.3) | +42.9% (−54.1 to +139.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | +19.0% (−37.1 to +75.2) | +93.1% (+54.5 to +131.8) | +35.6% (−27.3 to +98.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | +40.9% (+31.9 to +49.9) | +39.7% (+30.6 to +48.8) | +38.0% (+28.4 to +47.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 3 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 1 power given by the mean of our three runs, 2 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
