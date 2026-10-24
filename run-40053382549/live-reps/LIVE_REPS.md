# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.188 | 4.629 |
| node-hours | 2.518 | 2.515 | 2.178 | 1.938 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.1 | 271.2 | 270.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.1 | 245.7 | 227.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 257 | 203.4 | 226.9 | 167.9 |
| response time (ms), 95th percentile | 778.4 | 477.5 | 821.2 | 508.3 |
| response time (ms), 99th percentile | 1117 | 790.8 | 1157 | 864.9 |
| time over the response line (% of samples) | 11.73 | 5.949 | 11.99 | 5.712 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.1 | 7.8 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.3 | 54.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.635 | 13.59 | 9.222 | 14.12 |
| utilisation (used / allocatable) | 0.05577 | 0.05677 | 0.06467 | 0.07281 |
| CPU used (cores), mean | 1.338 | 1.363 | 1.337 | 1.323 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01654 | 0.01851 |
| CPU used with Omni's own (cores), mean | 1.338 | 1.363 | 1.353 | 1.341 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494 | 485.1 | 440.4 | 411.8 |
| HPA replicas, mean | 2.026 | 2.004 | 2.39 | 2.293 |
| pods started | 0 | 0 | 0.7 | 0.1 |
| pod start wait, total (s) | 0 | 0 | 1.5 | 0.2 |
| pod start wait, mean (s) | 0 | 0 | 1.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.37 | 39.57 | 39.33 | 40.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 747 | 758.1 | 749.3 | 760.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.57 | 3.683 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.725 | 0.02917 | 0.6417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.4 | 0.1 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 54.72 | 69.86 | 56.58 | 69.82 |
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
| worker nodes in service, mean | 6 | 4.629 | -22.8% | -2.162 to -0.5796 | yes: GAIN |
| node-hours | 2.515 | 1.938 | -22.9% | -0.9113 to -0.2418 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 270.5 | -0.2% | -1.611 to +0.3338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 227.4 | -16.1% | -68.89 to -18.47 | yes: GAIN |
| response time (ms), mean | 203.4 | 167.9 | -17.5% | -53.38 to -17.65 | yes: GAIN |
| response time (ms), 95th percentile | 477.5 | 508.3 | +6.5% | -85.98 to +147.7 | no |
| response time (ms), 99th percentile | 790.8 | 864.9 | +9.4% | -109.7 to +258 | no |
| time over the response line (% of samples) | 5.949 | 5.712 | -4.0% | -2.136 to +1.662 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 6.4 | +4.9% | -0.5294 to +1.129 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.4 | +54.4 (native is 0) | +32.36 to +76.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 14.12 | +3.9% | -1.254 to +2.307 | no |
| utilisation (used / allocatable) | 0.05677 | 0.07281 | +28.2% | +0.005838 to +0.02623 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.363 | 1.323 | -2.9% | -0.06928 to -0.01031 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01851 | +0.0185 (native is 0) | +0.01612 to +0.0209 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.341 | -1.6% | -0.05037 to +0.007802 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.1 | 411.8 | -15.1% | -122.3 to -24.23 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.293 | +14.4% | +0.07239 to +0.5053 | yes: power given |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.57 | 40.5 | +2.4% | +0.6241 to +1.253 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.1 | 760.1 | +0.3% | -3.772 to +7.772 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.683 | -38.6% | -3.543 to -1.092 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.6417 | -11.5% | -0.1711 to +0.004409 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.3 | -7.1% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 69.86 | 69.82 | -0.1% | -5.266 to +5.191 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.466e-15 to +9.334e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.515 | -0.1% | -0.008427 to +0.00276 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.1 | +0.0% | -0.4667 to +0.4915 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.1 | +0.0% | -0.4667 to +0.4915 | no |
| response time (ms), mean | 257 | 203.4 | -20.9% | -90.72 to -16.51 | yes: GAIN |
| response time (ms), 95th percentile | 778.4 | 477.5 | -38.7% | -508.8 to -93.1 | yes: GAIN |
| response time (ms), 99th percentile | 1117 | 790.8 | -29.2% | -531.3 to -121.1 | yes: GAIN |
| time over the response line (% of samples) | 11.73 | 5.949 | -49.3% | -10.42 to -1.143 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.1 | -14.1% | -1.954 to -0.04626 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.635 | 13.59 | +41.1% | +2.359 to +5.554 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05577 | 0.05677 | +1.8% | +0.000347 to +0.001663 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.338 | 1.363 | +1.8% | +0.008328 to +0.0399 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.338 | 1.363 | +1.8% | +0.008328 to +0.0399 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494 | 485.1 | -1.8% | -15.77 to -2.032 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.004 | -1.1% | -0.1454 to +0.1015 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.37 | 39.57 | +3.1% | +0.8569 to +1.542 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747 | 758.1 | +1.5% | +3.527 to +18.67 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.725 | +1142.9% | +0.5978 to +0.7355 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.4 | +600.0% | +0.8984 to +1.502 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 54.72 | 69.86 | +27.7% | +4.821 to +25.45 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.188 | -13.5% | -1.481 to -0.1434 | yes: GAIN |
| node-hours | 2.518 | 2.178 | -13.5% | -0.6249 to -0.05401 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.0% | -1.015 to +1.213 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 245.7 | -9.4% | -47.18 to -3.694 | yes: GAIN |
| response time (ms), mean | 257 | 226.9 | -11.7% | -45.49 to -14.65 | yes: GAIN |
| response time (ms), 95th percentile | 778.4 | 821.2 | +5.5% | -30.72 to +116.4 | no |
| response time (ms), 99th percentile | 1117 | 1157 | +3.6% | -83.49 to +163.3 | no |
| time over the response line (% of samples) | 11.73 | 11.99 | +2.2% | -0.8583 to +1.376 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.8 | +9.9% | -0.1953 to +1.595 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 | +46.3 (native is 0) | +30.11 to +62.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.635 | 9.222 | -4.3% | -2.395 to +1.569 | no |
| utilisation (used / allocatable) | 0.05577 | 0.06467 | +16.0% | +0.001926 to +0.01587 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.338 | 1.337 | -0.1% | -0.02274 to +0.01947 | no |
| Omni's own CPU (cores), mean | 0 | 0.01654 | +0.0165 (native is 0) | +0.01518 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.338 | 1.353 | +1.1% | -0.006281 to +0.03609 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494 | 440.4 | -10.8% | -99.07 to -8.117 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.39 | +18.0% | +0.1068 to +0.6214 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.1111 to +1.289 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | +0.02055 to +2.979 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.1 (native is 0) | +0.06342 to +2.137 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.37 | 39.33 | +2.5% | +0.7398 to +1.18 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747 | 749.3 | +0.3% | -1.899 to +6.499 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.57 | -23.8% | -2.564 to -0.2963 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.02917 | -50.0% | -0.07992 to +0.02159 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | -50.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 54.72 | 56.58 | +3.4% | -2.102 to +5.81 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.188 | -13.5% | -1.481 to -0.1434 | yes: GAIN |
| node-hours | 2.515 | 2.178 | -13.4% | -0.623 to -0.05023 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.0% | -0.8149 to +0.9886 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 245.7 | -9.4% | -47.16 to -3.74 | yes: GAIN |
| response time (ms), mean | 203.4 | 226.9 | +11.6% | -13.3 to +60.39 | no |
| response time (ms), 95th percentile | 477.5 | 821.2 | +72.0% | +128.5 to +559 | yes: LOSS |
| response time (ms), 99th percentile | 790.8 | 1157 | +46.3% | +148 to +584.1 | yes: LOSS |
| time over the response line (% of samples) | 5.949 | 11.99 | +101.5% | +1.438 to +10.64 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 7.8 | +27.9% | +0.2674 to +3.133 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 | +46.3 (native is 0) | +30.11 to +62.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.59 | 9.222 | -32.2% | -5.522 to -3.218 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05677 | 0.06467 | +13.9% | +0.0008604 to +0.01493 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.363 | 1.337 | -1.9% | -0.03895 to -0.01255 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01654 | +0.0165 (native is 0) | +0.01518 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.353 | -0.7% | -0.02293 to +0.004504 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.1 | 440.4 | -9.2% | -86.92 to -2.465 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.39 | +19.3% | +0.1427 to +0.6294 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.1111 to +1.289 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | +0.02055 to +2.979 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.1 (native is 0) | +0.06342 to +2.137 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.57 | 39.33 | -0.6% | -0.5306 to +0.05139 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.1 | 749.3 | -1.2% | -15.37 to -2.229 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.57 | -23.8% | -2.564 to -0.2963 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.02917 | -96.0% | -0.779 to -0.6127 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.1 | -92.9% | -1.646 to -0.9545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 69.86 | 56.58 | -19.0% | -23.48 to -3.085 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.629 | -22.8% | -2.162 to -0.5796 | yes: GAIN |
| node-hours | 2.518 | 1.938 | -23.0% | -0.9142 to -0.2446 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 270.5 | -0.2% | -1.647 to +0.3946 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 227.4 | -16.1% | -69.04 to -18.29 | yes: GAIN |
| response time (ms), mean | 257 | 167.9 | -34.7% | -130.1 to -48.15 | yes: GAIN |
| response time (ms), 95th percentile | 778.4 | 508.3 | -34.7% | -469.3 to -70.89 | yes: GAIN |
| response time (ms), 99th percentile | 1117 | 864.9 | -22.6% | -522.1 to +18.05 | no |
| time over the response line (% of samples) | 11.73 | 5.712 | -51.3% | -11.59 to -0.4414 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.4 | -9.9% | -1.529 to +0.1294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.4 | +54.4 (native is 0) | +32.36 to +76.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.635 | 14.12 | +46.5% | +2.116 to +6.85 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05577 | 0.07281 | +30.5% | +0.006988 to +0.02709 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.338 | 1.323 | -1.2% | -0.0457 to +0.01434 | no |
| Omni's own CPU (cores), mean | 0 | 0.01851 | +0.0185 (native is 0) | +0.01612 to +0.0209 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.338 | 1.341 | +0.2% | -0.02682 to +0.03248 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494 | 411.8 | -16.6% | -133.6 to -30.78 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.293 | +13.2% | +0.04871 to +0.4851 | yes: power given |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 38.37 | 40.5 | +5.6% | +1.848 to +2.428 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747 | 760.1 | +1.8% | +5.153 to +21.05 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.683 | -38.6% | -3.543 to -1.092 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6417 | +1000.0% | +0.509 to +0.6577 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.3 | +550.0% | +0.8738 to +1.326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 54.72 | 69.82 | +27.6% | +3.748 to +26.45 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*