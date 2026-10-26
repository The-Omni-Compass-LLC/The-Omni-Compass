# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.512 | 1.52 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.7 | 159.7 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.7 | 159.7 | 160.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 143.7 | 147.2 | 141.4 | 147 |
| response time (ms), 95th percentile | 295.6 | 293.3 | 281.4 | 290.3 |
| response time (ms), 99th percentile | 407 | 405.9 | 388.1 | 393.5 |
| time over the response line (% of samples) | 0.3331 | 0.3599 | 0.2813 | 0.2999 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | 0.1 | 0.1111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2 | 1.889 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1067 | 0.2667 | 0.1519 |
| utilisation (used / allocatable) | 0.03847 | 0.04252 | 0.03878 | 0.04301 |
| CPU used (cores), mean | 0.9234 | 1.021 | 0.9308 | 1.032 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00578 | 0.0098 |
| CPU used with Omni's own (cores), mean | 0.9234 | 1.021 | 0.9366 | 1.042 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.3 | 622.5 | 679 | 616.1 |
| HPA replicas, mean | 8.886 | 8.973 | 10.2 | 10.22 |
| pods started | 4.8 | 4.2 | 7.2 | 7 |
| pod start wait, total (s) | 7.3 | 6 | 11.8 | 12.89 |
| pod start wait, mean (s) | 1.533 | 1.475 | 1.626 | 1.848 |
| host CPU busy, the real machine under kind (%) | 26.97 | 30.74 | 27.53 | 31.65 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

