# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.81 | 11.11 |
| node-hours | 5.033 | 5.033 | 4.53 | 4.654 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 527.8 | 526.4 | 528.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 527.8 | 488.9 | 500.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 665.7 | 1041 | 642 | 1010 |
| response time (ms), 95th percentile | 2682 | 4095 | 2784 | 4162 |
| response time (ms), 99th percentile | 3704 | 5491 | 3891 | 5867 |
| time over the response line (% of samples) | 26.74 | 33.85 | 26.34 | 33.12 |
| failed requests (%) | 0.007491 | 0.05059 | 0 | 0.1132 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 14.8 | 12.7 | 15.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 56.2 | 57.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.67 | 33.32 | 17.88 | 26.76 |
| utilisation (used / allocatable) | 0.03529 | 0.03686 | 0.03923 | 0.04139 |
| CPU used (cores), mean | 1.694 | 1.769 | 1.683 | 1.846 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01182 | 0.01242 |
| CPU used with Omni's own (cores), mean | 1.694 | 1.769 | 1.695 | 1.858 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.7 | 732.7 | 698.6 | 658 |
| HPA replicas, mean | 4.144 | 4.02 | 4.425 | 4.432 |
| pods started | 0.1 | 0 | 1.5 | 1.4 |
| pod start wait, total (s) | 0.2 | 0 | 2.4 | 2.9 |
| pod start wait, mean (s) | 0.2 | 0 | 1.25 | 1.617 |
| host CPU busy, the real machine under kind (%) | 51.46 | 59.3 | 53.14 | 61.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 885.4 | 1026 | 898.2 | 1058 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.03 | 10.7 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 6.929 | 0.08333 | 18.62 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 55.9 | 0.5 | 105.6 |
| queue: job turnaround, submitted to done, mean (s) | 194.8 | 305.8 | 204.3 | 326.8 |
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
| worker nodes in service, mean | 12 | 11.11 | -7.4% | -2.224 to +0.452 | no |
| node-hours | 5.033 | 4.654 | -7.5% | -0.9383 to +0.1805 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.8 | 528.3 | +0.1% | -1.501 to +2.608 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.8 | 500.4 | -5.2% | -70.01 to +15.28 | no |
| response time (ms), mean | 1041 | 1010 | -3.0% | -169.6 to +106.5 | no |
| response time (ms), 95th percentile | 4095 | 4162 | +1.6% | -491 to +624.3 | no |
| response time (ms), 99th percentile | 5491 | 5867 | +6.9% | -421.7 to +1175 | no |
| time over the response line (% of samples) | 33.85 | 33.12 | -2.1% | -1.992 to +0.539 | no |
| failed requests (%) | 0.05059 | 0.1132 | +123.7% | -0.1028 to +0.228 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 15.7 | +6.1% | +0.1128 to +1.687 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.4 | +57.4 (native is 0) | +34.35 to +80.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.32 | 26.76 | -19.7% | -25.49 to +12.37 | no |
| utilisation (used / allocatable) | 0.03686 | 0.04139 | +12.3% | +0.0009865 to +0.008085 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.769 | 1.846 | +4.4% | +0.01672 to +0.1372 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01242 | +0.0124 (native is 0) | +0.01188 to +0.01296 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.858 | +5.1% | +0.02877 to +0.15 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.7 | 658 | -10.2% | -138.5 to -10.99 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.02 | 4.432 | +10.2% | +0.08842 to +0.7342 | yes: power given |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.7089 to +2.091 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +1.101 to +4.699 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.617 | +1.62 (native is 0) | +0.8358 to +2.398 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.3 | 61.58 | +3.8% | +1.684 to +2.88 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1026 | 1058 | +3.0% | +10.4 to +51.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.7 | -10.8% | -3.268 to +0.6676 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 6.929 | 18.62 | +168.7% | -3.414 to +26.8 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 55.9 | 105.6 | +88.9% | -17.97 to +117.4 | no |
| queue: job turnaround, submitted to done, mean (s) | 305.8 | 326.8 | +6.9% | -15.25 to +57.25 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -2.72e-15 to +5.562e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.033 | 5.033 | +0.0% | -0.01578 to +0.01578 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 527.8 | +0.2% | -0.5914 to +2.671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 527.8 | +0.2% | -0.5914 to +2.671 | no |
| response time (ms), mean | 665.7 | 1041 | +56.4% | +210.5 to +540.5 | yes: LOSS |
| response time (ms), 95th percentile | 2682 | 4095 | +52.7% | +756.2 to +2071 | yes: LOSS |
| response time (ms), 99th percentile | 3704 | 5491 | +48.2% | +1018 to +2555 | yes: LOSS |
| time over the response line (% of samples) | 26.74 | 33.85 | +26.6% | +3.269 to +10.95 | yes: LOSS |
| failed requests (%) | 0.007491 | 0.05059 | +575.3% | -0.0219 to +0.1081 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 14.8 | +19.4% | +1.323 to +3.477 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.67 | 33.32 | +112.7% | -8.058 to +43.37 | no |
| utilisation (used / allocatable) | 0.03529 | 0.03686 | +4.4% | -0.0002402 to +0.003364 | no |
| CPU used (cores), mean | 1.694 | 1.769 | +4.4% | -0.01153 to +0.1615 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.694 | 1.769 | +4.4% | -0.01153 to +0.1615 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.7 | 732.7 | -3.9% | -58.08 to -1.848 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.144 | 4.02 | -3.0% | -0.3978 to +0.1513 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 51.46 | 59.3 | +15.2% | +5.434 to +10.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 885.4 | 1026 | +15.9% | +82.43 to +199.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 6.929 | +5839.3% | +0.4006 to +13.22 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 55.9 | +6887.5% | -1.737 to +111.9 | no |
| queue: job turnaround, submitted to done, mean (s) | 194.8 | 305.8 | +57.0% | +59.9 to +162 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.81 | -9.9% | -2.711 to +0.3241 | no |
| node-hours | 5.033 | 4.53 | -10.0% | -1.143 to +0.1365 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 526.4 | -0.1% | -1.561 to +0.9608 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 488.9 | -7.2% | -85.77 to +10.2 | no |
| response time (ms), mean | 665.7 | 642 | -3.6% | -53.12 to +5.806 | no |
| response time (ms), 95th percentile | 2682 | 2784 | +3.8% | -112.4 to +317 | no |
| response time (ms), 99th percentile | 3704 | 3891 | +5.1% | -111.2 to +485.5 | no |
| time over the response line (% of samples) | 26.74 | 26.34 | -1.5% | -1.008 to +0.2165 | no |
| failed requests (%) | 0.007491 | 0 | -100.0% | -0.02443 to +0.009453 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 12.7 | +2.4% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.2 | +56.2 (native is 0) | +28.28 to +84.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.67 | 17.88 | +14.1% | -4.469 to +8.896 | no |
| utilisation (used / allocatable) | 0.03529 | 0.03923 | +11.1% | -0.001297 to +0.009165 | no |
| CPU used (cores), mean | 1.694 | 1.683 | -0.7% | -0.06374 to +0.04148 | no |
| Omni's own CPU (cores), mean | 0 | 0.01182 | +0.0118 (native is 0) | +0.01146 to +0.01218 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.694 | 1.695 | +0.0% | -0.05179 to +0.05316 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.7 | 698.6 | -8.4% | -153.2 to +25.05 | no |
| HPA replicas, mean | 4.144 | 4.425 | +6.8% | -0.2096 to +0.7718 | no |
| pods started | 0.1 | 1.5 | +1400.0% | +0.5604 to +2.24 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.4 | +1100.0% | +0.4872 to +3.913 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | +0.1045 to +1.996 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.46 | 53.14 | +3.3% | +1.061 to +2.295 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 885.4 | 898.2 | +1.4% | +2.288 to +23.31 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.03 | -16.4% | -4.279 to +0.3387 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.08333 | -28.6% | -0.0836 to +0.01693 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.5 | -37.5% | -0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 194.8 | 204.3 | +4.9% | -0.3148 to +19.36 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.81 | -9.9% | -2.711 to +0.3241 | no |
| node-hours | 5.033 | 4.53 | -10.0% | -1.144 to +0.1375 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.8 | 526.4 | -0.3% | -3.272 to +0.5928 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.8 | 488.9 | -7.4% | -86.78 to +9.132 | no |
| response time (ms), mean | 1041 | 642 | -38.3% | -560.9 to -237.5 | yes: GAIN |
| response time (ms), 95th percentile | 4095 | 2784 | -32.0% | -1938 to -684.1 | yes: GAIN |
| response time (ms), 99th percentile | 5491 | 3891 | -29.1% | -2334 to -865.4 | yes: GAIN |
| time over the response line (% of samples) | 33.85 | 26.34 | -22.2% | -11.15 to -3.864 | yes: GAIN |
| failed requests (%) | 0.05059 | 0 | -100.0% | -0.1278 to +0.02663 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 12.7 | -14.2% | -3.02 to -1.18 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.2 | +56.2 (native is 0) | +28.28 to +84.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.32 | 17.88 | -46.3% | -42.72 to +11.84 | no |
| utilisation (used / allocatable) | 0.03686 | 0.03923 | +6.4% | -0.003515 to +0.008258 | no |
| CPU used (cores), mean | 1.769 | 1.683 | -4.9% | -0.1936 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.01182 | +0.0118 (native is 0) | +0.01146 to +0.01218 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.695 | -4.2% | -0.1819 to +0.03327 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.7 | 698.6 | -4.7% | -129.2 to +61.03 | no |
| HPA replicas, mean | 4.02 | 4.425 | +10.1% | +0.06552 to +0.7432 | yes: power given |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.8048 to +2.195 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.4 (native is 0) | +0.9225 to +3.878 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.25 | +1.25 (native is 0) | +0.6136 to +1.886 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.3 | 53.14 | -10.4% | -8.291 to -4.024 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1026 | 898.2 | -12.5% | -180.4 to -76.24 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.03 | -16.4% | -4.279 to +0.3387 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 6.929 | 0.08333 | -98.8% | -13.27 to -0.4223 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 55.9 | 0.5 | -99.1% | -112.2 to +1.412 | no |
| queue: job turnaround, submitted to done, mean (s) | 305.8 | 204.3 | -33.2% | -145 to -57.91 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.11 | -7.4% | -2.224 to +0.452 | no |
| node-hours | 5.033 | 4.654 | -7.5% | -0.9378 to +0.18 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 528.3 | +0.3% | -0.4154 to +3.602 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 500.4 | -5.0% | -69.08 to +16.42 | no |
| response time (ms), mean | 665.7 | 1010 | +51.7% | +155.3 to +532.6 | yes: LOSS |
| response time (ms), 95th percentile | 2682 | 4162 | +55.2% | +600 to +2360 | yes: LOSS |
| response time (ms), 99th percentile | 3704 | 5867 | +58.4% | +959.3 to +3367 | yes: LOSS |
| time over the response line (% of samples) | 26.74 | 33.12 | +23.9% | +2.999 to +9.768 | yes: LOSS |
| failed requests (%) | 0.007491 | 0.1132 | +1410.9% | -0.0364 to +0.2478 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 15.7 | +26.6% | +2.542 to +4.058 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.4 | +57.4 (native is 0) | +34.35 to +80.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.67 | 26.76 | +70.8% | +2.097 to +20.09 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03529 | 0.04139 | +17.3% | +0.002719 to +0.009477 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.694 | 1.846 | +9.0% | +0.06491 to +0.239 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01242 | +0.0124 (native is 0) | +0.01188 to +0.01296 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.694 | 1.858 | +9.7% | +0.07703 to +0.2517 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.7 | 658 | -13.7% | -168.9 to -40.51 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.144 | 4.432 | +7.0% | -0.1522 to +0.7283 | no |
| pods started | 0.1 | 1.4 | +1300.0% | +0.4706 to +2.129 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.9 | +1350.0% | +0.6754 to +4.725 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.617 | +708.3% | +0.3295 to +2.504 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.46 | 61.58 | +19.7% | +7.591 to +12.64 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 885.4 | 1058 | +19.4% | +101.8 to +242.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.7 | -10.8% | -3.268 to +0.6676 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 18.62 | +15860.7% | +1.688 to +35.32 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 105.6 | +13100.0% | +9.924 to +199.7 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 194.8 | 326.8 | +67.7% | +74 to +189.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*