# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.474 | 5.977 |
| node-hours | 2.515 | 2.516 | 2.294 | 2.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.9 | 271.6 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.9 | 255.1 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 294.7 | 143 | 262.8 | 106.7 |
| response time (ms), 95th percentile | 942.9 | 247.7 | 966.5 | 230.5 |
| response time (ms), 99th percentile | 1343 | 347.7 | 1400 | 347 |
| time over the response line (% of samples) | 16.83 | 0.1544 | 17.65 | 0.1714 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 0 | 10.7 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 37.9 | 13.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.602 | 1138 | 10.02 | 1172 |
| utilisation (used / allocatable) | 0.05852 | 0.05932 | 0.06364 | 0.05976 |
| CPU used (cores), mean | 1.405 | 1.424 | 1.381 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01591 | 0.0126 |
| CPU used with Omni's own (cores), mean | 1.405 | 1.424 | 1.397 | 1.442 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 456.3 | 441.8 | 454.2 |
| HPA replicas, mean | 1.951 | 2.017 | 2.509 | 2.025 |
| pods started | 0 | 0 | 0.5 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 1.4 | 0.3 |
| pod start wait, mean (s) | 0 | 0 | 1.15 | 0.3 |
| host CPU busy, the real machine under kind (%) | 39.89 | 43.93 | 40.64 | 44.84 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 749.3 | 1440 | 751.4 | 1449 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.11 | 5.543 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 157.9 | 0.06667 | 148.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 723.1 | 0.5 | 678 |
| queue: job turnaround, submitted to done, mean (s) | 58.93 | 841.2 | 59.91 | 872.9 |
| queue: jobs unfinished at the window's end | 0 | 12 | 0 | 12.6 |

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
| worker nodes in service, mean | 6 | 5.977 | -0.4% | -0.07413 to +0.02868 | no |
| node-hours | 2.516 | 2.507 | -0.4% | -0.03161 to +0.01361 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.2 | +0.1% | -0.8817 to +1.47 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.5 | -0.2% | -2.619 to +1.782 | no |
| response time (ms), mean | 143 | 106.7 | -25.4% | -43.54 to -29.16 | yes: GAIN |
| response time (ms), 95th percentile | 247.7 | 230.5 | -6.9% | -28.52 to -5.845 | yes: GAIN |
| response time (ms), 99th percentile | 347.7 | 347 | -0.2% | -19.05 to +17.67 | no |
| time over the response line (% of samples) | 0.1544 | 0.1714 | +11.0% | -0.1036 to +0.1376 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.4 | +13.4 (native is 0) | +10.76 to +16.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1138 | 1172 | +3.0% | -36.92 to +104.5 | no |
| utilisation (used / allocatable) | 0.05932 | 0.05976 | +0.7% | -0.0005676 to +0.001438 | no |
| CPU used (cores), mean | 1.424 | 1.429 | +0.4% | -0.02387 to +0.035 | no |
| Omni's own CPU (cores), mean | 0 | 0.0126 | +0.0126 (native is 0) | +0.01172 to +0.01348 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.442 | +1.3% | -0.0113 to +0.04764 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.3 | 454.2 | -0.5% | -9.271 to +4.968 | no |
| HPA replicas, mean | 2.017 | 2.025 | +0.4% | -0.1319 to +0.1476 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.84 | +2.1% | -0.07739 to +1.894 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1440 | 1449 | +0.6% | -11.31 to +28.51 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.543 | -7.6% | -6.257 to +5.344 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 157.9 | 148.8 | -5.8% | -51.67 to +33.41 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 723.1 | 678 | -6.2% | -253.8 to +163.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 841.2 | 872.9 | +3.8% | -24.2 to +87.63 | no |
| queue: jobs unfinished at the window's end | 12 | 12.6 | +5.0% | -1.159 to +2.359 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.695e-15 to +2.737e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.516 | +0.0% | -0.007756 to +0.01009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.9 | +0.0% | -1.447 to +1.665 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.9 | +0.0% | -1.447 to +1.665 | no |
| response time (ms), mean | 294.7 | 143 | -51.5% | -210.5 to -92.95 | yes: GAIN |
| response time (ms), 95th percentile | 942.9 | 247.7 | -73.7% | -965.1 to -425.3 | yes: GAIN |
| response time (ms), 99th percentile | 1343 | 347.7 | -74.1% | -1383 to -607.7 | yes: GAIN |
| time over the response line (% of samples) | 16.83 | 0.1544 | -99.1% | -23.93 to -9.419 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 0 | -100.0% | -14.04 to -7.158 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.602 | 1138 | +11751.8% | +887.5 to +1369 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05852 | 0.05932 | +1.4% | -0.002922 to +0.004516 | no |
| CPU used (cores), mean | 1.405 | 1.424 | +1.4% | -0.07014 to +0.1084 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.405 | 1.424 | +1.4% | -0.07014 to +0.1084 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 456.3 | -2.6% | -46.13 to +21.75 | no |
| HPA replicas, mean | 1.951 | 2.017 | +3.4% | -0.06503 to +0.1985 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 39.89 | 43.93 | +10.1% | +2.22 to +5.851 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 749.3 | 1440 | +92.2% | +595 to +786.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 157.9 | +252553.3% | +116.4 to +199.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 723.1 | +180675.0% | +506.5 to +938.9 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.93 | 841.2 | +1327.5% | +638.5 to +926 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12 | +12 (native is 0) | +7.255 to +16.74 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.474 | -8.8% | -1.221 to +0.1681 | no |
| node-hours | 2.515 | 2.294 | -8.8% | -0.51 to +0.06976 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.6 | -0.1% | -0.9565 to +0.5865 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 255.1 | -6.2% | -38.67 to +5.225 | no |
| response time (ms), mean | 294.7 | 262.8 | -10.8% | -43.7 to -20.24 | yes: GAIN |
| response time (ms), 95th percentile | 942.9 | 966.5 | +2.5% | -17.9 to +65.15 | no |
| response time (ms), 99th percentile | 1343 | 1400 | +4.2% | -5.521 to +118.7 | no |
| time over the response line (% of samples) | 16.83 | 17.65 | +4.9% | -0.08898 to +1.741 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.7 | +0.9% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.9 (native is 0) | +21.62 to +54.18 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.602 | 10.02 | +4.4% | -1.153 to +1.989 | no |
| utilisation (used / allocatable) | 0.05852 | 0.06364 | +8.7% | -0.002173 to +0.0124 | no |
| CPU used (cores), mean | 1.405 | 1.381 | -1.7% | -0.04827 to +0.000668 | no |
| Omni's own CPU (cores), mean | 0 | 0.01591 | +0.0159 (native is 0) | +0.01449 to +0.01733 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.405 | 1.397 | -0.6% | -0.03289 to +0.0171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 441.8 | -5.7% | -66.68 to +13.2 | no |
| HPA replicas, mean | 1.951 | 2.509 | +28.6% | +0.294 to +0.8232 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.4 (native is 0) | +0.001538 to +2.798 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.15 | +1.15 (native is 0) | +0.031 to +2.269 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.89 | 40.64 | +1.9% | +0.5886 to +0.9122 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 749.3 | 751.4 | +0.3% | +0.1791 to +4.021 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.11 | -14.8% | -2.034 to +0.2544 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.06667 | +6.7% | -0.03418 to +0.04252 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.93 | 59.91 | +1.7% | -0.9795 to +2.946 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.474 | -8.8% | -1.221 to +0.1681 | no |
| node-hours | 2.516 | 2.294 | -8.8% | -0.5131 to +0.07049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | -0.1% | -1.972 to +1.384 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 255.1 | -6.2% | -40.06 to +6.401 | no |
| response time (ms), mean | 143 | 262.8 | +83.8% | +70.15 to +169.4 | yes: LOSS |
| response time (ms), 95th percentile | 247.7 | 966.5 | +290.2% | +466.7 to +971 | yes: LOSS |
| response time (ms), 99th percentile | 347.7 | 1400 | +302.6% | +670.4 to +1434 | yes: LOSS |
| time over the response line (% of samples) | 0.1544 | 17.65 | +11329.7% | +10.4 to +24.6 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.7 | +10.7 (native is 0) | +7.211 to +14.19 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.9 (native is 0) | +21.62 to +54.18 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1138 | 10.02 | -99.1% | -1369 to -887.3 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05932 | 0.06364 | +7.3% | -0.0002776 to +0.008907 | no |
| CPU used (cores), mean | 1.424 | 1.381 | -3.0% | -0.1509 to +0.06506 | no |
| Omni's own CPU (cores), mean | 0 | 0.01591 | +0.0159 (native is 0) | +0.01449 to +0.01733 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.397 | -1.9% | -0.1353 to +0.08123 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.3 | 441.8 | -3.2% | -30.67 to +1.566 | no |
| HPA replicas, mean | 2.017 | 2.509 | +24.4% | +0.2498 to +0.7338 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.4 (native is 0) | +0.001538 to +2.798 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.15 | +1.15 (native is 0) | +0.031 to +2.269 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.93 | 40.64 | -7.5% | -5.083 to -1.487 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1440 | 751.4 | -47.8% | -783.7 to -593.7 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.115 | -64.8% | -5.341 to -2.43 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 157.9 | 0.06667 | -100.0% | -199.3 to -116.4 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 723.1 | 0.5 | -99.9% | -939 to -506.2 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 841.2 | 59.91 | -92.9% | -925 to -637.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12 | 0 | -100.0% | -16.74 to -7.255 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.977 | -0.4% | -0.07413 to +0.02868 | no |
| node-hours | 2.515 | 2.507 | -0.3% | -0.02964 to +0.01397 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.2 | +0.1% | -0.7627 to +1.569 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.5 | -0.1% | -1.745 to +1.127 | no |
| response time (ms), mean | 294.7 | 106.7 | -63.8% | -253.5 to -122.6 | yes: GAIN |
| response time (ms), 95th percentile | 942.9 | 230.5 | -75.6% | -987.3 to -437.5 | yes: GAIN |
| response time (ms), 99th percentile | 1343 | 347 | -74.2% | -1387 to -605.2 | yes: GAIN |
| time over the response line (% of samples) | 16.83 | 0.1714 | -99.0% | -23.89 to -9.418 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 0.1 | -99.1% | -13.91 to -7.09 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.4 | +13.4 (native is 0) | +10.76 to +16.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.602 | 1172 | +12103.4% | +914.5 to +1410 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05852 | 0.05976 | +2.1% | -0.002043 to +0.004506 | no |
| CPU used (cores), mean | 1.405 | 1.429 | +1.8% | -0.04693 to +0.09631 | no |
| Omni's own CPU (cores), mean | 0 | 0.0126 | +0.0126 (native is 0) | +0.01172 to +0.01348 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.405 | 1.442 | +2.7% | -0.03396 to +0.1085 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 454.2 | -3.1% | -44.22 to +15.54 | no |
| HPA replicas, mean | 1.951 | 2.025 | +3.8% | -0.1143 to +0.2635 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 39.89 | 44.84 | +12.4% | +3.297 to +6.591 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 749.3 | 1449 | +93.3% | +613.1 to +785.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.543 | -7.6% | -6.257 to +5.344 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 148.8 | +237946.7% | +106.5 to +191 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 678 | +169400.0% | +518.7 to +836.5 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.93 | 872.9 | +1381.3% | +656.7 to +971.3 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.6 | +12.6 (native is 0) | +7.619 to +17.58 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*