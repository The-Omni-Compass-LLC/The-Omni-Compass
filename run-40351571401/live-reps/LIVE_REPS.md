# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.512 | 1.516 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.1 | 158.6 | 159.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.1 | 158.6 | 159.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 104.8 | 104.7 | 104.9 | 106.8 |
| response time (ms), 95th percentile | 220.9 | 218.5 | 218.1 | 219.2 |
| response time (ms), 99th percentile | 325.7 | 304.1 | 313.3 | 307.5 |
| time over the response line (% of samples) | 0.08974 | 0.08886 | 0.1147 | 0.1032 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0.5 | 0.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | 0.025 | 0.1567 |
| utilisation (used / allocatable) | 0.03582 | 0.03966 | 0.03589 | 0.03988 |
| CPU used (cores), mean | 0.8598 | 0.952 | 0.8615 | 0.9571 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00484 | 0.00777 |
| CPU used with Omni's own (cores), mean | 0.8598 | 0.952 | 0.8663 | 0.9649 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.3 | 665.9 | 730.7 | 662.8 |
| HPA replicas, mean | 8.81 | 8.828 | 9.065 | 9.288 |
| pods started | 4.7 | 4.9 | 5.9 | 6 |
| pod start wait, total (s) | 6.3 | 6.8 | 8.3 | 8.6 |
| pod start wait, mean (s) | 1.368 | 1.403 | 1.418 | 1.38 |
| host CPU busy, the real machine under kind (%) | 25.36 | 28.64 | 25.74 | 29.26 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 8 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 7, 8, 9): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0086 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.2 | +0.1% | −0.7881 to +1.0557 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.2 | +0.1% | −0.7881 to +1.0557 | no |
| response time (ms), mean | 104.7 | 106.8 | +2.0% | +0.0520 to +4.1646 | yes: LOSS |
| response time (ms), 95th percentile | 218.5 | 219.2 | +0.3% | −10.7187 to +11.9947 | no |
| response time (ms), 99th percentile | 304.1 | 307.5 | +1.1% | −15.9636 to +22.7722 | no |
| time over the response line (% of samples) | 0.08886 | 0.1032 | +16.2% | −0.1613 to +0.1900 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.9 | +0.900 (native is 0) | −0.6977 to +2.4977 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1567 | +95.8% | −0.0455 to +0.1988 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03988 | +0.5% | −0.0004 to +0.0009 | no |
| CPU used (cores), mean | 0.952 | 0.9571 | +0.5% | −0.0105 to +0.0209 | no |
| Omni's own CPU (cores), mean | 0 | 0.00777 | +0.008 (native is 0) | +0.0058 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.952 | 0.9649 | +1.4% | −0.0039 to +0.0297 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 662.8 | −0.5% | −12.6662 to +6.4613 | no |
| HPA replicas, mean | 8.828 | 9.288 | +5.2% | −0.3389 to +1.2595 | no |
| pods started | 4.9 | 6 | +22.4% | −0.4617 to +2.6617 | no |
| pod start wait, total (s) | 6.8 | 8.6 | +26.5% | −1.0172 to +4.6172 | no |
| pod start wait, mean (s) | 1.403 | 1.38 | −1.7% | −0.1774 to +0.1308 | no |
| host CPU busy, the real machine under kind (%) | 28.64 | 29.26 | +2.2% | +0.0861 to +1.1595 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | −0.3% | −0.0125 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.1 | +0.2% | −0.5547 to +1.3362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.1 | +0.2% | −0.5547 to +1.3362 | no |
| response time (ms), mean | 104.8 | 104.7 | −0.0% | −2.0209 to +1.9747 | no |
| response time (ms), 95th percentile | 220.9 | 218.5 | −1.1% | −12.5010 to +7.8500 | no |
| response time (ms), 99th percentile | 325.7 | 304.1 | −6.6% | −33.1384 to −10.1590 | yes: GAIN |
| time over the response line (% of samples) | 0.08974 | 0.08886 | −1.0% | −0.1143 to +0.1125 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.080 (native is 0) | −0.0121 to +0.1721 | no |
| utilisation (used / allocatable) | 0.03582 | 0.03966 | +10.7% | +0.0030 to +0.0047 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8598 | 0.952 | +10.7% | +0.0724 to +0.1120 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8598 | 0.952 | +10.7% | +0.0724 to +0.1120 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.3 | 665.9 | −9.1% | −78.5639 to −54.2964 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.81 | 8.828 | +0.2% | −0.1029 to +0.1377 | no |
| pods started | 4.7 | 4.9 | +4.3% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 6.3 | 6.8 | +7.9% | −1.1259 to +2.1259 | no |
| pod start wait, mean (s) | 1.368 | 1.403 | +2.6% | −0.2292 to +0.2992 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 28.64 | +12.9% | +2.6402 to +3.9131 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | −0.0% | −0.0066 to +0.0052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.6 | −0.0% | −0.7838 to +0.6439 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.6 | −0.0% | −0.7838 to +0.6439 | no |
| response time (ms), mean | 104.8 | 104.9 | +0.2% | −2.3060 to +2.6949 | no |
| response time (ms), 95th percentile | 220.9 | 218.1 | −1.2% | −8.6329 to +3.1559 | no |
| response time (ms), 99th percentile | 325.7 | 313.3 | −3.8% | −23.4686 to −1.4110 | yes: GAIN |
| time over the response line (% of samples) | 0.08974 | 0.1147 | +27.9% | −0.0127 to +0.0627 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.025 | +0.025 (native is 0) | −0.0315 to +0.0815 | no |
| utilisation (used / allocatable) | 0.03582 | 0.03589 | +0.2% | −0.0007 to +0.0008 | no |
| CPU used (cores), mean | 0.8598 | 0.8615 | +0.2% | −0.0162 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0 | 0.00484 | +0.005 (native is 0) | +0.0041 to +0.0056 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8598 | 0.8663 | +0.8% | −0.0114 to +0.0244 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.3 | 730.7 | −0.2% | −16.7810 to +13.6411 | no |
| HPA replicas, mean | 8.81 | 9.065 | +2.9% | −0.1625 to +0.6722 | no |
| pods started | 4.7 | 5.9 | +25.5% | −0.0064 to +2.4064 | no |
| pod start wait, total (s) | 6.3 | 8.3 | +31.7% | +0.2157 to +3.7843 | yes: LOSS |
| pod start wait, mean (s) | 1.368 | 1.418 | +3.7% | −0.3113 to +0.4113 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.74 | +1.5% | −0.1431 to +0.9011 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.516 | +0.2% | −0.0046 to +0.0113 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.6 | −0.3% | −1.3226 to +0.4012 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.6 | −0.3% | −1.3226 to +0.4012 | no |
| response time (ms), mean | 104.7 | 104.9 | +0.2% | −2.0406 to +2.4758 | no |
| response time (ms), 95th percentile | 218.5 | 218.1 | −0.2% | −9.9379 to +9.1119 | no |
| response time (ms), 99th percentile | 304.1 | 313.3 | +3.0% | −6.3437 to +24.7615 | no |
| time over the response line (% of samples) | 0.08886 | 0.1147 | +29.1% | −0.0776 to +0.1293 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.025 | −68.8% | −0.1349 to +0.0249 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03589 | −9.5% | −0.0047 to −0.0028 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.952 | 0.8615 | −9.5% | −0.1133 to −0.0677 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00484 | +0.005 (native is 0) | +0.0041 to +0.0056 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.952 | 0.8663 | −9.0% | −0.1081 to −0.0632 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 730.7 | +9.7% | +50.2909 to +79.4295 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.828 | 9.065 | +2.7% | −0.1837 to +0.6586 | no |
| pods started | 4.9 | 5.9 | +20.4% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 6.8 | 8.3 | +22.1% | +0.5921 to +2.4079 | yes: LOSS |
| pod start wait, mean (s) | 1.403 | 1.418 | +1.1% | −0.2852 to +0.3152 | no |
| host CPU busy, the real machine under kind (%) | 28.64 | 25.74 | −10.1% | −3.6742 to −2.1210 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.513 | −0.2% | −0.0121 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 159.2 | +0.3% | −0.3884 to +1.4375 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 159.2 | +0.3% | −0.3884 to +1.4375 | no |
| response time (ms), mean | 104.8 | 106.8 | +2.0% | −0.4222 to +4.5925 | no |
| response time (ms), 95th percentile | 220.9 | 219.2 | −0.8% | −10.0810 to +6.7060 | no |
| response time (ms), 99th percentile | 325.7 | 307.5 | −5.6% | −37.1904 to +0.7016 | no |
| time over the response line (% of samples) | 0.08974 | 0.1032 | +15.0% | −0.0553 to +0.0822 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.9 | +0.900 (native is 0) | −0.6977 to +2.4977 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1567 | +0.157 (native is 0) | +0.0001 to +0.3132 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03582 | 0.03988 | +11.3% | +0.0030 to +0.0051 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8598 | 0.9571 | +11.3% | +0.0718 to +0.1228 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00777 | +0.008 (native is 0) | +0.0058 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8598 | 0.9649 | +12.2% | +0.0782 to +0.1321 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.3 | 662.8 | −9.5% | −83.6147 to −55.4506 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.81 | 9.288 | +5.4% | −0.3317 to +1.2871 | no |
| pods started | 4.7 | 6 | +27.7% | −0.4538 to +3.0538 | no |
| pod start wait, total (s) | 6.3 | 8.6 | +36.5% | −0.7169 to +5.3169 | no |
| pod start wait, mean (s) | 1.368 | 1.38 | +0.9% | −0.2209 to +0.2444 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 29.26 | +15.4% | +2.9417 to +4.8571 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*