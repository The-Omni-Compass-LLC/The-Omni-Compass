# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.726 | 4.832 |
| node-hours | 2.514 | 2.514 | 1.982 | 2.021 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.4 | 272.4 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.4 | 232.4 | 235.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 368.9 | 387.4 | 331.2 | 360.3 |
| response time (ms), 95th percentile | 1381 | 1468 | 1408 | 1483 |
| response time (ms), 99th percentile | 1939 | 2026 | 1975 | 2084 |
| time over the response line (% of samples) | 16.06 | 16.36 | 15.59 | 16.52 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.5 | 7.3 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 44.3 | 44.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 87.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 9.742 | 11.53 | 11.65 |
| utilisation (used / allocatable) | 0.06087 | 0.06023 | 0.07532 | 0.07481 |
| CPU used (cores), mean | 1.461 | 1.446 | 1.412 | 1.438 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01656 | 0.01751 |
| CPU used with Omni's own (cores), mean | 1.461 | 1.446 | 1.429 | 1.455 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 467.6 | 396.2 | 396.8 |
| HPA replicas, mean | 1.948 | 1.898 | 2.236 | 2.102 |
| pods started | 0 | 0.1 | 0.9 | 0.2 |
| pod start wait, total (s) | 0 | 0.3 | 1.5 | 0.7 |
| pod start wait, mean (s) | 0 | 0.3 | 0.975 | 0.7 |
| host CPU busy, the real machine under kind (%) | 41.39 | 41.81 | 41.91 | 43.05 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 795.3 | 802.5 | 796.2 | 806.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.877 | 3.968 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.2833 | 0.1167 | 0.3708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | 0.5 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 102 | 107.2 | 102.1 | 111.2 |
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
| worker nodes in service, mean | 6 | 4.832 | -19.5% | -1.981 to -0.3543 | yes: GAIN |
| node-hours | 2.514 | 2.021 | -19.6% | -0.8331 to -0.152 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.1 | -0.1% | -1.497 to +0.9172 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 235.4 | -13.6% | -62.68 to -11.23 | yes: GAIN |
| response time (ms), mean | 387.4 | 360.3 | -7.0% | -43.62 to -10.56 | yes: GAIN |
| response time (ms), 95th percentile | 1468 | 1483 | +1.0% | -43.9 to +74.34 | no |
| response time (ms), 99th percentile | 2026 | 2084 | +2.9% | -25.11 to +142.1 | no |
| time over the response line (% of samples) | 16.36 | 16.52 | +1.0% | -0.2509 to +0.5862 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.9 | +5.3% | -0.2032 to +1.003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.7 | +44.7 (native is 0) | +19.45 to +69.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.742 | 11.65 | +19.6% | -0.9967 to +4.82 | no |
| utilisation (used / allocatable) | 0.06023 | 0.07481 | +24.2% | +0.004369 to +0.02479 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.438 | -0.5% | -0.0351 to +0.01959 | no |
| Omni's own CPU (cores), mean | 0 | 0.01751 | +0.0175 (native is 0) | +0.01644 to +0.01858 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.455 | +0.7% | -0.01786 to +0.03737 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 396.8 | -15.2% | -121 to -20.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.898 | 2.102 | +10.8% | -0.0002512 to +0.409 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | -1.189 to +1.989 | no |
| pod start wait, mean (s) | 0.3 | 0.7 | +133.3% | -1.189 to +1.989 | no |
| host CPU busy, the real machine under kind (%) | 41.81 | 43.05 | +3.0% | +0.7367 to +1.754 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 802.5 | 806.9 | +0.5% | -0.9444 to +9.744 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.968 | -33.9% | -3.376 to -0.687 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2833 | 0.3708 | +30.9% | -0.123 to +0.298 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.2 | +33.3% | -0.2889 to +0.8889 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.2 | 111.2 | +3.7% | -2.236 to +10.11 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.037e-15 to +1.037e-15 | no |
| node-hours | 2.514 | 2.514 | +0.0% | -0.008098 to +0.009098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.4 | -0.1% | -1.204 to +0.6214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.4 | -0.1% | -1.204 to +0.6214 | no |
| response time (ms), mean | 368.9 | 387.4 | +5.0% | +1.672 to +35.32 | yes: LOSS |
| response time (ms), 95th percentile | 1381 | 1468 | +6.3% | +19.71 to +155.3 | yes: LOSS |
| response time (ms), 99th percentile | 1939 | 2026 | +4.5% | +9.079 to +164.3 | yes: LOSS |
| time over the response line (% of samples) | 16.06 | 16.36 | +1.9% | -0.2253 to +0.8268 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.5 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 9.742 | -11.8% | -3.266 to +0.6559 | no |
| utilisation (used / allocatable) | 0.06087 | 0.06023 | -1.0% | -0.002183 to +0.0009078 | no |
| CPU used (cores), mean | 1.461 | 1.446 | -1.0% | -0.0524 to +0.02179 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.461 | 1.446 | -1.0% | -0.0524 to +0.02179 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 467.6 | +1.8% | -6.232 to +22.52 | no |
| HPA replicas, mean | 1.948 | 1.898 | -2.6% | -0.1982 to +0.09761 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 41.81 | +1.0% | -0.1056 to +0.9471 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 802.5 | +0.9% | +1.012 to +13.39 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.2833 | +126.7% | +0.04264 to +0.274 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.9 | +125.0% | -0.005799 to +1.006 | no |
| queue: job turnaround, submitted to done, mean (s) | 102 | 107.2 | +5.1% | -1.265 to +11.71 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.726 | -21.2% | -2.143 to -0.4057 | yes: GAIN |
| node-hours | 2.514 | 1.982 | -21.1% | -0.8999 to -0.1631 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.4 | -0.1% | -1.359 to +0.8036 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.4 | -14.8% | -68.27 to -12.28 | yes: GAIN |
| response time (ms), mean | 368.9 | 331.2 | -10.2% | -55.96 to -19.39 | yes: GAIN |
| response time (ms), 95th percentile | 1381 | 1408 | +2.0% | -45.99 to +100.5 | no |
| response time (ms), 99th percentile | 1939 | 1975 | +1.8% | -56.63 to +128 | no |
| time over the response line (% of samples) | 16.06 | 15.59 | -2.9% | -1.449 to +0.5134 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.3 | -2.7% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 | +44.3 (native is 0) | +24.12 to +64.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 11.53 | +4.4% | -1.791 to +2.765 | no |
| utilisation (used / allocatable) | 0.06087 | 0.07532 | +23.7% | +0.004387 to +0.0245 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.461 | 1.412 | -3.3% | -0.08794 to -0.009465 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.0166 (native is 0) | +0.01565 to +0.01747 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.429 | -2.2% | -0.07107 to +0.006786 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 396.2 | -13.8% | -107.7 to -18.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.236 | +14.8% | +0.02346 to +0.553 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | +0.04362 to +1.756 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | -0.0174 to +3.017 | no |
| pod start wait, mean (s) | 0 | 0.975 | +0.975 (native is 0) | +0.3196 to +1.63 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.39 | 41.91 | +1.3% | +0.09368 to +0.9466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 796.2 | +0.1% | -3.63 to +5.43 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.877 | -35.4% | -3.535 to -0.7114 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.1167 | -6.7% | -0.03572 to +0.01906 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 102 | 102.1 | +0.1% | -5.154 to +5.296 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.726 | -21.2% | -2.143 to -0.4057 | yes: GAIN |
| node-hours | 2.514 | 1.982 | -21.2% | -0.8998 to -0.1642 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | +0.0% | -0.8491 to +0.8771 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 232.4 | -14.7% | -67.69 to -12.28 | yes: GAIN |
| response time (ms), mean | 387.4 | 331.2 | -14.5% | -88.88 to -23.46 | yes: GAIN |
| response time (ms), 95th percentile | 1468 | 1408 | -4.1% | -166.1 to +45.62 | no |
| response time (ms), 99th percentile | 2026 | 1975 | -2.5% | -188.5 to +86.43 | no |
| time over the response line (% of samples) | 16.36 | 15.59 | -4.7% | -1.709 to +0.1718 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.3 | -2.7% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.3 | +44.3 (native is 0) | +24.12 to +64.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.742 | 11.53 | +18.4% | -0.3265 to +3.91 | no |
| utilisation (used / allocatable) | 0.06023 | 0.07532 | +25.0% | +0.004151 to +0.02602 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.412 | -2.3% | -0.06247 to -0.004322 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.0166 (native is 0) | +0.01565 to +0.01747 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.429 | -1.2% | -0.0456 to +0.01193 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 396.2 | -15.3% | -124.6 to -18.15 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.898 | 2.236 | +17.8% | +0.0345 to +0.6426 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | -0.1417 to +1.742 | no |
| pod start wait, total (s) | 0.3 | 1.5 | +400.0% | -0.6096 to +3.01 | no |
| pod start wait, mean (s) | 0.3 | 0.975 | +225.0% | -0.4307 to +1.781 | no |
| host CPU busy, the real machine under kind (%) | 41.81 | 41.91 | +0.2% | -0.3829 to +0.5817 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 802.5 | 796.2 | -0.8% | -11.74 to -0.8623 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.877 | -35.4% | -3.535 to -0.7114 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2833 | 0.1167 | -58.8% | -0.2782 to -0.05515 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.5 | -44.4% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 107.2 | 102.1 | -4.8% | -10.07 to -0.2337 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.832 | -19.5% | -1.981 to -0.3543 | yes: GAIN |
| node-hours | 2.514 | 2.021 | -19.6% | -0.8322 to -0.1519 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | -0.2% | -1.635 to +0.4724 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 235.4 | -13.7% | -63.17 to -11.32 | yes: GAIN |
| response time (ms), mean | 368.9 | 360.3 | -2.3% | -19.36 to +2.171 | no |
| response time (ms), 95th percentile | 1381 | 1483 | +7.4% | +31.18 to +174.2 | yes: LOSS |
| response time (ms), 99th percentile | 1939 | 2084 | +7.5% | +30.76 to +259.6 | yes: LOSS |
| time over the response line (% of samples) | 16.06 | 16.52 | +2.9% | -0.2669 to +1.204 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.9 | +5.3% | -0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.7 | +44.7 (native is 0) | +19.45 to +69.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 11.65 | +5.5% | -1.781 to +2.995 | no |
| utilisation (used / allocatable) | 0.06087 | 0.07481 | +22.9% | +0.004524 to +0.02336 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.461 | 1.438 | -1.6% | -0.06976 to +0.02363 | no |
| Omni's own CPU (cores), mean | 0 | 0.01751 | +0.0175 (native is 0) | +0.01644 to +0.01858 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.455 | -0.4% | -0.05254 to +0.04143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 396.8 | -13.7% | -104.8 to -20.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.102 | +7.9% | -0.06265 to +0.3708 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.6509 to +2.051 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.6509 to +2.051 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 43.05 | +4.0% | +1.147 to +2.185 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.3 | 806.9 | +1.5% | +3.506 to +19.69 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.968 | -33.9% | -3.376 to -0.687 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.3708 | +196.7% | +0.02172 to +0.47 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | +0.2358 to +1.364 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 102 | 111.2 | +9.0% | +2.209 to +16.11 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*