# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.92 | 11.31 |
| node-hours | 5.028 | 5.026 | 4.575 | 4.746 |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 527.2 | 525.8 | 528.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 527.2 | 492 | 506.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 576 | 939.5 | 614.6 | 1096 |
| response time (ms), 95th percentile | 2346 | 3982 | 2851 | 4543 |
| response time (ms), 99th percentile | 3468 | 5453 | 4127 | 6070 |
| time over the response line (% of samples) | 22.98 | 29.32 | 24.14 | 33.2 |
| failed requests (%) | 0 | 0.1034 | 0 | 0.2436 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 14.3 | 12.6 | 15.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 171.2 | 157.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 35.71 | 14.17 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 19.9 | 18.79 | 24.99 |
| utilisation (used / allocatable) | 0.03367 | 0.03713 | 0.03901 | 0.03971 |
| CPU used (cores), mean | 1.616 | 1.782 | 1.683 | 1.806 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03856 | 0.04111 |
| CPU used with Omni's own (cores), mean | 1.616 | 1.782 | 1.722 | 1.847 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.9 | 733.1 | 701.6 | 680.8 |
| HPA replicas, mean | 4.105 | 3.975 | 5.095 | 4.906 |
| pods started | 0.2 | 0.3 | 3.2 | 3.4 |
| pod start wait, total (s) | 0.6 | 0.5 | 7.4 | 8.3 |
| pod start wait, mean (s) | 0.6 | 0.35 | 2.081 | 2.035 |
| host CPU busy, the real machine under kind (%) | 49.8 | 58.28 | 54.36 | 63.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 851.8 | 1002 | 890.2 | 1050 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.41 | 10.83 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 7.117 | 0.06667 | 16.25 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 24.1 | 0.6 | 86.9 |
| queue: job turnaround, submitted to done, mean (s) | 162.6 | 273.8 | 191.2 | 334.1 |
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
| worker nodes in service, mean | 12 | 11.31 | -5.8% | -1.728 to +0.3456 | no |
| node-hours | 5.026 | 4.746 | -5.6% | -0.711 to +0.1495 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 528.7 | +0.3% | -0.3995 to +3.485 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 506.9 | -3.8% | -52.52 to +11.94 | no |
| response time (ms), mean | 939.5 | 1096 | +16.7% | +17.83 to +296.1 | yes: LOSS |
| response time (ms), 95th percentile | 3982 | 4543 | +14.1% | +72.9 to +1047 | yes: LOSS |
| response time (ms), 99th percentile | 5453 | 6070 | +11.3% | -189.3 to +1425 | no |
| time over the response line (% of samples) | 29.32 | 33.2 | +13.2% | -0.06052 to +7.82 | no |
| failed requests (%) | 0.1034 | 0.2436 | +135.5% | -0.1246 to +0.405 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 15.4 | +7.7% | +0.3887 to +1.811 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 157.5 | +158 (native is 0) | +116.8 to +198.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.9 | 24.99 | +25.6% | +0.1983 to +9.978 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03713 | 0.03971 | +6.9% | -0.000549 to +0.005708 | no |
| CPU used (cores), mean | 1.782 | 1.806 | +1.3% | -0.03014 to +0.07716 | no |
| Omni's own CPU (cores), mean | 0 | 0.04111 | +0.0411 (native is 0) | +0.03653 to +0.04569 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.782 | 1.847 | +3.6% | +0.01234 to +0.1169 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.1 | 680.8 | -7.1% | -114.5 to +9.913 | no |
| HPA replicas, mean | 3.975 | 4.906 | +23.4% | +0.4863 to +1.376 | yes: power given |
| pods started | 0.3 | 3.4 | +1033.3% | +1.179 to +5.021 | yes: power given |
| pod start wait, total (s) | 0.5 | 8.3 | +1560.0% | +3.406 to +12.19 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 2.035 | +481.4% | +0.5154 to +2.854 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.28 | 63.37 | +8.7% | +3.574 to +6.601 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1002 | 1050 | +4.8% | +18.62 to +78.18 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.83 | -9.7% | -2.941 to +0.6017 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.117 | 16.25 | +128.3% | -5.637 to +23.9 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 24.1 | 86.9 | +260.6% | -31.15 to +156.7 | no |
| queue: job turnaround, submitted to done, mean (s) | 273.8 | 334.1 | +22.0% | +20.44 to +100.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -1.652e-15 to +4.849e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.028 | 5.026 | -0.0% | -0.01435 to +0.01101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 527.2 | +0.4% | +0.7146 to +3.703 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 527.2 | +0.4% | +0.7146 to +3.703 | yes: power given |
| response time (ms), mean | 576 | 939.5 | +63.1% | +187.9 to +539.1 | yes: LOSS |
| response time (ms), 95th percentile | 2346 | 3982 | +69.8% | +874 to +2399 | yes: LOSS |
| response time (ms), 99th percentile | 3468 | 5453 | +57.2% | +1017 to +2951 | yes: LOSS |
| time over the response line (% of samples) | 22.98 | 29.32 | +27.6% | +3.827 to +8.849 | yes: LOSS |
| failed requests (%) | 0 | 0.1034 | +0.103 (native is 0) | -0.0207 to +0.2276 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 14.3 | +28.8% | +1.818 to +4.582 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 19.9 | +32.4% | +1.551 to +8.182 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03367 | 0.03713 | +10.3% | +0.002147 to +0.004772 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.782 | +10.3% | +0.1031 to +0.229 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.616 | 1.782 | +10.3% | +0.1031 to +0.229 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.9 | 733.1 | -7.9% | -81.48 to -44.13 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.105 | 3.975 | -3.2% | -0.2628 to +0.002693 | no |
| pods started | 0.2 | 0.3 | +50.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.6 | 0.5 | -16.7% | -1.468 to +1.268 | no |
| pod start wait, mean (s) | 0.6 | 0.35 | -41.7% | -1.457 to +0.957 | no |
| host CPU busy, the real machine under kind (%) | 49.8 | 58.28 | +17.0% | +6.016 to +10.95 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 851.8 | 1002 | +17.6% | +78.92 to +221.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 7.117 | +8440.0% | +1.307 to +12.76 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 24.1 | +3916.7% | -12.09 to +59.09 | no |
| queue: job turnaround, submitted to done, mean (s) | 162.6 | 273.8 | +68.5% | +58.8 to +163.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | -9.0% | -2.659 to +0.5029 | no |
| node-hours | 5.028 | 4.575 | -9.0% | -1.114 to +0.2074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 525.8 | +0.2% | -1.104 to +2.788 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 492 | -6.3% | -82.74 to +16.74 | no |
| response time (ms), mean | 576 | 614.6 | +6.7% | -1.771 to +79.03 | no |
| response time (ms), 95th percentile | 2346 | 2851 | +21.5% | +209.3 to +801 | yes: LOSS |
| response time (ms), 99th percentile | 3468 | 4127 | +19.0% | +267.3 to +1051 | yes: LOSS |
| time over the response line (% of samples) | 22.98 | 24.14 | +5.0% | -0.2581 to +2.578 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 12.6 | +13.5% | +0.2726 to +2.727 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 171.2 | +171 (native is 0) | +118 to +224.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 18.79 | +25.0% | +0.7693 to +6.741 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03367 | 0.03901 | +15.9% | +0.0001276 to +0.01056 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.683 | +4.2% | +0.02612 to +0.1083 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03856 | +0.0386 (native is 0) | +0.03459 to +0.04253 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.722 | +6.5% | +0.06171 to +0.1499 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.9 | 701.6 | -11.8% | -180.8 to -7.754 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.105 | 5.095 | +24.1% | +0.4706 to +1.509 | yes: power given |
| pods started | 0.2 | 3.2 | +1500.0% | +1.184 to +4.816 | yes: power given |
| pod start wait, total (s) | 0.6 | 7.4 | +1133.3% | +1.06 to +12.54 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.081 | +246.8% | +0.1605 to +2.801 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.8 | 54.36 | +9.2% | +3.418 to +5.712 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 851.8 | 890.2 | +4.5% | +17.27 to +59.53 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.41 | -13.3% | -3.888 to +0.7003 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.06667 | -20.0% | -0.06154 to +0.02821 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 162.6 | 191.2 | +17.6% | +12.36 to +45.02 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.92 | -9.0% | -2.659 to +0.5029 | no |
| node-hours | 5.026 | 4.575 | -9.0% | -1.116 to +0.2123 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 525.8 | -0.3% | -3.594 to +0.8595 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 492 | -6.7% | -84.68 to +14.26 | no |
| response time (ms), mean | 939.5 | 614.6 | -34.6% | -490 to -159.8 | yes: GAIN |
| response time (ms), 95th percentile | 3982 | 2851 | -28.4% | -1778 to -485.2 | yes: GAIN |
| response time (ms), 99th percentile | 5453 | 4127 | -24.3% | -2143 to -507.3 | yes: GAIN |
| time over the response line (% of samples) | 29.32 | 24.14 | -17.7% | -7.877 to -2.478 | yes: GAIN |
| failed requests (%) | 0.1034 | 0 | -100.0% | -0.2276 to +0.0207 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 12.6 | -11.9% | -2.714 to -0.6856 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 171.2 | +171 (native is 0) | +118 to +224.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.9 | 18.79 | -5.6% | -3.386 to +1.163 | no |
| utilisation (used / allocatable) | 0.03713 | 0.03901 | +5.1% | -0.004411 to +0.00818 | no |
| CPU used (cores), mean | 1.782 | 1.683 | -5.5% | -0.1531 to -0.04454 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03856 | +0.0386 (native is 0) | +0.03459 to +0.04253 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.782 | 1.722 | -3.4% | -0.113 to -0.00754 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.1 | 701.6 | -4.3% | -129.1 to +66.16 | no |
| HPA replicas, mean | 3.975 | 5.095 | +28.2% | +0.5951 to +1.645 | yes: power given |
| pods started | 0.3 | 3.2 | +966.7% | +0.9791 to +4.821 | yes: power given |
| pod start wait, total (s) | 0.5 | 7.4 | +1380.0% | +1.283 to +12.52 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 2.081 | +494.6% | +0.9442 to +2.518 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.28 | 54.36 | -6.7% | -5.909 to -1.925 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1002 | 890.2 | -11.1% | -167.7 to -55.52 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.41 | -13.3% | -3.888 to +0.7003 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.117 | 0.06667 | -99.1% | -12.75 to -1.345 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 24.1 | 0.6 | -97.5% | -59.09 to +12.09 | no |
| queue: job turnaround, submitted to done, mean (s) | 273.8 | 191.2 | -30.2% | -127.7 to -37.49 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.31 | -5.8% | -1.728 to +0.3456 | no |
| node-hours | 5.028 | 4.746 | -5.6% | -0.711 to +0.1462 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 528.7 | +0.7% | +1.806 to +5.698 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 506.9 | -3.4% | -50.66 to +14.5 | no |
| response time (ms), mean | 576 | 1096 | +90.4% | +279 to +761.9 | yes: LOSS |
| response time (ms), 95th percentile | 2346 | 4543 | +93.7% | +1263 to +3131 | yes: LOSS |
| response time (ms), 99th percentile | 3468 | 6070 | +75.0% | +1490 to +3714 | yes: LOSS |
| time over the response line (% of samples) | 22.98 | 33.2 | +44.5% | +5.234 to +15.2 | yes: LOSS |
| failed requests (%) | 0 | 0.2436 | +0.244 (native is 0) | -0.02502 to +0.5123 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 15.4 | +38.7% | +2.79 to +5.81 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 157.5 | +158 (native is 0) | +116.8 to +198.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 24.99 | +66.2% | +2.529 to +17.38 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03367 | 0.03971 | +17.9% | +0.003814 to +0.008263 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.806 | +11.7% | +0.1202 to +0.2589 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04111 | +0.0411 (native is 0) | +0.03653 to +0.04569 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.847 | +14.3% | +0.1589 to +0.3025 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.9 | 680.8 | -14.5% | -169.1 to -61.15 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.105 | 4.906 | +19.5% | +0.3513 to +1.251 | yes: power given |
| pods started | 0.2 | 3.4 | +1600.0% | +1.359 to +5.041 | yes: power given |
| pod start wait, total (s) | 0.6 | 8.3 | +1283.3% | +3.163 to +12.24 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.035 | +239.1% | -0.101 to +2.971 | no |
| host CPU busy, the real machine under kind (%) | 49.8 | 63.37 | +27.2% | +10.51 to +16.63 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 851.8 | 1050 | +23.3% | +115.9 to +280.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.83 | -9.7% | -2.941 to +0.6017 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 16.25 | +19395.0% | +1.177 to +31.15 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 86.9 | +14383.3% | +2.305 to +170.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 162.6 | 334.1 | +105.5% | +99.07 to +244.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*