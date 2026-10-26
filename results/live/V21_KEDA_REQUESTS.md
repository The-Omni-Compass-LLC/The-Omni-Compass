# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 40232040937 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| B | 40254201062 | `babd7a2ceac0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |
| C | 40276902708 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.2% (−0.5 to +0.2) | =0.3% (−0.7 to +0.1) | =0.4% (−0.8 to −0.0) | EVEN, under the floor (the three runs' mean 0.29%) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.4% (+1.9 to +2.9) | +2.1% (+1.5 to +2.7) | +1.9% (+1.2 to +2.5) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.4% (+1.9 to +2.9) | +2.1% (+1.5 to +2.7) | +1.9% (+1.2 to +2.5) | **power given in all three of our runs** |
| response time (ms), mean | +58.3% (+51.1 to +65.5) | +57.5% (+45.9 to +69.0) | +57.2% (+44.0 to +70.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +73.6% (+65.8 to +81.4) | +72.6% (+61.1 to +84.2) | +72.7% (+59.8 to +85.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +63.4% (+54.4 to +72.3) | +60.2% (+43.0 to +77.4) | +66.3% (+56.2 to +76.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +97.0% (+62.3 to +131.8) | +94.8% (+55.3 to +134.3) | +97.4% (+33.6 to +161.2) | **GAIN in all three of our runs** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +98.1% (+62.8 to +133.4) | +93.9% (+55.4 to +132.3) | +100.0% (+35.4 to +164.6) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.1000 (+3.8738 to +4.3262) | +5.7000 (+3.4118 to +7.9882) | +5.7000 (+3.4118 to +7.9882) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | −6.2% (−333.0 to +320.5) | −31.9% (−109.6 to +45.8) | −64.4% (−218.6 to +89.8) | shown, not judged |
| utilisation (used / allocatable) | +57.7% (+50.7 to +64.7) | +55.7% (+48.5 to +62.8) | +53.7% (+43.1 to +64.2) | shown, not judged |
| CPU used (cores), mean | +57.7% (+50.7 to +64.7) | +55.7% (+48.5 to +62.8) | +53.7% (+43.1 to +64.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0100 (+0.0090 to +0.0111) | +0.0102 (+0.0089 to +0.0115) | +0.0097 (+0.0081 to +0.0112) | shown, not judged |
| CPU used with Omni's own (cores), mean | +59.1% (+51.9 to +66.2) | +57.1% (+49.7 to +64.4) | +55.0% (+44.3 to +65.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | −34.5% (−35.9 to −33.2) | −33.8% (−35.6 to −32.0) | −32.6% (−34.6 to −30.5) | shown, not judged |
| HPA replicas, mean | +21.2% (+14.0 to +28.4) | +17.7% (+10.8 to +24.6) | +15.2% (+6.4 to +24.1) | **GAIN in all three of our runs** |
| pods started | +25.0% (+12.7 to +37.3) | +20.7% (+8.0 to +33.4) | +23.3% (+7.2 to +39.4) | **GAIN in all three of our runs** |
| pod start wait, total (s) | +26.3% (−5.7 to +58.3) | +21.6% (+6.4 to +36.9) | +25.6% (+1.5 to +49.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pod start wait, mean (s) | +4.8% (−21.6 to +31.2) | +1.3% (−21.6 to +24.2) | +2.3% (−13.4 to +18.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +51.7% (+45.5 to +57.9) | +50.7% (+43.8 to +57.6) | +48.1% (+37.8 to +58.3) | shown, not judged |
| host cores (the real machine under kind) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | ±0.0% (±0.0 to ±0.0) | shown, not judged |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 2 GAIN by the mean of our three runs, 7 GAIN in all three of our runs, 2 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
