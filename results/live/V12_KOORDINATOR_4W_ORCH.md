# Koordinator under the batch stream, the four ways: Koordinator as shipped against the organism alone (register row 89): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for the orchestrator as shipped and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39368366066 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39368373713 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39368380786 | `cf4235e29cb4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to −0.0) | =0.0% (−0.0 to −0.0) | =0.0% (−0.0 to −0.0) | EVEN, the same |
| node-hours | =0.0% (−0.3 to +0.2) | =0.4% (+0.2 to +0.6) | =0.1% (−0.4 to +0.5) | EVEN, under the floor (the three runs' mean 0.15%) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.6% (+0.3 to +1.0) | =0.1% (−0.6 to +0.8) | =0.2% (−0.3 to +0.7) | EVEN, under the floor (the three runs' mean 0.33%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.6% (+0.3 to +1.0) | =0.1% (−0.6 to +0.8) | =0.2% (−0.3 to +0.7) | EVEN, under the floor (the three runs' mean 0.33%) |
| response time (ms), mean | +39.6% (+10.6 to +68.6) | +63.0% (+25.1 to +101.0) | +49.2% (+20.6 to +77.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +63.7% (+18.9 to +108.5) | +81.7% (+30.7 to +132.8) | +72.6% (+29.3 to +115.8) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +62.1% (+20.5 to +103.7) | +81.6% (+32.1 to +131.0) | +73.1% (+30.4 to +115.8) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +97.8% (−2.0 to +197.7) | +98.7% (+39.1 to +158.3) | +98.8% (+42.5 to +155.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+17.8 to +182.2) | +98.9% (+43.9 to +153.8) | +98.9% (+59.6 to +138.3) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +9533.6% (+6049.1 to +13018.2) | +11180.9% (+8457.9 to +13904.0) | +10871.5% (+7838.4 to +13904.6) | shown, not judged |
| utilisation (used / allocatable) | +12.9% (+5.0 to +20.8) | -1.9% (-12.8 to +8.9) | +3.4% (-3.3 to +10.1) | shown, not judged |
| CPU used (cores), mean | +12.9% (+5.0 to +20.8) | -1.9% (-12.8 to +8.9) | +3.4% (-3.3 to +10.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| CPU used with Omni's own (cores), mean | +12.9% (+5.0 to +20.8) | -1.9% (-12.8 to +8.9) | +3.4% (-3.3 to +10.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -13.5% (-23.1 to -4.0) | -0.7% (-11.3 to +9.9) | -4.2% (-10.3 to +2.0) | shown, not judged |
| HPA replicas, mean | +2.0% (−4.4 to +8.5) | +2.7% (−3.6 to +8.9) | +0.8% (−4.6 to +6.2) | **the runs disagree** |
| pods started | +400.0% (−100.1 to +900.1) | +0.1000 (−0.1262 to +0.3262) | +100.0% (−126.2 to +326.2) | **the runs disagree** |
| pod start wait, total (s) | −450.0% (−1044.9 to +144.9) | −0.3000 (−0.9786 to +0.3786) | +100.0% (−126.2 to +326.2) | **the runs disagree** |
| pod start wait, mean (s) | −225.0% (−566.9 to +116.9) | −0.3000 (−0.9786 to +0.3786) | +100.0% (−126.2 to +326.2) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +18.3% (+13.4 to +23.3) | +7.6% (-0.7 to +15.9) | +12.6% (+8.1 to +17.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | −76.5% (−54.1 to −98.9) | −82.5% (−72.8 to −92.1) | −86.9% (−68.4 to −105.4) | **LOSS in all three of our runs** |
| batch: worker machines in service after the queue finished, mean | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | =0.0% (±0.0 to ±0.0) | EVEN, the same |
| queue: job wait, submitted to its first pod running, mean (s) | −310637.5% (−166814.0 to −454461.0) | −686083.3% (−439006.5 to −933160.2) | −233933.3% (−162122.7 to −305743.9) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | −171200.0% (−91149.9 to −251250.1) | −797900.0% (−545467.5 to −1050332.5) | −139600.0% (−101748.5 to −177451.5) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | −1512.7% (−1011.0 to −2014.4) | −831.8% (−691.5 to −972.0) | −1276.6% (−979.1 to −1574.2) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | −4.9000 (−10.5971 to +0.7971) | −9.4000 (−3.5091 to −15.2909) | −9.6000 (−3.5005 to −15.6995) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |

Readings: 5 EVEN, the same, 3 EVEN, under the floor, 1 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 4 LOSS in all three of our runs, 9 shown, not judged, 4 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
