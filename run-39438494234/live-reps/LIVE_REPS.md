# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.162 | 5.929 |
| node-hours | 2.514 | 2.518 | 2.16 | 2.483 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 286.3 | 273.3 | 285.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 286.3 | 247.1 | 283.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 405.7 | 692.2 | 376.5 | 677.4 |
| response time (ms), 95th percentile | 1496 | 1432 | 1547 | 1440 |
| response time (ms), 99th percentile | 2030 | 1921 | 2294 | 1917 |
| time over the response line (% of samples) | 19.25 | 61.12 | 18.71 | 59.29 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 24.1 | 9.8 | 23.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.6 | 15.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 2.418 | 13.35 | 2.193 |
| utilisation (used / allocatable) | 0.06335 | 0.09613 | 0.07401 | 0.09741 |
| CPU used (cores), mean | 1.52 | 2.307 | 1.516 | 2.311 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01724 | 0.00909 |
| CPU used with Omni's own (cores), mean | 1.52 | 2.307 | 1.534 | 2.32 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 296.4 | 392.1 | 293.5 |
| HPA replicas, mean | 1.935 | 2.124 | 2.109 | 2.088 |
| pods started | 0 | 0.2 | 0.3 | 0.4 |
| pod start wait, total (s) | 0 | 0.3 | 0.6 | 0.8 |
| pod start wait, mean (s) | 0 | 0.3 | 0.6 | 0.8 |
| host CPU busy, the real machine under kind (%) | 42.95 | 74.73 | 43.93 | 74.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 802.6 | 1456 | 807.7 | 1451 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.478 | 4.106 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 670.7 | 0.09583 | 677.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1145 | 0.6 | 1141 |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 946.3 | 114.2 | 941.7 |
| queue: jobs unfinished at the window's end | 0 | 14.6 | 0 | 14.5 |

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
| worker nodes in service, mean | 6 | 5.929 | -1.2% | -0.1806 to +0.03898 | no |
| node-hours | 2.518 | 2.483 | -1.4% | -0.07915 to +0.01032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.3 | 285.9 | -0.1% | -0.9624 to +0.1642 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.3 | 283.6 | -0.9% | -5.988 to +0.7523 | no |
| response time (ms), mean | 692.2 | 677.4 | -2.1% | -53.68 to +24.07 | no |
| response time (ms), 95th percentile | 1432 | 1440 | +0.5% | -84.28 to +99.94 | no |
| response time (ms), 99th percentile | 1921 | 1917 | -0.2% | -142.1 to +133.3 | no |
| time over the response line (% of samples) | 61.12 | 59.29 | -3.0% | -4.302 to +0.6297 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 23.9 | -0.8% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.6 (native is 0) | +12.13 to +19.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.418 | 2.193 | -9.3% | -0.7505 to +0.3005 | no |
| utilisation (used / allocatable) | 0.09613 | 0.09741 | +1.3% | -0.0003476 to +0.00289 | no |
| CPU used (cores), mean | 2.307 | 2.311 | +0.2% | -0.008136 to +0.0164 | no |
| Omni's own CPU (cores), mean | 0 | 0.00909 | +0.00909 (native is 0) | +0.008394 to +0.009786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.307 | 2.32 | +0.6% | +0.0007144 to +0.02573 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.4 | 293.5 | -1.0% | -6.533 to +0.8128 | no |
| HPA replicas, mean | 2.124 | 2.088 | -1.7% | -0.1714 to +0.1007 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | -0.5796 to +1.58 | no |
| pod start wait, mean (s) | 0.3 | 0.8 | +166.7% | -0.5796 to +1.58 | no |
| host CPU busy, the real machine under kind (%) | 74.73 | 74.9 | +0.2% | -0.1125 to +0.4464 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1456 | 1451 | -0.3% | -11.28 to +2.676 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.106 | -31.6% | -4.514 to +0.7269 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 670.7 | 677.6 | +1.0% | -24.8 to +38.48 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1145 | 1141 | -0.4% | -41.85 to +32.58 | no |
| queue: job turnaround, submitted to done, mean (s) | 946.3 | 941.7 | -0.5% | -20.62 to +11.3 | no |
| queue: jobs unfinished at the window's end | 14.6 | 14.5 | -0.7% | -1.08 to +0.8802 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.747e-15 to -2.732e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.518 | +0.2% | -0.002324 to +0.009991 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 286.3 | +4.6% | +10.1 to +15.24 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 286.3 | +4.6% | +10.1 to +15.24 | yes: power given |
| response time (ms), mean | 405.7 | 692.2 | +70.6% | +202.1 to +371 | yes: LOSS |
| response time (ms), 95th percentile | 1496 | 1432 | -4.3% | -689.2 to +560.6 | no |
| response time (ms), 99th percentile | 2030 | 1921 | -5.4% | -964.6 to +746.1 | no |
| time over the response line (% of samples) | 19.25 | 61.12 | +217.5% | +35.15 to +48.59 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 24.1 | +159.1% | +10.78 to +18.82 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 2.418 | -77.8% | -11.3 to -5.654 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.09613 | +51.7% | +0.02589 to +0.03967 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.52 | 2.307 | +51.7% | +0.6214 to +0.9522 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.52 | 2.307 | +51.7% | +0.6214 to +0.9522 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 296.4 | -32.2% | -182.4 to -99.64 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.935 | 2.124 | +9.8% | +0.04624 to +0.3312 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 42.95 | 74.73 | +74.0% | +28.36 to +35.21 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 802.6 | 1456 | +81.4% | +581.4 to +724.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 670.7 | +1238207.0% | +406.9 to +934.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1145 | +286211.2% | +762.4 to +1527 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 946.3 | +779.3% | +705.6 to +971.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.6 | +14.6 (native is 0) | +8.613 to +20.59 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.162 | -14.0% | -1.519 to -0.1567 | yes: GAIN |
| node-hours | 2.514 | 2.16 | -14.1% | -0.6375 to -0.07084 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.3 | -0.1% | -1.345 to +0.855 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 247.1 | -9.7% | -47.94 to -5.126 | yes: GAIN |
| response time (ms), mean | 405.7 | 376.5 | -7.2% | -40.08 to -18.33 | yes: GAIN |
| response time (ms), 95th percentile | 1496 | 1547 | +3.4% | -9.939 to +111.4 | no |
| response time (ms), 99th percentile | 2030 | 2294 | +13.0% | +96.07 to +430.8 | yes: LOSS |
| time over the response line (% of samples) | 19.25 | 18.71 | -2.8% | -1.503 to +0.4151 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.8 | +5.4% | -0.2726 to +1.273 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 | +46.6 (native is 0) | +33.06 to +60.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 13.35 | +22.5% | +0.4519 to +4.461 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.07401 | +16.8% | +0.002278 to +0.01903 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.52 | 1.516 | -0.3% | -0.03305 to +0.025 | no |
| Omni's own CPU (cores), mean | 0 | 0.01724 | +0.0172 (native is 0) | +0.01631 to +0.01817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.52 | 1.534 | +0.9% | -0.01599 to +0.04241 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 392.1 | -10.4% | -79.62 to -10.97 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.935 | 2.109 | +9.0% | +0.04722 to +0.3015 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 42.95 | 43.93 | +2.3% | +0.5382 to +1.426 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 802.6 | 807.7 | +0.6% | +1.493 to +8.707 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.478 | -25.4% | -2.673 to -0.3714 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.09583 | +76.9% | -0.03529 to +0.1186 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 114.2 | +6.1% | +2.039 to +11.15 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.162 | -14.0% | -1.519 to -0.1567 | yes: GAIN |
| node-hours | 2.518 | 2.16 | -14.2% | -0.6389 to -0.07709 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.3 | 273.3 | -4.5% | -15.43 to -10.4 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.3 | 247.1 | -13.7% | -61.78 to -16.62 | yes: GAIN |
| response time (ms), mean | 692.2 | 376.5 | -45.6% | -398.3 to -233.3 | yes: GAIN |
| response time (ms), 95th percentile | 1432 | 1547 | +8.0% | -508.8 to +738.8 | no |
| response time (ms), 99th percentile | 1921 | 2294 | +19.4% | -592 to +1337 | no |
| time over the response line (% of samples) | 61.12 | 18.71 | -69.4% | -49.22 to -35.61 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 9.8 | -59.3% | -17.85 to -10.75 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.6 | +46.6 (native is 0) | +33.06 to +60.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.418 | 13.35 | +452.2% | +6.621 to +15.25 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09613 | 0.07401 | -23.0% | -0.0305 to -0.01376 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.307 | 1.516 | -34.3% | -0.9736 to -0.608 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01724 | +0.0172 (native is 0) | +0.01631 to +0.01817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.307 | 1.534 | -33.5% | -0.9565 to -0.5906 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.4 | 392.1 | +32.3% | +67.89 to +123.6 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.124 | 2.109 | -0.7% | -0.1587 to +0.13 | no |
| pods started | 0.2 | 0.3 | +50.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | -0.7144 to +1.314 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | -0.7144 to +1.314 | no |
| host CPU busy, the real machine under kind (%) | 74.73 | 43.93 | -41.2% | -34.3 to -27.3 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1456 | 807.7 | -44.5% | -719.9 to -576.1 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.021 | -66.3% | -3.979 to -3.979 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 670.7 | 0.09583 | -100.0% | -934.4 to -406.9 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1145 | 0.6 | -99.9% | -1527 to -762.1 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 946.3 | 114.2 | -87.9% | -962 to -702.2 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.6 | 0 | -100.0% | -20.59 to -8.613 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.929 | -1.2% | -0.1806 to +0.03898 | no |
| node-hours | 2.514 | 2.483 | -1.2% | -0.07615 to +0.01499 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 285.9 | +4.5% | +9.59 to +14.95 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 283.6 | +3.7% | +6.016 to +14.09 | yes: power given |
| response time (ms), mean | 405.7 | 677.4 | +67.0% | +199 to +344.4 | yes: LOSS |
| response time (ms), 95th percentile | 1496 | 1440 | -3.8% | -644.8 to +532 | no |
| response time (ms), 99th percentile | 2030 | 1917 | -5.6% | -942.3 to +715.1 | no |
| time over the response line (% of samples) | 19.25 | 59.29 | +207.9% | +33.29 to +46.78 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 23.9 | +157.0% | +10.74 to +18.46 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.6 (native is 0) | +12.13 to +19.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 2.193 | -79.9% | -11.37 to -6.038 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06335 | 0.09741 | +53.8% | +0.02694 to +0.04117 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.52 | 2.311 | +52.0% | +0.6301 to +0.9517 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00909 | +0.00909 (native is 0) | +0.008394 to +0.009786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.52 | 2.32 | +52.6% | +0.6399 to +0.9601 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 293.5 | -32.9% | -186.6 to -101.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.935 | 2.088 | +7.9% | +0.06988 to +0.2368 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.01208 to +1.612 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | -0.01208 to +1.612 | no |
| host CPU busy, the real machine under kind (%) | 42.95 | 74.9 | +74.4% | +28.47 to +35.43 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 802.6 | 1451 | +80.8% | +574.6 to +723 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.106 | -31.6% | -4.514 to +0.7269 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 677.6 | +1250833.4% | +404.7 to +950.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1141 | +285052.5% | +773.6 to +1507 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 941.7 | +774.9% | +699.3 to +968.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.5 | +14.5 (native is 0) | +8.326 to +20.67 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*