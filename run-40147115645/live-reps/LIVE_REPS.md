# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.918 | 5.421 |
| node-hours | 2.52 | 2.513 | 2.061 | 2.275 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.1 | 271.6 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.1 | 237.4 | 253.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 280.9 | 246.1 | 239 | 226.3 |
| response time (ms), 95th percentile | 879 | 826.5 | 872.8 | 929.5 |
| response time (ms), 99th percentile | 1280 | 1293 | 1271 | 1446 |
| time over the response line (% of samples) | 14.18 | 9.462 | 13.45 | 10.21 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 6.8 | 7.4 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38.3 | 43.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.182 | 9.408 | 9.068 | 10.8 |
| utilisation (used / allocatable) | 0.05718 | 0.05669 | 0.07073 | 0.06381 |
| CPU used (cores), mean | 1.372 | 1.361 | 1.372 | 1.358 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01567 | 0.01555 |
| CPU used with Omni's own (cores), mean | 1.372 | 1.361 | 1.388 | 1.374 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.8 | 482.2 | 412.5 | 446.6 |
| HPA replicas, mean | 1.943 | 2.022 | 2.229 | 2.536 |
| pods started | 0 | 0 | 0.4 | 0.8 |
| pod start wait, total (s) | 0 | 0 | 0.7 | 1.3 |
| pod start wait, mean (s) | 0 | 0 | 0.7 | 0.9 |
| host CPU busy, the real machine under kind (%) | 39.13 | 38.72 | 39.91 | 39.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 756 | 746.6 | 754.2 | 754.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.075 | 5.022 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05417 | 0.04167 | 0.0625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | 0.2 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 62.55 | 57.52 | 61.41 | 63.42 |
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
| worker nodes in service, mean | 6 | 5.421 | −9.6% | −1.2774 to +0.1197 | no |
| node-hours | 2.513 | 2.275 | −9.5% | −0.5295 to +0.0533 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | +0.2% | −0.1274 to +1.3323 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 253.4 | −6.5% | −39.5708 to +4.2840 | no |
| response time (ms), mean | 246.1 | 226.3 | −8.0% | −40.9920 to +1.5495 | no |
| response time (ms), 95th percentile | 826.5 | 929.5 | +12.5% | −24.9330 to +230.8260 | no |
| response time (ms), 99th percentile | 1293 | 1446 | +11.8% | +32.5696 to +273.1052 | yes: LOSS |
| time over the response line (% of samples) | 9.462 | 10.21 | +8.0% | −0.4634 to +1.9697 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.4 | +8.8% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 | +43.200 (native is 0) | +31.9313 to +54.4687 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.408 | 10.8 | +14.8% | −0.7774 to +3.5641 | no |
| utilisation (used / allocatable) | 0.05669 | 0.06381 | +12.6% | −0.0012 to +0.0154 | no |
| CPU used (cores), mean | 1.361 | 1.358 | −0.2% | −0.0316 to +0.0268 | no |
| Omni's own CPU (cores), mean | 0 | 0.01555 | +0.016 (native is 0) | +0.0134 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.361 | 1.374 | +1.0% | −0.0164 to +0.0427 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.2 | 446.6 | −7.4% | −75.1194 to +3.8169 | no |
| HPA replicas, mean | 2.022 | 2.536 | +25.4% | +0.2475 to +0.7797 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | −0.0924 to +2.6924 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.72 | 39.76 | +2.7% | +0.5428 to +1.5349 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.6 | 754.6 | +1.1% | +1.2729 to +14.7271 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.022 | −16.3% | −2.1354 to +0.1786 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0625 | +15.4% | −0.0191 to +0.0357 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.52 | 63.43 | +10.3% | +0.0182 to +11.7985 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.52 | 2.513 | −0.3% | −0.0131 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.1 | −0.3% | −1.7672 to +0.0670 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.1 | −0.3% | −1.7672 to +0.0670 | no |
| response time (ms), mean | 280.9 | 246.1 | −12.4% | −63.5255 to −6.2165 | yes: GAIN |
| response time (ms), 95th percentile | 879 | 826.5 | −6.0% | −123.4915 to +18.6255 | no |
| response time (ms), 99th percentile | 1280 | 1293 | +1.0% | −103.4265 to +128.4899 | no |
| time over the response line (% of samples) | 14.18 | 9.462 | −33.3% | −8.0948 to −1.3353 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 6.8 | −16.0% | −2.5639 to −0.0361 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.182 | 9.408 | +2.5% | −1.6239 to +2.0772 | no |
| utilisation (used / allocatable) | 0.05718 | 0.05669 | −0.9% | −0.0016 to +0.0006 | no |
| CPU used (cores), mean | 1.372 | 1.361 | −0.9% | −0.0390 to +0.0156 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.372 | 1.361 | −0.9% | −0.0390 to +0.0156 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.8 | 482.2 | +0.5% | −7.4976 to +12.3566 | no |
| HPA replicas, mean | 1.943 | 2.022 | +4.1% | −0.0637 to +0.2224 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 39.13 | 38.72 | −1.1% | −0.8440 to +0.0192 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756 | 746.6 | −1.2% | −17.4307 to −1.3693 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05417 | −13.3% | −0.0476 to +0.0309 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.55 | 57.52 | −8.0% | −10.8342 to +0.7759 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.918 | −18.0% | −1.8160 to −0.3487 | yes: GAIN |
| node-hours | 2.52 | 2.061 | −18.2% | −0.7621 to −0.1543 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | −0.1% | −0.9737 to +0.2313 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 237.4 | −12.7% | −57.2126 to −11.7631 | yes: GAIN |
| response time (ms), mean | 280.9 | 239 | −14.9% | −54.4079 to −29.4306 | yes: GAIN |
| response time (ms), 95th percentile | 879 | 872.8 | −0.7% | −47.7484 to +35.4764 | no |
| response time (ms), 99th percentile | 1280 | 1271 | −0.7% | −105.0186 to +86.2334 | no |
| time over the response line (% of samples) | 14.18 | 13.45 | −5.1% | −1.2480 to −0.2102 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 7.4 | −8.6% | −1.5953 to +0.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.300 (native is 0) | +27.5781 to +49.0219 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.182 | 9.068 | −1.2% | −1.5478 to +1.3211 | no |
| utilisation (used / allocatable) | 0.05718 | 0.07073 | +23.7% | +0.0041 to +0.0230 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.372 | −0.0% | −0.0272 to +0.0270 | no |
| Omni's own CPU (cores), mean | 0 | 0.01567 | +0.016 (native is 0) | +0.0144 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.388 | +1.1% | −0.0114 to +0.0425 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.8 | 412.5 | −14.0% | −114.9235 to −19.5946 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 2.229 | +14.7% | +0.0251 to +0.5478 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| host CPU busy, the real machine under kind (%) | 39.13 | 39.91 | +2.0% | +0.4802 to +1.0800 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756 | 754.2 | −0.2% | −5.7295 to +2.1295 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.075 | −32.1% | −3.1684 to −0.6819 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | −33.3% | −0.0530 to +0.0114 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | −60.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.55 | 61.41 | −1.8% | −3.9281 to +1.6615 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.918 | −18.0% | −1.8160 to −0.3487 | yes: GAIN |
| node-hours | 2.513 | 2.061 | −18.0% | −0.7556 to −0.1476 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.6 | +0.2% | −0.3030 to +1.2608 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 237.4 | −12.4% | −56.6685 to −10.6071 | yes: GAIN |
| response time (ms), mean | 246.1 | 239 | −2.9% | −27.6276 to +13.5311 | no |
| response time (ms), 95th percentile | 826.5 | 872.8 | +5.6% | −6.1816 to +98.7756 | no |
| response time (ms), 99th percentile | 1293 | 1271 | −1.7% | −145.4149 to +101.5663 | no |
| time over the response line (% of samples) | 9.462 | 13.45 | +42.1% | +0.9571 to +7.0148 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.4 | +8.8% | −0.1689 to +1.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.300 (native is 0) | +27.5781 to +49.0219 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.408 | 9.068 | −3.6% | −2.4563 to +1.7763 | no |
| utilisation (used / allocatable) | 0.05669 | 0.07073 | +24.8% | +0.0053 to +0.0228 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.361 | 1.372 | +0.9% | −0.0178 to +0.0411 | no |
| Omni's own CPU (cores), mean | 0 | 0.01567 | +0.016 (native is 0) | +0.0144 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.361 | 1.388 | +2.0% | −0.0028 to +0.0574 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.2 | 412.5 | −14.5% | −112.0545 to −27.3226 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.229 | +10.2% | −0.0607 to +0.4749 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.0578 to +1.4578 | no |
| host CPU busy, the real machine under kind (%) | 38.72 | 39.91 | +3.1% | +0.7375 to +1.6476 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.6 | 754.2 | +1.0% | +0.3271 to +14.8729 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.075 | −32.1% | −3.1684 to −0.6819 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04167 | −23.1% | −0.0408 to +0.0158 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | −50.0% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.52 | 61.41 | +6.8% | −0.7892 to +8.5809 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.421 | −9.6% | −1.2774 to +0.1197 | no |
| node-hours | 2.52 | 2.275 | −9.7% | −0.5377 to +0.0481 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | −0.1% | −1.0433 to +0.5480 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 253.4 | −6.8% | −40.2705 to +3.2836 | no |
| response time (ms), mean | 280.9 | 226.3 | −19.4% | −72.0918 to −37.0927 | yes: GAIN |
| response time (ms), 95th percentile | 879 | 929.5 | +5.7% | −27.2337 to +128.2607 | no |
| response time (ms), 99th percentile | 1280 | 1446 | +12.9% | +8.3289 to +322.4093 | yes: LOSS |
| time over the response line (% of samples) | 14.18 | 10.21 | −27.9% | −6.7526 to −1.1711 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 7.4 | −8.6% | −1.4578 to +0.0578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 | +43.200 (native is 0) | +31.9313 to +54.4687 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.182 | 10.8 | +17.6% | −0.8149 to +4.0549 | no |
| utilisation (used / allocatable) | 0.05718 | 0.06381 | +11.6% | −0.0025 to +0.0157 | no |
| CPU used (cores), mean | 1.372 | 1.358 | −1.0% | −0.0275 to −0.0006 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01555 | +0.016 (native is 0) | +0.0134 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.374 | +0.1% | −0.0113 to +0.0142 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.8 | 446.6 | −6.9% | −79.6614 to +13.2180 | no |
| HPA replicas, mean | 1.943 | 2.536 | +30.5% | +0.3786 to +0.8074 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | −0.0924 to +2.6924 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.13 | 39.76 | +1.6% | +0.3163 to +0.9365 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756 | 754.6 | −0.2% | −4.5668 to +1.7668 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.022 | −16.3% | −2.1354 to +0.1786 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.0625 | ±0.0% | −0.0344 to +0.0344 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.55 | 63.42 | +1.4% | −1.7564 to +3.5148 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*