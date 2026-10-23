# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.385 | 5.247 |
| node-hours | 2.514 | 2.512 | 2.257 | 2.199 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | 271.7 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.3 | 252.4 | 248 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 283.7 | 306.7 | 267.9 | 300.1 |
| response time (ms), 95th percentile | 918.5 | 1018 | 1026 | 1180 |
| response time (ms), 99th percentile | 1277 | 1505 | 1569 | 1762 |
| time over the response line (% of samples) | 16.23 | 16.79 | 16.48 | 17.32 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.3 | 8.5 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 108.2 | 117.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.362 | 9.372 | 9.765 | 9.465 |
| utilisation (used / allocatable) | 0.05753 | 0.05761 | 0.06445 | 0.06591 |
| CPU used (cores), mean | 1.381 | 1.383 | 1.389 | 1.385 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04905 | 0.05068 |
| CPU used with Omni's own (cores), mean | 1.381 | 1.383 | 1.438 | 1.436 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 479.3 | 437.4 | 432.5 |
| HPA replicas, mean | 2.012 | 2.034 | 2.548 | 2.67 |
| pods started | 0 | 0 | 0.5 | 1.8 |
| pod start wait, total (s) | 0 | 0 | 1 | 3.7 |
| pod start wait, mean (s) | 0 | 0 | 0.6 | 1.267 |
| host CPU busy, the real machine under kind (%) | 39.11 | 40 | 41.62 | 42.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 756.2 | 766 | 762.6 | 774.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.814 | 4.516 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1792 | 0.05417 | 0.1958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | 0.4 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 64.42 | 72.67 | 71.25 | 83.22 |
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
| worker nodes in service, mean | 6 | 5.247 | -12.6% | -1.357 to -0.1491 | yes: GAIN |
| node-hours | 2.512 | 2.199 | -12.5% | -0.5651 to -0.06069 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.7 | +0.1% | -0.544 to +1.324 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 248 | -8.6% | -42.33 to -4.249 | yes: GAIN |
| response time (ms), mean | 306.7 | 300.1 | -2.1% | -27.13 to +13.96 | no |
| response time (ms), 95th percentile | 1018 | 1180 | +16.0% | +6.081 to +318.9 | yes: LOSS |
| response time (ms), 99th percentile | 1505 | 1762 | +17.1% | +72.1 to +441.4 | yes: LOSS |
| time over the response line (% of samples) | 16.79 | 17.32 | +3.1% | +0.01101 to +1.043 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.4 | +1.2% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.7 | +118 (native is 0) | +67.33 to +168.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.372 | 9.465 | +1.0% | -1.526 to +1.713 | no |
| utilisation (used / allocatable) | 0.05761 | 0.06591 | +14.4% | +0.002404 to +0.0142 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.385 | +0.2% | -0.03074 to +0.03599 | no |
| Omni's own CPU (cores), mean | 0 | 0.05068 | +0.0507 (native is 0) | +0.04521 to +0.05615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.436 | +3.9% | +0.01591 to +0.0907 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.3 | 432.5 | -9.8% | -80.94 to -12.64 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.034 | 2.67 | +31.2% | +0.1864 to +1.085 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.6417 to +2.958 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.7 (native is 0) | +1.198 to +6.202 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.267 | +1.27 (native is 0) | +0.4029 to +2.13 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40 | 42.47 | +6.2% | +2.034 to +2.903 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 766 | 774.9 | +1.2% | +1.872 to +15.93 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.516 | -24.7% | -2.66 to -0.3081 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.1958 | +9.3% | -0.02821 to +0.06154 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | -12.5% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.67 | 83.22 | +14.5% | +1.681 to +19.44 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.218e-15 to +8.636e-17 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.512 | -0.1% | -0.01065 to +0.00632 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | -0.0% | -1.198 to +0.9677 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.3 | -0.0% | -1.198 to +0.9677 | no |
| response time (ms), mean | 283.7 | 306.7 | +8.1% | +4.287 to +41.7 | yes: LOSS |
| response time (ms), 95th percentile | 918.5 | 1018 | +10.8% | -21.32 to +219.9 | no |
| response time (ms), 99th percentile | 1277 | 1505 | +17.8% | +64.69 to +390 | yes: LOSS |
| time over the response line (% of samples) | 16.23 | 16.79 | +3.5% | -0.3202 to +1.45 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.3 | +1.2% | -0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.362 | 9.372 | +0.1% | -1.249 to +1.269 | no |
| utilisation (used / allocatable) | 0.05753 | 0.05761 | +0.1% | -0.001086 to +0.001236 | no |
| CPU used (cores), mean | 1.381 | 1.383 | +0.1% | -0.02605 to +0.02967 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.381 | 1.383 | +0.1% | -0.02605 to +0.02967 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 479.3 | -0.0% | -11.9 to +11.58 | no |
| HPA replicas, mean | 2.012 | 2.034 | +1.1% | -0.1181 to +0.1632 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 39.11 | 40 | +2.3% | +0.6586 to +1.134 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 766 | +1.3% | +2.761 to +16.84 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1792 | +258.3% | +0.0672 to +0.1911 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | +0.123 to +0.877 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.42 | 72.67 | +12.8% | +1.978 to +14.51 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.385 | -10.3% | -1.189 to -0.04088 | yes: GAIN |
| node-hours | 2.514 | 2.257 | -10.2% | -0.4972 to -0.01737 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.7 | +0.1% | -0.5833 to +1.101 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 252.4 | -7.0% | -37.05 to -1.027 | yes: GAIN |
| response time (ms), mean | 283.7 | 267.9 | -5.6% | -27.71 to -3.808 | yes: GAIN |
| response time (ms), 95th percentile | 918.5 | 1026 | +11.7% | +6.649 to +208.9 | yes: LOSS |
| response time (ms), 99th percentile | 1277 | 1569 | +22.8% | +109.3 to +473.3 | yes: LOSS |
| time over the response line (% of samples) | 16.23 | 16.48 | +1.6% | -0.8604 to +1.367 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.5 | +3.7% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108.2 | +108 (native is 0) | +68.18 to +148.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.362 | 9.765 | +4.3% | -1.303 to +2.11 | no |
| utilisation (used / allocatable) | 0.05753 | 0.06445 | +12.0% | +0.001282 to +0.01256 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.381 | 1.389 | +0.6% | -0.01596 to +0.03341 | no |
| Omni's own CPU (cores), mean | 0 | 0.04905 | +0.049 (native is 0) | +0.04329 to +0.05481 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.381 | 1.438 | +4.2% | +0.02993 to +0.08561 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 437.4 | -8.8% | -77.77 to -6.372 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.012 | 2.548 | +26.6% | +0.2082 to +0.8638 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.1952 to +1.195 | no |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | -0.3903 to +2.39 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 39.11 | 41.62 | +6.4% | +2.197 to +2.833 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 762.6 | +0.8% | +1.131 to +11.67 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.814 | -19.8% | -2.284 to -0.08796 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05417 | +8.3% | -0.03418 to +0.04252 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.42 | 71.25 | +10.6% | +1.759 to +11.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.385 | -10.3% | -1.189 to -0.04088 | yes: GAIN |
| node-hours | 2.512 | 2.257 | -10.2% | -0.4978 to -0.0125 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.7 | +0.1% | -0.7706 to +1.518 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 252.4 | -7.0% | -37.22 to -0.627 | yes: GAIN |
| response time (ms), mean | 306.7 | 267.9 | -12.6% | -53.54 to -23.95 | yes: GAIN |
| response time (ms), 95th percentile | 1018 | 1026 | +0.8% | -46.54 to +63.43 | no |
| response time (ms), 99th percentile | 1505 | 1569 | +4.2% | -5.649 to +133.5 | no |
| time over the response line (% of samples) | 16.79 | 16.48 | -1.9% | -1.219 to +0.5962 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.5 | +2.4% | -0.6121 to +1.012 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108.2 | +108 (native is 0) | +68.18 to +148.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.372 | 9.765 | +4.2% | -1.151 to +1.938 | no |
| utilisation (used / allocatable) | 0.05761 | 0.06445 | +11.9% | +0.001022 to +0.01267 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.389 | +0.5% | -0.0155 to +0.02932 | no |
| Omni's own CPU (cores), mean | 0 | 0.04905 | +0.049 (native is 0) | +0.04329 to +0.05481 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.438 | +4.0% | +0.02992 to +0.082 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.3 | 437.4 | -8.7% | -78 to -5.824 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.034 | 2.548 | +25.2% | +0.1643 to +0.8626 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.1952 to +1.195 | no |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | -0.3903 to +2.39 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 40 | 41.62 | +4.0% | +1.285 to +1.952 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 766 | 762.6 | -0.4% | -6.707 to -0.0927 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.814 | -19.8% | -2.284 to -0.08796 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.05417 | -69.8% | -0.1737 to -0.07633 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.4 | -50.0% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 72.67 | 71.25 | -1.9% | -4.191 to +1.366 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.247 | -12.6% | -1.357 to -0.1491 | yes: GAIN |
| node-hours | 2.514 | 2.199 | -12.5% | -0.566 to -0.06412 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.7 | +0.1% | -0.4043 to +0.9535 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 248 | -8.6% | -42.38 to -4.427 | yes: GAIN |
| response time (ms), mean | 283.7 | 300.1 | +5.8% | -11.85 to +44.66 | no |
| response time (ms), 95th percentile | 918.5 | 1180 | +28.5% | +69.12 to +454.5 | yes: LOSS |
| response time (ms), 99th percentile | 1277 | 1762 | +37.9% | +164.9 to +803.3 | yes: LOSS |
| time over the response line (% of samples) | 16.23 | 17.32 | +6.7% | +0.3352 to +1.848 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.4 | +2.4% | -0.4573 to +0.8573 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.7 | +118 (native is 0) | +67.33 to +168.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.362 | 9.465 | +1.1% | -1.503 to +1.71 | no |
| utilisation (used / allocatable) | 0.05753 | 0.06591 | +14.6% | +0.002904 to +0.01385 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.381 | 1.385 | +0.3% | -0.02711 to +0.03599 | no |
| Omni's own CPU (cores), mean | 0 | 0.05068 | +0.0507 (native is 0) | +0.04521 to +0.05615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.381 | 1.436 | +4.0% | +0.01929 to +0.09095 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 432.5 | -9.8% | -78.63 to -15.27 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.012 | 2.67 | +32.7% | +0.2535 to +1.063 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.6417 to +2.958 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.7 (native is 0) | +1.198 to +6.202 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.267 | +1.27 (native is 0) | +0.4029 to +2.13 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.11 | 42.47 | +8.6% | +2.871 to +3.86 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 774.9 | +2.5% | +6.342 to +31.06 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.516 | -24.7% | -2.66 to -0.3081 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1958 | +291.7% | +0.06856 to +0.2231 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.42 | 83.22 | +29.2% | +6.431 to +31.17 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*