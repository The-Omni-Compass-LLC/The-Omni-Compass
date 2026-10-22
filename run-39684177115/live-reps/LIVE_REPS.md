# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.954 | 5.967 |
| node-hours | 2.517 | 2.515 | 2.494 | 2.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.2 | 276.1 | 276.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.2 | 274.6 | 275.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 605.2 | 597.8 | 600.2 | 607.3 |
| response time (ms), 95th percentile | 2366 | 2491 | 2392 | 2528 |
| response time (ms), 99th percentile | 3396 | 3723 | 3477 | 3709 |
| time over the response line (% of samples) | 29.68 | 26.86 | 29.06 | 27.85 |
| failed requests (%) | 0.01156 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 14.3 | 14.3 | 14.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 8 | 8.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.67 | 26.68 | 20.1 | 27.14 |
| utilisation (used / allocatable) | 0.07101 | 0.07106 | 0.07142 | 0.0712 |
| CPU used (cores), mean | 1.704 | 1.706 | 1.701 | 1.7 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01156 | 0.01245 |
| CPU used with Omni's own (cores), mean | 1.704 | 1.706 | 1.712 | 1.712 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.8 | 389.7 | 388.5 | 389.6 |
| HPA replicas, mean | 2.046 | 2.151 | 2.35 | 2.289 |
| pods started | 0 | 0.1 | 0.5 | 0.9 |
| pod start wait, total (s) | 0 | 0.1 | 1.5 | 1.6 |
| pod start wait, mean (s) | 0 | 0.1 | 1.5 | 1.25 |
| host CPU busy, the real machine under kind (%) | 48.46 | 49.33 | 48.99 | 49.83 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 867.8 | 878.5 | 869 | 879.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.891 | 5.927 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5375 | 1.058 | 0.4083 | 0.6708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 2 | 2.3 | 2 |
| queue: job turnaround, submitted to done, mean (s) | 176.5 | 189.9 | 178.4 | 189.4 |
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
| worker nodes in service, mean | 6 | 5.967 | -0.6% | -0.09499 to +0.02898 | no |
| node-hours | 2.515 | 2.503 | -0.5% | -0.03903 to +0.01625 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.4 | +0.1% | -0.5721 to +1.003 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 275.4 | -0.3% | -2.824 to +1.171 | no |
| response time (ms), mean | 597.8 | 607.3 | +1.6% | -11.35 to +30.35 | no |
| response time (ms), 95th percentile | 2491 | 2528 | +1.5% | -119.2 to +192.3 | no |
| response time (ms), 99th percentile | 3723 | 3709 | -0.4% | -274.7 to +245.1 | no |
| time over the response line (% of samples) | 26.86 | 27.85 | +3.7% | +0.1436 to +1.836 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14.4 | +0.7% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.3 | +8.3 (native is 0) | +6.452 to +10.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.68 | 27.14 | +1.8% | -2.538 to +3.475 | no |
| utilisation (used / allocatable) | 0.07106 | 0.0712 | +0.2% | -0.001122 to +0.001406 | no |
| CPU used (cores), mean | 1.706 | 1.7 | -0.3% | -0.0213 to +0.009599 | no |
| Omni's own CPU (cores), mean | 0 | 0.01245 | +0.0125 (native is 0) | +0.01145 to +0.01345 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.706 | 1.712 | +0.4% | -0.00944 to +0.02264 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.7 | 389.6 | -0.0% | -6.014 to +5.892 | no |
| HPA replicas, mean | 2.151 | 2.289 | +6.4% | -0.1004 to +0.3778 | no |
| pods started | 0.1 | 0.9 | +800.0% | +0.2358 to +1.364 | yes: power given |
| pod start wait, total (s) | 0.1 | 1.6 | +1500.0% | +0.369 to +2.631 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.25 | +1150.0% | +0.3951 to +1.905 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.33 | 49.83 | +1.0% | +0.2423 to +0.7466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 878.5 | 879.9 | +0.2% | -1.385 to +4.185 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.927 | -1.2% | -0.2108 to +0.06445 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.058 | 0.6708 | -36.6% | -2.097 to +1.322 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2 | +0.0% | -3.217 to +3.217 | no |
| queue: job turnaround, submitted to done, mean (s) | 189.9 | 189.4 | -0.3% | -4.497 to +3.531 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.734e-15 to +1.024e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.515 | -0.1% | -0.00932 to +0.005653 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.2 | -0.1% | -0.9415 to +0.4931 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.2 | -0.1% | -0.9415 to +0.4931 | no |
| response time (ms), mean | 605.2 | 597.8 | -1.2% | -22.21 to +7.318 | no |
| response time (ms), 95th percentile | 2366 | 2491 | +5.3% | -48.76 to +299.7 | no |
| response time (ms), 99th percentile | 3396 | 3723 | +9.6% | +84.67 to +569.7 | yes: LOSS |
| time over the response line (% of samples) | 29.68 | 26.86 | -9.5% | -3.693 to -1.944 | yes: GAIN |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 14.3 | -1.4% | -0.9388 to +0.5388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.67 | 26.68 | +23.1% | +1.381 to +8.636 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07101 | 0.07106 | +0.1% | -0.0005773 to +0.0006749 | no |
| CPU used (cores), mean | 1.704 | 1.706 | +0.1% | -0.01385 to +0.0162 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.704 | 1.706 | +0.1% | -0.01385 to +0.0162 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.8 | 389.7 | -0.0% | -3.595 to +3.291 | no |
| HPA replicas, mean | 2.046 | 2.151 | +5.1% | -0.08253 to +0.2921 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 48.46 | 49.33 | +1.8% | +0.6549 to +1.09 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.8 | 878.5 | +1.2% | +7.036 to +14.36 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5375 | 1.058 | +96.9% | -0.602 to +1.644 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 2 | -33.3% | -2.545 to +0.5452 | no |
| queue: job turnaround, submitted to done, mean (s) | 176.5 | 189.9 | +7.6% | +9.365 to +17.45 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.954 | -0.8% | -0.1074 to +0.01591 | no |
| node-hours | 2.517 | 2.494 | -0.9% | -0.0434 to -0.001044 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.1 | -0.1% | -1.519 to +0.8276 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 274.6 | -0.6% | -3.399 to -0.1758 | yes: GAIN |
| response time (ms), mean | 605.2 | 600.2 | -0.8% | -19.5 to +9.523 | no |
| response time (ms), 95th percentile | 2366 | 2392 | +1.1% | -68.05 to +119.9 | no |
| response time (ms), 99th percentile | 3396 | 3477 | +2.4% | -109 to +270.3 | no |
| time over the response line (% of samples) | 29.68 | 29.06 | -2.1% | -1.62 to +0.3848 | no |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 14.3 | -1.4% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8 | +8 (native is 0) | +5.345 to +10.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.67 | 20.1 | -7.2% | -3.499 to +0.3622 | no |
| utilisation (used / allocatable) | 0.07101 | 0.07142 | +0.6% | -0.0002873 to +0.001103 | no |
| CPU used (cores), mean | 1.704 | 1.701 | -0.2% | -0.01867 to +0.01148 | no |
| Omni's own CPU (cores), mean | 0 | 0.01156 | +0.0116 (native is 0) | +0.0109 to +0.01222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.704 | 1.712 | +0.5% | -0.007144 to +0.02307 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.8 | 388.5 | -0.4% | -4.665 to +1.906 | no |
| HPA replicas, mean | 2.046 | 2.35 | +14.9% | +0.08278 to +0.5252 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | -0.4734 to +3.473 | no |
| pod start wait, mean (s) | 0 | 1.5 | +1.5 (native is 0) | -0.4734 to +3.473 | no |
| host CPU busy, the real machine under kind (%) | 48.46 | 48.99 | +1.1% | +0.1724 to +0.8956 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.8 | 869 | +0.1% | -2.537 to +4.937 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.891 | -1.8% | -0.263 to +0.04539 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5375 | 0.4083 | -24.0% | -0.3077 to +0.04936 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 2.3 | -23.3% | -2.388 to +0.9877 | no |
| queue: job turnaround, submitted to done, mean (s) | 176.5 | 178.4 | +1.1% | -1.821 to +5.646 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.954 | -0.8% | -0.1074 to +0.01591 | no |
| node-hours | 2.515 | 2.494 | -0.8% | -0.04589 to +0.005115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.1 | -0.0% | -0.9412 to +0.6984 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 274.6 | -0.6% | -3.48 to +0.3544 | no |
| response time (ms), mean | 597.8 | 600.2 | +0.4% | -24.6 to +29.51 | no |
| response time (ms), 95th percentile | 2491 | 2392 | -4.0% | -286.6 to +87.55 | no |
| response time (ms), 99th percentile | 3723 | 3477 | -6.6% | -468.3 to -24.78 | yes: GAIN |
| time over the response line (% of samples) | 26.86 | 29.06 | +8.2% | +1.205 to +3.197 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14.3 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8 | +8 (native is 0) | +5.345 to +10.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.68 | 20.1 | -24.7% | -10.15 to -3.008 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.07106 | 0.07142 | +0.5% | -0.0006462 to +0.001364 | no |
| CPU used (cores), mean | 1.706 | 1.701 | -0.3% | -0.01935 to +0.009812 | no |
| Omni's own CPU (cores), mean | 0 | 0.01156 | +0.0116 (native is 0) | +0.0109 to +0.01222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.706 | 1.712 | +0.4% | -0.007882 to +0.02146 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.7 | 388.5 | -0.3% | -5.421 to +2.967 | no |
| HPA replicas, mean | 2.151 | 2.35 | +9.3% | -0.03525 to +0.4337 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.1 | 1.5 | +1400.0% | -0.6006 to +3.401 | no |
| pod start wait, mean (s) | 0.1 | 1.5 | +1400.0% | -0.6006 to +3.401 | no |
| host CPU busy, the real machine under kind (%) | 49.33 | 48.99 | -0.7% | -0.5872 to -0.08917 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 878.5 | 869 | -1.1% | -14.24 to -4.764 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.891 | -1.8% | -0.263 to +0.04539 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.058 | 0.4083 | -61.4% | -1.89 to +0.5896 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2.3 | +15.0% | -1.388 to +1.988 | no |
| queue: job turnaround, submitted to done, mean (s) | 189.9 | 178.4 | -6.1% | -16.86 to -6.132 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.967 | -0.6% | -0.09499 to +0.02898 | no |
| node-hours | 2.517 | 2.503 | -0.5% | -0.03873 to +0.01229 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.4 | -0.0% | -1.032 to +1.014 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 275.4 | -0.4% | -2.963 to +0.8617 | no |
| response time (ms), mean | 605.2 | 607.3 | +0.3% | -16.24 to +20.35 | no |
| response time (ms), 95th percentile | 2366 | 2528 | +6.8% | +9.017 to +315.1 | yes: LOSS |
| response time (ms), 99th percentile | 3396 | 3709 | +9.2% | +77.07 to +547.7 | yes: LOSS |
| time over the response line (% of samples) | 29.68 | 27.85 | -6.2% | -2.807 to -0.8507 | yes: GAIN |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 14.4 | -0.7% | -0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.3 | +8.3 (native is 0) | +6.452 to +10.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.67 | 27.14 | +25.3% | -0.1398 to +11.09 | no |
| utilisation (used / allocatable) | 0.07101 | 0.0712 | +0.3% | -0.00113 to +0.001511 | no |
| CPU used (cores), mean | 1.704 | 1.7 | -0.3% | -0.02569 to +0.01634 | no |
| Omni's own CPU (cores), mean | 0 | 0.01245 | +0.0125 (native is 0) | +0.01145 to +0.01345 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.704 | 1.712 | +0.5% | -0.01359 to +0.02914 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.8 | 389.6 | -0.1% | -6.932 to +6.505 | no |
| HPA replicas, mean | 2.046 | 2.289 | +11.9% | +0.04053 to +0.4464 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | +0.3722 to +1.428 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | +0.5231 to +2.677 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.25 | +1.25 (native is 0) | +0.5498 to +1.95 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.46 | 49.83 | +2.8% | +1.114 to +1.619 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.8 | 879.9 | +1.4% | +8.823 to +15.38 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.927 | -1.2% | -0.2108 to +0.06445 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5375 | 0.6708 | +24.8% | -0.672 to +0.9387 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 2 | -33.3% | -5.13 to +3.13 | no |
| queue: job turnaround, submitted to done, mean (s) | 176.5 | 189.4 | +7.3% | +9.311 to +16.54 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*