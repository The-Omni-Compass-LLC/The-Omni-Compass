# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.51 | 10.94 |
| node-hours | 5.035 | 5.022 | 4.402 | 4.588 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 525 | 525.7 | 526.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 525 | 478.8 | 493.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 574.4 | 691.8 | 545.9 | 764.6 |
| response time (ms), 95th percentile | 2260 | 3140 | 2366 | 3665 |
| response time (ms), 99th percentile | 3117 | 4602 | 3349 | 5114 |
| time over the response line (% of samples) | 22.45 | 23.99 | 22.16 | 25.28 |
| failed requests (%) | 0 | 0.0524 | 0 | 0.1452 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 13.8 | 12.3 | 15.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 64.7 | 44.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.65 | 32.71 | 14.12 | 36.67 |
| utilisation (used / allocatable) | 0.03445 | 0.03433 | 0.0396 | 0.03851 |
| CPU used (cores), mean | 1.654 | 1.648 | 1.649 | 1.677 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01306 | 0.00974 |
| CPU used with Omni's own (cores), mean | 1.654 | 1.648 | 1.662 | 1.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.1 | 776 | 699.8 | 708 |
| HPA replicas, mean | 4.013 | 4.08 | 4.279 | 4.424 |
| pods started | 0 | 0.5 | 0.8 | 1.1 |
| pod start wait, total (s) | 0 | 1.1 | 1.2 | 1.9 |
| pod start wait, mean (s) | 0 | 0.65 | 0.95 | 1.033 |
| host CPU busy, the real machine under kind (%) | 50.3 | 56.34 | 52.03 | 59.04 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 856.4 | 952.2 | 866.9 | 991 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.496 | 10.07 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1.867 | 0.1083 | 3.271 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.5 | 0.8 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 167.6 | 261.5 | 171.2 | 298.5 |
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
| worker nodes in service, mean | 12 | 10.94 | -8.8% | -2.316 to +0.2043 | no |
| node-hours | 5.022 | 4.588 | -8.6% | -0.9592 to +0.09202 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 526.7 | +0.3% | -0.2193 to +3.647 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 493.4 | -6.0% | -71.08 to +7.918 | no |
| response time (ms), mean | 691.8 | 764.6 | +10.5% | -3.4 to +149.2 | no |
| response time (ms), 95th percentile | 3140 | 3665 | +16.7% | +51.05 to +998.1 | yes: LOSS |
| response time (ms), 99th percentile | 4602 | 5114 | +11.1% | +57.46 to +965.3 | yes: LOSS |
| time over the response line (% of samples) | 23.99 | 25.28 | +5.4% | +0.4104 to +2.182 | yes: LOSS |
| failed requests (%) | 0.0524 | 0.1452 | +177.2% | -0.03086 to +0.2166 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 15.2 | +10.1% | +0.4952 to +2.305 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 | +44.3 (native is 0) | +31.46 to +57.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.71 | 36.67 | +12.1% | -18.91 to +26.83 | no |
| utilisation (used / allocatable) | 0.03433 | 0.03851 | +12.2% | -0.0001685 to +0.008522 | no |
| CPU used (cores), mean | 1.648 | 1.677 | +1.8% | -0.06355 to +0.1216 | no |
| Omni's own CPU (cores), mean | 0 | 0.00974 | +0.00974 (native is 0) | +0.008487 to +0.01099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.648 | 1.687 | +2.4% | -0.05411 to +0.1316 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776 | 708 | -8.8% | -140.5 to +4.455 | no |
| HPA replicas, mean | 4.08 | 4.424 | +8.4% | -0.1255 to +0.8139 | no |
| pods started | 0.5 | 1.1 | +120.0% | -0.6251 to +1.825 | no |
| pod start wait, total (s) | 1.1 | 1.9 | +72.7% | -1.603 to +3.203 | no |
| pod start wait, mean (s) | 0.65 | 1.033 | +59.0% | -0.7862 to +1.553 | no |
| host CPU busy, the real machine under kind (%) | 56.34 | 59.04 | +4.8% | +1.797 to +3.602 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 952.2 | 991 | +4.1% | +17.41 to +60.19 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.07 | -16.1% | -4.072 to +0.2078 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.867 | 3.271 | +75.2% | -1.7 to +4.509 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.7 | +13.3% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 261.5 | 298.5 | +14.2% | +15.86 to +58.15 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -7.388e-15 to +2.827e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.035 | 5.022 | -0.3% | -0.03225 to +0.006254 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 525 | -0.3% | -2.997 to +0.352 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 525 | -0.3% | -2.997 to +0.352 | no |
| response time (ms), mean | 574.4 | 691.8 | +20.4% | +62.29 to +172.5 | yes: LOSS |
| response time (ms), 95th percentile | 2260 | 3140 | +38.9% | +415 to +1345 | yes: LOSS |
| response time (ms), 99th percentile | 3117 | 4602 | +47.7% | +782.1 to +2189 | yes: LOSS |
| time over the response line (% of samples) | 22.45 | 23.99 | +6.9% | -1.386 to +4.462 | no |
| failed requests (%) | 0 | 0.0524 | +0.0524 (native is 0) | -0.03554 to +0.1403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 13.8 | +22.1% | +1.369 to +3.631 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.65 | 32.71 | +139.6% | -5.212 to +43.34 | no |
| utilisation (used / allocatable) | 0.03445 | 0.03433 | -0.3% | -0.002779 to +0.002542 | no |
| CPU used (cores), mean | 1.654 | 1.648 | -0.3% | -0.1334 to +0.122 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.654 | 1.648 | -0.3% | -0.1334 to +0.122 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.1 | 776 | -0.1% | -47.74 to +45.7 | no |
| HPA replicas, mean | 4.013 | 4.08 | +1.7% | -0.2165 to +0.3503 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | -0.2676 to +2.468 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.65 (native is 0) | -0.1049 to +1.405 | no |
| host CPU busy, the real machine under kind (%) | 50.3 | 56.34 | +12.0% | +5.006 to +7.083 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.4 | 952.2 | +11.2% | +52.6 to +139 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1.867 | +1692.0% | -1.316 to +4.841 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.5 | +150.0% | +0.1887 to +1.611 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 167.6 | 261.5 | +56.1% | +51.2 to +136.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.51 | -12.4% | -2.978 to +0.001036 | no |
| node-hours | 5.035 | 4.402 | -12.6% | -1.253 to -0.01288 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 525.7 | -0.1% | -2.099 to +0.8859 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 478.8 | -9.0% | -93.96 to -0.922 | yes: GAIN |
| response time (ms), mean | 574.4 | 545.9 | -5.0% | -51.9 to -5.014 | yes: GAIN |
| response time (ms), 95th percentile | 2260 | 2366 | +4.6% | -80.83 to +291 | no |
| response time (ms), 99th percentile | 3117 | 3349 | +7.4% | -11.52 to +475.7 | no |
| time over the response line (% of samples) | 22.45 | 22.16 | -1.3% | -2.232 to +1.659 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 12.3 | +8.8% | -0.306 to +2.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.7 | +64.7 (native is 0) | +36.32 to +93.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.65 | 14.13 | +3.5% | -1.445 to +2.391 | no |
| utilisation (used / allocatable) | 0.03445 | 0.0396 | +15.0% | +0.0001822 to +0.01012 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.654 | 1.649 | -0.3% | -0.04528 to +0.03583 | no |
| Omni's own CPU (cores), mean | 0 | 0.01306 | +0.0131 (native is 0) | +0.01216 to +0.01396 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.654 | 1.662 | +0.5% | -0.03276 to +0.04943 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.1 | 699.8 | -9.9% | -148.3 to -6.212 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.013 | 4.279 | +6.6% | +0.02732 to +0.5036 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.2358 to +1.364 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | +0.3879 to +2.012 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.95 | +0.95 (native is 0) | +0.3091 to +1.591 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.3 | 52.03 | +3.4% | +1.215 to +2.248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.4 | 866.9 | +1.2% | -0.8464 to +21.85 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.496 | -20.9% | -4.749 to -0.2591 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1083 | +4.0% | -0.0609 to +0.06924 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 167.6 | 171.2 | +2.2% | -2.886 to +10.13 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.51 | -12.4% | -2.978 to +0.001036 | no |
| node-hours | 5.022 | 4.402 | -12.3% | -1.242 to +0.002805 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 525.7 | +0.1% | -0.8383 to +2.27 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 478.8 | -8.8% | -93.15 to +0.9124 | no |
| response time (ms), mean | 691.8 | 545.9 | -21.1% | -211.2 to -80.51 | yes: GAIN |
| response time (ms), 95th percentile | 3140 | 2366 | -24.7% | -1310 to -239.1 | yes: GAIN |
| response time (ms), 99th percentile | 4602 | 3349 | -27.2% | -1950 to -556.2 | yes: GAIN |
| time over the response line (% of samples) | 23.99 | 22.16 | -7.6% | -3.629 to -0.02124 | yes: GAIN |
| failed requests (%) | 0.0524 | 0 | -100.0% | -0.1403 to +0.03554 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 12.3 | -10.9% | -2.343 to -0.657 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.7 | +64.7 (native is 0) | +36.32 to +93.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.71 | 14.13 | -56.8% | -42.65 to +5.47 | no |
| utilisation (used / allocatable) | 0.03433 | 0.0396 | +15.3% | -0.0001966 to +0.01073 | no |
| CPU used (cores), mean | 1.648 | 1.649 | +0.1% | -0.1374 to +0.1393 | no |
| Omni's own CPU (cores), mean | 0 | 0.01306 | +0.0131 (native is 0) | +0.01216 to +0.01396 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.648 | 1.662 | +0.9% | -0.1245 to +0.1525 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776 | 699.8 | -9.8% | -157.7 to +5.283 | no |
| HPA replicas, mean | 4.08 | 4.279 | +4.9% | -0.1595 to +0.5566 | no |
| pods started | 0.5 | 0.8 | +60.0% | -0.7144 to +1.314 | no |
| pod start wait, total (s) | 1.1 | 1.2 | +9.1% | -1.791 to +1.991 | no |
| pod start wait, mean (s) | 0.65 | 0.95 | +46.2% | -0.8081 to +1.408 | no |
| host CPU busy, the real machine under kind (%) | 56.34 | 52.03 | -7.7% | -5.414 to -3.213 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 952.2 | 866.9 | -9.0% | -123 to -47.58 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.496 | -20.9% | -4.749 to -0.2591 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.867 | 0.1083 | -94.2% | -4.88 to +1.364 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | -46.7% | -1.458 to +0.05776 | no |
| queue: job turnaround, submitted to done, mean (s) | 261.5 | 171.2 | -34.5% | -131.3 to -49.36 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | -8.8% | -2.316 to +0.2043 | no |
| node-hours | 5.035 | 4.588 | -8.9% | -0.9669 to +0.07364 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 526.7 | +0.1% | -2.263 to +3.046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 493.4 | -6.3% | -71.62 to +5.814 | no |
| response time (ms), mean | 574.4 | 764.6 | +33.1% | +80.13 to +300.4 | yes: LOSS |
| response time (ms), 95th percentile | 2260 | 3665 | +62.1% | +610 to +2199 | yes: LOSS |
| response time (ms), 99th percentile | 3117 | 5114 | +64.1% | +950 to +3044 | yes: LOSS |
| time over the response line (% of samples) | 22.45 | 25.28 | +12.6% | +0.06129 to +5.608 | yes: LOSS |
| failed requests (%) | 0 | 0.1452 | +0.145 (native is 0) | -0.008503 to +0.299 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 15.2 | +34.5% | +2.375 to +5.425 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 | +44.3 (native is 0) | +31.46 to +57.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.65 | 36.67 | +168.6% | -9.077 to +55.12 | no |
| utilisation (used / allocatable) | 0.03445 | 0.03851 | +11.8% | -0.0008164 to +0.008933 | no |
| CPU used (cores), mean | 1.654 | 1.677 | +1.4% | -0.1068 to +0.1535 | no |
| Omni's own CPU (cores), mean | 0 | 0.00974 | +0.00974 (native is 0) | +0.008487 to +0.01099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.654 | 1.687 | +2.0% | -0.09687 to +0.163 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.1 | 708 | -8.9% | -148.7 to +10.58 | no |
| HPA replicas, mean | 4.013 | 4.424 | +10.2% | +0.0255 to +0.7966 | yes: power given |
| pods started | 0 | 1.1 | +1.1 (native is 0) | +0.3128 to +1.887 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.9 (native is 0) | +0.4914 to +3.309 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.033 | +1.03 (native is 0) | +0.3341 to +1.733 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.3 | 59.04 | +17.4% | +6.919 to +10.57 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.4 | 991 | +15.7% | +72.46 to +196.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.07 | -16.1% | -4.072 to +0.2078 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 3.271 | +3040.0% | -1.093 to +7.426 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.7 | +183.3% | +0.3128 to +1.887 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 167.6 | 298.5 | +78.2% | +71.3 to +190.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*