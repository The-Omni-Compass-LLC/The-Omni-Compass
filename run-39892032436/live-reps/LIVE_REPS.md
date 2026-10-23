# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.682 | 5.768 |
| node-hours | 2.513 | 2.519 | 2.383 | 2.415 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.3 | 272.3 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 272.3 | 262.3 | 264.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 333.3 | 346.5 | 349.2 | 347.9 |
| response time (ms), 95th percentile | 1170 | 1285 | 1288 | 1344 |
| response time (ms), 99th percentile | 1778 | 2080 | 1911 | 2166 |
| time over the response line (% of samples) | 15.53 | 14.66 | 16.31 | 14.75 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.2 | 10.5 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 44.6 | 40.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 10.21 | 11.32 | 13.26 |
| utilisation (used / allocatable) | 0.05971 | 0.05959 | 0.06327 | 0.06312 |
| CPU used (cores), mean | 1.433 | 1.43 | 1.438 | 1.452 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.038 | 0.04213 |
| CPU used with Omni's own (cores), mean | 1.433 | 1.43 | 1.476 | 1.494 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 461.2 | 439.8 | 440.3 |
| HPA replicas, mean | 2.077 | 2.177 | 2.852 | 2.764 |
| pods started | 0.1 | 0 | 1.8 | 1.5 |
| pod start wait, total (s) | 0.3 | 0 | 5.2 | 3.5 |
| pod start wait, mean (s) | 0.3 | 0 | 1.51 | 1.817 |
| host CPU busy, the real machine under kind (%) | 40.98 | 41.73 | 42.42 | 43.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772.7 | 777.5 | 777 | 784.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.386 | 5.547 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.2125 | 0.04167 | 0.1417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | 0.2 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 79.5 | 88.81 | 84.11 | 95.4 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.768 | -3.9% | -0.6864 to +0.2231 | no |
| node-hours | 2.519 | 2.415 | -4.1% | -0.2915 to +0.08516 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | -0.1% | -1.377 to +0.8339 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 264.8 | -2.8% | -21.68 to +6.578 | no |
| response time (ms), mean | 346.5 | 347.9 | +0.4% | -12.64 to +15.4 | no |
| response time (ms), 95th percentile | 1285 | 1344 | +4.6% | -54.89 to +172.7 | no |
| response time (ms), 99th percentile | 2080 | 2166 | +4.1% | -191.7 to +363.3 | no |
| time over the response line (% of samples) | 14.66 | 14.75 | +0.7% | -0.7067 to +0.8978 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.4 | +2.2% | -1.731 to +2.131 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | +40.2 (native is 0) | +19.33 to +61.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.21 | 13.26 | +29.8% | +1.502 to +4.588 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05959 | 0.06312 | +5.9% | -0.001036 to +0.008101 | no |
| CPU used (cores), mean | 1.43 | 1.452 | +1.5% | +0.004189 to +0.03955 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04213 | +0.0421 (native is 0) | +0.03573 to +0.04853 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.494 | +4.5% | +0.0446 to +0.0834 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.2 | 440.3 | -4.5% | -46.13 to +4.388 | no |
| HPA replicas, mean | 2.177 | 2.764 | +26.9% | +0.3927 to +0.7795 | yes: power given |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.5921 to +2.408 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.5 (native is 0) | +0.971 to +6.029 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.817 | +1.82 (native is 0) | +0.9237 to +2.71 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.73 | 43.66 | +4.6% | +1.445 to +2.411 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 777.5 | 784.9 | +1.0% | +1.208 to +13.59 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.547 | -7.5% | -1.333 to +0.4277 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.1417 | -33.3% | -0.1337 to -0.007922 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | -11.1% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.81 | 95.4 | +7.4% | +0.4844 to +12.69 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.561e-15 to +8.502e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.519 | +0.2% | -0.004007 to +0.01434 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.3 | +0.2% | -0.4362 to +1.437 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 272.3 | +0.2% | -0.4362 to +1.437 | no |
| response time (ms), mean | 333.3 | 346.5 | +4.0% | -8.638 to +35.08 | no |
| response time (ms), 95th percentile | 1170 | 1285 | +9.9% | -43.11 to +274.2 | no |
| response time (ms), 99th percentile | 1778 | 2080 | +17.0% | +27.55 to +577.2 | yes: LOSS |
| time over the response line (% of samples) | 15.53 | 14.66 | -5.6% | -2.25 to +0.5037 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.2 | -5.2% | -2.017 to +1.017 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 10.21 | -4.1% | -2.217 to +1.34 | no |
| utilisation (used / allocatable) | 0.05971 | 0.05959 | -0.2% | -0.001124 to +0.000888 | no |
| CPU used (cores), mean | 1.433 | 1.43 | -0.2% | -0.02699 to +0.02131 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.433 | 1.43 | -0.2% | -0.02699 to +0.02131 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 461.2 | +0.0% | -8.145 to +8.169 | no |
| HPA replicas, mean | 2.077 | 2.177 | +4.9% | -0.07104 to +0.2726 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 40.98 | 41.73 | +1.8% | +0.3169 to +1.19 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 777.5 | +0.6% | -2.223 to +11.82 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.2125 | +240.0% | +0.07027 to +0.2297 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | +80.0% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.5 | 88.81 | +11.7% | +0.3609 to +18.25 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.682 | -5.3% | -0.7821 to +0.1452 | no |
| node-hours | 2.513 | 2.383 | -5.2% | -0.3257 to +0.06424 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.3 | +0.2% | -0.007818 to +0.9085 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 262.3 | -3.5% | -24.31 to +5.147 | no |
| response time (ms), mean | 333.3 | 349.2 | +4.8% | -3.745 to +35.49 | no |
| response time (ms), 95th percentile | 1170 | 1288 | +10.1% | +18.59 to +218.1 | yes: LOSS |
| response time (ms), 99th percentile | 1778 | 1911 | +7.5% | -0.3966 to +266.3 | no |
| time over the response line (% of samples) | 15.53 | 16.31 | +5.0% | -0.1493 to +1.71 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.5 | +8.2% | -1.041 to +2.641 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 | +44.6 (native is 0) | +28.81 to +60.39 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 11.32 | +6.2% | -1.298 to +2.628 | no |
| utilisation (used / allocatable) | 0.05971 | 0.06327 | +6.0% | -0.0009465 to +0.008073 | no |
| CPU used (cores), mean | 1.433 | 1.438 | +0.3% | -0.02071 to +0.02977 | no |
| Omni's own CPU (cores), mean | 0 | 0.038 | +0.038 (native is 0) | +0.03193 to +0.04407 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.476 | +3.0% | +0.01614 to +0.06892 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 439.8 | -4.6% | -48.31 to +5.569 | no |
| HPA replicas, mean | 2.077 | 2.852 | +37.3% | +0.4631 to +1.087 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.3076 to +3.092 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.2 | +1633.3% | +0.1378 to +9.662 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.51 | +403.3% | +0.02238 to +2.398 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.98 | 42.42 | +3.5% | +1.008 to +1.884 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 777 | +0.6% | -1.609 to +10.21 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.386 | -10.2% | -1.494 to +0.2668 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | -33.3% | -0.06356 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | -60.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.5 | 84.11 | +5.8% | -0.3767 to +9.593 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.682 | -5.3% | -0.7821 to +0.1452 | no |
| node-hours | 2.519 | 2.383 | -5.4% | -0.3281 to +0.05622 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.3 | -0.0% | -0.9579 to +0.858 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 262.3 | -3.7% | -24.68 to +4.519 | no |
| response time (ms), mean | 346.5 | 349.2 | +0.8% | -5.599 to +10.9 | no |
| response time (ms), 95th percentile | 1285 | 1288 | +0.2% | -60.87 to +66.46 | no |
| response time (ms), 99th percentile | 2080 | 1911 | -8.1% | -337.4 to -1.552 | yes: GAIN |
| time over the response line (% of samples) | 14.66 | 16.31 | +11.3% | +0.5285 to +2.778 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.5 | +14.1% | -0.421 to +3.021 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.6 | +44.6 (native is 0) | +28.81 to +60.39 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.21 | 11.32 | +10.8% | -1.408 to +3.615 | no |
| utilisation (used / allocatable) | 0.05959 | 0.06327 | +6.2% | -0.000351 to +0.007714 | no |
| CPU used (cores), mean | 1.43 | 1.438 | +0.5% | -0.02095 to +0.03569 | no |
| Omni's own CPU (cores), mean | 0 | 0.038 | +0.038 (native is 0) | +0.03193 to +0.04407 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.476 | +3.2% | +0.01573 to +0.07501 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.2 | 439.8 | -4.6% | -43.37 to +0.6025 | no |
| HPA replicas, mean | 2.177 | 2.852 | +31.0% | +0.3122 to +1.037 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.2996 to +3.3 | yes: power given |
| pod start wait, total (s) | 0 | 5.2 | +5.2 (native is 0) | +0.2811 to +10.12 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.51 | +1.51 (native is 0) | +0.4213 to +2.599 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.73 | 42.42 | +1.7% | +0.3192 to +1.066 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 777.5 | 777 | -0.1% | -2.768 to +1.768 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.386 | -10.2% | -1.494 to +0.2668 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.04167 | -80.4% | -0.2557 to -0.08601 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.2 | -77.8% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 88.81 | 84.11 | -5.3% | -9.725 to +0.3331 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.768 | -3.9% | -0.6864 to +0.2231 | no |
| node-hours | 2.513 | 2.415 | -3.9% | -0.2898 to +0.09372 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.1 | +0.1% | -0.6993 to +1.157 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 264.8 | -2.6% | -21.36 to +7.267 | no |
| response time (ms), mean | 333.3 | 347.9 | +4.4% | -15.68 to +44.87 | no |
| response time (ms), 95th percentile | 1170 | 1344 | +14.9% | -1.82 to +350.7 | no |
| response time (ms), 99th percentile | 1778 | 2166 | +21.8% | +16.31 to +760 | yes: LOSS |
| time over the response line (% of samples) | 15.53 | 14.75 | -5.0% | -1.87 to +0.3154 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.4 | -3.1% | -1.919 to +1.319 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | +40.2 (native is 0) | +19.33 to +61.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.65 | 13.26 | +24.5% | +1.278 to +3.935 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05971 | 0.06312 | +5.7% | -0.001621 to +0.008449 | no |
| CPU used (cores), mean | 1.433 | 1.452 | +1.3% | -0.003829 to +0.04189 | no |
| Omni's own CPU (cores), mean | 0 | 0.04213 | +0.0421 (native is 0) | +0.03573 to +0.04853 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.494 | +4.3% | +0.03725 to +0.08507 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 440.3 | -4.5% | -51.28 to +9.555 | no |
| HPA replicas, mean | 2.077 | 2.764 | +33.1% | +0.3976 to +0.9762 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.4344 to +2.366 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.5 | +1066.7% | +0.4235 to +5.977 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.817 | +505.6% | +0.2771 to +2.756 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.98 | 43.66 | +6.5% | +2.144 to +3.219 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 784.9 | +1.6% | +1.581 to +22.82 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.547 | -7.5% | -1.333 to +0.4277 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.1417 | +126.7% | +0.02394 to +0.1344 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.5 | 95.4 | +20.0% | +3.228 to +28.55 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*