# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38701101796 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38712444594 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38725705826 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.4% (-0.8 to +0.1) | -0.6% (-0.9 to -0.3) | -0.6% (-0.8 to -0.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.1% (+1.5 to +2.7) | +1.7% (+1.0 to +2.4) | +1.6% (+1.0 to +2.3) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.1% (+1.5 to +2.7) | +1.7% (+1.0 to +2.4) | +1.6% (+1.0 to +2.3) | **power given in all three of our runs** |
| response time (ms), mean | -59.0% (-68.8 to -49.3) | -58.7% (-71.0 to -46.5) | -59.5% (-74.3 to -44.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -74.6% (-85.5 to -63.7) | -72.9% (-85.3 to -60.5) | -74.8% (-92.2 to -57.5) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -68.3% (-78.3 to -58.4) | -70.2% (-82.0 to -58.4) | -74.0% (-90.9 to -57.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -96.9% (-141.2 to -52.6) | -97.4% (-144.0 to -50.8) | -99.1% (-171.5 to -26.7) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -98.1% (-142.7 to -53.4) | -98.0% (-149.1 to -46.9) | -100.0% (-168.3 to -31.7) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.3 (+3.954 to +4.646) | +4.3 (+3.954 to +4.646) | +4.7 (+3.579 to +5.821) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -12.6% (-100.8 to +75.7) | +11.6% (-66.1 to +89.3) | +11.8% (-33.3 to +56.8) | shown, not judged |
| utilisation (used / allocatable) | +55.4% (+47.6 to +63.3) | +51.3% (+41.7 to +60.9) | +52.5% (+41.6 to +63.3) | shown, not judged |
| CPU used (cores), mean | +55.4% (+47.6 to +63.3) | +51.3% (+41.7 to +60.9) | +52.5% (+41.6 to +63.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00915 (+0.008066 to +0.01023) | +0.00945 (+0.008233 to +0.01067) | +0.00886 (+0.007459 to +0.01026) | shown, not judged |
| CPU used with Omni's own (cores), mean | +56.7% (+48.7 to +64.6) | +52.6% (+42.8 to +62.3) | +53.7% (+42.6 to +64.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -33.6% (-36.5 to -30.8) | -31.6% (-33.8 to -29.3) | -32.1% (-35.2 to -29.1) | shown, not judged |
| HPA replicas, mean | -15.5% (-22.7 to -8.3) | -17.6% (-23.5 to -11.6) | -11.1% (-17.4 to -4.8) | **GAIN in all three of our runs** |
| pods started | -14.8% (-33.3 to +3.7) | -20.7% (-33.4 to -8.0) | -11.5% (-24.8 to +1.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, total (s) | -3.7% (-30.8 to +23.3) | -10.9% (-33.1 to +11.2) | +9.1% (-14.1 to +32.3) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +12.5% (+2.3 to +22.7) | +12.0% (-5.1 to +29.2) | +22.7% (+7.9 to +37.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU busy, the real machine under kind (%) | +49.1% (+41.4 to +56.9) | +47.1% (+38.2 to +55.9) | +47.6% (+38.4 to +56.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 6 GAIN in all three of our runs, 2 power given in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 1 EVEN, no difference beyond the noise (2 of 3 runs), 1 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
