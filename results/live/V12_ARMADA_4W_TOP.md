# Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Armada against Armada as shipped (register row 94): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39482335827 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39482351075 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39482365814 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +39.9% (+35.0 to +44.8) | +40.3% (+37.5 to +43.2) | +42.5% (+40.2 to +44.8) | **GAIN in all three of our runs** |
| node-hours | +39.9% (+34.9 to +44.9) | +40.3% (+37.3 to +43.2) | +42.5% (+40.1 to +44.8) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.2 to +0.3) | =0.1% (−0.1 to +0.3) | =0.0% (−0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +29.8% (+26.0 to +33.5) | +30.0% (+27.8 to +32.3) | +31.8% (+30.0 to +33.5) | **GAIN in all three of our runs** |
| response time (ms), mean | +42.0% (+32.0 to +52.1) | +41.7% (+37.7 to +45.8) | +41.0% (+29.2 to +52.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +45.4% (+35.2 to +55.6) | +44.1% (+40.2 to +48.0) | +45.1% (+32.1 to +58.1) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +35.0% (+25.3 to +44.7) | +27.1% (+20.3 to +33.8) | +34.3% (+26.5 to +42.2) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +100.0% (−130.6 to +330.6) | −0.0036 (−0.0117 to +0.0045) | −0.0036 (−0.0117 to +0.0045) | **the runs disagree** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| settings commands the governor wrote on its own (no person touched either arm) | +25.56 (+24.06 to +27.05) | +25.5 (+23.98 to +27.02) | +24.2 (+23.14 to +25.26) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.02778 (-0.03628 to +0.09183) | +0.05333 (-0.06731 to +0.174) | -100.0% (-326.2 to +126.2) | shown, not judged |
| utilisation (used / allocatable) | +42.6% (+36.0 to +49.2) | +45.7% (+41.8 to +49.5) | +43.7% (+36.9 to +50.5) | shown, not judged |
| CPU used (cores), mean | -14.0% (-16.3 to -11.6) | -12.9% (-15.1 to -10.7) | -17.0% (-18.7 to -15.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.008889 (+0.007841 to +0.009937) | +0.00954 (+0.008604 to +0.01048) | +0.0082 (+0.006926 to +0.009474) | shown, not judged |
| CPU used with Omni's own (cores), mean | -10.9% (-13.3 to -8.5) | -9.8% (-12.2 to -7.5) | -13.9% (-15.5 to -12.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -18.1% (-21.3 to -14.9) | -19.5% (-21.3 to -17.6) | -17.2% (-19.5 to -14.8) | shown, not judged |
| HPA replicas, mean | +6.5% (+0.1 to +12.8) | +7.0% (+1.1 to +12.9) | +1.8% (−2.0 to +5.7) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +650.0% (−22.3 to +1322.3) | +1.4000 (+0.7968 to +2.0032) | +57.1% (−159.4 to +273.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −400.0% (−879.7 to +79.7) | −2.3000 (−1.0361 to −3.5639) | −6.7% (−181.4 to +168.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −425.0% (−869.7 to +19.7) | −1.4000 (−0.9291 to −1.8709) | +0.9% (−147.4 to +149.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +6.7% (+4.6 to +8.7) | +8.2% (+5.6 to +10.9) | +6.2% (+3.8 to +8.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.1% (−0.4 to +0.2) | =0.1% (−0.1 to +0.3) | =0.0% (−0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.01%) |
| queue: job wait, submitted to its first pod running, mean (s) | =0.2% (−0.6 to +0.2) | =0.1% (−0.1 to +0.4) | =0.0% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | =0.1% (−0.4 to +0.2) | =0.1% (−0.1 to +0.3) | =0.0% (−0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.00%) |
| queue: job turnaround, submitted to done, mean (s) | =0.2% (−0.6 to +0.2) | =0.1% (−0.1 to +0.4) | =0.0% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| queue: jobs unfinished at the window's end | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | EVEN, the same |

Readings: 5 EVEN, the same, 5 EVEN, under the floor, 6 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
