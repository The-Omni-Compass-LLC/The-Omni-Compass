# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.93 | 6.511 |
| node-hours | 5.023 | 5.027 | 4.573 | 2.725 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 504.6 | 524.7 | 504.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 504.6 | 491.1 | 331.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 513.9 | 125.1 | 553.1 | 72.97 |
| response time (ms), 95th percentile | 2033 | 169.9 | 2494 | 93.04 |
| response time (ms), 99th percentile | 2908 | 189.2 | 3715 | 118.7 |
| time over the response line (% of samples) | 20.41 | 0 | 22.38 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 0 | 12.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 205.2 | 32.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 38.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 0 | 16.76 | 0.08 |
| utilisation (used / allocatable) | 0.03354 | 0.006085 | 0.0379 | 0.009516 |
| CPU used (cores), mean | 1.61 | 0.2921 | 1.636 | 0.2467 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03778 | 0.02083 |
| CPU used with Omni's own (cores), mean | 1.61 | 0.2921 | 1.674 | 0.2676 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.1 | 4221 | 725.7 | 3305 |
| HPA replicas, mean | 4.051 | 4.235 | 5.357 | 4.48 |
| pods started | 0.1 | 0.5 | 3.6 | 1.6 |
| pod start wait, total (s) | 0.2 | 0.8 | 8.6 | 2.5 |
| pod start wait, mean (s) | 0.2 | 0.7 | 2.039 | 1.25 |
| host CPU busy, the real machine under kind (%) | 48.77 | 13.68 | 53.15 | 15.7 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 835.3 | 1506 | 867.4 | 1504 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.43 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1159 | 0.075 | 1157 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1476 | 0.5 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 147.6 | 1159 | 171.8 | 1157 |
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
| worker nodes in service, mean | 12 | 6.511 | -45.7% | -6.125 to -4.854 | yes: GAIN |
| node-hours | 5.027 | 2.725 | -45.8% | -2.559 to -2.046 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 504.3 | -0.1% | -2.167 to +1.454 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 331.9 | -34.2% | -191.7 to -153.8 | yes: GAIN |
| response time (ms), mean | 125.1 | 72.97 | -41.7% | -62.43 to -41.91 | yes: GAIN |
| response time (ms), 95th percentile | 169.9 | 93.04 | -45.2% | -90.89 to -62.8 | yes: GAIN |
| response time (ms), 99th percentile | 189.2 | 118.7 | -37.2% | -84.5 to -56.42 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 | +32.6 (native is 0) | +29.86 to +35.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.08 (native is 0) | -0.04875 to +0.2087 | no |
| utilisation (used / allocatable) | 0.006085 | 0.009516 | +56.4% | +0.00277 to +0.004093 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2921 | 0.2467 | -15.5% | -0.05377 to -0.03691 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02083 | +0.0208 (native is 0) | +0.01806 to +0.0236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2921 | 0.2676 | -8.4% | -0.03333 to -0.01568 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4221 | 3305 | -21.7% | -1044 to -787.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.235 | 4.48 | +5.8% | -0.01441 to +0.504 | no |
| pods started | 0.5 | 1.6 | +220.0% | +0.1796 to +2.02 | yes: power given |
| pod start wait, total (s) | 0.8 | 2.5 | +212.5% | +0.1529 to +3.247 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 1.25 | +78.6% | -0.4396 to +1.54 | no |
| host CPU busy, the real machine under kind (%) | 13.68 | 15.7 | +14.7% | +1.551 to +2.484 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1506 | 1504 | -0.1% | -7.755 to +3.955 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1157 | -0.2% | -7.64 to +3.94 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1474 | -0.1% | -7.886 to +3.686 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1157 | -0.2% | -7.64 to +3.94 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -5.849e-15 to +1.647e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.023 | 5.027 | +0.1% | -0.0152 to +0.02387 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 504.6 | -3.7% | -22.11 to -17 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 504.6 | -3.7% | -22.11 to -17 | yes: GAIN |
| response time (ms), mean | 513.9 | 125.1 | -75.6% | -593.9 to -183.6 | yes: GAIN |
| response time (ms), 95th percentile | 2033 | 169.9 | -91.6% | -2897 to -829.2 | yes: GAIN |
| response time (ms), 99th percentile | 2908 | 189.2 | -93.5% | -4163 to -1276 | yes: GAIN |
| time over the response line (% of samples) | 20.41 | 0 | -100.0% | -31.77 to -9.05 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 0 | -100.0% | -15.13 to -5.471 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 0 | -100.0% | -15.2 to -8.08 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03354 | 0.006085 | -81.9% | -0.03022 to -0.02469 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.61 | 0.2921 | -81.9% | -1.45 to -1.185 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.61 | 0.2921 | -81.9% | -1.45 to -1.185 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.1 | 4221 | +432.9% | +2984 to +3874 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.051 | 4.235 | +4.5% | -0.07013 to +0.4372 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | -0.09105 to +1.291 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | -0.2726 to +1.273 | no |
| host CPU busy, the real machine under kind (%) | 48.77 | 13.68 | -71.9% | -39.26 to -30.93 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 835.3 | 1506 | +80.3% | +604 to +737 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1159 | +1854780.0% | +1155 to +1163 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1476 | +295020.0% | +1471 to +1479 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 147.6 | 1159 | +685.3% | +942.7 to +1081 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.93 | -8.9% | -2.663 to +0.5272 | no |
| node-hours | 5.023 | 4.573 | -9.0% | -1.116 to +0.2156 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 524.7 | +0.1% | -1.045 to +2.002 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 491.1 | -6.3% | -83.64 to +17.41 | no |
| response time (ms), mean | 513.9 | 553.1 | +7.6% | +2.799 to +75.53 | yes: LOSS |
| response time (ms), 95th percentile | 2033 | 2494 | +22.7% | +195.7 to +725.9 | yes: LOSS |
| response time (ms), 99th percentile | 2908 | 3715 | +27.7% | +329.3 to +1283 | yes: LOSS |
| time over the response line (% of samples) | 20.41 | 22.38 | +9.6% | -0.1159 to +4.049 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 12.2 | +18.4% | +0.008978 to +3.791 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 205.2 | +205 (native is 0) | +131.8 to +278.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 16.76 | +44.0% | +1.741 to +8.496 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03354 | 0.0379 | +13.0% | +0.0001071 to +0.00862 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.636 | +1.6% | -0.05074 to +0.1036 | no |
| Omni's own CPU (cores), mean | 0 | 0.03778 | +0.0378 (native is 0) | +0.03426 to +0.0413 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.674 | +4.0% | -0.01577 to +0.1441 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.1 | 725.7 | -8.4% | -121.5 to -11.21 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.051 | 5.357 | +32.2% | +0.8297 to +1.782 | yes: power given |
| pods started | 0.1 | 3.6 | +3500.0% | +1.527 to +5.473 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.6 | +4200.0% | +2.95 to +13.85 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.039 | +919.5% | +0.7827 to +2.895 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.77 | 53.15 | +9.0% | +3.308 to +5.448 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 835.3 | 867.4 | +3.8% | +11.19 to +53.01 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.43 | -13.1% | -3.897 to +0.7598 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.075 | +20.0% | -0.05495 to +0.07995 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 147.6 | 171.8 | +16.3% | +10.11 to +38.15 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.93 | -8.9% | -2.663 to +0.5272 | no |
| node-hours | 5.027 | 4.573 | -9.0% | -1.121 to +0.2124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 524.7 | +4.0% | +17.34 to +22.73 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 491.1 | -2.7% | -65.66 to +38.54 | no |
| response time (ms), mean | 125.1 | 553.1 | +342.0% | +194.8 to +661.1 | yes: LOSS |
| response time (ms), 95th percentile | 169.9 | 2494 | +1368.0% | +1109 to +3539 | yes: LOSS |
| response time (ms), 99th percentile | 189.2 | 3715 | +1863.6% | +1681 to +5369 | yes: LOSS |
| time over the response line (% of samples) | 0 | 22.38 | +22.4 (native is 0) | +11.8 to +32.96 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.2 | +12.2 (native is 0) | +7.422 to +16.98 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 205.2 | +205 (native is 0) | +131.8 to +278.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 16.76 | +16.8 (native is 0) | +11.03 to +22.49 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006085 | 0.0379 | +522.9% | +0.02836 to +0.03528 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2921 | 1.636 | +460.2% | +1.15 to +1.538 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03778 | +0.0378 (native is 0) | +0.03426 to +0.0413 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2921 | 1.674 | +473.1% | +1.184 to +1.579 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4221 | 725.7 | -82.8% | -3992 to -2999 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.235 | 5.357 | +26.5% | +0.7426 to +1.502 | yes: power given |
| pods started | 0.5 | 3.6 | +620.0% | +1.064 to +5.136 | yes: power given |
| pod start wait, total (s) | 0.8 | 8.6 | +975.0% | +2.303 to +13.3 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.039 | +191.3% | +0.1112 to +2.567 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.68 | 53.15 | +288.5% | +34.57 to +44.37 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1506 | 867.4 | -42.4% | -724.2 to -552.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.075 | -100.0% | -1163 to -1155 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.5 | -100.0% | -1479 to -1471 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 171.8 | -85.2% | -1068 to -906.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.511 | -45.7% | -6.125 to -4.854 | yes: GAIN |
| node-hours | 5.023 | 2.725 | -45.7% | -2.566 to -2.03 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 504.3 | -3.8% | -22.12 to -17.71 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 331.9 | -36.7% | -211.9 to -172.7 | yes: GAIN |
| response time (ms), mean | 513.9 | 72.97 | -85.8% | -654.9 to -227 | yes: GAIN |
| response time (ms), 95th percentile | 2033 | 93.04 | -95.4% | -2982 to -897.7 | yes: GAIN |
| response time (ms), 99th percentile | 2908 | 118.7 | -95.9% | -4239 to -1340 | yes: GAIN |
| time over the response line (% of samples) | 20.41 | 0 | -100.0% | -31.77 to -9.05 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 0 | -100.0% | -15.13 to -5.471 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 | +32.6 (native is 0) | +29.86 to +35.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.64 | 0.08 | -99.3% | -15.18 to -7.946 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03354 | 0.009516 | -71.6% | -0.02653 to -0.02151 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.61 | 0.2467 | -84.7% | -1.495 to -1.231 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02083 | +0.0208 (native is 0) | +0.01806 to +0.0236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 0.2676 | -83.4% | -1.472 to -1.213 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.1 | 3305 | +317.3% | +2140 to +2886 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.051 | 4.48 | +10.6% | +0.1653 to +0.6914 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.657 to +2.343 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | +0.7529 to +3.847 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | +0.2876 to +1.812 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.77 | 15.7 | -67.8% | -36.88 to -29.27 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 835.3 | 1504 | +80.0% | +600.1 to +737.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1157 | +1851820.0% | +1155 to +1160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1474 | +294600.0% | +1470 to +1476 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 147.6 | 1157 | +684.0% | +938.7 to +1081 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*