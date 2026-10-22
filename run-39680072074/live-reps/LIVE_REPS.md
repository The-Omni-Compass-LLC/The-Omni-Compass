# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.94 | 11.81 |
| node-hours | 5.029 | 5.031 | 5.004 | 4.95 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527 | 527.8 | 528.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527 | 525.9 | 522.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 784.3 | 966.5 | 755 | 1011 |
| response time (ms), 95th percentile | 3138 | 4425 | 3273 | 4822 |
| response time (ms), 99th percentile | 4425 | 5976 | 4559 | 6281 |
| time over the response line (% of samples) | 28.11 | 32.24 | 28.65 | 32.98 |
| failed requests (%) | 0.02091 | 0.04372 | 0 | 0.126 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 17.6 | 14.5 | 18.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 58.2 | 34.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.95 | 58.51 | 24.18 | 49.35 |
| utilisation (used / allocatable) | 0.03701 | 0.03596 | 0.03745 | 0.03844 |
| CPU used (cores), mean | 1.777 | 1.726 | 1.79 | 1.821 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0124 | 0.01026 |
| CPU used with Omni's own (cores), mean | 1.777 | 1.726 | 1.802 | 1.831 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 740.1 | 710.1 | 695.8 |
| HPA replicas, mean | 4.099 | 4.117 | 4.7 | 4.812 |
| pods started | 0.1 | 0.4 | 1.6 | 1.9 |
| pod start wait, total (s) | 0.2 | 1.2 | 2.8 | 3.8 |
| pod start wait, mean (s) | 0.2 | 0.85 | 1.6 | 1.792 |
| host CPU busy, the real machine under kind (%) | 54.13 | 61.36 | 56.05 | 63.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 919.9 | 1054 | 938.8 | 1093 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.86 | 11.62 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 5.979 | 0.09167 | 12.87 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34.3 | 0.6 | 97.9 |
| queue: job turnaround, submitted to done, mean (s) | 229.7 | 358.1 | 241.4 | 387.9 |
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
| worker nodes in service, mean | 12 | 11.81 | -1.6% | -0.4936 to +0.1065 | no |
| node-hours | 5.031 | 4.95 | -1.6% | -0.2083 to +0.04561 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 528.5 | +0.3% | -1.145 to +4.054 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 522.4 | -0.9% | -14.94 to +5.7 | no |
| response time (ms), mean | 966.5 | 1011 | +4.6% | -22.62 to +110.8 | no |
| response time (ms), 95th percentile | 4425 | 4822 | +9.0% | -105.6 to +900.6 | no |
| response time (ms), 99th percentile | 5976 | 6281 | +5.1% | -142.7 to +753.7 | no |
| time over the response line (% of samples) | 32.24 | 32.98 | +2.3% | -0.8439 to +2.314 | no |
| failed requests (%) | 0.04372 | 0.126 | +188.2% | -0.06043 to +0.225 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 18.3 | +4.0% | +0.2172 to +1.183 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 | +34.7 (native is 0) | +27.85 to +41.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 58.51 | 49.35 | -15.6% | -52.4 to +34.09 | no |
| utilisation (used / allocatable) | 0.03596 | 0.03844 | +6.9% | -0.0006181 to +0.005589 | no |
| CPU used (cores), mean | 1.726 | 1.821 | +5.5% | -0.05894 to +0.2488 | no |
| Omni's own CPU (cores), mean | 0 | 0.01026 | +0.0103 (native is 0) | +0.009458 to +0.01106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.726 | 1.831 | +6.1% | -0.04912 to +0.2595 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.1 | 695.8 | -6.0% | -102.2 to +13.48 | no |
| HPA replicas, mean | 4.117 | 4.812 | +16.9% | +0.3613 to +1.029 | yes: power given |
| pods started | 0.4 | 1.9 | +375.0% | +0.5315 to +2.469 | yes: power given |
| pod start wait, total (s) | 1.2 | 3.8 | +216.7% | -0.1642 to +5.364 | no |
| pod start wait, mean (s) | 0.85 | 1.792 | +110.8% | -0.325 to +2.208 | no |
| host CPU busy, the real machine under kind (%) | 61.36 | 63.9 | +4.1% | +1.373 to +3.706 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1054 | 1093 | +3.7% | +15.29 to +62.11 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.62 | -3.1% | -0.9693 to +0.2145 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.979 | 12.87 | +115.3% | -5.458 to +19.24 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.3 | 97.9 | +185.4% | -32.7 to +159.9 | no |
| queue: job turnaround, submitted to done, mean (s) | 358.1 | 387.9 | +8.3% | +0.7824 to +58.81 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -5.475e-15 to +2.633e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.029 | 5.031 | +0.0% | -0.01013 to +0.0148 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527 | -0.1% | -3.011 to +2.134 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 527 | -0.1% | -3.011 to +2.134 | no |
| response time (ms), mean | 784.3 | 966.5 | +23.2% | +124.3 to +240.2 | yes: LOSS |
| response time (ms), 95th percentile | 3138 | 4425 | +41.0% | +765.5 to +1808 | yes: LOSS |
| response time (ms), 99th percentile | 4425 | 5976 | +35.1% | +839.1 to +2263 | yes: LOSS |
| time over the response line (% of samples) | 28.11 | 32.24 | +14.7% | +1.157 to +7.109 | yes: LOSS |
| failed requests (%) | 0.02091 | 0.04372 | +109.1% | -0.01494 to +0.06056 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 17.6 | +30.4% | +2.009 to +6.191 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.95 | 58.51 | +226.0% | -0.5472 to +81.66 | no |
| utilisation (used / allocatable) | 0.03701 | 0.03596 | -2.8% | -0.004265 to +0.002162 | no |
| CPU used (cores), mean | 1.777 | 1.726 | -2.8% | -0.2047 to +0.1038 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.777 | 1.726 | -2.8% | -0.2047 to +0.1038 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 740.1 | +2.7% | -40.4 to +79.99 | no |
| HPA replicas, mean | 4.099 | 4.117 | +0.5% | -0.231 to +0.2683 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | -0.7843 to +2.784 | no |
| pod start wait, mean (s) | 0.2 | 0.85 | +325.0% | -0.5428 to +1.843 | no |
| host CPU busy, the real machine under kind (%) | 54.13 | 61.36 | +13.4% | +6.015 to +8.45 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 919.9 | 1054 | +14.6% | +89.79 to +179.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 5.979 | +4848.3% | -0.9564 to +12.67 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 34.3 | +4800.0% | -38.9 to +106.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.7 | 358.1 | +55.9% | +84.78 to +171.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.94 | -0.5% | -0.1787 to +0.05407 | no |
| node-hours | 5.029 | 5.004 | -0.5% | -0.07698 to +0.02681 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 527.8 | +0.1% | -1.305 to +1.98 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 525.9 | -0.3% | -5.795 to +2.558 | no |
| response time (ms), mean | 784.3 | 755 | -3.7% | -67.02 to +8.462 | no |
| response time (ms), 95th percentile | 3138 | 3273 | +4.3% | -46.22 to +316.3 | no |
| response time (ms), 99th percentile | 4425 | 4559 | +3.0% | -161.2 to +430.5 | no |
| time over the response line (% of samples) | 28.11 | 28.65 | +1.9% | -0.7996 to +1.889 | no |
| failed requests (%) | 0.02091 | 0 | -100.0% | -0.0682 to +0.02638 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 14.5 | +7.4% | -0.1681 to +2.168 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.2 | +58.2 (native is 0) | +25.32 to +91.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.95 | 24.18 | +34.7% | -4.105 to +16.58 | no |
| utilisation (used / allocatable) | 0.03701 | 0.03745 | +1.2% | -0.0006505 to +0.001532 | no |
| CPU used (cores), mean | 1.777 | 1.79 | +0.7% | -0.03682 to +0.06296 | no |
| Omni's own CPU (cores), mean | 0 | 0.0124 | +0.0124 (native is 0) | +0.01115 to +0.01365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.777 | 1.802 | +1.4% | -0.02366 to +0.07459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 710.1 | -1.4% | -29.88 to +9.469 | no |
| HPA replicas, mean | 4.099 | 4.7 | +14.7% | +0.3822 to +0.8213 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.8921 to +2.108 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | +1.422 to +3.778 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.6 | +700.0% | +0.7968 to +2.003 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.13 | 56.05 | +3.6% | +1.221 to +2.624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 919.9 | 938.8 | +2.1% | +3.609 to +34.19 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.86 | -1.1% | -0.3673 to +0.09587 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.09167 | -24.1% | -0.08886 to +0.03052 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | -14.3% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.7 | 241.4 | +5.1% | -0.326 to +23.63 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.94 | -0.5% | -0.1787 to +0.05407 | no |
| node-hours | 5.031 | 5.004 | -0.5% | -0.07769 to +0.02286 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 527.8 | +0.1% | -1.614 to +3.167 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 525.9 | -0.2% | -5.707 to +3.347 | no |
| response time (ms), mean | 966.5 | 755 | -21.9% | -275.2 to -147.8 | yes: GAIN |
| response time (ms), 95th percentile | 4425 | 3273 | -26.0% | -1662 to -641.3 | yes: GAIN |
| response time (ms), 99th percentile | 5976 | 4559 | -23.7% | -2174 to -658.8 | yes: GAIN |
| time over the response line (% of samples) | 32.24 | 28.65 | -11.1% | -5.611 to -1.566 | yes: GAIN |
| failed requests (%) | 0.04372 | 0 | -100.0% | -0.08706 to -0.0003796 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 14.5 | -17.6% | -4.698 to -1.502 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.2 | +58.2 (native is 0) | +25.32 to +91.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 58.51 | 24.19 | -58.7% | -70.37 to +1.727 | no |
| utilisation (used / allocatable) | 0.03596 | 0.03745 | +4.1% | -0.001672 to +0.004657 | no |
| CPU used (cores), mean | 1.726 | 1.79 | +3.7% | -0.08861 to +0.2157 | no |
| Omni's own CPU (cores), mean | 0 | 0.0124 | +0.0124 (native is 0) | +0.01115 to +0.01365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.726 | 1.802 | +4.4% | -0.07647 to +0.2283 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.1 | 710.1 | -4.1% | -89.2 to +29.19 | no |
| HPA replicas, mean | 4.117 | 4.7 | +14.2% | +0.2559 to +0.9102 | yes: power given |
| pods started | 0.4 | 1.6 | +300.0% | +0.6358 to +1.764 | yes: power given |
| pod start wait, total (s) | 1.2 | 2.8 | +133.3% | -0.4566 to +3.657 | no |
| pod start wait, mean (s) | 0.85 | 1.6 | +88.2% | -0.5032 to +2.003 | no |
| host CPU busy, the real machine under kind (%) | 61.36 | 56.05 | -8.7% | -6.447 to -4.173 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1054 | 938.8 | -11.0% | -154.2 to -76.98 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.86 | -1.1% | -0.3673 to +0.09587 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.979 | 0.09167 | -98.5% | -12.7 to +0.923 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 34.3 | 0.6 | -98.3% | -106.2 to +38.77 | no |
| queue: job turnaround, submitted to done, mean (s) | 358.1 | 241.4 | -32.6% | -157.9 to -75.43 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.81 | -1.6% | -0.4936 to +0.1065 | no |
| node-hours | 5.029 | 4.95 | -1.6% | -0.2057 to +0.04764 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.5 | 528.5 | +0.2% | -0.9688 to +3.001 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.5 | 522.4 | -1.0% | -14.84 to +4.715 | no |
| response time (ms), mean | 784.3 | 1011 | +28.9% | +125.8 to +326.8 | yes: LOSS |
| response time (ms), 95th percentile | 3138 | 4822 | +53.7% | +925.3 to +2443 | yes: LOSS |
| response time (ms), 99th percentile | 4425 | 6281 | +42.0% | +937.3 to +2776 | yes: LOSS |
| time over the response line (% of samples) | 28.11 | 32.98 | +17.3% | +3.011 to +6.726 | yes: LOSS |
| failed requests (%) | 0.02091 | 0.126 | +502.6% | -0.02965 to +0.2398 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 18.3 | +35.6% | +2.99 to +6.61 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 | +34.7 (native is 0) | +27.85 to +41.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.95 | 49.35 | +174.9% | +3.036 to +59.77 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03701 | 0.03844 | +3.9% | -0.001049 to +0.003917 | no |
| CPU used (cores), mean | 1.777 | 1.821 | +2.5% | -0.07426 to +0.1632 | no |
| Omni's own CPU (cores), mean | 0 | 0.01026 | +0.0103 (native is 0) | +0.009458 to +0.01106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.777 | 1.831 | +3.1% | -0.06414 to +0.1736 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.3 | 695.8 | -3.4% | -66.61 to +17.53 | no |
| HPA replicas, mean | 4.099 | 4.812 | +17.4% | +0.4312 to +0.9959 | yes: power given |
| pods started | 0.1 | 1.9 | +1800.0% | +1.143 to +2.457 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.8 | +1800.0% | +1.976 to +5.224 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.792 | +795.8% | +0.8761 to +2.307 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.13 | 63.9 | +18.1% | +7.755 to +11.79 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 919.9 | 1093 | +18.8% | +112.9 to +233.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.62 | -3.1% | -0.9693 to +0.2145 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 12.87 | +10551.7% | -0.6779 to +26.18 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 97.9 | +13885.7% | -13.61 to +208 | no |
| queue: job turnaround, submitted to done, mean (s) | 229.7 | 387.9 | +68.8% | +105.9 to +210.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*