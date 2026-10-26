# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.458 | 4.509 |
| node-hours | 2.518 | 2.51 | 1.868 | 1.891 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 269.6 | 270.4 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 269.6 | 221.9 | 223.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 227.5 | 234.7 | 202.9 | 213.3 |
| response time (ms), 95th percentile | 707.5 | 738.6 | 742.3 | 806.2 |
| response time (ms), 99th percentile | 1052 | 1079 | 1063 | 1172 |
| time over the response line (% of samples) | 9.53 | 9.781 | 9.877 | 10.19 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 5.6 | 5.7 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38.6 | 61.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.302 | 7.372 | 9.217 | 7.767 |
| utilisation (used / allocatable) | 0.05397 | 0.05383 | 0.07412 | 0.07179 |
| CPU used (cores), mean | 1.295 | 1.292 | 1.299 | 1.277 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01497 | 0.01662 |
| CPU used with Omni's own (cores), mean | 1.295 | 1.292 | 1.314 | 1.294 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.5 | 513.9 | 408.1 | 418.9 |
| HPA replicas, mean | 2.007 | 1.965 | 1.935 | 2.076 |
| pods started | 0 | 0 | 0.1 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 0.1 | 0.2 |
| pod start wait, mean (s) | 0 | 0 | 0.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 37.09 | 37.96 | 38.12 | 38.69 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 747.9 | 751.3 | 748.5 | 754.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.434 | 3.523 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1542 | 0.04583 | 0.1625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | 0.2 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 54.09 | 58.19 | 56.08 | 60.7 |
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
| worker nodes in service, mean | 6 | 4.509 | −24.8% | −2.3129 to −0.6688 | yes: GAIN |
| node-hours | 2.51 | 1.891 | −24.7% | −0.9656 to −0.2720 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 270.3 | +0.2% | −0.3581 to +1.6597 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 223.4 | −17.1% | −72.3232 to −20.0502 | yes: GAIN |
| response time (ms), mean | 234.7 | 213.3 | −9.1% | −28.5174 to −14.3326 | yes: GAIN |
| response time (ms), 95th percentile | 738.6 | 806.2 | +9.1% | +21.1780 to +113.9080 | yes: LOSS |
| response time (ms), 99th percentile | 1079 | 1172 | +8.6% | −11.5993 to +197.2707 | no |
| time over the response line (% of samples) | 9.781 | 10.19 | +4.2% | −0.1025 to +0.9306 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 6.1 | +8.9% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.1 | +61.100 (native is 0) | +33.9634 to +88.2366 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.372 | 7.767 | +5.4% | −1.1075 to +1.8975 | no |
| utilisation (used / allocatable) | 0.05383 | 0.07179 | +33.4% | +0.0077 to +0.0282 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.292 | 1.277 | −1.1% | −0.0471 to +0.0175 | no |
| Omni's own CPU (cores), mean | 0 | 0.01662 | +0.017 (native is 0) | +0.0147 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.292 | 1.294 | +0.1% | −0.0306 to +0.0343 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 513.9 | 418.9 | −18.5% | −153.2455 to −36.8477 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.965 | 2.076 | +5.6% | −0.0680 to +0.2897 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 37.96 | 38.69 | +1.9% | +0.4066 to +1.0597 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.3 | 754.3 | +0.4% | −0.8888 to +6.8888 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.523 | −41.3% | −3.7720 to −1.1826 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.1625 | +5.4% | −0.0457 to +0.0624 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.19 | 60.7 | +4.3% | −0.0599 to +5.0849 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.51 | −0.3% | −0.0179 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 269.6 | −0.3% | −2.0572 to +0.1825 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 269.6 | −0.3% | −2.0572 to +0.1825 | no |
| response time (ms), mean | 227.5 | 234.7 | +3.1% | +1.3922 to +12.9145 | yes: LOSS |
| response time (ms), 95th percentile | 707.5 | 738.6 | +4.4% | +0.3519 to +62.0001 | yes: LOSS |
| response time (ms), 99th percentile | 1052 | 1079 | +2.6% | −73.4435 to +127.4183 | no |
| time over the response line (% of samples) | 9.53 | 9.781 | +2.6% | −0.2686 to +0.7694 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 5.6 | −6.7% | −1.2396 to +0.4396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.302 | 7.372 | −20.7% | −2.8599 to −1.0001 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05397 | 0.05383 | −0.3% | −0.0013 to +0.0010 | no |
| CPU used (cores), mean | 1.295 | 1.292 | −0.3% | −0.0315 to +0.0247 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.295 | 1.292 | −0.3% | −0.0315 to +0.0247 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.5 | 513.9 | +0.9% | −9.4983 to +18.3085 | no |
| HPA replicas, mean | 2.007 | 1.965 | −2.1% | −0.2435 to +0.1606 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 37.09 | 37.96 | +2.3% | +0.6300 to +1.0997 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 747.9 | 751.3 | +0.5% | −1.4772 to +8.2772 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1542 | +362.5% | +0.0500 to +0.1917 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 54.09 | 58.19 | +7.6% | +0.4944 to +7.7139 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.458 | −25.7% | −2.3251 to −0.7586 | yes: GAIN |
| node-hours | 2.518 | 1.868 | −25.8% | −0.9732 to −0.3266 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.4 | −0.0% | −1.1646 to +0.9128 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 221.9 | −18.0% | −72.6794 to −24.5849 | yes: GAIN |
| response time (ms), mean | 227.5 | 202.9 | −10.8% | −36.7030 to −12.5882 | yes: GAIN |
| response time (ms), 95th percentile | 707.5 | 742.3 | +4.9% | +0.9695 to +68.6725 | yes: LOSS |
| response time (ms), 99th percentile | 1052 | 1063 | +1.0% | −128.9695 to +150.6719 | no |
| time over the response line (% of samples) | 9.53 | 9.877 | +3.6% | −0.6286 to +1.3218 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 5.7 | −5.0% | −1.5181 to +0.9181 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.6 | +38.600 (native is 0) | +25.6006 to +51.5994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.302 | 9.217 | −0.9% | −1.8454 to +1.6754 | no |
| utilisation (used / allocatable) | 0.05397 | 0.07412 | +37.3% | +0.0094 to +0.0309 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.295 | 1.299 | +0.3% | −0.0270 to +0.0342 | no |
| Omni's own CPU (cores), mean | 0 | 0.01497 | +0.015 (native is 0) | +0.0129 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.295 | 1.314 | +1.4% | −0.0111 to +0.0481 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.5 | 408.1 | −19.9% | −157.4450 to −45.3367 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 1.935 | −3.6% | −0.3108 to +0.1670 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 37.09 | 38.12 | +2.8% | +0.6889 to +1.3723 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 747.9 | 748.5 | +0.1% | −1.9503 to +3.1503 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.434 | −42.8% | −3.7644 to −1.3682 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.04583 | +37.5% | −0.0158 to +0.0408 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 54.09 | 56.07 | +3.7% | −0.2337 to +4.2087 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.458 | −25.7% | −2.3251 to −0.7586 | yes: GAIN |
| node-hours | 2.51 | 1.868 | −25.6% | −0.9686 to −0.3149 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 270.4 | +0.3% | −0.5521 to +2.1750 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 221.9 | −17.7% | −71.9334 to −23.4562 | yes: GAIN |
| response time (ms), mean | 234.7 | 202.9 | −13.5% | −46.4398 to −17.1581 | yes: GAIN |
| response time (ms), 95th percentile | 738.6 | 742.3 | +0.5% | −45.9620 to +53.2520 | no |
| response time (ms), 99th percentile | 1079 | 1063 | −1.5% | −103.3308 to +71.0584 | no |
| time over the response line (% of samples) | 9.781 | 9.877 | +1.0% | −0.5369 to +0.7292 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 5.7 | +1.8% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.6 | +38.600 (native is 0) | +25.6006 to +51.5994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.372 | 9.217 | +25.0% | +0.1179 to +3.5721 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05383 | 0.07412 | +37.7% | +0.0088 to +0.0318 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.292 | 1.299 | +0.5% | −0.0411 to +0.0551 | no |
| Omni's own CPU (cores), mean | 0 | 0.01497 | +0.015 (native is 0) | +0.0129 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.292 | 1.314 | +1.7% | −0.0249 to +0.0688 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 513.9 | 408.1 | −20.6% | −171.9078 to −39.6840 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.965 | 1.935 | −1.5% | −0.2179 to +0.1570 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 37.96 | 38.12 | +0.4% | −0.0750 to +0.4065 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.3 | 748.5 | −0.4% | −5.6573 to +0.0573 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.434 | −42.8% | −3.7644 to −1.3682 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.04583 | −70.3% | −0.1789 to −0.0378 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.2 | −66.7% | −0.7694 to −0.0306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 58.19 | 56.08 | −3.6% | −5.0309 to +0.7975 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.509 | −24.8% | −2.3129 to −0.6688 | yes: GAIN |
| node-hours | 2.518 | 1.891 | −24.9% | −0.9701 to −0.2839 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.3 | −0.1% | −1.7930 to +1.2198 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 223.4 | −17.4% | −73.0709 to −21.1773 | yes: GAIN |
| response time (ms), mean | 227.5 | 213.3 | −6.3% | −23.1610 to −5.3823 | yes: GAIN |
| response time (ms), 95th percentile | 707.5 | 806.2 | +14.0% | +31.4458 to +165.9922 | yes: LOSS |
| response time (ms), 99th percentile | 1052 | 1172 | +11.4% | +38.5763 to +201.0699 | yes: LOSS |
| time over the response line (% of samples) | 9.53 | 10.19 | +7.0% | −0.2985 to +1.6275 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.1 | +1.7% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.1 | +61.100 (native is 0) | +33.9634 to +88.2366 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.302 | 7.767 | −16.5% | −3.0710 to +0.0010 | no |
| utilisation (used / allocatable) | 0.05397 | 0.07179 | +33.0% | +0.0082 to +0.0275 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.295 | 1.277 | −1.4% | −0.0541 to +0.0177 | no |
| Omni's own CPU (cores), mean | 0 | 0.01662 | +0.017 (native is 0) | +0.0147 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.295 | 1.294 | −0.1% | −0.0383 to +0.0352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.5 | 418.9 | −17.8% | −140.5635 to −40.7194 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 2.076 | +3.5% | −0.1845 to +0.3232 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 37.09 | 38.69 | +4.3% | +1.1843 to +2.0117 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 747.9 | 754.3 | +0.9% | −1.0734 to +13.8734 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.523 | −41.3% | −3.7720 to −1.1826 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1625 | +387.5% | +0.0491 to +0.2092 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.8 | +300.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 54.09 | 60.7 | +12.2% | +0.6067 to +12.6266 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*