# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.015 | 5.962 |
| node-hours | 2.516 | 2.512 | 2.101 | 2.5 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.9 | 270.9 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.9 | 240 | 270.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 268.8 | 140.5 | 230 | 103.9 |
| response time (ms), 95th percentile | 819 | 229.9 | 826.2 | 223.5 |
| response time (ms), 99th percentile | 1186 | 329 | 1224 | 326.5 |
| time over the response line (% of samples) | 12.9 | 0.1309 | 13.19 | 0.1188 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0 | 8.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 37.4 | 12.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.613 | 1028 | 8.788 | 1033 |
| utilisation (used / allocatable) | 0.05572 | 0.06003 | 0.0675 | 0.05924 |
| CPU used (cores), mean | 1.337 | 1.441 | 1.341 | 1.413 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01544 | 0.01182 |
| CPU used with Omni's own (cores), mean | 1.337 | 1.441 | 1.356 | 1.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.8 | 451.5 | 428 | 457.3 |
| HPA replicas, mean | 1.938 | 2.093 | 2.146 | 1.975 |
| pods started | 0.1 | 0.1 | 0.4 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.1 | 1 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.1 | 1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.39 | 44.21 | 39.19 | 44.18 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 744.7 | 1425 | 746 | 1448 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.203 | 5.65 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 135.4 | 0.04583 | 147.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 570.1 | 0.2 | 680.8 |
| queue: job turnaround, submitted to done, mean (s) | 53.67 | 786.3 | 53.64 | 763.3 |
| queue: jobs unfinished at the window's end | 0 | 7.9 | 0 | 8.4 |

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
| worker nodes in service, mean | 6 | 5.962 | −0.6% | −0.1228 to +0.0475 | no |
| node-hours | 2.512 | 2.5 | −0.4% | −0.0514 to +0.0290 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.9 | +0.0% | −1.1337 to +1.3183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.8 | −0.4% | −4.3058 to +2.1362 | no |
| response time (ms), mean | 140.5 | 103.9 | −26.0% | −42.2694 to −30.8764 | yes: GAIN |
| response time (ms), 95th percentile | 229.9 | 223.5 | −2.8% | −18.1490 to +5.4170 | no |
| response time (ms), 99th percentile | 329 | 326.5 | −0.7% | −28.1060 to +23.2428 | no |
| time over the response line (% of samples) | 0.1309 | 0.1188 | −9.3% | −0.0982 to +0.0739 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 | +12.800 (native is 0) | +10.8688 to +14.7312 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1028 | 1033 | +0.4% | −69.2330 to +77.6830 | no |
| utilisation (used / allocatable) | 0.06003 | 0.05924 | −1.3% | −0.0018 to +0.0002 | no |
| CPU used (cores), mean | 1.441 | 1.413 | −1.9% | −0.0428 to −0.0119 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01182 | +0.012 (native is 0) | +0.0107 to +0.0130 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.441 | 1.425 | −1.1% | −0.0308 to −0.0003 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.5 | 457.3 | +1.3% | −0.1300 to +11.8562 | no |
| HPA replicas, mean | 2.093 | 1.975 | −5.6% | −0.2643 to +0.0285 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, mean (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 44.18 | −0.1% | −0.9231 to +0.8550 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1425 | 1448 | +1.6% | −29.0972 to +74.0972 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.65 | −5.8% | −1.4637 to +0.7637 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 135.4 | 147.9 | +9.3% | −36.5299 to +61.6799 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 570.1 | 680.8 | +19.4% | −37.2290 to +258.6290 | no |
| queue: job turnaround, submitted to done, mean (s) | 786.3 | 763.3 | −2.9% | −85.7018 to +39.8185 | no |
| queue: jobs unfinished at the window's end | 7.9 | 8.4 | +6.3% | −1.5302 to +2.5302 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.512 | −0.2% | −0.0101 to +0.0005 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.9 | +0.3% | −0.4961 to +2.2179 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.9 | +0.3% | −0.4961 to +2.2179 | no |
| response time (ms), mean | 268.8 | 140.5 | −47.7% | −204.2202 to −52.4384 | yes: GAIN |
| response time (ms), 95th percentile | 819 | 229.9 | −71.9% | −937.0201 to −241.2139 | yes: GAIN |
| response time (ms), 99th percentile | 1186 | 329 | −72.3% | −1370.9521 to −343.2361 | yes: GAIN |
| time over the response line (% of samples) | 12.9 | 0.1309 | −99.0% | −21.2612 to −4.2731 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0 | −100.0% | −12.3011 to −5.0989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.613 | 1028 | +10597.0% | +783.2297 to +1254.2236 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.06003 | +7.7% | −0.0002 to +0.0088 | no |
| CPU used (cores), mean | 1.337 | 1.441 | +7.7% | −0.0050 to +0.2117 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.337 | 1.441 | +7.7% | −0.0050 to +0.2117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.8 | 451.5 | −8.2% | −80.4093 to −0.3134 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 2.093 | +8.0% | +0.0365 to +0.2740 | yes: power given |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 44.21 | +15.1% | +3.6299 to +7.9998 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.7 | 1425 | +91.4% | +592.0000 to +769.0000 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 135.4 | +295227.3% | +90.0795 to +180.5455 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 570.1 | +189933.3% | +444.4423 to +695.1577 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.67 | 786.3 | +1365.1% | +609.5822 to +855.6511 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 7.9 | +7.900 (native is 0) | +2.2029 to +13.5971 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.015 | −16.4% | −1.6996 to −0.2701 | yes: GAIN |
| node-hours | 2.516 | 2.101 | −16.5% | −0.7152 to −0.1163 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.9 | −0.0% | −0.8281 to +0.6644 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 240 | −11.5% | −53.4925 to −8.5836 | yes: GAIN |
| response time (ms), mean | 268.8 | 230 | −14.4% | −55.0137 to −22.6627 | yes: GAIN |
| response time (ms), 95th percentile | 819 | 826.2 | +0.9% | −82.3245 to +96.7325 | no |
| response time (ms), 99th percentile | 1186 | 1224 | +3.2% | −57.3048 to +133.2996 | no |
| time over the response line (% of samples) | 12.9 | 13.19 | +2.3% | −0.9400 to +1.5298 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.8 | +1.1% | −0.6872 to +0.8872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 | +37.400 (native is 0) | +21.9064 to +52.8936 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.613 | 8.788 | −8.6% | −1.6341 to −0.0159 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.0675 | +21.1% | +0.0036 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.337 | 1.341 | +0.2% | −0.0227 to +0.0294 | no |
| Omni's own CPU (cores), mean | 0 | 0.01544 | +0.015 (native is 0) | +0.0141 to +0.0168 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.356 | +1.4% | −0.0074 to +0.0450 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.8 | 428 | −13.0% | −110.7286 to −17.0310 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 2.146 | +10.7% | −0.0277 to +0.4432 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.4526 to +2.0526 | no |
| pod start wait, mean (s) | 0.2 | 1 | +400.0% | −0.4526 to +2.0526 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 39.19 | +2.1% | +0.4958 to +1.1004 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.7 | 746 | +0.2% | −3.3851 to +5.9851 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.203 | −29.9% | −3.0543 to −0.5393 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 | =0.0% | −0.0199 to +0.0199 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | −33.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 53.67 | 53.64 | −0.0% | −5.3639 to +5.3139 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.015 | −16.4% | −1.6996 to −0.2701 | yes: GAIN |
| node-hours | 2.512 | 2.101 | −16.4% | −0.7086 to −0.1132 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 270.9 | −0.3% | −2.1941 to +0.3087 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 240 | −11.7% | −55.5003 to −8.2976 | yes: GAIN |
| response time (ms), mean | 140.5 | 230 | +63.7% | +19.2831 to +159.6990 | yes: LOSS |
| response time (ms), 95th percentile | 229.9 | 826.2 | +259.4% | +265.4199 to +927.2221 | yes: LOSS |
| response time (ms), 99th percentile | 329 | 1224 | +272.1% | +389.3177 to +1400.8653 | yes: LOSS |
| time over the response line (% of samples) | 0.1309 | 13.19 | +9978.0% | +4.3738 to +21.7503 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.8 | +8.800 (native is 0) | +5.2506 to +12.3494 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 | +37.400 (native is 0) | +21.9064 to +52.8936 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1028 | 8.788 | −99.1% | −1254.8372 to −784.2662 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06003 | 0.0675 | +12.4% | +0.0029 to +0.0120 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.441 | 1.341 | −6.9% | −0.2218 to +0.0218 | no |
| Omni's own CPU (cores), mean | 0 | 0.01544 | +0.015 (native is 0) | +0.0141 to +0.0168 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.441 | 1.356 | −5.9% | −0.2072 to +0.0381 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.5 | 428 | −5.2% | −38.7645 to −8.2724 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.093 | 2.146 | +2.5% | −0.2374 to +0.3424 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.1 | 1 | +900.0% | −0.2410 to +2.0410 | no |
| pod start wait, mean (s) | 0.1 | 1 | +900.0% | −0.2410 to +2.0410 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 39.19 | −11.3% | −7.2586 to −2.7749 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1425 | 746 | −47.7% | −768.0069 to −590.3931 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.663 | −55.6% | −4.0625 to −2.6125 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 135.4 | 0.04583 | −100.0% | −180.5616 to −90.0634 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 570.1 | 0.2 | −100.0% | −695.3636 to −444.4364 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 786.3 | 53.64 | −93.2% | −856.1349 to −609.1485 | yes: GAIN |
| queue: jobs unfinished at the window's end | 7.9 | 0 | −100.0% | −13.5971 to −2.2029 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.962 | −0.6% | −0.1228 to +0.0475 | no |
| node-hours | 2.516 | 2.5 | −0.6% | −0.0591 to +0.0271 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.9 | +0.4% | −0.9348 to +2.8412 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 270.8 | −0.1% | −3.5213 to +3.0735 | no |
| response time (ms), mean | 268.8 | 103.9 | −61.3% | −244.0104 to −85.7939 | yes: GAIN |
| response time (ms), 95th percentile | 819 | 223.5 | −72.7% | −945.6556 to −245.3104 | yes: GAIN |
| response time (ms), 99th percentile | 1186 | 326.5 | −72.5% | −1372.5303 to −346.5211 | yes: GAIN |
| time over the response line (% of samples) | 12.9 | 0.1188 | −99.1% | −21.2852 to −4.2734 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0 | −100.0% | −12.3011 to −5.0989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 | +12.800 (native is 0) | +10.8688 to +14.7312 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.613 | 1033 | +10641.0% | +744.0875 to +1301.8158 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.05924 | +6.3% | −0.0014 to +0.0084 | no |
| CPU used (cores), mean | 1.337 | 1.413 | +5.7% | −0.0329 to +0.1849 | no |
| Omni's own CPU (cores), mean | 0 | 0.01182 | +0.012 (native is 0) | +0.0107 to +0.0130 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.425 | +6.6% | −0.0202 to +0.1958 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.8 | 457.3 | −7.0% | −77.1892 to +8.1926 | no |
| HPA replicas, mean | 1.938 | 1.975 | +1.9% | −0.1290 to +0.2038 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 44.18 | +15.1% | +3.7453 to +7.8163 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.7 | 1448 | +94.4% | +615.7684 to +790.2316 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.65 | −5.8% | −1.4637 to +0.7637 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 147.9 | +322663.6% | +111.7792 to +183.9958 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 680.8 | +226833.3% | +541.1844 to +819.8156 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.67 | 763.3 | +1322.4% | +550.1858 to +869.1642 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.4 | +8.400 (native is 0) | +1.9826 to +14.8174 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*