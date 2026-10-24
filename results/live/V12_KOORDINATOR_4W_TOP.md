# Koordinator under the batch stream, the four ways: Omni-Compass on top of Koordinator against Koordinator as shipped (register row 89): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +2.5% (−1.1 to +6.2) | =0.4% (−1.2 to +0.3) | +1.4% (−1.8 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| node-hours | +2.4% (−1.5 to +6.3) | +0.6% (−0.1 to +1.2) | +1.5% (−1.4 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.3 to +0.3) | =0.1% (−0.4 to +0.2) | =0.1% (−0.6 to +0.4) | EVEN, under the floor (the three runs' mean 0.06%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.8% (−1.0 to +4.5) | =0.4% (−0.9 to +0.1) | +1.1% (−0.9 to +3.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), mean | +27.1% (+19.8 to +34.5) | +24.7% (+18.9 to +30.5) | +26.7% (+22.7 to +30.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +8.9% (+3.5 to +14.3) | +5.6% (−1.7 to +13.0) | +6.6% (+3.8 to +9.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | +5.6% (−2.7 to +13.9) | +3.8% (−4.3 to +11.8) | =0.4% (−7.1 to +8.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +31.1% (−9.6 to +71.8) | −19.5% (−69.1 to +30.1) | −35.6% (−105.4 to +34.1) | **the runs disagree** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | =0.0000 (±0.0000 to ±0.0000) | −100.0% (−506.0 to +306.0) | =0.0% (−337.2 to +337.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +14.2 (+11.13 to +17.27) | +12.5 (+10.84 to +14.16) | +11.4 (+8.555 to +14.25) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +8.0% (-2.2 to +18.2) | +0.6% (-4.4 to +5.7) | +7.4% (+3.1 to +11.8) | shown, not judged |
| utilisation (used / allocatable) | +0.3% (-3.8 to +4.4) | +0.5% (-1.0 to +2.0) | +0.9% (-2.3 to +4.2) | shown, not judged |
| CPU used (cores), mean | -2.0% (-4.7 to +0.8) | +0.1% (-1.3 to +1.6) | -0.2% (-2.7 to +2.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01124 (+0.01006 to +0.01242) | +0.01219 (+0.01113 to +0.01325) | +0.01196 (+0.01105 to +0.01287) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.1% (-3.8 to +1.6) | +1.0% (-0.5 to +2.5) | +0.6% (-1.8 to +3.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.2% (-3.6 to +3.3) | -0.4% (-1.7 to +1.0) | -0.9% (-4.0 to +2.1) | shown, not judged |
| HPA replicas, mean | +1.7% (−3.3 to +6.8) | +3.1% (−2.8 to +9.0) | +2.2% (−6.2 to +10.7) | **the runs disagree** |
| pods started | +60.0% (−36.6 to +156.6) | +200.0% (−252.4 to +652.4) | +0.1000 (−0.1262 to +0.3262) | **the runs disagree** |
| pod start wait, total (s) | +72.7% (−32.6 to +178.0) | −133.3% (−525.9 to +259.3) | −0.2000 (−0.6524 to +0.2524) | **the runs disagree** |
| pod start wait, mean (s) | +76.9% (−26.8 to +180.7) | −133.3% (−525.9 to +259.3) | −0.2000 (−0.6524 to +0.2524) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +0.5% (-1.8 to +2.8) | +0.7% (-0.5 to +2.0) | +0.7% (-1.5 to +2.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −1.8% (−7.2 to +3.7) | =0.0% (−0.8 to +0.8) | −1.8% (−4.8 to +1.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| batch: worker machines in service after the queue finished, mean | +9.7% (−4.1 to +23.5) | +6.2% (−11.3 to +23.8) | +11.0% (−36.2 to +58.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job wait, submitted to its first pod running, mean (s) | −7.1% (−42.2 to +28.1) | −2.2% (−25.7 to +21.2) | +2.5% (−24.5 to +29.5) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −0.9% (−33.7 to +31.9) | +4.3% (−18.2 to +26.7) | +2.0% (−24.3 to +28.3) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −5.9% (−14.1 to +2.3) | −1.9% (−8.5 to +4.7) | −3.4% (−7.8 to +1.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: jobs unfinished at the window's end | −8.2% (−44.1 to +27.7) | −13.8% (−1.4 to −26.3) | +8.3% (−11.5 to +28.1) | **the runs disagree** |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 6 GAIN by the mean of our three runs, 1 GAIN in all three of our runs, 3 LOSS by the mean of our three runs, 9 shown, not judged, 8 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
