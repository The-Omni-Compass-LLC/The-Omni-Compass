# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.849 | 4.747 |
| node-hours | 2.517 | 2.512 | 2.035 | 1.987 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.7 | 270.9 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 270.7 | 234.7 | 231.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 262.8 | 199.6 | 227.9 | 162.9 |
| response time (ms), 95th percentile | 823.2 | 487.3 | 840.9 | 464 |
| response time (ms), 99th percentile | 1158 | 781.2 | 1222 | 762.1 |
| time over the response line (% of samples) | 13.78 | 6.535 | 13.01 | 6.415 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.7 | 7 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 47.4 | 26.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.522 | 14.72 | 10.07 | 13.96 |
| utilisation (used / allocatable) | 0.0569 | 0.05647 | 0.06901 | 0.07149 |
| CPU used (cores), mean | 1.366 | 1.355 | 1.312 | 1.325 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01553 | 0.01524 |
| CPU used with Omni's own (cores), mean | 1.366 | 1.355 | 1.327 | 1.34 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 488.2 | 427.2 | 416.7 |
| HPA replicas, mean | 2.043 | 2.023 | 1.973 | 1.966 |
| pods started | 0.3 | 0.2 | 0 | 0.2 |
| pod start wait, total (s) | 0.8 | 0.7 | 0 | 0.6 |
| pod start wait, mean (s) | 0.55 | 0.7 | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 38.3 | 39.24 | 39.09 | 40.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750.5 | 762.2 | 751.3 | 762.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.152 | 3.968 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.6875 | 0.05417 | 0.7125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | 0.3 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 58.56 | 75.43 | 58.76 | 74.58 |
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
| worker nodes in service, mean | 6 | 4.747 | −20.9% | −2.1622 to −0.3447 | yes: GAIN |
| node-hours | 2.512 | 1.987 | −20.9% | −0.9049 to −0.1454 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.6 | −0.0% | −1.1234 to +0.9282 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 231.2 | −14.6% | −67.9431 to −10.9980 | yes: GAIN |
| response time (ms), mean | 199.6 | 162.9 | −18.4% | −48.6073 to −24.7695 | yes: GAIN |
| response time (ms), 95th percentile | 487.3 | 464 | −4.8% | −69.5383 to +22.9423 | no |
| response time (ms), 99th percentile | 781.2 | 762.1 | −2.4% | −116.4112 to +78.3202 | no |
| time over the response line (% of samples) | 6.535 | 6.415 | −1.8% | −0.9418 to +0.7035 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.5 | −3.0% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +17.7702 to +35.2298 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 13.96 | −5.2% | −2.7652 to +1.2485 | no |
| utilisation (used / allocatable) | 0.05647 | 0.07149 | +26.6% | +0.0035 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.355 | 1.325 | −2.2% | −0.0568 to −0.0039 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01524 | +0.015 (native is 0) | +0.0134 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.34 | −1.1% | −0.0419 to +0.0117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.2 | 416.7 | −14.6% | −127.3585 to −15.5267 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 1.966 | −2.8% | −0.2631 to +0.1491 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.7 | 0.6 | −14.3% | −0.8872 to +0.6872 | no |
| pod start wait, mean (s) | 0.7 | 0.6 | −14.3% | −0.8872 to +0.6872 | no |
| host CPU busy, the real machine under kind (%) | 39.24 | 40.11 | +2.2% | +0.3436 to +1.3869 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 762.2 | 762.4 | +0.0% | −3.4442 to +3.8442 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.968 | −33.9% | −3.4611 to −0.6030 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 0.7125 | +3.6% | −0.1069 to +0.1569 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.4 | +7.7% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.43 | 74.58 | −1.1% | −5.7694 to +4.0611 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.512 | −0.2% | −0.0128 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.7 | −0.3% | −1.7209 to +0.1189 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 270.7 | −0.3% | −1.7209 to +0.1189 | no |
| response time (ms), mean | 262.8 | 199.6 | −24.0% | −103.5132 to −22.9133 | yes: GAIN |
| response time (ms), 95th percentile | 823.2 | 487.3 | −40.8% | −539.7200 to −131.9260 | yes: GAIN |
| response time (ms), 99th percentile | 1158 | 781.2 | −32.6% | −606.5273 to −148.0349 | yes: GAIN |
| time over the response line (% of samples) | 13.78 | 6.535 | −52.6% | −12.5862 to −1.9057 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.7 | −4.3% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.522 | 14.72 | +72.8% | +3.4130 to +8.9870 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0569 | 0.05647 | −0.8% | −0.0014 to +0.0006 | no |
| CPU used (cores), mean | 1.366 | 1.355 | −0.8% | −0.0345 to +0.0138 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.366 | 1.355 | −0.8% | −0.0345 to +0.0138 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 488.2 | +1.2% | −4.1901 to +15.7821 | no |
| HPA replicas, mean | 2.043 | 2.023 | −1.0% | −0.1388 to +0.0987 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.8 | 0.7 | −12.5% | −1.5086 to +1.3086 | no |
| pod start wait, mean (s) | 0.55 | 0.7 | +27.3% | −0.8045 to +1.1045 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 39.24 | +2.5% | +0.4190 to +1.4659 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.5 | 762.2 | +1.6% | +3.0566 to +20.3434 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.6875 | +1550.0% | +0.5567 to +0.7350 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | +225.0% | +0.6738 to +1.1262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.56 | 75.43 | +28.8% | +4.5987 to +29.1346 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.849 | −19.2% | −2.0391 to −0.2633 | yes: GAIN |
| node-hours | 2.517 | 2.035 | −19.1% | −0.8604 to −0.1033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.9 | −0.2% | −1.8057 to +0.7298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 234.7 | −13.5% | −65.7396 to −7.7405 | yes: GAIN |
| response time (ms), mean | 262.8 | 227.9 | −13.3% | −52.2035 to −17.5944 | yes: GAIN |
| response time (ms), 95th percentile | 823.2 | 840.9 | +2.2% | −45.7492 to +81.2472 | no |
| response time (ms), 99th percentile | 1158 | 1222 | +5.5% | −60.1287 to +186.8569 | no |
| time over the response line (% of samples) | 13.78 | 13.01 | −5.6% | −1.6006 to +0.0652 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | ±0.0% | −0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.400 (native is 0) | +19.9101 to +74.8899 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.522 | 10.07 | +18.2% | −0.6905 to +3.7872 | no |
| utilisation (used / allocatable) | 0.0569 | 0.06901 | +21.3% | +0.0019 to +0.0223 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.312 | −4.0% | −0.0925 to −0.0157 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01553 | +0.016 (native is 0) | +0.0141 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.327 | −2.8% | −0.0776 to +0.0004 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 427.2 | −11.4% | −102.3637 to −8.0509 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.043 | 1.973 | −3.4% | −0.2684 to +0.1280 | no |
| pods started | 0.3 | 0 | −100.0% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.8 | 0 | −100.0% | −2.0526 to +0.4526 | no |
| pod start wait, mean (s) | 0.55 | 0 | −100.0% | −1.3837 to +0.2837 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 39.09 | +2.1% | +0.5098 to +1.0618 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.5 | 751.3 | +0.1% | −1.1015 to +2.7015 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.152 | −30.8% | −3.2271 to −0.4682 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05417 | +30.0% | −0.0298 to +0.0548 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.56 | 58.76 | +0.3% | −3.0648 to +3.4648 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.849 | −19.2% | −2.0391 to −0.2633 | yes: GAIN |
| node-hours | 2.512 | 2.035 | −19.0% | −0.8507 to −0.1023 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | −0.3952 to +0.9213 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 234.7 | −13.3% | −64.1778 to −7.7003 | yes: GAIN |
| response time (ms), mean | 199.6 | 227.9 | +14.2% | −1.5076 to +58.1363 | no |
| response time (ms), 95th percentile | 487.3 | 840.9 | +72.6% | +168.2185 to +538.9255 | yes: LOSS |
| response time (ms), 99th percentile | 781.2 | 1222 | +56.4% | +194.6921 to +686.5983 | yes: LOSS |
| time over the response line (% of samples) | 6.535 | 13.01 | +99.1% | +1.8689 to +11.0875 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 7 | +4.5% | −0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.400 (native is 0) | +19.9101 to +74.8899 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 10.07 | −31.6% | −6.9177 to −2.3857 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05647 | 0.06901 | +22.2% | +0.0017 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.355 | 1.312 | −3.2% | −0.0640 to −0.0235 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01553 | +0.016 (native is 0) | +0.0141 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.327 | −2.1% | −0.0489 to −0.0075 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.2 | 427.2 | −12.5% | −114.6267 to −7.3799 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.023 | 1.973 | −2.5% | −0.1930 to +0.0928 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.7 | 0 | −100.0% | −1.7690 to +0.3690 | no |
| pod start wait, mean (s) | 0.7 | 0 | −100.0% | −1.7690 to +0.3690 | no |
| host CPU busy, the real machine under kind (%) | 39.24 | 39.09 | −0.4% | −0.9045 to +0.5912 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 762.2 | 751.3 | −1.4% | −19.2721 to −2.5279 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.152 | −30.8% | −3.2271 to −0.4682 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 0.05417 | −92.1% | −0.7305 to −0.5362 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.3 | −76.9% | −1.3372 to −0.6628 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 75.43 | 58.76 | −22.1% | −29.3112 to −4.0221 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.747 | −20.9% | −2.1622 to −0.3447 | yes: GAIN |
| node-hours | 2.517 | 1.987 | −21.1% | −0.9143 to −0.1466 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.6 | −0.3% | −1.8698 to +0.0725 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 231.2 | −14.8% | −69.5013 to −11.0418 | yes: GAIN |
| response time (ms), mean | 262.8 | 162.9 | −38.0% | −143.6880 to −56.1153 | yes: GAIN |
| response time (ms), 95th percentile | 823.2 | 464 | −43.6% | −564.2526 to −153.9894 | yes: GAIN |
| response time (ms), 99th percentile | 1158 | 762.1 | −34.2% | −610.4004 to −182.2528 | yes: GAIN |
| time over the response line (% of samples) | 13.78 | 6.415 | −53.4% | −12.5952 to −2.1349 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.5 | −7.1% | −1.1952 to +0.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.5 | +26.500 (native is 0) | +17.7702 to +35.2298 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.522 | 13.96 | +63.9% | +3.3792 to +7.5042 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0569 | 0.07149 | +25.6% | +0.0038 to +0.0254 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.325 | −3.0% | −0.0844 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.01524 | +0.015 (native is 0) | +0.0134 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.34 | −1.9% | −0.0700 to +0.0190 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 416.7 | −13.6% | −114.6196 to −16.6736 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.043 | 1.966 | −3.8% | −0.2670 to +0.1128 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.8 | 0.6 | −25.0% | −1.4972 to +1.0972 | no |
| pod start wait, mean (s) | 0.55 | 0.6 | +9.1% | −0.7488 to +0.8488 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 40.11 | +4.7% | +1.5213 to +2.0942 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.5 | 762.4 | +1.6% | +4.3340 to +19.4660 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.968 | −33.9% | −3.4611 to −0.6030 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.7125 | +1610.0% | +0.5572 to +0.7845 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | +250.0% | +1.0000 to +1.0000 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.56 | 74.58 | +27.3% | +5.1596 to +26.8654 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*