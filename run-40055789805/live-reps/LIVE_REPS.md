# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.242 | 5.201 |
| node-hours | 2.513 | 2.516 | 2.198 | 2.18 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271 | 271.3 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271 | 247.4 | 245.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 274.4 | 292.6 | 252 | 270.8 |
| response time (ms), 95th percentile | 852 | 940.1 | 956.1 | 1055 |
| response time (ms), 99th percentile | 1248 | 1362 | 1400 | 1537 |
| time over the response line (% of samples) | 14.03 | 14.89 | 14.38 | 14.8 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 7.8 | 8.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 53 | 65.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.963 | 9.582 | 8.113 | 9.115 |
| utilisation (used / allocatable) | 0.05676 | 0.05597 | 0.06494 | 0.06477 |
| CPU used (cores), mean | 1.362 | 1.343 | 1.352 | 1.338 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01668 | 0.01707 |
| CPU used with Omni's own (cores), mean | 1.362 | 1.343 | 1.369 | 1.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 494.4 | 440.4 | 442.9 |
| HPA replicas, mean | 1.969 | 1.998 | 2.295 | 2.449 |
| pods started | 0 | 0.1 | 0.2 | 0.4 |
| pod start wait, total (s) | 0 | 0.2 | 0.8 | 1.3 |
| pod start wait, mean (s) | 0 | 0.2 | 0.4 | 1.3 |
| host CPU busy, the real machine under kind (%) | 38.55 | 39.46 | 39.64 | 40.53 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 752.6 | 757.7 | 756.3 | 766.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.687 | 4.656 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1375 | 0.05417 | 0.1542 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | 0.3 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 59.11 | 66.4 | 64.84 | 71.98 |
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
| worker nodes in service, mean | 6 | 5.201 | -13.3% | -1.573 to -0.02566 | yes: GAIN |
| node-hours | 2.516 | 2.18 | -13.4% | -0.6612 to -0.01145 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.9 | -0.0% | -0.9856 to +0.7764 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 245.8 | -9.3% | -49.81 to -0.5931 | yes: GAIN |
| response time (ms), mean | 292.6 | 270.8 | -7.4% | -38.18 to -5.324 | yes: GAIN |
| response time (ms), 95th percentile | 940.1 | 1055 | +12.2% | +7.206 to +222.9 | yes: LOSS |
| response time (ms), 99th percentile | 1362 | 1537 | +12.8% | -36.62 to +385.8 | no |
| time over the response line (% of samples) | 14.89 | 14.8 | -0.6% | -0.8531 to +0.6668 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.3 | +6.4% | -0.005799 to +1.006 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.9 | +65.9 (native is 0) | +37.54 to +94.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.582 | 9.115 | -4.9% | -2.24 to +1.306 | no |
| utilisation (used / allocatable) | 0.05597 | 0.06477 | +15.7% | +0.0008564 to +0.01675 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.343 | 1.338 | -0.4% | -0.03865 to +0.02742 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.0171 (native is 0) | +0.01552 to +0.01862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.343 | 1.355 | +0.9% | -0.02184 to +0.04476 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.4 | 442.9 | -10.4% | -99.03 to -3.977 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.449 | +22.6% | +0.2229 to +0.6791 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | -0.9635 to +3.164 | no |
| pod start wait, mean (s) | 0.2 | 1.3 | +550.0% | -0.9635 to +3.164 | no |
| host CPU busy, the real machine under kind (%) | 39.46 | 40.53 | +2.7% | +0.5938 to +1.541 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.7 | 766.3 | +1.1% | +1.358 to +15.84 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 | -22.4% | -2.569 to -0.1196 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.1542 | +12.1% | -0.03035 to +0.06369 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 66.4 | 71.98 | +8.4% | -1.373 to +12.53 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.062e-15 to +1.733e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.516 | +0.1% | -0.005403 to +0.01074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271 | -0.1% | -1.291 to +1.008 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271 | -0.1% | -1.291 to +1.008 | no |
| response time (ms), mean | 274.4 | 292.6 | +6.6% | +3.397 to +32.98 | yes: LOSS |
| response time (ms), 95th percentile | 852 | 940.1 | +10.3% | +14.21 to +162 | yes: LOSS |
| response time (ms), 99th percentile | 1248 | 1362 | +9.1% | +10.81 to +217.4 | yes: LOSS |
| time over the response line (% of samples) | 14.03 | 14.89 | +6.1% | -0.1186 to +1.833 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 7.8 | +5.4% | +0.03062 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.963 | 9.582 | +6.9% | -1.837 to +3.073 | no |
| utilisation (used / allocatable) | 0.05676 | 0.05597 | -1.4% | -0.00223 to +0.000656 | no |
| CPU used (cores), mean | 1.362 | 1.343 | -1.4% | -0.05353 to +0.01575 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.362 | 1.343 | -1.4% | -0.05353 to +0.01575 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 494.4 | +2.2% | -6.047 to +27.48 | no |
| HPA replicas, mean | 1.969 | 1.998 | +1.5% | -0.1592 to +0.2165 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 38.55 | 39.46 | +2.4% | +0.7546 to +1.071 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.6 | 757.7 | +0.7% | +0.03696 to +10.16 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1375 | +230.0% | +0.02412 to +0.1675 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.11 | 66.4 | +12.3% | +1.541 to +13.04 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.242 | -12.6% | -1.456 to -0.06064 | yes: GAIN |
| node-hours | 2.513 | 2.198 | -12.6% | -0.6073 to -0.024 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.3 | +0.0% | -0.4239 to +0.6533 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 247.4 | -8.8% | -46.01 to -1.483 | yes: GAIN |
| response time (ms), mean | 274.4 | 252 | -8.2% | -31.74 to -12.99 | yes: GAIN |
| response time (ms), 95th percentile | 852 | 956.1 | +12.2% | +32.88 to +175.3 | yes: LOSS |
| response time (ms), 99th percentile | 1248 | 1400 | +12.2% | +38.83 to +265.8 | yes: LOSS |
| time over the response line (% of samples) | 14.03 | 14.38 | +2.4% | -0.6556 to +1.343 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 8.8 | +18.9% | +0.0428 to +2.757 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 | +53 (native is 0) | +32.81 to +73.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.963 | 8.113 | -9.5% | -2.895 to +1.195 | no |
| utilisation (used / allocatable) | 0.05676 | 0.06494 | +14.4% | +0.001248 to +0.01512 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.362 | 1.352 | -0.7% | -0.05038 to +0.03065 | no |
| Omni's own CPU (cores), mean | 0 | 0.01668 | +0.0167 (native is 0) | +0.01484 to +0.01852 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.362 | 1.369 | +0.5% | -0.03483 to +0.04845 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 440.4 | -8.9% | -79.25 to -7.232 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.295 | +16.5% | +0.09536 to +0.5557 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -1.01 to +2.61 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| host CPU busy, the real machine under kind (%) | 38.55 | 39.64 | +2.8% | +0.8842 to +1.305 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.6 | 756.3 | +0.5% | -0.1895 to +7.59 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.687 | -21.9% | -2.454 to -0.1724 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05417 | +30.0% | -0.007616 to +0.03262 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.11 | 64.84 | +9.7% | +1.241 to +10.23 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.242 | -12.6% | -1.456 to -0.06064 | yes: GAIN |
| node-hours | 2.516 | 2.198 | -12.7% | -0.6105 to -0.02617 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.3 | +0.1% | -0.7697 to +1.281 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 247.4 | -8.7% | -45.44 to -1.772 | yes: GAIN |
| response time (ms), mean | 292.6 | 252 | -13.9% | -55.33 to -25.78 | yes: GAIN |
| response time (ms), 95th percentile | 940.1 | 956.1 | +1.7% | -37.26 to +69.3 | no |
| response time (ms), 99th percentile | 1362 | 1400 | +2.8% | -85.15 to +161.5 | no |
| time over the response line (% of samples) | 14.89 | 14.38 | -3.4% | -1.292 to +0.2646 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.8 | +12.8% | -0.306 to +2.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 | +53 (native is 0) | +32.81 to +73.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.582 | 8.113 | -15.3% | -2.972 to +0.03567 | no |
| utilisation (used / allocatable) | 0.05597 | 0.06494 | +16.0% | +0.0008194 to +0.01712 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.343 | 1.352 | +0.7% | -0.01705 to +0.0351 | no |
| Omni's own CPU (cores), mean | 0 | 0.01668 | +0.0167 (native is 0) | +0.01484 to +0.01852 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.343 | 1.369 | +1.9% | +5.802e-05 to +0.05135 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.4 | 440.4 | -10.9% | -105 to -2.91 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.295 | +14.9% | +0.05761 to +0.5361 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | -0.7572 to +1.957 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.46 | 39.64 | +0.5% | -0.09175 to +0.4549 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.7 | 756.3 | -0.2% | -4.585 to +1.785 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.687 | -21.9% | -2.454 to -0.1724 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.05417 | -60.6% | -0.1522 to -0.0145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.3 | -57.1% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 66.4 | 64.84 | -2.3% | -3.624 to +0.507 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.201 | -13.3% | -1.573 to -0.02566 | yes: GAIN |
| node-hours | 2.513 | 2.18 | -13.3% | -0.66 to -0.007242 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 270.9 | -0.1% | -1.706 to +1.214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 245.8 | -9.3% | -50.6 to -0.08368 | yes: GAIN |
| response time (ms), mean | 274.4 | 270.8 | -1.3% | -23.57 to +16.44 | no |
| response time (ms), 95th percentile | 852 | 1055 | +23.8% | +50.79 to +355.5 | yes: LOSS |
| response time (ms), 99th percentile | 1248 | 1537 | +23.1% | +41.54 to +535.9 | yes: LOSS |
| time over the response line (% of samples) | 14.03 | 14.8 | +5.4% | +0.138 to +1.39 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 8.3 | +12.2% | +0.1887 to +1.611 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.9 | +65.9 (native is 0) | +37.54 to +94.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.963 | 9.115 | +1.7% | -2.653 to +2.956 | no |
| utilisation (used / allocatable) | 0.05676 | 0.06477 | +14.1% | +0.001254 to +0.01478 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.362 | 1.338 | -1.8% | -0.07903 to +0.03003 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.0171 (native is 0) | +0.01552 to +0.01862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.362 | 1.355 | -0.5% | -0.06289 to +0.04802 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 442.9 | -8.4% | -73.82 to -7.746 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.449 | +24.4% | +0.17 to +0.7893 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | -0.6963 to +3.296 | no |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | -0.6963 to +3.296 | no |
| host CPU busy, the real machine under kind (%) | 38.55 | 40.53 | +5.1% | +1.516 to +2.445 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.6 | 766.3 | +1.8% | +3.328 to +24.07 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 | -22.4% | -2.569 to -0.1196 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1542 | +270.0% | +0.03296 to +0.192 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.11 | 71.98 | +21.8% | +2.945 to +22.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*