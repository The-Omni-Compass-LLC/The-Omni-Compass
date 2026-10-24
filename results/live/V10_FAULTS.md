# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107193417 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115232348 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122532509 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.1% (−0.2 to +0.0) | =0.1% (−0.0 to +0.2) | =0.0% (−0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| node-hours | =0.2% (−0.8 to +0.4) | =0.1% (−0.4 to +0.6) | =0.3% (−0.8 to +0.1) | EVEN, under the floor (the three runs' mean 0.14%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.3% (−0.8 to +0.3) | =0.3% (−0.9 to +0.2) | =0.4% (−0.9 to +0.0) | EVEN, under the floor (the three runs' mean 0.35%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.3% (−0.9 to +0.3) | =0.3% (−0.8 to +0.2) | =0.4% (−0.9 to +0.0) | EVEN, under the floor (the three runs' mean 0.35%) |
| response time (ms), mean | +33.0% (+15.7 to +50.2) | +32.7% (+7.9 to +57.5) | +40.5% (+11.0 to +70.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +56.4% (+48.8 to +64.0) | +63.2% (+48.9 to +77.5) | +54.0% (+39.7 to +68.3) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +48.6% (+7.7 to +89.6) | +43.0% (+6.8 to +79.3) | +51.2% (+3.5 to +98.8) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +26.4% (+9.9 to +43.0) | +31.5% (+14.7 to +48.2) | +26.9% (+12.1 to +41.7) | **GAIN in all three of our runs** |
| failed requests (%) | +8.2% (−2.4 to +18.7) | +14.5% (+5.7 to +23.3) | +15.0% (+2.2 to +27.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +12.5% (−1.2 to +26.2) | +19.7% (+5.3 to +34.1) | +20.3% (+4.5 to +36.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +32.5 (+27.06 to +37.94) | +27.7 (+24.36 to +31.04) | +29.4 (+24.85 to +33.95) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +220.1% (+31.0 to +409.3) | -44.9% (-94.8 to +5.1) | -20.2% (-109.6 to +69.3) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-3.5 to +0.0) | -3.7% (-7.1 to -0.3) | -1.2% (-4.0 to +1.6) | shown, not judged |
| CPU used (cores), mean | -1.8% (-3.5 to -0.0) | -3.6% (-7.0 to -0.3) | -1.2% (-4.0 to +1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00972 (+0.008402 to +0.01104) | +0.01012 (+0.009436 to +0.0108) | +0.00935 (+0.008016 to +0.01068) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.2% (-2.9 to +0.5) | -3.1% (-6.4 to +0.3) | -0.6% (-3.4 to +2.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.1% (-0.3 to +2.6) | +3.0% (+0.2 to +5.8) | +0.2% (-3.4 to +3.7) | shown, not judged |
| HPA replicas, mean | +20.4% (+10.5 to +30.3) | +15.1% (+7.1 to +23.0) | +13.6% (+0.5 to +26.7) | **power given in all three of our runs** |
| pods started | +52.0% (+20.2 to +83.8) | +12.0% (−16.8 to +40.8) | +17.3% (−8.2 to +42.8) | **the runs disagree** |
| pod start wait, total (s) | −89.7% (−214.9 to +35.6) | +50.4% (−9.0 to +109.8) | +35.6% (−32.3 to +103.6) | **the runs disagree** |
| pod start wait, mean (s) | −39.6% (−130.7 to +51.6) | +50.5% (−7.2 to +108.3) | +45.8% (−31.0 to +122.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -0.5% (-1.8 to +0.8) | -2.8% (-5.4 to -0.2) | -0.5% (-2.7 to +1.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 2 EVEN, the same, 4 EVEN, under the floor, 2 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 1 power given in all three of our runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
