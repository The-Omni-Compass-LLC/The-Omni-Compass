# The KAI scheduler under the batch stream: Omni-Compass on top of KAI's queues (register row 91): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39350900880 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39350907916 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39350915166 | `7dee891c54d1` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +16.2% (+8.3 to +24.1) | +14.7% (+5.1 to +24.2) | +11.1% (+1.5 to +20.8) | **GAIN in all three of our runs** |
| node-hours | +16.2% (+8.2 to +24.1) | +14.4% (+4.9 to +24.0) | +11.1% (+1.2 to +20.9) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.6 to +0.3) | =0.0% (−0.4 to +0.5) | =0.1% (−0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +11.3% (+5.7 to +17.0) | +10.1% (+3.4 to +16.9) | +7.5% (+0.8 to +14.2) | **GAIN in all three of our runs** |
| response time (ms), mean | +22.9% (+19.1 to +26.7) | +20.6% (+16.1 to +25.2) | +21.5% (+15.1 to +27.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +1.3% (−3.1 to +5.7) | −9.9% (−25.4 to +5.7) | =0.1% (−16.7 to +16.9) | **the runs disagree** |
| response time (ms), 99th percentile | −0.7% (−4.7 to +3.4) | −9.7% (−21.7 to +2.4) | −5.7% (−23.3 to +11.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | −8.8% (−42.4 to +24.7) | −42.3% (−93.8 to +9.2) | −6.5% (−60.1 to +47.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −28.6% (−131.3 to +74.2) | −61.1% (−143.7 to +21.5) | =0.0% (−46.2 to +46.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +22.1 (+15.15 to +29.05) | +26.2 (+17.28 to +35.12) | +24.4 (+17.59 to +31.21) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +13.0% (+1.5 to +24.6) | -7.2% (-26.4 to +12.0) | +11.6% (-6.5 to +29.7) | shown, not judged |
| utilisation (used / allocatable) | +15.8% (+7.4 to +24.3) | +12.1% (+2.9 to +21.4) | +14.0% (-1.1 to +29.0) | shown, not judged |
| CPU used (cores), mean | -3.3% (-5.7 to -1.0) | -4.1% (-8.3 to +0.0) | +0.1% (-2.3 to +2.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02092 (+0.01957 to +0.02227) | +0.02089 (+0.01478 to +0.027) | +0.01945 (+0.01805 to +0.02085) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.9% (-4.3 to +0.5) | -2.7% (-6.6 to +1.2) | +1.4% (-1.0 to +3.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -8.5% (-13.5 to -3.5) | -7.1% (-13.8 to -0.4) | -8.8% (-18.6 to +1.0) | shown, not judged |
| HPA replicas, mean | +2.9% (−3.9 to +9.6) | +11.5% (−0.1 to +23.2) | +6.8% (−1.9 to +15.5) | **the runs disagree** |
| pods started | +0.2000 (−0.1016 to +0.5016) | +100.0% (−60.9 to +260.9) | =0.0% (−292.0 to +292.0) | **the runs disagree** |
| pod start wait, total (s) | −0.5000 (−1.2726 to +0.2726) | +100.0% (−60.9 to +260.9) | +25.0% (−247.5 to +297.5) | **the runs disagree** |
| pod start wait, mean (s) | −0.5000 (−1.2726 to +0.2726) | +100.0% (−50.8 to +250.8) | −50.0% (−405.7 to +305.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +2.8% (+1.8 to +3.8) | +1.6% (-0.2 to +3.3) | +1.3% (+0.4 to +2.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | =0.4% (+0.1 to +0.7) | =0.4% (+0.1 to +0.8) | =0.2% (−0.1 to +0.5) | EVEN, under the floor (the three runs' mean 0.34%) |
| batch: worker machines in service after the queue finished, mean | +30.4% (+16.0 to +44.8) | +27.7% (+9.8 to +45.6) | +20.4% (+3.5 to +37.2) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +2.6% (−6.2 to +11.4) | +0.7% (−7.3 to +8.6) | −2.6% (−11.0 to +5.7) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | −20.0% (−50.2 to +10.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| queue: job turnaround, submitted to done, mean (s) | −1.5% (−0.4 to −2.5) | −5.3% (−13.1 to +2.4) | −2.2% (−9.9 to +5.4) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 4 EVEN, the same, 2 EVEN, under the floor, 5 GAIN in all three of our runs, 5 LOSS by the mean of our three runs, 9 shown, not judged, 6 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
