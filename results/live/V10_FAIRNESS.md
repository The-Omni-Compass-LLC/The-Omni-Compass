# Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107190192 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39114217887 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122528801 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.3% (+0.1 to +0.4) | =0.1% (−0.3 to +0.5) | =0.2% (−0.0 to +0.5) | EVEN, under the floor (the three runs' mean 0.19%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.2 to +0.3) | =0.1% (−0.4 to +0.5) | =0.1% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.0% (−0.2 to +0.3) | =0.1% (−0.4 to +0.5) | =0.1% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| response time (ms), mean | +14.7% (+6.6 to +22.8) | +9.6% (−1.2 to +20.5) | +14.0% (+6.1 to +21.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 95th percentile | +11.5% (+2.2 to +20.9) | −3.9% (−19.1 to +11.3) | +3.3% (−12.1 to +18.7) | **the runs disagree** |
| response time (ms), 99th percentile | +1.9% (−6.9 to +10.7) | +4.1% (−12.7 to +20.9) | +11.8% (−3.6 to +27.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +10.6% (+4.8 to +16.3) | +11.1% (+4.2 to +18.0) | +11.0% (+3.3 to +18.6) | **GAIN in all three of our runs** |
| failed requests (%) | +3.8% (−20.6 to +28.2) | +11.6% (−16.9 to +40.2) | −0.8% (−16.6 to +15.0) | **the runs disagree** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +7.7% (+3.9 to +11.5) | +4.9% (−0.1 to +9.8) | +7.0% (+1.2 to +12.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +33.1 (+31.09 to +35.11) | +33.2 (+31.86 to +34.54) | +33.1 (+31.3 to +34.9) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +37.2% (-36.8 to +111.2) | +77.9% (-35.4 to +191.3) | -7.8% (-82.8 to +67.3) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-3.2 to -0.2) | -0.4% (-1.0 to +0.1) | -1.5% (-2.8 to -0.1) | shown, not judged |
| CPU used (cores), mean | -1.7% (-3.2 to -0.2) | -0.4% (-1.0 to +0.1) | -1.5% (-2.8 to -0.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0114 (+0.01008 to +0.01272) | +0.01185 (+0.01126 to +0.01244) | +0.01069 (+0.009419 to +0.01196) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.3% (-2.8 to +0.3) | +0.0% (-0.5 to +0.6) | -1.0% (-2.4 to +0.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.4% (-0.2 to +5.0) | +0.4% (-0.1 to +0.9) | +1.8% (-0.3 to +4.0) | shown, not judged |
| HPA replicas, mean | +0.9% (−0.4 to +2.2) | +2.7% (−0.0 to +5.5) | +1.0% (−1.2 to +3.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | +24.4% (+0.2 to +48.7) | +21.6% (−2.1 to +45.4) | +26.5% (+4.7 to +48.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, total (s) | +31.7% (+3.0 to +60.4) | +21.2% (−19.4 to +61.8) | +23.0% (−3.8 to +49.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | +8.8% (−14.6 to +32.1) | −4.1% (−34.4 to +26.2) | −2.8% (−31.3 to +25.6) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -0.5% (-1.3 to +0.3) | +0.2% (-0.5 to +0.8) | -0.5% (-1.5 to +0.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | −0.9% (−12.4 to +10.7) | +0.7% (−6.9 to +8.3) | +7.3% (−4.8 to +19.5) | **the runs disagree** |
| second app: response time (ms), 99th percentile | −86.2% (−1.0 to −171.4) | +1.3% (−41.6 to +44.1) | +41.8% (−18.1 to +101.7) | **the runs disagree** |
| second app: time over the response line (% of samples) | −1.2% (−3.8 to +1.5) | =0.4% (−2.1 to +2.8) | +2.9% (+0.2 to +5.7) | **the runs disagree** |
| second app: failed requests (%) | +1.3% (−1.9 to +4.4) | −1.9% (−4.0 to +0.2) | −0.8% (−4.4 to +2.7) | **the runs disagree** |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 5 GAIN by the mean of our three runs, 1 GAIN in all three of our runs, 1 power given by the mean of our three runs, 9 shown, not judged, 7 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
