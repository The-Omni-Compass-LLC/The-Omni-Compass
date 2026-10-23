# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.29 | 6.845 |
| node-hours | 5.038 | 5.024 | 4.311 | 2.863 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 504.2 | 524.4 | 503.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 504.2 | 470.6 | 342.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 436.4 | 116.4 | 480.9 | 67.69 |
| response time (ms), 95th percentile | 1695 | 160.8 | 2134 | 89.35 |
| response time (ms), 99th percentile | 2571 | 189.4 | 3136 | 116.2 |
| time over the response line (% of samples) | 16.75 | 0 | 18.83 | 0.00361 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0 | 10.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 197.8 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 39.4 | 95 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 0 | 13.72 | 0.02667 |
| utilisation (used / allocatable) | 0.03138 | 0.005876 | 0.03859 | 0.008782 |
| CPU used (cores), mean | 1.506 | 0.2821 | 1.564 | 0.2391 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03823 | 0.02019 |
| CPU used with Omni's own (cores), mean | 1.506 | 0.2821 | 1.602 | 0.2593 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 4412 | 725.1 | 3548 |
| HPA replicas, mean | 4.024 | 4.203 | 4.996 | 4.645 |
| pods started | 0.2 | 0.3 | 3.1 | 2 |
| pod start wait, total (s) | 0.4 | 0.4 | 6.5 | 3 |
| pod start wait, mean (s) | 0.2 | 0.4 | 1.715 | 1.13 |
| host CPU busy, the real machine under kind (%) | 46.43 | 13.35 | 51.12 | 15.13 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 813.6 | 1503 | 847.4 | 1504 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.24 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1156 | 0.05833 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1473 | 0.4 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 124 | 1156 | 150 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 6.845 | -43.0% | -6.155 to -4.156 | yes: GAIN |
| node-hours | 5.024 | 2.863 | -43.0% | -2.584 to -1.737 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 503.9 | -0.1% | -1.62 to +1.011 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 342.2 | -32.1% | -194 to -130.1 | yes: GAIN |
| response time (ms), mean | 116.4 | 67.69 | -41.8% | -61.15 to -36.25 | yes: GAIN |
| response time (ms), 95th percentile | 160.8 | 89.35 | -44.4% | -88.63 to -54.33 | yes: GAIN |
| response time (ms), 99th percentile | 189.4 | 116.2 | -38.7% | -89.78 to -56.68 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.00361 | +0.00361 (native is 0) | -0.004556 to +0.01178 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +31.84 to +36.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.02667 | +0.0267 (native is 0) | -0.03365 to +0.08699 | no |
| utilisation (used / allocatable) | 0.005876 | 0.008782 | +49.5% | +0.002164 to +0.003648 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2821 | 0.2391 | -15.2% | -0.05458 to -0.0313 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02019 | +0.0202 (native is 0) | +0.01717 to +0.02321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2821 | 0.2593 | -8.1% | -0.03502 to -0.01048 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4412 | 3548 | -19.6% | -1051 to -677.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.203 | 4.645 | +10.5% | +0.107 to +0.7779 | yes: power given |
| pods started | 0.3 | 2 | +566.7% | +0.2283 to +3.172 | yes: power given |
| pod start wait, total (s) | 0.4 | 3 | +650.0% | +0.3582 to +4.842 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.13 | +182.5% | -0.1015 to +1.561 | no |
| host CPU busy, the real machine under kind (%) | 13.35 | 15.13 | +13.3% | +1.174 to +2.373 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 1504 | +0.1% | -1.296 to +3.696 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1158 | +0.1% | -1.155 to +3.697 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 1474 | +0.1% | -1.156 to +3.556 | no |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1158 | +0.1% | -1.155 to +3.697 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -3.992e-15 to +1.505e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.038 | 5.024 | -0.3% | -0.0318 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 504.2 | -3.9% | -24.03 to -16.47 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 504.2 | -3.9% | -24.03 to -16.47 | yes: GAIN |
| response time (ms), mean | 436.4 | 116.4 | -73.3% | -528 to -111.9 | yes: GAIN |
| response time (ms), 95th percentile | 1695 | 160.8 | -90.5% | -2577 to -491.4 | yes: GAIN |
| response time (ms), 99th percentile | 2571 | 189.4 | -92.6% | -3945 to -818.6 | yes: GAIN |
| time over the response line (% of samples) | 16.75 | 0 | -100.0% | -28.53 to -4.978 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0 | -100.0% | -13.58 to -3.218 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 0 | -100.0% | -15.75 to -8.588 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03138 | 0.005876 | -81.3% | -0.02889 to -0.02212 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.506 | 0.2821 | -81.3% | -1.387 to -1.062 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.506 | 0.2821 | -81.3% | -1.387 to -1.062 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 4412 | +416.3% | +3031 to +4084 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.024 | 4.203 | +4.4% | +0.004434 to +0.3528 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.4 | 0.4 | +0.0% | -1.118 to +1.118 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 46.43 | 13.35 | -71.2% | -37.93 to -28.23 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 813.6 | 1503 | +84.8% | +622 to +757.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1156 | +1632605.9% | +1154 to +1159 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1473 | +294420.0% | +1469 to +1475 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124 | 1156 | +832.5% | +961.3 to +1104 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.29 | -14.3% | -3.386 to -0.03719 | yes: GAIN |
| node-hours | 5.038 | 4.311 | -14.4% | -1.427 to -0.02643 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 524.4 | -0.0% | -0.9363 to +0.8772 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 470.6 | -10.3% | -106.5 to -1.198 | yes: GAIN |
| response time (ms), mean | 436.4 | 480.9 | +10.2% | +5.739 to +83.29 | yes: LOSS |
| response time (ms), 95th percentile | 1695 | 2134 | +25.9% | +180.6 to +696.8 | yes: LOSS |
| response time (ms), 99th percentile | 2571 | 3136 | +21.9% | +218.4 to +909.9 | yes: LOSS |
| time over the response line (% of samples) | 16.75 | 18.83 | +12.4% | -0.04451 to +4.2 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 10.3 | +22.6% | -0.1635 to +3.964 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 197.8 | +198 (native is 0) | +137.2 to +258.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 13.72 | +12.7% | -1.87 to +4.97 | no |
| utilisation (used / allocatable) | 0.03138 | 0.03859 | +23.0% | +0.001574 to +0.01284 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.564 | +3.8% | +0.02254 to +0.09233 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03823 | +0.0382 (native is 0) | +0.0341 to +0.04236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.602 | +6.4% | +0.05761 to +0.1337 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 725.1 | -15.1% | -219.1 to -39.65 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.024 | 4.996 | +24.2% | +0.4586 to +1.486 | yes: power given |
| pods started | 0.2 | 3.1 | +1450.0% | +1.618 to +4.182 | yes: power given |
| pod start wait, total (s) | 0.4 | 6.5 | +1525.0% | +2.654 to +9.546 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.715 | +757.5% | +0.8423 to +2.188 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.43 | 51.12 | +10.1% | +3.658 to +5.71 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 813.6 | 847.4 | +4.2% | +9.424 to +58.18 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.24 | -23.0% | -5.345 to -0.1742 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.05833 | -17.6% | -0.04981 to +0.02481 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 124 | 150 | +21.0% | +10.34 to +41.67 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.29 | -14.3% | -3.386 to -0.03719 | yes: GAIN |
| node-hours | 5.024 | 4.311 | -14.2% | -1.421 to -0.003925 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 524.4 | +4.0% | +16.41 to +24.03 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 470.6 | -6.7% | -89.33 to +22.14 | no |
| response time (ms), mean | 116.4 | 480.9 | +313.1% | +121.1 to +607.9 | yes: LOSS |
| response time (ms), 95th percentile | 160.8 | 2134 | +1226.7% | +697.8 to +3248 | yes: LOSS |
| response time (ms), 99th percentile | 189.4 | 3136 | +1555.4% | +1062 to +4830 | yes: LOSS |
| time over the response line (% of samples) | 0 | 18.83 | +18.8 (native is 0) | +7.454 to +30.21 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.3 | +10.3 (native is 0) | +5.054 to +15.55 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 197.8 | +198 (native is 0) | +137.2 to +258.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 13.72 | +13.7 (native is 0) | +7.768 to +19.67 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005876 | 0.03859 | +556.7% | +0.02884 to +0.03658 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2821 | 1.564 | +454.4% | +1.091 to +1.472 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03823 | +0.0382 (native is 0) | +0.0341 to +0.04236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2821 | 1.602 | +468.0% | +1.127 to +1.513 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4412 | 725.1 | -83.6% | -4301 to -3072 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.203 | 4.996 | +18.9% | +0.2238 to +1.364 | yes: power given |
| pods started | 0.3 | 3.1 | +933.3% | +1.377 to +4.223 | yes: power given |
| pod start wait, total (s) | 0.4 | 6.5 | +1525.0% | +2.524 to +9.676 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.715 | +328.7% | +0.549 to +2.081 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.35 | 51.12 | +282.8% | +32.06 to +43.46 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 847.4 | -43.6% | -747 to -564.6 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 0.05833 | -100.0% | -1159 to -1154 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 0.4 | -100.0% | -1475 to -1469 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 150 | -87.0% | -1092 to -920.5 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.845 | -43.0% | -6.155 to -4.156 | yes: GAIN |
| node-hours | 5.038 | 2.863 | -43.2% | -2.594 to -1.756 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 503.9 | -3.9% | -23.39 to -17.72 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 342.2 | -34.8% | -212.6 to -152 | yes: GAIN |
| response time (ms), mean | 436.4 | 67.69 | -84.5% | -588 to -149.3 | yes: GAIN |
| response time (ms), 95th percentile | 1695 | 89.35 | -94.7% | -2661 to -549.9 | yes: GAIN |
| response time (ms), 99th percentile | 2571 | 116.2 | -95.5% | -4028 to -882.7 | yes: GAIN |
| time over the response line (% of samples) | 16.75 | 0.00361 | -100.0% | -28.52 to -4.977 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0 | -100.0% | -13.58 to -3.218 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +31.84 to +36.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 0.02667 | -99.8% | -15.7 to -8.587 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03138 | 0.008782 | -72.0% | -0.02593 to -0.01927 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.506 | 0.2391 | -84.1% | -1.428 to -1.107 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02019 | +0.0202 (native is 0) | +0.01717 to +0.02321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 0.2593 | -82.8% | -1.405 to -1.089 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.4 | 3548 | +315.2% | +2282 to +3104 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.024 | 4.645 | +15.4% | +0.2942 to +0.9479 | yes: power given |
| pods started | 0.2 | 2 | +900.0% | +0.2621 to +3.338 | yes: power given |
| pod start wait, total (s) | 0.4 | 3 | +650.0% | +0.2109 to +4.989 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.13 | +465.0% | +0.3064 to +1.554 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.43 | 15.13 | -67.4% | -35.64 to -26.97 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 813.6 | 1504 | +84.9% | +624.6 to +757 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1158 | +1634400.0% | +1156 to +1160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1474 | +294660.0% | +1471 to +1476 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124 | 1158 | +833.5% | +964.1 to +1103 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*