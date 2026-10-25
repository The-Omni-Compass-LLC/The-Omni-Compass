# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.514 | 1.513 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.5 | 160.9 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.5 | 160.9 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 131.4 | 131.4 | 83.06 | 83.28 |
| response time (ms), 95th percentile | 269.5 | 268.3 | 134 | 134.2 |
| response time (ms), 99th percentile | 380.5 | 393.6 | 169.9 | 169.7 |
| time over the response line (% of samples) | 0.1902 | 0.4714 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 22.5 | 25 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0 | 0.08 | 0.16 |
| utilisation (used / allocatable) | 0.03609 | 0.03629 | 0.04731 | 0.04771 |
| CPU used (cores), mean | 0.8662 | 0.871 | 1.135 | 1.145 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00771 | 0.00819 |
| CPU used with Omni's own (cores), mean | 0.8662 | 0.871 | 1.143 | 1.153 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.8 | 722.1 | 564.5 | 559.6 |
| HPA replicas, mean | 8.859 | 9.55 | 9.571 | 10.07 |
| pods started | 5 | 4 | 5.8 | 3.5 |
| pod start wait, total (s) | 7.3 | 6 | 9.3 | 5.6 |
| pod start wait, mean (s) | 1.43 | 1.5 | 1.633 | 1.562 |
| host CPU busy, the real machine under kind (%) | 25.73 | 26.09 | 33.3 | 33.8 |
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

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.511 | −0.2% | −0.0129 to +0.0065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 160.7 | +1.4% | +1.3047 to +3.1479 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 160.7 | +1.4% | +1.3047 to +3.1479 | yes: power given |
| response time (ms), mean | 131.4 | 83.28 | −36.6% | −57.4509 to −38.7833 | yes: GAIN |
| response time (ms), 95th percentile | 268.3 | 134.2 | −50.0% | −150.5177 to −117.6513 | yes: GAIN |
| response time (ms), 99th percentile | 393.6 | 169.7 | −56.9% | −270.2015 to −177.6445 | yes: GAIN |
| time over the response line (% of samples) | 0.4714 | 0 | −100.0% | −0.8108 to −0.1319 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25 | +25.000 (native is 0) | +20.2194 to +29.7806 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.16 | +0.160 (native is 0) | −0.0813 to +0.4013 | no |
| utilisation (used / allocatable) | 0.03629 | 0.04771 | +31.5% | +0.0098 to +0.0130 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.871 | 1.145 | +31.5% | +0.2358 to +0.3123 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00819 | +0.008 (native is 0) | +0.0074 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.871 | 1.153 | +32.4% | +0.2436 to +0.3209 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.1 | 559.6 | −22.5% | −179.5055 to −145.3907 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.55 | 10.07 | +5.5% | −0.0347 to +1.0779 | no |
| pods started | 4 | 3.5 | −12.5% | −1.5796 to +0.5796 | no |
| pod start wait, total (s) | 6 | 5.6 | −6.7% | −2.7891 to +1.9891 | no |
| pod start wait, mean (s) | 1.5 | 1.562 | +4.1% | −0.2995 to +0.4229 | no |
| host CPU busy, the real machine under kind (%) | 26.09 | 33.8 | +29.5% | +6.6753 to +8.7354 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.514 | +0.0% | −0.0049 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.5 | +0.1% | −0.4682 to +0.6659 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.5 | +0.1% | −0.4682 to +0.6659 | no |
| response time (ms), mean | 131.4 | 131.4 | −0.0% | −3.4045 to +3.3556 | no |
| response time (ms), 95th percentile | 269.5 | 268.3 | −0.4% | −12.7396 to +10.3356 | no |
| response time (ms), 99th percentile | 380.5 | 393.6 | +3.4% | −28.9757 to +55.1959 | no |
| time over the response line (% of samples) | 0.1902 | 0.4714 | +147.8% | −0.0006 to +0.5629 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0 | −100.0% | −0.1338 to +0.0271 | no |
| utilisation (used / allocatable) | 0.03609 | 0.03629 | +0.6% | −0.0004 to +0.0008 | no |
| CPU used (cores), mean | 0.8662 | 0.871 | +0.6% | −0.0089 to +0.0184 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8662 | 0.871 | +0.6% | −0.0089 to +0.0184 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.8 | 722.1 | −0.5% | −14.5955 to +7.0570 | no |
| HPA replicas, mean | 8.859 | 9.55 | +7.8% | +0.5639 to +0.8177 | yes: power given |
| pods started | 5 | 4 | −20.0% | −1.5840 to −0.4160 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 6 | −17.8% | −3.1174 to +0.5174 | no |
| pod start wait, mean (s) | 1.43 | 1.5 | +4.9% | −0.2230 to +0.3630 | no |
| host CPU busy, the real machine under kind (%) | 25.73 | 26.09 | +1.4% | +0.1011 to +0.6189 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.513 | −0.0% | −0.0083 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 160.9 | +1.6% | +1.6325 to +3.3517 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 160.9 | +1.6% | +1.6325 to +3.3517 | yes: power given |
| response time (ms), mean | 131.4 | 83.06 | −36.8% | −54.7127 to −42.0097 | yes: GAIN |
| response time (ms), 95th percentile | 269.5 | 134 | −50.3% | −147.3673 to −123.6347 | yes: GAIN |
| response time (ms), 99th percentile | 380.5 | 169.9 | −55.3% | −234.5514 to −186.5014 | yes: GAIN |
| time over the response line (% of samples) | 0.1902 | 0 | −100.0% | −0.3273 to −0.0531 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.5 | +22.500 (native is 0) | +17.6456 to +27.3544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.08 | +50.0% | −0.1404 to +0.1937 | no |
| utilisation (used / allocatable) | 0.03609 | 0.04731 | +31.1% | +0.0095 to +0.0130 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8662 | 1.135 | +31.1% | +0.2271 to +0.3111 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00771 | +0.008 (native is 0) | +0.0068 to +0.0086 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8662 | 1.143 | +32.0% | +0.2342 to +0.3195 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.8 | 564.5 | −22.2% | −179.7941 to −142.8528 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.859 | 9.571 | +8.0% | +0.0301 to +1.3925 | yes: power given |
| pods started | 5 | 5.8 | +16.0% | −0.4526 to +2.0526 | no |
| pod start wait, total (s) | 7.3 | 9.3 | +27.4% | −1.6317 to +5.6317 | no |
| pod start wait, mean (s) | 1.43 | 1.633 | +14.2% | −0.2756 to +0.6819 | no |
| host CPU busy, the real machine under kind (%) | 25.73 | 33.3 | +29.4% | +6.5001 to +8.6348 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.513 | −0.1% | −0.0080 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 160.9 | +1.5% | +1.7276 to +3.0589 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 160.9 | +1.5% | +1.7276 to +3.0589 | yes: power given |
| response time (ms), mean | 131.4 | 83.06 | −36.8% | −57.2208 to −39.4528 | yes: GAIN |
| response time (ms), 95th percentile | 268.3 | 134 | −50.1% | −150.4785 to −118.1195 | yes: GAIN |
| response time (ms), 99th percentile | 393.6 | 169.9 | −56.8% | −271.3552 to −175.9178 | yes: GAIN |
| time over the response line (% of samples) | 0.4714 | 0 | −100.0% | −0.8108 to −0.1319 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.5 | +22.500 (native is 0) | +17.6456 to +27.3544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.080 (native is 0) | −0.0487 to +0.2087 | no |
| utilisation (used / allocatable) | 0.03629 | 0.04731 | +30.3% | +0.0093 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.871 | 1.135 | +30.3% | +0.2222 to +0.3064 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00771 | +0.008 (native is 0) | +0.0068 to +0.0086 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.871 | 1.143 | +31.2% | +0.2293 to +0.3147 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.1 | 564.5 | −21.8% | −176.3151 to −138.7933 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.55 | 9.571 | +0.2% | −0.6962 to +0.7372 | no |
| pods started | 4 | 5.8 | +45.0% | +0.5028 to +3.0972 | yes: power given |
| pod start wait, total (s) | 6 | 9.3 | +55.0% | +0.3983 to +6.2017 | yes: LOSS |
| pod start wait, mean (s) | 1.5 | 1.633 | +8.9% | −0.2349 to +0.5012 | no |
| host CPU busy, the real machine under kind (%) | 26.09 | 33.3 | +27.6% | +6.1610 to +8.2539 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.51 | −0.2% | −0.0123 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 160.7 | +1.5% | +1.4171 to +3.2333 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 160.7 | +1.5% | +1.4171 to +3.2333 | yes: power given |
| response time (ms), mean | 131.4 | 83.28 | −36.6% | −54.9593 to −41.3238 | yes: GAIN |
| response time (ms), 95th percentile | 269.5 | 134.2 | −50.2% | −147.6627 to −122.9103 | yes: GAIN |
| response time (ms), 99th percentile | 380.5 | 169.7 | −55.4% | −232.4091 to −189.2167 | yes: GAIN |
| time over the response line (% of samples) | 0.1902 | 0 | −100.0% | −0.3273 to −0.0531 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25 | +25.000 (native is 0) | +20.2194 to +29.7806 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 | +200.0% | −0.1661 to +0.3794 | no |
| utilisation (used / allocatable) | 0.03609 | 0.04771 | +32.2% | +0.0100 to +0.0132 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8662 | 1.145 | +32.2% | +0.2411 to +0.3166 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00819 | +0.008 (native is 0) | +0.0074 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8662 | 1.153 | +33.1% | +0.2488 to +0.3253 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.8 | 559.6 | −22.9% | −182.3711 to −150.0635 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.859 | 10.07 | +13.7% | +0.6469 to +1.7779 | yes: power given |
| pods started | 5 | 3.5 | −30.0% | −2.9405 to −0.0595 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 5.6 | −23.3% | −5.0390 to +1.6390 | no |
| pod start wait, mean (s) | 1.43 | 1.562 | +9.2% | −0.2625 to +0.5258 | no |
| host CPU busy, the real machine under kind (%) | 25.73 | 33.8 | +31.3% | +7.0117 to +9.1190 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*