# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.949 | 5.923 |
| node-hours | 2.512 | 2.516 | 2.076 | 2.485 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 271.1 | 269.5 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 271.1 | 236.5 | 269 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 189.9 | 109.6 | 171.8 | 88.44 |
| response time (ms), 95th percentile | 553.6 | 189.1 | 619.9 | 190.5 |
| response time (ms), 99th percentile | 821.8 | 268.6 | 925.1 | 269.8 |
| time over the response line (% of samples) | 7.527 | 0.04633 | 8.179 | 0.08367 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 0 | 5.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 171.8 | 25.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.585 | 804.9 | 8.482 | 877.8 |
| utilisation (used / allocatable) | 0.05196 | 0.05715 | 0.06253 | 0.0581 |
| CPU used (cores), mean | 1.247 | 1.372 | 1.229 | 1.377 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04254 | 0.04071 |
| CPU used with Omni's own (cores), mean | 1.247 | 1.372 | 1.271 | 1.418 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 525.4 | 473.3 | 462.1 | 467 |
| HPA replicas, mean | 1.85 | 2.007 | 2.432 | 1.937 |
| pods started | 0 | 0.3 | 0.8 | 0 |
| pod start wait, total (s) | 0 | 0.4 | 1.6 | 0 |
| pod start wait, mean (s) | 0 | 0.3 | 0.6 | 0 |
| host CPU busy, the real machine under kind (%) | 35.33 | 41.66 | 37.16 | 42.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 731 | 1334 | 734.9 | 1380 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.97 | 5.243 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 116.2 | 0.0375 | 108.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 520.7 | 0.3 | 487.4 |
| queue: job turnaround, submitted to done, mean (s) | 38.37 | 617 | 42.89 | 671.5 |
| queue: jobs unfinished at the window's end | 0 | 4.9 | 0 | 5.4 |

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
| worker nodes in service, mean | 6 | 5.923 | -1.3% | -0.1628 to +0.007823 | no |
| node-hours | 2.516 | 2.485 | -1.2% | -0.06713 to +0.005516 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.4 | +0.1% | -0.4654 to +1.132 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 269 | -0.8% | -4.816 to +0.6117 | no |
| response time (ms), mean | 109.6 | 88.44 | -19.3% | -28.9 to -13.36 | yes: GAIN |
| response time (ms), 95th percentile | 189.1 | 190.5 | +0.7% | -12.94 to +15.67 | no |
| response time (ms), 99th percentile | 268.6 | 269.8 | +0.4% | -15.54 to +17.9 | no |
| time over the response line (% of samples) | 0.04633 | 0.08367 | +80.6% | -0.02102 to +0.09569 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.4 | +25.4 (native is 0) | +13.21 to +37.59 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 804.9 | 877.8 | +9.1% | +8.645 to +137.2 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05715 | 0.0581 | +1.7% | +3.376e-05 to +0.001873 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.377 | +0.4% | -0.01105 to +0.02285 | no |
| Omni's own CPU (cores), mean | 0 | 0.04071 | +0.0407 (native is 0) | +0.03515 to +0.04627 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.418 | +3.4% | +0.03147 to +0.06174 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.3 | 467 | -1.3% | -12.58 to +0.05625 | no |
| HPA replicas, mean | 2.007 | 1.937 | -3.5% | -0.145 to +0.00373 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| host CPU busy, the real machine under kind (%) | 41.66 | 42.97 | +3.1% | +0.7446 to +1.879 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1334 | 1380 | +3.5% | +0.6036 to +92 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.243 | -12.6% | -1.474 to -0.03976 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 116.2 | 108.7 | -6.5% | -29.46 to +14.41 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 520.7 | 487.4 | -6.4% | -146.5 to +79.92 | no |
| queue: job turnaround, submitted to done, mean (s) | 617 | 671.5 | +8.8% | -9.076 to +118.1 | no |
| queue: jobs unfinished at the window's end | 4.9 | 5.4 | +10.2% | -1.558 to +2.558 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.938e-15 to -9.698e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.516 | +0.1% | -0.001092 to +0.007759 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 271.1 | +0.7% | +0.5423 to +3.128 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 271.1 | +0.7% | +0.5423 to +3.128 | yes: power given |
| response time (ms), mean | 189.9 | 109.6 | -42.3% | -133.4 to -27.16 | yes: GAIN |
| response time (ms), 95th percentile | 553.6 | 189.1 | -65.8% | -610.9 to -118.1 | yes: GAIN |
| response time (ms), 99th percentile | 821.8 | 268.6 | -67.3% | -892.1 to -214.3 | yes: GAIN |
| time over the response line (% of samples) | 7.527 | 0.04633 | -99.4% | -14.94 to -0.01735 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 0 | -100.0% | -9.55 to -1.65 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.585 | 804.9 | +10511.5% | +533 to +1062 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05196 | 0.05715 | +10.0% | +0.001313 to +0.009062 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.247 | 1.372 | +10.0% | +0.03152 to +0.2175 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.247 | 1.372 | +10.0% | +0.03152 to +0.2175 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 525.4 | 473.3 | -9.9% | -90.22 to -14.03 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.85 | 2.007 | +8.5% | +0.03195 to +0.283 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 35.33 | 41.66 | +17.9% | +4.513 to +8.15 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 1334 | +82.4% | +494.1 to +710.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 116.2 | +697000.0% | +70.48 to +161.9 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 520.7 | +520600.0% | +331.9 to +709.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 38.37 | 617 | +1508.1% | +409.9 to +747.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 4.9 | +4.9 (native is 0) | -0.7671 to +10.57 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.949 | -17.5% | -1.687 to -0.4151 | yes: GAIN |
| node-hours | 2.512 | 2.076 | -17.4% | -0.7044 to -0.1682 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 269.5 | +0.1% | -0.5652 to +1.045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 236.5 | -12.2% | -52.95 to -12.6 | yes: GAIN |
| response time (ms), mean | 189.9 | 171.8 | -9.5% | -30.37 to -5.803 | yes: GAIN |
| response time (ms), 95th percentile | 553.6 | 619.9 | +12.0% | -20.42 to +152.9 | no |
| response time (ms), 99th percentile | 821.8 | 925.1 | +12.6% | -32.71 to +239.2 | no |
| time over the response line (% of samples) | 7.527 | 8.179 | +8.7% | -0.4933 to +1.798 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 5.2 | -7.1% | -2.126 to +1.326 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 171.8 | +172 (native is 0) | +116.1 to +227.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.585 | 8.482 | +11.8% | -0.6222 to +2.416 | no |
| utilisation (used / allocatable) | 0.05196 | 0.06253 | +20.3% | +0.003509 to +0.01763 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.247 | 1.229 | -1.5% | -0.06507 to +0.02829 | no |
| Omni's own CPU (cores), mean | 0 | 0.04254 | +0.0425 (native is 0) | +0.03715 to +0.04793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.247 | 1.271 | +1.9% | -0.02416 to +0.07247 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 525.4 | 462.1 | -12.0% | -110.2 to -16.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.85 | 2.432 | +31.5% | +0.2625 to +0.9013 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | -0.1417 to +1.742 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | -0.2835 to +3.483 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 35.33 | 37.16 | +5.2% | +1.345 to +2.326 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 734.9 | +0.5% | -1.479 to +9.279 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.97 | -33.8% | -3.259 to -0.801 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 0.0375 | +125.0% | -0.0002416 to +0.04191 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.3 | +200.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 38.37 | 42.89 | +11.8% | -0.6167 to +9.658 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.949 | -17.5% | -1.687 to -0.4151 | yes: GAIN |
| node-hours | 2.516 | 2.076 | -17.5% | -0.7085 to -0.1707 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 269.5 | -0.6% | -3.077 to -0.1142 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 236.5 | -12.8% | -55.81 to -13.41 | yes: GAIN |
| response time (ms), mean | 109.6 | 171.8 | +56.8% | -0.1716 to +124.6 | no |
| response time (ms), 95th percentile | 189.1 | 619.9 | +227.7% | +107.8 to +753.7 | yes: LOSS |
| response time (ms), 99th percentile | 268.6 | 925.1 | +244.4% | +190.2 to +1123 | yes: LOSS |
| time over the response line (% of samples) | 0.04633 | 8.179 | +17553.8% | -0.02142 to +16.29 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 5.2 | +5.2 (native is 0) | +0.806 to +9.594 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 171.8 | +172 (native is 0) | +116.1 to +227.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 804.9 | 8.482 | -98.9% | -1060 to -532.7 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05715 | 0.06253 | +9.4% | +0.0006971 to +0.01007 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.229 | -10.4% | -0.2424 to -0.04337 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04254 | +0.0425 (native is 0) | +0.03715 to +0.04793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.271 | -7.3% | -0.2048 to +0.004136 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.3 | 462.1 | -2.4% | -36.49 to +14.13 | no |
| HPA replicas, mean | 2.007 | 2.432 | +21.1% | +0.03731 to +0.8116 | yes: power given |
| pods started | 0.3 | 0.8 | +166.7% | -0.6802 to +1.68 | no |
| pod start wait, total (s) | 0.4 | 1.6 | +300.0% | -0.9539 to +3.354 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | -0.6567 to +1.257 | no |
| host CPU busy, the real machine under kind (%) | 41.66 | 37.16 | -10.8% | -6.682 to -2.311 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1334 | 734.9 | -44.9% | -703.1 to -494.1 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.1 | -48.3% | -4.027 to -1.773 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 116.2 | 0.0375 | -100.0% | -161.8 to -70.47 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 520.7 | 0.3 | -99.9% | -709 to -331.8 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 617 | 42.89 | -93.0% | -738.7 to -409.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 4.9 | 0 | -100.0% | -10.57 to +0.7671 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.923 | -1.3% | -0.1628 to +0.007823 | no |
| node-hours | 2.512 | 2.485 | -1.1% | -0.06377 to +0.008825 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 271.4 | +0.8% | +0.6093 to +3.728 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 269 | -0.1% | -3.023 to +2.489 | no |
| response time (ms), mean | 189.9 | 88.44 | -53.4% | -156 to -46.84 | yes: GAIN |
| response time (ms), 95th percentile | 553.6 | 190.5 | -65.6% | -599.7 to -126.5 | yes: GAIN |
| response time (ms), 99th percentile | 821.8 | 269.8 | -67.2% | -881.7 to -222.4 | yes: GAIN |
| time over the response line (% of samples) | 7.527 | 0.08367 | -98.9% | -14.86 to -0.02248 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 0 | -100.0% | -9.55 to -1.65 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.4 | +25.4 (native is 0) | +13.21 to +37.59 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.585 | 877.8 | +11472.6% | +592.5 to +1148 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05196 | 0.0581 | +11.8% | +0.001796 to +0.01049 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.247 | 1.377 | +10.5% | +0.03238 to +0.2284 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04071 | +0.0407 (native is 0) | +0.03515 to +0.04627 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.247 | 1.418 | +13.7% | +0.07803 to +0.2642 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 525.4 | 467 | -11.1% | -99.54 to -17.23 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.85 | 1.937 | +4.7% | -0.01472 to +0.1883 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 35.33 | 42.97 | +21.6% | +5.98 to +9.306 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 1380 | +88.8% | +546.5 to +751.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.243 | -12.6% | -1.474 to -0.03976 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 108.7 | +651850.0% | +66.54 to +150.7 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 487.4 | +487300.0% | +291 to +683.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 38.37 | 671.5 | +1650.1% | +460.3 to +806 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 5.4 | +5.4 (native is 0) | -0.9908 to +11.79 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*