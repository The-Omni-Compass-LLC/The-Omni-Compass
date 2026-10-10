# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C confirmation (Omni v3): the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013462081 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 38013467123 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 38013471943 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -1.9% (-9.9 to +6.2) | +0.0% (-0.0 to +0.0) | -4.1% (-20.1 to +11.9) | no difference beyond the noise (all three runs) |
| node-hours | -1.9% (-9.8 to +6.1) | -0.0% (-0.4 to +0.3) | -4.0% (-20.3 to +12.3) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.4% (-0.7 to -0.0) | -0.3% (-1.2 to +0.6) | -0.1% (-1.1 to +1.0) | no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.6% (-7.0 to +3.9) | -0.3% (-1.2 to +0.6) | -2.8% (-13.5 to +7.9) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -43.9% (-113.1 to +25.3) | -45.2% (-75.0 to -15.5) | -33.5% (-84.5 to +17.5) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 95th percentile | -58.6% (-153.2 to +35.9) | -49.8% (-64.4 to -35.1) | -41.9% (-102.6 to +18.7) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 99th percentile | -18.0% (-40.7 to +4.6) | -37.5% (-73.7 to -1.2) | +6.1% (-64.9 to +77.1) | no difference beyond the noise in 2 of 3 runs |
| time over the response line (% of samples) | -42.8% (-126.4 to +40.9) | -45.3% (-47.9 to -42.8) | -33.2% (-106.1 to +39.6) | no difference beyond the noise in 2 of 3 runs |
| failed requests (%) | -12.6% (-53.6 to +28.4) | -8.0% (-19.9 to +4.0) | -7.1% (-26.8 to +12.6) | no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +79.9% (-258.0 to +417.9) | +46.0% (-55.3 to +147.4) | +4.9% (-221.5 to +231.4) | shown, not judged |
| utilisation (used / allocatable) | -2.0% (-5.5 to +1.5) | -1.5% (-5.3 to +2.4) | +1.4% (-13.0 to +15.8) | shown, not judged |
| CPU used (cores), mean | -3.1% (-6.1 to -0.0) | -1.5% (-5.3 to +2.4) | -1.4% (-9.6 to +6.7) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0063 (+nan to +nan) | +0.008 (+nan to +nan) | +0.0083 (-0.006947 to +0.02355) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.7% (+nan to +nan) | -1.1% (+nan to +nan) | +0.7% (-12.7 to +14.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.4% (-1.3 to +6.1) | +1.5% (-2.5 to +5.6) | -2.0% (-20.0 to +16.1) | shown, not judged |
| HPA replicas, mean | -4.4% (-23.9 to +15.0) | +0.2% (-0.7 to +1.0) | -4.7% (-24.0 to +14.6) | no difference beyond the noise (all three runs) |
| pods started | +9.5% (-92.9 to +112.0) | -35.3% (-151.3 to +80.7) | +35.0% (-133.0 to +203.0) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +4.5% (-115.0 to +124.1) | -37.3% (-126.0 to +51.4) | +50.0% (-187.4 to +287.4) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +3.9% (-146.4 to +154.2) | -35.9% (-139.4 to +67.5) | -0.5% (-93.0 to +92.1) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -2.1% (-4.4 to +0.2) | -0.8% (-4.0 to +2.4) | -0.6% (-8.6 to +7.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.067 | 1.053 | 1.073 | no leak (every repetition under 1.25) |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 97.5% | 97.5% | 97.5% | valid (every repetition at 95% of the expected or more) |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 1 | 3 | 5 | shown, not judged: API 500 for apis/autoscaling/v2/horizontalpodautoscalers; the governor held and resumed |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 1.15 | 1.27 | 1.30 | no growth beyond the limit (every repetition under 1.5) |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **confirmed: every setting handed back at the end of every repetition** |

Readings: 1 confirmed: every setting handed back at the end of every repetition, 8 no difference beyond the noise (all three runs), 5 no difference beyond the noise in 2 of 3 runs, 1 no growth beyond the limit (every repetition under 1.5), 1 no leak (every repetition under 1.25), 2 same, 8 shown, not judged, 1 shown, not judged: API 500 for apis/autoscaling/v2/horizontalpodautoscalers; the governor held and resumed, 1 valid (every repetition at 95% of the expected or more).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
