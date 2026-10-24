# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38931373773 | `ccce256f4079` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38943562450 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38953643978 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge) | +60.7% (+43.5 to +78.0) | +47.1% (+32.3 to +61.8) | +40.5% (+32.2 to +48.7) | **GAIN in all three of our runs** |
| worker nodes in service, mean | =0.0% (−0.0 to −0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.1 to +0.1) | =0.1% (−0.1 to +0.2) | =0.0% (−0.2 to +0.2) | EVEN, under the floor (the three runs' mean 0.03%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.3 to +0.1) | =0.2% (−0.3 to +0.0) | =0.4% (−0.6 to −0.1) | EVEN, under the floor (the three runs' mean 0.22%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.1% (−0.3 to +0.1) | =0.2% (−0.3 to +0.0) | =0.4% (−0.6 to −0.1) | EVEN, under the floor (the three runs' mean 0.22%) |
| response time (ms), mean | +39.8% (+27.8 to +51.7) | +43.4% (+31.1 to +55.7) | +44.1% (+28.8 to +59.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +55.6% (+44.5 to +66.7) | +57.0% (+41.8 to +72.2) | +61.5% (+45.6 to +77.4) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +18.4% (−26.7 to +63.5) | +37.8% (+20.4 to +55.2) | +29.7% (−2.4 to +61.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| time over the response line (% of samples) | +36.6% (+24.6 to +48.6) | +37.0% (+23.5 to +50.5) | +43.9% (+25.3 to +62.6) | **GAIN in all three of our runs** |
| failed requests (%) | +10.6% (+3.1 to +18.1) | +9.3% (+0.8 to +17.9) | +13.8% (+1.3 to +26.4) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +19.9% (+14.6 to +25.3) | +24.0% (+17.5 to +30.5) | +34.7% (+26.9 to +42.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +36.3 (+29.55 to +43.05) | +30.1 (+20.54 to +39.66) | +29.9 (+21.51 to +38.29) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +84.2% (-89.8 to +258.2) | +3.9% (-88.7 to +96.5) | +0.4% (-40.5 to +41.2) | shown, not judged |
| utilisation (used / allocatable) | -1.2% (-2.3 to -0.0) | -1.9% (-3.0 to -0.8) | -3.5% (-5.1 to -2.0) | shown, not judged |
| CPU used (cores), mean | -1.2% (-2.3 to -0.0) | -1.9% (-3.0 to -0.8) | -3.5% (-5.1 to -2.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00923 (+0.008185 to +0.01028) | +0.00854 (+0.007263 to +0.009817) | +0.00754 (+0.006157 to +0.008923) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.8% (-1.9 to +0.3) | -1.6% (-2.7 to -0.4) | -3.2% (-4.8 to -1.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.5% (+0.0 to +3.0) | +2.6% (+0.3 to +4.9) | +5.2% (+1.6 to +8.9) | shown, not judged |
| HPA replicas, mean | +4.9% (−1.6 to +11.3) | +2.6% (−4.1 to +9.4) | +2.0% (−1.4 to +5.4) | **the runs disagree** |
| pods started | +33.3% (−19.3 to +85.9) | +20.0% (−28.2 to +68.2) | +3.8% (−26.4 to +34.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −6.0% (−61.0 to +48.9) | −9.2% (−58.8 to +40.5) | +6.0% (−19.0 to +31.0) | **the runs disagree** |
| pod start wait, mean (s) | +14.9% (−16.9 to +46.7) | +4.4% (−24.4 to +33.2) | +11.7% (−1.1 to +24.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | -0.6% (-1.8 to +0.5) | -1.4% (-2.4 to -0.3) | -3.1% (-4.6 to -1.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 2 GAIN by the mean of our three runs, 6 GAIN in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
