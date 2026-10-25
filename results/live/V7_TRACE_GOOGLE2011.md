# A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38933435153 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38945578014 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38955589372 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.0 to +0.3) | =0.1% (−0.1 to +0.3) | =0.1% (−0.0 to +0.2) | EVEN, under the floor (the three runs' mean 0.09%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.3% (−0.5 to −0.0) | =0.4% (−0.6 to −0.2) | =0.2% (−0.4 to +0.0) | EVEN, under the floor (the three runs' mean 0.29%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.3% (−0.5 to −0.0) | =0.4% (−0.6 to −0.2) | =0.2% (−0.4 to +0.0) | EVEN, under the floor (the three runs' mean 0.29%) |
| response time (ms), mean | +48.5% (+26.2 to +70.8) | +48.8% (+36.3 to +61.3) | +47.6% (+25.5 to +69.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +55.8% (+33.1 to +78.4) | +54.4% (+42.1 to +66.8) | +57.7% (+34.2 to +81.2) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +46.9% (+25.7 to +68.1) | +38.4% (+26.7 to +50.2) | +49.1% (+27.2 to +71.0) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +72.5% (+28.7 to +116.4) | +71.9% (+42.9 to +100.8) | +74.0% (+25.1 to +123.0) | **GAIN in all three of our runs** |
| failed requests (%) | +13.2% (+4.1 to +22.4) | +13.7% (+2.5 to +24.8) | +11.7% (+0.2 to +23.2) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +52.3% (+19.4 to +85.1) | +66.5% (+49.3 to +83.8) | +57.1% (+20.9 to +93.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +59.2 (+39.12 to +79.28) | +52.6 (+34.57 to +70.63) | +54 (+34.58 to +73.42) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +104.3% (+16.5 to +192.2) | -4.6% (-61.2 to +52.0) | +63.3% (-24.7 to +151.3) | shown, not judged |
| utilisation (used / allocatable) | -3.7% (-5.2 to -2.3) | -4.3% (-5.5 to -3.2) | -3.1% (-5.0 to -1.3) | shown, not judged |
| CPU used (cores), mean | -3.7% (-5.2 to -2.3) | -4.3% (-5.5 to -3.2) | -3.1% (-5.0 to -1.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00907 (+0.006988 to +0.01115) | +0.00926 (+0.007194 to +0.01133) | +0.00855 (+0.006503 to +0.0106) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.2% (-4.6 to -1.9) | -3.9% (-5.0 to -2.7) | -2.6% (-4.4 to -0.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +3.1% (+1.6 to +4.6) | +3.7% (+2.6 to +4.8) | +2.5% (-0.4 to +5.4) | shown, not judged |
| HPA replicas, mean | +8.7% (−6.5 to +23.8) | +7.4% (−3.6 to +18.4) | +6.1% (−9.3 to +21.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +127.3% (+41.6 to +212.9) | +142.6% (+76.8 to +208.4) | +106.9% (+41.2 to +172.7) | **power given in all three of our runs** |
| pod start wait, total (s) | −58.9% (−2.3 to −115.5) | −25.7% (−71.4 to +19.9) | −51.7% (−16.3 to −87.1) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, mean (s) | +8.8% (−13.2 to +30.9) | +40.6% (+13.4 to +67.9) | +17.4% (−17.2 to +51.9) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy, the real machine under kind (%) | -2.4% (-3.5 to -1.3) | -3.1% (-4.1 to -2.1) | -1.8% (-3.7 to +0.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 1 GAIN by the mean of our three runs, 6 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
