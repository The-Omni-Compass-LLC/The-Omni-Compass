# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.613 | 6 |
| node-hours | 2.512 | 2.518 | 2.353 | 2.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.9 | 273.6 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.9 | 261.5 | 272.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 400.1 | 162.6 | 360.1 | 118 |
| response time (ms), 95th percentile | 1412 | 293.6 | 1444 | 258.6 |
| response time (ms), 99th percentile | 2041 | 408.5 | 2165 | 374.8 |
| time over the response line (% of samples) | 22.2 | 0.6996 | 21.69 | 0.3214 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 1.1 | 12.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 28.1 | 11.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 1307 | 11.82 | 1312 |
| utilisation (used / allocatable) | 0.0624 | 0.06044 | 0.06737 | 0.06038 |
| CPU used (cores), mean | 1.498 | 1.45 | 1.512 | 1.449 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01703 | 0.01265 |
| CPU used with Omni's own (cores), mean | 1.498 | 1.45 | 1.529 | 1.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.2 | 448.6 | 415.2 | 448.9 |
| HPA replicas, mean | 2.002 | 2.112 | 2.211 | 2.039 |
| pods started | 0 | 0.1 | 0.3 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 | 0.5 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 | 0.5 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.1 | 45.75 | 44.03 | 46.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 782.8 | 1510 | 788.1 | 1509 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.226 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 178.4 | 0.04583 | 186 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 757.1 | 0.3 | 814.4 |
| queue: job turnaround, submitted to done, mean (s) | 92.04 | 943.4 | 95.8 | 949.1 |
| queue: jobs unfinished at the window's end | 0 | 14.2 | 0 | 14.4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.517 | -0.0% | -0.009854 to +0.007854 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.8 | -0.0% | -1.029 to +0.7622 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.8 | -0.0% | -1.029 to +0.7622 | no |
| response time (ms), mean | 162.6 | 118 | -27.4% | -56.54 to -32.56 | yes: GAIN |
| response time (ms), 95th percentile | 293.6 | 258.6 | -11.9% | -74.06 to +4.07 | no |
| response time (ms), 99th percentile | 408.5 | 374.8 | -8.3% | -85.42 to +18 | no |
| time over the response line (% of samples) | 0.6996 | 0.3214 | -54.1% | -1.236 to +0.4792 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 0 | -100.0% | -3.108 to +0.9077 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.6 (native is 0) | +10.58 to +12.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1307 | 1312 | +0.4% | -43.09 to +52.84 | no |
| utilisation (used / allocatable) | 0.06044 | 0.06038 | -0.1% | -0.001323 to +0.001209 | no |
| CPU used (cores), mean | 1.45 | 1.449 | -0.1% | -0.03176 to +0.02901 | no |
| Omni's own CPU (cores), mean | 0 | 0.01265 | +0.0126 (native is 0) | +0.01195 to +0.01335 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.462 | +0.8% | -0.01935 to +0.04191 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.6 | 448.9 | +0.1% | -8.29 to +8.915 | no |
| HPA replicas, mean | 2.112 | 2.039 | -3.5% | -0.2029 to +0.05626 | no |
| pods started | 0.1 | 0.1 | +0.0% | +0 to +0 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | +0 to +0 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 45.75 | 46.52 | +1.7% | -0.1044 to +1.652 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1510 | 1509 | -0.0% | -5.558 to +4.358 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 178.4 | 186 | +4.3% | -32.86 to +48.11 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 757.1 | 814.4 | +7.6% | -115.9 to +230.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 943.4 | 949.1 | +0.6% | -40.16 to +51.6 | no |
| queue: jobs unfinished at the window's end | 14.2 | 14.4 | +1.4% | -1.671 to +2.071 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.623e-15 to +3.141e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.518 | +0.2% | -0.003474 to +0.01547 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.9 | -0.1% | -1.744 to +1.47 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.9 | -0.1% | -1.744 to +1.47 | no |
| response time (ms), mean | 400.1 | 162.6 | -59.4% | -335.4 to -139.6 | yes: GAIN |
| response time (ms), 95th percentile | 1412 | 293.6 | -79.2% | -1581 to -656.8 | yes: GAIN |
| response time (ms), 99th percentile | 2041 | 408.5 | -80.0% | -2312 to -952.1 | yes: GAIN |
| time over the response line (% of samples) | 22.2 | 0.6996 | -96.8% | -29.31 to -13.7 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 1.1 | -90.6% | -13.6 to -7.599 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 1307 | +11260.0% | +1116 to +1475 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0624 | 0.06044 | -3.2% | -0.007129 to +0.003195 | no |
| CPU used (cores), mean | 1.498 | 1.45 | -3.2% | -0.1711 to +0.07668 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.498 | 1.45 | -3.2% | -0.1711 to +0.07668 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.2 | 448.6 | +1.9% | -28.65 to +45.48 | no |
| HPA replicas, mean | 2.002 | 2.112 | +5.5% | -0.07817 to +0.2981 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.1 | 45.75 | +6.1% | +0.05835 to +5.238 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 782.8 | 1510 | +92.9% | +693.7 to +760.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 178.4 | +251711.8% | +150.6 to +206 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 757.1 | +189175.0% | +666.5 to +846.9 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.04 | 943.4 | +925.0% | +782 to +920.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.2 | +14.2 (native is 0) | +9.339 to +19.06 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.613 | -6.5% | -0.7372 to -0.03697 | yes: GAIN |
| node-hours | 2.512 | 2.353 | -6.3% | -0.3103 to -0.007397 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.6 | +0.2% | -0.5222 to +1.623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 261.5 | -4.2% | -23.11 to -0.08913 | yes: GAIN |
| response time (ms), mean | 400.1 | 360.1 | -10.0% | -50.79 to -29.21 | yes: GAIN |
| response time (ms), 95th percentile | 1412 | 1444 | +2.2% | -24.98 to +88.07 | no |
| response time (ms), 99th percentile | 2041 | 2165 | +6.1% | -38.03 to +286.8 | no |
| time over the response line (% of samples) | 22.2 | 21.69 | -2.3% | -1.695 to +0.6675 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.4 | +6.0% | -0.05776 to +1.458 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.1 | +28.1 (native is 0) | +12.57 to +43.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 11.82 | +2.8% | -1.5 to +2.14 | no |
| utilisation (used / allocatable) | 0.0624 | 0.06737 | +8.0% | +0.001343 to +0.008582 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.498 | 1.512 | +1.0% | +0.0007633 to +0.02818 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01703 | +0.017 (native is 0) | +0.0153 to +0.01876 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.498 | 1.529 | +2.1% | +0.01859 to +0.04441 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.2 | 415.2 | -5.7% | -44.78 to -5.132 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.211 | +10.4% | -0.05444 to +0.4723 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| host CPU busy, the real machine under kind (%) | 43.1 | 44.03 | +2.1% | +0.6741 to +1.172 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 782.8 | 788.1 | +0.7% | +2.19 to +8.41 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.226 | -12.9% | -1.436 to -0.1123 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.04583 | -35.3% | -0.07202 to +0.02202 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.04 | 95.8 | +4.1% | -0.9453 to +8.462 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.613 | -6.5% | -0.7372 to -0.03697 | yes: GAIN |
| node-hours | 2.518 | 2.353 | -6.5% | -0.3101 to -0.01965 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.6 | +0.3% | -1.262 to +2.637 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 261.5 | -4.2% | -23.68 to +0.7512 | no |
| response time (ms), mean | 162.6 | 360.1 | +121.5% | +102.4 to +292.6 | yes: LOSS |
| response time (ms), 95th percentile | 293.6 | 1444 | +391.9% | +671 to +1630 | yes: LOSS |
| response time (ms), 99th percentile | 408.5 | 2165 | +430.0% | +1000 to +2512 | yes: LOSS |
| time over the response line (% of samples) | 0.6996 | 21.69 | +2999.9% | +13.5 to +28.47 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 12.4 | +1027.3% | +8.867 to +13.73 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.1 | +28.1 (native is 0) | +12.57 to +43.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1307 | 11.83 | -99.1% | -1474 to -1116 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06044 | 0.06737 | +11.5% | +0.002787 to +0.01107 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.512 | +4.3% | -0.06808 to +0.1914 | no |
| Omni's own CPU (cores), mean | 0 | 0.01703 | +0.017 (native is 0) | +0.0153 to +0.01876 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.529 | +5.4% | -0.05047 to +0.2079 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.6 | 415.2 | -7.4% | -58.59 to -8.154 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.112 | 2.211 | +4.7% | -0.2342 to +0.4321 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | -0.5294 to +1.129 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | -0.5294 to +1.129 | no |
| host CPU busy, the real machine under kind (%) | 45.75 | 44.03 | -3.8% | -4.252 to +0.8024 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1510 | 788.1 | -47.8% | -754.9 to -688.3 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 178.4 | 0.04583 | -100.0% | -206.1 to -150.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 757.1 | 0.3 | -100.0% | -847.3 to -666.3 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 943.4 | 95.8 | -89.8% | -916.1 to -779.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.2 | 0 | -100.0% | -19.06 to -9.339 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.627e-15 to -2.156e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.517 | +0.2% | -0.001333 to +0.01133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.8 | -0.1% | -2.033 to +1.492 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.8 | -0.1% | -2.033 to +1.492 | no |
| response time (ms), mean | 400.1 | 118 | -70.5% | -385.8 to -178.3 | yes: GAIN |
| response time (ms), 95th percentile | 1412 | 258.6 | -81.7% | -1628 to -680.1 | yes: GAIN |
| response time (ms), 99th percentile | 2041 | 374.8 | -81.6% | -2363 to -968.2 | yes: GAIN |
| time over the response line (% of samples) | 22.2 | 0.3214 | -98.6% | -29.89 to -13.87 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 0 | -100.0% | -14.48 to -8.918 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.6 (native is 0) | +10.58 to +12.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.5 | 1312 | +11302.4% | +1130 to +1471 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0624 | 0.06038 | -3.2% | -0.006617 to +0.002568 | no |
| CPU used (cores), mean | 1.498 | 1.449 | -3.2% | -0.1588 to +0.06164 | no |
| Omni's own CPU (cores), mean | 0 | 0.01265 | +0.0126 (native is 0) | +0.01195 to +0.01335 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.498 | 1.462 | -2.4% | -0.1456 to +0.07374 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.2 | 448.9 | +2.0% | -24.61 to +42.06 | no |
| HPA replicas, mean | 2.002 | 2.039 | +1.8% | -0.07276 to +0.1461 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.1 | 46.52 | +7.9% | +1.082 to +5.762 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 782.8 | 1509 | +92.8% | +691.4 to +761.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 186 | +262482.4% | +144.1 to +227.7 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 814.4 | +203500.0% | +679.5 to +948.5 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.04 | 949.1 | +931.2% | +788.8 to +925.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.4 | +14.4 (native is 0) | +9.75 to +19.05 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*