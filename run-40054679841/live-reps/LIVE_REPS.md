# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.241 | 5.466 |
| node-hours | 2.515 | 2.513 | 2.197 | 2.289 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | 272.4 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | 248.5 | 255.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 326.6 | 314.8 | 291.7 | 282.5 |
| response time (ms), 95th percentile | 1080 | 1168 | 1115 | 1276 |
| response time (ms), 99th percentile | 1564 | 1811 | 1635 | 1992 |
| time over the response line (% of samples) | 19.12 | 14.68 | 18.46 | 13.94 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.6 | 9.6 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 33.8 | 33.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 11.5 | 11.25 | 11.35 |
| utilisation (used / allocatable) | 0.05999 | 0.05889 | 0.06909 | 0.06699 |
| CPU used (cores), mean | 1.44 | 1.413 | 1.428 | 1.433 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0159 | 0.01542 |
| CPU used with Omni's own (cores), mean | 1.44 | 1.413 | 1.444 | 1.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 468.3 | 415.5 | 426.1 |
| HPA replicas, mean | 1.966 | 2.008 | 2.266 | 2.489 |
| pods started | 0 | 0 | 0.2 | 0.8 |
| pod start wait, total (s) | 0 | 0 | 0.7 | 1.3 |
| pod start wait, mean (s) | 0 | 0 | 0.7 | 1.3 |
| host CPU busy, the real machine under kind (%) | 40.94 | 40.46 | 41.5 | 41.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 770 | 762.8 | 769 | 769.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.706 | 5.177 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05 | 0.05833 | 0.09167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | 0.3 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 76.74 | 75.04 | 76.7 | 80.58 |
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
| worker nodes in service, mean | 6 | 5.466 | -8.9% | -1.319 to +0.2509 | no |
| node-hours | 2.513 | 2.289 | -8.9% | -0.5496 to +0.1017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.3 | +0.2% | -0.6915 to +1.605 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 255.5 | -6.0% | -40.46 to +7.725 | no |
| response time (ms), mean | 314.8 | 282.5 | -10.3% | -62.32 to -2.326 | yes: GAIN |
| response time (ms), 95th percentile | 1168 | 1276 | +9.3% | -81.35 to +297.9 | no |
| response time (ms), 99th percentile | 1811 | 1992 | +10.0% | -109.8 to +470.5 | no |
| time over the response line (% of samples) | 14.68 | 13.94 | -5.0% | -2.052 to +0.5756 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.7 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.3 (native is 0) | +24.96 to +41.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 11.35 | -1.3% | -2.007 to +1.714 | no |
| utilisation (used / allocatable) | 0.05889 | 0.06699 | +13.8% | -0.002653 to +0.01885 | no |
| CPU used (cores), mean | 1.413 | 1.433 | +1.4% | -0.005764 to +0.04518 | no |
| Omni's own CPU (cores), mean | 0 | 0.01542 | +0.0154 (native is 0) | +0.01375 to +0.01709 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.449 | +2.5% | +0.01003 to +0.06023 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.3 | 426.1 | -9.0% | -96.43 to +11.87 | no |
| HPA replicas, mean | 2.008 | 2.489 | +23.9% | +0.1702 to +0.7909 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.4984 to +1.102 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | +0.7111 to +1.889 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.7111 to +1.889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.46 | 41.66 | +3.0% | +0.8132 to +1.6 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.8 | 769.7 | +0.9% | +0.6782 to +13.12 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.177 | -13.7% | -2.022 to +0.3755 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.09167 | +83.3% | +0.004494 to +0.07884 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.04 | 80.58 | +7.4% | -1.127 to +12.22 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 2.515 | 2.513 | -0.1% | -0.007732 to +0.003398 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | -0.2% | -1.091 to -0.04104 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | -0.2% | -1.091 to -0.04104 | yes: GAIN |
| response time (ms), mean | 326.6 | 314.8 | -3.6% | -25.7 to +2.129 | no |
| response time (ms), 95th percentile | 1080 | 1168 | +8.1% | -32.04 to +208 | no |
| response time (ms), 99th percentile | 1564 | 1811 | +15.8% | +69.99 to +423.9 | yes: LOSS |
| time over the response line (% of samples) | 19.12 | 14.68 | -23.2% | -6.548 to -2.326 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.6 | -3.0% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 11.5 | +14.2% | -0.3218 to +3.185 | no |
| utilisation (used / allocatable) | 0.05999 | 0.05889 | -1.8% | -0.002204 to +9.499e-06 | no |
| CPU used (cores), mean | 1.44 | 1.413 | -1.8% | -0.0529 to +0.000228 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.44 | 1.413 | -1.8% | -0.0529 to +0.000228 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 468.3 | +2.0% | -0.9455 to +19.53 | no |
| HPA replicas, mean | 1.966 | 2.008 | +2.1% | -0.05405 to +0.1383 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 40.46 | -1.2% | -0.8201 to -0.1516 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770 | 762.8 | -0.9% | -11.89 to -2.506 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05 | -14.3% | -0.05451 to +0.03784 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.74 | 75.04 | -2.2% | -5.341 to +1.941 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | -12.7% | -1.528 to +0.009852 | no |
| node-hours | 2.515 | 2.197 | -12.6% | -0.6401 to +0.003911 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | -0.0% | -0.897 to +0.7559 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 248.5 | -8.8% | -48.15 to +0.3453 | no |
| response time (ms), mean | 326.6 | 291.7 | -10.7% | -55.74 to -14.02 | yes: GAIN |
| response time (ms), 95th percentile | 1080 | 1115 | +3.2% | -83.04 to +152.1 | no |
| response time (ms), 99th percentile | 1564 | 1635 | +4.5% | -45.78 to +187.2 | no |
| time over the response line (% of samples) | 19.12 | 18.46 | -3.4% | -1.784 to +0.4752 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.6 | -3.0% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.8 (native is 0) | +21.53 to +46.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 11.25 | +11.7% | -0.7537 to +3.114 | no |
| utilisation (used / allocatable) | 0.05999 | 0.06909 | +15.2% | -0.0001869 to +0.01839 | no |
| CPU used (cores), mean | 1.44 | 1.428 | -0.8% | -0.03892 to +0.01585 | no |
| Omni's own CPU (cores), mean | 0 | 0.0159 | +0.0159 (native is 0) | +0.0145 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.444 | +0.3% | -0.0237 to +0.03243 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 415.5 | -9.5% | -88.92 to +1.838 | no |
| HPA replicas, mean | 1.966 | 2.266 | +15.3% | +0.02204 to +0.5785 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.369 to +1.769 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.369 to +1.769 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 41.5 | +1.4% | +0.08027 to +1.044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770 | 769 | -0.1% | -6.663 to +4.663 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.706 | -21.6% | -2.527 to -0.06169 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05833 | +0.0% | -0.06124 to +0.06124 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.74 | 76.7 | -0.1% | -6.187 to +6.104 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | -12.7% | -1.528 to +0.009852 | no |
| node-hours | 2.513 | 2.197 | -12.6% | -0.6394 to +0.00759 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.4 | +0.2% | -0.8092 to +1.8 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 248.5 | -8.6% | -47.67 to +0.9991 | no |
| response time (ms), mean | 314.8 | 291.7 | -7.3% | -40.93 to -5.256 | yes: GAIN |
| response time (ms), 95th percentile | 1168 | 1115 | -4.6% | -179.7 to +72.8 | no |
| response time (ms), 99th percentile | 1811 | 1635 | -9.7% | -342.2 to -10.36 | yes: GAIN |
| time over the response line (% of samples) | 14.68 | 18.46 | +25.8% | +1.765 to +5.801 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.8 (native is 0) | +21.53 to +46.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 11.25 | -2.2% | -1.604 to +1.101 | no |
| utilisation (used / allocatable) | 0.05889 | 0.06909 | +17.3% | +0.0005765 to +0.01983 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.413 | 1.428 | +1.0% | -0.004106 to +0.0337 | no |
| Omni's own CPU (cores), mean | 0 | 0.0159 | +0.0159 (native is 0) | +0.0145 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.444 | +2.2% | +0.01112 to +0.05028 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.3 | 415.5 | -11.3% | -103.2 to -2.513 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.266 | +12.9% | +0.009097 to +0.5072 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.369 to +1.769 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.369 to +1.769 | no |
| host CPU busy, the real machine under kind (%) | 40.46 | 41.5 | +2.6% | +0.782 to +1.314 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.8 | 769 | +0.8% | +2.199 to +10.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.706 | -21.6% | -2.527 to -0.06169 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05833 | +16.7% | -0.0283 to +0.04497 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.04 | 76.7 | +2.2% | -2.123 to +5.44 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.466 | -8.9% | -1.319 to +0.2509 | no |
| node-hours | 2.515 | 2.289 | -9.0% | -0.5524 to +0.1002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 | -0.0% | -1.015 to +0.7961 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 255.5 | -6.2% | -41.05 to +7.19 | no |
| response time (ms), mean | 326.6 | 282.5 | -13.5% | -76.03 to -12.19 | yes: GAIN |
| response time (ms), 95th percentile | 1080 | 1276 | +18.2% | +7.855 to +384.6 | yes: LOSS |
| response time (ms), 99th percentile | 1564 | 1992 | +27.3% | +97.97 to +756.7 | yes: LOSS |
| time over the response line (% of samples) | 19.12 | 13.94 | -27.1% | -8.167 to -2.184 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.7 | -2.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.3 (native is 0) | +24.96 to +41.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 11.35 | +12.8% | -0.8378 to +3.408 | no |
| utilisation (used / allocatable) | 0.05999 | 0.06699 | +11.7% | -0.003691 to +0.01769 | no |
| CPU used (cores), mean | 1.44 | 1.433 | -0.5% | -0.02327 to +0.01002 | no |
| Omni's own CPU (cores), mean | 0 | 0.01542 | +0.0154 (native is 0) | +0.01375 to +0.01709 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.449 | +0.6% | -0.008322 to +0.02591 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 426.1 | -7.2% | -84.59 to +18.61 | no |
| HPA replicas, mean | 1.966 | 2.489 | +26.6% | +0.1827 to +0.8627 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.4984 to +1.102 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | +0.7111 to +1.889 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.7111 to +1.889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.94 | 41.66 | +1.8% | +0.2044 to +1.238 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770 | 769.7 | -0.0% | -8.851 to +8.251 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.177 | -13.7% | -2.022 to +0.3755 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.09167 | +57.1% | -0.01886 to +0.08553 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.74 | 80.58 | +5.0% | -4.9 to +12.59 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*