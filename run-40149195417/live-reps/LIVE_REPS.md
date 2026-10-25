# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.533 | 5.618 |
| node-hours | 2.515 | 2.519 | 2.319 | 2.355 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 | 272.9 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273 | 258.2 | 260.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 347.5 | 332.8 | 315.9 | 292.2 |
| response time (ms), 95th percentile | 1153 | 1221 | 1209 | 1290 |
| response time (ms), 99th percentile | 1590 | 1901 | 1796 | 1999 |
| time over the response line (% of samples) | 21.41 | 15.61 | 21.06 | 15.56 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.5 | 11.1 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 32.6 | 37.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.15 | 10.83 | 11.52 | 12.31 |
| utilisation (used / allocatable) | 0.06139 | 0.06026 | 0.0669 | 0.06562 |
| CPU used (cores), mean | 1.473 | 1.446 | 1.475 | 1.456 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01719 | 0.01702 |
| CPU used with Omni's own (cores), mean | 1.473 | 1.446 | 1.492 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 453.2 | 418.9 | 428 |
| HPA replicas, mean | 1.99 | 2.041 | 2.539 | 2.5 |
| pods started | 0 | 0.1 | 0.4 | 0.8 |
| pod start wait, total (s) | 0 | 0.2 | 1.6 | 1.3 |
| pod start wait, mean (s) | 0 | 0.2 | 1.6 | 1.05 |
| host CPU busy, the real machine under kind (%) | 41.95 | 41.59 | 43.11 | 42.72 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 768.2 | 763.1 | 774.1 | 769 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.098 | 5.302 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.07083 | 0.07083 | 0.1083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | 0.6 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 76.53 | 74.48 | 81.1 | 79.31 |
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
| worker nodes in service, mean | 6 | 5.618 | −6.4% | −0.9159 to +0.1523 | no |
| node-hours | 2.519 | 2.355 | −6.5% | −0.3878 to +0.0603 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | −0.1% | −1.0660 to +0.6727 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 260.8 | −4.5% | −28.9492 to +4.4685 | no |
| response time (ms), mean | 332.8 | 292.2 | −12.2% | −75.2667 to −5.9472 | yes: GAIN |
| response time (ms), 95th percentile | 1221 | 1290 | +5.6% | −115.1771 to +252.8671 | no |
| response time (ms), 99th percentile | 1901 | 1999 | +5.2% | −76.0050 to +272.3920 | no |
| time over the response line (% of samples) | 15.61 | 15.56 | −0.3% | −1.9361 to +1.8400 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.6 | +1.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 | +37.700 (native is 0) | +28.7782 to +46.6218 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 12.31 | +13.6% | +0.2431 to +2.7136 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06026 | 0.06562 | +8.9% | −0.0021 to +0.0128 | no |
| CPU used (cores), mean | 1.446 | 1.456 | +0.6% | −0.0055 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.0155 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.473 | +1.8% | +0.0121 to +0.0407 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 428 | −5.6% | −59.0560 to +8.6712 | no |
| HPA replicas, mean | 2.041 | 2.5 | +22.5% | +0.2195 to +0.6995 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | +0.2172 to +1.1828 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | +0.0100 to +2.1900 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.05 | +425.0% | +0.2180 to +1.4820 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.59 | 42.72 | +2.7% | +0.7619 to +1.4892 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.1 | 769 | +0.8% | +0.2129 to +11.5871 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.302 | −11.6% | −1.6061 to +0.2106 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.1083 | +52.9% | −0.0008 to +0.0758 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.48 | 79.31 | +6.5% | −0.0448 to +9.7115 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.519 | +0.1% | −0.0038 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 | +0.0% | −0.7199 to +0.8571 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273 | +0.0% | −0.7199 to +0.8571 | no |
| response time (ms), mean | 347.5 | 332.8 | −4.2% | −48.7023 to +19.2883 | no |
| response time (ms), 95th percentile | 1153 | 1221 | +5.9% | −128.7557 to +264.4887 | no |
| response time (ms), 99th percentile | 1590 | 1901 | +19.6% | +44.1790 to +577.7718 | yes: LOSS |
| time over the response line (% of samples) | 21.41 | 15.61 | −27.1% | −8.4154 to −3.2019 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.5 | −3.7% | −1.0032 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.15 | 10.83 | +6.7% | −1.2536 to +2.6169 | no |
| utilisation (used / allocatable) | 0.06139 | 0.06026 | −1.9% | −0.0016 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.473 | 1.446 | −1.9% | −0.0374 to −0.0172 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.473 | 1.446 | −1.9% | −0.0374 to −0.0172 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 453.2 | +1.7% | +5.1039 to +10.2202 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.041 | +2.6% | −0.0443 to +0.1464 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 41.95 | 41.59 | −0.9% | −0.7374 to +0.0131 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 768.2 | 763.1 | −0.7% | −10.7671 to +0.5671 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.07083 | +21.4% | −0.0191 to +0.0441 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.53 | 74.48 | −2.7% | −6.6518 to +2.5602 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.533 | −7.8% | −1.0004 to +0.0657 | no |
| node-hours | 2.515 | 2.319 | −7.8% | −0.4210 to +0.0281 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −1.0247 to +0.9362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 258.2 | −5.4% | −31.9248 to +2.4738 | no |
| response time (ms), mean | 347.5 | 315.9 | −9.1% | −50.4505 to −12.7749 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 1209 | +4.9% | −62.3847 to +174.5717 | no |
| response time (ms), 99th percentile | 1590 | 1796 | +13.0% | +16.7207 to +396.2027 | yes: LOSS |
| time over the response line (% of samples) | 21.41 | 21.06 | −1.7% | −1.2514 to +0.5347 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.1 | +1.8% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 | +32.600 (native is 0) | +22.8901 to +42.3099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.15 | 11.52 | +13.4% | −0.6028 to +3.3328 | no |
| utilisation (used / allocatable) | 0.06139 | 0.0669 | +9.0% | +0.0001 to +0.0109 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.473 | 1.475 | +0.1% | −0.0276 to +0.0306 | no |
| Omni's own CPU (cores), mean | 0 | 0.01719 | +0.017 (native is 0) | +0.0162 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.473 | 1.492 | +1.3% | −0.0102 to +0.0476 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 418.9 | −6.0% | −52.2720 to −1.0245 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.539 | +27.6% | +0.2780 to +0.8197 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | −0.0242 to +3.2242 | no |
| pod start wait, mean (s) | 0 | 1.6 | +1.600 (native is 0) | −0.0242 to +3.2242 | no |
| host CPU busy, the real machine under kind (%) | 41.95 | 43.11 | +2.8% | +0.7967 to +1.5149 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 768.2 | 774.1 | +0.8% | +0.0552 to +11.7448 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.098 | −15.0% | −1.9124 to +0.1089 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.07083 | +21.4% | −0.0191 to +0.0441 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.53 | 81.1 | +6.0% | −0.6182 to +9.7682 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.533 | −7.8% | −1.0004 to +0.0657 | no |
| node-hours | 2.519 | 2.319 | −7.9% | −0.4262 to +0.0263 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −1.1975 to +0.9718 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 258.2 | −5.4% | −32.2833 to +2.6952 | no |
| response time (ms), mean | 332.8 | 315.9 | −5.1% | −45.2294 to +11.4180 | no |
| response time (ms), 95th percentile | 1221 | 1209 | −1.0% | −173.7740 to +150.2280 | no |
| response time (ms), 99th percentile | 1901 | 1796 | −5.5% | −287.8056 to +78.7782 | no |
| time over the response line (% of samples) | 15.61 | 21.06 | +34.9% | +3.2133 to +7.6873 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 11.1 | +5.7% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 | +32.600 (native is 0) | +22.8901 to +42.3099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 11.52 | +6.3% | −0.5029 to +1.8695 | no |
| utilisation (used / allocatable) | 0.06026 | 0.0669 | +11.0% | +0.0013 to +0.0119 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.475 | +2.0% | −0.0065 to +0.0640 | no |
| Omni's own CPU (cores), mean | 0 | 0.01719 | +0.017 (native is 0) | +0.0162 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.492 | +3.2% | +0.0108 to +0.0812 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 418.9 | −7.6% | −60.0298 to −8.5908 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.041 | 2.539 | +24.4% | +0.2696 to +0.7260 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 1.6 | +700.0% | −0.3907 to +3.1907 | no |
| pod start wait, mean (s) | 0.2 | 1.6 | +700.0% | −0.3907 to +3.1907 | no |
| host CPU busy, the real machine under kind (%) | 41.59 | 43.11 | +3.6% | +1.0056 to +2.0302 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.1 | 774.1 | +1.4% | +1.9835 to +20.0165 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.098 | −15.0% | −1.9124 to +0.1089 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.07083 | ±0.0% | −0.0281 to +0.0281 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.48 | 81.1 | +8.9% | +0.2354 to +13.0062 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.618 | −6.4% | −0.9159 to +0.1523 | no |
| node-hours | 2.515 | 2.355 | −6.4% | −0.3833 to +0.0628 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | −0.0% | −0.7018 to +0.4457 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 260.8 | −4.5% | −28.7557 to +4.4122 | no |
| response time (ms), mean | 347.5 | 292.2 | −15.9% | −73.5957 to −37.0322 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 1290 | +11.9% | +20.8644 to +252.5586 | yes: LOSS |
| response time (ms), 99th percentile | 1590 | 1999 | +25.7% | +188.1940 to +630.1438 | yes: LOSS |
| time over the response line (% of samples) | 21.41 | 15.56 | −27.4% | −8.2138 to −3.4996 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.6 | −2.8% | −0.8889 to +0.2889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 | +37.700 (native is 0) | +28.7782 to +46.6218 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.15 | 12.31 | +21.3% | +0.6962 to +3.6238 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06139 | 0.06562 | +6.9% | −0.0033 to +0.0118 | no |
| CPU used (cores), mean | 1.473 | 1.456 | −1.2% | −0.0353 to −0.0005 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.0155 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.473 | 1.473 | −0.1% | −0.0174 to +0.0157 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 428 | −3.9% | −51.5194 to +16.4588 | no |
| HPA replicas, mean | 1.99 | 2.5 | +25.7% | +0.2963 to +0.7247 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.3476 to +1.2524 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.2310 to +2.3690 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.05 | +1.050 (native is 0) | +0.4091 to +1.6909 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.95 | 42.72 | +1.8% | +0.4694 to +1.0574 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 768.2 | 769 | +0.1% | −3.4626 to +5.0626 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.302 | −11.6% | −1.6061 to +0.2106 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1083 | +85.7% | +0.0083 to +0.0917 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.53 | 79.31 | +3.6% | −0.8086 to +6.3836 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*