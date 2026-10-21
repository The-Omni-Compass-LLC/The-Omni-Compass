# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38697567716 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38708517967 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38721995611 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.3% (-0.0 to +0.7) | -0.2% (-0.7 to +0.4) | +0.2% (-0.3 to +0.6) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.7% (+2.2 to +3.2) | +1.8% (+1.2 to +2.4) | +2.4% (+1.7 to +3.0) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.7% (+2.2 to +3.2) | +1.8% (+1.2 to +2.4) | +2.4% (+1.7 to +3.0) | **power given in all three of our runs** |
| response time (ms), mean | -46.0% (-52.1 to -39.9) | -44.9% (-57.6 to -32.1) | -46.6% (-55.6 to -37.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -57.9% (-65.0 to -50.9) | -59.8% (-71.6 to -48.0) | -61.3% (-70.6 to -51.9) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -65.2% (-72.7 to -57.8) | -69.1% (-81.2 to -57.0) | -67.4% (-76.5 to -58.3) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -98.7% (-138.5 to -58.8) | -100.0% (-170.2 to -29.8) | -100.0% (-151.2 to -48.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-200.5 to +0.5) | -100.0% (-201.2 to +1.2) | -100.0% (-196.9 to -3.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +15.1 (+13.33 to +16.87) | +16.4 (+13.44 to +19.36) | +16 (+13.64 to +18.36) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.08 (-0.01214 to +0.1721) | +33.3% (-42.1 to +108.7) | +200.0% (-101.6 to +501.6) | shown, not judged |
| utilisation (used / allocatable) | +47.9% (+43.5 to +52.2) | +40.6% (+31.7 to +49.4) | +44.6% (+37.0 to +52.3) | shown, not judged |
| CPU used (cores), mean | +47.9% (+43.5 to +52.2) | +40.6% (+31.7 to +49.4) | +44.6% (+37.0 to +52.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00854 (+0.007949 to +0.009131) | +0.00792 (+0.00717 to +0.00867) | +0.00816 (+0.007314 to +0.009006) | shown, not judged |
| CPU used with Omni's own (cores), mean | +48.9% (+44.5 to +53.3) | +41.6% (+32.6 to +50.5) | +45.6% (+37.9 to +53.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -30.8% (-33.8 to -27.8) | -26.7% (-30.0 to -23.4) | -28.8% (-32.2 to -25.3) | shown, not judged |
| HPA replicas, mean | +1.1% (-0.3 to +2.5) | +0.3% (-2.1 to +2.6) | +0.6% (-1.4 to +2.6) | EVEN, no difference beyond the noise (all three runs) |
| pods started | -66.7% (-120.4 to -12.9) | -42.1% (-108.0 to +23.8) | -45.0% (-119.4 to +29.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, total (s) | -57.1% (-113.9 to -0.4) | -41.4% (-113.8 to +31.0) | -41.9% (-133.6 to +49.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, mean (s) | -21.5% (-90.6 to +47.5) | -47.3% (-107.5 to +12.9) | -40.7% (-112.6 to +31.2) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +44.2% (+40.8 to +47.7) | +37.3% (+29.7 to +44.9) | +41.1% (+34.0 to +48.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 2 power given in all three of our runs, 3 EVEN, no difference beyond the noise (2 of 3 runs), 3 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