Omni-Compass stayed native in 3 of 9 repetitions (repetitions 3, 7, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.518 | +0.4% | −0.0003 to +0.0118 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 160.5 | +0.5% | +0.0791 to +1.5009 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 160.5 | +0.5% | +0.0791 to +1.5009 | yes: power given |
| response time (ms), mean | 145.5 | 147 | +1.1% | −1.4064 to +4.4687 | no |
| response time (ms), 95th percentile | 291.7 | 290.3 | −0.5% | −11.2402 to +8.5035 | no |
| response time (ms), 99th percentile | 406.6 | 393.5 | −3.2% | −30.8753 to +4.6913 | no |
| time over the response line (% of samples) | 0.3425 | 0.2999 | −12.4% | −0.2641 to +0.1788 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.889 | +1.889 (native is 0) | +0.5887 to +3.1891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08889 | 0.1519 | +70.8% | −0.1390 to +0.2649 | no |
| utilisation (used / allocatable) | 0.04234 | 0.04301 | +1.6% | +0.0001 to +0.0012 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.016 | 1.032 | +1.6% | +0.0029 to +0.0293 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0098 | +0.010 (native is 0) | +0.0080 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 1.042 | +2.6% | +0.0125 to +0.0393 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 625.1 | 616.1 | −1.4% | −16.3016 to −1.7355 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.966 | 10.22 | +14.0% | +0.3637 to +2.1405 | yes: power given |
| pods started | 4.222 | 7 | +65.8% | +0.4155 to +5.1400 | yes: power given |
| pod start wait, total (s) | 6.222 | 12.89 | +107.1% | +1.9910 to +11.3423 | yes: LOSS |
| pod start wait, mean (s) | 1.528 | 1.848 | +21.0% | −0.0855 to +0.7262 | no |
| host CPU busy, the real machine under kind (%) | 30.64 | 31.65 | +3.3% | +0.6085 to +1.4121 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | −0.3% | −0.0119 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.7 | +0.3% | −0.3223 to +1.2261 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.7 | +0.3% | −0.3223 to +1.2261 | no |
| response time (ms), mean | 143.7 | 147.2 | +2.4% | −0.7353 to +7.5910 | no |
| response time (ms), 95th percentile | 295.6 | 293.3 | −0.8% | −11.2155 to +6.7195 | no |
| response time (ms), 99th percentile | 407 | 405.9 | −0.3% | −29.5332 to +27.3956 | no |
| time over the response line (% of samples) | 0.3331 | 0.3599 | +8.0% | −0.3141 to +0.3677 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1067 | −32.6% | −0.1707 to +0.0673 | no |
| utilisation (used / allocatable) | 0.03847 | 0.04252 | +10.5% | +0.0032 to +0.0049 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9234 | 1.021 | +10.5% | +0.0774 to +0.1170 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9234 | 1.021 | +10.5% | +0.0774 to +0.1170 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.3 | 622.5 | −8.9% | −70.9955 to −50.4416 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.886 | 8.973 | +1.0% | −0.0560 to +0.2303 | no |
| pods started | 4.8 | 4.2 | −12.5% | −1.4396 to +0.2396 | no |
| pod start wait, total (s) | 7.3 | 6 | −17.8% | −3.1174 to +0.5174 | no |
| pod start wait, mean (s) | 1.533 | 1.475 | −3.8% | −0.4765 to +0.3599 | no |
| host CPU busy, the real machine under kind (%) | 26.97 | 30.74 | +14.0% | +3.1429 to +4.3903 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.519 | +0.2% | +0.0011 to +0.0052 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.7 | +0.3% | +0.0501 to +0.8276 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.7 | +0.3% | +0.0501 to +0.8276 | yes: power given |
| response time (ms), mean | 143.7 | 141.4 | −1.7% | −4.7718 to +0.0105 | no |
| response time (ms), 95th percentile | 295.6 | 281.4 | −4.8% | −22.0152 to −6.4358 | yes: GAIN |
| response time (ms), 99th percentile | 407 | 388.1 | −4.6% | −43.2630 to +5.4630 | no |
| time over the response line (% of samples) | 0.3331 | 0.2813 | −15.5% | −0.2367 to +0.1331 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.2667 | +68.4% | −0.0950 to +0.3117 | no |
| utilisation (used / allocatable) | 0.03847 | 0.03878 | +0.8% | −0.0007 to +0.0013 | no |
| CPU used (cores), mean | 0.9234 | 0.9308 | +0.8% | −0.0159 to +0.0307 | no |
| Omni's own CPU (cores), mean | 0 | 0.00578 | +0.006 (native is 0) | +0.0051 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9234 | 0.9366 | +1.4% | −0.0104 to +0.0368 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.3 | 679 | −0.6% | −19.9800 to +11.4555 | no |
| HPA replicas, mean | 8.886 | 10.2 | +14.8% | +0.5907 to +2.0318 | yes: power given |
| pods started | 4.8 | 7.2 | +50.0% | +0.5469 to +4.2531 | yes: power given |
| pod start wait, total (s) | 7.3 | 11.8 | +61.6% | +1.1407 to +7.8593 | yes: LOSS |
| pod start wait, mean (s) | 1.533 | 1.626 | +6.1% | −0.2426 to +0.4284 | no |
| host CPU busy, the real machine under kind (%) | 26.97 | 27.53 | +2.1% | +0.0353 to +1.0724 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.519 | +0.5% | +0.0007 to +0.0143 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 159.7 | −0.0% | −0.6748 to +0.6487 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 159.7 | −0.0% | −0.6748 to +0.6487 | no |
| response time (ms), mean | 147.2 | 141.4 | −3.9% | −9.9502 to −1.6668 | yes: GAIN |
| response time (ms), 95th percentile | 293.3 | 281.4 | −4.1% | −20.6919 to −3.2631 | yes: GAIN |
| response time (ms), 99th percentile | 405.9 | 388.1 | −4.4% | −47.2286 to +11.5662 | no |
| time over the response line (% of samples) | 0.3599 | 0.2813 | −21.8% | −0.2876 to +0.1304 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.2667 | +150.0% | −0.0813 to +0.4013 | no |
| utilisation (used / allocatable) | 0.04252 | 0.03878 | −8.8% | −0.0044 to −0.0031 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.021 | 0.9308 | −8.8% | −0.1059 to −0.0736 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00578 | +0.006 (native is 0) | +0.0051 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.021 | 0.9366 | −8.2% | −0.0998 to −0.0681 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 622.5 | 679 | +9.1% | +47.0700 to +65.8426 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.973 | 10.2 | +13.6% | +0.5035 to +1.9446 | yes: power given |
| pods started | 4.2 | 7.2 | +71.4% | +0.8942 to +5.1058 | yes: power given |
| pod start wait, total (s) | 6 | 11.8 | +96.7% | +1.7006 to +9.8994 | yes: LOSS |
| pod start wait, mean (s) | 1.475 | 1.626 | +10.3% | −0.2174 to +0.5199 | no |
| host CPU busy, the real machine under kind (%) | 30.74 | 27.53 | −10.5% | −3.5227 to −2.9028 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | −0.0092 to +0.0140 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.5 | +0.8% | +0.1017 to +2.5921 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.5 | +0.8% | +0.1017 to +2.5921 | yes: power given |
| response time (ms), mean | 143.4 | 147 | +2.5% | +0.7948 to +6.5071 | yes: LOSS |
| response time (ms), 95th percentile | 294.9 | 290.3 | −1.6% | −15.1649 to +5.9283 | no |
| response time (ms), 99th percentile | 406.1 | 393.5 | −3.1% | −43.9159 to +18.8448 | no |
| time over the response line (% of samples) | 0.3701 | 0.2999 | −19.0% | −0.3073 to +0.1669 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 0.1111 | ±0.0% | −0.3843 to +0.3843 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.889 | +1.889 (native is 0) | +0.5887 to +3.1891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1463 | 0.1519 | +3.8% | −0.1740 to +0.1851 | no |
| utilisation (used / allocatable) | 0.0383 | 0.04301 | +12.3% | +0.0037 to +0.0057 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9192 | 1.032 | +12.3% | +0.0888 to +0.1374 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0098 | +0.010 (native is 0) | +0.0080 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9192 | 1.042 | +13.4% | +0.0971 to +0.1486 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.2 | 616.1 | −10.2% | −82.3443 to −57.7474 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.873 | 10.22 | +15.2% | +0.4744 to +2.2166 | yes: power given |
| pods started | 4.889 | 7 | +43.2% | +0.2903 to +3.9319 | yes: power given |
| pod start wait, total (s) | 7.444 | 12.89 | +73.1% | +1.8368 to +9.0521 | yes: LOSS |
| pod start wait, mean (s) | 1.537 | 1.848 | +20.2% | +0.0301 to +0.5921 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.86 | 31.65 | +17.8% | +3.9181 to +5.6544 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*