# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.512 | 1.511 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 159.3 | 158.4 | 160.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 159.3 | 158.4 | 160.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 123.2 | 126.9 | 123.4 | 125.9 |
| response time (ms), 95th percentile | 252.1 | 262 | 251.5 | 253.8 |
| response time (ms), 99th percentile | 350.1 | 357.2 | 362.6 | 364.8 |
| time over the response line (% of samples) | 0.08854 | 0.1785 | 0.1786 | 0.216 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0.6 | 0.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.02667 | 0.1033 | 0.1867 |
| utilisation (used / allocatable) | 0.03674 | 0.04066 | 0.0366 | 0.04089 |
| CPU used (cores), mean | 0.8817 | 0.9759 | 0.8784 | 0.9813 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0049 | 0.00783 |
| CPU used with Omni's own (cores), mean | 0.8817 | 0.9759 | 0.8833 | 0.9892 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.9 | 648.9 | 717.6 | 646.1 |
| HPA replicas, mean | 8.856 | 8.844 | 9.099 | 9.314 |
| pods started | 4.7 | 5 | 5.8 | 5.7 |
| pod start wait, total (s) | 7 | 6.3 | 9.4 | 8.3 |
| pod start wait, mean (s) | 1.455 | 1.262 | 1.645 | 1.432 |
| host CPU busy, the real machine under kind (%) | 25.98 | 29.28 | 26.11 | 29.99 |
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

