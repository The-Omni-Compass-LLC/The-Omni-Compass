# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.065 | 5.107 |
| node-hours | 2.52 | 2.513 | 2.124 | 2.142 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.3 | 272.2 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.3 | 242.7 | 243.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 296.9 | 356.8 | 275.8 | 323.1 |
| response time (ms), 95th percentile | 959.7 | 1486 | 1061 | 1541 |
| response time (ms), 99th percentile | 1415 | 2380 | 1568 | 2390 |
| time over the response line (% of samples) | 16.35 | 14.32 | 16.82 | 13.52 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.4 | 8.6 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 39.4 | 41.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.96 | 15.92 | 9.927 | 16.63 |
| utilisation (used / allocatable) | 0.05787 | 0.05713 | 0.0698 | 0.06951 |
| CPU used (cores), mean | 1.389 | 1.371 | 1.391 | 1.388 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01518 | 0.01656 |
| CPU used with Omni's own (cores), mean | 1.389 | 1.371 | 1.406 | 1.404 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.2 | 490.3 | 416.6 | 420.3 |
| HPA replicas, mean | 1.93 | 2.019 | 2.326 | 2.267 |
| pods started | 0 | 0.2 | 0.3 | 0.5 |
| pod start wait, total (s) | 0 | 0.5 | 0.4 | 0.7 |
| pod start wait, mean (s) | 0 | 0.5 | 0.4 | 0.7 |
| host CPU busy, the real machine under kind (%) | 39.41 | 41.68 | 40.32 | 42.5 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 761.7 | 795 | 768.4 | 797.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.468 | 4.594 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7917 | 0.0875 | 0.8042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | 0.6 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 70.23 | 105.3 | 75.83 | 108.3 |
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
| worker nodes in service, mean | 6 | 5.107 | −14.9% | −1.7757 to −0.0104 | yes: GAIN |
| node-hours | 2.513 | 2.142 | −14.8% | −0.7425 to −0.0003 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.9 | +0.2% | −0.4267 to +1.5182 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 243.8 | −10.1% | −55.0888 to +0.0428 | no |
| response time (ms), mean | 356.8 | 323.1 | −9.4% | −61.0264 to −6.3288 | yes: GAIN |
| response time (ms), 95th percentile | 1486 | 1541 | +3.7% | −66.2248 to +175.7198 | no |
| response time (ms), 99th percentile | 2380 | 2390 | +0.4% | −267.0218 to +287.9470 | no |
| time over the response line (% of samples) | 14.32 | 13.52 | −5.6% | −1.7275 to +0.1255 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.8 | +4.8% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 | +41.300 (native is 0) | +28.8371 to +53.7629 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.92 | 16.63 | +4.4% | −1.2450 to +2.6617 | no |
| utilisation (used / allocatable) | 0.05713 | 0.06951 | +21.7% | −0.0001 to +0.0249 | no |
| CPU used (cores), mean | 1.371 | 1.388 | +1.2% | −0.0225 to +0.0559 | no |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.017 (native is 0) | +0.0145 to +0.0186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.404 | +2.4% | −0.0051 to +0.0716 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.3 | 420.3 | −14.3% | −144.1619 to +4.2663 | no |
| HPA replicas, mean | 2.019 | 2.267 | +12.3% | +0.0156 to +0.4797 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | −0.7417 to +1.1417 | no |
| pod start wait, mean (s) | 0.5 | 0.7 | +40.0% | −0.7417 to +1.1417 | no |
| host CPU busy, the real machine under kind (%) | 41.68 | 42.5 | +2.0% | +0.5797 to +1.0565 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795 | 797.5 | +0.3% | −2.0271 to +7.0271 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.594 | −23.4% | −2.7029 to −0.1092 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7917 | 0.8042 | +1.6% | −0.0849 to +0.1099 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.3 | 108.3 | +2.8% | −1.8625 to +7.8542 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.52 | 2.513 | −0.3% | −0.0134 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.3 | −0.3% | −1.8399 to +0.0358 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.3 | −0.3% | −1.8399 to +0.0358 | no |
| response time (ms), mean | 296.9 | 356.8 | +20.2% | +15.4849 to +104.2597 | yes: LOSS |
| response time (ms), 95th percentile | 959.7 | 1486 | +54.8% | +180.0743 to +872.1587 | yes: LOSS |
| response time (ms), 99th percentile | 1415 | 2380 | +68.2% | +283.5930 to +1646.6596 | yes: LOSS |
| time over the response line (% of samples) | 16.35 | 14.32 | −12.4% | −3.3167 to −0.7450 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.4 | +2.4% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.96 | 15.92 | +77.7% | +5.1217 to +8.7983 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05787 | 0.05713 | −1.3% | −0.0029 to +0.0014 | no |
| CPU used (cores), mean | 1.389 | 1.371 | −1.3% | −0.0690 to +0.0337 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.389 | 1.371 | −1.3% | −0.0690 to +0.0337 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.2 | 490.3 | +2.7% | −13.9528 to +40.0810 | no |
| HPA replicas, mean | 1.93 | 2.019 | +4.6% | −0.0606 to +0.2390 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 39.41 | 41.68 | +5.8% | +1.4947 to +3.0461 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761.7 | 795 | +4.4% | +13.7539 to +52.8461 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7917 | +1627.3% | +0.6543 to +0.8374 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | +275.0% | +0.5722 to +1.6278 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 70.23 | 105.3 | +49.9% | +14.3558 to +55.7858 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.065 | −15.6% | −1.8019 to −0.0688 | yes: GAIN |
| node-hours | 2.52 | 2.124 | −15.7% | −0.7569 to −0.0346 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.2 | −0.0% | −0.8235 to +0.7418 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 242.7 | −10.9% | −56.6835 to −2.3899 | yes: GAIN |
| response time (ms), mean | 296.9 | 275.8 | −7.1% | −33.4486 to −8.6553 | yes: GAIN |
| response time (ms), 95th percentile | 959.7 | 1061 | +10.6% | +25.0505 to +178.2145 | yes: LOSS |
| response time (ms), 99th percentile | 1415 | 1568 | +10.9% | −18.0588 to +325.8362 | no |
| time over the response line (% of samples) | 16.35 | 16.82 | +2.9% | −0.1353 to +1.0878 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.6 | +4.9% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.4 | +39.400 (native is 0) | +23.9285 to +54.8715 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.96 | 9.927 | +10.8% | −1.6216 to +3.5549 | no |
| utilisation (used / allocatable) | 0.05787 | 0.0698 | +20.6% | +0.0018 to +0.0220 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.389 | 1.391 | +0.2% | −0.0275 to +0.0320 | no |
| Omni's own CPU (cores), mean | 0 | 0.01518 | +0.015 (native is 0) | +0.0137 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.389 | 1.406 | +1.3% | −0.0131 to +0.0480 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.2 | 416.6 | −12.7% | −111.8342 to −9.4319 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.93 | 2.326 | +20.5% | +0.1389 to +0.6526 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 39.41 | 40.32 | +2.3% | +0.4841 to +1.3388 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761.7 | 768.4 | +0.9% | +0.8883 to +12.5117 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.468 | −25.5% | −2.9162 to −0.1470 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.0875 | +90.9% | −0.0049 to +0.0883 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.23 | 75.83 | +8.0% | −0.8980 to +12.0980 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.065 | −15.6% | −1.8019 to −0.0688 | yes: GAIN |
| node-hours | 2.513 | 2.124 | −15.5% | −0.7509 to −0.0270 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 272.2 | +0.3% | −0.2227 to +1.9450 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 242.7 | −10.6% | −55.4465 to −1.8228 | yes: GAIN |
| response time (ms), mean | 356.8 | 275.8 | −22.7% | −124.1741 to −37.6743 | yes: GAIN |
| response time (ms), 95th percentile | 1486 | 1061 | −28.6% | −715.9263 to −133.0417 | yes: GAIN |
| response time (ms), 99th percentile | 2380 | 1568 | −34.1% | −1389.8915 to −232.5837 | yes: GAIN |
| time over the response line (% of samples) | 14.32 | 16.82 | +17.5% | +1.1573 to +3.8569 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.6 | +2.4% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.4 | +39.400 (native is 0) | +23.9285 to +54.8715 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.92 | 9.927 | −37.6% | −8.4289 to −3.5578 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05713 | 0.0698 | +22.2% | +0.0010 to +0.0243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 1.391 | +1.5% | −0.0169 to +0.0566 | no |
| Omni's own CPU (cores), mean | 0 | 0.01518 | +0.015 (native is 0) | +0.0137 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.406 | +2.6% | −0.0013 to +0.0714 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.3 | 416.6 | −15.0% | −145.3941 to −2.0003 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.326 | +15.2% | +0.0493 to +0.5639 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.5 | 0.4 | −20.0% | −0.8872 to +0.6872 | no |
| pod start wait, mean (s) | 0.5 | 0.4 | −20.0% | −0.8872 to +0.6872 | no |
| host CPU busy, the real machine under kind (%) | 41.68 | 40.32 | −3.3% | −1.8053 to −0.9127 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795 | 768.4 | −3.3% | −42.5099 to −10.6901 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.468 | −25.5% | −2.9162 to −0.1470 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7917 | 0.0875 | −88.9% | −0.7804 to −0.6279 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.6 | −60.0% | −1.1262 to −0.6738 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 105.3 | 75.83 | −28.0% | −46.2467 to −12.6950 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.107 | −14.9% | −1.7757 to −0.0104 | yes: GAIN |
| node-hours | 2.52 | 2.142 | −15.0% | −0.7490 to −0.0075 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 | −0.1% | −1.2318 to +0.5192 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 243.8 | −10.4% | −56.4535 to −0.3965 | yes: GAIN |
| response time (ms), mean | 296.9 | 323.1 | +8.8% | −13.9844 to +66.3738 | no |
| response time (ms), 95th percentile | 959.7 | 1541 | +60.5% | +191.9059 to +969.8221 | yes: LOSS |
| response time (ms), 99th percentile | 1415 | 2390 | +69.0% | +296.3054 to +1654.8724 | yes: LOSS |
| time over the response line (% of samples) | 16.35 | 13.52 | −17.3% | −4.7388 to −0.9249 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.8 | +7.3% | +0.0999 to +1.1001 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 | +41.300 (native is 0) | +28.8371 to +53.7629 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.96 | 16.63 | +85.6% | +5.1277 to +10.2089 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05787 | 0.06951 | +20.1% | +0.0009 to +0.0224 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.389 | 1.388 | −0.1% | −0.0317 to +0.0298 | no |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.017 (native is 0) | +0.0145 to +0.0186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.389 | 1.404 | +1.1% | −0.0167 to +0.0479 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.2 | 420.3 | −11.9% | −108.5239 to −5.2434 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.93 | 2.267 | +17.4% | +0.1313 to +0.5422 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.41 | 42.5 | +7.8% | +2.1491 to +4.0278 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761.7 | 797.5 | +4.7% | +15.2342 to +56.3658 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.594 | −23.4% | −2.7029 to −0.1092 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.8042 | +1654.5% | +0.6352 to +0.8815 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | +275.0% | +0.6940 to +1.5060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 70.23 | 108.3 | +54.2% | +15.3242 to +60.8091 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*