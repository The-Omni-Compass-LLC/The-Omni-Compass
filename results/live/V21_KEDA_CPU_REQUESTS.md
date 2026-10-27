# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40232040937 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40254201062 | `babd7a2ceac0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40276902708 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.6 to +0.4) | =0.3% (−0.7 to +0.2) | =0.1% (−0.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.09%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.6% (+1.2 to +2.1) | +1.4% (+0.7 to +2.1) | +1.7% (+0.8 to +2.7) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.6% (+1.2 to +2.1) | +1.4% (+0.7 to +2.1) | +1.7% (+0.8 to +2.7) | **power given in all three of our runs** |
| response time (ms), mean | +38.1% (+31.1 to +45.0) | +36.8% (+27.0 to +46.6) | +36.8% (+25.9 to +47.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +52.1% (+46.1 to +58.2) | +51.6% (+42.1 to +61.1) | +50.8% (+42.8 to +58.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +58.4% (+51.2 to +65.6) | +54.0% (+44.1 to +64.0) | +54.5% (+44.6 to +64.4) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +97.4% (+32.7 to +162.1) | +91.2% (+39.7 to +142.7) | +100.0% (+39.1 to +160.9) | **GAIN in all three of our runs** |
| failed requests (%) | +100.0% (−126.2 to +326.2) | −0.0118 (−0.0384 to +0.0148) | =0.0000 (±0.0000 to ±0.0000) | **the runs disagree** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (−50.8 to +250.8) | +100.0% (−126.2 to +326.2) | +100.0% (−15.2 to +215.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +30.6000 (+21.3335 to +39.8665) | +32.4000 (+22.2213 to +42.5787) | +37.0000 (+22.9505 to +51.0495) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +38.5% (−197.5 to +274.6) | −90.9% (−159.5 to −22.4) | −100.0% (−201.8 to +1.8) | shown, not judged |
| utilisation (used / allocatable) | +32.3% (+25.3 to +39.4) | +32.2% (+24.1 to +40.3) | +31.0% (+21.4 to +40.5) | shown, not judged |
| CPU used (cores), mean | +32.3% (+25.3 to +39.4) | +32.2% (+24.1 to +40.3) | +31.0% (+21.4 to +40.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0161 (+0.0131 to +0.0191) | +0.0164 (+0.0129 to +0.0199) | +0.0170 (+0.0127 to +0.0213) | shown, not judged |
| CPU used with Omni's own (cores), mean | +34.2% (+26.9 to +41.4) | +34.1% (+25.7 to +42.5) | +32.9% (+22.9 to +42.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | −22.5% (−26.4 to −18.6) | −22.1% (−26.2 to −18.1) | −21.2% (−26.3 to −16.2) | shown, not judged |
| HPA replicas, mean | +15.9% (+8.5 to +23.3) | +11.5% (+2.0 to +21.0) | +12.9% (+4.8 to +21.0) | **power given in all three of our runs** |
| pods started | +49.0% (+25.9 to +72.0) | +37.3% (+0.2 to +74.3) | +30.8% (−0.5 to +62.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, total (s) | −84.1% (−40.6 to −127.6) | −30.9% (−69.3 to +7.6) | −27.5% (−69.0 to +14.0) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −21.3% (−44.5 to +1.8) | +6.4% (−9.3 to +22.1) | +2.4% (−22.0 to +26.7) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +31.7% (+24.9 to +38.4) | +32.1% (+24.8 to +39.4) | +30.0% (+21.3 to +38.7) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 1 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 power given by the mean of our three runs, 3 power given in all three of our runs, 9 shown, not judged, 2 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
