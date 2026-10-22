# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.3 | 7.295 |
| node-hours | 5.022 | 5.022 | 4.731 | 3.053 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 504.1 | 526.3 | 504.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 504.1 | 504.2 | 356.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 626.4 | 128.6 | 637.9 | 76.39 |
| response time (ms), 95th percentile | 2523 | 177.5 | 2753 | 100.4 |
| response time (ms), 99th percentile | 3423 | 199.2 | 3829 | 137.4 |
| time over the response line (% of samples) | 24.12 | 0 | 24.4 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 0 | 13.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 57.4 | 25.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 0.1067 | 15.46 | 0.1317 |
| utilisation (used / allocatable) | 0.03527 | 0.006183 | 0.03804 | 0.008955 |
| CPU used (cores), mean | 1.693 | 0.2968 | 1.719 | 0.2619 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01192 | 0.00899 |
| CPU used with Omni's own (cores), mean | 1.693 | 0.2968 | 1.731 | 0.2709 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 4109 | 711.8 | 3306 |
| HPA replicas, mean | 3.989 | 4.298 | 4.678 | 4.412 |
| pods started | 0.1 | 0.9 | 1.4 | 1 |
| pod start wait, total (s) | 0.2 | 1.9 | 2.2 | 1.5 |
| pod start wait, mean (s) | 0.2 | 1.033 | 1.1 | 0.9 |
| host CPU busy, the real machine under kind (%) | 51.68 | 14.16 | 53.64 | 15.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 873.6 | 1503 | 895.8 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.66 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1157 | 0.05 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1473 | 0.2 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 182.9 | 1157 | 201 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.295 | -39.2% | -5.245 to -4.166 | yes: GAIN |
| node-hours | 5.022 | 3.053 | -39.2% | -2.201 to -1.737 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.1 | 504.2 | +0.0% | -1.489 to +1.746 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.1 | 356.6 | -29.3% | -165.2 to -129.8 | yes: GAIN |
| response time (ms), mean | 128.6 | 76.39 | -40.6% | -60.18 to -44.3 | yes: GAIN |
| response time (ms), 95th percentile | 177.5 | 100.4 | -43.4% | -89.71 to -64.54 | yes: GAIN |
| response time (ms), 99th percentile | 199.2 | 137.4 | -31.0% | -76.3 to -47.2 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 | +25.1 (native is 0) | +24.12 to +26.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1317 | +23.4% | -0.1452 to +0.1952 | no |
| utilisation (used / allocatable) | 0.006183 | 0.008955 | +44.8% | +0.002473 to +0.003071 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2968 | 0.2619 | -11.7% | -0.04339 to -0.02629 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00899 | +0.00899 (native is 0) | +0.007948 to +0.01003 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2968 | 0.2709 | -8.7% | -0.03481 to -0.0169 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4109 | 3306 | -19.5% | -893.7 to -712.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.298 | 4.412 | +2.6% | -0.08705 to +0.3144 | no |
| pods started | 0.9 | 1 | +11.1% | -1.041 to +1.241 | no |
| pod start wait, total (s) | 1.9 | 1.5 | -21.1% | -2.741 to +1.941 | no |
| pod start wait, mean (s) | 1.033 | 0.9 | -12.9% | -1.39 to +1.123 | no |
| host CPU busy, the real machine under kind (%) | 14.16 | 15.5 | +9.5% | +0.9283 to +1.748 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 1505 | +0.1% | -3.385 to +5.985 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1157 | 1158 | +0.1% | -3.374 to +5.583 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 1474 | +0.1% | -3.161 to +5.761 | no |
| queue: job turnaround, submitted to done, mean (s) | 1157 | 1158 | +0.1% | -3.374 to +5.583 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -4.436e-15 to +1.727e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.022 | 5.022 | -0.0% | -0.01648 to +0.01582 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 504.1 | -4.1% | -24.47 to -18.4 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 504.1 | -4.1% | -24.47 to -18.4 | yes: GAIN |
| response time (ms), mean | 626.4 | 128.6 | -79.5% | -764 to -231.5 | yes: GAIN |
| response time (ms), 95th percentile | 2523 | 177.5 | -93.0% | -3632 to -1059 | yes: GAIN |
| response time (ms), 99th percentile | 3423 | 199.2 | -94.2% | -4898 to -1548 | yes: GAIN |
| time over the response line (% of samples) | 24.12 | 0 | -100.0% | -34.64 to -13.61 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 0 | -100.0% | -16.8 to -8.399 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 0.1067 | -99.3% | -21.22 to -8.909 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03527 | 0.006183 | -82.5% | -0.03248 to -0.0257 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.693 | 0.2968 | -82.5% | -1.559 to -1.234 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.693 | 0.2968 | -82.5% | -1.559 to -1.234 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 4109 | +442.8% | +3052 to +3653 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.989 | 4.298 | +7.8% | +0.02697 to +0.592 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | -0.1417 to +1.742 | no |
| pod start wait, total (s) | 0.2 | 1.9 | +850.0% | -0.3525 to +3.752 | no |
| pod start wait, mean (s) | 0.2 | 1.033 | +416.7% | -0.2462 to +1.913 | no |
| host CPU busy, the real machine under kind (%) | 51.68 | 14.16 | -72.6% | -41.97 to -33.08 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 873.6 | 1503 | +72.1% | +539.3 to +720.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1157 | +1461226.3% | +1153 to +1161 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1473 | +245383.3% | +1468 to +1476 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 182.9 | 1157 | +532.7% | +885 to +1063 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.3 | -5.8% | -1.666 to +0.2646 | no |
| node-hours | 5.022 | 4.731 | -5.8% | -0.6891 to +0.1073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 526.3 | +0.1% | -0.5303 to +1.967 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 504.2 | -4.1% | -51.27 to +8.575 | no |
| response time (ms), mean | 626.4 | 637.9 | +1.8% | -55.46 to +78.39 | no |
| response time (ms), 95th percentile | 2523 | 2753 | +9.1% | -38.02 to +497.9 | no |
| response time (ms), 99th percentile | 3423 | 3829 | +11.9% | +64.2 to +749.2 | yes: LOSS |
| time over the response line (% of samples) | 24.12 | 24.4 | +1.1% | -1.449 to +2.001 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 13.4 | +6.3% | +0.06123 to +1.539 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.4 | +57.4 (native is 0) | +28.56 to +86.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 15.46 | +1.9% | -3.171 to +3.744 | no |
| utilisation (used / allocatable) | 0.03527 | 0.03804 | +7.9% | -1.589e-05 to +0.005557 | no |
| CPU used (cores), mean | 1.693 | 1.719 | +1.5% | -0.02501 to +0.07732 | no |
| Omni's own CPU (cores), mean | 0 | 0.01192 | +0.0119 (native is 0) | +0.01114 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.693 | 1.731 | +2.2% | -0.01332 to +0.08947 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 711.8 | -6.0% | -92.9 to +2.431 | no |
| HPA replicas, mean | 3.989 | 4.678 | +17.3% | +0.3532 to +1.026 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.6214 to +1.979 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.2 | +1000.0% | +0.9337 to +3.066 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.1 | +450.0% | +0.3208 to +1.479 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.68 | 53.64 | +3.8% | +0.8639 to +3.047 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 873.6 | 895.8 | +2.5% | -1.669 to +46.07 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.66 | -11.2% | -3.114 to +0.4351 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.05 | -36.8% | -0.07587 to +0.01754 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.2 | -66.7% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 182.9 | 201 | +9.9% | -4.027 to +40.29 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.3 | -5.8% | -1.666 to +0.2646 | no |
| node-hours | 5.022 | 4.731 | -5.8% | -0.694 to +0.1129 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.1 | 526.3 | +4.4% | +18.97 to +25.33 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.1 | 504.2 | +0.0% | -32.19 to +32.36 | no |
| response time (ms), mean | 128.6 | 637.9 | +395.9% | +204 to +814.5 | yes: LOSS |
| response time (ms), 95th percentile | 177.5 | 2753 | +1450.8% | +1134 to +4018 | yes: LOSS |
| response time (ms), 99th percentile | 199.2 | 3829 | +1822.8% | +1680 to +5580 | yes: LOSS |
| time over the response line (% of samples) | 0 | 24.4 | +24.4 (native is 0) | +13.72 to +35.08 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 13.4 | +13.4 (native is 0) | +9.508 to +17.29 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.4 | +57.4 (native is 0) | +28.56 to +86.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 15.46 | +14393.8% | +8.271 to +22.44 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006183 | 0.03804 | +515.3% | +0.0288 to +0.03492 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2968 | 1.719 | +479.3% | +1.23 to +1.615 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01192 | +0.0119 (native is 0) | +0.01114 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2968 | 1.731 | +483.3% | +1.242 to +1.627 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4109 | 711.8 | -82.7% | -3733 to -3062 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.298 | 4.678 | +8.8% | +0.1691 to +0.5916 | yes: power given |
| pods started | 0.9 | 1.4 | +55.6% | -0.9795 to +1.979 | no |
| pod start wait, total (s) | 1.9 | 2.2 | +15.8% | -2.602 to +3.202 | no |
| pod start wait, mean (s) | 1.033 | 1.1 | +6.5% | -1.248 to +1.381 | no |
| host CPU busy, the real machine under kind (%) | 14.16 | 53.64 | +278.8% | +34.21 to +44.76 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 895.8 | -40.4% | -717.1 to -498.1 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1157 | 0.05 | -100.0% | -1161 to -1153 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 0.2 | -100.0% | -1477 to -1469 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1157 | 201 | -82.6% | -1060 to -852.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.295 | -39.2% | -5.245 to -4.166 | yes: GAIN |
| node-hours | 5.022 | 3.053 | -39.2% | -2.2 to -1.738 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 504.2 | -4.1% | -23.34 to -19.27 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 356.6 | -32.1% | -184.7 to -153.2 | yes: GAIN |
| response time (ms), mean | 626.4 | 76.39 | -87.8% | -821.3 to -278.7 | yes: GAIN |
| response time (ms), 95th percentile | 2523 | 100.4 | -96.0% | -3713 to -1133 | yes: GAIN |
| response time (ms), 99th percentile | 3423 | 137.4 | -96.0% | -4962 to -1608 | yes: GAIN |
| time over the response line (% of samples) | 24.12 | 0 | -100.0% | -34.64 to -13.61 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 0 | -100.0% | -16.8 to -8.399 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 | +25.1 (native is 0) | +24.12 to +26.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.17 | 0.1317 | -99.1% | -21.13 to -8.953 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03527 | 0.008955 | -74.6% | -0.02972 to -0.02291 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.693 | 0.2619 | -84.5% | -1.588 to -1.274 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00899 | +0.00899 (native is 0) | +0.007948 to +0.01003 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.693 | 0.2709 | -84.0% | -1.578 to -1.266 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757 | 3306 | +336.7% | +2307 to +2791 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.989 | 4.412 | +10.6% | +0.132 to +0.7142 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | +0.2737 to +1.526 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.5 | +650.0% | +0.2856 to +2.314 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | +0.04268 to +1.357 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.68 | 15.5 | -70.0% | -40.31 to -32.06 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 873.6 | 1505 | +72.2% | +542 to +720.2 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1158 | +1462621.1% | +1155 to +1160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1474 | +245600.0% | +1471 to +1476 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 182.9 | 1158 | +533.3% | +887.3 to +1063 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*