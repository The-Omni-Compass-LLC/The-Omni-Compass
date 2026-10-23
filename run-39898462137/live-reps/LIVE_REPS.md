# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.538 | 5.935 |
| node-hours | 2.517 | 2.516 | 2.322 | 2.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 285.4 | 272.2 | 285.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 285.4 | 257.6 | 283.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 308.5 | 628.1 | 292.9 | 645.5 |
| response time (ms), 95th percentile | 998.1 | 1331 | 1119 | 1385 |
| response time (ms), 99th percentile | 1456 | 1788 | 1619 | 1838 |
| time over the response line (% of samples) | 16.81 | 54.59 | 17.7 | 57.03 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 23.5 | 9.7 | 23.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 111.5 | 23.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 1.998 | 10.48 | 2.417 |
| utilisation (used / allocatable) | 0.05893 | 0.0944 | 0.06344 | 0.09539 |
| CPU used (cores), mean | 1.414 | 2.266 | 1.411 | 2.267 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04759 | 0.0283 |
| CPU used with Omni's own (cores), mean | 1.414 | 2.266 | 1.459 | 2.296 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 302.5 | 441.1 | 299.5 |
| HPA replicas, mean | 1.948 | 1.978 | 2.626 | 2.813 |
| pods started | 0.3 | 0 | 1.1 | 0.8 |
| pod start wait, total (s) | 0.6 | 0 | 2.5 | 1.8 |
| pod start wait, mean (s) | 0.4 | 0 | 0.86 | 1 |
| host CPU busy, the real machine under kind (%) | 40.03 | 72.8 | 42.09 | 73.73 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 762.7 | 1427 | 771.2 | 1429 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.113 | 4.796 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 664.5 | 0.0625 | 684.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1134 | 0.4 | 1140 |
| queue: job turnaround, submitted to done, mean (s) | 71.76 | 909.6 | 79.54 | 912.1 |
| queue: jobs unfinished at the window's end | 0 | 14.2 | 0 | 14.6 |

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
| worker nodes in service, mean | 6 | 5.935 | -1.1% | -0.1644 to +0.03539 | no |
| node-hours | 2.516 | 2.489 | -1.1% | -0.07005 to +0.01572 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.4 | 285.4 | -0.0% | -1.149 to +1.101 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.4 | 283.4 | -0.7% | -5.221 to +1.123 | no |
| response time (ms), mean | 628.1 | 645.5 | +2.8% | -12.14 to +46.89 | no |
| response time (ms), 95th percentile | 1331 | 1385 | +4.1% | -17.27 to +125.6 | no |
| response time (ms), 99th percentile | 1788 | 1838 | +2.8% | -79.09 to +180.2 | no |
| time over the response line (% of samples) | 54.59 | 57.03 | +4.5% | -0.04017 to +4.929 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 23.6 | +0.4% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.8 | +23.8 (native is 0) | +18.88 to +28.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.998 | 2.417 | +20.9% | -0.1768 to +1.013 | no |
| utilisation (used / allocatable) | 0.0944 | 0.09539 | +1.1% | -0.000993 to +0.002978 | no |
| CPU used (cores), mean | 2.266 | 2.267 | +0.1% | -0.01906 to +0.02262 | no |
| Omni's own CPU (cores), mean | 0 | 0.0283 | +0.0283 (native is 0) | +0.02422 to +0.03238 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.266 | 2.296 | +1.3% | +0.01185 to +0.0483 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.5 | 299.5 | -1.0% | -9.046 to +2.914 | no |
| HPA replicas, mean | 1.978 | 2.813 | +42.2% | +0.5234 to +1.147 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | -0.07931 to +1.679 | no |
| pod start wait, total (s) | 0 | 1.8 | +1.8 (native is 0) | -0.07138 to +3.671 | no |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | -0.01782 to +2.018 | no |
| host CPU busy, the real machine under kind (%) | 72.8 | 73.73 | +1.3% | +0.5302 to +1.328 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1427 | 1429 | +0.1% | -8.513 to +12.51 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.796 | -20.1% | -3.792 to +1.385 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 664.5 | 684.1 | +2.9% | -74.97 to +114.1 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1134 | 1140 | +0.5% | -62.08 to +73.97 | no |
| queue: job turnaround, submitted to done, mean (s) | 909.6 | 912.1 | +0.3% | -36.72 to +41.69 | no |
| queue: jobs unfinished at the window's end | 14.2 | 14.6 | +2.8% | -1.657 to +2.457 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.59e-15 to +1.026e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.516 | -0.0% | -0.0114 to +0.009729 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 285.4 | +4.8% | +11.03 to +15.27 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 285.4 | +4.8% | +11.03 to +15.27 | yes: power given |
| response time (ms), mean | 308.5 | 628.1 | +103.6% | +235.9 to +403.4 | yes: LOSS |
| response time (ms), 95th percentile | 998.1 | 1331 | +33.4% | +90.77 to +575.4 | yes: LOSS |
| response time (ms), 99th percentile | 1456 | 1788 | +22.8% | -117.2 to +780.6 | no |
| time over the response line (% of samples) | 16.81 | 54.59 | +224.7% | +26.81 to +48.74 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 23.5 | +150.0% | +11.68 to +16.52 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 1.998 | -79.2% | -10.43 to -4.78 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05893 | 0.0944 | +60.2% | +0.03095 to +0.03999 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 2.266 | +60.2% | +0.7427 to +0.9598 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.414 | 2.266 | +60.2% | +0.7427 to +0.9598 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 302.5 | -35.3% | -200 to -129.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 1.978 | +1.5% | -0.1161 to +0.1763 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 40.03 | 72.8 | +81.9% | +29.71 to +35.84 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.7 | 1427 | +87.0% | +551.7 to +776.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 664.5 | +938086.7% | +395.4 to +933.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1134 | +283453.4% | +776.2 to +1491 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 71.76 | 909.6 | +1167.6% | +642.8 to +1033 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.2 | +14.2 (native is 0) | +8.039 to +20.36 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.538 | -7.7% | -0.9768 to +0.05219 | no |
| node-hours | 2.517 | 2.322 | -7.8% | -0.4101 to +0.02002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.2 | -0.0% | -0.8699 to +0.6423 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 257.6 | -5.4% | -31.19 to +1.805 | no |
| response time (ms), mean | 308.5 | 292.9 | -5.1% | -28.2 to -2.992 | yes: GAIN |
| response time (ms), 95th percentile | 998.1 | 1119 | +12.1% | +13.74 to +227.3 | yes: LOSS |
| response time (ms), 99th percentile | 1456 | 1619 | +11.2% | +62.86 to +263.6 | yes: LOSS |
| time over the response line (% of samples) | 16.81 | 17.7 | +5.3% | -0.009403 to +1.78 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.7 | +3.2% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.5 | +112 (native is 0) | +88.71 to +134.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 10.48 | +9.2% | -0.6849 to +2.445 | no |
| utilisation (used / allocatable) | 0.05893 | 0.06344 | +7.7% | +0.000626 to +0.008398 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.411 | -0.2% | -0.03954 to +0.03322 | no |
| Omni's own CPU (cores), mean | 0 | 0.04759 | +0.0476 (native is 0) | +0.04076 to +0.05442 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.459 | +3.1% | +0.002133 to +0.08672 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 441.1 | -5.6% | -49.91 to -2.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.626 | +34.8% | +0.3001 to +1.056 | yes: power given |
| pods started | 0.3 | 1.1 | +266.7% | -0.6621 to +2.262 | no |
| pod start wait, total (s) | 0.6 | 2.5 | +316.7% | -1.546 to +5.346 | no |
| pod start wait, mean (s) | 0.4 | 0.86 | +115.0% | -0.5127 to +1.433 | no |
| host CPU busy, the real machine under kind (%) | 40.03 | 42.09 | +5.2% | +1.536 to +2.588 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.7 | 771.2 | +1.1% | +4.218 to +12.78 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.113 | -14.8% | -1.861 to +0.0871 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | -11.8% | -0.05001 to +0.03335 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.76 | 79.54 | +10.8% | +2.159 to +13.41 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.538 | -7.7% | -0.9768 to +0.05219 | no |
| node-hours | 2.516 | 2.322 | -7.7% | -0.4058 to +0.01735 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.4 | 272.2 | -4.6% | -15.02 to -11.5 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.4 | 257.6 | -9.8% | -44.04 to -11.64 | yes: GAIN |
| response time (ms), mean | 628.1 | 292.9 | -53.4% | -419.9 to -250.6 | yes: GAIN |
| response time (ms), 95th percentile | 1331 | 1119 | -16.0% | -544.2 to +119 | no |
| response time (ms), 99th percentile | 1788 | 1619 | -9.4% | -680 to +343.1 | no |
| time over the response line (% of samples) | 54.59 | 17.7 | -67.6% | -47.32 to -26.46 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 9.7 | -58.7% | -16.34 to -11.26 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.5 | +112 (native is 0) | +88.71 to +134.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.998 | 10.48 | +424.6% | +5.791 to +11.18 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0944 | 0.06344 | -32.8% | -0.0369 to -0.02502 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.266 | 1.411 | -37.7% | -0.9715 to -0.7374 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04759 | +0.0476 (native is 0) | +0.04076 to +0.05442 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.266 | 1.459 | -35.6% | -0.9275 to -0.6862 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.5 | 441.1 | +45.8% | +116.7 to +160.5 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.626 | +32.8% | +0.2831 to +1.013 | yes: power given |
| pods started | 0 | 1.1 | +1.1 (native is 0) | -0.2254 to +2.425 | no |
| pod start wait, total (s) | 0 | 2.5 | +2.5 (native is 0) | -0.6856 to +5.686 | no |
| pod start wait, mean (s) | 0 | 0.86 | +0.86 (native is 0) | +0.05622 to +1.664 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.8 | 42.09 | -42.2% | -33.65 to -27.77 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1427 | 771.2 | -45.9% | -766.1 to -544.7 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.646 | -55.9% | -3.784 to -2.923 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 664.5 | 0.0625 | -100.0% | -933.6 to -395.4 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1134 | 0.4 | -100.0% | -1491 to -776.2 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 909.6 | 79.54 | -91.3% | -1022 to -638.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.2 | 0 | -100.0% | -20.36 to -8.039 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.935 | -1.1% | -0.1644 to +0.03539 | no |
| node-hours | 2.517 | 2.489 | -1.1% | -0.07455 to +0.01855 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 285.4 | +4.8% | +10.63 to +15.62 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 283.4 | +4.1% | +6.717 to +15.48 | yes: power given |
| response time (ms), mean | 308.5 | 645.5 | +109.3% | +257.2 to +416.9 | yes: LOSS |
| response time (ms), 95th percentile | 998.1 | 1385 | +38.8% | +146.3 to +628.2 | yes: LOSS |
| response time (ms), 99th percentile | 1456 | 1838 | +26.3% | -67.63 to +832.1 | no |
| time over the response line (% of samples) | 16.81 | 57.03 | +239.2% | +30.2 to +50.24 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 23.6 | +151.1% | +11.7 to +16.7 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.8 | +23.8 (native is 0) | +18.88 to +28.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 2.417 | -74.8% | -10.31 to -4.064 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05893 | 0.09539 | +61.9% | +0.03155 to +0.04138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 2.267 | +60.3% | +0.7384 to +0.9677 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0283 | +0.0283 (native is 0) | +0.02422 to +0.03238 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 2.296 | +62.3% | +0.7681 to +0.9946 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 299.5 | -35.9% | -207.7 to -128.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.813 | +44.4% | +0.6066 to +1.124 | yes: power given |
| pods started | 0.3 | 0.8 | +166.7% | -0.5796 to +1.58 | no |
| pod start wait, total (s) | 0.6 | 1.8 | +200.0% | -0.9801 to +3.38 | no |
| pod start wait, mean (s) | 0.4 | 1 | +150.0% | -0.3721 to +1.572 | no |
| host CPU busy, the real machine under kind (%) | 40.03 | 73.73 | +84.2% | +30.62 to +36.78 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.7 | 1429 | +87.3% | +556.3 to +775.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.796 | -20.1% | -3.792 to +1.385 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 684.1 | +965736.0% | +425.5 to +942.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1140 | +284939.5% | +761.9 to +1518 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 71.76 | 912.1 | +1171.0% | +646.5 to +1034 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.6 | +14.6 (native is 0) | +8.846 to +20.35 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*