# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.258 | 5.592 |
| node-hours | 2.518 | 2.514 | 2.206 | 2.344 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | 272.6 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | 249.3 | 259.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 334.2 | 394.1 | 308.7 | 342.1 |
| response time (ms), 95th percentile | 1122 | 1604 | 1220 | 1558 |
| response time (ms), 99th percentile | 1586 | 2344 | 1799 | 2354 |
| time over the response line (% of samples) | 15.93 | 14.78 | 15.78 | 13.41 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.8 | 9.6 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 50 | 24 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 33.33 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.96 | 20.01 | 12.36 | 19.94 |
| utilisation (used / allocatable) | 0.05947 | 0.06028 | 0.06818 | 0.06361 |
| CPU used (cores), mean | 1.427 | 1.447 | 1.432 | 1.426 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01772 | 0.01591 |
| CPU used with Omni's own (cores), mean | 1.427 | 1.447 | 1.45 | 1.442 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 460.4 | 418.8 | 441.5 |
| HPA replicas, mean | 1.982 | 2.011 | 2.135 | 2.325 |
| pods started | 0 | 0.1 | 0.3 | 0.6 |
| pod start wait, total (s) | 0 | 0.2 | 0.5 | 0.9 |
| pod start wait, mean (s) | 0 | 0.2 | 0.5 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.88 | 43.59 | 41.88 | 44.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 774.4 | 809.5 | 780.7 | 809.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.636 | 5.266 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.013 | 0.0625 | 1.008 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.8 | 0.5 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 81.62 | 116.4 | 86.07 | 115.8 |
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
| worker nodes in service, mean | 6 | 5.592 | -6.8% | -0.9729 to +0.1569 | no |
| node-hours | 2.514 | 2.344 | -6.8% | -0.4087 to +0.06884 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 | -0.0% | -1.3 to +1.104 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 259.5 | -4.8% | -31.42 to +5.511 | no |
| response time (ms), mean | 394.1 | 342.1 | -13.2% | -70.33 to -33.73 | yes: GAIN |
| response time (ms), 95th percentile | 1604 | 1558 | -2.8% | -120.3 to +29.62 | no |
| response time (ms), 99th percentile | 2344 | 2354 | +0.4% | -94.9 to +114.5 | no |
| time over the response line (% of samples) | 14.78 | 13.41 | -9.2% | -2.399 to -0.3309 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.9 | +1.0% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24 | +24 (native is 0) | +16.22 to +31.78 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.01 | 19.94 | -0.3% | -1.939 to +1.809 | no |
| utilisation (used / allocatable) | 0.06028 | 0.06361 | +5.5% | -0.000915 to +0.007575 | no |
| CPU used (cores), mean | 1.447 | 1.426 | -1.4% | -0.06707 to +0.02633 | no |
| Omni's own CPU (cores), mean | 0 | 0.01591 | +0.0159 (native is 0) | +0.01399 to +0.01783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.447 | 1.442 | -0.3% | -0.05114 to +0.04222 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.4 | 441.5 | -4.1% | -41.19 to +3.318 | no |
| HPA replicas, mean | 2.011 | 2.325 | +15.6% | +0.1257 to +0.5027 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | +0.1111 to +1.289 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | +0.1111 to +1.289 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.59 | 44.27 | +1.6% | +0.103 to +1.254 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 809.5 | 809.6 | +0.0% | -7.057 to +7.257 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.266 | -12.2% | -1.742 to +0.2732 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.013 | 1.008 | -0.4% | -0.1152 to +0.1069 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.8 | 2.1 | -25.0% | -2.051 to +0.6509 | no |
| queue: job turnaround, submitted to done, mean (s) | 116.4 | 115.8 | -0.5% | -7.185 to +6.06 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.368e-15 to +1.013e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.514 | -0.2% | -0.01165 to +0.002654 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | -0.1% | -1.197 to +0.8136 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.4 | -0.1% | -1.197 to +0.8136 | no |
| response time (ms), mean | 334.2 | 394.1 | +17.9% | +14.13 to +105.8 | yes: LOSS |
| response time (ms), 95th percentile | 1122 | 1604 | +42.9% | +124.1 to +838.9 | yes: LOSS |
| response time (ms), 99th percentile | 1586 | 2344 | +47.8% | +281.3 to +1236 | yes: LOSS |
| time over the response line (% of samples) | 15.93 | 14.78 | -7.2% | -3.56 to +1.259 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.8 | +16.7% | -0.4221 to +3.222 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.96 | 20.01 | +82.6% | +2.566 to +15.53 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05947 | 0.06028 | +1.4% | -0.0004683 to +0.002098 | no |
| CPU used (cores), mean | 1.427 | 1.447 | +1.4% | -0.01124 to +0.05035 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.427 | 1.447 | +1.4% | -0.01124 to +0.05035 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 460.4 | -0.8% | -14.97 to +7.527 | no |
| HPA replicas, mean | 1.982 | 2.011 | +1.4% | -0.0958 to +0.1527 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.88 | 43.59 | +6.6% | +1.946 to +3.471 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.4 | 809.5 | +4.5% | +10.3 to +59.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.012 | +1769.2% | +0.6156 to +1.301 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.8 | +833.3% | +0.1577 to +4.842 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.62 | 116.4 | +42.5% | +13.25 to +56.21 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.258 | -12.4% | -1.291 to -0.193 | yes: GAIN |
| node-hours | 2.518 | 2.206 | -12.4% | -0.5471 to -0.07727 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 | -0.0% | -0.9652 to +0.9634 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 249.3 | -8.5% | -41.24 to -5.358 | yes: GAIN |
| response time (ms), mean | 334.2 | 308.7 | -7.6% | -47.87 to -2.965 | yes: GAIN |
| response time (ms), 95th percentile | 1122 | 1220 | +8.7% | -75 to +270.5 | no |
| response time (ms), 99th percentile | 1586 | 1799 | +13.5% | +5.874 to +421 | yes: LOSS |
| time over the response line (% of samples) | 15.93 | 15.78 | -1.0% | -1.142 to +0.8379 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.6 | +14.3% | -0.3004 to +2.7 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 | +50 (native is 0) | +27.85 to +72.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.96 | 12.36 | +12.8% | -0.4414 to +3.251 | no |
| utilisation (used / allocatable) | 0.05947 | 0.06818 | +14.7% | +0.002647 to +0.01478 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.427 | 1.432 | +0.4% | -0.0252 to +0.03524 | no |
| Omni's own CPU (cores), mean | 0 | 0.01772 | +0.0177 (native is 0) | +0.01559 to +0.01985 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.427 | 1.45 | +1.6% | -0.007623 to +0.0531 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 418.8 | -9.8% | -77.3 to -13.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.982 | 2.135 | +7.7% | -0.004972 to +0.3107 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1952 to +1.195 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1952 to +1.195 | no |
| host CPU busy, the real machine under kind (%) | 40.88 | 41.88 | +2.5% | +0.5548 to +1.45 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.4 | 780.7 | +0.8% | -1.39 to +13.99 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.636 | -22.7% | -2.279 to -0.4499 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0625 | +15.4% | -0.0283 to +0.04497 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.62 | 86.07 | +5.4% | -3.164 to +12.06 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.258 | -12.4% | -1.291 to -0.193 | yes: GAIN |
| node-hours | 2.514 | 2.206 | -12.2% | -0.5437 to -0.07164 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.6 | +0.1% | -0.7623 to +1.144 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 249.3 | -8.5% | -40.96 to -5.262 | yes: GAIN |
| response time (ms), mean | 394.1 | 308.7 | -21.7% | -126.4 to -44.34 | yes: GAIN |
| response time (ms), 95th percentile | 1604 | 1220 | -23.9% | -696.9 to -70.59 | yes: GAIN |
| response time (ms), 99th percentile | 2344 | 1799 | -23.3% | -924.3 to -166.1 | yes: GAIN |
| time over the response line (% of samples) | 14.78 | 15.78 | +6.8% | -0.8313 to +2.829 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.6 | -2.0% | -1.738 to +1.338 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 | +50 (native is 0) | +27.85 to +72.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.01 | 12.36 | -38.2% | -13.37 to -1.916 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06028 | 0.06818 | +13.1% | +0.001101 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.447 | 1.432 | -1.0% | -0.04272 to +0.01365 | no |
| Omni's own CPU (cores), mean | 0 | 0.01772 | +0.0177 (native is 0) | +0.01559 to +0.01985 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.447 | 1.45 | +0.2% | -0.02411 to +0.03047 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.4 | 418.8 | -9.0% | -80.02 to -3.135 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.135 | +6.2% | +0.001527 to +0.2473 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | -0.5953 to +1.195 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | -0.5953 to +1.195 | no |
| host CPU busy, the real machine under kind (%) | 43.59 | 41.88 | -3.9% | -2.365 to -1.048 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 809.5 | 780.7 | -3.6% | -48.64 to -8.963 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.636 | -22.7% | -2.279 to -0.4499 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.013 | 0.0625 | -93.8% | -1.278 to -0.6218 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.8 | 0.5 | -82.1% | -4.46 to -0.1396 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 116.4 | 86.07 | -26.0% | -48.08 to -12.48 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.592 | -6.8% | -0.9729 to +0.1569 | no |
| node-hours | 2.518 | 2.344 | -6.9% | -0.411 to +0.06212 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 | -0.1% | -1.587 to +1.007 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 259.5 | -4.8% | -31.58 to +5.282 | no |
| response time (ms), mean | 334.2 | 342.1 | +2.4% | -24.79 to +40.65 | no |
| response time (ms), 95th percentile | 1122 | 1558 | +38.9% | +97.39 to +774.9 | yes: LOSS |
| response time (ms), 99th percentile | 1586 | 2354 | +48.5% | +232.7 to +1304 | yes: LOSS |
| time over the response line (% of samples) | 15.93 | 13.41 | -15.8% | -5.128 to +0.09616 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.9 | +17.9% | -0.05441 to +3.054 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24 | +24 (native is 0) | +16.22 to +31.78 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.96 | 19.94 | +82.0% | +1.452 to +16.52 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05947 | 0.06361 | +7.0% | +0.0003606 to +0.007929 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.427 | 1.426 | -0.1% | -0.06083 to +0.0592 | no |
| Omni's own CPU (cores), mean | 0 | 0.01591 | +0.0159 (native is 0) | +0.01399 to +0.01783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.427 | 1.442 | +1.1% | -0.04556 to +0.07575 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.1 | 441.5 | -4.9% | -41.5 to -3.816 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.982 | 2.325 | +17.3% | +0.1067 to +0.5787 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.88 | 44.27 | +8.3% | +2.5 to +4.274 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 774.4 | 809.6 | +4.5% | +9.251 to +61.15 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.266 | -12.2% | -1.742 to +0.2732 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.008 | +1761.5% | +0.6617 to +1.247 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 2.1 | +600.0% | +0.6919 to +2.908 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 81.62 | 115.8 | +41.9% | +13.2 to +55.13 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*