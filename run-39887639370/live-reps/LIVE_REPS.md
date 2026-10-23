# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.381 | 5.459 |
| node-hours | 2.519 | 2.514 | 2.259 | 2.283 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.1 | 272.6 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.1 | 253.1 | 255.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 324.7 | 382.6 | 320.4 | 380.1 |
| response time (ms), 95th percentile | 1072 | 1638 | 1253 | 1834 |
| response time (ms), 99th percentile | 1533 | 2573 | 1892 | 2964 |
| time over the response line (% of samples) | 19.38 | 15.46 | 20.19 | 16.17 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.8 | 10.2 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 90.9 | 102.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 16.21 | 11.69 | 16.38 |
| utilisation (used / allocatable) | 0.0592 | 0.05894 | 0.06528 | 0.06595 |
| CPU used (cores), mean | 1.421 | 1.415 | 1.411 | 1.449 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04709 | 0.05442 |
| CPU used with Omni's own (cores), mean | 1.421 | 1.415 | 1.458 | 1.503 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.3 | 474.7 | 435.6 | 428.6 |
| HPA replicas, mean | 1.966 | 2.02 | 2.689 | 2.533 |
| pods started | 0 | 0.1 | 1.4 | 1.7 |
| pod start wait, total (s) | 0 | 0.2 | 2.9 | 2.9 |
| pod start wait, mean (s) | 0 | 0.2 | 1.375 | 1.2 |
| host CPU busy, the real machine under kind (%) | 40.03 | 42.7 | 42.39 | 45.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 766.1 | 804.6 | 778.8 | 816.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.98 | 4.906 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.8458 | 0.06667 | 0.8542 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.7 | 0.5 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 76.49 | 115.7 | 86.63 | 128.1 |
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
| worker nodes in service, mean | 6 | 5.459 | -9.0% | -1.033 to -0.05046 | yes: GAIN |
| node-hours | 2.514 | 2.283 | -9.2% | -0.4366 to -0.02517 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | -0.0% | -0.7739 to +0.6896 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 255.1 | -6.3% | -32.55 to -1.513 | yes: GAIN |
| response time (ms), mean | 382.6 | 380.1 | -0.6% | -42.8 to +37.87 | no |
| response time (ms), 95th percentile | 1638 | 1834 | +12.0% | -105.9 to +497.7 | no |
| response time (ms), 99th percentile | 2573 | 2964 | +15.2% | +68.21 to +713.7 | yes: LOSS |
| time over the response line (% of samples) | 15.46 | 16.17 | +4.6% | -0.4746 to +1.882 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.3 | +5.1% | -0.005799 to +1.006 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.3 | +102 (native is 0) | +80.98 to +123.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.21 | 16.38 | +1.1% | -2.151 to +2.508 | no |
| utilisation (used / allocatable) | 0.05894 | 0.06595 | +11.9% | +0.002229 to +0.01179 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.449 | +2.4% | +0.01882 to +0.04899 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05442 | +0.0544 (native is 0) | +0.04671 to +0.06213 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.503 | +6.2% | +0.06849 to +0.1082 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.7 | 428.6 | -9.7% | -82.84 to -9.307 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.02 | 2.533 | +25.4% | +0.219 to +0.8079 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.2854 to +2.915 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.9 | +1350.0% | +0.3871 to +5.013 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | +0.0575 to +1.942 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.7 | 45.28 | +6.0% | +1.758 to +3.386 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 804.6 | 816.8 | +1.5% | +4.993 to +19.41 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.906 | -18.2% | -2.05 to -0.1386 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 0.8542 | +1.0% | -0.06163 to +0.0783 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.6 | -5.9% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.7 | 128.1 | +10.7% | +3.749 to +21.04 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | no |
| node-hours | 2.519 | 2.514 | -0.2% | -0.009012 to -0.001988 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.1 | -0.2% | -1.189 to +0.1798 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.1 | -0.2% | -1.189 to +0.1798 | no |
| response time (ms), mean | 324.7 | 382.6 | +17.8% | +13.18 to +102.5 | yes: LOSS |
| response time (ms), 95th percentile | 1072 | 1638 | +52.8% | +199.7 to +932.8 | yes: LOSS |
| response time (ms), 99th percentile | 1533 | 2573 | +67.9% | +479.8 to +1602 | yes: LOSS |
| time over the response line (% of samples) | 19.38 | 15.46 | -20.2% | -6.075 to -1.753 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.8 | +2.1% | -0.9081 to +1.308 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 16.2 | +48.8% | +3.01 to +7.613 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0592 | 0.05894 | -0.4% | -0.001604 to +0.00109 | no |
| CPU used (cores), mean | 1.421 | 1.415 | -0.4% | -0.0385 to +0.02616 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.421 | 1.415 | -0.4% | -0.0385 to +0.02616 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.3 | 474.7 | +1.2% | -8.409 to +19.22 | no |
| HPA replicas, mean | 1.966 | 2.02 | +2.7% | -0.1095 to +0.216 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.03 | 42.7 | +6.7% | +2.2 to +3.146 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 766.1 | 804.6 | +5.0% | +20.79 to +56.21 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.8458 | +2437.5% | +0.734 to +0.891 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.7 | +1600.0% | +1.231 to +1.969 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.49 | 115.7 | +51.2% | +19.88 to +58.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.381 | -10.3% | -1.372 to +0.1338 | no |
| node-hours | 2.519 | 2.259 | -10.3% | -0.5772 to +0.05578 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 | -0.0% | -0.8995 to +0.8338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 253.1 | -7.2% | -43.95 to +4.872 | no |
| response time (ms), mean | 324.7 | 320.4 | -1.3% | -26.63 to +17.94 | no |
| response time (ms), 95th percentile | 1072 | 1253 | +16.9% | +51.55 to +310.5 | yes: LOSS |
| response time (ms), 99th percentile | 1533 | 1892 | +23.5% | +82.89 to +636.6 | yes: LOSS |
| time over the response line (% of samples) | 19.38 | 20.19 | +4.2% | +0.1601 to +1.463 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.2 | +6.2% | +0.2306 to +0.9694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.9 | +90.9 (native is 0) | +66.5 to +115.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 11.69 | +7.3% | -2.679 to +4.269 | no |
| utilisation (used / allocatable) | 0.0592 | 0.06528 | +10.3% | +0.0002808 to +0.01188 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.411 | -0.7% | -0.06707 to +0.04766 | no |
| Omni's own CPU (cores), mean | 0 | 0.04709 | +0.0471 (native is 0) | +0.04094 to +0.05324 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.458 | +2.6% | -0.02497 to +0.09975 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.3 | 435.6 | -7.2% | -65.68 to -1.572 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.689 | +36.8% | +0.4022 to +1.043 | yes: power given |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.4952 to +2.305 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +0.7821 to +5.018 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.375 | +1.38 (native is 0) | +0.6058 to +2.144 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.03 | 42.39 | +5.9% | +1.648 to +3.06 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 766.1 | 778.8 | +1.7% | +4.699 to +20.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.98 | -17.0% | -2.194 to +0.1539 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.06667 | +100.0% | -0.0005035 to +0.06717 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.49 | 86.63 | +13.3% | +2.3 to +17.98 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.381 | -10.3% | -1.372 to +0.1338 | no |
| node-hours | 2.514 | 2.259 | -10.2% | -0.5717 to +0.06124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.6 | +0.2% | -0.581 to +1.524 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.1 | -7.0% | -43.33 to +5.267 | no |
| response time (ms), mean | 382.6 | 320.4 | -16.3% | -89.06 to -35.31 | yes: GAIN |
| response time (ms), 95th percentile | 1638 | 1253 | -23.5% | -648.8 to -121.6 | yes: GAIN |
| response time (ms), 99th percentile | 2573 | 1892 | -26.5% | -1063 to -298.8 | yes: GAIN |
| time over the response line (% of samples) | 15.46 | 20.19 | +30.6% | +2.471 to +6.98 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.2 | +4.1% | -0.8251 to +1.625 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.9 | +90.9 (native is 0) | +66.5 to +115.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.21 | 11.69 | -27.9% | -6.751 to -2.283 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05894 | 0.06528 | +10.8% | -0.0003484 to +0.01302 | no |
| CPU used (cores), mean | 1.415 | 1.411 | -0.2% | -0.0633 to +0.05623 | no |
| Omni's own CPU (cores), mean | 0 | 0.04709 | +0.0471 (native is 0) | +0.04094 to +0.05324 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.458 | +3.1% | -0.01902 to +0.1061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.7 | 435.6 | -8.2% | -81.61 to +3.542 | no |
| HPA replicas, mean | 2.02 | 2.689 | +33.1% | +0.357 to +0.9818 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.2856 to +2.314 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.9 | +1350.0% | +0.3871 to +5.013 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.375 | +587.5% | +0.1219 to +2.228 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.7 | 42.39 | -0.7% | -0.792 to +0.1547 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 804.6 | 778.8 | -3.2% | -37.8 to -13.8 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.98 | -17.0% | -2.194 to +0.1539 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 0.06667 | -92.1% | -0.8587 to -0.6996 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.5 | -70.6% | -1.502 to -0.8984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 115.7 | 86.63 | -25.1% | -42.46 to -15.63 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.459 | -9.0% | -1.033 to -0.05046 | yes: GAIN |
| node-hours | 2.519 | 2.283 | -9.4% | -0.4421 to -0.03062 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.1 | -0.2% | -1.315 to +0.2223 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 255.1 | -6.4% | -33.34 to -1.734 | yes: GAIN |
| response time (ms), mean | 324.7 | 380.1 | +17.1% | +6.67 to +104.1 | yes: LOSS |
| response time (ms), 95th percentile | 1072 | 1834 | +71.1% | +355 to +1169 | yes: LOSS |
| response time (ms), 99th percentile | 1533 | 2964 | +93.4% | +691.8 to +2172 | yes: LOSS |
| time over the response line (% of samples) | 19.38 | 16.17 | -16.6% | -5.082 to -1.339 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.3 | +7.3% | -0.1294 to +1.529 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.3 | +102 (native is 0) | +80.98 to +123.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 16.38 | +50.4% | +3.366 to +7.614 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0592 | 0.06595 | +11.4% | +0.003037 to +0.01046 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.449 | +2.0% | -0.006048 to +0.06151 | no |
| Omni's own CPU (cores), mean | 0 | 0.05442 | +0.0544 (native is 0) | +0.04671 to +0.06213 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.503 | +5.8% | +0.04219 to +0.1221 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.3 | 428.6 | -8.7% | -68.29 to -13.04 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.533 | +28.8% | +0.2641 to +0.8693 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.4819 to +2.918 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +0.7821 to +5.018 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | +0.5591 to +1.841 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.03 | 45.28 | +13.1% | +4.133 to +6.358 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 766.1 | 816.8 | +6.6% | +27.35 to +74.05 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.906 | -18.2% | -2.05 to -0.1386 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.8542 | +2462.5% | +0.7032 to +0.9384 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.6 | +1500.0% | +1.123 to +1.877 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.49 | 128.1 | +67.4% | +27.39 to +75.78 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*