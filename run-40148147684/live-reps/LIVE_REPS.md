# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.355 | 4.921 |
| node-hours | 2.515 | 2.514 | 2.245 | 2.062 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 | 272 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.3 | 251.8 | 238.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 321.1 | 232.6 | 285.1 | 205.7 |
| response time (ms), 95th percentile | 1069 | 572.9 | 1068 | 662.4 |
| response time (ms), 99th percentile | 1564 | 952.3 | 1563 | 1136 |
| time over the response line (% of samples) | 18.89 | 9.3 | 18.7 | 9.269 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | 9.5 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 31.5 | 41.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 13.97 | 10.56 | 14.62 |
| utilisation (used / allocatable) | 0.05888 | 0.06 | 0.06628 | 0.07311 |
| CPU used (cores), mean | 1.413 | 1.44 | 1.41 | 1.412 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01536 | 0.0185 |
| CPU used with Omni's own (cores), mean | 1.413 | 1.44 | 1.425 | 1.431 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 460.1 | 428.9 | 403.4 |
| HPA replicas, mean | 1.992 | 2.026 | 2.31 | 2.339 |
| pods started | 0.1 | 0.2 | 0.4 | 0.3 |
| pod start wait, total (s) | 0.2 | 0.5 | 0.8 | 1.1 |
| pod start wait, mean (s) | 0.2 | 0.25 | 0.8 | 1.1 |
| host CPU busy, the real machine under kind (%) | 40.3 | 41.39 | 41.1 | 42.31 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.3 | 780.2 | 766.7 | 781.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.944 | 4.151 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.675 | 0.05833 | 0.75 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | 0.3 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 72 | 92.75 | 74.23 | 94.74 |
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
| worker nodes in service, mean | 6 | 4.921 | −18.0% | −1.8694 to −0.2896 | yes: GAIN |
| node-hours | 2.514 | 2.062 | −18.0% | −0.7824 to −0.1208 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −0.8815 to +0.4792 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 238.2 | −12.5% | −59.0166 to −9.1773 | yes: GAIN |
| response time (ms), mean | 232.6 | 205.7 | −11.6% | −43.9745 to −9.8946 | yes: GAIN |
| response time (ms), 95th percentile | 572.9 | 662.4 | +15.6% | −19.5737 to +198.6537 | no |
| response time (ms), 99th percentile | 952.3 | 1136 | +19.3% | −71.7819 to +439.5761 | no |
| time over the response line (% of samples) | 9.3 | 9.269 | −0.3% | −1.7420 to +1.6801 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.2 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +30.9476 to +52.6524 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.97 | 14.62 | +4.7% | −1.1980 to +2.4980 | no |
| utilisation (used / allocatable) | 0.06 | 0.07311 | +21.9% | +0.0028 to +0.0235 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.44 | 1.412 | −1.9% | −0.0485 to −0.0068 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0185 | +0.018 (native is 0) | +0.0153 to +0.0217 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.431 | −0.6% | −0.0324 to +0.0141 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.1 | 403.4 | −12.3% | −104.0883 to −9.2627 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.339 | +15.5% | +0.0571 to +0.5700 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.5 | 1.1 | +120.0% | −1.5112 to +2.7112 | no |
| pod start wait, mean (s) | 0.25 | 1.1 | +340.0% | −0.9347 to +2.6347 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 42.31 | +2.2% | +0.6433 to +1.1964 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.2 | 781.4 | +0.2% | −3.7074 to +6.1074 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.151 | −30.8% | −3.0191 to −0.6790 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.675 | 0.75 | +11.1% | −0.0190 to +0.1690 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 | −7.7% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.75 | 94.74 | +2.1% | −4.1135 to +8.0885 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.514 | −0.0% | −0.0111 to +0.0094 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 | +0.1% | −0.6925 to +1.3099 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.3 | +0.1% | −0.6925 to +1.3099 | no |
| response time (ms), mean | 321.1 | 232.6 | −27.6% | −131.3276 to −45.6891 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 572.9 | −46.4% | −739.5821 to −252.9469 | yes: GAIN |
| response time (ms), 99th percentile | 1564 | 952.3 | −39.1% | −916.7569 to −307.0659 | yes: GAIN |
| time over the response line (% of samples) | 18.89 | 9.3 | −50.8% | −14.1755 to −4.9971 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | −4.2% | −1.3048 to +0.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 13.97 | +43.3% | +3.2086 to +5.2314 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05888 | 0.06 | +1.9% | +0.0003 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.413 | 1.44 | +1.9% | +0.0072 to +0.0463 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.413 | 1.44 | +1.9% | +0.0072 to +0.0463 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 460.1 | −2.0% | −19.0649 to +0.0521 | no |
| HPA replicas, mean | 1.992 | 2.026 | +1.7% | −0.0937 to +0.1604 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.2 | 0.25 | +25.0% | −0.0631 to +0.1631 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 41.39 | +2.7% | +0.5027 to +1.6784 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 780.2 | +2.2% | +6.8153 to +26.9847 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.675 | +980.0% | +0.5496 to +0.6754 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | +160.0% | +0.3476 to +1.2524 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72 | 92.75 | +28.8% | +8.6880 to +32.8036 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.355 | −10.8% | −1.4002 to +0.1098 | no |
| node-hours | 2.515 | 2.245 | −10.7% | −0.5873 to +0.0474 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272 | +0.0% | −1.1161 to +1.1187 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 251.8 | −7.4% | −44.3406 to +3.9016 | no |
| response time (ms), mean | 321.1 | 285.1 | −11.2% | −55.2947 to −16.8497 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 1068 | −0.2% | −114.2795 to +110.9695 | no |
| response time (ms), 99th percentile | 1564 | 1563 | −0.1% | −161.1155 to +158.4415 | no |
| time over the response line (% of samples) | 18.89 | 18.7 | −1.0% | −1.5084 to +1.1434 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.5 | −1.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +19.1507 to +43.8493 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 10.56 | +8.3% | −1.3491 to +2.9624 | no |
| utilisation (used / allocatable) | 0.05888 | 0.06628 | +12.6% | −0.0006 to +0.0154 | no |
| CPU used (cores), mean | 1.413 | 1.41 | −0.3% | −0.0337 to +0.0265 | no |
| Omni's own CPU (cores), mean | 0 | 0.01536 | +0.015 (native is 0) | +0.0137 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.425 | +0.8% | −0.0196 to +0.0431 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 428.9 | −8.7% | −84.4433 to +3.0611 | no |
| HPA replicas, mean | 1.992 | 2.31 | +16.0% | +0.1168 to +0.5191 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.5285 to +1.7285 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | −0.5285 to +1.7285 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 41.1 | +2.0% | +0.5426 to +1.0631 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 766.7 | +0.4% | −0.7736 to +7.5736 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.944 | −17.6% | −2.2228 to +0.1105 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05833 | −6.7% | −0.0557 to +0.0474 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 72 | 74.23 | +3.1% | −1.5918 to +6.0501 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.355 | −10.8% | −1.4002 to +0.1098 | no |
| node-hours | 2.514 | 2.245 | −10.7% | −0.5868 to +0.0486 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272 | −0.1% | −1.2737 to +0.6591 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 251.8 | −7.5% | −44.8387 to +3.7824 | no |
| response time (ms), mean | 232.6 | 285.1 | +22.5% | +19.2462 to +85.6262 | yes: LOSS |
| response time (ms), 95th percentile | 572.9 | 1068 | +86.3% | +284.2362 to +704.9828 | yes: LOSS |
| response time (ms), 99th percentile | 952.3 | 1563 | +64.1% | +344.8558 to +876.2930 | yes: LOSS |
| time over the response line (% of samples) | 9.3 | 18.7 | +101.1% | +4.8984 to +13.9092 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.5 | +3.3% | −0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.5 | +31.500 (native is 0) | +19.1507 to +43.8493 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.97 | 10.56 | −24.4% | −5.4742 to −1.3525 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06 | 0.06628 | +10.5% | −0.0016 to +0.0141 | no |
| CPU used (cores), mean | 1.44 | 1.41 | −2.1% | −0.0706 to +0.0099 | no |
| Omni's own CPU (cores), mean | 0 | 0.01536 | +0.015 (native is 0) | +0.0137 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.425 | −1.0% | −0.0565 to +0.0265 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.1 | 428.9 | −6.8% | −70.5608 to +8.1914 | no |
| HPA replicas, mean | 2.026 | 2.31 | +14.0% | +0.0807 to +0.4884 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.5 | 0.8 | +60.0% | −1.3189 to +1.9189 | no |
| pod start wait, mean (s) | 0.25 | 0.8 | +220.0% | −0.6475 to +1.7475 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 41.1 | −0.7% | −0.6429 to +0.0674 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.2 | 766.7 | −1.7% | −20.6868 to −6.3132 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.944 | −17.6% | −2.2228 to +0.1105 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.675 | 0.05833 | −91.4% | −0.7053 to −0.5280 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.3 | −76.9% | −1.4769 to −0.5231 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 92.75 | 74.23 | −20.0% | −28.0839 to −8.9494 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.921 | −18.0% | −1.8694 to −0.2896 | yes: GAIN |
| node-hours | 2.515 | 2.062 | −18.0% | −0.7846 to −0.1203 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 | +0.0% | −1.0444 to +1.2595 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 238.2 | −12.4% | −58.7661 to −8.8105 | yes: GAIN |
| response time (ms), mean | 321.1 | 205.7 | −35.9% | −160.5295 to −70.3564 | yes: GAIN |
| response time (ms), 95th percentile | 1069 | 662.4 | −38.0% | −616.3201 to −197.1289 | yes: GAIN |
| response time (ms), 99th percentile | 1564 | 1136 | −27.4% | −766.2637 to −89.7649 | yes: GAIN |
| time over the response line (% of samples) | 18.89 | 9.269 | −50.9% | −14.3913 to −4.8432 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | −4.2% | −1.3656 to +0.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +30.9476 to +52.6524 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 14.62 | +49.9% | +3.4466 to +6.2934 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05888 | 0.07311 | +24.2% | +0.0037 to +0.0247 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.413 | 1.412 | −0.1% | −0.0279 to +0.0260 | no |
| Omni's own CPU (cores), mean | 0 | 0.0185 | +0.018 (native is 0) | +0.0153 to +0.0217 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.431 | +1.2% | −0.0102 to +0.0454 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.6 | 403.4 | −14.1% | −118.2308 to −14.1331 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.992 | 2.339 | +17.4% | +0.0910 to +0.6029 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.8342 to +2.6342 | no |
| pod start wait, mean (s) | 0.2 | 1.1 | +450.0% | −0.8342 to +2.6342 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 42.31 | +5.0% | +1.5427 to +2.4782 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 781.4 | +2.4% | +9.1502 to +27.0498 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.151 | −30.8% | −3.0191 to −0.6790 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.75 | +1100.0% | +0.5784 to +0.7966 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.2 | +140.0% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72 | 94.74 | +31.6% | +11.2643 to +34.2023 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*