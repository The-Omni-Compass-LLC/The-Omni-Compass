# Steady load: the same fixed-rate work sent to both arms: the A/B/C confirmation (Omni v3): the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013195851 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013200499 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013204648 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -2.0% (-2.1 to -1.8) | -2.0% (-2.6 to -1.4) | -1.7% (-2.2 to -1.2) | **confirmed better** |
| node-hours | -1.7% (-2.1 to -1.3) | -1.9% (-2.5 to -1.3) | -2.0% (-3.0 to -1.0) | **confirmed better** |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.3 to +0.5) | -0.2% (-0.6 to +0.1) | -0.6% (-1.3 to +0.1) | no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.3% (-1.7 to -1.0) | -1.6% (-2.0 to -1.3) | -1.8% (-2.7 to -0.9) | **confirmed better** |
| response time (ms), mean | -47.2% (-65.7 to -28.8) | -47.6% (-68.3 to -26.9) | -48.2% (-65.7 to -30.8) | **confirmed better** |
| response time (ms), 95th percentile | -64.6% (-87.6 to -41.7) | -65.6% (-90.0 to -41.3) | -64.4% (-83.9 to -45.0) | **confirmed better** |
| response time (ms), 99th percentile | -69.7% (-93.0 to -46.3) | -69.0% (-94.2 to -43.8) | -72.9% (-98.3 to -47.4) | **confirmed better** |
| time over the response line (% of samples) | -97.9% (-166.6 to -29.3) | -97.1% (-159.7 to -34.5) | -98.7% (-161.1 to -36.3) | **confirmed better** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.5% (-66.8 to +67.7) | -21.8% (-57.4 to +13.9) | -27.0% (-71.9 to +18.0) | shown, not judged |
| utilisation (used / allocatable) | -2.6% (-6.1 to +1.0) | -3.9% (-8.2 to +0.4) | -4.0% (-6.7 to -1.3) | shown, not judged |
| CPU used (cores), mean | -4.5% (-8.3 to -0.6) | -5.7% (-9.9 to -1.5) | -5.6% (-8.3 to -2.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00977 (+0.008234 to +0.01131) | +0.00939 (+0.007756 to +0.01102) | +0.00979 (+0.008132 to +0.01145) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.4% (-7.1 to +0.3) | -4.6% (-8.7 to -0.5) | -4.5% (-7.0 to -1.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.8% (-3.0 to +4.5) | +1.8% (-1.9 to +5.5) | +3.1% (+0.9 to +5.3) | shown, not judged |
| HPA replicas, mean | -1.1% (-3.1 to +0.9) | -1.7% (-5.3 to +2.0) | -2.6% (-5.6 to +0.3) | no difference beyond the noise (all three runs) |
| pods started | -4.5% (-21.3 to +12.2) | -25.5% (-43.0 to -7.9) | -10.6% (-30.0 to +8.7) | no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -16.8% (-46.1 to +12.5) | -33.2% (-54.5 to -11.9) | +0.0% (-36.0 to +36.0) | no difference beyond the noise in 2 of 3 runs |
| pod start wait, mean (s) | -19.1% (-47.9 to +9.7) | -21.0% (-42.8 to +0.7) | +5.2% (-28.8 to +39.2) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -2.6% (-5.8 to +0.6) | -3.0% (-6.4 to +0.5) | -3.7% (-5.9 to -1.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 confirmed better, 3 no difference beyond the noise (all three runs), 2 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
