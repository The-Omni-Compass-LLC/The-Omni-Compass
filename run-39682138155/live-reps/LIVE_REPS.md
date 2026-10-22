# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.971 | 6 |
| node-hours | 2.514 | 2.512 | 2.086 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 285.6 | 272.6 | 285.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 285.6 | 240.3 | 285.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 319.1 | 633.1 | 289.4 | 640.1 |
| response time (ms), 95th percentile | 1044 | 1319 | 1107 | 1363 |
| response time (ms), 99th percentile | 1525 | 1738 | 1557 | 1847 |
| time over the response line (% of samples) | 16.92 | 55.61 | 16.83 | 56.1 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.1 | 8.4 | 24.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38.4 | 20.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.44 | 2.445 | 11.37 | 2.462 |
| utilisation (used / allocatable) | 0.05983 | 0.096 | 0.07268 | 0.09631 |
| CPU used (cores), mean | 1.436 | 2.304 | 1.421 | 2.311 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01698 | 0.00886 |
| CPU used with Omni's own (cores), mean | 1.436 | 2.304 | 1.438 | 2.32 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.2 | 296.8 | 403.6 | 295.8 |
| HPA replicas, mean | 1.998 | 2.006 | 2.174 | 2.623 |
| pods started | 0 | 0.2 | 0.6 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 | 1.7 | 0.6 |
| pod start wait, mean (s) | 0 | 0.3 | 1.35 | 0.6 |
| host CPU busy, the real machine under kind (%) | 40.68 | 74.3 | 41.55 | 74.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 768 | 1452 | 770.8 | 1454 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.185 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 673.1 | 0.06667 | 651.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1159 | 0.4 | 1148 |
| queue: job turnaround, submitted to done, mean (s) | 76.17 | 946.3 | 79.25 | 951 |
| queue: jobs unfinished at the window's end | 0 | 14.5 | 0 | 14.3 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.738e-15 to -2.164e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.509 | -0.1% | -0.00994 to +0.005273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.6 | 285.4 | -0.1% | -1.073 to +0.6835 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.6 | 285.4 | -0.1% | -1.073 to +0.6835 | no |
| response time (ms), mean | 633.1 | 640.1 | +1.1% | -24.05 to +37.93 | no |
| response time (ms), 95th percentile | 1319 | 1363 | +3.3% | -43.82 to +131.4 | no |
| response time (ms), 99th percentile | 1738 | 1847 | +6.2% | +33.63 to +183.2 | yes: LOSS |
| time over the response line (% of samples) | 55.61 | 56.1 | +0.9% | -3.099 to +4.073 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 24.1 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.4 | +20.4 (native is 0) | +15.22 to +25.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.445 | 2.462 | +0.7% | -0.05464 to +0.08798 | no |
| utilisation (used / allocatable) | 0.096 | 0.09631 | +0.3% | -0.0006095 to +0.001226 | no |
| CPU used (cores), mean | 2.304 | 2.311 | +0.3% | -0.01463 to +0.02943 | no |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.00886 (native is 0) | +0.008005 to +0.009715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.304 | 2.32 | +0.7% | -0.005605 to +0.03813 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.8 | 295.8 | -0.3% | -3.772 to +1.865 | no |
| HPA replicas, mean | 2.006 | 2.623 | +30.8% | +0.3934 to +0.8415 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 74.3 | 74.75 | +0.6% | -0.2116 to +1.106 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1452 | 1454 | +0.2% | -9.703 to +14.5 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 673.1 | 651.7 | -3.2% | -96.06 to +53.33 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1159 | 1148 | -1.0% | -52.79 to +29.63 | no |
| queue: job turnaround, submitted to done, mean (s) | 946.3 | 951 | +0.5% | -28.29 to +37.64 | no |
| queue: jobs unfinished at the window's end | 14.5 | 14.3 | -1.4% | -1.453 to +1.053 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.34e-15 to +7.409e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.512 | -0.1% | -0.007849 to +0.004515 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 285.6 | +4.9% | +11.31 to +15.44 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 285.6 | +4.9% | +11.31 to +15.44 | yes: power given |
| response time (ms), mean | 319.1 | 633.1 | +98.4% | +250.5 to +377.6 | yes: LOSS |
| response time (ms), 95th percentile | 1044 | 1319 | +26.3% | -132.9 to +682.6 | no |
| response time (ms), 99th percentile | 1525 | 1738 | +14.0% | -437.6 to +864 | no |
| time over the response line (% of samples) | 16.92 | 55.61 | +228.8% | +30.93 to +46.47 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.1 | +190.4% | +11.86 to +19.74 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.44 | 2.445 | -76.6% | -10.72 to -5.271 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05983 | 0.096 | +60.4% | +0.03095 to +0.04139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 2.304 | +60.4% | +0.7428 to +0.9933 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.436 | 2.304 | +60.4% | +0.7428 to +0.9933 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.2 | 296.8 | -35.4% | -198.8 to -126 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.006 | +0.4% | -0.07856 to +0.09328 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 40.68 | 74.3 | +82.6% | +30.41 to +36.83 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768 | 1452 | +89.0% | +609.6 to +758.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 673.1 | +897310.1% | +423.8 to +922.2 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1159 | +231716.4% | +797.9 to +1519 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.17 | 946.3 | +1142.4% | +731.5 to +1009 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.5 | +14.5 (native is 0) | +8.785 to +20.22 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.971 | -17.2% | -1.775 to -0.2837 | yes: GAIN |
| node-hours | 2.514 | 2.086 | -17.0% | -0.7412 to -0.1142 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.6 | +0.1% | -0.2346 to +1.024 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 240.3 | -11.7% | -55.66 to -8.305 | yes: GAIN |
| response time (ms), mean | 319.1 | 289.4 | -9.3% | -40.76 to -18.63 | yes: GAIN |
| response time (ms), 95th percentile | 1044 | 1107 | +6.0% | +14.98 to +110.2 | yes: LOSS |
| response time (ms), 99th percentile | 1525 | 1557 | +2.1% | -46.68 to +111.7 | no |
| time over the response line (% of samples) | 16.92 | 16.83 | -0.5% | -0.5239 to +0.3507 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.4 | +1.2% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.4 | +38.4 (native is 0) | +21.79 to +55.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.44 | 11.37 | +8.9% | -1.914 to +3.77 | no |
| utilisation (used / allocatable) | 0.05983 | 0.07268 | +21.5% | +0.003074 to +0.02261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.421 | -1.0% | -0.03857 to +0.008433 | no |
| Omni's own CPU (cores), mean | 0 | 0.01698 | +0.017 (native is 0) | +0.01544 to +0.01852 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.438 | +0.1% | -0.02199 to +0.02582 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.2 | 403.6 | -12.1% | -96.81 to -14.38 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.174 | +8.8% | -0.1184 to +0.4704 | no |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 0 | 1.7 | +1.7 (native is 0) | +0.01232 to +3.388 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.35 | +1.35 (native is 0) | +0.1813 to +2.519 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.68 | 41.55 | +2.1% | +0.6788 to +1.061 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768 | 770.8 | +0.4% | -0.1933 to +5.793 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.185 | -30.3% | -3.019 to -0.6115 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.06667 | -11.1% | -0.05001 to +0.03335 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.17 | 79.25 | +4.0% | -0.7434 to +6.91 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.971 | -17.2% | -1.775 to -0.2837 | yes: GAIN |
| node-hours | 2.512 | 2.086 | -17.0% | -0.7397 to -0.1123 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.6 | 272.6 | -4.5% | -15.25 to -10.71 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.6 | 240.3 | -15.9% | -70.28 to -20.44 | yes: GAIN |
| response time (ms), mean | 633.1 | 289.4 | -54.3% | -414.3 to -273.2 | yes: GAIN |
| response time (ms), 95th percentile | 1319 | 1107 | -16.1% | -629.2 to +204.6 | no |
| response time (ms), 99th percentile | 1738 | 1557 | -10.4% | -792 to +430.6 | no |
| time over the response line (% of samples) | 55.61 | 16.83 | -69.7% | -46.7 to -30.87 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 8.4 | -65.1% | -19.5 to -11.9 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.4 | +38.4 (native is 0) | +21.79 to +55.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.445 | 11.37 | +365.0% | +4.209 to +13.64 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.096 | 0.07268 | -24.3% | -0.03199 to -0.01466 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.304 | 1.421 | -38.3% | -1.027 to -0.7389 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01698 | +0.017 (native is 0) | +0.01544 to +0.01852 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.304 | 1.438 | -37.6% | -1.011 to -0.7215 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.8 | 403.6 | +36.0% | +84.43 to +129.2 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.006 | 2.174 | +8.4% | -0.06882 to +0.406 | no |
| pods started | 0.2 | 0.6 | +200.0% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | -0.2588 to +3.059 | no |
| pod start wait, mean (s) | 0.3 | 1.35 | +350.0% | -0.0223 to +2.122 | no |
| host CPU busy, the real machine under kind (%) | 74.3 | 41.55 | -44.1% | -35.91 to -29.58 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1452 | 770.8 | -46.9% | -755.3 to -606.9 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.02 | -66.3% | -4.239 to -3.72 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 673.1 | 0.06667 | -100.0% | -922.2 to -423.8 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1159 | 0.4 | -100.0% | -1519 to -798 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 946.3 | 79.25 | -91.6% | -1005 to -729.2 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.5 | 0 | -100.0% | -20.22 to -8.785 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.974e-15 to -5.784e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.51 | -0.2% | -0.01298 to +0.004978 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 285.4 | +4.8% | +10.85 to +15.51 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 285.4 | +4.8% | +10.85 to +15.51 | yes: power given |
| response time (ms), mean | 319.1 | 640.1 | +100.6% | +256.3 to +385.7 | yes: LOSS |
| response time (ms), 95th percentile | 1044 | 1363 | +30.5% | -102 to +739.3 | no |
| response time (ms), 99th percentile | 1525 | 1847 | +21.1% | -354.1 to +997.5 | no |
| time over the response line (% of samples) | 16.92 | 56.1 | +231.7% | +33.42 to +44.95 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 24.1 | +190.4% | +11.86 to +19.74 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.4 | +20.4 (native is 0) | +15.22 to +25.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.44 | 2.462 | -76.4% | -10.73 to -5.231 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05983 | 0.09631 | +61.0% | +0.03129 to +0.04167 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 2.311 | +61.0% | +0.7509 to +1 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.00886 (native is 0) | +0.008005 to +0.009715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 2.32 | +61.6% | +0.7601 to +1.009 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.2 | 295.8 | -35.6% | -200 to -126.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.623 | +31.3% | +0.337 to +0.9126 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 40.68 | 74.75 | +83.7% | +30.92 to +37.21 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768 | 1454 | +89.4% | +611.8 to +760.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 651.7 | +868826.8% | +405.4 to +897.8 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1148 | +229400.6% | +788.7 to +1505 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.17 | 951 | +1148.5% | +725.7 to +1024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.3 | +14.3 (native is 0) | +8.449 to +20.15 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*