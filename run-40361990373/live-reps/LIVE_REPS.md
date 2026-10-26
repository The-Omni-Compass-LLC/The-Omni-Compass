# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.331 | 5.245 |
| node-hours | 2.517 | 2.514 | 2.232 | 2.196 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.3 | 271.9 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.3 | 250.9 | 248 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 340.7 | 353.1 | 343.6 | 341.4 |
| response time (ms), 95th percentile | 1219 | 1365 | 1209 | 1247 |
| response time (ms), 99th percentile | 1857 | 2125 | 1876 | 2013 |
| time over the response line (% of samples) | 16.37 | 15.12 | 16.43 | 15.26 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 | 9.9 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 11.2 | 10.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.917 | 12.33 | 11.32 | 11.57 |
| utilisation (used / allocatable) | 0.06072 | 0.06104 | 0.06756 | 0.06812 |
| CPU used (cores), mean | 1.457 | 1.465 | 1.436 | 1.427 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01201 | 0.01389 |
| CPU used with Omni's own (cores), mean | 1.457 | 1.465 | 1.448 | 1.441 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453 | 450.2 | 420.1 | 418.1 |
| HPA replicas, mean | 2.122 | 2.1 | 2.119 | 2.096 |
| pods started | 0 | 0 | 0.1 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 0.1 | 0.2 |
| pod start wait, mean (s) | 0 | 0 | 0.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 41.68 | 42.68 | 42.39 | 43.3 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.7 | 782.3 | 781.7 | 783.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.737 | 4.591 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2083 | 0.06667 | 0.2167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | 0.4 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 84.46 | 93.74 | 88.04 | 94.63 |
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
| worker nodes in service, mean | 6 | 5.245 | −12.6% | −1.3802 to −0.1298 | yes: GAIN |
| node-hours | 2.514 | 2.196 | −12.6% | −0.5793 to −0.0566 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.7 | −0.2% | −1.7916 to +0.6628 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 248 | −8.9% | −44.2499 to −4.2414 | yes: GAIN |
| response time (ms), mean | 353.1 | 341.4 | −3.3% | −28.2649 to +4.7137 | no |
| response time (ms), 95th percentile | 1365 | 1247 | −8.7% | −290.6388 to +54.4498 | no |
| response time (ms), 99th percentile | 2125 | 2013 | −5.3% | −331.5901 to +106.7671 | no |
| time over the response line (% of samples) | 15.12 | 15.26 | +0.9% | −0.8498 to +1.1267 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.4 | −2.1% | −0.9388 to +0.5388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.900 (native is 0) | +9.0701 to +12.7299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.33 | 11.56 | −6.2% | −2.6633 to +1.1299 | no |
| utilisation (used / allocatable) | 0.06104 | 0.06812 | +11.6% | +0.0013 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.427 | −2.6% | −0.0787 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0 | 0.01389 | +0.014 (native is 0) | +0.0114 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.441 | −1.7% | −0.0653 to +0.0169 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.2 | 418.1 | −7.1% | −58.1751 to −5.8712 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.1 | 2.096 | −0.2% | −0.1164 to +0.1078 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 42.68 | 43.3 | +1.4% | +0.2221 to +1.0149 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 783.9 | +0.2% | −2.1275 to +5.3275 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.591 | −23.5% | −2.5304 to −0.2876 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2083 | 0.2167 | +4.0% | −0.0696 to +0.0863 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.8 | −20.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.74 | 94.63 | +1.0% | −2.6163 to +4.3996 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0116 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.3 | −0.1% | −1.2691 to +0.7424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.3 | −0.1% | −1.2691 to +0.7424 | no |
| response time (ms), mean | 340.7 | 353.1 | +3.7% | −5.8223 to +30.7387 | no |
| response time (ms), 95th percentile | 1219 | 1365 | +11.9% | −30.7389 to +321.7599 | no |
| response time (ms), 99th percentile | 1857 | 2125 | +14.4% | −38.1959 to +574.1495 | no |
| time over the response line (% of samples) | 16.37 | 15.12 | −7.6% | −2.2875 to −0.2019 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 | ±0.0% | −1.5816 to +1.5816 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.917 | 12.33 | +24.4% | −0.1537 to +4.9837 | no |
| utilisation (used / allocatable) | 0.06072 | 0.06104 | +0.5% | −0.0002 to +0.0009 | no |
| CPU used (cores), mean | 1.457 | 1.465 | +0.5% | −0.0052 to +0.0206 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.457 | 1.465 | +0.5% | −0.0052 to +0.0206 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453 | 450.2 | −0.6% | −7.3220 to +1.7241 | no |
| HPA replicas, mean | 2.122 | 2.1 | −1.0% | −0.2357 to +0.1923 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.68 | 42.68 | +2.4% | +0.7242 to +1.2689 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.7 | 782.3 | +0.7% | −0.2229 to +11.4229 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2083 | +150.0% | +0.0606 to +0.1894 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | +66.7% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 84.46 | 93.74 | +11.0% | +2.3717 to +16.1867 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.331 | −11.2% | −1.2380 to −0.1009 | yes: GAIN |
| node-hours | 2.517 | 2.232 | −11.3% | −0.5191 to −0.0504 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 271.9 | −0.2% | −1.2977 to +0.0439 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 250.9 | −7.9% | −39.2476 to −4.0687 | yes: GAIN |
| response time (ms), mean | 340.7 | 343.6 | +0.8% | −13.1096 to +18.8681 | no |
| response time (ms), 95th percentile | 1219 | 1209 | −0.8% | −63.0164 to +43.3324 | no |
| response time (ms), 99th percentile | 1857 | 1876 | +1.0% | −165.5435 to +202.5707 | no |
| time over the response line (% of samples) | 16.37 | 16.43 | +0.4% | −0.4830 to +0.6023 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.9 | +3.1% | −0.5953 to +1.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 | +11.200 (native is 0) | +9.0199 to +13.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.917 | 11.32 | +14.1% | −0.3322 to +3.1356 | no |
| utilisation (used / allocatable) | 0.06072 | 0.06756 | +11.3% | +0.0004 to +0.0133 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.457 | 1.436 | −1.5% | −0.0410 to −0.0019 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01201 | +0.012 (native is 0) | +0.0108 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.448 | −0.6% | −0.0295 to +0.0107 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453 | 420.1 | −7.2% | −65.4431 to −0.1658 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.122 | 2.119 | −0.1% | −0.2004 to +0.1951 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 41.68 | 42.39 | +1.7% | +0.3607 to +1.0650 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.7 | 781.7 | +0.6% | −0.7621 to +10.7621 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.737 | −21.1% | −2.2631 to −0.2631 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.06667 | −20.0% | −0.0782 to +0.0449 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.46 | 88.04 | +4.2% | −3.1936 to +10.3602 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.331 | −11.2% | −1.2380 to −0.1009 | yes: GAIN |
| node-hours | 2.514 | 2.232 | −11.2% | −0.5189 to −0.0446 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.9 | −0.1% | −1.2013 to +0.4742 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 250.9 | −7.9% | −39.3821 to −3.4076 | yes: GAIN |
| response time (ms), mean | 353.1 | 343.6 | −2.7% | −31.2341 to +12.0762 | no |
| response time (ms), 95th percentile | 1365 | 1209 | −11.4% | −340.4155 to +29.7105 | no |
| response time (ms), 99th percentile | 2125 | 1876 | −11.7% | −558.0151 to +59.0887 | no |
| time over the response line (% of samples) | 15.12 | 16.43 | +8.6% | +0.1858 to +2.4229 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.9 | +3.1% | −1.1717 to +1.7717 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 | +11.200 (native is 0) | +9.0199 to +13.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.33 | 11.32 | −8.2% | −3.5007 to +1.4740 | no |
| utilisation (used / allocatable) | 0.06104 | 0.06756 | +10.7% | +0.0002 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.436 | −2.0% | −0.0568 to −0.0015 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01201 | +0.012 (native is 0) | +0.0108 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.448 | −1.2% | −0.0452 to +0.0109 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.2 | 420.1 | −6.7% | −61.4179 to +1.4070 | no |
| HPA replicas, mean | 2.1 | 2.119 | +0.9% | −0.2225 to +0.2606 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 42.68 | 42.39 | −0.7% | −0.6930 to +0.1257 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 781.7 | −0.1% | −7.1749 to +5.9749 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.737 | −21.1% | −2.2631 to −0.2631 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2083 | 0.06667 | −68.0% | −0.2226 to −0.0607 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.4 | −60.0% | −0.9694 to −0.2306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 93.74 | 88.04 | −6.1% | −12.9027 to +1.5111 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.245 | −12.6% | −1.3802 to −0.1298 | yes: GAIN |
| node-hours | 2.517 | 2.196 | −12.8% | −0.5805 to −0.0613 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 271.7 | −0.3% | −1.8316 to +0.1761 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 248 | −9.0% | −44.1759 to −4.8421 | yes: GAIN |
| response time (ms), mean | 340.7 | 341.4 | +0.2% | −7.1204 to +8.4856 | no |
| response time (ms), 95th percentile | 1219 | 1247 | +2.2% | −46.0321 to +100.8641 | no |
| response time (ms), 99th percentile | 1857 | 2013 | +8.4% | −48.3250 to +359.4556 | no |
| time over the response line (% of samples) | 16.37 | 15.26 | −6.8% | −2.2126 to +0.0001 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.4 | −2.1% | −1.9779 to +1.5779 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.900 (native is 0) | +9.0701 to +12.7299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.917 | 11.57 | +16.6% | −0.6181 to +3.9148 | no |
| utilisation (used / allocatable) | 0.06072 | 0.06812 | +12.2% | +0.0014 to +0.0134 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.457 | 1.427 | −2.1% | −0.0623 to +0.0016 | no |
| Omni's own CPU (cores), mean | 0 | 0.01389 | +0.014 (native is 0) | +0.0114 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.441 | −1.1% | −0.0489 to +0.0159 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453 | 418.1 | −7.7% | −63.4865 to −6.1577 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.122 | 2.096 | −1.2% | −0.2511 to +0.1991 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 41.68 | 43.3 | +3.9% | +1.3186 to +1.9115 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.7 | 783.9 | +0.9% | +1.8069 to +12.5931 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.591 | −23.5% | −2.5304 to −0.2876 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2167 | +160.0% | +0.0566 to +0.2100 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.46 | 94.63 | +12.0% | +3.6000 to +16.7417 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*