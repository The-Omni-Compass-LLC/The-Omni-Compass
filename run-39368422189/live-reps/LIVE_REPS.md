# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.291 | 5.091 |
| node-hours | 2.517 | 2.51 | 2.22 | 2.135 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | 272.7 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | 250.3 | 243.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.7 | 253.5 | 286.6 | 223.2 |
| response time (ms), 95th percentile | 1065 | 758.9 | 1145 | 839.4 |
| response time (ms), 99th percentile | 1483 | 1326 | 1638 | 1413 |
| time over the response line (% of samples) | 15.07 | 9.369 | 14.5 | 8.687 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 6.9 | 8.5 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.7 | 38.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.892 | 14.68 | 10.15 | 14.74 |
| utilisation (used / allocatable) | 0.0594 | 0.05954 | 0.06778 | 0.07025 |
| CPU used (cores), mean | 1.426 | 1.429 | 1.418 | 1.414 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01698 | 0.01846 |
| CPU used with Omni's own (cores), mean | 1.426 | 1.429 | 1.435 | 1.432 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 464.1 | 424.1 | 414.3 |
| HPA replicas, mean | 1.984 | 2.058 | 2.001 | 2.143 |
| pods started | 0.1 | 0 | 0.1 | 0.3 |
| pod start wait, total (s) | 0.2 | 0 | 0.2 | 1.2 |
| pod start wait, mean (s) | 0.2 | 0 | 0.2 | 1.2 |
| host CPU busy, the real machine under kind (%) | 40.44 | 41.46 | 41.28 | 42.42 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 770.9 | 781.9 | 775.3 | 784.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.767 | 4.371 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7958 | 0.05833 | 0.7583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.2 | 0.5 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 75.65 | 93.17 | 82.42 | 95.34 |
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
| worker nodes in service, mean | 6 | 5.091 | -15.2% | -1.619 to -0.2004 | yes: GAIN |
| node-hours | 2.51 | 2.135 | -15.0% | -0.6719 to -0.08007 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.3 | +0.2% | -0.5588 to +1.387 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 243.7 | -10.4% | -50.41 to -5.909 | yes: GAIN |
| response time (ms), mean | 253.5 | 223.2 | -12.0% | -51.14 to -9.558 | yes: GAIN |
| response time (ms), 95th percentile | 758.9 | 839.4 | +10.6% | -52.81 to +213.9 | no |
| response time (ms), 99th percentile | 1326 | 1413 | +6.6% | -69.29 to +243.3 | no |
| time over the response line (% of samples) | 9.369 | 8.687 | -7.3% | -2.179 to +0.8145 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.3 | +5.8% | -0.3689 to +1.169 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.3 (native is 0) | +22.68 to +53.92 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.68 | 14.74 | +0.4% | -2.729 to +2.856 | no |
| utilisation (used / allocatable) | 0.05954 | 0.07025 | +18.0% | +0.002329 to +0.01908 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.414 | -1.1% | -0.04249 to +0.01173 | no |
| Omni's own CPU (cores), mean | 0 | 0.01846 | +0.0185 (native is 0) | +0.01514 to +0.02178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.432 | +0.2% | -0.02543 to +0.03159 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 414.3 | -10.7% | -89.32 to -10.25 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.143 | +4.1% | -0.07704 to +0.2468 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | -0.3004 to +2.7 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | -0.3004 to +2.7 | no |
| host CPU busy, the real machine under kind (%) | 41.46 | 42.42 | +2.3% | +0.5652 to +1.368 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 781.9 | 784.7 | +0.4% | -1.607 to +7.207 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.371 | -27.2% | -2.755 to -0.5033 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.7583 | -4.7% | -0.1503 to +0.07529 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.3 | +8.3% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.17 | 95.34 | +2.3% | -1.949 to +6.299 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.086e-15 to +3.098e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.51 | -0.2% | -0.01496 to +0.002631 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | -0.2% | -1.595 to +0.4711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | -0.2% | -1.595 to +0.4711 | no |
| response time (ms), mean | 313.7 | 253.5 | -19.2% | -90.79 to -29.51 | yes: GAIN |
| response time (ms), 95th percentile | 1065 | 758.9 | -28.8% | -457.4 to -155.4 | yes: GAIN |
| response time (ms), 99th percentile | 1483 | 1326 | -10.6% | -438 to +122.7 | no |
| time over the response line (% of samples) | 15.07 | 9.369 | -37.8% | -9.281 to -2.123 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 6.9 | -20.7% | -3.9 to +0.3004 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.892 | 14.68 | +48.4% | +3.63 to +5.936 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0594 | 0.05954 | +0.2% | -0.0007411 to +0.001025 | no |
| CPU used (cores), mean | 1.426 | 1.429 | +0.2% | -0.01779 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.426 | 1.429 | +0.2% | -0.01779 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 464.1 | +0.2% | -6.047 to +8.066 | no |
| HPA replicas, mean | 1.984 | 2.058 | +3.8% | -0.02148 to +0.1704 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 40.44 | 41.46 | +2.5% | +0.7084 to +1.326 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.9 | 781.9 | +1.4% | +2.246 to +19.75 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7958 | +1491.7% | +0.5425 to +0.9492 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.2 | +500.0% | +0.6628 to +1.337 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.65 | 93.17 | +23.2% | +5.195 to +29.84 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.291 | -11.8% | -1.425 to +0.006405 | no |
| node-hours | 2.517 | 2.22 | -11.8% | -0.5966 to +0.004082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.7 | +0.1% | -0.4148 to +1.038 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 250.3 | -8.1% | -44.76 to +0.6192 | no |
| response time (ms), mean | 313.7 | 286.6 | -8.6% | -40.88 to -13.21 | yes: GAIN |
| response time (ms), 95th percentile | 1065 | 1145 | +7.5% | -1.116 to +160.4 | no |
| response time (ms), 99th percentile | 1483 | 1638 | +10.4% | -12.9 to +322 | no |
| time over the response line (% of samples) | 15.07 | 14.5 | -3.8% | -1.18 to +0.03443 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.5 | -2.3% | -1.308 to +0.9081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.7 | +49.7 (native is 0) | +37.2 to +62.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.892 | 10.15 | +2.6% | -1.35 to +1.867 | no |
| utilisation (used / allocatable) | 0.0594 | 0.06778 | +14.1% | +0.0003642 to +0.0164 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.426 | 1.418 | -0.5% | -0.04727 to +0.03199 | no |
| Omni's own CPU (cores), mean | 0 | 0.01698 | +0.017 (native is 0) | +0.0147 to +0.01926 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.426 | 1.435 | +0.7% | -0.03095 to +0.04963 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 424.1 | -8.4% | -75.69 to -2.303 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.001 | +0.9% | -0.1184 to +0.1532 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 40.44 | 41.28 | +2.1% | +0.3134 to +1.368 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.9 | 775.3 | +0.6% | +0.0268 to +8.773 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.767 | -20.5% | -2.412 to -0.05316 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05833 | +16.7% | -0.04572 to +0.06238 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.65 | 82.43 | +9.0% | +1.101 to +12.45 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.291 | -11.8% | -1.425 to +0.006405 | no |
| node-hours | 2.51 | 2.22 | -11.6% | -0.5852 to +0.005021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.7 | +0.3% | +0.01724 to +1.729 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 250.3 | -7.9% | -43.51 to +0.4975 | no |
| response time (ms), mean | 253.5 | 286.6 | +13.1% | -3.833 to +70.03 | no |
| response time (ms), 95th percentile | 758.9 | 1145 | +50.9% | +175.7 to +596.3 | yes: LOSS |
| response time (ms), 99th percentile | 1326 | 1638 | +23.6% | +14.29 to +610.1 | yes: LOSS |
| time over the response line (% of samples) | 9.369 | 14.5 | +54.8% | +1.789 to +8.47 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 8.5 | +23.2% | -0.126 to +3.326 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.7 | +49.7 (native is 0) | +37.2 to +62.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.68 | 10.15 | -30.8% | -6.405 to -2.645 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05954 | 0.06778 | +13.8% | -0.0003961 to +0.01687 | no |
| CPU used (cores), mean | 1.429 | 1.418 | -0.8% | -0.03928 to +0.01718 | no |
| Omni's own CPU (cores), mean | 0 | 0.01698 | +0.017 (native is 0) | +0.0147 to +0.01926 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.435 | +0.4% | -0.02268 to +0.03454 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 424.1 | -8.6% | -82.05 to +2.036 | no |
| HPA replicas, mean | 2.058 | 2.001 | -2.8% | -0.1868 to +0.07261 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 41.46 | 41.28 | -0.4% | -0.5487 to +0.1962 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 781.9 | 775.3 | -0.8% | -11.91 to -1.288 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.767 | -20.5% | -2.412 to -0.05316 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.05833 | -92.7% | -0.9038 to -0.5712 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.5 | -58.3% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 93.17 | 82.42 | -11.5% | -17.78 to -3.701 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.091 | -15.2% | -1.619 to -0.2004 | yes: GAIN |
| node-hours | 2.517 | 2.135 | -15.2% | -0.6813 to -0.08298 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 | -0.1% | -1.19 to +0.8947 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 243.7 | -10.5% | -51.43 to -6.013 | yes: GAIN |
| response time (ms), mean | 313.7 | 223.2 | -28.8% | -127.8 to -53.18 | yes: GAIN |
| response time (ms), 95th percentile | 1065 | 839.4 | -21.2% | -386.8 to -64.76 | yes: GAIN |
| response time (ms), 99th percentile | 1483 | 1413 | -4.8% | -405 to +263.6 | no |
| time over the response line (% of samples) | 15.07 | 8.687 | -42.4% | -10.99 to -1.775 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 7.3 | -16.1% | -3.059 to +0.2588 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.3 (native is 0) | +22.68 to +53.92 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.892 | 14.74 | +49.0% | +1.621 to +8.072 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0594 | 0.07025 | +18.3% | +0.002942 to +0.01875 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.426 | 1.414 | -0.8% | -0.04743 to +0.02348 | no |
| Omni's own CPU (cores), mean | 0 | 0.01846 | +0.0185 (native is 0) | +0.01514 to +0.02178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.426 | 1.432 | +0.5% | -0.03046 to +0.04344 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 414.3 | -10.5% | -84.32 to -13.23 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.143 | +8.0% | -0.003396 to +0.3221 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | -0.6519 to +2.652 | no |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | -0.6519 to +2.652 | no |
| host CPU busy, the real machine under kind (%) | 40.44 | 42.42 | +4.9% | +1.498 to +2.469 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.9 | 784.7 | +1.8% | +2.979 to +24.62 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.371 | -27.2% | -2.755 to -0.5033 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7583 | +1416.7% | +0.4934 to +0.9233 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.3 | +550.0% | +0.8738 to +1.326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.65 | 95.34 | +26.0% | +6.149 to +33.23 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*