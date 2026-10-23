# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.377 | 5.416 |
| node-hours | 2.511 | 2.512 | 2.252 | 2.269 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | 271.3 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.1 | 251.8 | 253 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 272.4 | 295.1 | 266.2 | 286 |
| response time (ms), 95th percentile | 848.5 | 956.4 | 1014 | 1118 |
| response time (ms), 99th percentile | 1224 | 1398 | 1481 | 1673 |
| time over the response line (% of samples) | 15.23 | 16.3 | 16.27 | 17.05 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.4 | 8.6 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 116 | 134 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.66 | 9.345 | 10.72 | 9.917 |
| utilisation (used / allocatable) | 0.05662 | 0.057 | 0.06353 | 0.06282 |
| CPU used (cores), mean | 1.359 | 1.368 | 1.371 | 1.369 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04613 | 0.04873 |
| CPU used with Omni's own (cores), mean | 1.359 | 1.368 | 1.417 | 1.417 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.9 | 485.3 | 443.6 | 447.6 |
| HPA replicas, mean | 1.95 | 1.886 | 2.635 | 2.737 |
| pods started | 0 | 0 | 1.3 | 1.7 |
| pod start wait, total (s) | 0 | 0 | 2.9 | 3.5 |
| pod start wait, mean (s) | 0 | 0 | 0.8917 | 1.533 |
| host CPU busy, the real machine under kind (%) | 38.7 | 39.47 | 41.02 | 41.78 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 753 | 761.8 | 763.1 | 770.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.825 | 4.869 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.175 | 0.04583 | 0.1958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | 0.3 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 60.58 | 68.85 | 69.48 | 77.85 |
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
| worker nodes in service, mean | 6 | 5.416 | -9.7% | -1.137 to -0.03007 | yes: GAIN |
| node-hours | 2.512 | 2.269 | -9.7% | -0.4723 to -0.01286 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.3 | +0.1% | -0.8909 to +1.459 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 253 | -6.7% | -35.63 to -0.4935 | yes: GAIN |
| response time (ms), mean | 295.1 | 286 | -3.1% | -20.82 to +2.687 | no |
| response time (ms), 95th percentile | 956.4 | 1118 | +16.9% | +54.47 to +268.1 | yes: LOSS |
| response time (ms), 99th percentile | 1398 | 1673 | +19.7% | +92.31 to +458.3 | yes: LOSS |
| time over the response line (% of samples) | 16.3 | 17.05 | +4.7% | +0.2509 to +1.269 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.9 | +6.0% | -0.005799 to +1.006 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134 (native is 0) | +71.52 to +196.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.345 | 9.917 | +6.1% | -0.9175 to +2.061 | no |
| utilisation (used / allocatable) | 0.057 | 0.06282 | +10.2% | +0.001033 to +0.01061 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.368 | 1.369 | +0.1% | -0.04638 to +0.04794 | no |
| Omni's own CPU (cores), mean | 0 | 0.04873 | +0.0487 (native is 0) | +0.04266 to +0.0548 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.368 | 1.417 | +3.6% | -0.000708 to +0.09972 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.3 | 447.6 | -7.8% | -73.18 to -2.238 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.886 | 2.737 | +45.1% | +0.5528 to +1.148 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.6856 to +2.714 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.5 (native is 0) | +1.387 to +5.613 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.533 | +1.53 (native is 0) | +0.6119 to +2.455 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.47 | 41.78 | +5.8% | +1.713 to +2.901 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.8 | 770.7 | +1.2% | +4.511 to +13.29 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.869 | -18.9% | -2.196 to -0.06573 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.1958 | +11.9% | -0.02629 to +0.06796 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 68.85 | 77.85 | +13.1% | +2.553 to +15.45 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.262e-15 to +7.291e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.511 | 2.512 | +0.0% | -0.00485 to +0.006516 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | +0.1% | -0.6602 to +1.064 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.1 | +0.1% | -0.6602 to +1.064 | no |
| response time (ms), mean | 272.4 | 295.1 | +8.3% | +2.755 to +42.57 | yes: LOSS |
| response time (ms), 95th percentile | 848.5 | 956.4 | +12.7% | +5.524 to +210.3 | yes: LOSS |
| response time (ms), 99th percentile | 1224 | 1398 | +14.2% | +56.46 to +290.9 | yes: LOSS |
| time over the response line (% of samples) | 15.23 | 16.3 | +7.0% | +0.0945 to +2.028 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.4 | +5.0% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.66 | 9.345 | -3.3% | -2.593 to +1.963 | no |
| utilisation (used / allocatable) | 0.05662 | 0.057 | +0.7% | -0.001063 to +0.001817 | no |
| CPU used (cores), mean | 1.359 | 1.368 | +0.7% | -0.02551 to +0.04362 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.359 | 1.368 | +0.7% | -0.02551 to +0.04362 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.9 | 485.3 | -0.3% | -17.93 to +14.83 | no |
| HPA replicas, mean | 1.95 | 1.886 | -3.3% | -0.174 to +0.0471 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.7 | 39.47 | +2.0% | +0.4304 to +1.115 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753 | 761.8 | +1.2% | +1.966 to +15.63 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.175 | +162.5% | +0.03241 to +0.1843 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.58 | 68.85 | +13.6% | +1.846 to +14.69 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.377 | -10.4% | -1.201 to -0.04575 | yes: GAIN |
| node-hours | 2.511 | 2.252 | -10.3% | -0.498 to -0.01969 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | -0.4404 to +1.441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 251.8 | -7.0% | -37.05 to -1.051 | yes: GAIN |
| response time (ms), mean | 272.4 | 266.2 | -2.3% | -21.92 to +9.464 | no |
| response time (ms), 95th percentile | 848.5 | 1014 | +19.5% | +54.45 to +276.7 | yes: LOSS |
| response time (ms), 99th percentile | 1224 | 1481 | +21.0% | +90.57 to +424.3 | yes: LOSS |
| time over the response line (% of samples) | 15.23 | 16.27 | +6.8% | +0.07163 to +2.001 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.6 | +7.5% | -0.09105 to +1.291 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116 | +116 (native is 0) | +66.47 to +165.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.66 | 10.72 | +11.0% | -1.031 to +3.158 | no |
| utilisation (used / allocatable) | 0.05662 | 0.06353 | +12.2% | +0.001482 to +0.01234 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.359 | 1.371 | +0.9% | -0.02533 to +0.04872 | no |
| Omni's own CPU (cores), mean | 0 | 0.04613 | +0.0461 (native is 0) | +0.03984 to +0.05242 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.359 | 1.417 | +4.3% | +0.01861 to +0.09704 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.9 | 443.6 | -8.9% | -77.8 to -8.682 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.635 | +35.1% | +0.338 to +1.031 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.08188 to +2.518 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +0.1307 to +5.669 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8917 | +0.892 (native is 0) | +0.05052 to +1.733 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.7 | 41.02 | +6.0% | +1.812 to +2.82 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753 | 763.1 | +1.3% | +1.941 to +18.26 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.825 | -19.6% | -2.255 to -0.09464 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.04583 | -31.3% | -0.07387 to +0.0322 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.58 | 69.48 | +14.7% | +2.554 to +15.24 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.377 | -10.4% | -1.201 to -0.04575 | yes: GAIN |
| node-hours | 2.512 | 2.252 | -10.3% | -0.5012 to -0.0181 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.3 | +0.1% | -0.9066 to +1.503 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 251.8 | -7.1% | -37.38 to -1.124 | yes: GAIN |
| response time (ms), mean | 295.1 | 266.2 | -9.8% | -40.53 to -17.25 | yes: GAIN |
| response time (ms), 95th percentile | 956.4 | 1014 | +6.0% | -26.29 to +141.6 | no |
| response time (ms), 99th percentile | 1398 | 1481 | +6.0% | +16.75 to +150.7 | yes: LOSS |
| time over the response line (% of samples) | 16.3 | 16.27 | -0.2% | -0.6893 to +0.6401 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.6 | +2.4% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116 | +116 (native is 0) | +66.47 to +165.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.345 | 10.72 | +14.7% | -0.7653 to +3.522 | no |
| utilisation (used / allocatable) | 0.057 | 0.06353 | +11.5% | +0.0004076 to +0.01266 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.368 | 1.371 | +0.2% | -0.05366 to +0.05894 | no |
| Omni's own CPU (cores), mean | 0 | 0.04613 | +0.0461 (native is 0) | +0.03984 to +0.05242 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.368 | 1.417 | +3.6% | -0.007608 to +0.1051 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.3 | 443.6 | -8.6% | -85.45 to +2.061 | no |
| HPA replicas, mean | 1.886 | 2.635 | +39.7% | +0.4082 to +1.088 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.08188 to +2.518 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +0.1307 to +5.669 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8917 | +0.892 (native is 0) | +0.05052 to +1.733 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.47 | 41.02 | +3.9% | +1.187 to +1.9 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.8 | 763.1 | +0.2% | -1.66 to +4.26 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.825 | -19.6% | -2.255 to -0.09464 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.04583 | -73.8% | -0.228 to -0.03037 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.3 | -57.1% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 68.85 | 69.48 | +0.9% | -1.573 to +2.831 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.416 | -9.7% | -1.137 to -0.03007 | yes: GAIN |
| node-hours | 2.511 | 2.269 | -9.6% | -0.4692 to -0.01433 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | -0.1492 to +1.121 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 253 | -6.6% | -35.32 to -0.3924 | yes: GAIN |
| response time (ms), mean | 272.4 | 286 | +5.0% | -16.43 to +43.63 | no |
| response time (ms), 95th percentile | 848.5 | 1118 | +31.7% | +70.55 to +467.9 | yes: LOSS |
| response time (ms), 99th percentile | 1224 | 1673 | +36.7% | +157.5 to +740.4 | yes: LOSS |
| time over the response line (% of samples) | 15.23 | 17.05 | +12.0% | +0.8381 to +2.804 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.9 | +11.3% | -0.19 to +1.99 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134 (native is 0) | +71.52 to +196.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.66 | 9.917 | +2.7% | -2.448 to +2.961 | no |
| utilisation (used / allocatable) | 0.05662 | 0.06282 | +10.9% | +0.001986 to +0.01041 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.359 | 1.369 | +0.7% | -0.03446 to +0.05412 | no |
| Omni's own CPU (cores), mean | 0 | 0.04873 | +0.0487 (native is 0) | +0.04266 to +0.0548 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.359 | 1.417 | +4.3% | +0.01011 to +0.107 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486.9 | 447.6 | -8.1% | -67.13 to -11.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.737 | +40.4% | +0.4583 to +1.116 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.6856 to +2.714 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.5 (native is 0) | +1.387 to +5.613 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.533 | +1.53 (native is 0) | +0.6119 to +2.455 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.7 | 41.78 | +8.0% | +2.314 to +3.845 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753 | 770.7 | +2.4% | +6.789 to +28.61 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.869 | -18.9% | -2.196 to -0.06573 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1958 | +193.8% | +0.0626 to +0.1957 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.58 | 77.85 | +28.5% | +5.112 to +29.42 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*