# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.011 | 4.696 |
| node-hours | 2.519 | 2.519 | 2.104 | 1.971 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.3 | 271.4 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.3 | 240.3 | 230.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 268.3 | 253.3 | 238.5 | 207.2 |
| response time (ms), 95th percentile | 866.2 | 908.4 | 923.9 | 874.5 |
| response time (ms), 99th percentile | 1230 | 1412 | 1274 | 1327 |
| time over the response line (% of samples) | 12.32 | 8.854 | 12.15 | 8.435 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6 | 7.7 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 55.5 | 46.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 83.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.417 | 10.35 | 9.752 | 11.25 |
| utilisation (used / allocatable) | 0.0552 | 0.05548 | 0.06727 | 0.07145 |
| CPU used (cores), mean | 1.325 | 1.331 | 1.338 | 1.318 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01616 | 0.01651 |
| CPU used with Omni's own (cores), mean | 1.325 | 1.331 | 1.354 | 1.335 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.8 | 498.6 | 433.5 | 419.4 |
| HPA replicas, mean | 1.952 | 1.956 | 2.036 | 2.09 |
| pods started | 0 | 0.3 | 0.3 | 0.3 |
| pod start wait, total (s) | 0 | 0.5 | 0.7 | 1 |
| pod start wait, mean (s) | 0 | 0.4 | 0.4 | 0.65 |
| host CPU busy, the real machine under kind (%) | 37.86 | 37.9 | 38.94 | 38.71 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 757.5 | 756.2 | 761.1 | 757.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.297 | 3.837 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.06667 | 0.0375 | 0.07917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | 0.2 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 63.56 | 63.75 | 65.83 | 65.27 |
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
| worker nodes in service, mean | 6 | 4.696 | -21.7% | -2.117 to -0.4913 | yes: GAIN |
| node-hours | 2.519 | 1.971 | -21.7% | -0.8895 to -0.206 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.3 | -0.0% | -0.8047 to +0.7498 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 230.3 | -15.1% | -66.69 to -15.38 | yes: GAIN |
| response time (ms), mean | 253.3 | 207.2 | -18.2% | -58.56 to -33.77 | yes: GAIN |
| response time (ms), 95th percentile | 908.4 | 874.5 | -3.7% | -87.33 to +19.61 | no |
| response time (ms), 99th percentile | 1412 | 1327 | -6.0% | -175.9 to +7.031 | no |
| time over the response line (% of samples) | 8.854 | 8.435 | -4.7% | -1.45 to +0.611 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 5.8 | -3.3% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 | +46.3 (native is 0) | +35.52 to +57.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 11.25 | +8.7% | -1.016 to +2.819 | no |
| utilisation (used / allocatable) | 0.05548 | 0.07145 | +28.8% | +0.005572 to +0.02638 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.331 | 1.318 | -1.0% | -0.03393 to +0.00788 | no |
| Omni's own CPU (cores), mean | 0 | 0.01651 | +0.0165 (native is 0) | +0.01459 to +0.01843 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.331 | 1.335 | +0.3% | -0.01876 to +0.02573 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.6 | 419.4 | -15.9% | -130.9 to -27.48 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.956 | 2.09 | +6.9% | -0.06375 to +0.3319 | no |
| pods started | 0.3 | 0.3 | +0.0% | -0.754 to +0.754 | no |
| pod start wait, total (s) | 0.5 | 1 | +100.0% | -1.473 to +2.473 | no |
| pod start wait, mean (s) | 0.4 | 0.65 | +62.5% | -1.069 to +1.569 | no |
| host CPU busy, the real machine under kind (%) | 37.9 | 38.71 | +2.1% | +0.5329 to +1.092 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 757.9 | +0.2% | -1.948 to +5.348 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.837 | -36.1% | -3.408 to -0.9181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.07917 | +18.7% | -0.0342 to +0.0592 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.75 | 65.27 | +2.4% | -0.7541 to +3.796 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.539e-15 to +1.006e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.519 | -0.0% | -0.006711 to +0.006045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.3 | +0.1% | -0.8802 to +1.481 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.3 | +0.1% | -0.8802 to +1.481 | no |
| response time (ms), mean | 268.3 | 253.3 | -5.6% | -26.85 to -3.003 | yes: GAIN |
| response time (ms), 95th percentile | 866.2 | 908.4 | +4.9% | -72.63 to +156.9 | no |
| response time (ms), 99th percentile | 1230 | 1412 | +14.7% | -39.91 to +402.7 | no |
| time over the response line (% of samples) | 12.32 | 8.854 | -28.1% | -6.273 to -0.6519 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6 | -13.0% | -1.99 to +0.19 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.417 | 10.35 | +22.9% | +0.5024 to +3.358 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0552 | 0.05548 | +0.5% | -0.001899 to +0.002451 | no |
| CPU used (cores), mean | 1.325 | 1.331 | +0.5% | -0.04557 to +0.05882 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.325 | 1.331 | +0.5% | -0.04557 to +0.05882 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.8 | 498.6 | -2.2% | -47.38 to +24.94 | no |
| HPA replicas, mean | 1.952 | 1.956 | +0.2% | -0.07211 to +0.08047 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.2726 to +1.273 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 37.86 | 37.9 | +0.1% | -0.244 to +0.3169 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.5 | 756.2 | -0.2% | -3.802 to +1.202 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.06667 | +33.3% | -0.02821 to +0.06154 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.56 | 63.75 | +0.3% | -1.975 to +2.359 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.011 | -16.5% | -1.751 to -0.2263 | yes: GAIN |
| node-hours | 2.519 | 2.104 | -16.5% | -0.738 to -0.09175 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.4 | +0.1% | -0.4271 to +1.094 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 240.3 | -11.3% | -54.87 to -6.615 | yes: GAIN |
| response time (ms), mean | 268.3 | 238.5 | -11.1% | -45.63 to -13.92 | yes: GAIN |
| response time (ms), 95th percentile | 866.2 | 923.9 | +6.7% | -14.73 to +130.1 | no |
| response time (ms), 99th percentile | 1230 | 1274 | +3.5% | -31.97 to +118.5 | no |
| time over the response line (% of samples) | 12.32 | 12.15 | -1.4% | -1.122 to +0.7796 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.7 | +11.6% | -0.1417 to +1.742 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.5 | +55.5 (native is 0) | +41.92 to +69.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.417 | 9.752 | +15.9% | -0.1882 to +2.858 | no |
| utilisation (used / allocatable) | 0.0552 | 0.06727 | +21.9% | +0.002732 to +0.0214 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.325 | 1.338 | +1.0% | -0.01245 to +0.03787 | no |
| Omni's own CPU (cores), mean | 0 | 0.01616 | +0.0162 (native is 0) | +0.01481 to +0.01751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.325 | 1.354 | +2.2% | +0.003332 to +0.0544 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.8 | 433.5 | -15.0% | -144.6 to -7.975 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.036 | +4.3% | -0.03923 to +0.2083 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.6509 to +2.051 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 37.86 | 38.94 | +2.8% | +0.6395 to +1.519 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.5 | 761.1 | +0.5% | -1.984 to +9.184 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.297 | -28.4% | -2.94 to -0.4667 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 | -25.0% | -0.05704 to +0.03204 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | -33.3% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.56 | 65.83 | +3.6% | -2.027 to +6.577 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.011 | -16.5% | -1.751 to -0.2263 | yes: GAIN |
| node-hours | 2.519 | 2.104 | -16.5% | -0.7357 to -0.09337 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.4 | +0.0% | -1.095 to +1.161 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 240.3 | -11.4% | -55.5 to -6.586 | yes: GAIN |
| response time (ms), mean | 253.3 | 238.5 | -5.9% | -26 to -3.686 | yes: GAIN |
| response time (ms), 95th percentile | 908.4 | 923.9 | +1.7% | -86.43 to +117.5 | no |
| response time (ms), 99th percentile | 1412 | 1274 | -9.8% | -368.1 to +91.85 | no |
| time over the response line (% of samples) | 8.854 | 12.15 | +37.2% | +1.1 to +5.483 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 7.7 | +28.3% | -0.179 to +3.579 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.5 | +55.5 (native is 0) | +41.92 to +69.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 9.752 | -5.8% | -2.241 to +1.051 | no |
| utilisation (used / allocatable) | 0.05548 | 0.06727 | +21.3% | +0.003477 to +0.02011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.331 | 1.338 | +0.5% | -0.02913 to +0.0413 | no |
| Omni's own CPU (cores), mean | 0 | 0.01616 | +0.0162 (native is 0) | +0.01481 to +0.01751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.331 | 1.354 | +1.7% | -0.01367 to +0.05816 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.6 | 433.5 | -13.1% | -110.3 to -19.85 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.956 | 2.036 | +4.1% | -0.05168 to +0.2123 | no |
| pods started | 0.3 | 0.3 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | -1.006 to +1.406 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | +0.0% | -0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 37.9 | 38.94 | +2.8% | +0.6338 to +1.451 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 761.1 | +0.6% | -1.136 to +10.94 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.297 | -28.4% | -2.94 to -0.4667 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0375 | -43.8% | -0.07794 to +0.01961 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | -50.0% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.75 | 65.83 | +3.3% | -1.779 to +5.946 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.696 | -21.7% | -2.117 to -0.4913 | yes: GAIN |
| node-hours | 2.519 | 1.971 | -21.8% | -0.8902 to -0.2059 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.3 | +0.1% | -0.6389 to +1.185 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 230.3 | -15.0% | -66.04 to -15.42 | yes: GAIN |
| response time (ms), mean | 268.3 | 207.2 | -22.8% | -83.53 to -38.66 | yes: GAIN |
| response time (ms), 95th percentile | 866.2 | 874.5 | +1.0% | -88.01 to +104.6 | no |
| response time (ms), 99th percentile | 1230 | 1327 | +7.9% | -40.42 to +234.4 | no |
| time over the response line (% of samples) | 12.32 | 8.435 | -31.5% | -7.208 to -0.5563 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.8 | -15.9% | -2.241 to +0.04101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 | +46.3 (native is 0) | +35.52 to +57.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.417 | 11.25 | +33.6% | +1.164 to +4.499 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0552 | 0.07145 | +29.4% | +0.005008 to +0.02749 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.325 | 1.318 | -0.5% | -0.05367 to +0.04086 | no |
| Omni's own CPU (cores), mean | 0 | 0.01651 | +0.0165 (native is 0) | +0.01459 to +0.01843 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.325 | 1.335 | +0.8% | -0.03674 to +0.05696 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.8 | 419.4 | -17.7% | -165.8 to -15.06 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.09 | +7.1% | -0.07663 to +0.3532 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | -0.6519 to +2.652 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.65 (native is 0) | -0.3338 to +1.634 | no |
| host CPU busy, the real machine under kind (%) | 37.86 | 38.71 | +2.2% | +0.4018 to +1.296 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.5 | 757.9 | +0.1% | -3.343 to +4.143 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.837 | -36.1% | -3.408 to -0.9181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.07917 | +58.3% | -0.01754 to +0.07587 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.56 | 65.27 | +2.7% | -0.291 to +3.716 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*