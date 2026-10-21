# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.334 | 5.309 |
| node-hours | 2.517 | 2.513 | 2.238 | 2.225 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.7 | 273 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.7 | 252.1 | 251.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 332.6 | 254.1 | 300.8 | 232.6 |
| response time (ms), 95th percentile | 1097 | 726.3 | 1129 | 809.1 |
| response time (ms), 99th percentile | 1580 | 1184 | 1561 | 1326 |
| time over the response line (% of samples) | 18.02 | 9.402 | 18.03 | 10.42 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 8.8 | 10.4 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 35.9 | 42.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 13.44 | 10.77 | 14.51 |
| utilisation (used / allocatable) | 0.06129 | 0.06171 | 0.06902 | 0.07058 |
| CPU used (cores), mean | 1.471 | 1.481 | 1.453 | 1.479 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01716 | 0.01762 |
| CPU used with Omni's own (cores), mean | 1.471 | 1.481 | 1.471 | 1.497 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 444.9 | 413.7 | 405.3 |
| HPA replicas, mean | 1.973 | 2.014 | 2.317 | 2.334 |
| pods started | 0 | 0 | 0.3 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 0.7 | 1.7 |
| pod start wait, mean (s) | 0 | 0 | 0.7 | 1.35 |
| host CPU busy, the real machine under kind (%) | 42.01 | 43.08 | 42.78 | 44.03 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 771.5 | 785.8 | 773.5 | 788.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.797 | 4.767 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7 | 0.06667 | 0.6917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | 0.5 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 78.9 | 100.7 | 81.4 | 101.6 |
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
| worker nodes in service, mean | 6 | 5.309 | -11.5% | -1.35 to -0.03232 | yes: GAIN |
| node-hours | 2.513 | 2.225 | -11.4% | -0.5618 to -0.01313 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273 | +0.1% | -0.227 to +0.8073 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 251.3 | -7.9% | -41.98 to -0.9082 | yes: GAIN |
| response time (ms), mean | 254.1 | 232.6 | -8.5% | -42.88 to -0.1713 | yes: GAIN |
| response time (ms), 95th percentile | 726.3 | 809.1 | +11.4% | -62.55 to +228.3 | no |
| response time (ms), 99th percentile | 1184 | 1326 | +12.0% | -92.56 to +376.6 | no |
| time over the response line (% of samples) | 9.402 | 10.42 | +10.8% | -0.9401 to +2.968 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.1 | +3.4% | -0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 | +42.5 (native is 0) | +27.52 to +57.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.44 | 14.51 | +8.0% | -0.8448 to +2.988 | no |
| utilisation (used / allocatable) | 0.06171 | 0.07058 | +14.4% | +6.067e-05 to +0.01769 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.481 | 1.479 | -0.1% | -0.02062 to +0.01655 | no |
| Omni's own CPU (cores), mean | 0 | 0.01762 | +0.0176 (native is 0) | +0.01606 to +0.01918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.481 | 1.497 | +1.1% | -0.002501 to +0.03367 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.9 | 405.3 | -8.9% | -79.22 to +0.07532 | no |
| HPA replicas, mean | 2.014 | 2.334 | +15.9% | +0.0237 to +0.6162 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 1.7 | +1.7 (native is 0) | -0.1174 to +3.517 | no |
| pod start wait, mean (s) | 0 | 1.35 | +1.35 (native is 0) | +0.000677 to +2.699 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.08 | 44.03 | +2.2% | +0.5532 to +1.354 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785.8 | 788.4 | +0.3% | -3.537 to +8.737 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.767 | -20.6% | -2.325 to -0.1413 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7 | 0.6917 | -1.2% | -0.1114 to +0.09472 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.2 | -14.3% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.7 | 101.6 | +0.8% | -7.385 to +9.06 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.513 | -0.2% | -0.01179 to +0.003127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.7 | -0.1% | -1.178 to +0.3967 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.7 | -0.1% | -1.178 to +0.3967 | no |
| response time (ms), mean | 332.6 | 254.1 | -23.6% | -115.5 to -41.6 | yes: GAIN |
| response time (ms), 95th percentile | 1097 | 726.3 | -33.8% | -557.9 to -183.7 | yes: GAIN |
| response time (ms), 99th percentile | 1580 | 1184 | -25.0% | -684.7 to -106.7 | yes: GAIN |
| time over the response line (% of samples) | 18.02 | 9.402 | -47.8% | -12.88 to -4.36 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 8.8 | -12.0% | -2.913 to +0.5128 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 13.44 | +28.8% | +1.834 to +4.183 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06129 | 0.06171 | +0.7% | -0.0008593 to +0.001696 | no |
| CPU used (cores), mean | 1.471 | 1.481 | +0.7% | -0.02062 to +0.04071 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.471 | 1.481 | +0.7% | -0.02062 to +0.04071 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 444.9 | -0.4% | -12.06 to +8.573 | no |
| HPA replicas, mean | 1.973 | 2.014 | +2.1% | -0.1065 to +0.188 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 42.01 | 43.08 | +2.5% | +0.7922 to +1.347 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 785.8 | +1.9% | +7.422 to +21.18 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7 | +1020.0% | +0.558 to +0.717 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | +250.0% | +0.5231 to +1.477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.9 | 100.7 | +27.7% | +10.29 to +33.37 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.334 | -11.1% | -1.33 to -0.0006453 | yes: GAIN |
| node-hours | 2.517 | 2.238 | -11.1% | -0.5572 to -0.0009879 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | -0.0% | -0.8599 to +0.7309 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 252.1 | -7.7% | -42.08 to +0.05514 | no |
| response time (ms), mean | 332.6 | 300.8 | -9.6% | -41 to -22.57 | yes: GAIN |
| response time (ms), 95th percentile | 1097 | 1129 | +2.9% | -11.79 to +75.69 | no |
| response time (ms), 99th percentile | 1580 | 1561 | -1.2% | -124.9 to +87.08 | no |
| time over the response line (% of samples) | 18.02 | 18.03 | +0.0% | -0.5615 to +0.5735 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.4 | +4.0% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.9 (native is 0) | +17.37 to +54.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 10.77 | +3.3% | -1.733 to +2.419 | no |
| utilisation (used / allocatable) | 0.06129 | 0.06902 | +12.6% | -0.0002425 to +0.01572 | no |
| CPU used (cores), mean | 1.471 | 1.453 | -1.2% | -0.04515 to +0.01011 | no |
| Omni's own CPU (cores), mean | 0 | 0.01716 | +0.0172 (native is 0) | +0.0141 to +0.02022 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.471 | 1.471 | -0.0% | -0.02772 to +0.027 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 413.7 | -7.4% | -65.99 to +0.1498 | no |
| HPA replicas, mean | 1.973 | 2.317 | +17.4% | +0.128 to +0.5598 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.2567 to +1.657 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.2567 to +1.657 | no |
| host CPU busy, the real machine under kind (%) | 42.01 | 42.78 | +1.8% | +0.4682 to +1.069 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 773.5 | +0.3% | -1.439 to +5.439 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.797 | -20.1% | -2.341 to -0.06542 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.06667 | +6.7% | -0.03902 to +0.04736 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.9 | 81.4 | +3.2% | -0.1243 to +5.141 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.334 | -11.1% | -1.33 to -0.0006453 | yes: GAIN |
| node-hours | 2.513 | 2.238 | -10.9% | -0.5512 to +0.00169 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273 | +0.1% | -0.5284 to +1.18 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 252.1 | -7.6% | -41.24 to -0.003337 | yes: GAIN |
| response time (ms), mean | 254.1 | 300.8 | +18.4% | +10.2 to +83.28 | yes: LOSS |
| response time (ms), 95th percentile | 726.3 | 1129 | +55.5% | +194.8 to +610.8 | yes: LOSS |
| response time (ms), 99th percentile | 1184 | 1561 | +31.8% | +51.76 to +701.8 | yes: LOSS |
| time over the response line (% of samples) | 9.402 | 18.03 | +91.8% | +4.253 to +13 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 10.4 | +18.2% | -0.09273 to +3.293 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.9 (native is 0) | +17.37 to +54.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.44 | 10.77 | -19.8% | -5.053 to -0.2767 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06171 | 0.06902 | +11.9% | -0.001445 to +0.01608 | no |
| CPU used (cores), mean | 1.481 | 1.453 | -1.9% | -0.05299 to -0.002137 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01716 | +0.0172 (native is 0) | +0.0141 to +0.02022 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.481 | 1.471 | -0.7% | -0.03535 to +0.01454 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.9 | 413.7 | -7.0% | -70.6 to +8.244 | no |
| HPA replicas, mean | 2.014 | 2.317 | +15.1% | +0.06173 to +0.5446 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.2567 to +1.657 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.2567 to +1.657 | no |
| host CPU busy, the real machine under kind (%) | 43.08 | 42.78 | -0.7% | -0.6015 to -0.0005408 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785.8 | 773.5 | -1.6% | -19.26 to -5.34 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.797 | -20.1% | -2.341 to -0.06542 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7 | 0.06667 | -90.5% | -0.7113 to -0.5554 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.5 | -64.3% | -1.526 to -0.2737 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 100.7 | 81.4 | -19.2% | -30.13 to -8.51 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.309 | -11.5% | -1.35 to -0.03232 | yes: GAIN |
| node-hours | 2.517 | 2.225 | -11.6% | -0.568 to -0.01557 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | -0.0% | -0.8727 to +0.672 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 251.3 | -8.0% | -42.82 to -0.8429 | yes: GAIN |
| response time (ms), mean | 332.6 | 232.6 | -30.1% | -137.1 to -63.01 | yes: GAIN |
| response time (ms), 95th percentile | 1097 | 809.1 | -26.2% | -462.6 to -113.4 | yes: GAIN |
| response time (ms), 99th percentile | 1580 | 1326 | -16.1% | -521.3 to +13.95 | no |
| time over the response line (% of samples) | 18.02 | 10.42 | -42.2% | -11.93 to -3.283 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.1 | -9.0% | -2.268 to +0.4676 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 | +42.5 (native is 0) | +27.52 to +57.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 14.51 | +39.1% | +2.729 to +5.431 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06129 | 0.07058 | +15.2% | +0.001176 to +0.01741 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.471 | 1.479 | +0.5% | -0.01837 to +0.03439 | no |
| Omni's own CPU (cores), mean | 0 | 0.01762 | +0.0176 (native is 0) | +0.01606 to +0.01918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.471 | 1.497 | +1.7% | +7.246e-05 to +0.05119 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 405.3 | -9.2% | -75.34 to -7.287 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.334 | +18.3% | +0.0886 to +0.6327 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 1.7 | +1.7 (native is 0) | -0.1174 to +3.517 | no |
| pod start wait, mean (s) | 0 | 1.35 | +1.35 (native is 0) | +0.000677 to +2.699 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.01 | 44.03 | +4.8% | +1.664 to +2.383 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 788.4 | +2.2% | +9.494 to +24.31 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.767 | -20.6% | -2.325 to -0.1413 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.6917 | +1006.7% | +0.5491 to +0.7092 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | +0.4984 to +1.102 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.9 | 101.6 | +28.7% | +12.48 to +32.85 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*