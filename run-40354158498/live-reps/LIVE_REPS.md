# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.412 | 5.405 |
| node-hours | 2.518 | 2.517 | 2.269 | 2.267 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | 272 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.1 | 253.6 | 252.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 331.4 | 341.8 | 340.2 | 345.5 |
| response time (ms), 95th percentile | 1208 | 1285 | 1260 | 1354 |
| response time (ms), 99th percentile | 1853 | 2134 | 1877 | 2181 |
| time over the response line (% of samples) | 16.19 | 15.49 | 16.79 | 15.43 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.3 | 9.4 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 10.4 | 13.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.51 | 11.29 | 11.18 | 10.69 |
| utilisation (used / allocatable) | 0.05919 | 0.05951 | 0.06589 | 0.0638 |
| CPU used (cores), mean | 1.421 | 1.428 | 1.425 | 1.39 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01223 | 0.01351 |
| CPU used with Omni's own (cores), mean | 1.421 | 1.428 | 1.438 | 1.404 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 466.8 | 428.4 | 443.6 |
| HPA replicas, mean | 2.09 | 2.056 | 2.18 | 2.071 |
| pods started | 0.1 | 0 | 0.1 | 0.3 |
| pod start wait, total (s) | 0.3 | 0 | 0.1 | 0.6 |
| pod start wait, mean (s) | 0.3 | 0 | 0.1 | 0.6 |
| host CPU busy, the real machine under kind (%) | 40.84 | 41.86 | 41.52 | 42.34 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772.7 | 779.9 | 775.7 | 781.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5 | 4.951 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2167 | 0.0625 | 0.2375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | 0.4 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 81.44 | 91.77 | 83.17 | 92.7 |
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
| worker nodes in service, mean | 6 | 5.405 | −9.9% | −1.2403 to +0.0507 | no |
| node-hours | 2.517 | 2.267 | −9.9% | −0.5203 to +0.0211 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.6 | −0.2% | −1.3494 to +0.3949 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 252.9 | −7.0% | −39.9441 to +1.6021 | no |
| response time (ms), mean | 341.8 | 345.5 | +1.1% | −17.1908 to +24.5446 | no |
| response time (ms), 95th percentile | 1285 | 1354 | +5.3% | −20.6279 to +157.4259 | no |
| response time (ms), 99th percentile | 2134 | 2181 | +2.2% | −116.5803 to +211.2297 | no |
| time over the response line (% of samples) | 15.49 | 15.43 | −0.4% | −0.7422 to +0.6178 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.7 | +4.3% | −0.4396 to +1.2396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 | +13.300 (native is 0) | +10.2831 to +16.3169 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 10.69 | −5.3% | −2.2363 to +1.0330 | no |
| utilisation (used / allocatable) | 0.05951 | 0.0638 | +7.2% | −0.0002 to +0.0088 | no |
| CPU used (cores), mean | 1.428 | 1.39 | −2.7% | −0.0951 to +0.0188 | no |
| Omni's own CPU (cores), mean | 0 | 0.01351 | +0.014 (native is 0) | +0.0119 to +0.0152 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 1.404 | −1.7% | −0.0828 to +0.0335 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.8 | 443.6 | −5.0% | −48.5304 to +2.0103 | no |
| HPA replicas, mean | 2.056 | 2.071 | +0.8% | −0.1917 to +0.2229 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 41.86 | 42.34 | +1.2% | +0.0763 to +0.8934 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.9 | 781.1 | +0.2% | −4.2036 to +6.6036 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.951 | −17.5% | −2.1511 to +0.0522 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.2375 | +9.6% | −0.0358 to +0.0775 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.77 | 92.7 | +1.0% | −4.8380 to +6.7047 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.517 | −0.1% | −0.0082 to +0.0052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −0.8257 to +0.7162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.1 | −0.0% | −0.8257 to +0.7162 | no |
| response time (ms), mean | 331.4 | 341.8 | +3.1% | −4.1294 to +24.9510 | no |
| response time (ms), 95th percentile | 1208 | 1285 | +6.4% | −18.5932 to +173.0572 | no |
| response time (ms), 99th percentile | 1853 | 2134 | +15.1% | +15.4746 to +545.7418 | yes: LOSS |
| time over the response line (% of samples) | 16.19 | 15.49 | −4.3% | −1.4019 to +0.0070 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.3 | +1.1% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.51 | 11.29 | +7.5% | −1.0265 to +2.5931 | no |
| utilisation (used / allocatable) | 0.05919 | 0.05951 | +0.5% | −0.0003 to +0.0010 | no |
| CPU used (cores), mean | 1.421 | 1.428 | +0.5% | −0.0081 to +0.0236 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.421 | 1.428 | +0.5% | −0.0081 to +0.0236 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 466.8 | −0.3% | −6.5501 to +4.1549 | no |
| HPA replicas, mean | 2.09 | 2.056 | −1.6% | −0.2169 to +0.1484 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 40.84 | 41.86 | +2.5% | +0.4430 to +1.5837 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772.7 | 779.9 | +0.9% | −0.0069 to +14.4069 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2167 | +147.6% | +0.0688 to +0.1895 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.44 | 91.77 | +12.7% | +2.2954 to +18.3629 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.412 | −9.8% | −1.2092 to +0.0342 | no |
| node-hours | 2.518 | 2.269 | −9.9% | −0.5119 to +0.0127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | −0.0% | −1.0633 to +0.8730 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.6 | −6.8% | −38.2477 to +1.1157 | no |
| response time (ms), mean | 331.4 | 340.2 | +2.7% | −3.3490 to +21.0170 | no |
| response time (ms), 95th percentile | 1208 | 1260 | +4.3% | −9.1576 to +112.2346 | no |
| response time (ms), 99th percentile | 1853 | 1877 | +1.3% | −125.2611 to +171.8097 | no |
| time over the response line (% of samples) | 16.19 | 16.79 | +3.7% | −0.0860 to +1.2788 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.4 | +2.2% | −0.6793 to +1.0793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.4 | +10.400 (native is 0) | +7.8275 to +12.9725 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.51 | 11.18 | +6.4% | −1.4303 to +2.7737 | no |
| utilisation (used / allocatable) | 0.05919 | 0.06589 | +11.3% | −0.0000 to +0.0134 | no |
| CPU used (cores), mean | 1.421 | 1.425 | +0.3% | −0.0189 to +0.0288 | no |
| Omni's own CPU (cores), mean | 0 | 0.01223 | +0.012 (native is 0) | +0.0106 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.438 | +1.2% | −0.0078 to +0.0421 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 428.4 | −8.5% | −81.2309 to +2.0044 | no |
| HPA replicas, mean | 2.09 | 2.18 | +4.3% | −0.1007 to +0.2809 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 40.84 | 41.52 | +1.6% | +0.1545 to +1.1877 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772.7 | 775.7 | +0.4% | −0.7549 to +6.7549 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | −1.9913 to −0.0082 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.0625 | −28.6% | −0.0652 to +0.0152 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.44 | 83.17 | +2.1% | −1.9404 to +5.3988 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.412 | −9.8% | −1.2092 to +0.0342 | no |
| node-hours | 2.517 | 2.269 | −9.9% | −0.5080 to +0.0118 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | −0.0% | −0.9037 to +0.8228 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.6 | −6.8% | −37.7493 to +0.7268 | no |
| response time (ms), mean | 341.8 | 340.2 | −0.5% | −12.4886 to +9.3349 | no |
| response time (ms), 95th percentile | 1285 | 1260 | −2.0% | −122.5014 to +71.1144 | no |
| response time (ms), 99th percentile | 2134 | 1877 | −12.1% | −511.5566 to −3.1112 | yes: GAIN |
| time over the response line (% of samples) | 15.49 | 16.79 | +8.4% | +0.1007 to +2.4870 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.4 | +1.1% | −0.6872 to +0.8872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.4 | +10.400 (native is 0) | +7.8275 to +12.9725 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 11.18 | −1.0% | −1.8783 to +1.6549 | no |
| utilisation (used / allocatable) | 0.05951 | 0.06589 | +10.7% | −0.0007 to +0.0135 | no |
| CPU used (cores), mean | 1.428 | 1.425 | −0.2% | −0.0245 to +0.0188 | no |
| Omni's own CPU (cores), mean | 0 | 0.01223 | +0.012 (native is 0) | +0.0106 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 1.438 | +0.7% | −0.0136 to +0.0324 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.8 | 428.4 | −8.2% | −83.8342 to +7.0028 | no |
| HPA replicas, mean | 2.056 | 2.18 | +6.0% | −0.0071 to +0.2557 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 41.86 | 41.52 | −0.8% | −0.6356 to −0.0489 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.9 | 775.7 | −0.5% | −11.1581 to +2.7581 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | −1.9913 to −0.0082 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2167 | 0.0625 | −71.2% | −0.2385 to −0.0698 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.4 | −55.6% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 91.77 | 83.17 | −9.4% | −15.9954 to −1.2046 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.405 | −9.9% | −1.2403 to +0.0507 | no |
| node-hours | 2.518 | 2.267 | −10.0% | −0.5228 to +0.0207 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.6 | −0.2% | −1.6546 to +0.5906 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 252.9 | −7.1% | −40.2863 to +1.8348 | no |
| response time (ms), mean | 331.4 | 345.5 | +4.3% | −1.4645 to +29.6399 | no |
| response time (ms), 95th percentile | 1208 | 1354 | +12.1% | +19.3133 to +271.9487 | yes: LOSS |
| response time (ms), 99th percentile | 1853 | 2181 | +17.7% | +100.2444 to +555.6214 | yes: LOSS |
| time over the response line (% of samples) | 16.19 | 15.43 | −4.7% | −1.5729 to +0.0536 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.7 | +5.4% | −0.1079 to +1.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 | +13.300 (native is 0) | +10.2831 to +16.3169 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.51 | 10.69 | +1.7% | −1.4039 to +1.7672 | no |
| utilisation (used / allocatable) | 0.05919 | 0.0638 | +7.8% | +0.0005 to +0.0087 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.39 | −2.1% | −0.0921 to +0.0313 | no |
| Omni's own CPU (cores), mean | 0 | 0.01351 | +0.014 (native is 0) | +0.0119 to +0.0152 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.404 | −1.2% | −0.0796 to +0.0459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 443.6 | −5.2% | −45.9839 to −2.9313 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.09 | 2.071 | −0.9% | −0.1861 to +0.1488 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.8209 to +1.4209 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.8209 to +1.4209 | no |
| host CPU busy, the real machine under kind (%) | 40.84 | 42.34 | +3.7% | +1.2291 to +1.7674 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 772.7 | 781.1 | +1.1% | +1.9384 to +14.8616 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.951 | −17.5% | −2.1511 to +0.0522 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2375 | +171.4% | +0.0525 to +0.2475 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.44 | 92.7 | +13.8% | +3.9444 to +18.5806 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*