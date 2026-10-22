# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.79 | 6.955 |
| node-hours | 5.022 | 5.021 | 4.525 | 2.912 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 504 | 525.4 | 504.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 504 | 487.5 | 346 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 555.5 | 126.3 | 560.8 | 71.44 |
| response time (ms), 95th percentile | 2124 | 174.8 | 2386 | 88.63 |
| response time (ms), 99th percentile | 2891 | 200.5 | 3355 | 125.8 |
| time over the response line (% of samples) | 19.86 | 0.003802 | 19.97 | 0 |
| failed requests (%) | 0 | 0 | 0.02181 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | 11.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 85.1 | 24.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.32 | 0.02667 | 14.16 | 0.05333 |
| utilisation (used / allocatable) | 0.03386 | 0.006109 | 0.03794 | 0.008795 |
| CPU used (cores), mean | 1.625 | 0.2933 | 1.63 | 0.2456 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0125 | 0.00878 |
| CPU used with Omni's own (cores), mean | 1.625 | 0.2933 | 1.643 | 0.2543 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.6 | 4204 | 726.7 | 3449 |
| HPA replicas, mean | 3.979 | 4.187 | 4.622 | 4.251 |
| pods started | 0.4 | 0.5 | 1.6 | 1.2 |
| pod start wait, total (s) | 0.7 | 0.6 | 2.7 | 1.8 |
| pod start wait, mean (s) | 0.7 | 0.45 | 1.533 | 1.35 |
| host CPU busy, the real machine under kind (%) | 49.72 | 14.31 | 51.52 | 15.1 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 856.3 | 1505 | 870.1 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.967 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1159 | 0.1083 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | 0.6 | 1475 |
| queue: job turnaround, submitted to done, mean (s) | 166.2 | 1159 | 172.9 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 6.955 | -42.0% | -5.286 to -4.805 | yes: GAIN |
| node-hours | 5.021 | 2.912 | -42.0% | -2.211 to -2.007 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504 | 504.5 | +0.1% | +0.06311 to +0.9071 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504 | 346 | -31.3% | -165.7 to -150.3 | yes: GAIN |
| response time (ms), mean | 126.3 | 71.44 | -43.4% | -64.7 to -44.95 | yes: GAIN |
| response time (ms), 95th percentile | 174.8 | 88.63 | -49.3% | -98.47 to -73.83 | yes: GAIN |
| response time (ms), 99th percentile | 200.5 | 125.8 | -37.3% | -89.57 to -59.95 | yes: GAIN |
| time over the response line (% of samples) | 0.003802 | 0 | -100.0% | -0.0124 to +0.004798 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.8 | +24.8 (native is 0) | +23.86 to +25.74 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 | +100.0% | -0.08161 to +0.1349 | no |
| utilisation (used / allocatable) | 0.006109 | 0.008795 | +44.0% | +0.002434 to +0.002936 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2933 | 0.2456 | -16.3% | -0.05366 to -0.04174 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00878 | +0.00878 (native is 0) | +0.007493 to +0.01007 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2933 | 0.2543 | -13.3% | -0.04416 to -0.03368 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4204 | 3449 | -18.0% | -877.2 to -634.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.187 | 4.251 | +1.5% | -0.1636 to +0.2909 | no |
| pods started | 0.5 | 1.2 | +140.0% | +0.0214 to +1.379 | yes: power given |
| pod start wait, total (s) | 0.6 | 1.8 | +200.0% | +0.09185 to +2.308 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 1.35 | +200.0% | +0.2737 to +1.526 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.31 | 15.1 | +5.6% | +0.4575 to +1.137 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 1505 | -0.0% | -2.556 to +2.156 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1158 | -0.0% | -2.524 to +2.258 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1475 | -0.0% | -2.495 to +2.295 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1158 | -0.0% | -2.524 to +2.258 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -7.023e-15 to +6.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.022 | 5.021 | -0.0% | -0.0207 to +0.02004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 504 | -3.9% | -23.71 to -17.54 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 504 | -3.9% | -23.71 to -17.54 | yes: GAIN |
| response time (ms), mean | 555.5 | 126.3 | -77.3% | -721.7 to -136.9 | yes: GAIN |
| response time (ms), 95th percentile | 2124 | 174.8 | -91.8% | -3302 to -596.8 | yes: GAIN |
| response time (ms), 99th percentile | 2891 | 200.5 | -93.1% | -4436 to -944.3 | yes: GAIN |
| time over the response line (% of samples) | 19.86 | 0.003802 | -100.0% | -32.26 to -7.449 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | -100.0% | -15.56 to -5.24 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.32 | 0.02667 | -99.8% | -26.75 to -5.83 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03386 | 0.006109 | -82.0% | -0.03134 to -0.02417 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.625 | 0.2933 | -82.0% | -1.504 to -1.16 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.625 | 0.2933 | -82.0% | -1.504 to -1.16 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.6 | 4204 | +431.1% | +2982 to +3843 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.979 | 4.187 | +5.2% | -0.05539 to +0.4718 | no |
| pods started | 0.4 | 0.5 | +25.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.7 | 0.6 | -14.3% | -1.137 to +0.9366 | no |
| pod start wait, mean (s) | 0.7 | 0.45 | -35.7% | -1.063 to +0.563 | no |
| host CPU busy, the real machine under kind (%) | 49.72 | 14.31 | -71.2% | -40.72 to -30.11 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.3 | 1505 | +75.8% | +547.5 to +750.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1159 | +1069350.0% | +1156 to +1161 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | +245683.3% | +1471 to +1477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 166.2 | 1159 | +597.1% | +889.8 to +1095 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.79 | -10.1% | -2.589 to +0.1766 | no |
| node-hours | 5.022 | 4.525 | -9.9% | -1.074 to +0.07979 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 525.4 | +0.1% | -0.933 to +2.503 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 487.5 | -7.1% | -80.88 to +6.689 | no |
| response time (ms), mean | 555.5 | 560.8 | +0.9% | -31.68 to +42.18 | no |
| response time (ms), 95th percentile | 2124 | 2386 | +12.3% | +19.48 to +503.3 | yes: LOSS |
| response time (ms), 99th percentile | 2891 | 3355 | +16.1% | +57.43 to +871.7 | yes: LOSS |
| time over the response line (% of samples) | 19.86 | 19.97 | +0.6% | -0.9018 to +1.133 | no |
| failed requests (%) | 0 | 0.02181 | +0.0218 (native is 0) | -0.01362 to +0.05724 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11.3 | +8.7% | -1.245 to +3.045 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.1 | +85.1 (native is 0) | +42.05 to +128.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.32 | 14.16 | -13.2% | -9.193 to +4.883 | no |
| utilisation (used / allocatable) | 0.03386 | 0.03794 | +12.0% | +0.0001138 to +0.008042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.625 | 1.63 | +0.3% | -0.0657 to +0.07545 | no |
| Omni's own CPU (cores), mean | 0 | 0.0125 | +0.0125 (native is 0) | +0.01161 to +0.01339 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.625 | 1.643 | +1.1% | -0.05332 to +0.08807 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.6 | 726.7 | -8.2% | -124.2 to -5.404 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.979 | 4.622 | +16.1% | +0.3692 to +0.9159 | yes: power given |
| pods started | 0.4 | 1.6 | +300.0% | +0.3879 to +2.012 | yes: power given |
| pod start wait, total (s) | 0.7 | 2.7 | +285.7% | +0.492 to +3.508 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 1.533 | +119.0% | -0.4605 to +2.127 | no |
| host CPU busy, the real machine under kind (%) | 49.72 | 51.52 | +3.6% | +1.226 to +2.38 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.3 | 870.1 | +1.6% | +1.699 to +25.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.967 | -16.9% | -4.243 to +0.1773 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.1083 | +0.0% | -0.07164 to +0.07164 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 166.2 | 172.9 | +4.1% | -1.598 to +15.06 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.79 | -10.1% | -2.589 to +0.1766 | no |
| node-hours | 5.021 | 4.525 | -9.9% | -1.08 to +0.08646 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504 | 525.4 | +4.2% | +17.73 to +25.08 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504 | 487.5 | -3.3% | -62.78 to +29.83 | no |
| response time (ms), mean | 126.3 | 560.8 | +344.1% | +111.7 to +757.4 | yes: LOSS |
| response time (ms), 95th percentile | 174.8 | 2386 | +1264.9% | +655.9 to +3766 | yes: LOSS |
| response time (ms), 99th percentile | 200.5 | 3355 | +1573.0% | +1045 to +5264 | yes: LOSS |
| time over the response line (% of samples) | 0.003802 | 19.97 | +525176.1% | +8.09 to +31.85 | yes: LOSS |
| failed requests (%) | 0 | 0.02181 | +0.0218 (native is 0) | -0.01362 to +0.05724 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.3 | +11.3 (native is 0) | +5.947 to +16.65 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.1 | +85.1 (native is 0) | +42.05 to +128.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 14.16 | +53000.0% | +7.08 to +21.19 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006109 | 0.03794 | +521.0% | +0.02853 to +0.03513 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2933 | 1.63 | +455.9% | +1.124 to +1.55 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0125 | +0.0125 (native is 0) | +0.01161 to +0.01339 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2933 | 1.643 | +460.2% | +1.136 to +1.563 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4204 | 726.7 | -82.7% | -3956 to -3000 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.187 | 4.622 | +10.4% | +0.1793 to +0.6894 | yes: power given |
| pods started | 0.5 | 1.6 | +220.0% | -0.04101 to +2.241 | no |
| pod start wait, total (s) | 0.6 | 2.7 | +350.0% | +0.6129 to +3.587 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 1.533 | +240.7% | +0.1425 to +2.024 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.31 | 51.52 | +260.1% | +31.62 to +42.82 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 870.1 | -42.2% | -746.3 to -523.7 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.1083 | -100.0% | -1161 to -1156 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.6 | -100.0% | -1477 to -1471 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 172.9 | -85.1% | -1092 to -879.5 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.955 | -42.0% | -5.286 to -4.805 | yes: GAIN |
| node-hours | 5.022 | 2.912 | -42.0% | -2.205 to -2.013 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 504.5 | -3.8% | -23.22 to -17.05 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 346 | -34.0% | -183.9 to -173.4 | yes: GAIN |
| response time (ms), mean | 555.5 | 71.44 | -87.1% | -784.4 to -183.8 | yes: GAIN |
| response time (ms), 95th percentile | 2124 | 88.63 | -95.8% | -3397 to -674.7 | yes: GAIN |
| response time (ms), 99th percentile | 2891 | 125.8 | -95.6% | -4522 to -1007 | yes: GAIN |
| time over the response line (% of samples) | 19.86 | 0 | -100.0% | -32.26 to -7.45 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | -100.0% | -15.56 to -5.24 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.8 | +24.8 (native is 0) | +23.86 to +25.74 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.32 | 0.05333 | -99.7% | -26.72 to -5.807 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03386 | 0.008795 | -74.0% | -0.02856 to -0.02157 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.625 | 0.2456 | -84.9% | -1.555 to -1.204 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00878 | +0.00878 (native is 0) | +0.007493 to +0.01007 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.625 | 0.2543 | -84.4% | -1.545 to -1.197 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.6 | 3449 | +335.7% | +2321 to +2992 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.979 | 4.251 | +6.8% | +0.05309 to +0.4906 | yes: power given |
| pods started | 0.4 | 1.2 | +200.0% | +0.1427 to +1.457 | yes: power given |
| pod start wait, total (s) | 0.7 | 1.8 | +157.1% | -0.04101 to +2.241 | no |
| pod start wait, mean (s) | 0.7 | 1.35 | +92.9% | -0.3193 to +1.619 | no |
| host CPU busy, the real machine under kind (%) | 49.72 | 15.1 | -69.6% | -39.84 to -29.39 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 856.3 | 1505 | +75.7% | +546.9 to +750.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 1158 | +1069226.9% | +1155 to +1162 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | +245666.7% | +1470 to +1478 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 166.2 | 1158 | +597.0% | +889.6 to +1095 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*