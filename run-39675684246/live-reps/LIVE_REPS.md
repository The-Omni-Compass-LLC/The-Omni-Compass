# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.93 | 4.802 |
| node-hours | 2.518 | 2.516 | 2.073 | 2.011 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.4 | 272.7 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.4 | 239 | 234.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 345.5 | 325.3 | 312.4 | 289.6 |
| response time (ms), 95th percentile | 1258 | 1367 | 1291 | 1365 |
| response time (ms), 99th percentile | 1818 | 1973 | 1820 | 1950 |
| time over the response line (% of samples) | 14.69 | 11.42 | 14.5 | 10.74 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.3 | 7.6 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.1 | 39.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.67 | 13.21 | 11.73 | 12.15 |
| utilisation (used / allocatable) | 0.0578 | 0.05907 | 0.0711 | 0.07363 |
| CPU used (cores), mean | 1.387 | 1.418 | 1.396 | 1.408 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01597 | 0.01658 |
| CPU used with Omni's own (cores), mean | 1.387 | 1.418 | 1.412 | 1.424 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 479.5 | 415 | 404.7 |
| HPA replicas, mean | 1.873 | 1.914 | 2.219 | 2.165 |
| pods started | 0.1 | 0 | 0.4 | 0.3 |
| pod start wait, total (s) | 0.2 | 0 | 0.8 | 0.5 |
| pod start wait, mean (s) | 0.2 | 0 | 0.8 | 0.3 |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.29 | 40.84 | 40.95 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 792.8 | 797.8 | 795.7 | 795.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.132 | 4.028 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2875 | 0.2083 | 0.1125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.2 | 1.2 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 97.74 | 104.5 | 100.2 | 103 |
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
| worker nodes in service, mean | 6 | 4.802 | -20.0% | -2.016 to -0.3807 | yes: GAIN |
| node-hours | 2.516 | 2.011 | -20.1% | -0.8502 to -0.1591 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272 | -0.2% | -1.419 to +0.5304 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 234.4 | -14.0% | -64.1 to -11.96 | yes: GAIN |
| response time (ms), mean | 325.3 | 289.6 | -11.0% | -75.24 to +3.778 | no |
| response time (ms), 95th percentile | 1367 | 1365 | -0.2% | -86.17 to +81.96 | no |
| response time (ms), 99th percentile | 1973 | 1950 | -1.2% | -164 to +117.2 | no |
| time over the response line (% of samples) | 11.42 | 10.74 | -6.0% | -2.394 to +1.033 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.3 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.9 | +39.9 (native is 0) | +23.49 to +56.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 12.15 | -8.1% | -5.106 to +2.976 | no |
| utilisation (used / allocatable) | 0.05907 | 0.07363 | +24.6% | +0.004143 to +0.02497 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.408 | -0.7% | -0.02701 to +0.006676 | no |
| Omni's own CPU (cores), mean | 0 | 0.01658 | +0.0166 (native is 0) | +0.01512 to +0.01804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.424 | +0.5% | -0.01058 to +0.0234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 404.7 | -15.6% | -127.7 to -21.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.914 | 2.165 | +13.1% | +0.1085 to +0.3923 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.4079 to +1.408 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 40.29 | 40.95 | +1.6% | +0.2176 to +1.094 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 797.8 | 795.6 | -0.3% | -8.202 to +3.802 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.028 | -32.9% | -3.244 to -0.6991 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 0.1125 | -60.9% | -0.5636 to +0.2136 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.2 | 0.7 | -68.2% | -4.668 to +1.668 | no |
| queue: job turnaround, submitted to done, mean (s) | 104.5 | 103 | -1.4% | -7.348 to +4.498 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.558e-15 to -2.185e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.516 | -0.1% | -0.007177 to +0.002177 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.4 | +0.1% | -0.7461 to +1.376 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.4 | +0.1% | -0.7461 to +1.376 | no |
| response time (ms), mean | 345.5 | 325.3 | -5.9% | -47.52 to +7.034 | no |
| response time (ms), 95th percentile | 1258 | 1367 | +8.7% | -1.739 to +219.7 | no |
| response time (ms), 99th percentile | 1818 | 1973 | +8.6% | -39.87 to +350.8 | no |
| time over the response line (% of samples) | 14.69 | 11.42 | -22.3% | -6.395 to -0.1466 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.3 | -3.9% | -0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.67 | 13.21 | +13.3% | -1.878 to +4.972 | no |
| utilisation (used / allocatable) | 0.0578 | 0.05907 | +2.2% | -0.000988 to +0.003536 | no |
| CPU used (cores), mean | 1.387 | 1.418 | +2.2% | -0.02371 to +0.08487 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.387 | 1.418 | +2.2% | -0.02371 to +0.08487 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 479.5 | -4.0% | -62.6 to +22.71 | no |
| HPA replicas, mean | 1.873 | 1.914 | +2.2% | -0.07453 to +0.1578 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.29 | +0.5% | -0.361 to +0.7546 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 792.8 | 797.8 | +0.6% | -1.153 to +11.15 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2875 | +176.0% | -0.173 to +0.5397 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.2 | +633.3% | -1.922 to +5.722 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.74 | 104.5 | +6.9% | -1.126 to +14.6 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.93 | -17.8% | -1.882 to -0.2572 | yes: GAIN |
| node-hours | 2.518 | 2.073 | -17.7% | -0.786 to -0.1053 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.7 | +0.2% | -0.148 to +1.384 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 239 | -12.2% | -58.36 to -7.852 | yes: GAIN |
| response time (ms), mean | 345.5 | 312.4 | -9.6% | -61.87 to -4.416 | yes: GAIN |
| response time (ms), 95th percentile | 1258 | 1291 | +2.6% | -132.5 to +198.5 | no |
| response time (ms), 99th percentile | 1818 | 1820 | +0.1% | -154.2 to +159.3 | no |
| time over the response line (% of samples) | 14.69 | 14.5 | -1.3% | -0.9165 to +0.5389 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.6 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.1 (native is 0) | +25.96 to +72.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.67 | 11.73 | +0.5% | -2.56 to +2.683 | no |
| utilisation (used / allocatable) | 0.0578 | 0.0711 | +23.0% | +0.002863 to +0.02374 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.387 | 1.396 | +0.6% | -0.03199 to +0.04937 | no |
| Omni's own CPU (cores), mean | 0 | 0.01597 | +0.016 (native is 0) | +0.01463 to +0.01731 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.387 | 1.412 | +1.8% | -0.01531 to +0.06463 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 415 | -16.9% | -160.4 to -8.522 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.873 | 2.219 | +18.5% | +0.1021 to +0.5897 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | -0.09105 to +1.291 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.84 | +1.9% | +0.2117 to +1.285 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 792.8 | 795.7 | +0.4% | -4.445 to +10.24 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.132 | -31.1% | -3.257 to -0.4781 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2083 | +100.0% | -0.1024 to +0.3108 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.2 | +300.0% | -0.9299 to +2.73 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.74 | 100.2 | +2.5% | -6.209 to +11.08 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.93 | -17.8% | -1.882 to -0.2572 | yes: GAIN |
| node-hours | 2.516 | 2.073 | -17.6% | -0.7864 to -0.09994 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.7 | +0.1% | -0.3925 to +0.9981 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 239 | -12.3% | -59.15 to -7.694 | yes: GAIN |
| response time (ms), mean | 325.3 | 312.4 | -4.0% | -37.67 to +11.86 | no |
| response time (ms), 95th percentile | 1367 | 1291 | -5.6% | -245.4 to +93.42 | no |
| response time (ms), 99th percentile | 1973 | 1820 | -7.7% | -351.5 to +45.69 | no |
| time over the response line (% of samples) | 11.42 | 14.5 | +27.0% | -0.1485 to +6.313 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.6 | +4.1% | -0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.1 (native is 0) | +25.96 to +72.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 11.73 | -11.2% | -3.648 to +0.678 | no |
| utilisation (used / allocatable) | 0.05907 | 0.0711 | +20.4% | +0.001734 to +0.02232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.396 | -1.5% | -0.04445 to +0.0006738 | no |
| Omni's own CPU (cores), mean | 0 | 0.01597 | +0.016 (native is 0) | +0.01463 to +0.01731 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.412 | -0.4% | -0.02881 to +0.01698 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 415 | -13.5% | -119.1 to -9.897 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.914 | 2.219 | +15.9% | +0.06575 to +0.5427 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | +0.06123 to +1.539 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.06123 to +1.539 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.29 | 40.84 | +1.4% | +0.2052 to +0.8977 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 797.8 | 795.7 | -0.3% | -6.331 to +2.131 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.132 | -31.1% | -3.257 to -0.4781 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 0.2083 | -27.5% | -0.2359 to +0.07757 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.2 | 1.2 | -45.5% | -3.051 to +1.051 | no |
| queue: job turnaround, submitted to done, mean (s) | 104.5 | 100.2 | -4.1% | -9.798 to +1.198 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.802 | -20.0% | -2.016 to -0.3807 | yes: GAIN |
| node-hours | 2.518 | 2.011 | -20.1% | -0.8501 to -0.1642 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | -0.0% | -1.158 to +0.9 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 234.4 | -13.9% | -63.37 to -12.07 | yes: GAIN |
| response time (ms), mean | 345.5 | 289.6 | -16.2% | -92.25 to -19.69 | yes: GAIN |
| response time (ms), 95th percentile | 1258 | 1365 | +8.5% | -37.13 to +250.8 | no |
| response time (ms), 99th percentile | 1818 | 1950 | +7.3% | -68.98 to +333.1 | no |
| time over the response line (% of samples) | 14.69 | 10.74 | -26.9% | -7.299 to -0.6045 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.3 | -3.9% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.9 | +39.9 (native is 0) | +23.49 to +56.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.67 | 12.15 | +4.1% | -0.8144 to +1.778 | no |
| utilisation (used / allocatable) | 0.0578 | 0.07363 | +27.4% | +0.005258 to +0.0264 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.387 | 1.408 | +1.5% | -0.0286 to +0.06942 | no |
| Omni's own CPU (cores), mean | 0 | 0.01658 | +0.0166 (native is 0) | +0.01512 to +0.01804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.387 | 1.424 | +2.7% | -0.01251 to +0.08649 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 404.7 | -19.0% | -169.6 to -19.83 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.873 | 2.165 | +15.6% | +0.1136 to +0.4705 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.95 | +2.1% | +0.4406 to +1.264 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 792.8 | 795.6 | +0.4% | -1.368 to +6.968 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.028 | -32.9% | -3.244 to -0.6991 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1125 | +8.0% | -0.03993 to +0.0566 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | -0.2911 to +1.091 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.74 | 103 | +5.4% | -1.27 to +11.89 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*