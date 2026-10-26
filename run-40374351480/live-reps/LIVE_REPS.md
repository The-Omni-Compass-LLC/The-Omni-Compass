# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.19 | 11.43 |
| node-hours | 5.035 | 5.032 | 4.693 | 4.776 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 527 | 525.9 | 525.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 527 | 500.5 | 507.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 539.7 | 730.6 | 522.5 | 788.9 |
| response time (ms), 95th percentile | 2110 | 3626 | 2299 | 3886 |
| response time (ms), 99th percentile | 3035 | 5135 | 3382 | 5514 |
| time over the response line (% of samples) | 23.14 | 25.14 | 22.66 | 26.33 |
| failed requests (%) | 0 | 0.03507 | 0 | 0.1342 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 15.9 | 11.9 | 16.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 68 | 31.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.66 | 18.11 | 14.32 | 29.42 |
| utilisation (used / allocatable) | 0.03404 | 0.03584 | 0.03668 | 0.03796 |
| CPU used (cores), mean | 1.634 | 1.72 | 1.645 | 1.741 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01313 | 0.00999 |
| CPU used with Omni's own (cores), mean | 1.634 | 1.72 | 1.658 | 1.751 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.5 | 745.8 | 731.8 | 707.8 |
| HPA replicas, mean | 4.184 | 3.997 | 4.259 | 4.408 |
| pods started | 0.1 | 0.3 | 1 | 0.6 |
| pod start wait, total (s) | 0.4 | 0.5 | 1.7 | 1.6 |
| pod start wait, mean (s) | 0.4 | 0.3 | 0.9333 | 1.067 |
| host CPU busy, the real machine under kind (%) | 49.94 | 56.51 | 51.49 | 59.34 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 841.8 | 950.6 | 852.2 | 992.7 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.55 | 10.87 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.4292 | 0.0625 | 1.808 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.2 | 0.4 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 153.8 | 252.9 | 161.3 | 300.7 |
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
| worker nodes in service, mean | 12 | 11.43 | −4.8% | −1.2988 to +0.1492 | no |
| node-hours | 5.032 | 4.776 | −5.1% | −0.5633 to +0.0511 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 525.6 | −0.3% | −2.7100 to −0.0201 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 507.6 | −3.7% | −42.6065 to +3.8598 | no |
| response time (ms), mean | 730.6 | 788.9 | +8.0% | −37.4959 to +154.1380 | no |
| response time (ms), 95th percentile | 3626 | 3886 | +7.2% | −252.0850 to +772.0870 | no |
| response time (ms), 99th percentile | 5135 | 5514 | +7.4% | −123.6527 to +881.7323 | no |
| time over the response line (% of samples) | 25.14 | 26.33 | +4.7% | −0.1863 to +2.5638 | no |
| failed requests (%) | 0.03507 | 0.1342 | +282.6% | −0.0119 to +0.2101 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.9 | 16.6 | +4.4% | +0.2172 to +1.1828 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 | +31.300 (native is 0) | +25.7999 to +36.8001 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.11 | 29.42 | +62.5% | −0.8940 to +23.5273 | no |
| utilisation (used / allocatable) | 0.03584 | 0.03796 | +5.9% | −0.0006 to +0.0049 | no |
| CPU used (cores), mean | 1.72 | 1.741 | +1.2% | −0.0656 to +0.1065 | no |
| Omni's own CPU (cores), mean | 0 | 0.00999 | +0.010 (native is 0) | +0.0093 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.72 | 1.751 | +1.8% | −0.0558 to +0.1167 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 707.8 | −5.1% | −87.2506 to +11.2536 | no |
| HPA replicas, mean | 3.997 | 4.408 | +10.3% | +0.1714 to +0.6503 | yes: power given |
| pods started | 0.3 | 0.6 | +100.0% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 0.5 | 1.6 | +220.0% | −0.6986 to +2.8986 | no |
| pod start wait, mean (s) | 0.3 | 1.067 | +255.6% | +0.0039 to +1.5294 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.51 | 59.34 | +5.0% | +1.5720 to +4.0800 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 950.6 | 992.7 | +4.4% | +14.2317 to +69.9683 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.87 | −9.4% | −2.4941 to +0.2411 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4292 | 1.808 | +321.4% | −1.6693 to +4.4276 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 252.9 | 300.7 | +18.9% | +16.8269 to +78.8898 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.035 | 5.032 | −0.1% | −0.0171 to +0.0097 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 527 | +0.2% | −0.4454 to +2.2160 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 527 | +0.2% | −0.4454 to +2.2160 | no |
| response time (ms), mean | 539.7 | 730.6 | +35.4% | +96.9691 to +284.7251 | yes: LOSS |
| response time (ms), 95th percentile | 2110 | 3626 | +71.9% | +737.2084 to +2294.6406 | yes: LOSS |
| response time (ms), 99th percentile | 3035 | 5135 | +69.2% | +1128.1497 to +3071.6409 | yes: LOSS |
| time over the response line (% of samples) | 23.14 | 25.14 | +8.7% | −0.9023 to +4.9101 | no |
| failed requests (%) | 0 | 0.03507 | +0.035 (native is 0) | −0.0075 to +0.0777 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 15.9 | +39.5% | +2.2317 to +6.7683 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.66 | 18.11 | +32.5% | +1.4693 to +7.4141 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03404 | 0.03584 | +5.3% | +0.0009 to +0.0027 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.634 | 1.72 | +5.3% | +0.0411 to +0.1320 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.634 | 1.72 | +5.3% | +0.0411 to +0.1320 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.5 | 745.8 | −4.3% | −49.3404 to −18.0548 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.184 | 3.997 | −4.5% | −0.4326 to +0.0577 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −1.2676 to +1.4676 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −1.1900 to +0.9900 | no |
| host CPU busy, the real machine under kind (%) | 49.94 | 56.51 | +13.2% | +4.9084 to +8.2422 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841.8 | 950.6 | +12.9% | +58.2192 to +159.3808 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.4292 | +505.9% | +0.2458 to +0.4709 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.2 | +100.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 153.8 | 252.9 | +64.4% | +56.9898 to +141.0436 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.19 | −6.7% | −1.7212 to +0.1041 | no |
| node-hours | 5.035 | 4.693 | −6.8% | −0.7247 to +0.0395 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 525.9 | −0.0% | −1.3495 to +1.0745 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 500.5 | −4.9% | −54.5123 to +3.2456 | no |
| response time (ms), mean | 539.7 | 522.5 | −3.2% | −34.7421 to +0.3612 | no |
| response time (ms), 95th percentile | 2110 | 2299 | +9.0% | +47.0131 to +331.5459 | yes: LOSS |
| response time (ms), 99th percentile | 3035 | 3382 | +11.4% | +149.3258 to +545.1278 | yes: LOSS |
| time over the response line (% of samples) | 23.14 | 22.66 | −2.0% | −1.3232 to +0.3784 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 11.9 | +4.4% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68 | +68.000 (native is 0) | +25.8070 to +110.1930 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.66 | 14.31 | +4.8% | −1.1257 to +2.4291 | no |
| utilisation (used / allocatable) | 0.03404 | 0.03668 | +7.8% | +0.0003 to +0.0050 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.634 | 1.645 | +0.7% | −0.0151 to +0.0383 | no |
| Omni's own CPU (cores), mean | 0 | 0.01313 | +0.013 (native is 0) | +0.0121 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.634 | 1.658 | +1.5% | −0.0013 to +0.0507 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.5 | 731.8 | −6.1% | −90.7606 to −4.6161 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.184 | 4.259 | +1.8% | −0.2965 to +0.4469 | no |
| pods started | 0.1 | 1 | +900.0% | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0.4 | 1.7 | +325.0% | −0.7246 to +3.3246 | no |
| pod start wait, mean (s) | 0.4 | 0.9333 | +133.3% | −0.7529 to +1.8196 | no |
| host CPU busy, the real machine under kind (%) | 49.94 | 51.49 | +3.1% | +0.9678 to +2.1308 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841.8 | 852.2 | +1.2% | −1.8844 to +22.6844 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.55 | −12.1% | −2.9891 to +0.0822 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | −11.8% | −0.0586 to +0.0419 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 153.8 | 161.3 | +4.8% | −0.1487 to +15.0654 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.19 | −6.7% | −1.7212 to +0.1041 | no |
| node-hours | 5.032 | 4.693 | −6.7% | −0.7196 to +0.0417 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 525.9 | −0.2% | −2.7192 to +0.6736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 500.5 | −5.0% | −54.8235 to +1.7862 | no |
| response time (ms), mean | 730.6 | 522.5 | −28.5% | −300.9942 to −115.0811 | yes: GAIN |
| response time (ms), 95th percentile | 3626 | 2299 | −36.6% | −2054.4352 to −598.8548 | yes: GAIN |
| response time (ms), 99th percentile | 5135 | 3382 | −34.1% | −2583.1874 to −922.1496 | yes: GAIN |
| time over the response line (% of samples) | 25.14 | 22.66 | −9.8% | −4.9391 to −0.0136 | yes: GAIN |
| failed requests (%) | 0.03507 | 0 | −100.0% | −0.0777 to +0.0075 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.9 | 11.9 | −25.2% | −6.0786 to −1.9214 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68 | +68.000 (native is 0) | +25.8070 to +110.1930 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.11 | 14.31 | −20.9% | −6.0698 to −1.5102 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03584 | 0.03668 | +2.4% | −0.0020 to +0.0037 | no |
| CPU used (cores), mean | 1.72 | 1.645 | −4.4% | −0.1147 to −0.0352 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01313 | +0.013 (native is 0) | +0.0121 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.72 | 1.658 | −3.6% | −0.1014 to −0.0222 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 731.8 | −1.9% | −61.5969 to +33.6153 | no |
| HPA replicas, mean | 3.997 | 4.259 | +6.6% | −0.0710 to +0.5964 | no |
| pods started | 0.3 | 1 | +233.3% | −0.2567 to +1.6567 | no |
| pod start wait, total (s) | 0.5 | 1.7 | +240.0% | −0.7892 to +3.1892 | no |
| pod start wait, mean (s) | 0.3 | 0.9333 | +211.1% | −0.2567 to +1.5234 | no |
| host CPU busy, the real machine under kind (%) | 56.51 | 51.49 | −8.9% | −6.6186 to −3.4334 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 950.6 | 852.2 | −10.4% | −144.4202 to −52.3798 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.55 | −12.1% | −2.9891 to +0.0822 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4292 | 0.0625 | −85.4% | −0.4840 to −0.2493 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.4 | −66.7% | −1.1016 to −0.4984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 252.9 | 161.3 | −36.2% | −130.8875 to −52.2292 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.43 | −4.8% | −1.2988 to +0.1492 | no |
| node-hours | 5.035 | 4.776 | −5.2% | −0.5680 to +0.0484 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 525.6 | −0.1% | −2.3932 to +1.4337 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 507.6 | −3.5% | −42.2929 to +5.3167 | no |
| response time (ms), mean | 539.7 | 788.9 | +46.2% | +111.2767 to +387.0597 | yes: LOSS |
| response time (ms), 95th percentile | 2110 | 3886 | +84.2% | +921.8625 to +2629.9885 | yes: LOSS |
| response time (ms), 99th percentile | 3035 | 5514 | +81.7% | +1374.7400 to +3583.1302 | yes: LOSS |
| time over the response line (% of samples) | 23.14 | 26.33 | +13.8% | +0.7773 to +5.6080 | yes: LOSS |
| failed requests (%) | 0 | 0.1342 | +0.134 (native is 0) | +0.0031 to +0.2653 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 16.6 | +45.6% | +3.2396 to +7.1604 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 | +31.300 (native is 0) | +25.7999 to +36.8001 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.66 | 29.42 | +115.3% | +2.0203 to +29.4964 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03404 | 0.03796 | +11.5% | +0.0016 to +0.0062 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.634 | 1.741 | +6.5% | +0.0249 to +0.1891 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00999 | +0.010 (native is 0) | +0.0093 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.634 | 1.751 | +7.2% | +0.0345 to +0.1995 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.5 | 707.8 | −9.2% | −115.6466 to −27.7455 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.184 | 4.408 | +5.3% | −0.0244 to +0.4711 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.1952 to +1.1952 | no |
| pod start wait, total (s) | 0.4 | 1.6 | +300.0% | −0.8456 to +3.2456 | no |
| pod start wait, mean (s) | 0.4 | 1.067 | +166.7% | −0.5646 to +1.8979 | no |
| host CPU busy, the real machine under kind (%) | 49.94 | 59.34 | +18.8% | +6.9307 to +11.8718 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841.8 | 992.7 | +17.9% | +80.1730 to +221.6270 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.87 | −9.4% | −2.4941 to +0.2411 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1.808 | +2452.9% | −1.3569 to +4.8319 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.2 | +100.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 153.8 | 300.7 | +95.5% | +81.6296 to +212.1204 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*