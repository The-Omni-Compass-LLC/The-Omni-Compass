# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.92 | 4.754 |
| node-hours | 2.514 | 2.514 | 2.061 | 1.994 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270 | 270.2 | 269.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 270 | 236.3 | 230.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 236.3 | 236 | 238.7 | 236.2 |
| response time (ms), 95th percentile | 756.6 | 788 | 788.4 | 782.2 |
| response time (ms), 99th percentile | 1172 | 1242 | 1206 | 1302 |
| time over the response line (% of samples) | 10.08 | 9.485 | 10.33 | 9.545 |
| failed requests (%) | 0 | 0.01961 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.7 | 7.7 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 9.8 | 12.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.892 | 9.603 | 8.342 | 9.137 |
| utilisation (used / allocatable) | 0.05593 | 0.05462 | 0.06766 | 0.06653 |
| CPU used (cores), mean | 1.342 | 1.311 | 1.306 | 1.256 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0108 | 0.0117 |
| CPU used with Omni's own (cores), mean | 1.342 | 1.311 | 1.316 | 1.268 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 500.9 | 432.9 | 442.5 |
| HPA replicas, mean | 1.976 | 2.11 | 2.146 | 2.018 |
| pods started | 0.1 | 0 | 0.1 | 0.2 |
| pod start wait, total (s) | 0.2 | 0 | 0.1 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0 | 0.1 | 0.4 |
| host CPU busy, the real machine under kind (%) | 38.3 | 38.89 | 38.75 | 39.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 748.3 | 751.1 | 748.7 | 751.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.197 | 3.781 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.2708 | 0.03333 | 0.1667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | 0.1 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 55.67 | 60.16 | 55.77 | 60.45 |
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
| worker nodes in service, mean | 6 | 4.754 | −20.8% | −2.0050 to −0.4872 | yes: GAIN |
| node-hours | 2.514 | 1.994 | −20.7% | −0.8418 to −0.1980 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 269.8 | −0.1% | −1.5996 to +1.0421 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 230.6 | −14.6% | −64.1193 to −14.7006 | yes: GAIN |
| response time (ms), mean | 236 | 236.2 | +0.1% | −10.4566 to +10.7457 | no |
| response time (ms), 95th percentile | 788 | 782.2 | −0.7% | −42.7139 to +31.1929 | no |
| response time (ms), 99th percentile | 1242 | 1302 | +4.9% | −113.2601 to +233.7421 | no |
| time over the response line (% of samples) | 9.485 | 9.545 | +0.6% | −0.4101 to +0.5304 | no |
| failed requests (%) | 0.01961 | 0 | −100.0% | −0.0640 to +0.0247 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 7 | +4.5% | −0.7144 to +1.3144 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 | +12.300 (native is 0) | +8.3238 to +16.2762 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 9.137 | −4.9% | −1.6581 to +0.7248 | no |
| utilisation (used / allocatable) | 0.05462 | 0.06653 | +21.8% | +0.0051 to +0.0187 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.311 | 1.256 | −4.2% | −0.1086 to −0.0004 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0117 | +0.012 (native is 0) | +0.0099 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.311 | 1.268 | −3.3% | −0.0983 to +0.0128 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.9 | 442.5 | −11.7% | −93.3468 to −23.5325 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.11 | 2.018 | −4.4% | −0.2107 to +0.0259 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 38.89 | 39.37 | +1.2% | −0.0034 to +0.9578 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.1 | 751.5 | +0.1% | −5.6995 to +6.4995 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.781 | −37.0% | −3.4981 to −0.9390 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2708 | 0.1667 | −38.5% | −0.4501 to +0.2418 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.16 | 60.45 | +0.5% | −5.3395 to +5.9145 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.514 | +0.0% | −0.0053 to +0.0066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270 | −0.2% | −1.1778 to +0.3306 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 270 | −0.2% | −1.1778 to +0.3306 | no |
| response time (ms), mean | 236.3 | 236 | −0.1% | −14.5856 to +14.0764 | no |
| response time (ms), 95th percentile | 756.6 | 788 | +4.1% | −57.0767 to +119.8697 | no |
| response time (ms), 99th percentile | 1172 | 1242 | +5.9% | −120.2676 to +259.4692 | no |
| time over the response line (% of samples) | 10.08 | 9.485 | −5.9% | −1.5453 to +0.3467 | no |
| failed requests (%) | 0 | 0.01961 | +0.020 (native is 0) | −0.0247 to +0.0640 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.7 | +1.5% | −0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.892 | 9.603 | +21.7% | +0.6067 to +2.8166 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05593 | 0.05462 | −2.3% | −0.0030 to +0.0004 | no |
| CPU used (cores), mean | 1.342 | 1.311 | −2.3% | −0.0710 to +0.0085 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.342 | 1.311 | −2.3% | −0.0710 to +0.0085 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 500.9 | +2.8% | −4.2958 to +31.2941 | no |
| HPA replicas, mean | 1.976 | 2.11 | +6.8% | −0.0163 to +0.2839 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 38.89 | +1.5% | +0.1515 to +1.0304 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.3 | 751.1 | +0.4% | −1.8577 to +7.4577 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.2708 | +550.0% | −0.1469 to +0.6052 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | −0.0058 to +1.0058 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.67 | 60.16 | +8.1% | −0.5271 to +9.5021 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.92 | −18.0% | −1.9003 to −0.2604 | yes: GAIN |
| node-hours | 2.514 | 2.061 | −18.0% | −0.7943 to −0.1106 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.2 | −0.1% | −0.9797 to +0.5373 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 236.3 | −12.6% | −60.1495 to −8.1846 | yes: GAIN |
| response time (ms), mean | 236.3 | 238.7 | +1.0% | −6.3218 to +11.1672 | no |
| response time (ms), 95th percentile | 756.6 | 788.4 | +4.2% | −31.6354 to +95.3654 | no |
| response time (ms), 99th percentile | 1172 | 1206 | +2.9% | −24.0599 to +91.6263 | no |
| time over the response line (% of samples) | 10.08 | 10.33 | +2.4% | −0.5120 to +0.9957 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.7 | +16.7% | −0.2676 to +2.4676 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 | +9.800 (native is 0) | +6.3811 to +13.2189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.892 | 8.342 | +5.7% | −1.4046 to +2.3046 | no |
| utilisation (used / allocatable) | 0.05593 | 0.06766 | +21.0% | +0.0032 to +0.0203 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.342 | 1.306 | −2.7% | −0.0841 to +0.0110 | no |
| Omni's own CPU (cores), mean | 0 | 0.0108 | +0.011 (native is 0) | +0.0091 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.342 | 1.316 | −1.9% | −0.0742 to +0.0227 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 432.9 | −11.2% | −93.2695 to −15.7148 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.146 | +8.6% | −0.0284 to +0.3686 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 38.75 | +1.2% | −0.0052 to +0.9127 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.3 | 748.7 | +0.1% | −3.1558 to +3.9558 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.197 | −30.0% | −3.1061 to −0.4991 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.03333 | −20.0% | −0.0545 to +0.0378 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.1 | −66.7% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.67 | 55.77 | +0.2% | −2.2556 to +2.4472 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.92 | −18.0% | −1.9003 to −0.2604 | yes: GAIN |
| node-hours | 2.514 | 2.061 | −18.0% | −0.7996 to −0.1067 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 270.2 | +0.1% | −0.6238 to +1.0286 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 236.3 | −12.5% | −59.9098 to −7.5772 | yes: GAIN |
| response time (ms), mean | 236 | 238.7 | +1.1% | −5.4689 to +10.8234 | no |
| response time (ms), 95th percentile | 788 | 788.4 | +0.1% | −43.6650 to +44.6020 | no |
| response time (ms), 99th percentile | 1242 | 1206 | −2.9% | −196.2362 to +124.6010 | no |
| time over the response line (% of samples) | 9.485 | 10.33 | +8.9% | +0.0949 to +1.5873 | yes: LOSS |
| failed requests (%) | 0.01961 | 0 | −100.0% | −0.0640 to +0.0247 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 7.7 | +14.9% | −0.0663 to +2.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.8 | +9.800 (native is 0) | +6.3811 to +13.2189 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.603 | 8.342 | −13.1% | −3.5602 to +1.0369 | no |
| utilisation (used / allocatable) | 0.05462 | 0.06766 | +23.9% | +0.0036 to +0.0225 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.311 | 1.306 | −0.4% | −0.0362 to +0.0257 | no |
| Omni's own CPU (cores), mean | 0 | 0.0108 | +0.011 (native is 0) | +0.0091 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.311 | 1.316 | +0.4% | −0.0259 to +0.0370 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.9 | 432.9 | −13.6% | −117.8961 to −18.0864 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.11 | 2.146 | +1.7% | −0.1156 to +0.1881 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 38.89 | 38.75 | −0.4% | −0.6588 to +0.3844 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.1 | 748.7 | −0.3% | −10.0760 to +5.2760 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.197 | −30.0% | −3.1061 to −0.4991 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2708 | 0.03333 | −87.7% | −0.5993 to +0.1243 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.1 | −87.5% | −1.0455 to −0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 60.16 | 55.77 | −7.3% | −11.1160 to +2.3327 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.754 | −20.8% | −2.0050 to −0.4872 | yes: GAIN |
| node-hours | 2.514 | 1.994 | −20.7% | −0.8377 to −0.2008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 269.8 | −0.3% | −2.1359 to +0.7313 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 230.6 | −14.7% | −64.4322 to −15.2349 | yes: GAIN |
| response time (ms), mean | 236.3 | 236.2 | −0.0% | −8.7999 to +8.5798 | no |
| response time (ms), 95th percentile | 756.6 | 782.2 | +3.4% | −40.5815 to +91.8535 | no |
| response time (ms), 99th percentile | 1172 | 1302 | +11.1% | −9.7940 to +269.4776 | no |
| time over the response line (% of samples) | 10.08 | 9.545 | −5.3% | −1.7661 to +0.6877 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7 | +6.1% | −0.7285 to +1.5285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 | +12.300 (native is 0) | +8.3238 to +16.2762 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.892 | 9.137 | +15.8% | −0.2449 to +2.7349 | no |
| utilisation (used / allocatable) | 0.05593 | 0.06653 | +19.0% | +0.0042 to +0.0170 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.342 | 1.256 | −6.4% | −0.1597 to −0.0117 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0117 | +0.012 (native is 0) | +0.0099 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.342 | 1.268 | −5.5% | −0.1495 to +0.0015 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 442.5 | −9.2% | −73.0458 to −16.8353 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.018 | +2.1% | −0.1148 to +0.1977 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 38.3 | 39.37 | +2.8% | +0.6609 to +1.4755 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.3 | 751.5 | +0.4% | −0.7295 to +7.1295 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.781 | −37.0% | −3.4981 to −0.9390 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1667 | +300.0% | +0.0743 to +0.1757 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.9 | +200.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.67 | 60.45 | +8.6% | −0.3151 to +9.8651 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*