# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.182 | 5.124 |
| node-hours | 2.519 | 2.512 | 2.176 | 2.148 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.3 | 272.3 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.3 | 246.5 | 243.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.4 | 307.2 | 314 | 321.9 |
| response time (ms), 95th percentile | 1100 | 1125 | 1156 | 1226 |
| response time (ms), 99th percentile | 1622 | 1741 | 1673 | 1925 |
| time over the response line (% of samples) | 13.36 | 12.46 | 13.07 | 12.38 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.5 | 8 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 9 | 10.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.75 | 12.24 | 11.05 | 13.53 |
| utilisation (used / allocatable) | 0.0588 | 0.05873 | 0.06841 | 0.06666 |
| CPU used (cores), mean | 1.411 | 1.409 | 1.4 | 1.364 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01132 | 0.01246 |
| CPU used with Omni's own (cores), mean | 1.411 | 1.409 | 1.411 | 1.376 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.7 | 474.5 | 424.7 | 435.5 |
| HPA replicas, mean | 2.089 | 2.053 | 2.304 | 2.203 |
| pods started | 0 | 0.1 | 0.5 | 0.5 |
| pod start wait, total (s) | 0 | 0.2 | 0.9 | 0.7 |
| pod start wait, mean (s) | 0 | 0.2 | 0.9 | 0.55 |
| host CPU busy, the real machine under kind (%) | 40.23 | 41.05 | 40.84 | 41.69 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.6 | 782 | 777.6 | 783.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.615 | 4.435 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.3292 | 0.06667 | 0.2167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.8 | 0.3 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 84.23 | 89.93 | 85.03 | 92.71 |
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
| worker nodes in service, mean | 6 | 5.124 | -14.6% | -1.646 to -0.1062 | yes: GAIN |
| node-hours | 2.512 | 2.148 | -14.5% | -0.6863 to -0.04156 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.1 | -0.1% | -1.158 to +0.8376 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 243.6 | -10.2% | -52.49 to -2.946 | yes: GAIN |
| response time (ms), mean | 307.2 | 321.9 | +4.8% | -4.634 to +34.18 | no |
| response time (ms), 95th percentile | 1125 | 1226 | +9.0% | -3.008 to +205 | no |
| response time (ms), 99th percentile | 1741 | 1925 | +10.6% | -21.06 to +389.6 | no |
| time over the response line (% of samples) | 12.46 | 12.38 | -0.6% | -0.9348 to +0.7796 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.6 | +1.3% | -0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.6 | +10.6 (native is 0) | +8.657 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 13.53 | +10.5% | -0.2304 to +2.804 | no |
| utilisation (used / allocatable) | 0.05873 | 0.06666 | +13.5% | +0.001013 to +0.01486 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.364 | -3.3% | -0.09545 to +0.003632 | no |
| Omni's own CPU (cores), mean | 0 | 0.01246 | +0.0125 (native is 0) | +0.01122 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.376 | -2.4% | -0.08246 to +0.01556 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.5 | 435.5 | -8.2% | -72.22 to -5.778 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.053 | 2.203 | +7.3% | -0.05219 to +0.3533 | no |
| pods started | 0.1 | 0.5 | +400.0% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | -0.4685 to +1.469 | no |
| pod start wait, mean (s) | 0.2 | 0.55 | +175.0% | -0.4417 to +1.142 | no |
| host CPU busy, the real machine under kind (%) | 41.05 | 41.69 | +1.6% | +0.3116 to +0.9665 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 782 | 783.6 | +0.2% | -3.669 to +6.869 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.435 | -26.1% | -2.913 to -0.2169 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 0.2167 | -34.2% | -0.5067 to +0.2817 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 0.9 | -50.0% | -3.198 to +1.398 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.93 | 92.71 | +3.1% | -2.895 to +8.462 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.935e-15 to +1.402e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.512 | -0.3% | -0.01373 to +6.003e-05 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.3 | -0.3% | -1.65 to +0.03948 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.3 | -0.3% | -1.65 to +0.03948 | no |
| response time (ms), mean | 313.4 | 307.2 | -2.0% | -21.41 to +8.979 | no |
| response time (ms), 95th percentile | 1100 | 1125 | +2.3% | -73.47 to +123.2 | no |
| response time (ms), 99th percentile | 1622 | 1741 | +7.3% | -95.85 to +332.4 | no |
| time over the response line (% of samples) | 13.36 | 12.46 | -6.7% | -1.629 to -0.1651 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.5 | -6.2% | -1.631 to +0.631 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.75 | 12.24 | +13.8% | -0.01319 to +2.99 | no |
| utilisation (used / allocatable) | 0.0588 | 0.05873 | -0.1% | -0.001025 to +0.0008899 | no |
| CPU used (cores), mean | 1.411 | 1.409 | -0.1% | -0.02461 to +0.02136 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.411 | 1.409 | -0.1% | -0.02461 to +0.02136 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.7 | 474.5 | +0.4% | -7.64 to +11.26 | no |
| HPA replicas, mean | 2.089 | 2.053 | -1.7% | -0.152 to +0.07948 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.23 | 41.05 | +2.0% | +0.5165 to +1.121 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.6 | 782 | +0.7% | +0.8735 to +9.927 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.3292 | +216.0% | -0.07836 to +0.5284 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.8 | +125.0% | -0.306 to +2.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.23 | 89.93 | +6.8% | +0.08211 to +11.32 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.182 | -13.6% | -1.587 to -0.04913 | yes: GAIN |
| node-hours | 2.519 | 2.176 | -13.6% | -0.6632 to -0.02173 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.3 | +0.1% | -0.6576 to +0.9476 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 246.5 | -9.4% | -49.67 to -1.533 | yes: GAIN |
| response time (ms), mean | 313.4 | 314 | +0.2% | -6.852 to +8.015 | no |
| response time (ms), 95th percentile | 1100 | 1156 | +5.1% | -25.4 to +136.9 | no |
| response time (ms), 99th percentile | 1622 | 1673 | +3.1% | -87.65 to +188.8 | no |
| time over the response line (% of samples) | 13.36 | 13.07 | -2.2% | -1.034 to +0.4547 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8 | +0.0% | -1.118 to +1.118 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9 | +9 (native is 0) | +5.17 to +12.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.75 | 11.05 | +2.7% | -1.011 to +1.595 | no |
| utilisation (used / allocatable) | 0.0588 | 0.06841 | +16.4% | +0.0001809 to +0.01905 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.4 | -0.8% | -0.03442 to +0.01199 | no |
| Omni's own CPU (cores), mean | 0 | 0.01132 | +0.0113 (native is 0) | +0.01028 to +0.01236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.411 | +0.0% | -0.02313 to +0.02333 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.7 | 424.7 | -10.2% | -92.56 to -3.46 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.304 | +10.3% | -0.08922 to +0.5183 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.23 | 40.84 | +1.5% | +0.4608 to +0.7534 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.6 | 777.6 | +0.1% | -2.016 to +4.016 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.615 | -23.1% | -2.637 to -0.1338 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.06667 | -36.0% | -0.09785 to +0.02285 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | -62.5% | -1.408 to +0.4079 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.23 | 85.03 | +0.9% | -2.462 to +4.062 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.182 | -13.6% | -1.587 to -0.04913 | yes: GAIN |
| node-hours | 2.512 | 2.176 | -13.4% | -0.6585 to -0.01269 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 272.3 | +0.4% | -0.2871 to +2.188 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 246.5 | -9.1% | -48.86 to -0.7287 | yes: GAIN |
| response time (ms), mean | 307.2 | 314 | +2.2% | -6.506 to +20.1 | no |
| response time (ms), 95th percentile | 1125 | 1156 | +2.7% | -54.3 to +116.1 | no |
| response time (ms), 99th percentile | 1741 | 1673 | -3.9% | -261.2 to +125.8 | no |
| time over the response line (% of samples) | 12.46 | 13.07 | +4.9% | -0.1133 to +1.328 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8 | +6.7% | -0.9005 to +1.9 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9 | +9 (native is 0) | +5.17 to +12.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 11.04 | -9.8% | -2.745 to +0.3521 | no |
| utilisation (used / allocatable) | 0.05873 | 0.06841 | +16.5% | -0.0003785 to +0.01975 | no |
| CPU used (cores), mean | 1.409 | 1.4 | -0.7% | -0.02557 to +0.006393 | no |
| Omni's own CPU (cores), mean | 0 | 0.01132 | +0.0113 (native is 0) | +0.01028 to +0.01236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.411 | +0.1% | -0.01363 to +0.01708 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.5 | 424.7 | -10.5% | -99.65 to +0.001741 | no |
| HPA replicas, mean | 2.053 | 2.304 | +12.2% | -0.08268 to +0.5843 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | +0.0214 to +1.379 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.05 | 40.84 | -0.5% | -0.5667 to +0.1437 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 782 | 777.6 | -0.6% | -9.637 to +0.8369 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.615 | -23.1% | -2.637 to -0.1338 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3292 | 0.06667 | -79.7% | -0.6215 to +0.09654 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 0.3 | -83.3% | -3.666 to +0.6657 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.93 | 85.03 | -5.4% | -10.18 to +0.3792 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.124 | -14.6% | -1.646 to -0.1062 | yes: GAIN |
| node-hours | 2.519 | 2.148 | -14.7% | -0.6912 to -0.05033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.1 | -0.4% | -2.26 to +0.3296 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 243.6 | -10.5% | -53.28 to -3.768 | yes: GAIN |
| response time (ms), mean | 313.4 | 321.9 | +2.7% | -7.62 to +24.73 | no |
| response time (ms), 95th percentile | 1100 | 1226 | +11.4% | -15.57 to +267.3 | no |
| response time (ms), 99th percentile | 1622 | 1925 | +18.6% | -16.12 to +621.2 | no |
| time over the response line (% of samples) | 13.36 | 12.38 | -7.3% | -2.028 to +0.07818 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.6 | -5.0% | -1.528 to +0.7285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.6 | +10.6 (native is 0) | +8.657 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.75 | 13.53 | +25.8% | +0.2907 to +5.259 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0588 | 0.06666 | +13.4% | +0.001259 to +0.01448 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.364 | -3.4% | -0.11 to +0.01489 | no |
| Omni's own CPU (cores), mean | 0 | 0.01246 | +0.0125 (native is 0) | +0.01122 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.376 | -2.5% | -0.09734 to +0.02718 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.7 | 435.5 | -7.9% | -68.1 to -6.271 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.203 | +5.5% | -0.09124 to +0.3198 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.05776 to +1.458 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.55 (native is 0) | +0.004977 to +1.095 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.23 | 41.69 | +3.6% | +1.038 to +1.878 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.6 | 783.6 | +0.9% | +0.2898 to +13.71 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.435 | -26.1% | -2.913 to -0.2169 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2167 | +108.0% | -0.01399 to +0.239 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | -0.99 to +1.19 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.23 | 92.71 | +10.1% | -0.1064 to +17.07 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*