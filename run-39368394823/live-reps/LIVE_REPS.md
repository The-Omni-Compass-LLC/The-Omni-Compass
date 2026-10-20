# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.415 | 5.418 |
| node-hours | 2.516 | 2.519 | 2.275 | 2.271 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.9 | 273.6 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.9 | 255.1 | 254.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 346.2 | 368.3 | 303.1 | 327.4 |
| response time (ms), 95th percentile | 1151 | 1266 | 1169 | 1305 |
| response time (ms), 99th percentile | 1720 | 1841 | 1688 | 1946 |
| time over the response line (% of samples) | 20.05 | 20.83 | 18.98 | 19.65 |
| failed requests (%) | 0 | 0 | 0 | 0.009302 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.3 | 10.3 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 39.9 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 10.56 | 9.512 | 11.3 |
| utilisation (used / allocatable) | 0.06052 | 0.06032 | 0.06719 | 0.068 |
| CPU used (cores), mean | 1.453 | 1.448 | 1.455 | 1.469 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01666 | 0.01711 |
| CPU used with Omni's own (cores), mean | 1.453 | 1.448 | 1.471 | 1.486 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 458.1 | 422.1 | 415.5 |
| HPA replicas, mean | 1.979 | 1.98 | 1.961 | 2.095 |
| pods started | 0 | 0.1 | 0.1 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 | 0.3 | 0.3 |
| pod start wait, mean (s) | 0 | 0.4 | 0.3 | 0.3 |
| host CPU busy, the real machine under kind (%) | 41.38 | 42.12 | 42.1 | 43.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772.9 | 781.3 | 775.3 | 785.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.819 | 4.849 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.2 | 0.05417 | 0.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | 0.3 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 81.23 | 88.75 | 83.89 | 92.45 |
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
| worker nodes in service, mean | 6 | 5.418 | -9.7% | -1.057 to -0.1065 | yes: GAIN |
| node-hours | 2.519 | 2.271 | -9.8% | -0.4499 to -0.04579 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.8 | -0.0% | -1.372 to +1.167 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 254.6 | -6.7% | -33.13 to -3.549 | yes: GAIN |
| response time (ms), mean | 368.3 | 327.4 | -11.1% | -60.37 to -21.28 | yes: GAIN |
| response time (ms), 95th percentile | 1266 | 1305 | +3.1% | -95.27 to +173.9 | no |
| response time (ms), 99th percentile | 1841 | 1946 | +5.7% | -68.05 to +277.8 | no |
| time over the response line (% of samples) | 20.83 | 19.65 | -5.6% | -2.21 to -0.143 | yes: GAIN |
| failed requests (%) | 0 | 0.009302 | +0.0093 (native is 0) | -0.01174 to +0.03034 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.6 | +2.9% | -0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +21.64 to +46.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.56 | 11.3 | +7.0% | -0.5869 to +2.064 | no |
| utilisation (used / allocatable) | 0.06032 | 0.068 | +12.7% | +0.0007224 to +0.01465 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.469 | +1.5% | -0.01838 to +0.06059 | no |
| Omni's own CPU (cores), mean | 0 | 0.01711 | +0.0171 (native is 0) | +0.01525 to +0.01897 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.486 | +2.6% | -0.002172 to +0.0786 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 415.5 | -9.3% | -86.1 to +0.9815 | no |
| HPA replicas, mean | 1.98 | 2.095 | +5.8% | -0.02049 to +0.251 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 42.12 | 43.38 | +3.0% | +0.6056 to +1.926 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 781.3 | 785.5 | +0.5% | -0.04924 to +8.449 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.849 | -19.2% | -2.052 to -0.25 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.2 | +0.0% | -0.1264 to +0.1264 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.8 | -20.0% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.75 | 92.45 | +4.2% | -1.971 to +9.379 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.294e-15 to -1.267e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.519 | +0.1% | -0.005461 to +0.01279 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.9 | +0.1% | -1.003 to +1.602 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.9 | +0.1% | -1.003 to +1.602 | no |
| response time (ms), mean | 346.2 | 368.3 | +6.4% | +6.143 to +37.94 | yes: LOSS |
| response time (ms), 95th percentile | 1151 | 1266 | +10.0% | +15.55 to +215.1 | yes: LOSS |
| response time (ms), 99th percentile | 1720 | 1841 | +7.0% | +7.729 to +234 | yes: LOSS |
| time over the response line (% of samples) | 20.05 | 20.83 | +3.9% | -0.145 to +1.712 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.3 | +1.0% | -0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 10.56 | -6.7% | -2.346 to +0.8398 | no |
| utilisation (used / allocatable) | 0.06052 | 0.06032 | -0.3% | -0.001152 to +0.0007328 | no |
| CPU used (cores), mean | 1.453 | 1.448 | -0.3% | -0.02765 to +0.01759 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.453 | 1.448 | -0.3% | -0.02765 to +0.01759 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 458.1 | +0.7% | -6.337 to +12.81 | no |
| HPA replicas, mean | 1.979 | 1.98 | +0.0% | -0.1274 to +0.1294 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| host CPU busy, the real machine under kind (%) | 41.38 | 42.12 | +1.8% | +0.482 to +0.9833 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.9 | 781.3 | +1.1% | +2.676 to +14.12 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.2 | +118.2% | +0.02037 to +0.1963 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | +25.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.23 | 88.75 | +9.3% | +1.637 to +13.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.415 | -9.8% | -0.9611 to -0.2091 | yes: GAIN |
| node-hours | 2.516 | 2.275 | -9.5% | -0.3968 to -0.08351 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 273.6 | +0.3% | +0.04439 to +1.786 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 255.1 | -6.4% | -29.3 to -5.791 | yes: GAIN |
| response time (ms), mean | 346.2 | 303.1 | -12.5% | -53.65 to -32.62 | yes: GAIN |
| response time (ms), 95th percentile | 1151 | 1169 | +1.6% | -57.81 to +94.91 | no |
| response time (ms), 99th percentile | 1720 | 1688 | -1.9% | -139.1 to +75.22 | no |
| time over the response line (% of samples) | 20.05 | 18.98 | -5.3% | -1.687 to -0.449 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.3 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.9 | +39.9 (native is 0) | +29.63 to +50.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 9.512 | -15.9% | -2.822 to -0.7817 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06052 | 0.06719 | +11.0% | +0.003068 to +0.01027 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.455 | +0.1% | -0.01676 to +0.02105 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.0167 (native is 0) | +0.01502 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.471 | +1.3% | +0.000697 to +0.03692 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 422.1 | -7.2% | -53.09 to -12.47 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 1.961 | -0.9% | -0.1282 to +0.09264 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 41.38 | 42.1 | +1.7% | +0.4672 to +0.9555 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.9 | 775.3 | +0.3% | -1.358 to +6.158 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.819 | -19.7% | -1.903 to -0.4582 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.05417 | -40.9% | -0.09091 to +0.01591 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | -62.5% | -0.877 to -0.123 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 81.23 | 83.89 | +3.3% | -0.9711 to +6.296 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.415 | -9.8% | -0.9611 to -0.2091 | yes: GAIN |
| node-hours | 2.519 | 2.275 | -9.7% | -0.3989 to -0.08872 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.6 | +0.2% | -0.4455 to +1.677 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 255.1 | -6.5% | -29.12 to -6.577 | yes: GAIN |
| response time (ms), mean | 368.3 | 303.1 | -17.7% | -84.19 to -46.16 | yes: GAIN |
| response time (ms), 95th percentile | 1266 | 1169 | -7.6% | -173.9 to -19.65 | yes: GAIN |
| response time (ms), 99th percentile | 1841 | 1688 | -8.3% | -323 to +17.32 | no |
| time over the response line (% of samples) | 20.83 | 18.98 | -8.9% | -3.003 to -0.7007 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.3 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.9 | +39.9 (native is 0) | +29.63 to +50.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.56 | 9.512 | -9.9% | -2.604 to +0.5072 | no |
| utilisation (used / allocatable) | 0.06032 | 0.06719 | +11.4% | +0.002682 to +0.01107 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.455 | +0.5% | -0.0127 to +0.02706 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.0167 (native is 0) | +0.01502 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.471 | +1.6% | +0.004374 to +0.04331 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 422.1 | -7.9% | -64.44 to -7.589 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 1.961 | -0.9% | -0.09972 to +0.06222 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0.3 | -25.0% | -1.29 to +1.09 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | -25.0% | -1.29 to +1.09 | no |
| host CPU busy, the real machine under kind (%) | 42.12 | 42.1 | -0.1% | -0.3811 to +0.3385 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 781.3 | 775.3 | -0.8% | -10.66 to -1.34 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.819 | -19.7% | -1.903 to -0.4582 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.05417 | -72.9% | -0.2424 to -0.04926 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.3 | -70.0% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 88.75 | 83.89 | -5.5% | -9.659 to -0.0576 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.418 | -9.7% | -1.057 to -0.1065 | yes: GAIN |
| node-hours | 2.516 | 2.271 | -9.7% | -0.4483 to -0.04005 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.8 | +0.1% | -0.5994 to +0.994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 254.6 | -6.6% | -33.29 to -2.788 | yes: GAIN |
| response time (ms), mean | 346.2 | 327.4 | -5.4% | -33.57 to -3.988 | yes: GAIN |
| response time (ms), 95th percentile | 1151 | 1305 | +13.4% | +39.36 to +269.9 | yes: LOSS |
| response time (ms), 99th percentile | 1720 | 1946 | +13.1% | +70.43 to +381.1 | yes: LOSS |
| time over the response line (% of samples) | 20.05 | 19.65 | -2.0% | -0.9332 to +0.1479 | no |
| failed requests (%) | 0 | 0.009302 | +0.0093 (native is 0) | -0.01174 to +0.03034 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.6 | +3.9% | -0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +21.64 to +46.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 11.3 | -0.1% | -1.69 to +1.66 | no |
| utilisation (used / allocatable) | 0.06052 | 0.068 | +12.3% | +0.00107 to +0.01388 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.469 | +1.1% | -0.007577 to +0.03972 | no |
| Omni's own CPU (cores), mean | 0 | 0.01711 | +0.0171 (native is 0) | +0.01525 to +0.01897 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.486 | +2.3% | +0.008419 to +0.05795 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.8 | 415.5 | -8.6% | -75.37 to -3.274 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.095 | +5.9% | -0.03592 to +0.2684 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 41.38 | 43.38 | +4.8% | +1.276 to +2.721 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.9 | 785.5 | +1.6% | +5.999 to +19.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.849 | -19.2% | -2.052 to -0.25 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.2 | +118.2% | +0.02498 to +0.1917 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.23 | 92.45 | +13.8% | +5.168 to +17.28 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*