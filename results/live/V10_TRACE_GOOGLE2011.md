# A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39108177259 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115239009 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122539586 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to −0.0) | =0.0% (−0.0 to −0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.1 to +0.3) | =0.1% (−0.1 to +0.3) | =0.1% (−0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.3% (−0.5 to −0.1) | =0.3% (−0.5 to −0.1) | =0.4% (−0.6 to −0.3) | EVEN, under the floor (the three runs' mean 0.34%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.3% (−0.5 to −0.1) | =0.3% (−0.5 to −0.1) | =0.4% (−0.6 to −0.3) | EVEN, under the floor (the three runs' mean 0.34%) |
| response time (ms), mean | +47.8% (+34.6 to +60.9) | +47.6% (+30.8 to +64.4) | +49.8% (+34.9 to +64.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +56.2% (+43.7 to +68.7) | +60.3% (+40.8 to +79.8) | +61.9% (+45.0 to +78.8) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +38.2% (+30.0 to +46.4) | +40.9% (+23.3 to +58.4) | +50.6% (+37.6 to +63.7) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +73.5% (+39.6 to +107.5) | +74.5% (+38.6 to +110.5) | +76.8% (+39.0 to +114.6) | **GAIN in all three of our runs** |
| failed requests (%) | +18.1% (+6.4 to +29.9) | +15.7% (+4.9 to +26.5) | +14.6% (+1.6 to +27.6) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +60.8% (+38.1 to +83.5) | +61.5% (+33.1 to +89.9) | +65.7% (+40.3 to +91.0) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +62.5 (+45.78 to +79.22) | +66 (+47.31 to +84.69) | +55.2 (+34.34 to +76.06) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +115.5% (+33.6 to +197.4) | +17.3% (-54.0 to +88.6) | +13.9% (-72.1 to +99.9) | shown, not judged |
| utilisation (used / allocatable) | -3.7% (-4.5 to -3.0) | -3.6% (-4.9 to -2.4) | -3.8% (-5.1 to -2.6) | shown, not judged |
| CPU used (cores), mean | -3.7% (-4.5 to -3.0) | -3.6% (-4.9 to -2.4) | -3.8% (-5.1 to -2.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00979 (+0.008182 to +0.0114) | +0.00968 (+0.007803 to +0.01156) | +0.00919 (+0.007481 to +0.0109) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.2% (-3.9 to -2.5) | -3.1% (-4.3 to -1.9) | -3.3% (-4.5 to -2.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +4.0% (+1.9 to +6.0) | +3.1% (+1.5 to +4.7) | +3.2% (+2.9 to +3.6) | shown, not judged |
| HPA replicas, mean | +11.2% (−0.1 to +22.5) | +14.8% (+0.9 to +28.6) | +7.9% (−4.6 to +20.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +163.8% (+95.4 to +232.2) | +192.7% (+96.1 to +289.3) | +120.0% (+35.4 to +204.6) | **power given in all three of our runs** |
| pod start wait, total (s) | −76.1% (−43.5 to −108.6) | −116.3% (−31.1 to −201.4) | −45.1% (−115.0 to +24.8) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, mean (s) | +25.1% (+6.7 to +43.6) | +10.4% (−28.8 to +49.6) | +29.7% (+0.7 to +58.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy, the real machine under kind (%) | -2.6% (-3.3 to -2.0) | -2.3% (-3.3 to -1.3) | -2.5% (-3.6 to -1.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 1 GAIN by the mean of our three runs, 6 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
