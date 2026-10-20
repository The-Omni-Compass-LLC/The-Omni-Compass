# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.884 | 5.948 |
| node-hours | 2.509 | 2.513 | 2.047 | 2.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 286.1 | 272 | 286.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 286.1 | 236.9 | 284.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 330.3 | 620.7 | 297.9 | 613.4 |
| response time (ms), 95th percentile | 1132 | 1305 | 1204 | 1356 |
| response time (ms), 99th percentile | 1583 | 1825 | 1738 | 1822 |
| time over the response line (% of samples) | 16.77 | 53.85 | 16.01 | 52.45 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 24.33 | 8.667 | 24.22 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 47.33 | 15.33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.41 | 2.422 | 10.93 | 2.47 |
| utilisation (used / allocatable) | 0.05804 | 0.09723 | 0.07239 | 0.09745 |
| CPU used (cores), mean | 1.393 | 2.334 | 1.404 | 2.32 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0191 | 0.008756 |
| CPU used with Omni's own (cores), mean | 1.393 | 2.334 | 1.423 | 2.329 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 293.6 | 405.7 | 293.2 |
| HPA replicas, mean | 1.961 | 2.032 | 2.055 | 2.12 |
| pods started | 0 | 0.1111 | 0.2222 | 0.5556 |
| pod start wait, total (s) | 0 | 0.2222 | 0.5556 | 1.111 |
| pod start wait, mean (s) | 0 | 0.2222 | 0.5556 | 0.7407 |
| host CPU busy, the real machine under kind (%) | 40.12 | 75.22 | 41.42 | 75.13 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 774.1 | 1474 | 780.1 | 1466 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.038 | 4.905 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03241 | 635 | 0.05093 | 637.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 1129 | 0.3333 | 1113 |
| queue: job turnaround, submitted to done, mean (s) | 81.79 | 954.8 | 87.35 | 955 |
| queue: jobs unfinished at the window's end | 0 | 14.33 | 0 | 13.44 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.948 | -0.9% | -0.1726 to +0.06819 | no |
| node-hours | 2.513 | 2.492 | -0.8% | -0.06822 to +0.02618 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 286.1 | -0.0% | -1.191 to +1.078 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 284.4 | -0.6% | -5.315 to +1.91 | no |
| response time (ms), mean | 620.7 | 613.4 | -1.2% | -63.31 to +48.69 | no |
| response time (ms), 95th percentile | 1305 | 1356 | +3.9% | -89.72 to +192.1 | no |
| response time (ms), 99th percentile | 1825 | 1822 | -0.2% | -218.9 to +213.2 | no |
| time over the response line (% of samples) | 53.85 | 52.45 | -2.6% | -5.104 to +2.302 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.33 | 24.22 | -0.5% | -0.3673 to +0.1451 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.33 | +15.3 (native is 0) | +12.14 to +18.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.422 | 2.47 | +2.0% | -0.157 to +0.2533 | no |
| utilisation (used / allocatable) | 0.09723 | 0.09745 | +0.2% | -0.001554 to +0.001989 | no |
| CPU used (cores), mean | 2.334 | 2.32 | -0.6% | -0.03492 to +0.007541 | no |
| Omni's own CPU (cores), mean | 0 | 0.008756 | +0.00876 (native is 0) | +0.007947 to +0.009564 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.334 | 2.329 | -0.2% | -0.02626 to +0.01639 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.6 | 293.2 | -0.1% | -4.469 to +3.779 | no |
| HPA replicas, mean | 2.032 | 2.12 | +4.3% | -0.1412 to +0.3163 | no |
| pods started | 0.1111 | 0.5556 | +400.0% | -0.4244 to +1.313 | no |
| pod start wait, total (s) | 0.2222 | 1.111 | +400.0% | -0.7163 to +2.494 | no |
| pod start wait, mean (s) | 0.2222 | 0.7407 | +233.3% | -0.6137 to +1.651 | no |
| host CPU busy, the real machine under kind (%) | 75.22 | 75.13 | -0.1% | -0.85 to +0.6656 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1474 | 1466 | -0.6% | -25.79 to +9.566 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.81 | -36.5% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 635 | 637.5 | +0.4% | -53.66 to +58.64 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1129 | 1113 | -1.4% | -97.8 to +66.48 | no |
| queue: job turnaround, submitted to done, mean (s) | 954.8 | 955 | +0.0% | -35.65 to +36.13 | no |
| queue: jobs unfinished at the window's end | 14.33 | 13.44 | -6.2% | -2.494 to +0.7163 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.975e-15 to -3.803e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.509 | 2.513 | +0.2% | -0.002086 to +0.009864 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 286.1 | +5.6% | +11.2 to +18.93 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 286.1 | +5.6% | +11.2 to +18.93 | yes: power given |
| response time (ms), mean | 330.3 | 620.7 | +87.9% | +201.6 to +379.2 | yes: LOSS |
| response time (ms), 95th percentile | 1132 | 1305 | +15.2% | -356.2 to +701.4 | no |
| response time (ms), 99th percentile | 1583 | 1825 | +15.3% | -484.9 to +968.4 | no |
| time over the response line (% of samples) | 16.77 | 53.85 | +221.2% | +30.76 to +43.41 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 24.33 | +204.2% | +11.67 to +20.99 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.41 | 2.422 | -78.8% | -12.93 to -5.06 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05804 | 0.09723 | +67.5% | +0.0286 to +0.04979 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.393 | 2.334 | +67.5% | +0.6865 to +1.195 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.393 | 2.334 | +67.5% | +0.6865 to +1.195 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 293.6 | -39.5% | -278.7 to -103.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.961 | 2.032 | +3.6% | -0.1282 to +0.2701 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | -0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| pod start wait, mean (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| host CPU busy, the real machine under kind (%) | 40.12 | 75.22 | +87.5% | +30.03 to +40.17 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.1 | 1474 | +90.4% | +622.1 to +777.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03241 | 635 | +1959438.6% | +368.6 to +901.4 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 1129 | +1015791.5% | +761 to +1496 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.79 | 954.8 | +1067.4% | +721.8 to +1024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.33 | +14.3 (native is 0) | +8.22 to +20.45 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.884 | -18.6% | -1.927 to -0.3061 | yes: GAIN |
| node-hours | 2.509 | 2.047 | -18.4% | -0.8003 to -0.1253 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 272 | +0.3% | -0.487 to +2.365 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 236.9 | -12.6% | -59.14 to -9.261 | yes: GAIN |
| response time (ms), mean | 330.3 | 297.9 | -9.8% | -49.21 to -15.63 | yes: GAIN |
| response time (ms), 95th percentile | 1132 | 1204 | +6.3% | -8.824 to +151.4 | no |
| response time (ms), 99th percentile | 1583 | 1738 | +9.8% | +23.89 to +285 | yes: LOSS |
| time over the response line (% of samples) | 16.77 | 16.01 | -4.5% | -1.699 to +0.1851 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.667 | +8.3% | -0.102 to +1.435 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.33 | +47.3 (native is 0) | +35.65 to +59.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.41 | 10.93 | -4.3% | -3.1 to +2.122 | no |
| utilisation (used / allocatable) | 0.05804 | 0.07239 | +24.7% | +0.0033 to +0.0254 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.393 | 1.404 | +0.8% | -0.04521 to +0.06737 | no |
| Omni's own CPU (cores), mean | 0 | 0.0191 | +0.0191 (native is 0) | +0.016 to +0.0222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.393 | 1.423 | +2.2% | -0.02613 to +0.08649 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 405.7 | -16.3% | -154.7 to -3.697 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.961 | 2.055 | +4.8% | -0.04907 to +0.237 | no |
| pods started | 0 | 0.2222 | +0.222 (native is 0) | -0.1167 to +0.5612 | no |
| pod start wait, total (s) | 0 | 0.5556 | +0.556 (native is 0) | -0.3133 to +1.424 | no |
| pod start wait, mean (s) | 0 | 0.5556 | +0.556 (native is 0) | -0.3133 to +1.424 | no |
| host CPU busy, the real machine under kind (%) | 40.12 | 41.42 | +3.2% | +0.7395 to +1.867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.1 | 780.1 | +0.8% | +0.7303 to +11.27 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.038 | -32.7% | -3.243 to -0.6802 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03241 | 0.05093 | +57.1% | -0.01769 to +0.05472 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 0.3333 | +200.0% | -0.1167 to +0.5612 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.79 | 87.35 | +6.8% | -0.4649 to +11.59 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.884 | -18.6% | -1.927 to -0.3061 | yes: GAIN |
| node-hours | 2.513 | 2.047 | -18.6% | -0.8009 to -0.1325 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 272 | -4.9% | -17.29 to -10.96 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 236.9 | -17.2% | -77.09 to -21.43 | yes: GAIN |
| response time (ms), mean | 620.7 | 297.9 | -52.0% | -403.3 to -242.3 | yes: GAIN |
| response time (ms), 95th percentile | 1305 | 1204 | -7.8% | -612.3 to +409.7 | no |
| response time (ms), 99th percentile | 1825 | 1738 | -4.8% | -836 to +661.3 | no |
| time over the response line (% of samples) | 53.85 | 16.01 | -70.3% | -44.64 to -31.05 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.33 | 8.667 | -64.4% | -20.03 to -11.3 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.33 | +47.3 (native is 0) | +35.65 to +59.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.422 | 10.93 | +351.1% | +4.8 to +12.21 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09723 | 0.07239 | -25.6% | -0.03003 to -0.01967 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.334 | 1.404 | -39.8% | -1.159 to -0.7002 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0191 | +0.0191 (native is 0) | +0.016 to +0.0222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.334 | 1.423 | -39.0% | -1.141 to -0.6802 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.6 | 405.7 | +38.2% | +92.01 to +132.2 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.032 | 2.055 | +1.1% | -0.1431 to +0.1891 | no |
| pods started | 0.1111 | 0.2222 | +100.0% | -0.3508 to +0.573 | no |
| pod start wait, total (s) | 0.2222 | 0.5556 | +150.0% | -0.7537 to +1.42 | no |
| pod start wait, mean (s) | 0.2222 | 0.5556 | +150.0% | -0.7537 to +1.42 | no |
| host CPU busy, the real machine under kind (%) | 75.22 | 41.42 | -44.9% | -38.44 to -29.16 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1474 | 780.1 | -47.1% | -770.2 to -617.1 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | -66.7% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 635 | 0.05093 | -100.0% | -901.3 to -368.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1129 | 0.3333 | -100.0% | -1496 to -760.9 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 954.8 | 87.35 | -90.9% | -1016 to -719.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.33 | 0 | -100.0% | -20.45 to -8.22 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.948 | -0.9% | -0.1726 to +0.06819 | no |
| node-hours | 2.509 | 2.492 | -0.7% | -0.06677 to +0.03252 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 286.1 | +5.5% | +10.95 to +19.06 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 284.4 | +4.9% | +7.701 to +19.02 | yes: power given |
| response time (ms), mean | 330.3 | 613.4 | +85.7% | +225.1 to +341.1 | yes: LOSS |
| response time (ms), 95th percentile | 1132 | 1356 | +19.8% | -246.9 to +694.5 | no |
| response time (ms), 99th percentile | 1583 | 1822 | +15.1% | -491.3 to +969.1 | no |
| time over the response line (% of samples) | 16.77 | 52.45 | +212.8% | +29.43 to +41.94 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 24.22 | +202.8% | +11.68 to +20.77 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.33 | +15.3 (native is 0) | +12.14 to +18.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.41 | 2.47 | -78.4% | -12.74 to -5.145 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05804 | 0.09745 | +67.9% | +0.02883 to +0.05 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.393 | 2.32 | +66.6% | +0.6732 to +1.181 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.008756 | +0.00876 (native is 0) | +0.007947 to +0.009564 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.393 | 2.329 | +67.2% | +0.6826 to +1.189 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 293.2 | -39.5% | -279.5 to -103.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.961 | 2.12 | +8.1% | +0.00939 to +0.3076 | yes: power given |
| pods started | 0 | 0.5556 | +0.556 (native is 0) | -0.2237 to +1.335 | no |
| pod start wait, total (s) | 0 | 1.111 | +1.11 (native is 0) | -0.2981 to +2.52 | no |
| pod start wait, mean (s) | 0 | 0.7407 | +0.741 (native is 0) | -0.154 to +1.635 | no |
| host CPU busy, the real machine under kind (%) | 40.12 | 75.13 | +87.3% | +30.45 to +39.58 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.1 | 1466 | +89.3% | +617.3 to +765.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.905 | -18.3% | -15.01 to +12.82 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03241 | 637.5 | +1967119.6% | +360.3 to +914.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 1113 | +1001696.3% | +692.7 to +1533 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.79 | 955 | +1067.6% | +729.2 to +1017 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.44 | +13.4 (native is 0) | +7.163 to +19.73 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*