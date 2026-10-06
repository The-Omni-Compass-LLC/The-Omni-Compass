# Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1): the A/B/C confirmation (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37384942870 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385643291 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37394436586 | `68d9bd172605` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.8% (-2.2 to +0.6) | -0.1% (-0.2 to +0.1) | -0.6% (-1.4 to +0.3) | no difference beyond the noise (all three runs) |
| node-hours | -0.9% (-2.2 to +0.5) | -0.1% (-0.4 to +0.1) | -0.6% (-1.4 to +0.3) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.5 to -0.1) | -0.3% (-0.5 to -0.2) | -0.3% (-0.4 to -0.2) | **confirmed better** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.8% (-1.6 to -0.1) | -0.4% (-0.5 to -0.2) | -0.7% (-1.3 to -0.0) | **confirmed better** |
| response time (ms), mean | -46.4% (-56.1 to -36.8) | -43.9% (-47.8 to -40.0) | -44.8% (-53.0 to -36.7) | **confirmed better** |
| response time (ms), 95th percentile | -56.4% (-66.6 to -46.3) | -58.2% (-62.2 to -54.2) | -60.3% (-71.7 to -48.9) | **confirmed better** |
| response time (ms), 99th percentile | -41.7% (-69.6 to -13.8) | -33.6% (-60.9 to -6.3) | -29.8% (-42.4 to -17.2) | **confirmed better** |
| time over the response line (% of samples) | -36.8% (-46.3 to -27.4) | -36.8% (-40.3 to -33.2) | -43.8% (-55.5 to -32.0) | **confirmed better** |
| failed requests (%) | -11.7% (-18.5 to -4.9) | -12.6% (-16.3 to -8.9) | -11.7% (-20.0 to -3.3) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -25.0% (-85.5 to +35.5) | -45.9% (-78.6 to -13.2) | -34.7% (-78.3 to +8.9) | shown, not judged |
| utilisation (used / allocatable) | -1.5% (-3.0 to -0.0) | -1.9% (-2.6 to -1.3) | -2.0% (-2.9 to -1.1) | shown, not judged |
| CPU used (cores), mean | -2.0% (-2.8 to -1.2) | -2.0% (-2.6 to -1.4) | -2.4% (-3.5 to -1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00938 (+0.008382 to +0.01038) | +0.0099 (+0.009276 to +0.01052) | +0.00905 (+0.007917 to +0.01018) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.6% (-2.4 to -0.8) | -1.6% (-2.3 to -1.0) | -2.0% (-3.1 to -0.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.7% (-1.4 to +2.8) | +1.7% (+1.2 to +2.2) | +2.4% (+1.0 to +3.8) | shown, not judged |
| HPA replicas, mean | -1.0% (-2.4 to +0.5) | +0.2% (-0.7 to +1.1) | -1.3% (-3.0 to +0.4) | no difference beyond the noise (all three runs) |
| pods started | -12.5% (-36.0 to +11.0) | -35.0% (-72.9 to +2.9) | -16.3% (-41.1 to +8.6) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -14.4% (-45.5 to +16.7) | -49.1% (-115.4 to +17.1) | -6.7% (-46.4 to +33.0) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -5.5% (-29.7 to +18.7) | -34.2% (-78.3 to +9.8) | +0.1% (-32.3 to +32.4) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.3% (-2.0 to -0.5) | -1.5% (-1.9 to -1.0) | -1.6% (-2.6 to -0.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 confirmed better, 6 no difference beyond the noise (all three runs), 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
