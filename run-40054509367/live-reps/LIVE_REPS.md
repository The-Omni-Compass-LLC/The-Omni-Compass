# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.766 | 4.843 |
| node-hours | 2.515 | 2.514 | 2 | 2.03 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.4 | 270.9 | 270.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.4 | 232.1 | 234.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 247.6 | 273.3 | 226 | 246.7 |
| response time (ms), 95th percentile | 753.5 | 879.1 | 837 | 928.2 |
| response time (ms), 99th percentile | 1085 | 1294 | 1168 | 1335 |
| time over the response line (% of samples) | 13.3 | 14.17 | 13.42 | 14.21 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | 7 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43.7 | 58.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.567 | 8.993 | 10.08 | 9.257 |
| utilisation (used / allocatable) | 0.05524 | 0.05501 | 0.06918 | 0.06857 |
| CPU used (cores), mean | 1.326 | 1.32 | 1.301 | 1.302 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0147 | 0.01642 |
| CPU used with Omni's own (cores), mean | 1.326 | 1.32 | 1.316 | 1.319 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.5 | 504.9 | 427.6 | 430.7 |
| HPA replicas, mean | 1.946 | 2.019 | 2.228 | 2.253 |
| pods started | 0.1 | 0.1 | 0.2 | 0.4 |
| pod start wait, total (s) | 0.3 | 0.1 | 0.5 | 0.5 |
| pod start wait, mean (s) | 0.3 | 0.1 | 0.5 | 0.5 |
| host CPU busy, the real machine under kind (%) | 37.66 | 38.53 | 38.43 | 39.53 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 747.4 | 756.2 | 751 | 759.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.973 | 4.209 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.1625 | 0.05417 | 0.175 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.9 | 0.2 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 55.47 | 63.88 | 58.68 | 65.38 |
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
| worker nodes in service, mean | 6 | 4.843 | -19.3% | -2.095 to -0.2191 | yes: GAIN |
| node-hours | 2.514 | 2.03 | -19.2% | -0.8794 to -0.08842 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.5 | +0.1% | -0.7767 to +1.094 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 234.2 | -13.4% | -66.08 to -6.333 | yes: GAIN |
| response time (ms), mean | 273.3 | 246.7 | -9.7% | -42.26 to -11.03 | yes: GAIN |
| response time (ms), 95th percentile | 879.1 | 928.2 | +5.6% | -24.17 to +122.4 | no |
| response time (ms), 99th percentile | 1294 | 1335 | +3.1% | -83.08 to +163.8 | no |
| time over the response line (% of samples) | 14.17 | 14.21 | +0.3% | -0.5322 to +0.605 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.3 | +4.3% | -0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.2 | +58.2 (native is 0) | +34.92 to +81.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.993 | 9.257 | +2.9% | -1.869 to +2.396 | no |
| utilisation (used / allocatable) | 0.05501 | 0.06857 | +24.6% | +0.002392 to +0.02472 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.32 | 1.302 | -1.4% | -0.05158 to +0.01587 | no |
| Omni's own CPU (cores), mean | 0 | 0.01642 | +0.0164 (native is 0) | +0.01513 to +0.01771 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.32 | 1.319 | -0.1% | -0.03584 to +0.03297 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.9 | 430.7 | -14.7% | -136.6 to -11.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.253 | +11.5% | -0.02999 to +0.4964 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 38.53 | 39.53 | +2.6% | +0.4381 to +1.567 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 759.4 | +0.4% | -0.1004 to +6.5 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.209 | -29.8% | -3.206 to -0.3756 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.175 | +7.7% | -0.02481 to +0.04981 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.88 | 65.38 | +2.3% | -2.13 to +5.122 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.003e-15 to +4.702e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.514 | -0.0% | -0.00904 to +0.007374 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.4 | -0.1% | -1.449 to +0.7849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.4 | -0.1% | -1.449 to +0.7849 | no |
| response time (ms), mean | 247.6 | 273.3 | +10.4% | +2.291 to +49.07 | yes: LOSS |
| response time (ms), 95th percentile | 753.5 | 879.1 | +16.7% | +7.953 to +243.3 | yes: LOSS |
| response time (ms), 99th percentile | 1085 | 1294 | +19.3% | +8.929 to +409.2 | yes: LOSS |
| time over the response line (% of samples) | 13.3 | 14.17 | +6.5% | -0.232 to +1.973 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.567 | 8.993 | +5.0% | -1.041 to +1.895 | no |
| utilisation (used / allocatable) | 0.05524 | 0.05501 | -0.4% | -0.002203 to +0.001743 | no |
| CPU used (cores), mean | 1.326 | 1.32 | -0.4% | -0.05286 to +0.04184 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.326 | 1.32 | -0.4% | -0.05286 to +0.04184 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.5 | 504.9 | +1.5% | -15.36 to +30.22 | no |
| HPA replicas, mean | 1.946 | 2.019 | +3.8% | -0.0645 to +0.211 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | -66.7% | -0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | -66.7% | -0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 37.66 | 38.53 | +2.3% | +0.3664 to +1.36 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.4 | 756.2 | +1.2% | +0.5831 to +17.02 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.1625 | +550.0% | +0.07005 to +0.205 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.9 | +350.0% | +0.3545 to +1.046 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.47 | 63.88 | +15.2% | +1.011 to +15.82 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.766 | -20.6% | -2.107 to -0.36 | yes: GAIN |
| node-hours | 2.515 | 2 | -20.5% | -0.8818 to -0.1481 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | -0.5461 to +0.8701 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 232.1 | -14.3% | -66.6 to -10.71 | yes: GAIN |
| response time (ms), mean | 247.6 | 226 | -8.7% | -33.65 to -9.605 | yes: GAIN |
| response time (ms), 95th percentile | 753.5 | 837 | +11.1% | -1.13 to +168 | no |
| response time (ms), 99th percentile | 1085 | 1168 | +7.6% | -10.98 to +176.6 | no |
| time over the response line (% of samples) | 13.3 | 13.42 | +0.9% | -0.496 to +0.7285 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.7 (native is 0) | +28.35 to +59.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.567 | 10.08 | +17.7% | +0.167 to +2.866 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05524 | 0.06918 | +25.2% | +0.004643 to +0.02323 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.326 | 1.301 | -1.8% | -0.078 to +0.02927 | no |
| Omni's own CPU (cores), mean | 0 | 0.0147 | +0.0147 (native is 0) | +0.01359 to +0.01581 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.326 | 1.316 | -0.7% | -0.064 to +0.04467 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.5 | 427.6 | -14.0% | -116.4 to -23.33 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.228 | +14.5% | +0.004195 to +0.5592 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | -0.9081 to +1.308 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | -0.9081 to +1.308 | no |
| host CPU busy, the real machine under kind (%) | 37.66 | 38.43 | +2.0% | +0.5171 to +1.022 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.4 | 751 | +0.5% | +0.2415 to +6.958 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.973 | -33.8% | -3.406 to -0.6475 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.05417 | +116.7% | -0.0107 to +0.06903 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.47 | 58.68 | +5.8% | -0.5562 to +6.981 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.766 | -20.6% | -2.107 to -0.36 | yes: GAIN |
| node-hours | 2.514 | 2 | -20.4% | -0.8822 to -0.1459 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.9 | +0.2% | -0.557 to +1.545 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 232.1 | -14.2% | -65.99 to -10.66 | yes: GAIN |
| response time (ms), mean | 273.3 | 226 | -17.3% | -70.4 to -24.22 | yes: GAIN |
| response time (ms), 95th percentile | 879.1 | 837 | -4.8% | -132.6 to +48.24 | no |
| response time (ms), 99th percentile | 1294 | 1168 | -9.8% | -295.8 to +43.32 | no |
| time over the response line (% of samples) | 14.17 | 13.42 | -5.3% | -1.518 to +0.00985 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.7 (native is 0) | +28.35 to +59.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.993 | 10.08 | +12.1% | -0.2004 to +2.38 | no |
| utilisation (used / allocatable) | 0.05501 | 0.06918 | +25.8% | +0.003944 to +0.02439 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.32 | 1.301 | -1.4% | -0.03634 to -0.00136 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0147 | +0.0147 (native is 0) | +0.01359 to +0.01581 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.32 | 1.316 | -0.3% | -0.02225 to +0.01395 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.9 | 427.6 | -15.3% | -135.1 to -19.55 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.228 | +10.3% | -0.08684 to +0.5038 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | -0.4396 to +1.24 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | -0.4396 to +1.24 | no |
| host CPU busy, the real machine under kind (%) | 38.53 | 38.43 | -0.2% | -0.3806 to +0.1926 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 751 | -0.7% | -10.88 to +0.4806 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.973 | -33.8% | -3.406 to -0.6475 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.05417 | -66.7% | -0.1699 to -0.04677 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.2 | -77.8% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 63.88 | 58.68 | -8.1% | -9.871 to -0.5371 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.843 | -19.3% | -2.095 to -0.2191 | yes: GAIN |
| node-hours | 2.515 | 2.03 | -19.3% | -0.8787 to -0.09072 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.5 | -0.1% | -1.409 to +1.062 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 234.2 | -13.5% | -66.68 to -6.399 | yes: GAIN |
| response time (ms), mean | 247.6 | 246.7 | -0.4% | -17.62 to +15.7 | no |
| response time (ms), 95th percentile | 753.5 | 928.2 | +23.2% | +63.91 to +285.5 | yes: LOSS |
| response time (ms), 99th percentile | 1085 | 1335 | +23.0% | +52.24 to +446.7 | yes: LOSS |
| time over the response line (% of samples) | 13.3 | 14.21 | +6.8% | -0.06013 to +1.874 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.3 | +4.3% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.2 | +58.2 (native is 0) | +34.92 to +81.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.567 | 9.257 | +8.1% | -1.777 to +3.157 | no |
| utilisation (used / allocatable) | 0.05524 | 0.06857 | +24.1% | +0.003289 to +0.02336 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.326 | 1.302 | -1.8% | -0.07376 to +0.02702 | no |
| Omni's own CPU (cores), mean | 0 | 0.01642 | +0.0164 (native is 0) | +0.01513 to +0.01771 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.326 | 1.319 | -0.5% | -0.05817 to +0.04427 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.5 | 430.7 | -13.4% | -115 to -18.61 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.253 | +15.7% | +0.01353 to +0.5993 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | -0.7417 to +1.142 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | -0.7417 to +1.142 | no |
| host CPU busy, the real machine under kind (%) | 37.66 | 39.53 | +5.0% | +1.45 to +2.282 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.4 | 759.4 | +1.6% | +3.503 to +20.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.209 | -29.8% | -3.206 to -0.3756 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.175 | +600.0% | +0.08088 to +0.2191 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.9 | +350.0% | +0.3545 to +1.046 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.47 | 65.38 | +17.9% | +2.213 to +17.61 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*