# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.12 | 10.66 |
| node-hours | 5.028 | 5.024 | 4.244 | 4.468 |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 523.9 | 524.2 | 525.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 523.9 | 465.1 | 483.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 405.3 | 596.3 | 416.8 | 701 |
| response time (ms), 95th percentile | 1515 | 2298 | 1821 | 2887 |
| response time (ms), 99th percentile | 2168 | 3212 | 2630 | 3964 |
| time over the response line (% of samples) | 13.98 | 18.97 | 15.73 | 26.3 |
| failed requests (%) | 0 | 0.06116 | 0.005848 | 0.04 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 10.7 | 9.8 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 210.5 | 175.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 38.33 | 25.28 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 13.52 | 11.12 | 18.81 |
| utilisation (used / allocatable) | 0.03095 | 0.03268 | 0.03812 | 0.03837 |
| CPU used (cores), mean | 1.486 | 1.569 | 1.514 | 1.635 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03594 | 0.03663 |
| CPU used with Omni's own (cores), mean | 1.486 | 1.569 | 1.55 | 1.672 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 871.3 | 833.3 | 740.7 | 719.6 |
| HPA replicas, mean | 4.182 | 4.084 | 5.068 | 4.967 |
| pods started | 0.5 | 0.1 | 2.5 | 3.8 |
| pod start wait, total (s) | 0.9 | 0.2 | 6.6 | 8.3 |
| pod start wait, mean (s) | 0.5 | 0.2 | 1.439 | 1.726 |
| host CPU busy, the real machine under kind (%) | 45.64 | 51.58 | 49.25 | 56.84 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806.4 | 884 | 824.7 | 935.5 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.155 | 10.09 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 3.046 | 0.0625 | 13.57 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 8 | 0.5 | 100.9 |
| queue: job turnaround, submitted to done, mean (s) | 115.8 | 175.2 | 131.2 | 223.4 |
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
| worker nodes in service, mean | 12 | 10.66 | -11.1% | -2.874 to +0.1995 | no |
| node-hours | 5.024 | 4.468 | -11.1% | -1.199 to +0.08701 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 525.7 | +0.3% | +0.6135 to +3.014 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 483.6 | -7.7% | -88.83 to +8.315 | no |
| response time (ms), mean | 596.3 | 701 | +17.5% | +28.03 to +181.3 | yes: LOSS |
| response time (ms), 95th percentile | 2298 | 2887 | +25.6% | +245.8 to +932.6 | yes: LOSS |
| response time (ms), 99th percentile | 3212 | 3964 | +23.4% | +287.9 to +1216 | yes: LOSS |
| time over the response line (% of samples) | 18.97 | 26.3 | +38.7% | +0.9412 to +13.72 | yes: LOSS |
| failed requests (%) | 0.06116 | 0.04 | -34.6% | -0.1221 to +0.07973 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 12.2 | +14.0% | +0.4744 to +2.526 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 175.7 | +176 (native is 0) | +116.5 to +234.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.52 | 18.81 | +39.2% | -1.935 to +12.52 | no |
| utilisation (used / allocatable) | 0.03268 | 0.03837 | +17.4% | +0.0015 to +0.009887 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.569 | 1.635 | +4.2% | -0.01031 to +0.1433 | no |
| Omni's own CPU (cores), mean | 0 | 0.03663 | +0.0366 (native is 0) | +0.0318 to +0.04146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.569 | 1.672 | +6.6% | +0.02751 to +0.1788 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 719.6 | -13.6% | -193.8 to -33.63 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.084 | 4.967 | +21.6% | +0.4435 to +1.323 | yes: power given |
| pods started | 0.1 | 3.8 | +3700.0% | +1.914 to +5.486 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.3 | +4050.0% | +3.232 to +12.97 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.726 | +762.9% | +0.8586 to +2.193 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.58 | 56.84 | +10.2% | +3.946 to +6.567 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 884 | 935.5 | +5.8% | +24.09 to +78.91 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.09 | -15.9% | -4.074 to +0.2606 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.046 | 13.57 | +345.7% | -2.998 to +24.06 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8 | 100.9 | +1161.2% | -21.07 to +206.9 | no |
| queue: job turnaround, submitted to done, mean (s) | 175.2 | 223.4 | +27.5% | +18.91 to +77.49 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -2.992e-15 to +4.413e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.028 | 5.024 | -0.1% | -0.01554 to +0.008876 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 523.9 | +0.2% | -0.4284 to +2.148 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 523.9 | +0.2% | -0.4284 to +2.148 | no |
| response time (ms), mean | 405.3 | 596.3 | +47.1% | +42.71 to +339.3 | yes: LOSS |
| response time (ms), 95th percentile | 1515 | 2298 | +51.7% | +174.9 to +1391 | yes: LOSS |
| response time (ms), 99th percentile | 2168 | 3212 | +48.2% | +202.3 to +1886 | yes: LOSS |
| time over the response line (% of samples) | 13.98 | 18.97 | +35.7% | +2.239 to +7.743 | yes: LOSS |
| failed requests (%) | 0 | 0.06116 | +0.0612 (native is 0) | -0.02727 to +0.1496 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 10.7 | +50.7% | +0.9621 to +6.238 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 13.52 | +34.2% | -1.467 to +8.353 | no |
| utilisation (used / allocatable) | 0.03095 | 0.03268 | +5.6% | +0.0005166 to +0.002941 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.569 | +5.6% | +0.0248 to +0.1412 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.486 | 1.569 | +5.6% | +0.0248 to +0.1412 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 871.3 | 833.3 | -4.4% | -60.73 to -15.21 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.182 | 4.084 | -2.3% | -0.4041 to +0.2076 | no |
| pods started | 0.5 | 0.1 | -80.0% | -1.091 to +0.2911 | no |
| pod start wait, total (s) | 0.9 | 0.2 | -77.8% | -2.092 to +0.6924 | no |
| pod start wait, mean (s) | 0.5 | 0.2 | -60.0% | -1.146 to +0.5464 | no |
| host CPU busy, the real machine under kind (%) | 45.64 | 51.58 | +13.0% | +3.839 to +8.038 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.4 | 884 | +9.6% | +16.19 to +139 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 3.046 | +4468.8% | -1.272 to +7.23 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 8 | +1233.3% | -7.861 to +22.66 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.8 | 175.2 | +51.4% | +13.72 to +105.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.12 | -15.6% | -3.704 to -0.04879 | yes: GAIN |
| node-hours | 5.028 | 4.244 | -15.6% | -1.546 to -0.02106 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 524.2 | +0.2% | -0.548 to +2.964 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 465.1 | -11.1% | -115.1 to -0.64 | yes: GAIN |
| response time (ms), mean | 405.3 | 416.8 | +2.8% | -8.973 to +31.99 | no |
| response time (ms), 95th percentile | 1515 | 1821 | +20.2% | +122.5 to +489 | yes: LOSS |
| response time (ms), 99th percentile | 2168 | 2630 | +21.3% | +164.8 to +760 | yes: LOSS |
| time over the response line (% of samples) | 13.98 | 15.73 | +12.5% | -0.9007 to +4.409 | no |
| failed requests (%) | 0 | 0.005848 | +0.00585 (native is 0) | -0.00738 to +0.01908 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 9.8 | +38.0% | -0.01963 to +5.42 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 210.5 | +210 (native is 0) | +151.7 to +269.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 11.12 | +10.3% | -1.207 to +3.29 | no |
| utilisation (used / allocatable) | 0.03095 | 0.03812 | +23.2% | +0.001215 to +0.01312 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.514 | +1.9% | -0.01911 to +0.07594 | no |
| Omni's own CPU (cores), mean | 0 | 0.03594 | +0.0359 (native is 0) | +0.03223 to +0.03965 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 1.55 | +4.3% | +0.01494 to +0.1138 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 871.3 | 740.7 | -15.0% | -235.3 to -25.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.182 | 5.068 | +21.2% | +0.07179 to +1.701 | yes: power given |
| pods started | 0.5 | 2.5 | +400.0% | -0.07863 to +4.079 | no |
| pod start wait, total (s) | 0.9 | 6.6 | +633.3% | -0.6448 to +12.04 | no |
| pod start wait, mean (s) | 0.5 | 1.439 | +187.8% | -0.15 to +2.028 | no |
| host CPU busy, the real machine under kind (%) | 45.64 | 49.25 | +7.9% | +2.766 to +4.46 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.4 | 824.7 | +2.3% | +3.644 to +32.96 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.155 | -23.7% | -5.484 to -0.2059 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0625 | -6.2% | -0.05171 to +0.04338 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.8 | 131.2 | +13.3% | +5.892 to +24.95 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.12 | -15.6% | -3.704 to -0.04879 | yes: GAIN |
| node-hours | 5.024 | 4.244 | -15.5% | -1.547 to -0.01367 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.2 | +0.1% | -1.609 to +2.306 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 465.1 | -11.2% | -115.9 to -1.556 | yes: GAIN |
| response time (ms), mean | 596.3 | 416.8 | -30.1% | -313 to -46.03 | yes: GAIN |
| response time (ms), 95th percentile | 2298 | 1821 | -20.8% | -943.4 to -10.89 | yes: GAIN |
| response time (ms), 99th percentile | 3212 | 2630 | -18.1% | -1177 to +13.54 | no |
| time over the response line (% of samples) | 18.97 | 15.73 | -17.1% | -6.381 to -0.09276 | yes: GAIN |
| failed requests (%) | 0.06116 | 0.005848 | -90.4% | -0.147 to +0.03634 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 9.8 | -8.4% | -1.611 to -0.1887 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 210.5 | +210 (native is 0) | +151.7 to +269.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.52 | 11.12 | -17.8% | -7.424 to +2.621 | no |
| utilisation (used / allocatable) | 0.03268 | 0.03812 | +16.6% | -0.001082 to +0.01196 | no |
| CPU used (cores), mean | 1.569 | 1.514 | -3.5% | -0.1026 to -0.006509 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03594 | +0.0359 (native is 0) | +0.03223 to +0.03965 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.569 | 1.55 | -1.2% | -0.06573 to +0.02847 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 740.7 | -11.1% | -197.8 to +12.66 | no |
| HPA replicas, mean | 4.084 | 5.068 | +24.1% | +0.3599 to +1.609 | yes: power given |
| pods started | 0.1 | 2.5 | +2400.0% | +0.5469 to +4.253 | yes: power given |
| pod start wait, total (s) | 0.2 | 6.6 | +3200.0% | +0.4229 to +12.38 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.439 | +619.6% | +0.3282 to +2.15 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.58 | 49.25 | -4.5% | -3.773 to -0.8784 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 884 | 824.7 | -6.7% | -106.5 to -12.05 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.155 | -23.7% | -5.484 to -0.2059 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.046 | 0.0625 | -97.9% | -7.225 to +1.258 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8 | 0.5 | -93.8% | -22.73 to +7.731 | no |
| queue: job turnaround, submitted to done, mean (s) | 175.2 | 131.2 | -25.1% | -81.22 to -6.822 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.66 | -11.1% | -2.874 to +0.1995 | no |
| node-hours | 5.028 | 4.468 | -11.1% | -1.2 to +0.08107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 525.7 | +0.5% | +1.299 to +4.048 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 483.6 | -7.5% | -88.11 to +9.32 | no |
| response time (ms), mean | 405.3 | 701 | +72.9% | +109 to +482.3 | yes: LOSS |
| response time (ms), 95th percentile | 1515 | 2887 | +90.6% | +586.1 to +2158 | yes: LOSS |
| response time (ms), 99th percentile | 2168 | 3964 | +82.8% | +820.4 to +2771 | yes: LOSS |
| time over the response line (% of samples) | 13.98 | 26.3 | +88.2% | +4.468 to +20.18 | yes: LOSS |
| failed requests (%) | 0 | 0.04 | +0.04 (native is 0) | -0.008747 to +0.08874 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 12.2 | +71.8% | +1.911 to +8.289 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 175.7 | +176 (native is 0) | +116.5 to +234.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 18.81 | +86.7% | +0.9073 to +16.57 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03095 | 0.03837 | +24.0% | +0.003784 to +0.01106 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.635 | +10.1% | +0.07755 to +0.2215 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03663 | +0.0366 (native is 0) | +0.0318 to +0.04146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 1.672 | +12.5% | +0.1121 to +0.2602 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 871.3 | 719.6 | -17.4% | -230.6 to -72.77 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.182 | 4.967 | +18.8% | +0.08594 to +1.484 | yes: power given |
| pods started | 0.5 | 3.8 | +660.0% | +1.452 to +5.148 | yes: power given |
| pod start wait, total (s) | 0.9 | 8.3 | +822.2% | +2.617 to +12.18 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.726 | +245.1% | +0.4917 to +1.96 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.64 | 56.84 | +24.5% | +8.505 to +13.88 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.4 | 935.5 | +16.0% | +51.33 to +206.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.09 | -15.9% | -4.074 to +0.2606 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 13.58 | +20262.5% | -1.036 to +28.05 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 100.9 | +16716.7% | -11.88 to +212.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.8 | 223.4 | +93.0% | +47.63 to +167.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*