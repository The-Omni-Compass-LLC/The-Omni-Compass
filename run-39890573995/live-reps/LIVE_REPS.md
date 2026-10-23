# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.419 | 5.189 |
| node-hours | 2.516 | 2.52 | 2.271 | 2.176 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.1 | 271.9 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 272.1 | 253.6 | 246.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 280.2 | 215.6 | 273.9 | 198.1 |
| response time (ms), 95th percentile | 881.8 | 513.2 | 1052 | 637.5 |
| response time (ms), 99th percentile | 1257 | 862.2 | 1517 | 1110 |
| time over the response line (% of samples) | 16.13 | 7.287 | 16.72 | 9.084 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 7.8 | 8.9 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 136.5 | 113 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.61 | 14.04 | 10.43 | 14.28 |
| utilisation (used / allocatable) | 0.05717 | 0.05775 | 0.06487 | 0.06615 |
| CPU used (cores), mean | 1.372 | 1.386 | 1.404 | 1.369 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04779 | 0.05046 |
| CPU used with Omni's own (cores), mean | 1.372 | 1.386 | 1.451 | 1.419 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 478.8 | 434.1 | 433.3 |
| HPA replicas, mean | 1.995 | 2.057 | 2.519 | 2.619 |
| pods started | 0 | 0 | 0.7 | 0.8 |
| pod start wait, total (s) | 0 | 0 | 1 | 1.6 |
| pod start wait, mean (s) | 0 | 0 | 0.8 | 0.8 |
| host CPU busy, the real machine under kind (%) | 38.95 | 40.18 | 41.62 | 42.39 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 755.5 | 770.3 | 764 | 776.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.88 | 4.485 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7083 | 0.05 | 0.6917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | 0.3 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 62.17 | 83.95 | 70.79 | 88.38 |
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
| worker nodes in service, mean | 6 | 5.189 | -13.5% | -1.518 to -0.1037 | yes: GAIN |
| node-hours | 2.52 | 2.176 | -13.6% | -0.6414 to -0.04574 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | -0.2% | -1.479 to +0.6371 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 246.2 | -9.5% | -48.62 to -3.276 | yes: GAIN |
| response time (ms), mean | 215.6 | 198.1 | -8.1% | -31 to -3.96 | yes: GAIN |
| response time (ms), 95th percentile | 513.2 | 637.5 | +24.2% | +8.418 to +240.3 | yes: LOSS |
| response time (ms), 99th percentile | 862.2 | 1110 | +28.7% | +45.36 to +450 | yes: LOSS |
| time over the response line (% of samples) | 7.287 | 9.084 | +24.6% | +0.1514 to +3.441 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.1 | +3.8% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113 (native is 0) | +80.41 to +145.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.04 | 14.28 | +1.7% | -1.298 to +1.785 | no |
| utilisation (used / allocatable) | 0.05775 | 0.06615 | +14.5% | +0.001297 to +0.01551 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.386 | 1.369 | -1.2% | -0.05999 to +0.02562 | no |
| Omni's own CPU (cores), mean | 0 | 0.05046 | +0.0505 (native is 0) | +0.04367 to +0.05725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.386 | 1.419 | +2.4% | -0.0129 to +0.07945 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.8 | 433.3 | -9.5% | -84.08 to -6.962 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.057 | 2.619 | +27.3% | +0.1133 to +1.012 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | -0.01208 to +1.612 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | -0.02417 to +3.224 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.06123 to +1.539 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.18 | 42.39 | +5.5% | +1.843 to +2.59 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.3 | 776.7 | +0.8% | +0.6065 to +12.19 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.485 | -25.2% | -2.804 to -0.2249 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 0.6917 | -2.4% | -0.1284 to +0.09503 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.1 | -21.4% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.95 | 88.38 | +5.3% | -1.896 to +10.77 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.995e-16 to +8.895e-17 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.52 | +0.1% | -0.001447 to +0.008781 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.1 | +0.2% | -0.166 to +1.124 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 272.1 | +0.2% | -0.166 to +1.124 | no |
| response time (ms), mean | 280.2 | 215.6 | -23.1% | -98.58 to -30.65 | yes: GAIN |
| response time (ms), 95th percentile | 881.8 | 513.2 | -41.8% | -548.5 to -188.7 | yes: GAIN |
| response time (ms), 99th percentile | 1257 | 862.2 | -31.4% | -586.6 to -203.8 | yes: GAIN |
| time over the response line (% of samples) | 16.13 | 7.287 | -54.8% | -14.19 to -3.495 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 7.8 | -4.9% | -1.366 to +0.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.61 | 14.04 | +63.1% | +3.009 to +7.851 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05717 | 0.05775 | +1.0% | -0.0002093 to +0.001375 | no |
| CPU used (cores), mean | 1.372 | 1.386 | +1.0% | -0.005023 to +0.033 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.372 | 1.386 | +1.0% | -0.005023 to +0.033 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 478.8 | -0.7% | -10.8 to +3.931 | no |
| HPA replicas, mean | 1.995 | 2.057 | +3.1% | -0.09428 to +0.2169 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.95 | 40.18 | +3.1% | +0.8043 to +1.644 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.5 | 770.3 | +2.0% | +5.181 to +24.42 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7083 | +1445.5% | +0.5627 to +0.7623 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | +366.7% | +0.5722 to +1.628 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.17 | 83.95 | +35.0% | +8.74 to +34.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.419 | -9.7% | -1.165 to +0.003183 | no |
| node-hours | 2.516 | 2.271 | -9.8% | -0.4876 to -0.00322 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.9 | +0.1% | -0.792 to +1.364 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 253.6 | -6.6% | -36 to -0.03443 | yes: GAIN |
| response time (ms), mean | 280.2 | 273.9 | -2.3% | -22.72 to +10.04 | no |
| response time (ms), 95th percentile | 881.8 | 1052 | +19.3% | +39.63 to +300.4 | yes: LOSS |
| response time (ms), 99th percentile | 1257 | 1517 | +20.7% | +80.25 to +439.3 | yes: LOSS |
| time over the response line (% of samples) | 16.13 | 16.72 | +3.6% | +0.01912 to +1.155 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.9 | +8.5% | -0.4209 to +1.821 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.5 | +136 (native is 0) | +79.58 to +193.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.61 | 10.43 | +21.1% | -0.2242 to +3.861 | no |
| utilisation (used / allocatable) | 0.05717 | 0.06487 | +13.5% | +0.0009653 to +0.01444 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.404 | +2.3% | -0.002176 to +0.06519 | no |
| Omni's own CPU (cores), mean | 0 | 0.04779 | +0.0478 (native is 0) | +0.04281 to +0.05277 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.451 | +5.8% | +0.04598 to +0.1126 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 434.1 | -10.0% | -91.76 to -4.707 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.519 | +26.2% | +0.2242 to +0.8234 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.2172 to +1.183 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | +0.1079 to +1.892 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.2358 to +1.364 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.95 | 41.62 | +6.8% | +2.16 to +3.176 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.5 | 764 | +1.1% | +0.8831 to +16.12 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.88 | -18.7% | -2.244 to +0.003916 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05 | +9.1% | -0.03152 to +0.03985 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.17 | 70.79 | +13.9% | +2.247 to +14.98 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.419 | -9.7% | -1.165 to +0.003183 | no |
| node-hours | 2.52 | 2.271 | -9.9% | -0.4925 to -0.005576 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.9 | -0.1% | -1.236 to +0.8493 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.6 | -6.8% | -36.46 to -0.5366 | yes: GAIN |
| response time (ms), mean | 215.6 | 273.9 | +27.0% | +15.52 to +101 | yes: LOSS |
| response time (ms), 95th percentile | 513.2 | 1052 | +105.0% | +263 to +814.3 | yes: LOSS |
| response time (ms), 99th percentile | 862.2 | 1517 | +76.0% | +326.3 to +983.7 | yes: LOSS |
| time over the response line (% of samples) | 7.287 | 16.72 | +129.4% | +3.95 to +14.91 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.9 | +14.1% | -0.9077 to +3.108 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.5 | +136 (native is 0) | +79.58 to +193.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.04 | 10.43 | -25.7% | -5.535 to -1.688 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05775 | 0.06487 | +12.3% | -6.199e-06 to +0.01424 | no |
| CPU used (cores), mean | 1.386 | 1.404 | +1.3% | -0.01706 to +0.0521 | no |
| Omni's own CPU (cores), mean | 0 | 0.04779 | +0.0478 (native is 0) | +0.04281 to +0.05277 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.386 | 1.451 | +4.7% | +0.03227 to +0.09835 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.8 | 434.1 | -9.4% | -91.52 to +1.927 | no |
| HPA replicas, mean | 2.057 | 2.519 | +22.5% | +0.1355 to +0.7895 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.2172 to +1.183 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | +0.1079 to +1.892 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.2358 to +1.364 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.18 | 41.62 | +3.6% | +1.007 to +1.881 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.3 | 764 | -0.8% | -11.07 to -1.531 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.88 | -18.7% | -2.244 to +0.003916 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 0.05 | -92.9% | -0.7436 to -0.5731 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.3 | -78.6% | -1.506 to -0.694 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 83.95 | 70.79 | -15.7% | -22.57 to -3.751 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.189 | -13.5% | -1.518 to -0.1037 | yes: GAIN |
| node-hours | 2.516 | 2.176 | -13.5% | -0.6353 to -0.04447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.7 | +0.0% | -0.7449 to +0.8614 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 246.2 | -9.4% | -48.04 to -2.897 | yes: GAIN |
| response time (ms), mean | 280.2 | 198.1 | -29.3% | -110.1 to -54.06 | yes: GAIN |
| response time (ms), 95th percentile | 881.8 | 637.5 | -27.7% | -359.6 to -128.9 | yes: GAIN |
| response time (ms), 99th percentile | 1257 | 1110 | -11.7% | -304 to +8.861 | no |
| time over the response line (% of samples) | 16.13 | 9.084 | -43.7% | -11.27 to -2.823 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.1 | -1.2% | -1.137 to +0.9366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113 (native is 0) | +80.41 to +145.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.61 | 14.28 | +65.9% | +3.692 to +7.654 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05717 | 0.06615 | +15.7% | +0.002042 to +0.01593 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.369 | -0.2% | -0.05131 to +0.04492 | no |
| Omni's own CPU (cores), mean | 0 | 0.05046 | +0.0505 (native is 0) | +0.04367 to +0.05725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.419 | +3.4% | -0.004869 to +0.0994 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 433.3 | -10.2% | -86 to -11.92 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.619 | +31.3% | +0.2062 to +1.041 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | -0.01208 to +1.612 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | -0.02417 to +3.224 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.06123 to +1.539 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.95 | 42.39 | +8.8% | +2.875 to +4.006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.5 | 776.7 | +2.8% | +8.535 to +33.87 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.485 | -25.2% | -2.804 to -0.2249 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.6917 | +1409.1% | +0.5624 to +0.7293 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | +0.3476 to +1.252 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.17 | 88.38 | +42.2% | +10.91 to +41.51 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*