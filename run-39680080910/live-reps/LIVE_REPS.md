# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.43 | 11.59 |
| node-hours | 5.028 | 5.023 | 4.79 | 4.858 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 527 | 526.3 | 528.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 527 | 508.5 | 515.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 628.6 | 962.2 | 609.9 | 1060 |
| response time (ms), 95th percentile | 2530 | 3764 | 2645 | 4457 |
| response time (ms), 99th percentile | 3503 | 5247 | 3704 | 5988 |
| time over the response line (% of samples) | 27.02 | 35.35 | 26.6 | 35.51 |
| failed requests (%) | 0 | 0.1099 | 0 | 0.09696 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 15.5 | 13.6 | 16.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 52.3 | 50.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 29.7 | 15.18 | 27.66 |
| utilisation (used / allocatable) | 0.03545 | 0.03726 | 0.03753 | 0.03996 |
| CPU used (cores), mean | 1.701 | 1.788 | 1.71 | 1.856 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01209 | 0.01251 |
| CPU used with Omni's own (cores), mean | 1.701 | 1.788 | 1.723 | 1.869 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751 | 720.3 | 715.9 | 670.6 |
| HPA replicas, mean | 4.138 | 3.953 | 4.736 | 4.611 |
| pods started | 0.1 | 0.1 | 1.5 | 2.3 |
| pod start wait, total (s) | 0.2 | 0.2 | 2.3 | 4.4 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.35 | 1.575 |
| host CPU busy, the real machine under kind (%) | 51.59 | 59.21 | 53.25 | 62.05 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 872.8 | 1021 | 886.1 | 1052 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.99 | 11.28 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 5.037 | 0.07917 | 10.23 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 25.5 | 0.5 | 55.2 |
| queue: job turnaround, submitted to done, mean (s) | 182.6 | 291.6 | 192.3 | 341.7 |
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
| worker nodes in service, mean | 12 | 11.59 | -3.4% | -1.306 to +0.4794 | no |
| node-hours | 5.023 | 4.858 | -3.3% | -0.5396 to +0.2091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 528.9 | +0.4% | +0.3737 to +3.468 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 515.9 | -2.1% | -39.17 to +16.98 | no |
| response time (ms), mean | 962.2 | 1060 | +10.1% | +9.037 to +186.1 | yes: LOSS |
| response time (ms), 95th percentile | 3764 | 4457 | +18.4% | +332.4 to +1053 | yes: LOSS |
| response time (ms), 99th percentile | 5247 | 5988 | +14.1% | +241.5 to +1240 | yes: LOSS |
| time over the response line (% of samples) | 35.35 | 35.51 | +0.5% | -1.353 to +1.679 | no |
| failed requests (%) | 0.1099 | 0.09696 | -11.8% | -0.2647 to +0.2387 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.5 | 16.4 | +5.8% | +0.3722 to +1.428 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | +50.4 (native is 0) | +21.91 to +78.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 29.7 | 27.66 | -6.9% | -19.39 to +15.32 | no |
| utilisation (used / allocatable) | 0.03726 | 0.03996 | +7.2% | +7.298e-05 to +0.005324 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.788 | 1.856 | +3.8% | +0.02528 to +0.1109 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01251 | +0.0125 (native is 0) | +0.01143 to +0.01359 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.788 | 1.869 | +4.5% | +0.0385 to +0.1227 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 670.6 | -6.9% | -103.9 to +4.483 | no |
| HPA replicas, mean | 3.953 | 4.611 | +16.6% | +0.3421 to +0.9741 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +1.2 to +3.2 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.4 | +2100.0% | +1.423 to +6.977 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.575 | +687.5% | +0.8469 to +1.903 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.21 | 62.05 | +4.8% | +1.678 to +4.017 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1021 | 1052 | +3.0% | -8.022 to +70.22 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 11.28 | -6.0% | -2.221 to +0.7911 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.037 | 10.23 | +103.1% | -4.156 to +14.54 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 25.5 | 55.2 | +116.5% | -29.42 to +88.82 | no |
| queue: job turnaround, submitted to done, mean (s) | 291.6 | 341.7 | +17.2% | +16.12 to +84.11 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -3.258e-15 to +2.903e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.028 | 5.023 | -0.1% | -0.02067 to +0.01067 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 527 | +0.1% | -1.121 to +2.62 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 527 | +0.1% | -1.121 to +2.62 | no |
| response time (ms), mean | 628.6 | 962.2 | +53.1% | +191.6 to +475.6 | yes: LOSS |
| response time (ms), 95th percentile | 2530 | 3764 | +48.8% | +684 to +1786 | yes: LOSS |
| response time (ms), 99th percentile | 3503 | 5247 | +49.8% | +1013 to +2474 | yes: LOSS |
| time over the response line (% of samples) | 27.02 | 35.35 | +30.8% | +4.71 to +11.94 | yes: LOSS |
| failed requests (%) | 0 | 0.1099 | +0.11 (native is 0) | -0.104 to +0.3239 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 15.5 | +14.8% | +1.174 to +2.826 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 29.7 | +96.5% | -3.335 to +32.51 | no |
| utilisation (used / allocatable) | 0.03545 | 0.03726 | +5.1% | +0.0001366 to +0.003488 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.701 | 1.788 | +5.1% | +0.006559 to +0.1674 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.701 | 1.788 | +5.1% | +0.006559 to +0.1674 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751 | 720.3 | -4.1% | -61.75 to +0.318 | no |
| HPA replicas, mean | 4.138 | 3.953 | -4.5% | -0.2999 to -0.07061 | yes: GAIN |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 51.59 | 59.21 | +14.8% | +5.694 to +9.534 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 1021 | +17.0% | +83.18 to +213.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 5.038 | +6616.7% | -1.028 to +10.95 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 25.5 | +4150.0% | -21.13 to +70.93 | no |
| queue: job turnaround, submitted to done, mean (s) | 182.6 | 291.6 | +59.7% | +65.84 to +152.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.43 | -4.7% | -1.606 to +0.4718 | no |
| node-hours | 5.028 | 4.79 | -4.7% | -0.67 to +0.1932 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 526.3 | +0.0% | -1.475 to +1.693 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 508.5 | -3.4% | -49.9 to +14.51 | no |
| response time (ms), mean | 628.6 | 609.9 | -3.0% | -42.78 to +5.377 | no |
| response time (ms), 95th percentile | 2530 | 2645 | +4.6% | -44.63 to +275 | no |
| response time (ms), 99th percentile | 3503 | 3704 | +5.7% | -91.33 to +492 | no |
| time over the response line (% of samples) | 27.02 | 26.6 | -1.6% | -1.349 to +0.5035 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 13.6 | +0.7% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.3 | +52.3 (native is 0) | +20.15 to +84.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 15.18 | +0.4% | -1.762 to +1.895 | no |
| utilisation (used / allocatable) | 0.03545 | 0.03753 | +5.9% | -0.001329 to +0.005503 | no |
| CPU used (cores), mean | 1.701 | 1.71 | +0.5% | -0.02084 to +0.03895 | no |
| Omni's own CPU (cores), mean | 0 | 0.01209 | +0.0121 (native is 0) | +0.0113 to +0.01288 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.701 | 1.723 | +1.2% | -0.008755 to +0.05104 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751 | 715.9 | -4.7% | -93.57 to +23.33 | no |
| HPA replicas, mean | 4.138 | 4.736 | +14.4% | +0.4271 to +0.768 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.7089 to +2.091 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.3 | +1050.0% | +0.7324 to +3.468 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.35 | +575.0% | +0.2731 to +2.027 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.59 | 53.25 | +3.2% | +1.073 to +2.249 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 886.1 | +1.5% | -0.2596 to +26.86 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.99 | -8.4% | -2.75 to +0.734 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.07917 | +5.6% | -0.05452 to +0.06286 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 182.6 | 192.3 | +5.3% | +0.3125 to +19.12 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.43 | -4.7% | -1.606 to +0.4718 | no |
| node-hours | 5.023 | 4.79 | -4.6% | -0.6714 to +0.2046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 526.3 | -0.1% | -2.746 to +1.465 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 508.5 | -3.5% | -50.87 to +13.97 | no |
| response time (ms), mean | 962.2 | 609.9 | -36.6% | -487.3 to -217.3 | yes: GAIN |
| response time (ms), 95th percentile | 3764 | 2645 | -29.7% | -1591 to -647.8 | yes: GAIN |
| response time (ms), 99th percentile | 5247 | 3704 | -29.4% | -2288 to -798.4 | yes: GAIN |
| time over the response line (% of samples) | 35.35 | 26.6 | -24.7% | -12.2 to -5.297 | yes: GAIN |
| failed requests (%) | 0.1099 | 0 | -100.0% | -0.3239 to +0.104 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.5 | 13.6 | -12.3% | -2.611 to -1.189 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.3 | +52.3 (native is 0) | +20.15 to +84.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 29.7 | 15.18 | -48.9% | -32.57 to +3.526 | no |
| utilisation (used / allocatable) | 0.03726 | 0.03753 | +0.7% | -0.004151 to +0.004699 | no |
| CPU used (cores), mean | 1.788 | 1.71 | -4.4% | -0.1619 to +0.005994 | no |
| Omni's own CPU (cores), mean | 0 | 0.01209 | +0.0121 (native is 0) | +0.0113 to +0.01288 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.788 | 1.723 | -3.7% | -0.1501 to +0.01842 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 715.9 | -0.6% | -85.57 to +76.76 | no |
| HPA replicas, mean | 3.953 | 4.736 | +19.8% | +0.5462 to +1.019 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.8999 to +1.9 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.3 | +1050.0% | +0.9102 to +3.29 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.35 | +575.0% | +0.4141 to +1.886 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.21 | 53.25 | -10.1% | -7.778 to -4.129 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1021 | 886.1 | -13.2% | -195.7 to -74.51 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.99 | -8.4% | -2.75 to +0.734 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.037 | 0.07917 | -98.4% | -10.93 to +1.015 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 25.5 | 0.5 | -98.0% | -71.05 to +21.05 | no |
| queue: job turnaround, submitted to done, mean (s) | 291.6 | 192.3 | -34.1% | -137.8 to -60.8 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.59 | -3.4% | -1.306 to +0.4794 | no |
| node-hours | 5.028 | 4.858 | -3.4% | -0.5393 to +0.1988 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 528.9 | +0.5% | +0.08221 to +5.258 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 515.9 | -2.0% | -38.43 to +17.73 | no |
| response time (ms), mean | 628.6 | 1060 | +68.6% | +259 to +603.3 | yes: LOSS |
| response time (ms), 95th percentile | 2530 | 4457 | +76.2% | +1108 to +2747 | yes: LOSS |
| response time (ms), 99th percentile | 3503 | 5988 | +70.9% | +1556 to +3412 | yes: LOSS |
| time over the response line (% of samples) | 27.02 | 35.51 | +31.4% | +5.094 to +11.88 | yes: LOSS |
| failed requests (%) | 0 | 0.09696 | +0.097 (native is 0) | +0.003267 to +0.1906 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 16.4 | +21.5% | +1.863 to +3.937 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | +50.4 (native is 0) | +21.91 to +78.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 27.67 | +83.1% | +0.2043 to +24.9 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03545 | 0.03996 | +12.7% | +0.00196 to +0.007062 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.701 | 1.856 | +9.1% | +0.05235 to +0.2578 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01251 | +0.0125 (native is 0) | +0.01143 to +0.01359 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.701 | 1.869 | +9.8% | +0.06535 to +0.2698 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751 | 670.6 | -10.7% | -125.4 to -35.41 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.138 | 4.611 | +11.4% | +0.1513 to +0.7943 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +0.9474 to +3.453 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.4 | +2100.0% | +0.9342 to +7.466 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.575 | +687.5% | +0.7484 to +2.002 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.59 | 62.05 | +20.3% | +8.347 to +12.58 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 1052 | +20.6% | +122.3 to +236.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.28 | -6.0% | -2.221 to +0.7911 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 10.23 | +13538.9% | -0.5773 to +20.89 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 55.2 | +9100.0% | -25.22 to +134.4 | no |
| queue: job turnaround, submitted to done, mean (s) | 182.6 | 341.7 | +87.2% | +106.4 to +211.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*