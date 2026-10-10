# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C confirmation (Omni v3): the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013248544 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013252615 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013257029 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.1% (-0.4 to +0.2) | -0.0% (-0.1 to +0.0) | -1.2% (-3.8 to +1.3) | no difference beyond the noise (all three runs) |
| node-hours | -0.0% (-0.4 to +0.3) | -0.4% (-1.0 to +0.1) | -1.5% (-4.0 to +1.1) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.5 to +0.1) | -0.4% (-1.0 to +0.1) | -0.4% (-0.8 to +0.1) | no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.2% (-0.6 to +0.1) | -0.4% (-1.0 to +0.1) | -1.2% (-3.0 to +0.5) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -42.1% (-64.3 to -19.8) | -51.1% (-76.0 to -26.3) | -33.6% (-56.5 to -10.7) | **confirmed better** |
| response time (ms), 95th percentile | -62.7% (-69.3 to -56.1) | -57.7% (-72.3 to -43.1) | -61.7% (-76.8 to -46.5) | **confirmed better** |
| response time (ms), 99th percentile | -39.6% (-98.2 to +19.0) | -42.5% (-80.7 to -4.3) | -16.5% (-82.5 to +49.5) | no difference beyond the noise in 2 of 3 runs |
| time over the response line (% of samples) | -34.4% (-46.9 to -21.8) | -42.7% (-58.8 to -26.5) | -26.6% (-44.3 to -9.0) | **confirmed better** |
| failed requests (%) | -18.1% (-34.7 to -1.5) | -13.8% (-27.5 to -0.1) | -15.1% (-29.1 to -1.1) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +24.1% (-83.7 to +132.0) | -17.6% (-42.4 to +7.2) | -17.6% (-67.6 to +32.3) | shown, not judged |
| utilisation (used / allocatable) | -2.6% (-4.9 to -0.3) | -0.2% (-2.5 to +2.2) | -1.0% (-4.5 to +2.5) | shown, not judged |
| CPU used (cores), mean | -2.6% (-4.9 to -0.4) | -0.2% (-2.5 to +2.1) | -1.9% (-4.5 to +0.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00873 (+0.007424 to +0.01004) | +0.0073 (+0.006109 to +0.008491) | +0.00913 (+0.008191 to +0.01007) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.1% (-4.3 to +0.1) | +0.3% (-1.9 to +2.6) | -1.3% (-3.9 to +1.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.9% (+0.3 to +3.6) | -0.6% (-2.9 to +1.7) | +0.1% (-3.4 to +3.6) | shown, not judged |
| HPA replicas, mean | -0.2% (-3.5 to +3.1) | -0.2% (-3.8 to +3.3) | +0.6% (-3.1 to +4.2) | no difference beyond the noise (all three runs) |
| pods started | -12.5% (-40.8 to +15.8) | -5.2% (-26.2 to +15.8) | -6.0% (-34.7 to +22.7) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +26.5% (-81.1 to +134.1) | -14.2% (-39.4 to +11.0) | -43.0% (-128.2 to +42.1) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +37.9% (-80.0 to +155.9) | -15.2% (-33.8 to +3.4) | -41.4% (-131.2 to +48.5) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.8% (-3.7 to +0.0) | +0.2% (-1.6 to +2.0) | -1.4% (-3.1 to +0.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 confirmed better, 8 no difference beyond the noise (all three runs), 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
