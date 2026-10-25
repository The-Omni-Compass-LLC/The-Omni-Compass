# CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38843284578 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38843287341 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38843289946 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | +0.5% (−0.7 to +1.7) | +0.7% (−0.9 to +2.2) | **the runs disagree** |
| node-hours | =0.2% (−0.5 to +0.8) | +1.0% (+0.2 to +1.8) | =0.1% (−1.6 to +1.4) | EVEN, under the floor (the three runs' mean 0.37%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.4 to +0.9) | =0.1% (−1.2 to +1.3) | +1.2% (−0.1 to +2.4) | EVEN, under the floor (the three runs' mean 0.48%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.2% (−0.4 to +0.9) | =0.4% (−0.1 to +0.9) | +0.7% (+0.2 to +1.1) | EVEN, under the floor (the three runs' mean 0.44%) |
| response time (ms), mean | −1.5% (−3.1 to +0.2) | =0.1% (−1.6 to +1.7) | −0.8% (−2.5 to +1.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 95th percentile | =0.3% (−1.1 to +1.8) | =0.1% (−2.3 to +2.2) | =0.1% (−1.7 to +1.5) | EVEN, under the floor (the three runs' mean 0.04%) |
| response time (ms), 99th percentile | −3.1% (−0.6 to −5.7) | =0.0% (−4.1 to +4.2) | =0.1% (−4.7 to +4.5) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| time over the response line (% of samples) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +2.1% (-156.9 to +161.1) | -57.8% (-178.1 to +62.6) | -80.2% (-152.5 to -8.0) | shown, not judged |
| utilisation (used / allocatable) | +0.9% (-0.6 to +2.3) | -0.7% (-2.3 to +0.8) | +1.1% (-0.5 to +2.6) | shown, not judged |
| CPU used (cores), mean | +0.9% (-0.6 to +2.3) | -0.1% (-1.8 to +1.5) | +0.4% (-1.1 to +1.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00953 (+0.008894 to +0.01017) | +0.00853 (+0.007232 to +0.009828) | +0.00964 (+0.008849 to +0.01043) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.6% (+0.2 to +3.1) | +0.6% (-1.0 to +2.3) | +1.2% (-0.3 to +2.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.7% (-2.0 to +0.6) | +0.3% (-1.0 to +1.5) | -0.2% (-1.5 to +1.1) | shown, not judged |
| HPA replicas, mean | +3.2% (−9.1 to +15.5) | +0.7% (−6.5 to +7.9) | +1.9% (−6.7 to +10.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +45.5% (−37.1 to +128.0) | +18.8% (−28.6 to +66.1) | +7.7% (−23.5 to +38.9) | **the runs disagree** |
| pod start wait, total (s) | −117.6% (−319.2 to +83.9) | +8.3% (−71.6 to +88.3) | +15.9% (−76.7 to +108.5) | **the runs disagree** |
| pod start wait, mean (s) | −120.9% (−279.2 to +37.5) | −24.7% (−118.0 to +68.6) | +14.0% (−54.1 to +82.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.0% (+0.8 to +3.3) | +0.2% (-1.4 to +1.8) | +1.6% (+0.5 to +2.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 EVEN, the same, 4 EVEN, under the floor, 2 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 9 shown, not judged, 4 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
