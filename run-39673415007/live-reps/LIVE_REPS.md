# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.055 | 5.095 |
| node-hours | 2.515 | 2.511 | 2.12 | 2.134 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.3 | 270.9 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.3 | 241.1 | 241.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 247.9 | 259.4 | 215.4 | 225.2 |
| response time (ms), 95th percentile | 755.8 | 800.3 | 785.3 | 825.4 |
| response time (ms), 99th percentile | 1070 | 1125 | 1097 | 1198 |
| time over the response line (% of samples) | 9.502 | 9.989 | 9.493 | 10.36 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 7.1 | 7.2 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 59.3 | 46.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.952 | 8.177 | 8.388 | 7.815 |
| utilisation (used / allocatable) | 0.05534 | 0.05532 | 0.06576 | 0.06524 |
| CPU used (cores), mean | 1.328 | 1.328 | 1.319 | 1.318 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01627 | 0.01653 |
| CPU used with Omni's own (cores), mean | 1.328 | 1.328 | 1.335 | 1.334 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.2 | 496.1 | 438.4 | 441.2 |
| HPA replicas, mean | 1.943 | 2.016 | 2.227 | 2.074 |
| pods started | 0 | 0 | 0.4 | 0.3 |
| pod start wait, total (s) | 0 | 0 | 0.7 | 0.6 |
| pod start wait, mean (s) | 0 | 0 | 0.7 | 0.6 |
| host CPU busy, the real machine under kind (%) | 38.17 | 38.87 | 38.99 | 39.69 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 747.6 | 753.1 | 749.8 | 754.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.277 | 4.362 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1333 | 0.04167 | 0.1792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | 0.2 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 55.24 | 59.35 | 55.56 | 59.83 |
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
| worker nodes in service, mean | 6 | 5.095 | -15.1% | -1.603 to -0.2073 | yes: GAIN |
| node-hours | 2.511 | 2.134 | -15.0% | -0.6678 to -0.08556 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 270.3 | +0.0% | -0.8474 to +0.9728 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 241.9 | -10.5% | -50.41 to -6.291 | yes: GAIN |
| response time (ms), mean | 259.4 | 225.2 | -13.2% | -49.88 to -18.54 | yes: GAIN |
| response time (ms), 95th percentile | 800.3 | 825.4 | +3.1% | -46.5 to +96.73 | no |
| response time (ms), 99th percentile | 1125 | 1198 | +6.6% | -23.22 to +170.8 | no |
| time over the response line (% of samples) | 9.989 | 10.36 | +3.7% | -1.413 to +2.155 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.1 | +0.0% | -1.907 to +1.907 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +26.19 to +67.61 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.177 | 7.815 | -4.4% | -1.191 to +0.4678 | no |
| utilisation (used / allocatable) | 0.05532 | 0.06524 | +17.9% | +0.002778 to +0.01705 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.328 | 1.318 | -0.7% | -0.05304 to +0.03342 | no |
| Omni's own CPU (cores), mean | 0 | 0.01653 | +0.0165 (native is 0) | +0.01485 to +0.01821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.328 | 1.334 | +0.5% | -0.03576 to +0.04921 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.1 | 441.2 | -11.1% | -92.42 to -17.41 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.074 | +2.9% | -0.08992 to +0.205 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 38.87 | 39.69 | +2.1% | +0.5614 to +1.071 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753.1 | 754.9 | +0.2% | -2.129 to +5.729 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.362 | -27.3% | -2.859 to -0.4159 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.1792 | +34.4% | -0.02364 to +0.1153 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.35 | 59.82 | +0.8% | -3.814 to +4.755 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.661e-15 to +5.957e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.511 | -0.2% | -0.01327 to +0.004934 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.3 | -0.2% | -1.66 to +0.8226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.3 | -0.2% | -1.66 to +0.8226 | no |
| response time (ms), mean | 247.9 | 259.4 | +4.6% | -5.743 to +28.76 | no |
| response time (ms), 95th percentile | 755.8 | 800.3 | +5.9% | -57.56 to +146.5 | no |
| response time (ms), 99th percentile | 1070 | 1125 | +5.1% | -52.94 to +161.3 | no |
| time over the response line (% of samples) | 9.502 | 9.989 | +5.1% | -0.8684 to +1.842 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 7.1 | +12.7% | -0.5821 to +2.182 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.952 | 8.177 | +2.8% | -1.848 to +2.298 | no |
| utilisation (used / allocatable) | 0.05534 | 0.05532 | -0.0% | -0.001513 to +0.001465 | no |
| CPU used (cores), mean | 1.328 | 1.328 | -0.0% | -0.03632 to +0.03516 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.328 | 1.328 | -0.0% | -0.03632 to +0.03516 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.2 | 496.1 | +0.4% | -12.69 to +16.4 | no |
| HPA replicas, mean | 1.943 | 2.016 | +3.8% | -0.06475 to +0.2116 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.17 | 38.87 | +1.8% | +0.3253 to +1.082 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 753.1 | +0.7% | -0.5999 to +11.6 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1333 | +255.6% | +0.04133 to +0.1503 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | +0.123 to +0.877 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.24 | 59.35 | +7.4% | -1.983 to +10.21 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.055 | -15.8% | -1.609 to -0.2818 | yes: GAIN |
| node-hours | 2.515 | 2.12 | -15.7% | -0.6731 to -0.1176 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | -0.2124 to +0.7135 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 241.1 | -10.9% | -50.49 to -8.605 | yes: GAIN |
| response time (ms), mean | 247.9 | 215.4 | -13.1% | -44.04 to -20.93 | yes: GAIN |
| response time (ms), 95th percentile | 755.8 | 785.3 | +3.9% | -35.03 to +93.97 | no |
| response time (ms), 99th percentile | 1070 | 1097 | +2.5% | -77.48 to +131.2 | no |
| time over the response line (% of samples) | 9.502 | 9.493 | -0.1% | -1.172 to +1.155 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 7.2 | +14.3% | -0.4676 to +2.268 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.3 | +59.3 (native is 0) | +36.43 to +82.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.952 | 8.388 | +5.5% | -1.202 to +2.075 | no |
| utilisation (used / allocatable) | 0.05534 | 0.06576 | +18.8% | +0.003336 to +0.0175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.328 | 1.319 | -0.7% | -0.03787 to +0.0186 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.0163 (native is 0) | +0.01492 to +0.01762 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.328 | 1.335 | +0.5% | -0.02074 to +0.034 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.2 | 438.4 | -11.3% | -91.35 to -20.35 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 2.227 | +14.7% | +0.0527 to +0.5166 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.05776 to +1.458 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.05776 to +1.458 | no |
| host CPU busy, the real machine under kind (%) | 38.17 | 38.99 | +2.1% | +0.5307 to +1.11 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 749.8 | +0.3% | -1.506 to +5.906 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.277 | -28.7% | -2.9 to -0.5457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04167 | +11.1% | -0.02863 to +0.03697 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | -33.3% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.24 | 55.56 | +0.6% | -2.832 to +3.465 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.055 | -15.8% | -1.609 to -0.2818 | yes: GAIN |
| node-hours | 2.511 | 2.12 | -15.6% | -0.6635 to -0.1189 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 270.9 | +0.2% | -0.7243 to +2.063 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 241.1 | -10.8% | -49.32 to -8.945 | yes: GAIN |
| response time (ms), mean | 259.4 | 215.4 | -17.0% | -60.35 to -27.64 | yes: GAIN |
| response time (ms), 95th percentile | 800.3 | 785.3 | -1.9% | -74.95 to +44.93 | no |
| response time (ms), 99th percentile | 1125 | 1097 | -2.4% | -93.94 to +39.32 | no |
| time over the response line (% of samples) | 9.989 | 9.493 | -5.0% | -1.323 to +0.3319 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.2 | +1.4% | -0.8204 to +1.02 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.3 | +59.3 (native is 0) | +36.43 to +82.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.177 | 8.388 | +2.6% | -0.7794 to +1.203 | no |
| utilisation (used / allocatable) | 0.05532 | 0.06576 | +18.9% | +0.002677 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.328 | 1.319 | -0.7% | -0.03401 to +0.01589 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.0163 (native is 0) | +0.01492 to +0.01762 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.328 | 1.335 | +0.5% | -0.01707 to +0.0315 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.1 | 438.4 | -11.6% | -100 to -15.37 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.227 | +10.5% | +0.03354 to +0.3889 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.05776 to +1.458 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.05776 to +1.458 | no |
| host CPU busy, the real machine under kind (%) | 38.87 | 38.99 | +0.3% | -0.01831 to +0.2516 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753.1 | 749.8 | -0.4% | -5.956 to -0.6438 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.277 | -28.7% | -2.9 to -0.5457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.04167 | -68.8% | -0.1509 to -0.03239 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.2 | -75.0% | -0.9694 to -0.2306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 59.35 | 55.56 | -6.4% | -7.627 to +0.03547 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.095 | -15.1% | -1.603 to -0.2073 | yes: GAIN |
| node-hours | 2.515 | 2.134 | -15.1% | -0.6769 to -0.08481 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.3 | -0.1% | -1.629 to +0.9167 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 241.9 | -10.6% | -51.43 to -6.107 | yes: GAIN |
| response time (ms), mean | 247.9 | 225.2 | -9.2% | -38.13 to -7.268 | yes: GAIN |
| response time (ms), 95th percentile | 755.8 | 825.4 | +9.2% | -15.28 to +154.5 | no |
| response time (ms), 99th percentile | 1070 | 1198 | +12.0% | -5.63 to +261.5 | no |
| time over the response line (% of samples) | 9.502 | 10.36 | +9.0% | +0.0996 to +1.616 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 7.1 | +12.7% | -0.3583 to +1.958 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +26.19 to +67.61 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.952 | 7.815 | -1.7% | -2.227 to +1.953 | no |
| utilisation (used / allocatable) | 0.05534 | 0.06524 | +17.9% | +0.002915 to +0.01687 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.328 | 1.318 | -0.8% | -0.05982 to +0.03905 | no |
| Omni's own CPU (cores), mean | 0 | 0.01653 | +0.0165 (native is 0) | +0.01485 to +0.01821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.328 | 1.334 | +0.5% | -0.04249 to +0.05477 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.2 | 441.2 | -10.7% | -88.52 to -17.61 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 2.074 | +6.7% | -0.08326 to +0.3452 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 38.17 | 39.69 | +4.0% | +1.255 to +1.785 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 754.9 | +1.0% | +1.1 to +13.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.362 | -27.3% | -2.859 to -0.4159 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1792 | +377.8% | +0.0801 to +0.2032 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.9 | +200.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.24 | 59.83 | +8.3% | -1.016 to +10.18 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*