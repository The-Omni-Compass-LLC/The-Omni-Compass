# Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Karmada against Karmada as shipped (register row 95): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438525862 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39438541616 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438559009 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +8.9% (−1.3 to +19.0) | +8.8% (−1.7 to +19.3) | +15.3% (+1.1 to +29.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| node-hours | +8.8% (−1.4 to +18.9) | +8.6% (−1.8 to +19.1) | +15.2% (+0.7 to +29.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | =0.4% (−0.1 to +0.9) | =0.3% (−0.0 to +0.7) | =0.0% (−0.4 to +0.4) | EVEN, under the floor (the three runs' mean 0.26%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +6.0% (−1.4 to +13.3) | +6.0% (−1.5 to +13.5) | +11.0% (+0.5 to +21.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), mean | −13.9% (−28.2 to +0.4) | −10.5% (−21.6 to +0.5) | −2.7% (−13.9 to +8.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 95th percentile | −20.0% (−4.1 to −35.9) | −16.7% (−1.6 to −31.8) | −2.5% (−11.3 to +6.2) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | −12.0% (−1.8 to −22.1) | −11.1% (−1.2 to −21.0) | −4.0% (−12.2 to +4.2) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| time over the response line (% of samples) | −4.9% (−10.0 to +0.1) | −5.4% (−1.7 to −9.1) | −8.3% (−24.3 to +7.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| failed requests (%) | −93.2% (−189.8 to +3.5) | −177.2% (−413.2 to +58.9) | −187.3% (−444.8 to +70.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | −8.0% (−0.1 to −15.9) | −10.1% (−3.6 to −16.7) | +0.7% (−25.6 to +27.1) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +43.11 (+37.35 to +48.87) | +44.3 (+31.46 to +57.14) | +48.2 (+35.57 to +60.83) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -23.0% (-94.4 to +48.5) | +12.1% (-57.8 to +82.0) | +41.5% (-16.0 to +99.0) | shown, not judged |
| utilisation (used / allocatable) | +14.7% (+3.8 to +25.7) | +12.2% (-0.5 to +24.8) | +14.3% (-2.6 to +31.1) | shown, not judged |
| CPU used (cores), mean | +4.8% (-1.8 to +11.4) | +1.8% (-3.9 to +7.4) | -4.1% (-10.1 to +2.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0099 (+0.008994 to +0.01081) | +0.00974 (+0.008487 to +0.01099) | +0.0097 (+0.008547 to +0.01085) | shown, not judged |
| CPU used with Omni's own (cores), mean | +5.4% (-1.2 to +12.0) | +2.4% (-3.3 to +8.0) | -3.5% (-9.5 to +2.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -10.5% (-18.2 to -2.8) | -8.8% (-18.1 to +0.6) | -9.2% (-21.3 to +2.9) | shown, not judged |
| HPA replicas, mean | +11.7% (+2.1 to +21.3) | +8.4% (−3.1 to +19.9) | +15.0% (+3.1 to +26.9) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | +300.0% (−157.6 to +757.6) | +120.0% (−125.0 to +365.0) | +150.0% (−119.2 to +419.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −250.0% (−712.5 to +212.5) | −72.7% (−291.2 to +145.8) | −100.0% (−364.5 to +164.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | −32.1% (−211.2 to +147.0) | −59.0% (−238.9 to +121.0) | −44.1% (−219.6 to +131.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +4.7% (+3.0 to +6.3) | +4.8% (+3.2 to +6.4) | +2.5% (-2.1 to +7.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −4.3% (−1.8 to −6.8) | −4.1% (−1.8 to −6.3) | −3.0% (−6.4 to +0.3) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| batch: worker machines in service after the queue finished, mean | +16.5% (−1.4 to +34.4) | +16.1% (−1.7 to +33.9) | +25.3% (+1.9 to +48.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| queue: job wait, submitted to its first pod running, mean (s) | +42.8% (−59.0 to +144.6) | −75.2% (−241.5 to +91.1) | −65.1% (−130.7 to +0.4) | **the runs disagree** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +95.8% (−127.4 to +319.0) | −13.3% (−33.4 to +6.8) | −89.9% (−239.9 to +60.1) | **the runs disagree** |
| queue: job turnaround, submitted to done, mean (s) | −15.7% (−5.9 to −25.6) | −14.2% (−6.1 to −22.2) | −9.6% (−20.8 to +1.7) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| queue: jobs unfinished at the window's end | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 4 GAIN by the mean of our three runs, 9 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 9 shown, not judged, 3 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
