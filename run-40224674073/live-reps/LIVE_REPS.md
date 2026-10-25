# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.517 | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.1 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.1 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 170 | 82.02 | 85.98 |
| response time (ms), 95th percentile | 394.3 | 125 | 108.8 |
| response time (ms), 99th percentile | 662.3 | 173.2 | 140 |
| time over the response line (% of samples) | 3.089 | 0 | 0.3276 |
| failed requests (%) | 0 | 0 | 0.08604 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | 69.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1517 | 0.16 | 0.05333 |
| utilisation (used / allocatable) | 0.04044 | 0.03801 | 0.03745 |
| CPU used (cores), mean | 0.9706 | 0.9123 | 0.8989 |
| Omni's own CPU (cores), mean | 0 | 0.0084 | 0.01237 |
| CPU used with Omni's own (cores), mean | 0.9706 | 0.9207 | 0.9113 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684 | 721.4 | 725.5 |
| HPA replicas, mean | 8.638 | 7.772 | 1 |
| pods started | 5.5 | 3.3 | 0 |
| pod start wait, total (s) | 8.8 | 4 | 0 |
| pod start wait, mean (s) | 1.612 | 1.153 | 0 |
| host CPU busy, the real machine under kind (%) | 28.93 | 27.52 | 27.41 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

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
| node-hours | 1.517 | 1.515 | −0.1% | −0.0063 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.1 | −0.5% | −1.3607 to −0.1778 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.1 | −0.5% | −1.3607 to −0.1778 | yes: GAIN |
| response time (ms), mean | 170 | 82.02 | −51.7% | −110.1518 to −65.7340 | yes: GAIN |
| response time (ms), 95th percentile | 394.3 | 125 | −68.3% | −332.0129 to −206.5171 | yes: GAIN |
| response time (ms), 99th percentile | 662.3 | 173.2 | −73.8% | −606.5284 to −371.6818 | yes: GAIN |
| time over the response line (% of samples) | 3.089 | 0 | −100.0% | −4.3136 to −1.8646 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | −100.0% | −4.6924 to −1.9076 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | +16.300 (native is 0) | +13.4980 to +19.1020 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1517 | 0.16 | +5.5% | −0.3395 to +0.3562 | no |
| utilisation (used / allocatable) | 0.04044 | 0.03801 | −6.0% | −0.0036 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9706 | 0.9123 | −6.0% | −0.0867 to −0.0299 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.008 (native is 0) | +0.0073 to +0.0095 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9706 | 0.9207 | −5.1% | −0.0782 to −0.0216 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684 | 721.4 | +5.5% | +17.5725 to +57.1256 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.638 | 7.772 | −10.0% | −1.8491 to +0.1178 | no |
| pods started | 5.5 | 3.3 | −40.0% | −3.5821 to −0.8179 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 4 | −54.5% | −6.2621 to −3.3379 | yes: GAIN |
| pod start wait, mean (s) | 1.612 | 1.153 | −28.4% | −0.6491 to −0.2681 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.93 | 27.52 | −4.9% | −2.0961 to −0.7110 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | −0.1% | −0.0059 to +0.0039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.4 | −0.3% | −1.2103 to +0.2795 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.4 | −0.3% | −1.2103 to +0.2795 | no |
| response time (ms), mean | 170 | 85.98 | −49.4% | −106.8646 to −61.1103 | yes: GAIN |
| response time (ms), 95th percentile | 394.3 | 108.8 | −72.4% | −355.7635 to −215.2065 | yes: GAIN |
| response time (ms), 99th percentile | 662.3 | 140 | −78.9% | −652.2317 to −392.3837 | yes: GAIN |
| time over the response line (% of samples) | 3.089 | 0.3276 | −89.4% | −3.9960 to −1.5271 | yes: GAIN |
| failed requests (%) | 0 | 0.08604 | +0.086 (native is 0) | +0.0266 to +0.1455 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0.5 | −84.8% | −4.2621 to −1.3379 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.4 | +69.400 (native is 0) | +68.4952 to +70.3048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1517 | 0.05333 | −64.8% | −0.3422 to +0.1455 | no |
| utilisation (used / allocatable) | 0.04044 | 0.03745 | −7.4% | −0.0047 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9706 | 0.8989 | −7.4% | −0.1119 to −0.0315 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.012 (native is 0) | +0.0111 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9706 | 0.9113 | −6.1% | −0.0991 to −0.0196 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 684 | 725.5 | +6.1% | +10.2570 to +72.5584 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.638 | 1 | −88.4% | −8.0648 to −7.2104 | yes: GAIN |
| pods started | 5.5 | 0 | −100.0% | −6.0058 to −4.9942 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 0 | −100.0% | −9.8003 to −7.7997 | yes: GAIN |
| pod start wait, mean (s) | 1.612 | 0 | −100.0% | −1.8080 to −1.4158 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.93 | 27.41 | −5.2% | −2.4318 to −0.6032 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0010 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.4 | +0.2% | −0.0647 to +0.6723 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.4 | +0.2% | −0.0647 to +0.6723 | no |
| response time (ms), mean | 82.02 | 85.98 | +4.8% | +0.4623 to +7.4486 | yes: LOSS |
| response time (ms), 95th percentile | 125 | 108.8 | −13.0% | −26.2196 to −6.2204 | yes: GAIN |
| response time (ms), 99th percentile | 173.2 | 140 | −19.2% | −50.6151 to −15.7901 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.3276 | +0.328 (native is 0) | +0.2071 to +0.4480 | yes: LOSS |
| failed requests (%) | 0 | 0.08604 | +0.086 (native is 0) | +0.0266 to +0.1455 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 16.3 | 69.4 | +325.8% | +50.4567 to +55.7433 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.05333 | −66.7% | −0.3479 to +0.1346 | no |
| utilisation (used / allocatable) | 0.03801 | 0.03745 | −1.5% | −0.0015 to +0.0004 | no |
| CPU used (cores), mean | 0.9123 | 0.8989 | −1.5% | −0.0363 to +0.0094 | no |
| Omni's own CPU (cores), mean | 0.0084 | 0.01237 | +47.3% | +0.0037 to +0.0043 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9207 | 0.9113 | −1.0% | −0.0323 to +0.0134 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 721.4 | 725.5 | +0.6% | −16.1468 to +24.2641 | no |
| HPA replicas, mean | 7.772 | 1 | −87.1% | −8.0799 to −5.4641 | yes: GAIN |
| pods started | 3.3 | 0 | −100.0% | −4.5639 to −2.0361 | yes: GAIN |
| pod start wait, total (s) | 4 | 0 | −100.0% | −5.8774 to −2.1226 | yes: GAIN |
| pod start wait, mean (s) | 1.153 | 0 | −100.0% | −1.3374 to −0.9693 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.52 | 27.41 | −0.4% | −0.6549 to +0.4270 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*