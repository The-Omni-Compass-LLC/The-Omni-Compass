# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.181 | 6 |
| node-hours | 2.518 | 2.515 | 2.173 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 284.9 | 272.7 | 284.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 284.9 | 246.9 | 284.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 335.2 | 626.3 | 307.7 | 602.2 |
| response time (ms), 95th percentile | 1158 | 1331 | 1190 | 1284 |
| response time (ms), 99th percentile | 1658 | 1850 | 1702 | 1811 |
| time over the response line (% of samples) | 17.44 | 54.36 | 17.62 | 52.71 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 23.2 | 8.8 | 23.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.2 | 16.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.32 | 2.04 | 10.93 | 2.425 |
| utilisation (used / allocatable) | 0.05914 | 0.09346 | 0.0692 | 0.09482 |
| CPU used (cores), mean | 1.419 | 2.243 | 1.43 | 2.276 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01628 | 0.0084 |
| CPU used with Omni's own (cores), mean | 1.419 | 2.243 | 1.446 | 2.284 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.9 | 304.7 | 416.1 | 300.4 |
| HPA replicas, mean | 1.952 | 2.092 | 2.178 | 2.485 |
| pods started | 0.1 | 0.5 | 0.6 | 0.2 |
| pod start wait, total (s) | 0.1 | 1.2 | 1.7 | 0.5 |
| pod start wait, mean (s) | 0.1 | 1.2 | 1.233 | 0.5 |
| host CPU busy, the real machine under kind (%) | 40.75 | 72.04 | 41.58 | 73.25 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 779.1 | 1403 | 782.5 | 1423 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.517 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 621.4 | 0.05 | 559 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1017 | 0.4 | 1000 |
| queue: job turnaround, submitted to done, mean (s) | 85.75 | 883.8 | 89.35 | 885.4 |
| queue: jobs unfinished at the window's end | 0 | 13.5 | 0 | 12.2 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.232e-15 to +1.41e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.51 | -0.2% | -0.01053 to +0.001195 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 284.9 | -0.0% | -0.7373 to +0.6827 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 284.9 | -0.0% | -0.7373 to +0.6827 | no |
| response time (ms), mean | 626.3 | 602.2 | -3.9% | -60.78 to +12.48 | no |
| response time (ms), 95th percentile | 1331 | 1284 | -3.6% | -138.5 to +43.83 | no |
| response time (ms), 99th percentile | 1850 | 1811 | -2.1% | -180.2 to +103.1 | no |
| time over the response line (% of samples) | 54.36 | 52.71 | -3.0% | -4.458 to +1.155 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.2 | 23.4 | +0.9% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.6 (native is 0) | +13.92 to +19.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.04 | 2.425 | +18.9% | -0.1018 to +0.8718 | no |
| utilisation (used / allocatable) | 0.09346 | 0.09482 | +1.4% | -0.0001516 to +0.002855 | no |
| CPU used (cores), mean | 2.243 | 2.276 | +1.4% | -0.003638 to +0.06851 | no |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.0084 (native is 0) | +0.007257 to +0.009543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.243 | 2.284 | +1.8% | +0.005479 to +0.0762 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.7 | 300.4 | -1.4% | -9.038 to +0.421 | no |
| HPA replicas, mean | 2.092 | 2.485 | +18.8% | +0.1072 to +0.6792 | yes: power given |
| pods started | 0.5 | 0.2 | -60.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 1.2 | 0.5 | -58.3% | -1.918 to +0.5181 | no |
| pod start wait, mean (s) | 1.2 | 0.5 | -58.3% | -1.918 to +0.5181 | no |
| host CPU busy, the real machine under kind (%) | 72.04 | 73.25 | +1.7% | -0.1931 to +2.607 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1403 | 1423 | +1.5% | -9.172 to +50.57 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 621.4 | 559 | -10.0% | -139.5 to +14.67 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1017 | 1000 | -1.6% | -69.94 to +36.38 | no |
| queue: job turnaround, submitted to done, mean (s) | 883.8 | 885.4 | +0.2% | -34.39 to +37.71 | no |
| queue: jobs unfinished at the window's end | 13.5 | 12.2 | -9.6% | -2.81 to +0.2099 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.902e-15 to -4.728e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.515 | -0.1% | -0.008266 to +0.002266 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 284.9 | +4.6% | +10.48 to +14.42 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 284.9 | +4.6% | +10.48 to +14.42 | yes: power given |
| response time (ms), mean | 335.2 | 626.3 | +86.8% | +212.7 to +369.5 | yes: LOSS |
| response time (ms), 95th percentile | 1158 | 1331 | +15.0% | -210.5 to +557.1 | no |
| response time (ms), 99th percentile | 1658 | 1850 | +11.5% | -397 to +779.6 | no |
| time over the response line (% of samples) | 17.44 | 54.36 | +211.7% | +26.13 to +47.71 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 23.2 | +169.8% | +11.51 to +17.69 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.32 | 2.04 | -80.2% | -9.665 to -6.899 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05914 | 0.09346 | +58.1% | +0.02994 to +0.03872 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 2.243 | +58.1% | +0.7185 to +0.9293 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.419 | 2.243 | +58.1% | +0.7185 to +0.9293 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.9 | 304.7 | -35.3% | -213 to -119.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.092 | +7.1% | +0.02136 to +0.2576 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.1 | 1.2 | +1100.0% | +0.2436 to +1.956 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.2 | +1100.0% | +0.2436 to +1.956 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.75 | 72.04 | +76.8% | +28.6 to +34 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.1 | 1403 | +80.0% | +522.7 to +724.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 621.4 | +745622.5% | +318.8 to +923.9 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1017 | +145162.8% | +569 to +1463 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.75 | 883.8 | +930.6% | +607.8 to +988.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.5 | +13.5 (native is 0) | +6.612 to +20.39 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.181 | -13.7% | -1.505 to -0.133 | yes: GAIN |
| node-hours | 2.518 | 2.173 | -13.7% | -0.6292 to -0.06105 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.7 | +0.1% | -0.5578 to +1.091 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 246.9 | -9.4% | -46.62 to -4.467 | yes: GAIN |
| response time (ms), mean | 335.2 | 307.7 | -8.2% | -42.06 to -13.03 | yes: GAIN |
| response time (ms), 95th percentile | 1158 | 1190 | +2.8% | -46.14 to +111.2 | no |
| response time (ms), 99th percentile | 1658 | 1702 | +2.6% | -47.21 to +135 | no |
| time over the response line (% of samples) | 17.44 | 17.62 | +1.0% | -0.4437 to +0.8018 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.8 | +2.3% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.2 | +46.2 (native is 0) | +23.41 to +68.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.32 | 10.93 | +5.9% | -2.344 to +3.557 | no |
| utilisation (used / allocatable) | 0.05914 | 0.0692 | +17.0% | +0.001989 to +0.01814 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.43 | +0.7% | -0.007704 to +0.02859 | no |
| Omni's own CPU (cores), mean | 0 | 0.01628 | +0.0163 (native is 0) | +0.01482 to +0.01774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.446 | +1.9% | +0.007946 to +0.0455 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.9 | 416.1 | -11.6% | -101.2 to -8.347 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.178 | +11.5% | +0.02991 to +0.4209 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | -0.2726 to +1.273 | no |
| pod start wait, total (s) | 0.1 | 1.7 | +1600.0% | -0.372 to +3.572 | no |
| pod start wait, mean (s) | 0.1 | 1.233 | +1133.3% | -0.3287 to +2.595 | no |
| host CPU busy, the real machine under kind (%) | 40.75 | 41.58 | +2.0% | +0.3505 to +1.317 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.1 | 782.5 | +0.4% | -0.4328 to +7.233 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | -24.7% | -2.656 to -0.31 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.05 | -40.0% | -0.06717 to +0.0005035 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 | -42.9% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.75 | 89.35 | +4.2% | -1.391 to +8.591 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.181 | -13.7% | -1.505 to -0.133 | yes: GAIN |
| node-hours | 2.515 | 2.173 | -13.6% | -0.6289 to -0.05539 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 272.7 | -4.3% | -13.99 to -10.38 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 246.9 | -13.3% | -60.46 to -15.54 | yes: GAIN |
| response time (ms), mean | 626.3 | 307.7 | -50.9% | -405.3 to -232 | yes: GAIN |
| response time (ms), 95th percentile | 1331 | 1190 | -10.6% | -564.2 to +282.6 | no |
| response time (ms), 99th percentile | 1850 | 1702 | -8.0% | -784.6 to +489.7 | no |
| time over the response line (% of samples) | 54.36 | 17.62 | -67.6% | -47.36 to -26.13 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.2 | 8.8 | -62.1% | -17.46 to -11.34 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.2 | +46.2 (native is 0) | +23.41 to +68.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.04 | 10.93 | +435.7% | +5.502 to +12.27 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09346 | 0.0692 | -26.0% | -0.03104 to -0.01749 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.243 | 1.43 | -36.3% | -0.9262 to -0.7006 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01628 | +0.0163 (native is 0) | +0.01482 to +0.01774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.243 | 1.446 | -35.5% | -0.9101 to -0.6842 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.7 | 416.1 | +36.6% | +91.76 to +131.1 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.092 | 2.178 | +4.1% | -0.07803 to +0.2499 | no |
| pods started | 0.5 | 0.6 | +20.0% | -0.6872 to +0.8872 | no |
| pod start wait, total (s) | 1.2 | 1.7 | +41.7% | -1.613 to +2.613 | no |
| pod start wait, mean (s) | 1.2 | 1.233 | +2.8% | -1.895 to +1.962 | no |
| host CPU busy, the real machine under kind (%) | 72.04 | 41.58 | -42.3% | -33.12 to -27.81 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1403 | 782.5 | -44.2% | -720.4 to -520 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.401 | -60.0% | -5.194 to -2.003 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 621.4 | 0.05 | -100.0% | -924 to -318.8 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1017 | 0.4 | -100.0% | -1464 to -569.2 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 883.8 | 89.35 | -89.9% | -983.5 to -605.3 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.5 | 0 | -100.0% | -20.39 to -6.612 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.997e-15 to -2.004e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.51 | -0.3% | -0.01244 to -0.002891 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 284.9 | +4.6% | +10.44 to +14.41 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 284.9 | +4.6% | +10.44 to +14.41 | yes: power given |
| response time (ms), mean | 335.2 | 602.2 | +79.6% | +193.6 to +340.3 | yes: LOSS |
| response time (ms), 95th percentile | 1158 | 1284 | +10.9% | -301 to +552.9 | no |
| response time (ms), 99th percentile | 1658 | 1811 | +9.2% | -512.4 to +818 | no |
| time over the response line (% of samples) | 17.44 | 52.71 | +202.2% | +26.7 to +43.84 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 23.4 | +172.1% | +11.52 to +18.08 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.6 (native is 0) | +13.92 to +19.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.32 | 2.425 | -76.5% | -9.603 to -6.191 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05914 | 0.09482 | +60.3% | +0.0308 to +0.04056 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 2.276 | +60.3% | +0.7393 to +0.9733 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.0084 (native is 0) | +0.007257 to +0.009543 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 2.284 | +60.9% | +0.7485 to +0.9809 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.9 | 300.4 | -36.2% | -220.2 to -120.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.485 | +27.3% | +0.2702 to +0.7951 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | -0.5656 to +1.366 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | -0.5656 to +1.366 | no |
| host CPU busy, the real machine under kind (%) | 40.75 | 73.25 | +79.8% | +30.12 to +34.89 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.1 | 1423 | +82.7% | +563.7 to +724.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 559 | +670753.1% | +291.4 to +826.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1000 | +142766.1% | +578.6 to +1420 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.75 | 885.4 | +932.5% | +637.4 to +961.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.2 | +12.2 (native is 0) | +5.948 to +18.45 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*