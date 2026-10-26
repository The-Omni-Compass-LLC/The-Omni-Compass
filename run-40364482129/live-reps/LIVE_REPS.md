# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.55 | 10.61 |
| node-hours | 5.027 | 5.028 | 4.418 | 4.445 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 525.2 | 524.2 | 525.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 525.2 | 478.5 | 481.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 454.4 | 605 | 445.7 | 663.9 |
| response time (ms), 95th percentile | 1735 | 2827 | 1879 | 3223 |
| response time (ms), 99th percentile | 2479 | 4053 | 2777 | 4438 |
| time over the response line (% of samples) | 17.45 | 19.1 | 17.67 | 21.16 |
| failed requests (%) | 0.01709 | 0.04722 | 0 | 0.1236 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 12.6 | 10.7 | 13.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 91.8 | 35.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 15.87 | 12.58 | 22.44 |
| utilisation (used / allocatable) | 0.03264 | 0.03402 | 0.03701 | 0.03803 |
| CPU used (cores), mean | 1.567 | 1.633 | 1.557 | 1.619 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01316 | 0.01049 |
| CPU used with Omni's own (cores), mean | 1.567 | 1.633 | 1.57 | 1.63 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.8 | 792.5 | 742 | 722.7 |
| HPA replicas, mean | 4.102 | 3.985 | 4.268 | 4.191 |
| pods started | 0.4 | 0 | 0.3 | 0.3 |
| pod start wait, total (s) | 1.1 | 0 | 0.6 | 0.4 |
| pod start wait, mean (s) | 0.5 | 0 | 0.4 | 0.4 |
| host CPU busy, the real machine under kind (%) | 47.91 | 53.79 | 49.6 | 56.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 821.9 | 903.7 | 832.6 | 944.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.53 | 9.546 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.3708 | 0.04167 | 0.6708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | 0.4 | 2.2 |
| queue: job turnaround, submitted to done, mean (s) | 129.1 | 205.1 | 141.3 | 248.8 |
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
| worker nodes in service, mean | 12 | 10.61 | −11.6% | −2.6417 to −0.1368 | yes: GAIN |
| node-hours | 5.028 | 4.445 | −11.6% | −1.1020 to −0.0632 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 525.1 | −0.0% | −1.7955 to +1.7585 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 481.5 | −8.3% | −82.7209 to −4.7035 | yes: GAIN |
| response time (ms), mean | 605 | 663.9 | +9.8% | −25.5310 to +143.5227 | no |
| response time (ms), 95th percentile | 2827 | 3223 | +14.0% | −40.5812 to +832.9852 | no |
| response time (ms), 99th percentile | 4053 | 4438 | +9.5% | +31.6632 to +737.6090 | yes: LOSS |
| time over the response line (% of samples) | 19.1 | 21.16 | +10.8% | +0.8471 to +3.2809 | yes: LOSS |
| failed requests (%) | 0.04722 | 0.1236 | +161.7% | −0.0280 to +0.1807 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 13.4 | +6.3% | +0.3476 to +1.2524 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +18.0120 to +53.5880 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 22.44 | +41.4% | −1.9719 to +15.1019 | no |
| utilisation (used / allocatable) | 0.03402 | 0.03803 | +11.8% | +0.0003 to +0.0078 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.633 | 1.619 | −0.8% | −0.0664 to +0.0394 | no |
| Omni's own CPU (cores), mean | 0 | 0.01049 | +0.010 (native is 0) | +0.0093 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.633 | 1.63 | −0.2% | −0.0564 to +0.0504 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.5 | 722.7 | −8.8% | −133.3597 to −6.3992 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.985 | 4.191 | +5.2% | −0.0216 to +0.4352 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 53.79 | 56.5 | +5.0% | +1.3673 to +4.0520 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 903.7 | 944.2 | +4.5% | +9.7478 to +71.2522 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.546 | −20.4% | −4.5675 to −0.3403 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.6708 | +80.9% | −0.1999 to +0.7999 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 2.2 | +100.0% | −1.4109 to +3.6109 | no |
| queue: job turnaround, submitted to done, mean (s) | 205.1 | 248.8 | +21.3% | +10.3916 to +76.8251 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.027 | 5.028 | +0.0% | −0.0071 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 525.2 | +0.2% | −0.2946 to +2.3251 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 525.2 | +0.2% | −0.2946 to +2.3251 | no |
| response time (ms), mean | 454.4 | 605 | +33.1% | +55.2688 to +245.8582 | yes: LOSS |
| response time (ms), 95th percentile | 1735 | 2827 | +62.9% | +369.2827 to +1814.0973 | yes: LOSS |
| response time (ms), 99th percentile | 2479 | 4053 | +63.5% | +507.6582 to +2640.9424 | yes: LOSS |
| time over the response line (% of samples) | 17.45 | 19.1 | +9.5% | −0.1274 to +3.4285 | no |
| failed requests (%) | 0.01709 | 0.04722 | +176.2% | −0.0508 to +0.1111 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 12.6 | +41.6% | +1.4118 to +5.9882 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 15.87 | +37.7% | +1.9773 to +6.7160 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03264 | 0.03402 | +4.2% | +0.0004 to +0.0024 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.633 | +4.2% | +0.0178 to +0.1146 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.567 | 1.633 | +4.2% | +0.0178 to +0.1146 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.8 | 792.5 | −3.0% | −44.9080 to −3.6590 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.102 | 3.985 | −2.9% | −0.3956 to +0.1612 | no |
| pods started | 0.4 | 0 | −100.0% | −1.0911 to +0.2911 | no |
| pod start wait, total (s) | 1.1 | 0 | −100.0% | −3.1358 to +0.9358 | no |
| pod start wait, mean (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| host CPU busy, the real machine under kind (%) | 47.91 | 53.79 | +12.3% | +4.1508 to +7.5908 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.9 | 903.7 | +10.0% | +27.5154 to +136.0846 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.3708 | +456.3% | +0.1833 to +0.4251 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 129.1 | 205.1 | +58.9% | +29.0386 to +122.9781 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.55 | −12.1% | −2.8322 to −0.0732 | yes: GAIN |
| node-hours | 5.027 | 4.418 | −12.1% | −1.1864 to −0.0329 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 524.2 | +0.0% | −1.3860 to +1.3945 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 478.5 | −8.7% | −89.1721 to −2.0653 | yes: GAIN |
| response time (ms), mean | 454.4 | 445.7 | −1.9% | −40.4770 to +23.0807 | no |
| response time (ms), 95th percentile | 1735 | 1879 | +8.3% | −4.4525 to +292.0245 | no |
| response time (ms), 99th percentile | 2479 | 2777 | +12.0% | −23.8162 to +620.6412 | no |
| time over the response line (% of samples) | 17.45 | 17.67 | +1.3% | −1.4650 to +1.9099 | no |
| failed requests (%) | 0.01709 | 0 | −100.0% | −0.0558 to +0.0216 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 10.7 | +20.2% | −0.0407 to +3.6407 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.8 | +91.800 (native is 0) | +40.2231 to +143.3769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 12.58 | +9.2% | −1.4035 to +3.5135 | no |
| utilisation (used / allocatable) | 0.03264 | 0.03701 | +13.4% | +0.0006 to +0.0081 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.557 | −0.6% | −0.0602 to +0.0414 | no |
| Omni's own CPU (cores), mean | 0 | 0.01316 | +0.013 (native is 0) | +0.0120 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.57 | +0.2% | −0.0470 to +0.0546 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.8 | 742 | −9.2% | −135.7400 to −13.8884 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.102 | 4.268 | +4.0% | −0.1383 to +0.4701 | no |
| pods started | 0.4 | 0.3 | −25.0% | −1.0204 to +0.8204 | no |
| pod start wait, total (s) | 1.1 | 0.6 | −45.5% | −2.9140 to +1.9140 | no |
| pod start wait, mean (s) | 0.5 | 0.4 | −20.0% | −1.1900 to +0.9900 | no |
| host CPU busy, the real machine under kind (%) | 47.91 | 49.6 | +3.5% | +1.0823 to +2.2815 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.9 | 832.6 | +1.3% | −2.0292 to +23.4292 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.529 | −20.6% | −4.6933 to −0.2477 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.04167 | −37.5% | −0.1022 to +0.0522 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.1 | 141.3 | +9.5% | +2.0107 to +22.4060 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.55 | −12.1% | −2.8322 to −0.0732 | yes: GAIN |
| node-hours | 5.028 | 4.418 | −12.1% | −1.1856 to −0.0343 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 524.2 | −0.2% | −2.6899 to +0.6679 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 478.5 | −8.9% | −89.5578 to −3.7100 | yes: GAIN |
| response time (ms), mean | 605 | 445.7 | −26.3% | −251.4961 to −67.0271 | yes: GAIN |
| response time (ms), 95th percentile | 2827 | 1879 | −33.5% | −1635.0032 to −260.8048 | yes: GAIN |
| response time (ms), 99th percentile | 4053 | 2777 | −31.5% | −2218.2496 to −333.5260 | yes: GAIN |
| time over the response line (% of samples) | 19.1 | 17.67 | −7.5% | −2.3128 to −0.5433 | yes: GAIN |
| failed requests (%) | 0.04722 | 0 | −100.0% | −0.1115 to +0.0171 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.6 | 10.7 | −15.1% | −2.9900 to −0.8100 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.8 | +91.800 (native is 0) | +40.2231 to +143.3769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 12.58 | −20.7% | −6.4309 to −0.1524 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03402 | 0.03701 | +8.8% | −0.0015 to +0.0075 | no |
| CPU used (cores), mean | 1.633 | 1.557 | −4.6% | −0.1148 to −0.0363 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01316 | +0.013 (native is 0) | +0.0120 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.633 | 1.57 | −3.8% | −0.1020 to −0.0228 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.5 | 742 | −6.4% | −122.7761 to +21.7147 | no |
| HPA replicas, mean | 3.985 | 4.268 | +7.1% | +0.0860 to +0.4802 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 53.79 | 49.6 | −7.8% | −5.8157 to −2.5621 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 903.7 | 832.6 | −7.9% | −119.7975 to −22.4025 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.529 | −20.6% | −4.6933 to −0.2477 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.04167 | −88.8% | −0.4583 to −0.2001 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.4 | −63.6% | −1.1828 to −0.2172 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 205.1 | 141.3 | −31.1% | −105.2857 to −22.3143 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.61 | −11.6% | −2.6417 to −0.1368 | yes: GAIN |
| node-hours | 5.027 | 4.445 | −11.6% | −1.1037 to −0.0608 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 525.1 | +0.2% | −0.6717 to +2.6653 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 481.5 | −8.1% | −82.5722 to −2.8217 | yes: GAIN |
| response time (ms), mean | 454.4 | 663.9 | +46.1% | +49.6007 to +369.5180 | yes: LOSS |
| response time (ms), 95th percentile | 1735 | 3223 | +85.8% | +453.8719 to +2521.9121 | yes: LOSS |
| response time (ms), 99th percentile | 2479 | 4438 | +79.0% | +631.6048 to +3286.2680 | yes: LOSS |
| time over the response line (% of samples) | 17.45 | 21.16 | +21.3% | +1.5767 to +5.8524 | yes: LOSS |
| failed requests (%) | 0.01709 | 0.1236 | +622.8% | +0.0239 to +0.1890 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 13.4 | +50.6% | +2.3607 to +6.6393 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +18.0120 to +53.5880 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 22.44 | +94.7% | +1.6707 to +20.1527 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03264 | 0.03803 | +16.5% | +0.0025 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.619 | +3.4% | −0.0292 to +0.1346 | no |
| Omni's own CPU (cores), mean | 0 | 0.01049 | +0.010 (native is 0) | +0.0093 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.63 | +4.0% | −0.0193 to +0.1457 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.8 | 722.7 | −11.5% | −142.4834 to −45.8425 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.102 | 4.191 | +2.2% | −0.2483 to +0.4275 | no |
| pods started | 0.4 | 0.3 | −25.0% | −0.7263 to +0.5263 | no |
| pod start wait, total (s) | 1.1 | 0.4 | −63.6% | −2.6676 to +1.2676 | no |
| pod start wait, mean (s) | 0.5 | 0.4 | −20.0% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 47.91 | 56.5 | +17.9% | +5.7316 to +11.4293 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.9 | 944.2 | +14.9% | +39.5700 to +205.0300 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.546 | −20.4% | −4.5675 to −0.3403 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.6708 | +906.3% | +0.0478 to +1.1606 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.2 | +633.3% | −0.6558 to +4.4558 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.1 | 248.8 | +92.6% | +41.3468 to +197.8866 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*