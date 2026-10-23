# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.923 | 5.796 |
| node-hours | 2.513 | 2.514 | 2.483 | 2.428 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | 274.2 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274 | 271.8 | 268 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 467 | 487.6 | 482.1 | 496.1 |
| response time (ms), 95th percentile | 1786 | 2051 | 1928 | 2093 |
| response time (ms), 99th percentile | 2724 | 3188 | 3030 | 3333 |
| time over the response line (% of samples) | 26.23 | 24.11 | 26.28 | 24.54 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 13 | 12.8 | 12.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 60.9 | 52.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.86 | 13.32 | 14.57 | 15.71 |
| utilisation (used / allocatable) | 0.06543 | 0.06573 | 0.06626 | 0.0683 |
| CPU used (cores), mean | 1.57 | 1.578 | 1.572 | 1.583 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04488 | 0.04953 |
| CPU used with Omni's own (cores), mean | 1.57 | 1.578 | 1.617 | 1.633 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.9 | 416.8 | 414.3 | 405.2 |
| HPA replicas, mean | 2.064 | 2.124 | 2.823 | 2.994 |
| pods started | 0.5 | 0 | 2 | 2.4 |
| pod start wait, total (s) | 1.2 | 0 | 4.7 | 4.9 |
| pod start wait, mean (s) | 0.75 | 0 | 2.158 | 1.75 |
| host CPU busy, the real machine under kind (%) | 45.01 | 45.83 | 46.81 | 47.96 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806.1 | 813.2 | 813.3 | 825.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.845 | 5.639 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2542 | 0.1167 | 0.2833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | 0.7 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 128.8 | 124.6 | 140.6 |
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
| worker nodes in service, mean | 6 | 5.796 | -3.4% | -0.5943 to +0.1871 | no |
| node-hours | 2.514 | 2.428 | -3.4% | -0.2475 to +0.07619 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.4 | +0.1% | -0.5912 to +1.292 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 268 | -2.2% | -17.9 to +5.829 | no |
| response time (ms), mean | 487.6 | 496.1 | +1.7% | -26.89 to +43.79 | no |
| response time (ms), 95th percentile | 2051 | 2093 | +2.0% | -268.7 to +351.8 | no |
| response time (ms), 99th percentile | 3188 | 3333 | +4.6% | -401.3 to +692.8 | no |
| time over the response line (% of samples) | 24.11 | 24.54 | +1.8% | -0.4916 to +1.366 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 12.8 | -1.5% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.4 | +52.4 (native is 0) | +41.42 to +63.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 15.71 | +17.9% | +0.4478 to +4.319 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06573 | 0.0683 | +3.9% | -0.00105 to +0.006174 | no |
| CPU used (cores), mean | 1.578 | 1.583 | +0.3% | -0.02193 to +0.03271 | no |
| Omni's own CPU (cores), mean | 0 | 0.04953 | +0.0495 (native is 0) | +0.04829 to +0.05077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.578 | 1.633 | +3.5% | +0.02662 to +0.08322 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.8 | 405.2 | -2.8% | -27.49 to +4.248 | no |
| HPA replicas, mean | 2.124 | 2.994 | +41.0% | +0.5712 to +1.17 | yes: power given |
| pods started | 0 | 2.4 | +2.4 (native is 0) | +0.9225 to +3.878 | yes: power given |
| pod start wait, total (s) | 0 | 4.9 | +4.9 (native is 0) | +1.588 to +8.212 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.75 | +1.75 (native is 0) | +1.199 to +2.301 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.83 | 47.96 | +4.7% | +1.813 to +2.457 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 813.2 | 825.4 | +1.5% | +4.572 to +19.83 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.639 | -6.0% | -1.02 to +0.2987 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.2833 | +11.5% | -0.02712 to +0.08545 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.9 | -10.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.8 | 140.6 | +9.1% | +3.416 to +20.06 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.006e-15 to +1.539e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.514 | +0.0% | -0.007394 to +0.009728 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | +0.1% | -0.6784 to +1.1 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 274 | +0.1% | -0.6784 to +1.1 | no |
| response time (ms), mean | 467 | 487.6 | +4.4% | -6.388 to +47.67 | no |
| response time (ms), 95th percentile | 1786 | 2051 | +14.9% | +11.86 to +518.6 | yes: LOSS |
| response time (ms), 99th percentile | 2724 | 3188 | +17.0% | +88.25 to +838.3 | yes: LOSS |
| time over the response line (% of samples) | 26.23 | 24.11 | -8.1% | -3.252 to -0.9966 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 13 | -2.3% | -0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.86 | 13.32 | -3.9% | -3.264 to +2.184 | no |
| utilisation (used / allocatable) | 0.06543 | 0.06573 | +0.5% | -0.0001464 to +0.0007638 | no |
| CPU used (cores), mean | 1.57 | 1.578 | +0.5% | -0.003514 to +0.01833 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.57 | 1.578 | +0.5% | -0.003514 to +0.01833 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.9 | 416.8 | -0.5% | -4.934 to +0.7696 | no |
| HPA replicas, mean | 2.064 | 2.124 | +2.9% | -0.1097 to +0.2278 | no |
| pods started | 0.5 | 0 | -100.0% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 1.2 | 0 | -100.0% | -2.623 to +0.2226 | no |
| pod start wait, mean (s) | 0.75 | 0 | -100.0% | -1.63 to +0.1301 | no |
| host CPU busy, the real machine under kind (%) | 45.01 | 45.83 | +1.8% | +0.5967 to +1.033 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.1 | 813.2 | +0.9% | +3.605 to +10.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2542 | +144.0% | +0.09173 to +0.2083 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | +66.7% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 128.8 | +10.0% | +7.478 to +15.96 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.923 | -1.3% | -0.196 to +0.04285 | no |
| node-hours | 2.513 | 2.483 | -1.2% | -0.07801 to +0.01823 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.2 | +0.1% | -0.4193 to +1.175 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 271.8 | -0.7% | -5.5 to +1.448 | no |
| response time (ms), mean | 467 | 482.1 | +3.2% | +1.001 to +29.27 | yes: LOSS |
| response time (ms), 95th percentile | 1786 | 1928 | +8.0% | +47.5 to +237 | yes: LOSS |
| response time (ms), 99th percentile | 2724 | 3030 | +11.2% | +121 to +489.5 | yes: LOSS |
| time over the response line (% of samples) | 26.23 | 26.28 | +0.2% | -0.6672 to +0.765 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 12.8 | -3.8% | -1.631 to +0.631 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.9 | +60.9 (native is 0) | +51.41 to +70.39 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.86 | 14.57 | +5.1% | -1.034 to +2.451 | no |
| utilisation (used / allocatable) | 0.06543 | 0.06626 | +1.3% | -0.0003872 to +0.002054 | no |
| CPU used (cores), mean | 1.57 | 1.572 | +0.1% | -0.009582 to +0.01284 | no |
| Omni's own CPU (cores), mean | 0 | 0.04488 | +0.0449 (native is 0) | +0.04251 to +0.04725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 1.617 | +3.0% | +0.03537 to +0.05765 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.9 | 414.3 | -1.1% | -12.33 to +3.161 | no |
| HPA replicas, mean | 2.064 | 2.823 | +36.8% | +0.4938 to +1.024 | yes: power given |
| pods started | 0.5 | 2 | +300.0% | +0.5921 to +2.408 | yes: power given |
| pod start wait, total (s) | 1.2 | 4.7 | +291.7% | +1.585 to +5.415 | yes: LOSS |
| pod start wait, mean (s) | 0.75 | 2.158 | +187.8% | +0.5339 to +2.283 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.01 | 46.81 | +4.0% | +1.532 to +2.07 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.1 | 813.3 | +0.9% | +2.806 to +11.59 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.845 | -2.6% | -0.3874 to +0.07742 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1167 | +12.0% | -0.09362 to +0.1186 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.7 | +16.7% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 124.6 | +6.4% | +2.298 to +12.75 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.923 | -1.3% | -0.196 to +0.04285 | no |
| node-hours | 2.514 | 2.483 | -1.2% | -0.07916 to +0.01705 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.2 | +0.1% | -0.429 to +0.7636 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 271.8 | -0.8% | -5.753 to +1.28 | no |
| response time (ms), mean | 487.6 | 482.1 | -1.1% | -35.42 to +24.41 | no |
| response time (ms), 95th percentile | 2051 | 1928 | -6.0% | -409.1 to +163.2 | no |
| response time (ms), 99th percentile | 3188 | 3030 | -5.0% | -570.8 to +254.8 | no |
| time over the response line (% of samples) | 24.11 | 26.28 | +9.0% | +1.029 to +3.317 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 12.8 | -1.5% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.9 | +60.9 (native is 0) | +51.41 to +70.39 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 14.57 | +9.4% | -0.7756 to +3.272 | no |
| utilisation (used / allocatable) | 0.06573 | 0.06626 | +0.8% | -0.0005927 to +0.001642 | no |
| CPU used (cores), mean | 1.578 | 1.572 | -0.4% | -0.01787 to +0.006309 | no |
| Omni's own CPU (cores), mean | 0 | 0.04488 | +0.0449 (native is 0) | +0.04251 to +0.04725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.578 | 1.617 | +2.5% | +0.0264 to +0.05181 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.8 | 414.3 | -0.6% | -8.883 to +3.882 | no |
| HPA replicas, mean | 2.124 | 2.823 | +33.0% | +0.4192 to +0.9805 | yes: power given |
| pods started | 0 | 2 | +2 (native is 0) | +1.108 to +2.892 | yes: power given |
| pod start wait, total (s) | 0 | 4.7 | +4.7 (native is 0) | +2.593 to +6.807 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.158 | +2.16 (native is 0) | +1.541 to +2.776 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.83 | 46.81 | +2.2% | +0.6921 to +1.28 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 813.2 | 813.3 | +0.0% | -4.674 to +4.874 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.845 | -2.6% | -0.3874 to +0.07742 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.1167 | -54.1% | -0.2064 to -0.0686 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.7 | -30.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 128.8 | 124.6 | -3.3% | -9.975 to +1.584 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.796 | -3.4% | -0.5943 to +0.1871 | no |
| node-hours | 2.513 | 2.428 | -3.4% | -0.2459 to +0.07685 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274.4 | +0.2% | -0.1248 to +1.247 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 268 | -2.1% | -17.58 to +5.926 | no |
| response time (ms), mean | 467 | 496.1 | +6.2% | +7.972 to +50.22 | yes: LOSS |
| response time (ms), 95th percentile | 1786 | 2093 | +17.2% | +106.9 to +506.7 | yes: LOSS |
| response time (ms), 99th percentile | 2724 | 3333 | +22.4% | +221.9 to +996.1 | yes: LOSS |
| time over the response line (% of samples) | 26.23 | 24.54 | -6.4% | -2.878 to -0.4963 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.3 | 12.8 | -3.8% | -1.631 to +0.631 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.4 | +52.4 (native is 0) | +41.42 to +63.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.86 | 15.71 | +13.3% | -1.118 to +4.805 | no |
| utilisation (used / allocatable) | 0.06543 | 0.0683 | +4.4% | -0.0008657 to +0.006607 | no |
| CPU used (cores), mean | 1.57 | 1.583 | +0.8% | -0.01036 to +0.03596 | no |
| Omni's own CPU (cores), mean | 0 | 0.04953 | +0.0495 (native is 0) | +0.04829 to +0.05077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 1.633 | +4.0% | +0.03823 to +0.08643 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.9 | 405.2 | -3.3% | -31 to +3.594 | no |
| HPA replicas, mean | 2.064 | 2.994 | +45.0% | +0.5961 to +1.264 | yes: power given |
| pods started | 0.5 | 2.4 | +380.0% | +0.03928 to +3.761 | yes: power given |
| pod start wait, total (s) | 1.2 | 4.9 | +308.3% | -0.4305 to +7.831 | no |
| pod start wait, mean (s) | 0.75 | 1.75 | +133.3% | -0.124 to +2.124 | no |
| host CPU busy, the real machine under kind (%) | 45.01 | 47.96 | +6.6% | +2.698 to +3.201 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.1 | 825.4 | +2.4% | +12.35 to +26.25 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.639 | -6.0% | -1.02 to +0.2987 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2833 | +172.0% | +0.08486 to +0.2735 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.1 | 140.6 | +20.0% | +15.44 to +31.48 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*