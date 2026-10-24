# Steady load: the same fixed-rate work sent to both arms: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107180703 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39114207589 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39121472594 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.1 to +0.1) | =0.1% (−0.4 to +0.2) | =0.2% (−0.2 to +0.5) | EVEN, under the floor (the three runs' mean 0.02%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.2% (−0.4 to −0.0) | =0.5% (−0.8 to −0.1) | =0.1% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.26%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.2% (−0.4 to −0.0) | =0.5% (−0.8 to −0.1) | =0.1% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.26%) |
| response time (ms), mean | +48.2% (+33.6 to +62.7) | +48.8% (+38.6 to +59.1) | +48.5% (+30.9 to +66.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +64.7% (+47.4 to +82.0) | +64.3% (+52.3 to +76.3) | +65.2% (+44.4 to +86.1) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +72.6% (+51.4 to +93.8) | +68.8% (+50.2 to +87.3) | +69.8% (+48.5 to +91.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +99.5% (+40.8 to +158.1) | +98.4% (+62.1 to +134.7) | +100.0% (+39.4 to +160.6) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+39.1 to +160.9) | +100.0% (+58.6 to +141.4) | +100.0% (+36.9 to +163.1) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +18.6 (+15.45 to +21.75) | +18.8 (+15.5 to +22.1) | +18.3 (+15.82 to +20.78) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -22.5% (-85.5 to +40.4) | -11.9% (-76.5 to +52.7) | +47.5% (-62.2 to +157.2) | shown, not judged |
| utilisation (used / allocatable) | -5.2% (-7.8 to -2.6) | -6.1% (-7.9 to -4.3) | -5.4% (-8.3 to -2.4) | shown, not judged |
| CPU used (cores), mean | -5.2% (-7.8 to -2.6) | -6.1% (-7.9 to -4.3) | -5.4% (-8.3 to -2.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00807 (+0.006859 to +0.009281) | +0.00866 (+0.007512 to +0.009808) | +0.00787 (+0.006607 to +0.009133) | shown, not judged |
| CPU used with Omni's own (cores), mean | -4.3% (-6.8 to -1.8) | -5.2% (-7.0 to -3.5) | -4.5% (-7.4 to -1.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +4.4% (+2.7 to +6.1) | +6.2% (+3.8 to +8.6) | +4.1% (+2.4 to +5.8) | shown, not judged |
| HPA replicas, mean | +6.7% (+0.7 to +12.8) | +5.9% (−0.6 to +12.5) | +2.5% (−0.7 to +5.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pods started | +27.7% (−4.5 to +59.8) | +16.7% (−18.6 to +52.0) | +17.0% (−7.6 to +41.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | +29.3% (−28.4 to +86.9) | +9.1% (−33.7 to +51.9) | +2.1% (−46.9 to +51.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | +11.8% (−32.7 to +56.3) | −13.1% (−63.8 to +37.6) | −5.0% (−44.8 to +34.8) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -3.7% (-5.8 to -1.7) | -4.2% (-5.6 to -2.7) | -3.8% (-5.9 to -1.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 EVEN, the same, 3 EVEN, under the floor, 3 GAIN by the mean of our three runs, 5 GAIN in all three of our runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
