# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.94 | 6.61 |
| node-hours | 5.024 | 5.018 | 4.59 | 2.766 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 503.8 | 526 | 504.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 503.8 | 492.7 | 335.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 513.6 | 126.2 | 557.1 | 72.93 |
| response time (ms), 95th percentile | 1993 | 174.7 | 2519 | 93.27 |
| response time (ms), 99th percentile | 2946 | 194.8 | 3683 | 125.6 |
| time over the response line (% of samples) | 19.55 | 0 | 21.59 | 0.007201 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0 | 12.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 205.2 | 33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 34.67 | 92.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.68 | 0 | 14.23 | 0.07833 |
| utilisation (used / allocatable) | 0.03317 | 0.00616 | 0.03778 | 0.009508 |
| CPU used (cores), mean | 1.592 | 0.2957 | 1.641 | 0.2509 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03944 | 0.02136 |
| CPU used with Omni's own (cores), mean | 1.592 | 0.2957 | 1.681 | 0.2723 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.8 | 4162 | 723.3 | 3271 |
| HPA replicas, mean | 4.103 | 4.117 | 5.03 | 4.727 |
| pods started | 0.4 | 0.5 | 2.7 | 1.9 |
| pod start wait, total (s) | 0.7 | 0.6 | 6.5 | 2.7 |
| pod start wait, mean (s) | 0.6 | 0.5 | 1.897 | 1.208 |
| host CPU busy, the real machine under kind (%) | 48.6 | 13.74 | 53.35 | 16.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 836 | 1503 | 869.1 | 1503 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.26 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1156 | 0.1 | 1156 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1472 | 0.7 | 1472 |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 1156 | 173.2 | 1156 |
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
| worker nodes in service, mean | 12 | 6.61 | -44.9% | -5.98 to -4.8 | yes: GAIN |
| node-hours | 5.018 | 2.766 | -44.9% | -2.504 to -2.002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 503.8 | 504.2 | +0.1% | -0.9052 to +1.801 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.8 | 335.1 | -33.5% | -187.7 to -149.7 | yes: GAIN |
| response time (ms), mean | 126.2 | 72.93 | -42.2% | -61.96 to -44.54 | yes: GAIN |
| response time (ms), 95th percentile | 174.7 | 93.27 | -46.6% | -93.06 to -69.76 | yes: GAIN |
| response time (ms), 99th percentile | 194.8 | 125.6 | -35.6% | -80.31 to -58.21 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.007201 | +0.0072 (native is 0) | -0.003658 to +0.01806 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 | +33 (native is 0) | +31.03 to +34.97 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.07833 | +0.0783 (native is 0) | -0.04909 to +0.2058 | no |
| utilisation (used / allocatable) | 0.00616 | 0.009508 | +54.3% | +0.00279 to +0.003905 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2957 | 0.2509 | -15.1% | -0.05459 to -0.03488 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02136 | +0.0214 (native is 0) | +0.01878 to +0.02394 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2957 | 0.2723 | -7.9% | -0.03316 to -0.0136 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4162 | 3271 | -21.4% | -1023 to -758.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.117 | 4.727 | +14.8% | +0.3613 to +0.8585 | yes: power given |
| pods started | 0.5 | 1.9 | +280.0% | +0.1749 to +2.625 | yes: power given |
| pod start wait, total (s) | 0.6 | 2.7 | +350.0% | +0.3989 to +3.801 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.208 | +141.7% | +0.1669 to +1.25 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.74 | 16.02 | +16.6% | +1.711 to +2.851 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 1503 | -0.0% | -4.671 to +4.071 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1156 | -0.0% | -4.491 to +4.116 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 1472 | -0.0% | -4.723 to +4.123 | no |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1156 | -0.0% | -4.491 to +4.116 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -4.991e-15 to +3.728e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.024 | 5.018 | -0.1% | -0.02083 to +0.009499 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 503.8 | -3.9% | -23.55 to -17.31 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 503.8 | -3.9% | -23.55 to -17.31 | yes: GAIN |
| response time (ms), mean | 513.6 | 126.2 | -75.4% | -602.4 to -172.5 | yes: GAIN |
| response time (ms), 95th percentile | 1993 | 174.7 | -91.2% | -2863 to -773.1 | yes: GAIN |
| response time (ms), 99th percentile | 2946 | 194.8 | -93.4% | -4291 to -1211 | yes: GAIN |
| time over the response line (% of samples) | 19.55 | 0 | -100.0% | -31.04 to -8.055 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0 | -100.0% | -15 to -4.803 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.68 | 0 | -100.0% | -17.7 to -7.656 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03317 | 0.00616 | -81.4% | -0.03022 to -0.0238 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.592 | 0.2957 | -81.4% | -1.45 to -1.143 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.592 | 0.2957 | -81.4% | -1.45 to -1.143 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.8 | 4162 | +416.5% | +2956 to +3756 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.103 | 4.117 | +0.3% | -0.1481 to +0.1766 | no |
| pods started | 0.4 | 0.5 | +25.0% | -0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.7 | 0.6 | -14.3% | -1.02 to +0.8204 | no |
| pod start wait, mean (s) | 0.6 | 0.5 | -16.7% | -1.02 to +0.8204 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 13.74 | -71.7% | -39.4 to -30.31 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 836 | 1503 | +79.8% | +597.9 to +736.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1156 | +1541527.8% | +1152 to +1160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1472 | +294380.0% | +1468 to +1476 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 1156 | +693.7% | +939.6 to +1081 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | -8.8% | -2.46 to +0.3449 | no |
| node-hours | 5.024 | 4.59 | -8.6% | -1.016 to +0.1468 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 526 | +0.3% | -0.08305 to +3.722 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 492.7 | -6.0% | -75.19 to +12.16 | no |
| response time (ms), mean | 513.6 | 557.1 | +8.5% | +13.38 to +73.73 | yes: LOSS |
| response time (ms), 95th percentile | 1993 | 2519 | +26.4% | +263.1 to +790 | yes: LOSS |
| response time (ms), 99th percentile | 2946 | 3683 | +25.0% | +354.3 to +1119 | yes: LOSS |
| time over the response line (% of samples) | 19.55 | 21.59 | +10.4% | -0.4276 to +4.511 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 12.3 | +24.2% | +0.05895 to +4.741 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 205.2 | +205 (native is 0) | +132.5 to +277.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.68 | 14.23 | +12.2% | -0.8277 to +3.931 | no |
| utilisation (used / allocatable) | 0.03317 | 0.03778 | +13.9% | +0.0002445 to +0.008984 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.592 | 1.641 | +3.1% | +0.01443 to +0.08354 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03944 | +0.0394 (native is 0) | +0.03661 to +0.04227 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.592 | 1.681 | +5.6% | +0.05201 to +0.1248 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.8 | 723.3 | -10.2% | -156.5 to -8.468 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.103 | 5.03 | +22.6% | +0.5341 to +1.32 | yes: power given |
| pods started | 0.4 | 2.7 | +575.0% | +0.7166 to +3.883 | yes: power given |
| pod start wait, total (s) | 0.7 | 6.5 | +828.6% | +2.003 to +9.597 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.897 | +216.1% | -0.1167 to +2.71 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 53.35 | +9.8% | +4.124 to +5.369 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 836 | 869.1 | +4.0% | +12.78 to +53.42 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.26 | -14.5% | -3.982 to +0.5044 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.1 | +33.3% | -0.03969 to +0.08969 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | -0.3642 to +0.7642 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 173.2 | +18.9% | +12.68 to +42.29 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | -8.8% | -2.46 to +0.3449 | no |
| node-hours | 5.018 | 4.59 | -8.5% | -1.016 to +0.1587 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 503.8 | 526 | +4.4% | +18.83 to +25.66 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.8 | 492.7 | -2.2% | -57.37 to +35.19 | no |
| response time (ms), mean | 126.2 | 557.1 | +341.5% | +192.2 to +669.8 | yes: LOSS |
| response time (ms), 95th percentile | 174.7 | 2519 | +1342.3% | +1085 to +3605 | yes: LOSS |
| response time (ms), 99th percentile | 194.8 | 3683 | +1790.2% | +1648 to +5328 | yes: LOSS |
| time over the response line (% of samples) | 0 | 21.59 | +21.6 (native is 0) | +11.34 to +31.84 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.3 | +12.3 (native is 0) | +7.664 to +16.94 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 205.2 | +205 (native is 0) | +132.5 to +277.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 14.23 | +14.2 (native is 0) | +9.145 to +19.31 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.00616 | 0.03778 | +513.4% | +0.02874 to +0.03451 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2957 | 1.641 | +455.1% | +1.166 to +1.525 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03944 | +0.0394 (native is 0) | +0.03661 to +0.04227 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2957 | 1.681 | +468.4% | +1.203 to +1.567 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4162 | 723.3 | -82.6% | -3903 to -2975 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.117 | 5.03 | +22.2% | +0.4775 to +1.348 | yes: power given |
| pods started | 0.5 | 2.7 | +440.0% | +0.9028 to +3.497 | yes: power given |
| pod start wait, total (s) | 0.6 | 6.5 | +983.3% | +2.711 to +9.089 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.897 | +279.3% | +0.473 to +2.32 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.74 | 53.35 | +288.2% | +34.65 to +44.56 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 869.1 | -42.2% | -721.2 to -546.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 0.1 | -100.0% | -1160 to -1152 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 0.7 | -100.0% | -1475 to -1468 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 173.2 | -85.0% | -1066 to -900.3 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.61 | -44.9% | -5.98 to -4.8 | yes: GAIN |
| node-hours | 5.024 | 2.766 | -45.0% | -2.511 to -2.006 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 504.2 | -3.8% | -23.07 to -16.89 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 335.1 | -36.1% | -207.6 to -170.7 | yes: GAIN |
| response time (ms), mean | 513.6 | 72.93 | -85.8% | -661.7 to -219.6 | yes: GAIN |
| response time (ms), 95th percentile | 1993 | 93.27 | -95.3% | -2949 to -849.7 | yes: GAIN |
| response time (ms), 99th percentile | 2946 | 125.6 | -95.7% | -4358 to -1282 | yes: GAIN |
| time over the response line (% of samples) | 19.55 | 0.007201 | -100.0% | -31.03 to -8.053 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0 | -100.0% | -15 to -4.803 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 | +33 (native is 0) | +31.03 to +34.97 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.68 | 0.07833 | -99.4% | -17.59 to -7.605 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03317 | 0.009508 | -71.3% | -0.02671 to -0.02061 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.592 | 0.2509 | -84.2% | -1.496 to -1.186 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02136 | +0.0214 (native is 0) | +0.01878 to +0.02394 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.592 | 0.2723 | -82.9% | -1.473 to -1.167 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.8 | 3271 | +306.0% | +2138 to +2793 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.103 | 4.727 | +15.2% | +0.3757 to +0.8725 | yes: power given |
| pods started | 0.4 | 1.9 | +375.0% | +0.1407 to +2.859 | yes: power given |
| pod start wait, total (s) | 0.7 | 2.7 | +285.7% | +0.1226 to +3.877 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.208 | +101.4% | -0.1509 to +1.368 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 16.02 | -67.0% | -36.65 to -28.5 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 836 | 1503 | +79.7% | +597.8 to +735.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1156 | +1541277.8% | +1153 to +1159 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1472 | +294320.0% | +1469 to +1474 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 145.7 | 1156 | +693.6% | +939.4 to +1081 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*