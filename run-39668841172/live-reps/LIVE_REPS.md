# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.08 | 4.799 |
| node-hours | 2.514 | 2.509 | 2.13 | 2.012 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.8 | 272.4 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.8 | 243.4 | 234.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 316.8 | 275.6 | 288.9 | 243.5 |
| response time (ms), 95th percentile | 1069 | 1004 | 1128 | 1016 |
| response time (ms), 99th percentile | 1497 | 1567 | 1538 | 1552 |
| time over the response line (% of samples) | 13.33 | 9.123 | 13.35 | 8.769 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 6.5 | 8.5 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.1 | 43.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.765 | 16.22 | 9.32 | 16 |
| utilisation (used / allocatable) | 0.05963 | 0.06006 | 0.0708 | 0.07415 |
| CPU used (cores), mean | 1.431 | 1.442 | 1.421 | 1.419 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01667 | 0.01996 |
| CPU used with Omni's own (cores), mean | 1.431 | 1.442 | 1.438 | 1.439 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 462 | 411.9 | 397.8 |
| HPA replicas, mean | 1.944 | 2.084 | 2.21 | 2.143 |
| pods started | 0.2 | 0.3 | 0.3 | 0.5 |
| pod start wait, total (s) | 0.3 | 0.7 | 0.3 | 0.9 |
| pod start wait, mean (s) | 0.15 | 0.5 | 0.3 | 0.55 |
| host CPU busy, the real machine under kind (%) | 40.81 | 42.18 | 41.75 | 42.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.6 | 790.3 | 778.4 | 787.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.455 | 3.874 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.85 | 0.0625 | 0.7458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.7 | 0.7 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 81.4 | 101.1 | 82.48 | 97 |
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
| worker nodes in service, mean | 6 | 4.799 | -20.0% | -1.841 to -0.5616 | yes: GAIN |
| node-hours | 2.509 | 2.012 | -19.8% | -0.7672 to -0.2269 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.4 | +0.2% | -0.4111 to +1.578 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 234.6 | -13.7% | -57.47 to -16.8 | yes: GAIN |
| response time (ms), mean | 275.6 | 243.5 | -11.6% | -51.09 to -13.05 | yes: GAIN |
| response time (ms), 95th percentile | 1004 | 1016 | +1.2% | -142.9 to +167.5 | no |
| response time (ms), 99th percentile | 1567 | 1552 | -0.9% | -212 to +183.4 | no |
| time over the response line (% of samples) | 9.123 | 8.769 | -3.9% | -1.321 to +0.6117 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.1 | -6.2% | -0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 | +43.2 (native is 0) | +28.51 to +57.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.22 | 16 | -1.3% | -3.303 to +2.873 | no |
| utilisation (used / allocatable) | 0.06006 | 0.07415 | +23.4% | +0.005849 to +0.02232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.419 | -1.6% | -0.04552 to -4.844e-05 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01996 | +0.02 (native is 0) | +0.01715 to +0.02277 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.439 | -0.2% | -0.02635 to +0.02071 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 397.8 | -13.9% | -102.1 to -26.39 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.084 | 2.143 | +2.8% | -0.1077 to +0.2254 | no |
| pods started | 0.3 | 0.5 | +66.7% | -0.6121 to +1.012 | no |
| pod start wait, total (s) | 0.7 | 0.9 | +28.6% | -1.338 to +1.738 | no |
| pod start wait, mean (s) | 0.5 | 0.55 | +10.0% | -0.7488 to +0.8488 | no |
| host CPU busy, the real machine under kind (%) | 42.18 | 42.87 | +1.6% | +0.08844 to +1.293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790.3 | 787.6 | -0.3% | -7.097 to +1.697 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.874 | -35.4% | -3.144 to -1.108 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.85 | 0.7458 | -12.3% | -0.3093 to +0.101 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.3 | -23.5% | -1.169 to +0.3689 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.1 | 97 | -4.0% | -10.89 to +2.728 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.902e-15 to -2.294e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.509 | -0.2% | -0.01142 to +0.0004224 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.8 | -0.2% | -1.31 to +0.2449 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.8 | -0.2% | -1.31 to +0.2449 | no |
| response time (ms), mean | 316.8 | 275.6 | -13.0% | -69.65 to -12.85 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 1004 | -6.2% | -245.6 to +113.8 | no |
| response time (ms), 99th percentile | 1497 | 1567 | +4.7% | -228.1 to +368 | no |
| time over the response line (% of samples) | 13.33 | 9.123 | -31.6% | -7.822 to -0.5951 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 6.5 | -12.2% | -1.99 to +0.19 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.765 | 16.22 | +66.1% | +3.384 to +9.519 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.06006 | +0.7% | -0.0007196 to +0.001593 | no |
| CPU used (cores), mean | 1.431 | 1.442 | +0.7% | -0.01727 to +0.03823 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.431 | 1.442 | +0.7% | -0.01727 to +0.03823 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 462 | -0.2% | -11.12 to +9.22 | no |
| HPA replicas, mean | 1.944 | 2.084 | +7.2% | +0.0531 to +0.2276 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | -0.9572 to +1.757 | no |
| pod start wait, mean (s) | 0.15 | 0.5 | +233.3% | -0.5429 to +1.243 | no |
| host CPU busy, the real machine under kind (%) | 40.81 | 42.18 | +3.4% | +0.7023 to +2.041 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.6 | 790.3 | +1.9% | +2.855 to +26.55 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.85 | +1600.0% | +0.532 to +1.068 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.7 | +325.0% | +0.4706 to +2.129 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.4 | 101.1 | +24.2% | +5.353 to +34 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.08 | -15.3% | -1.663 to -0.1772 | yes: GAIN |
| node-hours | 2.514 | 2.13 | -15.3% | -0.6948 to -0.0739 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.4 | +0.0% | -0.9627 to +1.076 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 243.4 | -10.6% | -52.52 to -5.274 | yes: GAIN |
| response time (ms), mean | 316.8 | 288.9 | -8.8% | -39.53 to -16.26 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 1128 | +5.5% | -12.08 to +128.6 | no |
| response time (ms), 99th percentile | 1497 | 1538 | +2.7% | -82.27 to +164.6 | no |
| time over the response line (% of samples) | 13.33 | 13.35 | +0.1% | -0.6402 to +0.6762 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 8.5 | +14.9% | -0.7299 to +2.93 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.1 (native is 0) | +26.47 to +71.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.765 | 9.32 | -4.6% | -2.003 to +1.113 | no |
| utilisation (used / allocatable) | 0.05963 | 0.0708 | +18.7% | +0.00192 to +0.02043 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.421 | -0.7% | -0.05539 to +0.03609 | no |
| Omni's own CPU (cores), mean | 0 | 0.01667 | +0.0167 (native is 0) | +0.01466 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.438 | +0.5% | -0.03851 to +0.05255 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 411.9 | -11.0% | -89.61 to -12.57 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.944 | 2.21 | +13.7% | +0.02333 to +0.5096 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.3 | 0.3 | +0.0% | -0.826 to +0.826 | no |
| pod start wait, mean (s) | 0.15 | 0.3 | +100.0% | -0.3845 to +0.6845 | no |
| host CPU busy, the real machine under kind (%) | 40.81 | 41.75 | +2.3% | +0.7349 to +1.14 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.6 | 778.4 | +0.4% | -0.1163 to +5.716 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.455 | -25.8% | -2.708 to -0.3829 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0625 | +25.0% | -0.01204 to +0.03704 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | +75.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.4 | 82.48 | +1.3% | -1.159 to +3.317 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.08 | -15.3% | -1.663 to -0.1772 | yes: GAIN |
| node-hours | 2.509 | 2.13 | -15.1% | -0.6913 to -0.06646 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.4 | +0.2% | -0.461 to +1.64 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 243.4 | -10.4% | -52 to -4.721 | yes: GAIN |
| response time (ms), mean | 275.6 | 288.9 | +4.8% | -15.56 to +42.27 | no |
| response time (ms), 95th percentile | 1004 | 1128 | +12.4% | -18.62 to +266.9 | no |
| response time (ms), 99th percentile | 1567 | 1538 | -1.8% | -291.7 to +234.1 | no |
| time over the response line (% of samples) | 9.123 | 13.35 | +46.3% | +1.023 to +7.43 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 8.5 | +30.8% | -0.262 to +4.262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.1 (native is 0) | +26.47 to +71.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.22 | 9.32 | -42.5% | -9.938 to -3.856 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06006 | 0.0708 | +17.9% | +0.001076 to +0.0204 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.421 | -1.4% | -0.04909 to +0.008832 | no |
| Omni's own CPU (cores), mean | 0 | 0.01667 | +0.0167 (native is 0) | +0.01466 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.438 | -0.2% | -0.03272 to +0.0258 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 411.9 | -10.9% | -91.95 to -8.329 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.084 | 2.21 | +6.1% | -0.08244 to +0.3347 | no |
| pods started | 0.3 | 0.3 | +0.0% | -0.584 to +0.584 | no |
| pod start wait, total (s) | 0.7 | 0.3 | -57.1% | -1.477 to +0.6769 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | -40.0% | -0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 42.18 | 41.75 | -1.0% | -1.034 to +0.1653 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790.3 | 778.4 | -1.5% | -22.61 to -1.192 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.455 | -25.8% | -2.708 to -0.3829 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.85 | 0.0625 | -92.6% | -1.052 to -0.5234 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.7 | -58.8% | -1.826 to -0.174 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 101.1 | 82.48 | -18.4% | -32.5 to -4.704 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.799 | -20.0% | -1.841 to -0.5616 | yes: GAIN |
| node-hours | 2.514 | 2.012 | -20.0% | -0.772 to -0.2332 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.4 | +0.0% | -0.8781 to +0.9801 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 234.6 | -13.8% | -58.13 to -17.2 | yes: GAIN |
| response time (ms), mean | 316.8 | 243.5 | -23.1% | -97.94 to -48.71 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 1016 | -5.0% | -207.1 to +99.93 | no |
| response time (ms), 99th percentile | 1497 | 1552 | +3.7% | -254.2 to +365.5 | no |
| time over the response line (% of samples) | 13.33 | 8.769 | -34.2% | -8.039 to -1.088 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 6.1 | -17.6% | -2.518 to -0.08188 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 | +43.2 (native is 0) | +28.51 to +57.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.765 | 16 | +63.9% | +2.975 to +9.498 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.07415 | +24.4% | +0.006775 to +0.02227 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.419 | -0.9% | -0.046 to +0.02139 | no |
| Omni's own CPU (cores), mean | 0 | 0.01996 | +0.02 (native is 0) | +0.01715 to +0.02277 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.439 | +0.5% | -0.0249 to +0.04021 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463 | 397.8 | -14.1% | -99.44 to -30.93 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.944 | 2.143 | +10.2% | +0.05257 to +0.3458 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 0.9 | +200.0% | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0.15 | 0.55 | +266.7% | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 40.81 | 42.87 | +5.1% | +1.644 to +2.481 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.6 | 787.6 | +1.5% | +1.8 to +22.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.874 | -35.4% | -3.144 to -1.108 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7458 | +1391.7% | +0.6015 to +0.7901 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | +225.0% | +0.2737 to +1.526 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.4 | 97 | +19.2% | +2.973 to +28.23 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*