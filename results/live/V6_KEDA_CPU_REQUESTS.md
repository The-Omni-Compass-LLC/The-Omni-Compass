# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38701101796 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38712444594 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38725705826 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.6 to +0.4) | =0.3% (−0.7 to +0.0) | =0.2% (−0.9 to +0.4) | EVEN, under the floor (the three runs' mean 0.23%) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.5% (+0.7 to +2.2) | +1.6% (+1.1 to +2.0) | +1.2% (+0.1 to +2.2) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.5% (+0.7 to +2.2) | +1.6% (+1.1 to +2.0) | +1.2% (+0.1 to +2.2) | **power given in all three of our runs** |
| response time (ms), mean | +40.8% (+30.4 to +51.3) | +40.0% (+36.5 to +43.6) | +36.7% (+22.6 to +50.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +57.3% (+46.2 to +68.3) | +56.2% (+51.4 to +61.0) | +54.8% (+41.4 to +68.1) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +63.1% (+51.2 to +75.1) | +58.6% (+53.0 to +64.2) | +61.8% (+47.8 to +75.8) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +100.0% (+31.9 to +168.1) | +100.0% (+50.9 to +149.1) | +100.0% (−3.0 to +203.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | +100.0% (−126.2 to +326.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (−0.5 to +200.5) | +100.0% (+7.7 to +192.3) | +100.0% (−28.2 to +228.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +17.4 (+16.9 to +17.9) | +17 (+16.42 to +17.58) | +17.7 (+16.63 to +18.77) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +12.6% (-55.1 to +80.4) | +0.4% (-54.7 to +55.5) | +140.0% (-73.8 to +353.8) | shown, not judged |
| utilisation (used / allocatable) | +30.3% (+22.5 to +38.1) | +35.3% (+31.1 to +39.4) | +27.4% (+18.4 to +36.4) | shown, not judged |
| CPU used (cores), mean | +30.3% (+22.5 to +38.1) | +35.3% (+31.1 to +39.4) | +27.4% (+18.4 to +36.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01199 (+0.01053 to +0.01345) | +0.0126 (+0.01154 to +0.01366) | +0.01119 (+0.009678 to +0.0127) | shown, not judged |
| CPU used with Omni's own (cores), mean | +31.6% (+23.7 to +39.5) | +36.6% (+32.4 to +40.9) | +28.7% (+19.5 to +37.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -21.3% (-25.6 to -17.0) | -24.5% (-26.5 to -22.5) | -19.2% (-23.1 to -15.3) | shown, not judged |
| HPA replicas, mean | +3.0% (+1.2 to +4.8) | +3.5% (+1.9 to +5.2) | +1.6% (−1.8 to +5.1) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pods started | =0.0% (−15.1 to +15.1) | +8.7% (−12.3 to +29.7) | +4.2% (−11.2 to +19.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, total (s) | −5.0% (−57.0 to +47.0) | −17.5% (−85.9 to +51.0) | −33.6% (−79.9 to +12.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| pod start wait, mean (s) | −4.3% (−45.7 to +37.0) | −9.6% (−59.3 to +40.0) | −27.3% (−60.3 to +5.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +29.1% (+21.8 to +36.3) | +34.7% (+31.0 to +38.3) | +26.0% (+18.6 to +33.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 3 GAIN by the mean of our three runs, 3 GAIN in all three of our runs, 2 LOSS by the mean of our three runs, 2 power given by the mean of our three runs, 2 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
