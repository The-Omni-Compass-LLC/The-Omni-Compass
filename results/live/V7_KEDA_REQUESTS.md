# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38843268161 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38843270386 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38843272786 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| node-hours | -0.2% (-0.7 to +0.3) | -0.3% (-0.7 to +0.1) | -0.2% (-0.6 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.2% (+1.6 to +2.8) | +2.3% (+1.7 to +2.9) | +2.3% (+1.8 to +2.9) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.2% (+1.6 to +2.8) | +2.3% (+1.7 to +2.9) | +2.3% (+1.8 to +2.9) | **power given in all three of our runs** |
| response time (ms), mean | -57.3% (-66.1 to -48.6) | -57.5% (-66.7 to -48.3) | -58.0% (-71.1 to -44.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -71.2% (-79.9 to -62.5) | -72.6% (-83.3 to -61.9) | -75.4% (-99.0 to -51.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -56.8% (-65.8 to -47.7) | -55.7% (-62.6 to -48.8) | -55.0% (-77.6 to -32.4) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -94.8% (-131.7 to -57.9) | -95.3% (-134.8 to -55.8) | -94.3% (-146.8 to -41.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -94.0% (-132.8 to -55.2) | -96.3% (-137.1 to -55.4) | -93.2% (-132.5 to -53.9) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.4 (+4.031 to +4.769) | +4.3 (+3.954 to +4.646) | +4.9 (+3.81 to +5.99) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -27.3% (-78.9 to +24.2) | -37.8% (-75.9 to +0.2) | +3.7% (-62.1 to +69.6) | shown, not judged |
| utilisation (used / allocatable) | +52.8% (+46.0 to +59.7) | +55.8% (+47.2 to +64.3) | +53.8% (+46.2 to +61.5) | shown, not judged |
| CPU used (cores), mean | +52.8% (+46.0 to +59.7) | +55.8% (+47.2 to +64.3) | +53.8% (+46.2 to +61.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00962 (+0.008465 to +0.01078) | +0.00969 (+0.008708 to +0.01067) | +0.0097 (+0.008557 to +0.01084) | shown, not judged |
| CPU used with Omni's own (cores), mean | +54.1% (+47.1 to +61.1) | +57.0% (+48.4 to +65.7) | +55.1% (+47.3 to +62.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -32.6% (-33.7 to -31.5) | -33.6% (-36.0 to -31.2) | -32.9% (-34.9 to -30.9) | shown, not judged |
| HPA replicas, mean | -18.6% (-24.3 to -12.8) | -15.4% (-19.2 to -11.6) | -16.9% (-21.5 to -12.4) | **GAIN in all three of our runs** |
| pods started | -20.0% (-32.3 to -7.7) | -23.3% (-34.9 to -11.8) | -16.7% (-29.2 to -4.1) | **GAIN in all three of our runs** |
| pod start wait, total (s) | -16.7% (-42.9 to +9.5) | -19.8% (-31.6 to -7.9) | -7.7% (-25.7 to +10.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, mean (s) | +3.4% (-24.9 to +31.6) | +5.6% (-0.5 to +11.7) | +8.6% (-1.0 to +18.1) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +49.2% (+42.8 to +55.6) | +49.4% (+42.5 to +56.2) | +50.0% (+42.6 to +57.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 GAIN in all three of our runs, 2 power given in all three of our runs, 1 EVEN, no difference beyond the noise (2 of 3 runs), 2 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
