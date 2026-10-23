# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.305 | 5.984 |
| node-hours | 2.509 | 2.518 | 2.223 | 2.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.9 | 271.3 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.9 | 249.4 | 271.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 287.3 | 136.1 | 262.5 | 102.6 |
| response time (ms), 95th percentile | 940.5 | 228.1 | 989.9 | 222.6 |
| response time (ms), 99th percentile | 1423 | 331 | 1530 | 323.9 |
| time over the response line (% of samples) | 15 | 0.2079 | 15.66 | 0.2021 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0 | 8.8 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 104.1 | 22.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.985 | 1066 | 10.81 | 1107 |
| utilisation (used / allocatable) | 0.05667 | 0.05835 | 0.06388 | 0.05846 |
| CPU used (cores), mean | 1.36 | 1.4 | 1.358 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04447 | 0.0438 |
| CPU used with Omni's own (cores), mean | 1.36 | 1.4 | 1.402 | 1.443 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.2 | 463.4 | 442.5 | 462.7 |
| HPA replicas, mean | 2.073 | 2.021 | 2.548 | 1.964 |
| pods started | 0.1 | 0.3 | 0.8 | 0 |
| pod start wait, total (s) | 0.2 | 0.6 | 1.7 | 0 |
| pod start wait, mean (s) | 0.2 | 0.6 | 1.05 | 0 |
| host CPU busy, the real machine under kind (%) | 38.88 | 43.83 | 40.62 | 45.2 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 752.8 | 1419 | 757.2 | 1434 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.652 | 5.667 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 149.2 | 0.04583 | 162.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 744 | 0.3 | 637.8 |
| queue: job turnaround, submitted to done, mean (s) | 61.94 | 780.3 | 65.76 | 812.3 |
| queue: jobs unfinished at the window's end | 0 | 9.4 | 0 | 10 |

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
| worker nodes in service, mean | 6 | 5.984 | -0.3% | -0.0354 to +0.003466 | no |
| node-hours | 2.518 | 2.509 | -0.3% | -0.01958 to +0.002193 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | -0.1% | -1.365 to +1.005 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.2 | -0.3% | -1.852 to +0.4882 | no |
| response time (ms), mean | 136.1 | 102.6 | -24.6% | -40.65 to -26.32 | yes: GAIN |
| response time (ms), 95th percentile | 228.1 | 222.6 | -2.4% | -12.07 to +1.055 | no |
| response time (ms), 99th percentile | 331 | 323.9 | -2.1% | -29.59 to +15.36 | no |
| time over the response line (% of samples) | 0.2079 | 0.2021 | -2.8% | -0.1344 to +0.1227 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.8 | +22.8 (native is 0) | +15.45 to +30.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1066 | 1107 | +3.9% | -6.59 to +89.66 | no |
| utilisation (used / allocatable) | 0.05835 | 0.05846 | +0.2% | -0.00116 to +0.001366 | no |
| CPU used (cores), mean | 1.4 | 1.399 | -0.1% | -0.03025 to +0.02801 | no |
| Omni's own CPU (cores), mean | 0 | 0.0438 | +0.0438 (native is 0) | +0.03848 to +0.04912 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.4 | 1.443 | +3.0% | +0.01285 to +0.07252 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.4 | 462.7 | -0.1% | -9.832 to +8.463 | no |
| HPA replicas, mean | 2.021 | 1.964 | -2.8% | -0.1493 to +0.03602 | no |
| pods started | 0.3 | 0 | -100.0% | -0.6455 to +0.04553 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.291 to +0.09105 | no |
| pod start wait, mean (s) | 0.6 | 0 | -100.0% | -1.291 to +0.09105 | no |
| host CPU busy, the real machine under kind (%) | 43.83 | 45.2 | +3.1% | +0.5011 to +2.239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1419 | 1434 | +1.1% | -12.65 to +43.05 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.667 | -5.6% | -0.6202 to -0.04647 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 149.2 | 162.4 | +8.9% | -22.63 to +49.16 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 744 | 637.8 | -14.3% | -304.9 to +92.49 | no |
| queue: job turnaround, submitted to done, mean (s) | 780.3 | 812.3 | +4.1% | -27.63 to +91.57 | no |
| queue: jobs unfinished at the window's end | 9.4 | 10 | +6.4% | -1.222 to +2.422 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.496e-15 to +1.864e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.509 | 2.518 | +0.3% | +0.00254 to +0.01446 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.9 | +0.5% | -0.5447 to +3.056 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.9 | +0.5% | -0.5447 to +3.056 | no |
| response time (ms), mean | 287.3 | 136.1 | -52.6% | -238.2 to -64.21 | yes: GAIN |
| response time (ms), 95th percentile | 940.5 | 228.1 | -75.7% | -1118 to -306.9 | yes: GAIN |
| response time (ms), 99th percentile | 1423 | 331 | -76.7% | -1736 to -446.9 | yes: GAIN |
| time over the response line (% of samples) | 15 | 0.2079 | -98.6% | -23.59 to -5.982 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0 | -100.0% | -13.09 to -4.111 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.985 | 1066 | +11761.2% | +786.8 to +1327 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05667 | 0.05835 | +3.0% | -0.003634 to +0.006992 | no |
| CPU used (cores), mean | 1.36 | 1.4 | +3.0% | -0.08721 to +0.1678 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.36 | 1.4 | +3.0% | -0.08721 to +0.1678 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.2 | 463.4 | -4.7% | -68.49 to +22.85 | no |
| HPA replicas, mean | 2.073 | 2.021 | -2.5% | -0.1823 to +0.07805 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 43.83 | +12.7% | +2.564 to +7.333 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.8 | 1419 | +88.5% | +575.4 to +757 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 149.2 | +275307.7% | +100.8 to +197.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 744 | +185900.0% | +538.7 to +948.5 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 61.94 | 780.3 | +1159.9% | +574.4 to +862.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.4 | +9.4 (native is 0) | +3.404 to +15.4 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.305 | -11.6% | -1.288 to -0.1025 | yes: GAIN |
| node-hours | 2.509 | 2.223 | -11.4% | -0.5354 to -0.03718 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.3 | +0.2% | -0.005947 to +1.2 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 249.4 | -7.8% | -40.06 to -2.419 | yes: GAIN |
| response time (ms), mean | 287.3 | 262.5 | -8.6% | -37.03 to -12.63 | yes: GAIN |
| response time (ms), 95th percentile | 940.5 | 989.9 | +5.3% | +2.598 to +96.18 | yes: LOSS |
| response time (ms), 99th percentile | 1423 | 1530 | +7.6% | -65.02 to +280.5 | no |
| time over the response line (% of samples) | 15 | 15.66 | +4.4% | -0.2225 to +1.557 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.8 | +2.3% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.1 | +104 (native is 0) | +81.55 to +126.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.985 | 10.81 | +20.3% | -0.2107 to +3.857 | no |
| utilisation (used / allocatable) | 0.05667 | 0.06388 | +12.7% | +0.001563 to +0.01285 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.36 | 1.358 | -0.2% | -0.02191 to +0.01754 | no |
| Omni's own CPU (cores), mean | 0 | 0.04447 | +0.0445 (native is 0) | +0.03761 to +0.05133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.36 | 1.402 | +3.1% | +0.01715 to +0.06742 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.2 | 442.5 | -9.0% | -78.73 to -8.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.073 | 2.548 | +22.9% | +0.1213 to +0.8292 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | -0.1294 to +1.529 | no |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | -0.2922 to +3.292 | no |
| pod start wait, mean (s) | 0.2 | 1.05 | +425.0% | -0.2433 to +1.943 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 40.62 | +4.5% | +1.292 to +2.2 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.8 | 757.2 | +0.6% | +0.1188 to +8.681 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.652 | -22.5% | -2.493 to -0.2041 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 | -15.4% | -0.06238 to +0.04572 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.94 | 65.76 | +6.2% | -0.6586 to +8.309 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.305 | -11.6% | -1.288 to -0.1025 | yes: GAIN |
| node-hours | 2.518 | 2.223 | -11.7% | -0.5441 to -0.04547 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.3 | -0.2% | -2.643 to +1.325 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 249.4 | -8.3% | -42.98 to -2.008 | yes: GAIN |
| response time (ms), mean | 136.1 | 262.5 | +92.9% | +44.29 to +208.5 | yes: LOSS |
| response time (ms), 95th percentile | 228.1 | 989.9 | +334.0% | +336 to +1188 | yes: LOSS |
| response time (ms), 99th percentile | 331 | 1530 | +362.3% | +517.1 to +1882 | yes: LOSS |
| time over the response line (% of samples) | 0.2079 | 15.66 | +7434.2% | +6.379 to +24.53 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.8 | +8.8 (native is 0) | +4.458 to +13.14 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.1 | +104 (native is 0) | +81.55 to +126.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1066 | 10.81 | -99.0% | -1325 to -784.7 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05835 | 0.06388 | +9.5% | +0.003588 to +0.007471 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.4 | 1.358 | -3.0% | -0.1821 to +0.09715 | no |
| Omni's own CPU (cores), mean | 0 | 0.04447 | +0.0445 (native is 0) | +0.03761 to +0.05133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.4 | 1.402 | +0.1% | -0.1435 to +0.1475 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.4 | 442.5 | -4.5% | -36.5 to -5.405 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.548 | +26.1% | +0.196 to +0.8587 | yes: power given |
| pods started | 0.3 | 0.8 | +166.7% | -0.343 to +1.343 | no |
| pod start wait, total (s) | 0.6 | 1.7 | +183.3% | -0.6667 to +2.867 | no |
| pod start wait, mean (s) | 0.6 | 1.05 | +75.0% | -0.7236 to +1.624 | no |
| host CPU busy, the real machine under kind (%) | 43.83 | 40.62 | -7.3% | -5.833 to -0.5723 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1419 | 757.2 | -46.6% | -750.5 to -573.1 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.807 | -53.2% | -3.568 to -2.818 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 149.2 | 0.04583 | -100.0% | -197.5 to -100.8 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 744 | 0.3 | -100.0% | -948.7 to -538.7 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 780.3 | 65.76 | -91.6% | -856.1 to -573.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.4 | 0 | -100.0% | -15.4 to -3.404 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.984 | -0.3% | -0.0354 to +0.003466 | no |
| node-hours | 2.509 | 2.509 | -0.0% | -0.0105 to +0.01011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.7 | +0.4% | -0.9983 to +3.15 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.2 | +0.2% | -1.148 to +2.296 | no |
| response time (ms), mean | 287.3 | 102.6 | -64.3% | -278.5 to -90.94 | yes: GAIN |
| response time (ms), 95th percentile | 940.5 | 222.6 | -76.3% | -1124 to -311.8 | yes: GAIN |
| response time (ms), 99th percentile | 1423 | 323.9 | -77.2% | -1761 to -436.6 | yes: GAIN |
| time over the response line (% of samples) | 15 | 0.2021 | -98.7% | -23.58 to -6.003 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 0.1 | -98.8% | -12.94 to -4.062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.8 | +22.8 (native is 0) | +15.45 to +30.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.985 | 1107 | +12223.4% | +830.9 to +1366 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05667 | 0.05846 | +3.1% | -0.003471 to +0.007036 | no |
| CPU used (cores), mean | 1.36 | 1.399 | +2.9% | -0.08366 to +0.162 | no |
| Omni's own CPU (cores), mean | 0 | 0.0438 | +0.0438 (native is 0) | +0.03848 to +0.04912 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.36 | 1.443 | +6.1% | -0.03553 to +0.2015 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.2 | 462.7 | -4.8% | -68.45 to +21.44 | no |
| HPA replicas, mean | 2.073 | 1.964 | -5.2% | -0.2562 to +0.03866 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 45.2 | +16.3% | +3.942 to +8.695 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.8 | 1434 | +90.5% | +609 to +753.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.667 | -5.6% | -0.6202 to -0.04647 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 162.4 | +299800.0% | +112.2 to +212.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 637.8 | +159350.0% | +477.5 to +797.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 61.94 | 812.3 | +1211.5% | +604.6 to +896.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10 | +10 (native is 0) | +3.801 to +16.2 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*