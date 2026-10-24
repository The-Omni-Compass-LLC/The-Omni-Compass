# Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 90): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on the organism alone and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438326588 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39438344234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438362894 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (+0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.4 to +0.3) | =0.2% (−0.7 to +0.4) | =0.2% (+0.0 to +0.3) | EVEN, under the floor (the three runs' mean 0.01%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.0% (−0.4 to +0.4) | =0.2% (−0.7 to +0.4) | =0.3% (+0.0 to +0.5) | EVEN, under the floor (the three runs' mean 0.03%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.0% (−0.4 to +0.4) | =0.2% (−0.7 to +0.4) | =0.3% (+0.0 to +0.5) | EVEN, under the floor (the three runs' mean 0.03%) |
| response time (ms), mean | +2.1% (−0.1 to +4.3) | =0.0% (−2.8 to +2.7) | +1.7% (+0.3 to +3.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| response time (ms), 95th percentile | +3.3% (+0.4 to +6.2) | +1.8% (−3.1 to +6.8) | +4.6% (+0.9 to +8.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | +3.8% (−1.7 to +9.3) | −3.4% (−0.3 to −6.5) | +5.7% (+1.9 to +9.5) | **the runs disagree** |
| time over the response line (% of samples) | +22.2% (−24.6 to +69.0) | +26.8% (−20.3 to +73.8) | +23.8% (−7.7 to +55.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +66.7% (−33.9 to +167.2) | =0.0000 (±0.0000 to ±0.0000) | +100.0% (−15.2 to +215.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +2.6 (+0.8414 to +4.359) | +1.2 (+0.2583 to +2.142) | +1.5 (+0.5315 to +2.469) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +11.1% (-98.8 to +121.1) | +99.1% (-51.3 to +249.6) | +37.0% (-57.8 to +131.8) | shown, not judged |
| utilisation (used / allocatable) | +0.9% (-0.9 to +2.7) | +0.1% (-1.5 to +1.8) | +1.7% (+0.1 to +3.2) | shown, not judged |
| CPU used (cores), mean | +0.9% (-0.9 to +2.7) | +0.1% (-1.5 to +1.8) | +1.7% (+0.1 to +3.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00617 (+0.005381 to +0.006959) | +0.00568 (+0.004916 to +0.006444) | +0.00596 (+0.005506 to +0.006414) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.6% (-0.3 to +3.4) | +0.8% (-0.9 to +2.4) | +2.3% (+0.7 to +3.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.6% (-2.5 to +1.2) | +0.0% (-1.6 to +1.6) | -1.5% (-2.9 to -0.1) | shown, not judged |
| HPA replicas, mean | +15.8% (+8.0 to +23.7) | +9.0% (+1.9 to +16.1) | +11.4% (+4.6 to +18.2) | **power given in all three of our runs** |
| pods started | +78.0% (+34.7 to +121.4) | +34.7% (−10.5 to +79.8) | +57.8% (+18.0 to +97.6) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, total (s) | −60.3% (−15.0 to −105.6) | −28.7% (−80.0 to +22.5) | −69.0% (−30.9 to −107.1) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, mean (s) | +10.0% (−15.1 to +35.1) | +5.9% (−10.0 to +21.7) | −7.8% (−25.7 to +10.1) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +1.9% (-0.1 to +3.9) | +1.9% (+0.1 to +3.6) | +2.7% (+1.1 to +4.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 EVEN, the same, 3 EVEN, under the floor, 4 GAIN by the mean of our three runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
