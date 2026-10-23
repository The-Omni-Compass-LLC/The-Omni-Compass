# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.48 | 11.47 |
| node-hours | 5.02 | 5.033 | 4.812 | 4.8 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 528.8 | 528 | 529.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 528.8 | 511.7 | 512.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 702.4 | 938 | 761.6 | 1182 |
| response time (ms), 95th percentile | 2910 | 4793 | 3598 | 5968 |
| response time (ms), 99th percentile | 4237 | 6738 | 5309 | 7843 |
| time over the response line (% of samples) | 29.43 | 30.07 | 29.67 | 33.08 |
| failed requests (%) | 0 | 0.04073 | 0.01314 | 0.4768 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 16.2 | 14.7 | 17.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 145.6 | 137.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 8.333 | 3.75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.31 | 21.16 | 21.34 | 33.48 |
| utilisation (used / allocatable) | 0.03629 | 0.03847 | 0.03962 | 0.04227 |
| CPU used (cores), mean | 1.742 | 1.847 | 1.806 | 1.935 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04155 | 0.03571 |
| CPU used with Omni's own (cores), mean | 1.742 | 1.847 | 1.847 | 1.971 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.2 | 694.9 | 676.4 | 637.4 |
| HPA replicas, mean | 4.056 | 4.227 | 5.551 | 5.296 |
| pods started | 0 | 0 | 4.5 | 3.8 |
| pod start wait, total (s) | 0 | 0 | 9.2 | 9.1 |
| pod start wait, mean (s) | 0 | 0 | 1.811 | 2.168 |
| host CPU busy, the real machine under kind (%) | 52.87 | 60.25 | 58.02 | 67.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 890 | 1031 | 939.3 | 1128 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.2 | 11.28 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.5542 | 0.09167 | 3.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.4 | 0.8 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 203.5 | 324.8 | 237.1 | 428.7 |
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
| worker nodes in service, mean | 12 | 11.47 | -4.4% | -1.74 to +0.6731 | no |
| node-hours | 5.033 | 4.8 | -4.6% | -0.7416 to +0.2768 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.8 | 529.2 | +0.1% | -2.117 to +2.925 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.8 | 512.5 | -3.1% | -55.01 to +22.46 | no |
| response time (ms), mean | 938 | 1182 | +26.0% | +123 to +364.2 | yes: LOSS |
| response time (ms), 95th percentile | 4793 | 5968 | +24.5% | +687.3 to +1663 | yes: LOSS |
| response time (ms), 99th percentile | 6738 | 7843 | +16.4% | +720.9 to +1489 | yes: LOSS |
| time over the response line (% of samples) | 30.07 | 33.08 | +10.0% | +1.083 to +4.938 | yes: LOSS |
| failed requests (%) | 0.04073 | 0.4768 | +1070.6% | +0.2186 to +0.6536 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.2 | 17.8 | +9.9% | +0.9968 to +2.203 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137.5 | +138 (native is 0) | +117.3 to +157.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.16 | 33.48 | +58.2% | +0.9533 to +23.68 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03847 | 0.04227 | +9.9% | -0.0001411 to +0.007736 | no |
| CPU used (cores), mean | 1.847 | 1.935 | +4.8% | +0.0107 to +0.1666 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03571 | +0.0357 (native is 0) | +0.03145 to +0.03997 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.847 | 1.971 | +6.7% | +0.04339 to +0.2053 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 637.4 | -8.3% | -121.2 to +6.104 | no |
| HPA replicas, mean | 4.227 | 5.296 | +25.3% | +0.6929 to +1.445 | yes: power given |
| pods started | 0 | 3.8 | +3.8 (native is 0) | +2.087 to +5.513 | yes: power given |
| pod start wait, total (s) | 0 | 9.1 | +9.1 (native is 0) | +4.496 to +13.7 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.168 | +2.17 (native is 0) | +1.453 to +2.882 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.25 | 67.27 | +11.6% | +5.687 to +8.348 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1031 | 1128 | +9.4% | +64.56 to +128.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.28 | -6.0% | -2.345 to +0.9071 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5542 | 3.5 | +531.6% | -1.039 to +6.931 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 3.5 | +150.0% | -1.939 to +6.139 | no |
| queue: job turnaround, submitted to done, mean (s) | 324.8 | 428.7 | +32.0% | +72.11 to +135.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | +9.405e-16 to +5.099e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.02 | 5.033 | +0.3% | +0.000767 to +0.02523 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 528.8 | +0.6% | +1.375 to +4.608 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 528.8 | +0.6% | +1.375 to +4.608 | yes: power given |
| response time (ms), mean | 702.4 | 938 | +33.5% | +171 to +300 | yes: LOSS |
| response time (ms), 95th percentile | 2910 | 4793 | +64.7% | +1383 to +2381 | yes: LOSS |
| response time (ms), 99th percentile | 4237 | 6738 | +59.0% | +1795 to +3206 | yes: LOSS |
| time over the response line (% of samples) | 29.43 | 30.07 | +2.2% | -0.3533 to +1.629 | no |
| failed requests (%) | 0 | 0.04073 | +0.0407 (native is 0) | -0.005916 to +0.08738 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 16.2 | +18.2% | +1.805 to +3.195 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.31 | 21.16 | +38.3% | +3.468 to +8.252 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03629 | 0.03847 | +6.0% | +0.001125 to +0.003235 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.742 | 1.847 | +6.0% | +0.05399 to +0.1553 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.742 | 1.847 | +6.0% | +0.05399 to +0.1553 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.2 | 694.9 | -4.6% | -57.59 to -8.919 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.056 | 4.227 | +4.2% | -0.02889 to +0.3715 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 52.87 | 60.25 | +14.0% | +6.19 to +8.573 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 890 | 1031 | +15.8% | +103.8 to +178.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.5542 | +638.9% | +0.3525 to +0.6058 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.4 | +133.3% | +0.2358 to +1.364 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 203.5 | 324.8 | +59.6% | +89.66 to +152.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.48 | -4.3% | -1.693 to +0.6551 | no |
| node-hours | 5.02 | 4.812 | -4.1% | -0.7022 to +0.2872 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 528 | +0.4% | +0.6078 to +3.747 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 511.7 | -2.7% | -51.3 to +23.08 | no |
| response time (ms), mean | 702.4 | 761.6 | +8.4% | +25.18 to +93.21 | yes: LOSS |
| response time (ms), 95th percentile | 2910 | 3598 | +23.6% | +422 to +953.4 | yes: LOSS |
| response time (ms), 99th percentile | 4237 | 5309 | +25.3% | +504.2 to +1639 | yes: LOSS |
| time over the response line (% of samples) | 29.43 | 29.67 | +0.8% | -0.7398 to +1.224 | no |
| failed requests (%) | 0 | 0.01314 | +0.0131 (native is 0) | -0.006685 to +0.03297 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 14.7 | +7.3% | +0.6628 to +1.337 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145.6 | +146 (native is 0) | +110.9 to +180.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.31 | 21.34 | +39.4% | +3.142 to +8.925 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03629 | 0.03962 | +9.2% | -0.0006972 to +0.007362 | no |
| CPU used (cores), mean | 1.742 | 1.806 | +3.7% | +0.02848 to +0.09904 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04155 | +0.0416 (native is 0) | +0.03989 to +0.04321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.742 | 1.847 | +6.0% | +0.06876 to +0.1419 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.2 | 676.4 | -7.1% | -109 to +5.536 | no |
| HPA replicas, mean | 4.056 | 5.551 | +36.9% | +1.082 to +1.909 | yes: power given |
| pods started | 0 | 4.5 | +4.5 (native is 0) | +3.141 to +5.859 | yes: power given |
| pod start wait, total (s) | 0 | 9.2 | +9.2 (native is 0) | +5.831 to +12.57 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.811 | +1.81 (native is 0) | +1.26 to +2.362 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.87 | 58.02 | +9.7% | +4.309 to +5.999 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 890 | 939.3 | +5.5% | +30.16 to +68.44 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.2 | -6.7% | -2.61 to +1.01 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.09167 | +22.2% | -0.04327 to +0.07661 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 203.5 | 237.1 | +16.5% | +18.95 to +48.17 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.48 | -4.3% | -1.693 to +0.6551 | no |
| node-hours | 5.033 | 4.812 | -4.4% | -0.7155 to +0.2745 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.8 | 528 | -0.2% | -3.034 to +1.405 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.8 | 511.7 | -3.2% | -53.86 to +19.65 | no |
| response time (ms), mean | 938 | 761.6 | -18.8% | -233 to -119.6 | yes: GAIN |
| response time (ms), 95th percentile | 4793 | 3598 | -24.9% | -1611 to -777.6 | yes: GAIN |
| response time (ms), 99th percentile | 6738 | 5309 | -21.2% | -1928 to -930.3 | yes: GAIN |
| time over the response line (% of samples) | 30.07 | 29.67 | -1.3% | -1.361 to +0.5697 | no |
| failed requests (%) | 0.04073 | 0.01314 | -67.7% | -0.07937 to +0.0242 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.2 | 14.7 | -9.3% | -2.195 to -0.8048 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 145.6 | +146 (native is 0) | +110.9 to +180.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.16 | 21.34 | +0.8% | -2.772 to +3.119 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03962 | +3.0% | -0.003805 to +0.006111 | no |
| CPU used (cores), mean | 1.847 | 1.806 | -2.2% | -0.06849 to -0.01323 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04155 | +0.0416 (native is 0) | +0.03989 to +0.04321 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.847 | 1.847 | +0.0% | -0.02654 to +0.02792 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 676.4 | -2.7% | -98.47 to +61.48 | no |
| HPA replicas, mean | 4.227 | 5.551 | +31.3% | +0.931 to +1.717 | yes: power given |
| pods started | 0 | 4.5 | +4.5 (native is 0) | +3.141 to +5.859 | yes: power given |
| pod start wait, total (s) | 0 | 9.2 | +9.2 (native is 0) | +5.831 to +12.57 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.811 | +1.81 (native is 0) | +1.26 to +2.362 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.25 | 58.02 | -3.7% | -3.575 to -0.8807 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1031 | 939.3 | -8.9% | -121.1 to -62.31 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.2 | -6.7% | -2.61 to +1.01 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5542 | 0.09167 | -83.5% | -0.6047 to -0.3203 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.8 | -42.9% | -1.203 to +0.0032 | no |
| queue: job turnaround, submitted to done, mean (s) | 324.8 | 237.1 | -27.0% | -113 to -62.38 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.47 | -4.4% | -1.74 to +0.6731 | no |
| node-hours | 5.02 | 4.8 | -4.4% | -0.7283 to +0.2895 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 529.2 | +0.6% | +1.552 to +5.239 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 512.5 | -2.5% | -52.44 to +25.87 | no |
| response time (ms), mean | 702.4 | 1182 | +68.2% | +325.4 to +632.8 | yes: LOSS |
| response time (ms), 95th percentile | 2910 | 5968 | +105.1% | +2239 to +3875 | yes: LOSS |
| response time (ms), 99th percentile | 4237 | 7843 | +85.1% | +2711 to +4500 | yes: LOSS |
| time over the response line (% of samples) | 29.43 | 33.08 | +12.4% | +1.777 to +5.519 | yes: LOSS |
| failed requests (%) | 0 | 0.4768 | +0.477 (native is 0) | +0.2734 to +0.6802 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 17.8 | +29.9% | +2.91 to +5.29 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 137.5 | +138 (native is 0) | +117.3 to +157.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.31 | 33.48 | +118.8% | +5.706 to +30.65 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03629 | 0.04227 | +16.5% | +0.003008 to +0.008946 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.742 | 1.935 | +11.1% | +0.09411 to +0.2924 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03571 | +0.0357 (native is 0) | +0.03145 to +0.03997 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.742 | 1.971 | +13.1% | +0.1257 to +0.3322 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 728.2 | 637.4 | -12.5% | -131.5 to -50.07 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.056 | 5.296 | +30.6% | +0.7957 to +1.685 | yes: power given |
| pods started | 0 | 3.8 | +3.8 (native is 0) | +2.087 to +5.513 | yes: power given |
| pod start wait, total (s) | 0 | 9.1 | +9.1 (native is 0) | +4.496 to +13.7 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.168 | +2.17 (native is 0) | +1.453 to +2.882 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.87 | 67.27 | +27.2% | +12.22 to +16.58 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 890 | 1128 | +26.7% | +175.8 to +299.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.28 | -6.0% | -2.345 to +0.9071 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 3.5 | +4566.7% | -0.5776 to +7.428 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 3.5 | +483.3% | -0.9513 to +6.751 | no |
| queue: job turnaround, submitted to done, mean (s) | 203.5 | 428.7 | +110.6% | +166.3 to +284 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*