# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.059 | 6.904 |
| node-hours | 5.022 | 5.026 | 3.801 | 2.891 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.7 | 504.3 | 523.7 | 504.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.7 | 504.3 | 431.2 | 344.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 385.7 | 102.2 | 379.7 | 60.3 |
| response time (ms), 95th percentile | 1422 | 141 | 1533 | 77.46 |
| response time (ms), 99th percentile | 1972 | 162.2 | 2162 | 106.5 |
| time over the response line (% of samples) | 12.61 | 0 | 13.96 | 0.003597 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0 | 8.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 87.9 | 24.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 73.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 0.025 | 15.32 | 0 |
| utilisation (used / allocatable) | 0.03125 | 0.005492 | 0.04053 | 0.007891 |
| CPU used (cores), mean | 1.5 | 0.2636 | 1.448 | 0.2187 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01309 | 0.0082 |
| CPU used with Omni's own (cores), mean | 1.5 | 0.2636 | 1.461 | 0.2269 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 856.1 | 4693 | 713.5 | 3886 |
| HPA replicas, mean | 4.05 | 4.042 | 4.095 | 4.117 |
| pods started | 0.2 | 0.7 | 0.6 | 1.1 |
| pod start wait, total (s) | 0.3 | 1.5 | 1 | 1.6 |
| pod start wait, mean (s) | 0.15 | 0.9 | 0.65 | 0.8917 |
| host CPU busy, the real machine under kind (%) | 45.76 | 13.3 | 47.68 | 14.12 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806 | 1505 | 818.8 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 7.14 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1158 | 0.04583 | 1159 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | 0.2 | 1475 |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 1158 | 125.8 | 1159 |
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
| worker nodes in service, mean | 12 | 6.904 | -42.5% | -5.373 to -4.819 | yes: GAIN |
| node-hours | 5.026 | 2.891 | -42.5% | -2.253 to -2.017 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.3 | 504.2 | -0.0% | -1.269 to +1.064 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.3 | 344.1 | -31.8% | -169.1 to -151.3 | yes: GAIN |
| response time (ms), mean | 102.2 | 60.3 | -41.0% | -53.91 to -29.87 | yes: GAIN |
| response time (ms), 95th percentile | 141 | 77.46 | -45.1% | -81.86 to -45.23 | yes: GAIN |
| response time (ms), 99th percentile | 162.2 | 106.5 | -34.3% | -68.48 to -42.92 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.003597 | +0.0036 (native is 0) | -0.00454 to +0.01173 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.2 | +24.2 (native is 0) | +23.14 to +25.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0 | -100.0% | -0.08155 to +0.03155 | no |
| utilisation (used / allocatable) | 0.005492 | 0.007891 | +43.7% | +0.002026 to +0.002772 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2636 | 0.2187 | -17.0% | -0.04917 to -0.04065 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0082 | +0.0082 (native is 0) | +0.006926 to +0.009474 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2636 | 0.2269 | -13.9% | -0.04095 to -0.03247 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4693 | 3886 | -17.2% | -917.1 to -696.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.042 | 4.117 | +1.8% | -0.08061 to +0.2286 | no |
| pods started | 0.7 | 1.1 | +57.1% | -1.116 to +1.916 | no |
| pod start wait, total (s) | 1.5 | 1.6 | +6.7% | -2.522 to +2.722 | no |
| pod start wait, mean (s) | 0.9 | 0.8917 | -0.9% | -1.343 to +1.326 | no |
| host CPU busy, the real machine under kind (%) | 13.3 | 14.12 | +6.2% | +0.5054 to +1.141 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 1505 | +0.0% | -4.036 to +4.436 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1159 | +0.0% | -3.794 to +4.711 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1475 | +0.0% | -3.808 to +4.808 | no |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1159 | +0.0% | -3.794 to +4.711 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -7.62e-15 to -3.393e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.022 | 5.026 | +0.1% | -0.01116 to +0.01983 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.7 | 504.3 | -3.5% | -21.74 to -15.09 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.7 | 504.3 | -3.5% | -21.74 to -15.09 | yes: GAIN |
| response time (ms), mean | 385.7 | 102.2 | -73.5% | -552.2 to -14.8 | yes: GAIN |
| response time (ms), 95th percentile | 1422 | 141 | -90.1% | -2524 to -38.9 | yes: GAIN |
| response time (ms), 99th percentile | 1972 | 162.2 | -91.8% | -3481 to -139.1 | yes: GAIN |
| time over the response line (% of samples) | 12.61 | 0 | -100.0% | -24.24 to -0.9786 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0 | -100.0% | -12.31 to -1.292 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 0.025 | -99.8% | -23.91 to -2.891 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03125 | 0.005492 | -82.4% | -0.02933 to -0.02219 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.5 | 0.2636 | -82.4% | -1.408 to -1.065 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.5 | 0.2636 | -82.4% | -1.408 to -1.065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 856.1 | 4693 | +448.2% | +3344 to +4330 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.05 | 4.042 | -0.2% | -0.2094 to +0.1945 | no |
| pods started | 0.2 | 0.7 | +250.0% | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0.3 | 1.5 | +400.0% | +0.04168 to +2.358 | yes: LOSS |
| pod start wait, mean (s) | 0.15 | 0.9 | +500.0% | -0.06296 to +1.563 | no |
| host CPU busy, the real machine under kind (%) | 45.76 | 13.3 | -70.9% | -37.75 to -27.18 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806 | 1505 | +86.7% | +607.7 to +790.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1158 | +1323895.2% | +1156 to +1161 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | +245666.7% | +1471 to +1477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 1158 | +904.5% | +950.1 to +1136 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.059 | -24.5% | -4.614 to -1.269 | yes: GAIN |
| node-hours | 5.022 | 3.801 | -24.3% | -1.923 to -0.5189 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.7 | 523.7 | +0.2% | -0.3459 to +2.393 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.7 | 431.2 | -17.5% | -144.1 to -38.82 | yes: GAIN |
| response time (ms), mean | 385.7 | 379.7 | -1.5% | -26.33 to +14.39 | no |
| response time (ms), 95th percentile | 1422 | 1533 | +7.7% | +19.79 to +200.5 | yes: LOSS |
| response time (ms), 99th percentile | 1972 | 2162 | +9.7% | +65.88 to +314.7 | yes: LOSS |
| time over the response line (% of samples) | 12.61 | 13.96 | +10.7% | +0.2125 to +2.488 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 8.2 | +20.6% | +0.001538 to +2.798 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 87.9 | +87.9 (native is 0) | +55.37 to +120.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 15.32 | +14.1% | -0.1439 to +3.934 | no |
| utilisation (used / allocatable) | 0.03125 | 0.04053 | +29.7% | +0.003482 to +0.01508 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.5 | 1.448 | -3.5% | -0.1062 to +0.002078 | no |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.0131 (native is 0) | +0.01213 to +0.01405 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.5 | 1.461 | -2.6% | -0.09334 to +0.01542 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 856.1 | 713.5 | -16.7% | -233.2 to -51.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.05 | 4.095 | +1.1% | -0.212 to +0.3024 | no |
| pods started | 0.2 | 0.6 | +200.0% | -0.4396 to +1.24 | no |
| pod start wait, total (s) | 0.3 | 1 | +233.3% | -0.7717 to +2.172 | no |
| pod start wait, mean (s) | 0.15 | 0.65 | +333.3% | -0.326 to +1.326 | no |
| host CPU busy, the real machine under kind (%) | 45.76 | 47.68 | +4.2% | +1.447 to +2.388 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806 | 818.8 | +1.6% | -0.5302 to +26.13 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 7.14 | -40.5% | -7.412 to -2.309 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.04583 | -47.6% | -0.1076 to +0.02423 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.2 | -66.7% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 125.8 | +9.1% | +1.018 to +20.01 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.059 | -24.5% | -4.614 to -1.269 | yes: GAIN |
| node-hours | 5.026 | 3.801 | -24.4% | -1.931 to -0.5188 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.3 | 523.7 | +3.9% | +15.72 to +23.15 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.3 | 431.2 | -14.5% | -128.7 to -17.46 | yes: GAIN |
| response time (ms), mean | 102.2 | 379.7 | +271.6% | +1.691 to +553.4 | yes: LOSS |
| response time (ms), 95th percentile | 141 | 1533 | +986.8% | +106.1 to +2677 | yes: LOSS |
| response time (ms), 99th percentile | 162.2 | 2162 | +1233.4% | +236.7 to +3764 | yes: LOSS |
| time over the response line (% of samples) | 0 | 13.96 | +14 (native is 0) | +2.291 to +25.63 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.2 | +8.2 (native is 0) | +2.509 to +13.89 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 87.9 | +87.9 (native is 0) | +55.37 to +120.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 15.32 | +61186.7% | +3.583 to +27.01 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005492 | 0.04053 | +638.0% | +0.03225 to +0.03783 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2636 | 1.448 | +449.3% | +1.001 to +1.368 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.0131 (native is 0) | +0.01213 to +0.01405 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2636 | 1.461 | +454.3% | +1.014 to +1.381 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4693 | 713.5 | -84.8% | -4549 to -3411 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.042 | 4.095 | +1.3% | -0.2158 to +0.3212 | no |
| pods started | 0.7 | 0.6 | -14.3% | -1.19 to +0.99 | no |
| pod start wait, total (s) | 1.5 | 1 | -33.3% | -2.743 to +1.743 | no |
| pod start wait, mean (s) | 0.9 | 0.65 | -27.8% | -1.526 to +1.026 | no |
| host CPU busy, the real machine under kind (%) | 13.3 | 47.68 | +258.6% | +28.82 to +39.95 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 818.8 | -45.6% | -789.7 to -582.7 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.04583 | -100.0% | -1161 to -1156 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.2 | -100.0% | -1477 to -1472 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 125.8 | -89.1% | -1135 to -930.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.904 | -42.5% | -5.373 to -4.819 | yes: GAIN |
| node-hours | 5.022 | 2.891 | -42.4% | -2.241 to -2.021 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.7 | 504.2 | -3.5% | -21.72 to -15.31 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.7 | 344.1 | -34.2% | -185.6 to -171.6 | yes: GAIN |
| response time (ms), mean | 385.7 | 60.3 | -84.4% | -604.3 to -46.5 | yes: GAIN |
| response time (ms), 95th percentile | 1422 | 77.46 | -94.6% | -2601 to -89 | yes: GAIN |
| response time (ms), 99th percentile | 1972 | 106.5 | -94.6% | -3541 to -190 | yes: GAIN |
| time over the response line (% of samples) | 12.61 | 0.003597 | -100.0% | -24.23 to -0.9784 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0 | -100.0% | -12.31 to -1.292 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.2 | +24.2 (native is 0) | +23.14 to +25.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 0 | -100.0% | -23.92 to -2.929 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03125 | 0.007891 | -74.8% | -0.02667 to -0.02005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.5 | 0.2187 | -85.4% | -1.453 to -1.11 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0082 | +0.0082 (native is 0) | +0.006926 to +0.009474 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.5 | 0.2269 | -84.9% | -1.443 to -1.103 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 856.1 | 3886 | +354.0% | +2611 to +3450 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.05 | 4.117 | +1.6% | -0.1321 to +0.2652 | no |
| pods started | 0.2 | 1.1 | +450.0% | -0.2898 to +2.09 | no |
| pod start wait, total (s) | 0.3 | 1.6 | +433.3% | -0.421 to +3.021 | no |
| pod start wait, mean (s) | 0.15 | 0.8917 | +494.4% | -0.05235 to +1.536 | no |
| host CPU busy, the real machine under kind (%) | 45.76 | 14.12 | -69.1% | -36.66 to -26.62 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806 | 1505 | +86.7% | +609.2 to +789.2 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1159 | +1324419.0% | +1155 to +1163 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1475 | +245750.0% | +1470 to +1479 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 115.3 | 1159 | +904.9% | +951.6 to +1136 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*