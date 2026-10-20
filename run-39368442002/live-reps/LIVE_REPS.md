# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.187 | 4.999 |
| node-hours | 2.517 | 2.514 | 2.175 | 2.097 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.6 | 271.9 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.6 | 246.3 | 240.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 271.9 | 249.6 | 233.1 | 213.4 |
| response time (ms), 95th percentile | 827.2 | 822.7 | 872.2 | 887.2 |
| response time (ms), 99th percentile | 1250 | 1375 | 1246 | 1410 |
| time over the response line (% of samples) | 14.12 | 10.38 | 13.47 | 10.12 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.9 | 8.6 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 47.4 | 42.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.69 | 10.04 | 9.003 | 10.73 |
| utilisation (used / allocatable) | 0.05809 | 0.05782 | 0.06849 | 0.0709 |
| CPU used (cores), mean | 1.394 | 1.388 | 1.389 | 1.373 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01653 | 0.01685 |
| CPU used with Omni's own (cores), mean | 1.394 | 1.388 | 1.405 | 1.39 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 471.3 | 424.5 | 417.1 |
| HPA replicas, mean | 1.914 | 1.971 | 1.992 | 2.134 |
| pods started | 0.2 | 0 | 0 | 0.4 |
| pod start wait, total (s) | 0.7 | 0 | 0 | 0.6 |
| pod start wait, mean (s) | 0.7 | 0 | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 39.81 | 39.54 | 40.51 | 40.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750.8 | 748.4 | 754.2 | 750.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.555 | 4.343 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.07917 | 0.0375 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | 0.3 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 58.77 | 58.35 | 61.3 | 61.38 |
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
| worker nodes in service, mean | 6 | 4.999 | -16.7% | -1.803 to -0.1993 | yes: GAIN |
| node-hours | 2.514 | 2.097 | -16.6% | -0.7546 to -0.07895 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.8 | +0.1% | -0.9122 to +1.27 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 240.4 | -11.5% | -56.65 to -5.855 | yes: GAIN |
| response time (ms), mean | 249.6 | 213.4 | -14.5% | -44.61 to -27.76 | yes: GAIN |
| response time (ms), 95th percentile | 822.7 | 887.2 | +7.8% | -15.8 to +144.8 | no |
| response time (ms), 99th percentile | 1375 | 1410 | +2.5% | -8.807 to +78.81 | no |
| time over the response line (% of samples) | 10.38 | 10.12 | -2.5% | -1.002 to +0.4784 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 7.8 | -1.3% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.1 | +42.1 (native is 0) | +32.08 to +52.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.04 | 10.73 | +6.9% | -0.3584 to +1.748 | no |
| utilisation (used / allocatable) | 0.05782 | 0.0709 | +22.6% | +0.001727 to +0.02444 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.388 | 1.373 | -1.1% | -0.0371 to +0.007517 | no |
| Omni's own CPU (cores), mean | 0 | 0.01685 | +0.0169 (native is 0) | +0.01557 to +0.01813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.39 | +0.1% | -0.02049 to +0.02461 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.3 | 417.1 | -11.5% | -102.2 to -6.229 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.971 | 2.134 | +8.3% | +0.008677 to +0.3177 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| host CPU busy, the real machine under kind (%) | 39.54 | 40.5 | +2.4% | +0.8158 to +1.105 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 748.4 | 750.4 | +0.3% | -1.553 to +5.553 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.343 | -27.6% | -2.893 to -0.421 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.05833 | -26.3% | -0.0498 to +0.008131 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | -33.3% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.35 | 61.38 | +5.2% | +0.5155 to +5.543 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.05e-15 to +1.405e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | -0.1% | -0.00946 to +0.00246 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.6 | -0.1% | -1.212 to +0.5686 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.6 | -0.1% | -1.212 to +0.5686 | no |
| response time (ms), mean | 271.9 | 249.6 | -8.2% | -41.23 to -3.357 | yes: GAIN |
| response time (ms), 95th percentile | 827.2 | 822.7 | -0.6% | -85.74 to +76.63 | no |
| response time (ms), 99th percentile | 1250 | 1375 | +9.9% | -92.29 to +340.8 | no |
| time over the response line (% of samples) | 14.12 | 10.38 | -26.5% | -6.867 to -0.6106 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.9 | -4.8% | -0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.69 | 10.04 | +3.6% | -1.045 to +1.735 | no |
| utilisation (used / allocatable) | 0.05809 | 0.05782 | -0.5% | -0.001233 to +0.0006862 | no |
| CPU used (cores), mean | 1.394 | 1.388 | -0.5% | -0.0296 to +0.01647 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.394 | 1.388 | -0.5% | -0.0296 to +0.01647 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 471.3 | +0.5% | -5.084 to +9.679 | no |
| HPA replicas, mean | 1.914 | 1.971 | +3.0% | -0.05449 to +0.1699 | no |
| pods started | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.7 | 0 | -100.0% | -1.769 to +0.369 | no |
| pod start wait, mean (s) | 0.7 | 0 | -100.0% | -1.769 to +0.369 | no |
| host CPU busy, the real machine under kind (%) | 39.81 | 39.54 | -0.7% | -0.5844 to +0.03353 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.8 | 748.4 | -0.3% | -8.339 to +3.539 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.07917 | +90.0% | -0.003342 to +0.07834 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.77 | 58.35 | -0.7% | -4.36 to +3.519 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.187 | -13.6% | -1.496 to -0.1303 | yes: GAIN |
| node-hours | 2.517 | 2.175 | -13.6% | -0.6229 to -0.06112 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.9 | -0.0% | -0.9933 to +0.9092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 246.3 | -9.4% | -46.74 to -4.542 | yes: GAIN |
| response time (ms), mean | 271.9 | 233.1 | -14.3% | -54.25 to -23.28 | yes: GAIN |
| response time (ms), 95th percentile | 827.2 | 872.2 | +5.4% | -12.35 to +102.4 | no |
| response time (ms), 99th percentile | 1250 | 1246 | -0.3% | -149 to +141 | no |
| time over the response line (% of samples) | 14.12 | 13.47 | -4.6% | -2.137 to +0.8452 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.6 | +3.6% | -0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.4 (native is 0) | +31.46 to +63.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.69 | 9.003 | -7.1% | -2.072 to +0.6984 | no |
| utilisation (used / allocatable) | 0.05809 | 0.06849 | +17.9% | +0.001521 to +0.01928 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.389 | -0.4% | -0.02987 to +0.01922 | no |
| Omni's own CPU (cores), mean | 0 | 0.01653 | +0.0165 (native is 0) | +0.01471 to +0.01835 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.405 | +0.8% | -0.01367 to +0.03609 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 424.5 | -9.5% | -81.76 to -7.241 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.914 | 1.992 | +4.1% | -0.09399 to +0.2501 | no |
| pods started | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.7 | 0 | -100.0% | -1.769 to +0.369 | no |
| pod start wait, mean (s) | 0.7 | 0 | -100.0% | -1.769 to +0.369 | no |
| host CPU busy, the real machine under kind (%) | 39.81 | 40.51 | +1.7% | +0.2496 to +1.134 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.8 | 754.2 | +0.5% | -0.4624 to +7.262 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.555 | -24.1% | -2.55 to -0.3411 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.0375 | -10.0% | -0.05374 to +0.04541 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.77 | 61.3 | +4.3% | -1.347 to +6.397 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.187 | -13.6% | -1.496 to -0.1303 | yes: GAIN |
| node-hours | 2.514 | 2.175 | -13.5% | -0.6213 to -0.05572 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.9 | +0.1% | -0.9609 to +1.52 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 246.3 | -9.3% | -46.6 to -4.042 | yes: GAIN |
| response time (ms), mean | 249.6 | 233.1 | -6.6% | -41.09 to +8.158 | no |
| response time (ms), 95th percentile | 822.7 | 872.2 | +6.0% | -59.93 to +159.1 | no |
| response time (ms), 99th percentile | 1375 | 1246 | -9.3% | -349.7 to +93.11 | no |
| time over the response line (% of samples) | 10.38 | 13.47 | +29.8% | +0.09942 to +6.086 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.6 | +8.9% | -0.369 to +1.769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.4 (native is 0) | +31.46 to +63.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.04 | 9.003 | -10.3% | -3.336 to +1.273 | no |
| utilisation (used / allocatable) | 0.05782 | 0.06849 | +18.5% | +0.001579 to +0.01977 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.388 | 1.389 | +0.1% | -0.03312 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0 | 0.01653 | +0.0165 (native is 0) | +0.01471 to +0.01835 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.405 | +1.3% | -0.01702 to +0.05256 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.3 | 424.5 | -9.9% | -86.49 to -7.106 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.971 | 1.992 | +1.0% | -0.1232 to +0.1638 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 39.54 | 40.51 | +2.4% | +0.5199 to +1.414 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 748.4 | 754.2 | +0.8% | -1.239 to +12.84 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.555 | -24.1% | -2.55 to -0.3411 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.0375 | -52.6% | -0.07608 to -0.007251 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.3 | -50.0% | -0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.35 | 61.3 | +5.0% | -2.88 to +8.771 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.999 | -16.7% | -1.803 to -0.1993 | yes: GAIN |
| node-hours | 2.517 | 2.097 | -16.7% | -0.757 to -0.08348 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | -0.1% | -1.15 to +0.864 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 240.4 | -11.6% | -56.91 to -6.241 | yes: GAIN |
| response time (ms), mean | 271.9 | 213.4 | -21.5% | -74.79 to -42.17 | yes: GAIN |
| response time (ms), 95th percentile | 827.2 | 887.2 | +7.2% | -26.9 to +146.8 | no |
| response time (ms), 99th percentile | 1250 | 1410 | +12.7% | -45.17 to +363.7 | no |
| time over the response line (% of samples) | 14.12 | 10.12 | -28.3% | -7.053 to -0.9477 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.8 | -6.0% | -1.108 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.1 | +42.1 (native is 0) | +32.08 to +52.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.69 | 10.73 | +10.7% | -0.4935 to +2.573 | no |
| utilisation (used / allocatable) | 0.05809 | 0.0709 | +22.1% | +0.001725 to +0.02389 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.373 | -1.5% | -0.04207 to -0.0006411 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01685 | +0.0169 (native is 0) | +0.01557 to +0.01813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.39 | -0.3% | -0.02554 to +0.01652 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 417.1 | -11.1% | -96.77 to -7.059 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.914 | 2.134 | +11.5% | +0.04645 to +0.3954 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.7 | 0.6 | -14.3% | -1.382 to +1.182 | no |
| pod start wait, mean (s) | 0.7 | 0.6 | -14.3% | -1.382 to +1.182 | no |
| host CPU busy, the real machine under kind (%) | 39.81 | 40.5 | +1.7% | +0.3272 to +1.043 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.8 | 750.4 | -0.1% | -3.742 to +2.942 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.343 | -27.6% | -2.893 to -0.421 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 | +40.0% | -0.02595 to +0.05928 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.77 | 61.38 | +4.4% | -0.6672 to +5.884 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*