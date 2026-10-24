# Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38933412682 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38943569010 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38955570717 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.2 to +0.2) | =0.3% (+0.1 to +0.4) | =0.1% (−0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.14%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.3 to +0.1) | =0.2% (−0.1 to +0.5) | =0.1% (−0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.08%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.1% (−0.3 to +0.1) | =0.2% (−0.1 to +0.5) | =0.1% (−0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.08%) |
| response time (ms), mean | +16.9% (+7.4 to +26.3) | +9.1% (−0.1 to +18.3) | +9.8% (+4.3 to +15.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 95th percentile | +2.6% (−14.1 to +19.4) | −6.7% (−31.0 to +17.5) | =0.3% (−10.4 to +11.1) | **the runs disagree** |
| response time (ms), 99th percentile | +4.0% (−10.7 to +18.8) | −2.7% (−15.9 to +10.6) | −3.5% (−15.9 to +8.9) | **the runs disagree** |
| time over the response line (% of samples) | +14.7% (+9.1 to +20.3) | +11.9% (+4.8 to +19.1) | +4.7% (−2.4 to +11.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | −3.9% (−28.1 to +20.2) | +24.8% (+7.1 to +42.4) | +10.5% (−18.9 to +39.8) | **the runs disagree** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +5.0% (−0.1 to +10.0) | +8.4% (+1.5 to +15.3) | +3.3% (−2.0 to +8.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +32.2 (+29.75 to +34.65) | +32.8 (+30.33 to +35.27) | +32.8 (+30.81 to +34.79) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +13.9% (-72.2 to +100.0) | +31.4% (-91.2 to +153.9) | -35.0% (-117.2 to +47.2) | shown, not judged |
| utilisation (used / allocatable) | -1.0% (-1.6 to -0.3) | -1.3% (-2.6 to +0.0) | -0.4% (-1.8 to +1.0) | shown, not judged |
| CPU used (cores), mean | -1.0% (-1.6 to -0.3) | -1.3% (-2.6 to +0.0) | -0.4% (-1.8 to +1.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01157 (+0.01081 to +0.01233) | +0.01154 (+0.01037 to +0.01271) | +0.01073 (+0.009713 to +0.01175) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.5% (-1.2 to +0.2) | -0.8% (-2.1 to +0.5) | +0.1% (-1.4 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.9% (+0.3 to +1.5) | +1.6% (-0.4 to +3.6) | +0.3% (-1.1 to +1.7) | shown, not judged |
| HPA replicas, mean | +1.8% (−0.6 to +4.1) | +0.7% (−1.6 to +2.9) | +0.7% (−1.0 to +2.4) | **the runs disagree** |
| pods started | +45.0% (+13.7 to +76.3) | +20.5% (−10.6 to +51.5) | +6.8% (−14.9 to +28.6) | **the runs disagree** |
| pod start wait, total (s) | +37.1% (−10.3 to +84.6) | +21.4% (−15.5 to +58.4) | −10.5% (−49.1 to +28.1) | **the runs disagree** |
| pod start wait, mean (s) | −7.0% (−48.7 to +34.7) | +16.3% (−13.7 to +46.4) | −7.4% (−36.4 to +21.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +0.1% (-0.6 to +0.8) | -0.1% (-1.4 to +1.1) | -0.1% (-1.2 to +1.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | −5.9% (−14.8 to +3.0) | −6.0% (−16.8 to +4.8) | −4.5% (−19.8 to +10.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| second app: response time (ms), 99th percentile | +24.5% (−71.6 to +120.5) | −27.4% (−100.2 to +45.4) | +11.1% (−51.1 to +73.4) | **the runs disagree** |
| second app: time over the response line (% of samples) | =0.1% (−3.5 to +3.8) | −2.0% (−7.0 to +3.1) | −0.8% (−4.2 to +2.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| second app: failed requests (%) | −1.2% (−4.3 to +1.9) | =0.4% (−2.8 to +3.6) | −1.6% (−7.9 to +4.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 3 GAIN by the mean of our three runs, 3 LOSS by the mean of our three runs, 9 shown, not judged, 8 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
