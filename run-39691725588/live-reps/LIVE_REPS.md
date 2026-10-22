# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.13 | 7.007 |
| node-hours | 5.025 | 5.026 | 4.24 | 2.933 |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.3 | 523.9 | 504.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 504.3 | 465.1 | 347.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 445.8 | 110.2 | 437.3 | 64.72 |
| response time (ms), 95th percentile | 1717 | 152.6 | 1844 | 83.95 |
| response time (ms), 99th percentile | 2375 | 174.2 | 2583 | 115.3 |
| time over the response line (% of samples) | 15.74 | 0 | 16.15 | 0 |
| failed requests (%) | 0 | 0 | 0.007273 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | 9.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 94.8 | 25.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.39 | 0.02667 | 13.5 | 0.025 |
| utilisation (used / allocatable) | 0.03265 | 0.005626 | 0.03919 | 0.008181 |
| CPU used (cores), mean | 1.567 | 0.27 | 1.566 | 0.2306 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01216 | 0.00823 |
| CPU used with Omni's own (cores), mean | 1.567 | 0.27 | 1.578 | 0.2388 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 820.3 | 4578 | 718 | 3720 |
| HPA replicas, mean | 3.951 | 4.149 | 4.487 | 4.274 |
| pods started | 0.6 | 0.8 | 1 | 1.2 |
| pod start wait, total (s) | 1.2 | 1.3 | 1.7 | 2.2 |
| pod start wait, mean (s) | 1 | 0.7 | 1.15 | 1.342 |
| host CPU busy, the real machine under kind (%) | 47.36 | 13.11 | 49.21 | 14.18 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 821.9 | 1505 | 834 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.848 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1159 | 0.06667 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1475 | 0.4 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 129.2 | 1159 | 138 | 1158 |
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
| worker nodes in service, mean | 12 | 7.007 | -41.6% | -5.286 to -4.7 | yes: GAIN |
| node-hours | 5.026 | 2.933 | -41.6% | -2.216 to -1.97 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.3 | 504.1 | -0.0% | -1.288 to +0.9544 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.3 | 347.4 | -31.1% | -166.2 to -147.7 | yes: GAIN |
| response time (ms), mean | 110.2 | 64.72 | -41.3% | -57.83 to -33.16 | yes: GAIN |
| response time (ms), 95th percentile | 152.6 | 83.95 | -45.0% | -86.89 to -50.47 | yes: GAIN |
| response time (ms), 99th percentile | 174.2 | 115.3 | -33.8% | -75.8 to -41.93 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 | +25.1 (native is 0) | +23.54 to +26.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.025 | -6.3% | -0.005437 to +0.002103 | no |
| utilisation (used / allocatable) | 0.005626 | 0.008181 | +45.4% | +0.002182 to +0.002928 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.27 | 0.2306 | -14.6% | -0.0453 to -0.03363 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00823 | +0.00823 (native is 0) | +0.007165 to +0.009295 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.27 | 0.2388 | -11.6% | -0.03739 to -0.02509 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4578 | 3720 | -18.7% | -1017 to -698.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.149 | 4.274 | +3.0% | -0.1165 to +0.366 | no |
| pods started | 0.8 | 1.2 | +50.0% | -0.9985 to +1.798 | no |
| pod start wait, total (s) | 1.3 | 2.2 | +69.2% | -1.245 to +3.045 | no |
| pod start wait, mean (s) | 0.7 | 1.342 | +91.7% | -0.3203 to +1.604 | no |
| host CPU busy, the real machine under kind (%) | 13.11 | 14.18 | +8.2% | +0.7323 to +1.405 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 1505 | -0.0% | -3.029 to +2.829 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1158 | -0.0% | -3.254 to +2.746 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1474 | -0.0% | -3.305 to +2.505 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1158 | -0.0% | -3.254 to +2.746 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -6.084e-15 to -6.664e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.025 | 5.026 | +0.0% | -0.01286 to +0.01486 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.3 | -3.8% | -22.77 to -16.77 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 504.3 | -3.8% | -22.77 to -16.77 | yes: GAIN |
| response time (ms), mean | 445.8 | 110.2 | -75.3% | -609.8 to -61.35 | yes: GAIN |
| response time (ms), 95th percentile | 1717 | 152.6 | -91.1% | -2877 to -251.1 | yes: GAIN |
| response time (ms), 99th percentile | 2375 | 174.2 | -92.7% | -3944 to -457 | yes: GAIN |
| time over the response line (% of samples) | 15.74 | 0 | -100.0% | -27.94 to -3.546 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | -100.0% | -13.86 to -2.738 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.39 | 0.02667 | -99.8% | -16.74 to -5.976 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03265 | 0.005626 | -82.8% | -0.03063 to -0.02343 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.567 | 0.27 | -82.8% | -1.47 to -1.124 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.567 | 0.27 | -82.8% | -1.47 to -1.124 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 820.3 | 4578 | +458.1% | +3280 to +4235 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.951 | 4.149 | +5.0% | +0.03237 to +0.3628 | yes: power given |
| pods started | 0.6 | 0.8 | +33.3% | -0.8556 to +1.256 | no |
| pod start wait, total (s) | 1.2 | 1.3 | +8.3% | -1.601 to +1.801 | no |
| pod start wait, mean (s) | 1 | 0.7 | -30.0% | -1.41 to +0.8096 | no |
| host CPU busy, the real machine under kind (%) | 47.36 | 13.11 | -72.3% | -39.14 to -29.36 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 821.9 | 1505 | +83.1% | +591.1 to +775.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1159 | +1544850.0% | +1155 to +1162 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1475 | +294860.0% | +1471 to +1478 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 129.2 | 1159 | +796.6% | +938.4 to +1121 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.13 | -15.6% | -3.517 to -0.2249 | yes: GAIN |
| node-hours | 5.025 | 4.24 | -15.6% | -1.471 to -0.09913 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 523.9 | -0.0% | -1.795 to +1.434 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 465.1 | -11.3% | -110.8 to -7.143 | yes: GAIN |
| response time (ms), mean | 445.8 | 437.3 | -1.9% | -26.25 to +9.358 | no |
| response time (ms), 95th percentile | 1717 | 1844 | +7.4% | -4.899 to +258.6 | no |
| response time (ms), 99th percentile | 2375 | 2583 | +8.8% | -32.14 to +447.9 | no |
| time over the response line (% of samples) | 15.74 | 16.15 | +2.6% | -0.6664 to +1.469 | no |
| failed requests (%) | 0 | 0.007273 | +0.00727 (native is 0) | -0.009178 to +0.02372 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.3 | +12.0% | -0.6171 to +2.617 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.8 | +94.8 (native is 0) | +53.07 to +136.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.39 | 13.5 | +18.5% | +0.2715 to +3.952 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03265 | 0.03919 | +20.0% | +0.001218 to +0.01185 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.566 | -0.1% | -0.04431 to +0.04052 | no |
| Omni's own CPU (cores), mean | 0 | 0.01216 | +0.0122 (native is 0) | +0.01133 to +0.01299 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.578 | +0.7% | -0.0323 to +0.05284 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 820.3 | 718 | -12.5% | -182.9 to -21.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.951 | 4.487 | +13.6% | +0.1633 to +0.9086 | yes: power given |
| pods started | 0.6 | 1 | +66.7% | -0.6228 to +1.423 | no |
| pod start wait, total (s) | 1.2 | 1.7 | +41.7% | -1.473 to +2.473 | no |
| pod start wait, mean (s) | 1 | 1.15 | +15.0% | -1.32 to +1.62 | no |
| host CPU busy, the real machine under kind (%) | 47.36 | 49.21 | +3.9% | +1.096 to +2.604 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 821.9 | 834 | +1.5% | +0.1142 to +24.09 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.848 | -26.3% | -5.852 to -0.4519 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.06667 | -11.1% | -0.04757 to +0.03091 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.2 | 138 | +6.8% | +0.2703 to +17.28 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.13 | -15.6% | -3.517 to -0.2249 | yes: GAIN |
| node-hours | 5.026 | 4.24 | -15.6% | -1.478 to -0.09389 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.3 | 523.9 | +3.9% | +16.17 to +23.01 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.3 | 465.1 | -7.8% | -93.66 to +15.29 | no |
| response time (ms), mean | 110.2 | 437.3 | +296.8% | +42.55 to +611.7 | yes: LOSS |
| response time (ms), 95th percentile | 152.6 | 1844 | +1107.8% | +305.9 to +3076 | yes: LOSS |
| response time (ms), 99th percentile | 174.2 | 2583 | +1382.6% | +544.3 to +4273 | yes: LOSS |
| time over the response line (% of samples) | 0 | 16.15 | +16.1 (native is 0) | +4.084 to +28.21 | yes: LOSS |
| failed requests (%) | 0 | 0.007273 | +0.00727 (native is 0) | -0.009178 to +0.02372 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.3 | +9.3 (native is 0) | +3.698 to +14.9 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.8 | +94.8 (native is 0) | +53.07 to +136.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 13.5 | +50512.5% | +6.745 to +20.19 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005626 | 0.03919 | +596.6% | +0.02978 to +0.03735 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.27 | 1.566 | +479.7% | +1.091 to +1.5 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01216 | +0.0122 (native is 0) | +0.01133 to +0.01299 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.27 | 1.578 | +484.2% | +1.103 to +1.512 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4578 | 718 | -84.3% | -4414 to -3306 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.149 | 4.487 | +8.2% | -0.01205 to +0.6888 | no |
| pods started | 0.8 | 1 | +25.0% | -0.9583 to +1.358 | no |
| pod start wait, total (s) | 1.3 | 1.7 | +30.8% | -1.359 to +2.159 | no |
| pod start wait, mean (s) | 0.7 | 1.15 | +64.3% | -0.6713 to +1.571 | no |
| host CPU busy, the real machine under kind (%) | 13.11 | 49.21 | +275.3% | +30.68 to +41.52 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 834 | -44.6% | -774.2 to -568 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.06667 | -100.0% | -1162 to -1155 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.4 | -100.0% | -1478 to -1471 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 138 | -88.1% | -1119 to -922.7 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.007 | -41.6% | -5.286 to -4.7 | yes: GAIN |
| node-hours | 5.025 | 2.933 | -41.6% | -2.217 to -1.966 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.1 | -3.8% | -23.22 to -16.66 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 347.4 | -33.7% | -184 to -169.4 | yes: GAIN |
| response time (ms), mean | 445.8 | 64.72 | -85.5% | -665.3 to -96.8 | yes: GAIN |
| response time (ms), 95th percentile | 1717 | 83.95 | -95.1% | -2958 to -307.9 | yes: GAIN |
| response time (ms), 99th percentile | 2375 | 115.3 | -95.1% | -4015 to -503.7 | yes: GAIN |
| time over the response line (% of samples) | 15.74 | 0 | -100.0% | -27.94 to -3.546 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | -100.0% | -13.86 to -2.738 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 | +25.1 (native is 0) | +23.54 to +26.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.39 | 0.025 | -99.8% | -16.74 to -5.977 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03265 | 0.008181 | -74.9% | -0.02794 to -0.02101 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.567 | 0.2306 | -85.3% | -1.509 to -1.165 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00823 | +0.00823 (native is 0) | +0.007165 to +0.009295 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 0.2388 | -84.8% | -1.5 to -1.158 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 820.3 | 3720 | +353.5% | +2501 to +3299 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.951 | 4.274 | +8.2% | +0.0904 to +0.5543 | yes: power given |
| pods started | 0.6 | 1.2 | +100.0% | -0.5285 to +1.728 | no |
| pod start wait, total (s) | 1.2 | 2.2 | +83.3% | -1.159 to +3.159 | no |
| pod start wait, mean (s) | 1 | 1.342 | +34.2% | -1 to +1.684 | no |
| host CPU busy, the real machine under kind (%) | 47.36 | 14.18 | -70.1% | -37.95 to -28.41 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 821.9 | 1505 | +83.1% | +590.2 to +776 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1158 | +1544511.1% | +1155 to +1162 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1474 | +294780.0% | +1470 to +1477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 129.2 | 1158 | +796.4% | +937.4 to +1121 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*