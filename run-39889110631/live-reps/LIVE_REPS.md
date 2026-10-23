# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.441 | 5.36 |
| node-hours | 2.514 | 2.517 | 2.284 | 2.244 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.3 | 272.3 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.3 | 254.7 | 251.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 298 | 351.5 | 286.2 | 332.4 |
| response time (ms), 95th percentile | 961.5 | 1474 | 1101 | 1594 |
| response time (ms), 99th percentile | 1412 | 2377 | 1666 | 2553 |
| time over the response line (% of samples) | 17.17 | 14.48 | 17.55 | 14.59 |
| failed requests (%) | 0 | 0 | 0 | 0.0102 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.7 | 9.1 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 126.6 | 92.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 16.01 | 10.38 | 16.84 |
| utilisation (used / allocatable) | 0.05857 | 0.05876 | 0.06442 | 0.06632 |
| CPU used (cores), mean | 1.406 | 1.41 | 1.403 | 1.412 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04908 | 0.0532 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.41 | 1.452 | 1.466 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.5 | 468.7 | 436.4 | 428.1 |
| HPA replicas, mean | 2.007 | 1.955 | 2.62 | 2.507 |
| pods started | 0.1 | 0 | 0.9 | 1.3 |
| pod start wait, total (s) | 0.2 | 0 | 2 | 2.5 |
| pod start wait, mean (s) | 0.2 | 0 | 0.9167 | 0.82 |
| host CPU busy, the real machine under kind (%) | 39.91 | 42.2 | 41.86 | 44.56 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 760.1 | 791.1 | 768.4 | 800.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.965 | 4.852 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7958 | 0.05417 | 0.8083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | 0.4 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 100.9 | 75.24 | 111.2 |
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
| worker nodes in service, mean | 6 | 5.36 | -10.7% | -1.362 to +0.08189 | no |
| node-hours | 2.517 | 2.244 | -10.9% | -0.5766 to +0.02932 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.8 | -0.2% | -1.189 to +0.1611 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 251.7 | -7.6% | -43.7 to +2.573 | no |
| response time (ms), mean | 351.5 | 332.4 | -5.5% | -52.75 to +14.42 | no |
| response time (ms), 95th percentile | 1474 | 1594 | +8.1% | -99.81 to +339.2 | no |
| response time (ms), 99th percentile | 2377 | 2553 | +7.4% | -122.2 to +474.4 | no |
| time over the response line (% of samples) | 14.48 | 14.59 | +0.7% | -1.197 to +1.401 | no |
| failed requests (%) | 0 | 0.0102 | +0.0102 (native is 0) | -0.01288 to +0.03329 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 92.3 | +92.3 (native is 0) | +75.19 to +109.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.01 | 16.84 | +5.2% | -0.9356 to +2.592 | no |
| utilisation (used / allocatable) | 0.05876 | 0.06632 | +12.9% | +7.054e-05 to +0.01505 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.41 | 1.412 | +0.1% | -0.03167 to +0.03589 | no |
| Omni's own CPU (cores), mean | 0 | 0.0532 | +0.0532 (native is 0) | +0.04596 to +0.06044 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.466 | +3.9% | +0.01566 to +0.09496 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 428.1 | -8.7% | -79.28 to -1.924 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.507 | +28.3% | +0.2121 to +0.8927 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.03607 to +2.564 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.5 (native is 0) | -0.2652 to +5.265 | no |
| pod start wait, mean (s) | 0 | 0.82 | +0.82 (native is 0) | +0.1315 to +1.509 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.2 | 44.56 | +5.6% | +1.651 to +3.064 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.1 | 800.9 | +1.2% | +1.625 to +17.98 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.852 | -19.1% | -2.425 to +0.1295 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.8083 | +1.6% | -0.07969 to +0.1047 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.5 | -6.3% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 111.2 | +10.2% | +1.57 to +19.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.471e-15 to +2.28e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.517 | +0.2% | -0.002476 to +0.01014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.3 | +0.2% | +0.007989 to +1.23 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.3 | +0.2% | +0.007989 to +1.23 | yes: power given |
| response time (ms), mean | 298 | 351.5 | +18.0% | +13.35 to +93.75 | yes: LOSS |
| response time (ms), 95th percentile | 961.5 | 1474 | +53.3% | +155.7 to +870 | yes: LOSS |
| response time (ms), 99th percentile | 1412 | 2377 | +68.3% | +399.6 to +1530 | yes: LOSS |
| time over the response line (% of samples) | 17.17 | 14.48 | -15.6% | -5.72 to +0.3523 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.7 | +5.4% | -0.1952 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 16.01 | +48.3% | +3.561 to +6.866 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05857 | 0.05876 | +0.3% | -0.0006933 to +0.001076 | no |
| CPU used (cores), mean | 1.406 | 1.41 | +0.3% | -0.01664 to +0.02582 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.406 | 1.41 | +0.3% | -0.01664 to +0.02582 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.5 | 468.7 | -0.2% | -7.546 to +5.936 | no |
| HPA replicas, mean | 2.007 | 1.955 | -2.6% | -0.2833 to +0.1802 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 39.91 | 42.2 | +5.7% | +1.76 to +2.811 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 760.1 | 791.1 | +4.1% | +16.09 to +45.91 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7958 | +1636.4% | +0.6527 to +0.8473 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | +433.3% | +0.9545 to +1.646 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 100.9 | +49.5% | +17.57 to +49.22 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.441 | -9.3% | -1.18 to +0.06192 | no |
| node-hours | 2.514 | 2.284 | -9.1% | -0.4905 to +0.03081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.3 | +0.2% | -0.3106 to +1.639 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 254.7 | -6.2% | -36.94 to +3.059 | no |
| response time (ms), mean | 298 | 286.2 | -3.9% | -25.41 to +1.948 | no |
| response time (ms), 95th percentile | 961.5 | 1101 | +14.5% | +34.23 to +245.4 | yes: LOSS |
| response time (ms), 99th percentile | 1412 | 1666 | +18.0% | +96.9 to +411.5 | yes: LOSS |
| time over the response line (% of samples) | 17.17 | 17.55 | +2.3% | -0.5103 to +1.283 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.1 | -1.1% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 126.6 | +127 (native is 0) | +73.74 to +179.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 10.38 | -3.8% | -2.47 to +1.643 | no |
| utilisation (used / allocatable) | 0.05857 | 0.06442 | +10.0% | +0.000159 to +0.01155 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.403 | -0.2% | -0.04283 to +0.03658 | no |
| Omni's own CPU (cores), mean | 0 | 0.04908 | +0.0491 (native is 0) | +0.04434 to +0.05382 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.452 | +3.3% | +0.004134 to +0.08777 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.5 | 436.4 | -7.1% | -66.07 to -0.1826 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 2.62 | +30.6% | +0.1302 to +1.096 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | -0.2003 to +1.8 | no |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | -0.406 to +4.006 | no |
| pod start wait, mean (s) | 0.2 | 0.9167 | +358.3% | -0.3989 to +1.832 | no |
| host CPU busy, the real machine under kind (%) | 39.91 | 41.86 | +4.9% | +1.254 to +2.636 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 760.1 | 768.4 | +1.1% | +2.738 to +13.86 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.965 | -17.3% | -2.173 to +0.1019 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05417 | +18.2% | -0.04386 to +0.06053 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 75.24 | +11.5% | +2.205 to +13.34 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.441 | -9.3% | -1.18 to +0.06192 | no |
| node-hours | 2.517 | 2.284 | -9.3% | -0.4943 to +0.02689 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.3 | +0.0% | -0.8086 to +0.8991 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 254.7 | -6.4% | -37.55 to +2.434 | no |
| response time (ms), mean | 351.5 | 286.2 | -18.6% | -94.56 to -36.01 | yes: GAIN |
| response time (ms), 95th percentile | 1474 | 1101 | -25.3% | -632.9 to -113.2 | yes: GAIN |
| response time (ms), 99th percentile | 2377 | 1666 | -29.9% | -1139 to -282 | yes: GAIN |
| time over the response line (% of samples) | 14.48 | 17.55 | +21.2% | +0.477 to +5.664 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.1 | -6.2% | -0.9694 to -0.2306 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 126.6 | +127 (native is 0) | +73.74 to +179.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.01 | 10.38 | -35.1% | -7.986 to -3.267 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05876 | 0.06442 | +9.6% | -0.0001113 to +0.01143 | no |
| CPU used (cores), mean | 1.41 | 1.403 | -0.5% | -0.04324 to +0.02781 | no |
| Omni's own CPU (cores), mean | 0 | 0.04908 | +0.0491 (native is 0) | +0.04434 to +0.05382 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.452 | +2.9% | +0.004191 to +0.07854 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 436.4 | -6.9% | -65.56 to +0.9198 | no |
| HPA replicas, mean | 1.955 | 2.62 | +34.0% | +0.305 to +1.025 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | -0.02037 to +1.82 | no |
| pod start wait, total (s) | 0 | 2 | +2 (native is 0) | -0.0511 to +4.051 | no |
| pod start wait, mean (s) | 0 | 0.9167 | +0.917 (native is 0) | +0.004825 to +1.829 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.2 | 41.86 | -0.8% | -0.8544 to +0.1735 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.1 | 768.4 | -2.9% | -32.91 to -12.49 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.965 | -17.3% | -2.173 to +0.1019 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.05417 | -93.2% | -0.8503 to -0.633 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.4 | -75.0% | -1.652 to -0.7476 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 75.24 | -25.4% | -37.32 to -13.92 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.36 | -10.7% | -1.362 to +0.08189 | no |
| node-hours | 2.514 | 2.244 | -10.7% | -0.5739 to +0.03424 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 | +0.0% | -0.6849 to +0.894 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 251.7 | -7.3% | -43.18 to +3.298 | no |
| response time (ms), mean | 298 | 332.4 | +11.5% | -1.571 to +70.34 | no |
| response time (ms), 95th percentile | 961.5 | 1594 | +65.8% | +256.3 to +1009 | yes: LOSS |
| response time (ms), 99th percentile | 1412 | 2553 | +80.8% | +451.2 to +1831 | yes: LOSS |
| time over the response line (% of samples) | 17.17 | 14.59 | -15.0% | -4.84 to -0.3244 | yes: GAIN |
| failed requests (%) | 0 | 0.0102 | +0.0102 (native is 0) | -0.01288 to +0.03329 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.7 | +5.4% | -0.1079 to +1.108 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 92.3 | +92.3 (native is 0) | +75.19 to +109.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 16.84 | +56.0% | +3.089 to +8.994 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05857 | 0.06632 | +13.2% | +0.0003971 to +0.0151 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.412 | +0.5% | -0.02588 to +0.03928 | no |
| Omni's own CPU (cores), mean | 0 | 0.0532 | +0.0532 (native is 0) | +0.04596 to +0.06044 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.466 | +4.3% | +0.02049 to +0.09931 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.5 | 428.1 | -8.8% | -79.13 to -3.677 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 2.507 | +25.0% | +0.01937 to +0.9823 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.09185 to +2.308 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | -0.1327 to +4.733 | no |
| pod start wait, mean (s) | 0.2 | 0.82 | +310.0% | +0.01594 to +1.224 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.91 | 44.56 | +11.6% | +3.679 to +5.608 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 760.1 | 800.9 | +5.4% | +19.47 to +62.13 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.852 | -19.1% | -2.425 to +0.1295 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.8083 | +1663.6% | +0.6165 to +0.9085 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.5 | +400.0% | +0.7476 to +1.652 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 111.2 | +64.8% | +21.97 to +65.49 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*