Omni-Compass stayed native in 7 of 10 repetitions (repetitions 2, 3, 4, 6, 7, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.519 | +0.5% | +0.0001 to +0.0142 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 160.2 | +0.5% | +0.1076 to +1.5541 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 160.2 | +0.5% | +0.1076 to +1.5541 | yes: power given |
| response time (ms), mean | 126.9 | 125.9 | −0.8% | −3.3840 to +1.4301 | no |
| response time (ms), 95th percentile | 262 | 253.8 | −3.1% | −19.0783 to +2.6193 | no |
| response time (ms), 99th percentile | 357.2 | 364.8 | +2.1% | −11.7583 to +27.0045 | no |
| time over the response line (% of samples) | 0.1785 | 0.216 | +21.1% | −0.0853 to +0.1605 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1867 | +600.0% | −0.0009 to +0.3209 | no |
| utilisation (used / allocatable) | 0.04066 | 0.04089 | +0.6% | −0.0003 to +0.0007 | no |
| CPU used (cores), mean | 0.9759 | 0.9813 | +0.6% | −0.0068 to +0.0177 | no |
| Omni's own CPU (cores), mean | 0 | 0.00783 | +0.008 (native is 0) | +0.0065 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9759 | 0.9892 | +1.4% | +0.0004 to +0.0262 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 648.9 | 646.1 | −0.4% | −10.7579 to +5.0824 | no |
| HPA replicas, mean | 8.844 | 9.314 | +5.3% | −0.0381 to +0.9777 | no |
| pods started | 5 | 5.7 | +14.0% | −0.5181 to +1.9181 | no |
| pod start wait, total (s) | 6.3 | 8.3 | +31.7% | −0.8413 to +4.8413 | no |
| pod start wait, mean (s) | 1.262 | 1.432 | +13.5% | −0.1625 to +0.5030 | no |
| host CPU busy, the real machine under kind (%) | 29.28 | 29.99 | +2.4% | +0.3215 to +1.0912 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0113 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 159.3 | +0.5% | −0.2054 to +1.6710 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 159.3 | +0.5% | −0.2054 to +1.6710 | no |
| response time (ms), mean | 123.2 | 126.9 | +3.0% | +0.8372 to +6.4587 | yes: LOSS |
| response time (ms), 95th percentile | 252.1 | 262 | +3.9% | +1.3688 to +18.5322 | yes: LOSS |
| response time (ms), 99th percentile | 350.1 | 357.2 | +2.0% | −6.9871 to +21.1807 | no |
| time over the response line (% of samples) | 0.08854 | 0.1785 | +101.6% | +0.0027 to +0.1771 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.02667 | +6.7% | −0.0855 to +0.0888 | no |
| utilisation (used / allocatable) | 0.03674 | 0.04066 | +10.7% | +0.0033 to +0.0046 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8817 | 0.9759 | +10.7% | +0.0780 to +0.1104 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8817 | 0.9759 | +10.7% | +0.0780 to +0.1104 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.9 | 648.9 | −9.1% | −75.2528 to −54.7264 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.856 | 8.844 | −0.1% | −0.2043 to +0.1814 | no |
| pods started | 4.7 | 5 | +6.4% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 7 | 6.3 | −10.0% | −3.1093 to +1.7093 | no |
| pod start wait, mean (s) | 1.455 | 1.262 | −13.3% | −0.5279 to +0.1412 | no |
| host CPU busy, the real machine under kind (%) | 25.98 | 29.28 | +12.7% | +2.7760 to +3.8266 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | −0.2% | −0.0084 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.4 | −0.2% | −0.8928 to +0.4104 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.4 | −0.2% | −0.8928 to +0.4104 | no |
| response time (ms), mean | 123.2 | 123.4 | +0.1% | −3.0863 to +3.4227 | no |
| response time (ms), 95th percentile | 252.1 | 251.5 | −0.2% | −10.2948 to +9.2438 | no |
| response time (ms), 99th percentile | 350.1 | 362.6 | +3.6% | −7.3924 to +32.2576 | no |
| time over the response line (% of samples) | 0.08854 | 0.1786 | +101.7% | −0.0814 to +0.2616 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1033 | +313.3% | −0.0119 to +0.1686 | no |
| utilisation (used / allocatable) | 0.03674 | 0.0366 | −0.4% | −0.0011 to +0.0008 | no |
| CPU used (cores), mean | 0.8817 | 0.8784 | −0.4% | −0.0252 to +0.0186 | no |
| Omni's own CPU (cores), mean | 0 | 0.0049 | +0.005 (native is 0) | +0.0042 to +0.0056 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8817 | 0.8833 | +0.2% | −0.0207 to +0.0239 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.9 | 717.6 | +0.5% | −12.2612 to +19.6109 | no |
| HPA replicas, mean | 8.856 | 9.099 | +2.8% | −0.3053 to +0.7925 | no |
| pods started | 4.7 | 5.8 | +23.4% | −0.4249 to +2.6249 | no |
| pod start wait, total (s) | 7 | 9.4 | +34.3% | −0.8727 to +5.6727 | no |
| pod start wait, mean (s) | 1.455 | 1.645 | +13.1% | −0.2289 to +0.6089 | no |
| host CPU busy, the real machine under kind (%) | 25.98 | 26.11 | +0.5% | −0.5977 to +0.8579 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.511 | −0.0% | −0.0099 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.4 | −0.6% | −1.9801 to +0.0321 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.4 | −0.6% | −1.9801 to +0.0321 | no |
| response time (ms), mean | 126.9 | 123.4 | −2.7% | −5.5909 to −1.3686 | yes: GAIN |
| response time (ms), 95th percentile | 262 | 251.5 | −4.0% | −23.1758 to +2.2238 | no |
| response time (ms), 99th percentile | 357.2 | 362.6 | +1.5% | −8.6086 to +19.2802 | no |
| time over the response line (% of samples) | 0.1785 | 0.1786 | +0.1% | −0.1034 to +0.1037 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1033 | +287.5% | −0.0750 to +0.2283 | no |
| utilisation (used / allocatable) | 0.04066 | 0.0366 | −10.0% | −0.0046 to −0.0035 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9759 | 0.8784 | −10.0% | −0.1112 to −0.0838 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0049 | +0.005 (native is 0) | +0.0042 to +0.0056 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9759 | 0.8833 | −9.5% | −0.1067 to −0.0786 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 648.9 | 717.6 | +10.6% | +57.1647 to +80.1643 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.844 | 9.099 | +2.9% | −0.3183 to +0.8284 | no |
| pods started | 5 | 5.8 | +16.0% | −0.5403 to +2.1403 | no |
| pod start wait, total (s) | 6.3 | 9.4 | +49.2% | +0.9554 to +5.2446 | yes: LOSS |
| pod start wait, mean (s) | 1.262 | 1.645 | +30.4% | +0.1304 to +0.6363 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.28 | 26.11 | −10.8% | −3.5622 to −2.7802 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.519 | +0.4% | −0.0035 to +0.0145 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 160.2 | +1.0% | +0.6112 to +2.5160 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 160.2 | +1.0% | +0.6112 to +2.5160 | yes: power given |
| response time (ms), mean | 123.2 | 125.9 | +2.2% | −0.2843 to +5.6263 | no |
| response time (ms), 95th percentile | 252.1 | 253.8 | +0.7% | −7.1934 to +10.6354 | no |
| response time (ms), 99th percentile | 350.1 | 364.8 | +4.2% | −11.7105 to +41.1503 | no |
| time over the response line (% of samples) | 0.08854 | 0.216 | +144.0% | −0.0286 to +0.2836 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1867 | +646.7% | −0.0605 to +0.3838 | no |
| utilisation (used / allocatable) | 0.03674 | 0.04089 | +11.3% | +0.0033 to +0.0050 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8817 | 0.9813 | +11.3% | +0.0800 to +0.1193 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00783 | +0.008 (native is 0) | +0.0065 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8817 | 0.9892 | +12.2% | +0.0871 to +0.1279 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.9 | 646.1 | −9.5% | −79.4220 to −56.2328 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.856 | 9.314 | +5.2% | +0.0079 to +0.9088 | yes: power given |
| pods started | 4.7 | 5.7 | +21.3% | −0.3903 to +2.3903 | no |
| pod start wait, total (s) | 7 | 8.3 | +18.6% | −1.5622 to +4.1622 | no |
| pod start wait, mean (s) | 1.455 | 1.432 | −1.6% | −0.2856 to +0.2395 | no |
| host CPU busy, the real machine under kind (%) | 25.98 | 29.99 | +15.4% | +3.2341 to +4.7812 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*