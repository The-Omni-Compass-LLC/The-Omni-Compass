# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.932 | 4.804 |
| node-hours | 2.514 | 2.517 | 2.068 | 2.012 |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 269.1 | 269 | 268.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 269.1 | 235.4 | 231 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 156.6 | 162.9 | 129 | 138.2 |
| response time (ms), 95th percentile | 402.9 | 429.5 | 427.6 | 461.5 |
| response time (ms), 99th percentile | 574 | 625.2 | 610.3 | 681.4 |
| time over the response line (% of samples) | 3.288 | 3.672 | 3.554 | 3.929 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 3 | 3.2 | 4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 161.8 | 225.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.24 | 5.563 | 7.23 | 6.222 |
| utilisation (used / allocatable) | 0.0506 | 0.05005 | 0.06091 | 0.06215 |
| CPU used (cores), mean | 1.214 | 1.201 | 1.193 | 1.188 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03887 | 0.04456 |
| CPU used with Omni's own (cores), mean | 1.214 | 1.201 | 1.232 | 1.233 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 533 | 539.1 | 471.7 | 467 |
| HPA replicas, mean | 1.973 | 1.881 | 2.182 | 2.267 |
| pods started | 0 | 0.1 | 0.3 | 1 |
| pod start wait, total (s) | 0 | 0.2 | 0.6 | 2 |
| pod start wait, mean (s) | 0 | 0.2 | 0.35 | 0.89 |
| host CPU busy, the real machine under kind (%) | 34.29 | 34.78 | 35.74 | 37.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 727.7 | 730.7 | 727.9 | 731.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.971 | 3.734 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.09167 | 0.03333 | 0.07917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | 0.1 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 34.01 | 36.01 | 34.47 | 36.59 |
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
| worker nodes in service, mean | 6 | 4.804 | -19.9% | -1.631 to -0.7614 | yes: GAIN |
| node-hours | 2.517 | 2.012 | -20.1% | -0.6862 to -0.3254 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.1 | 268.5 | -0.2% | -1.354 to +0.297 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.1 | 231 | -14.2% | -51.9 to -24.3 | yes: GAIN |
| response time (ms), mean | 162.9 | 138.2 | -15.2% | -28.91 to -20.52 | yes: GAIN |
| response time (ms), 95th percentile | 429.5 | 461.5 | +7.5% | -0.9609 to +65.01 | no |
| response time (ms), 99th percentile | 625.2 | 681.4 | +9.0% | -7.974 to +120.3 | no |
| time over the response line (% of samples) | 3.672 | 3.929 | +7.0% | -0.291 to +0.8051 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 4 | +33.3% | +0.1079 to +1.892 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 225.5 | +226 (native is 0) | +178.9 to +272.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.563 | 6.222 | +11.8% | -1.17 to +2.487 | no |
| utilisation (used / allocatable) | 0.05005 | 0.06215 | +24.2% | +0.008054 to +0.01615 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.201 | 1.188 | -1.1% | -0.04287 to +0.01698 | no |
| Omni's own CPU (cores), mean | 0 | 0.04456 | +0.0446 (native is 0) | +0.03964 to +0.04948 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.201 | 1.233 | +2.6% | -0.0002963 to +0.06352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.1 | 467 | -13.4% | -97.23 to -47.02 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.881 | 2.267 | +20.5% | +0.0555 to +0.715 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | -0.2898 to +2.09 | no |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | -0.956 to +4.556 | no |
| pod start wait, mean (s) | 0.2 | 0.89 | +345.0% | -0.2711 to +1.651 | no |
| host CPU busy, the real machine under kind (%) | 34.78 | 37.02 | +6.5% | +1.87 to +2.616 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 730.7 | 731.5 | +0.1% | -0.845 to +2.445 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.734 | -37.8% | -3.182 to -1.35 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.07917 | -13.6% | -0.06701 to +0.04201 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 36.01 | 36.59 | +1.6% | -0.05533 to +1.214 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.599e-16 to +1.115e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.517 | +0.1% | -0.004302 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 269.1 | +0.0% | -0.6684 to +0.8558 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 269.1 | +0.0% | -0.6684 to +0.8558 | no |
| response time (ms), mean | 156.6 | 162.9 | +4.0% | -7.341 to +19.99 | no |
| response time (ms), 95th percentile | 402.9 | 429.5 | +6.6% | -30.12 to +83.23 | no |
| response time (ms), 99th percentile | 574 | 625.2 | +8.9% | -62.29 to +164.7 | no |
| time over the response line (% of samples) | 3.288 | 3.672 | +11.7% | -0.4919 to +1.261 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 3 | +11.1% | -0.7144 to +1.314 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.24 | 5.563 | -23.2% | -3.165 to -0.1884 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0506 | 0.05005 | -1.1% | -0.001665 to +0.0005598 | no |
| CPU used (cores), mean | 1.214 | 1.201 | -1.1% | -0.03996 to +0.01344 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.214 | 1.201 | -1.1% | -0.03996 to +0.01344 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 533 | 539.1 | +1.2% | -5.259 to +17.52 | no |
| HPA replicas, mean | 1.973 | 1.881 | -4.7% | -0.2899 to +0.1063 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 34.29 | 34.78 | +1.4% | -0.04474 to +1.028 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 727.7 | 730.7 | +0.4% | -2.147 to +8.147 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.09167 | +214.3% | +0.007633 to +0.1174 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 34.01 | 36.01 | +5.9% | -2.001 to +5.992 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.932 | -17.8% | -1.626 to -0.511 | yes: GAIN |
| node-hours | 2.514 | 2.068 | -17.7% | -0.6771 to -0.2153 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 269 | +0.0% | -0.5381 to +0.6279 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 235.4 | -12.5% | -51.02 to -16.19 | yes: GAIN |
| response time (ms), mean | 156.6 | 129 | -17.6% | -34.65 to -20.4 | yes: GAIN |
| response time (ms), 95th percentile | 402.9 | 427.6 | +6.1% | +3.648 to +45.71 | yes: LOSS |
| response time (ms), 99th percentile | 574 | 610.3 | +6.3% | -16.14 to +88.63 | no |
| time over the response line (% of samples) | 3.288 | 3.554 | +8.1% | -0.05871 to +0.5922 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 3.2 | +18.5% | -0.1952 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.8 | +162 (native is 0) | +116.3 to +207.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.24 | 7.23 | -0.1% | -1.069 to +1.049 | no |
| utilisation (used / allocatable) | 0.0506 | 0.06091 | +20.4% | +0.00495 to +0.01566 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.214 | 1.193 | -1.8% | -0.04482 to +0.002022 | no |
| Omni's own CPU (cores), mean | 0 | 0.03887 | +0.0389 (native is 0) | +0.0348 to +0.04294 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.214 | 1.232 | +1.4% | -0.00819 to +0.04313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 533 | 471.7 | -11.5% | -93.91 to -28.62 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.182 | +10.6% | -0.05978 to +0.4768 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.5285 to +1.728 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.35 (native is 0) | -0.2353 to +0.9353 | no |
| host CPU busy, the real machine under kind (%) | 34.29 | 35.74 | +4.2% | +0.8374 to +2.064 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 727.7 | 727.9 | +0.0% | -1.513 to +1.913 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.971 | -33.8% | -3.083 to -0.9753 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 | +14.3% | -0.01783 to +0.02616 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | -50.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 34.01 | 34.47 | +1.3% | -0.4583 to +1.367 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.932 | -17.8% | -1.626 to -0.511 | yes: GAIN |
| node-hours | 2.517 | 2.068 | -17.8% | -0.678 to -0.2204 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.1 | 269 | -0.0% | -1.122 to +1.025 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.1 | 235.4 | -12.5% | -50.96 to -16.44 | yes: GAIN |
| response time (ms), mean | 162.9 | 129 | -20.8% | -49.15 to -18.55 | yes: GAIN |
| response time (ms), 95th percentile | 429.5 | 427.6 | -0.4% | -49.29 to +45.53 | no |
| response time (ms), 99th percentile | 625.2 | 610.3 | -2.4% | -82.95 to +53.05 | no |
| time over the response line (% of samples) | 3.672 | 3.554 | -3.2% | -1.067 to +0.8316 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 3.2 | +6.7% | -1.006 to +1.406 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.8 | +162 (native is 0) | +116.3 to +207.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.563 | 7.23 | +30.0% | +0.1002 to +3.233 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05005 | 0.06091 | +21.7% | +0.005453 to +0.01626 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.201 | 1.193 | -0.7% | -0.04221 to +0.02594 | no |
| Omni's own CPU (cores), mean | 0 | 0.03887 | +0.0389 (native is 0) | +0.0348 to +0.04294 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.201 | 1.232 | +2.6% | -0.004098 to +0.06557 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.1 | 471.7 | -12.5% | -100.8 to -33.98 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.881 | 2.182 | +16.0% | -0.01259 to +0.6133 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | -0.8707 to +1.671 | no |
| pod start wait, mean (s) | 0.2 | 0.35 | +75.0% | -0.6417 to +0.9417 | no |
| host CPU busy, the real machine under kind (%) | 34.78 | 35.74 | +2.8% | +0.6308 to +1.287 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 730.7 | 727.9 | -0.4% | -6.858 to +1.258 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.971 | -33.8% | -3.083 to -0.9753 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.03333 | -63.6% | -0.09603 to -0.02063 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.1 | -80.0% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 36.01 | 34.47 | -4.3% | -4.691 to +1.608 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.804 | -19.9% | -1.631 to -0.7614 | yes: GAIN |
| node-hours | 2.514 | 2.012 | -20.0% | -0.6843 to -0.3213 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 268.5 | -0.2% | -1.145 to +0.2757 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 231 | -14.1% | -51.77 to -24.24 | yes: GAIN |
| response time (ms), mean | 156.6 | 138.2 | -11.7% | -32.12 to -4.668 | yes: GAIN |
| response time (ms), 95th percentile | 402.9 | 461.5 | +14.5% | -26.62 to +143.8 | no |
| response time (ms), 99th percentile | 574 | 681.4 | +18.7% | -67.07 to +281.8 | no |
| time over the response line (% of samples) | 3.288 | 3.929 | +19.5% | +0.07004 to +1.213 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 4 | +48.1% | -0.2099 to +2.81 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 225.5 | +226 (native is 0) | +178.9 to +272.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.24 | 6.222 | -14.1% | -2.302 to +0.2655 | no |
| utilisation (used / allocatable) | 0.0506 | 0.06215 | +22.8% | +0.00713 to +0.01597 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.214 | 1.188 | -2.2% | -0.04642 to -0.005998 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04456 | +0.0446 (native is 0) | +0.03964 to +0.04948 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.214 | 1.233 | +1.5% | -0.005147 to +0.04185 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 533 | 467 | -12.4% | -93.14 to -38.86 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.267 | +14.9% | -0.01299 to +0.5999 | no |
| pods started | 0 | 1 | +1 (native is 0) | -0.1184 to +2.118 | no |
| pod start wait, total (s) | 0 | 2 | +2 (native is 0) | -0.6336 to +4.634 | no |
| pod start wait, mean (s) | 0 | 0.89 | +0.89 (native is 0) | +0.1712 to +1.609 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 34.29 | 37.02 | +8.0% | +2.009 to +3.461 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 727.7 | 731.5 | +0.5% | -1.13 to +8.73 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.734 | -37.8% | -3.182 to -1.35 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.07917 | +171.4% | +0.02649 to +0.07351 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 34.01 | 36.59 | +7.6% | -2.023 to +7.173 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*