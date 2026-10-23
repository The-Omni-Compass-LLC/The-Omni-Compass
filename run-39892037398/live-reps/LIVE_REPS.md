# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.23 | 10.13 |
| node-hours | 5.023 | 5.032 | 4.29 | 4.243 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 524.7 | 524.8 | 525.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 524.7 | 469 | 466.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 380.4 | 505.6 | 429.7 | 635.1 |
| response time (ms), 95th percentile | 1409 | 2316 | 1869 | 3045 |
| response time (ms), 99th percentile | 2073 | 3396 | 2736 | 4372 |
| time over the response line (% of samples) | 14.57 | 16.71 | 17.27 | 19.62 |
| failed requests (%) | 0 | 0.006515 | 0 | 0.161 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 10.9 | 10.1 | 12.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 202.9 | 125.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 40.5 | 28 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 12.87 | 11.88 | 18.89 |
| utilisation (used / allocatable) | 0.03119 | 0.03264 | 0.03906 | 0.04031 |
| CPU used (cores), mean | 1.497 | 1.567 | 1.552 | 1.61 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03655 | 0.02795 |
| CPU used with Omni's own (cores), mean | 1.497 | 1.567 | 1.589 | 1.638 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853 | 822.3 | 723.2 | 700.1 |
| HPA replicas, mean | 3.955 | 4.151 | 5.21 | 4.93 |
| pods started | 0.1 | 0.2 | 2.5 | 2.9 |
| pod start wait, total (s) | 0.1 | 0.5 | 6.1 | 7 |
| pod start wait, mean (s) | 0.1 | 0.5 | 1.625 | 1.316 |
| host CPU busy, the real machine under kind (%) | 45.8 | 51.41 | 50.47 | 56.68 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 795.3 | 867.6 | 827 | 930.3 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.401 | 9.109 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.3292 | 0.075 | 3.033 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1 | 0.6 | 32.9 |
| queue: job turnaround, submitted to done, mean (s) | 106.4 | 172 | 132.6 | 235.8 |
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
| worker nodes in service, mean | 12 | 10.13 | -15.6% | -3.618 to -0.1248 | yes: GAIN |
| node-hours | 5.032 | 4.243 | -15.7% | -1.523 to -0.05499 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.7 | 525.2 | +0.1% | -1.713 to +2.63 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.7 | 466.4 | -11.1% | -114.1 to -2.651 | yes: GAIN |
| response time (ms), mean | 505.6 | 635.1 | +25.6% | +10.15 to +248.9 | yes: LOSS |
| response time (ms), 95th percentile | 2316 | 3045 | +31.4% | +134.6 to +1322 | yes: LOSS |
| response time (ms), 99th percentile | 3396 | 4372 | +28.8% | +59.93 to +1893 | yes: LOSS |
| time over the response line (% of samples) | 16.71 | 19.62 | +17.4% | +1.133 to +4.692 | yes: LOSS |
| failed requests (%) | 0.006515 | 0.161 | +2370.9% | -0.01344 to +0.3223 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 12.1 | +11.0% | +0.2583 to +2.142 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.8 | +126 (native is 0) | +102.6 to +149 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.87 | 18.89 | +46.7% | +0.1338 to +11.9 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03264 | 0.04031 | +23.5% | +0.001973 to +0.01336 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.61 | +2.8% | -0.03927 to +0.1267 | no |
| Omni's own CPU (cores), mean | 0 | 0.02795 | +0.0279 (native is 0) | +0.02175 to +0.03415 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.638 | +4.6% | -0.01471 to +0.158 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.3 | 700.1 | -14.9% | -205.8 to -38.53 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.151 | 4.93 | +18.8% | +0.2414 to +1.317 | yes: power given |
| pods started | 0.2 | 2.9 | +1350.0% | +0.5396 to +4.86 | yes: power given |
| pod start wait, total (s) | 0.5 | 7 | +1300.0% | +0.9567 to +12.04 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.316 | +163.3% | -0.3507 to +1.984 | no |
| host CPU busy, the real machine under kind (%) | 51.41 | 56.68 | +10.2% | +2.914 to +7.615 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.6 | 930.3 | +7.2% | +16.73 to +108.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.109 | -24.1% | -5.417 to -0.3652 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 3.033 | +821.5% | -3.235 to +8.643 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 32.9 | +3190.0% | -39.76 to +103.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 172 | 235.8 | +37.1% | +16.04 to +111.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -5.47e-15 to +1.562e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.023 | 5.032 | +0.2% | -0.005485 to +0.02415 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 524.7 | +0.4% | +0.707 to +3.748 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 524.7 | +0.4% | +0.707 to +3.748 | yes: power given |
| response time (ms), mean | 380.4 | 505.6 | +32.9% | +32.79 to +217.6 | yes: LOSS |
| response time (ms), 95th percentile | 1409 | 2316 | +64.4% | +176.3 to +1639 | yes: LOSS |
| response time (ms), 99th percentile | 2073 | 3396 | +63.8% | +295 to +2349 | yes: LOSS |
| time over the response line (% of samples) | 14.57 | 16.71 | +14.7% | -0.03267 to +4.313 | no |
| failed requests (%) | 0 | 0.006515 | +0.00651 (native is 0) | -0.008221 to +0.02125 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 10.9 | +39.7% | +0.7049 to +5.495 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 12.87 | +28.0% | +0.7603 to +4.876 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03119 | 0.03264 | +4.7% | +0.0006633 to +0.002243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.497 | 1.567 | +4.7% | +0.03184 to +0.1077 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.497 | 1.567 | +4.7% | +0.03184 to +0.1077 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853 | 822.3 | -3.6% | -44.98 to -16.37 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.955 | 4.151 | +4.9% | -0.1571 to +0.5478 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | -0.4396 to +1.24 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | -0.4396 to +1.24 | no |
| host CPU busy, the real machine under kind (%) | 45.8 | 51.41 | +12.3% | +3.881 to +7.357 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 867.6 | +9.1% | +17.95 to +126.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.3292 | +507.7% | +0.121 to +0.429 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1 | +100.0% | +0.123 to +0.877 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106.4 | 172 | +61.6% | +19.39 to +111.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.23 | -14.8% | -3.627 to +0.08425 | no |
| node-hours | 5.023 | 4.29 | -14.6% | -1.507 to +0.04046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 524.8 | +0.4% | +0.6075 to +3.969 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 469 | -10.2% | -111.8 to +4.7 | no |
| response time (ms), mean | 380.4 | 429.7 | +12.9% | -3.467 to +102 | no |
| response time (ms), 95th percentile | 1409 | 1869 | +32.7% | +152.5 to +768.6 | yes: LOSS |
| response time (ms), 99th percentile | 2073 | 2736 | +32.0% | +246.2 to +1080 | yes: LOSS |
| time over the response line (% of samples) | 14.57 | 17.27 | +18.6% | -0.8053 to +6.213 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 10.1 | +29.5% | +0.062 to +4.538 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 202.9 | +203 (native is 0) | +139.7 to +266.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 11.88 | +18.2% | -1.482 to +5.132 | no |
| utilisation (used / allocatable) | 0.03119 | 0.03906 | +25.3% | +0.001478 to +0.01427 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.497 | 1.552 | +3.7% | +0.004457 to +0.1058 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03655 | +0.0365 (native is 0) | +0.03267 to +0.04043 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.497 | 1.589 | +6.1% | +0.03865 to +0.1448 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853 | 723.2 | -15.2% | -222.5 to -36.97 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.955 | 5.21 | +31.7% | +0.8132 to +1.696 | yes: power given |
| pods started | 0.1 | 2.5 | +2400.0% | +0.6093 to +4.191 | yes: power given |
| pod start wait, total (s) | 0.1 | 6.1 | +6000.0% | +1.184 to +10.82 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.625 | +1525.0% | +0.5056 to +2.544 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.8 | 50.47 | +10.2% | +3.461 to +5.889 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 827 | +4.0% | +7.223 to +56.18 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.401 | -21.7% | -5.228 to +0.03061 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.075 | +38.5% | -0.004496 to +0.04616 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.4 | 132.6 | +24.6% | +6.495 to +45.84 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.23 | -14.8% | -3.627 to +0.08425 | no |
| node-hours | 5.032 | 4.29 | -14.8% | -1.521 to +0.03631 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.7 | 524.8 | +0.0% | -1.601 to +1.722 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.7 | 469 | -10.6% | -114.2 to +2.694 | no |
| response time (ms), mean | 505.6 | 429.7 | -15.0% | -141.5 to -10.37 | yes: GAIN |
| response time (ms), 95th percentile | 2316 | 1869 | -19.3% | -966.4 to +72.11 | no |
| response time (ms), 99th percentile | 3396 | 2736 | -19.4% | -1404 to +85.39 | no |
| time over the response line (% of samples) | 16.71 | 17.27 | +3.4% | -2.227 to +3.354 | no |
| failed requests (%) | 0.006515 | 0 | -100.0% | -0.02125 to +0.008221 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.1 | -7.3% | -1.612 to +0.01208 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 202.9 | +203 (native is 0) | +139.7 to +266.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.87 | 11.88 | -7.7% | -3.83 to +1.844 | no |
| utilisation (used / allocatable) | 0.03264 | 0.03906 | +19.7% | -0.0004379 to +0.01328 | no |
| CPU used (cores), mean | 1.567 | 1.552 | -0.9% | -0.05979 to +0.03059 | no |
| Omni's own CPU (cores), mean | 0 | 0.03655 | +0.0365 (native is 0) | +0.03267 to +0.04043 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.589 | +1.4% | -0.02374 to +0.06764 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.3 | 723.2 | -12.0% | -197.8 to -0.3072 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.151 | 5.21 | +25.5% | +0.5343 to +1.584 | yes: power given |
| pods started | 0.2 | 2.5 | +1150.0% | +0.5462 to +4.054 | yes: power given |
| pod start wait, total (s) | 0.5 | 6.1 | +1120.0% | +0.688 to +10.51 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.625 | +225.0% | -0.1892 to +2.439 | no |
| host CPU busy, the real machine under kind (%) | 51.41 | 50.47 | -1.8% | -2.155 to +0.2668 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.6 | 827 | -4.7% | -77.46 to -3.74 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.401 | -21.7% | -5.228 to +0.03061 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 0.075 | -77.2% | -0.4018 to -0.1065 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.6 | -40.0% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 172 | 132.6 | -22.9% | -74.74 to -4.028 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.13 | -15.6% | -3.618 to -0.1248 | yes: GAIN |
| node-hours | 5.023 | 4.243 | -15.5% | -1.51 to -0.04962 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 525.2 | +0.5% | +0.331 to +5.042 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 466.4 | -10.7% | -111.8 to -0.4912 | yes: GAIN |
| response time (ms), mean | 380.4 | 635.1 | +67.0% | +68.82 to +440.6 | yes: LOSS |
| response time (ms), 95th percentile | 1409 | 3045 | +116.1% | +502.3 to +2770 | yes: LOSS |
| response time (ms), 99th percentile | 2073 | 4372 | +110.9% | +762.1 to +3836 | yes: LOSS |
| time over the response line (% of samples) | 14.57 | 19.62 | +34.7% | +1.955 to +8.151 | yes: LOSS |
| failed requests (%) | 0 | 0.161 | +0.161 (native is 0) | -0.01094 to +0.3329 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 12.1 | +55.1% | +1.938 to +6.662 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.8 | +126 (native is 0) | +102.6 to +149 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 18.89 | +87.9% | +2.434 to +15.24 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03119 | 0.04031 | +29.2% | +0.003961 to +0.01428 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.497 | 1.61 | +7.6% | +0.01577 to +0.2111 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02795 | +0.0279 (native is 0) | +0.02175 to +0.03415 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.497 | 1.638 | +9.4% | +0.03878 to +0.244 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853 | 700.1 | -17.9% | -227.6 to -78.06 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.955 | 4.93 | +24.6% | +0.5496 to +1.399 | yes: power given |
| pods started | 0.1 | 2.9 | +2800.0% | +0.594 to +5.006 | yes: power given |
| pod start wait, total (s) | 0.1 | 7 | +6900.0% | +1.355 to +12.45 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.316 | +1216.4% | +0.2325 to +2.2 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.8 | 56.68 | +23.8% | +7.416 to +14.35 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 930.3 | +17.0% | +43.37 to +226.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.109 | -24.1% | -5.417 to -0.3652 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 3.033 | +5500.0% | -3.07 to +9.028 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 32.9 | +6480.0% | -39.13 to +103.9 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.4 | 235.8 | +121.6% | +44.11 to +214.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*