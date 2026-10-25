# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.517 | 1.515 | 1.517 | 1.516 | 1.516 | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | 158.2 | 158.4 | 158.3 | 158.3 | 158.3 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | 158.2 | 158.4 | 158.3 | 158.3 | 158.3 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 138.7 | 73.08 | 72.62 | 72.95 | 72.88 | 73.01 | 73.45 | 73.69 |
| response time (ms), 95th percentile | 312.9 | 108.7 | 108.7 | 108.5 | 107.9 | 108.2 | 109.4 | 110.3 |
| response time (ms), 99th percentile | 498.7 | 144.8 | 148.6 | 143.6 | 149.4 | 149.7 | 144.2 | 148.5 |
| time over the response line (% of samples) | 1.807 | 0.0241 | 0 | 0.0241 | 0.0479 | 0 | 0.02424 | 0.0241 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | 15.8 | 16.7 | 14.6 | 16.4 | 19.3 | 20.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 90 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1067 | 0.05333 | 0.1333 | 0.08 | 0.02667 | 0 | 0.1067 |
| utilisation (used / allocatable) | 0.03571 | 0.03411 | 0.03418 | 0.03408 | 0.0338 | 0.034 | 0.03431 | 0.03456 |
| CPU used (cores), mean | 0.857 | 0.8187 | 0.8204 | 0.8178 | 0.8112 | 0.8159 | 0.8234 | 0.8294 |
| Omni's own CPU (cores), mean | 0 | 0.00812 | 0.00573 | 0.00625 | 0.00679 | 0.01287 | 0.02324 | 0.06329 |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8268 | 0.8261 | 0.8241 | 0.818 | 0.8288 | 0.8467 | 0.8927 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 804.6 | 803.8 | 804.2 | 816.7 | 812.9 | 802.8 | 800.7 |
| HPA replicas, mean | 8.269 | 7.938 | 8.163 | 7.657 | 6.437 | 7.213 | 8.329 | 8.336 |
| pods started | 5.6 | 4.5 | 4.4 | 4.4 | 3 | 4.2 | 4.8 | 5 |
| pod start wait, total (s) | 8.1 | 5.9 | 7.1 | 6.7 | 4.1 | 6.2 | 7.1 | 7.2 |
| pod start wait, mean (s) | 1.447 | 1.287 | 1.615 | 1.59 | 1.415 | 1.465 | 1.554 | 1.483 |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.36 | 25.24 | 25.32 | 25.09 | 25.33 | 25.99 | 27.33 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

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
| node-hours | 1.514 | 1.517 | +0.2% | −0.0016 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.0% | −0.5088 to +0.4542 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.0% | −0.5088 to +0.4542 | no |
| response time (ms), mean | 138.7 | 73.08 | −47.3% | −88.8276 to −42.4921 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 108.7 | −65.2% | −271.6369 to −136.6721 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 144.8 | −71.0% | −474.3519 to −233.5661 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0.0241 | −98.7% | −3.1312 to −0.4345 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.700 (native is 0) | +15.1981 to +20.2019 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1067 | +36.2% | −0.1988 to +0.2555 | no |
| utilisation (used / allocatable) | 0.03571 | 0.03411 | −4.5% | −0.0027 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8187 | −4.5% | −0.0652 to −0.0114 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00812 | +0.008 (native is 0) | +0.0070 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8268 | −3.5% | −0.0563 to −0.0042 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 804.6 | +2.8% | +1.8927 to +41.3942 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.269 | 7.938 | −4.0% | −0.7546 to +0.0927 | no |
| pods started | 5.6 | 4.5 | −19.6% | −2.3818 to +0.1818 | no |
| pod start wait, total (s) | 8.1 | 5.9 | −27.2% | −4.6502 to +0.2502 | no |
| pod start wait, mean (s) | 1.447 | 1.287 | −11.1% | −0.5238 to +0.2038 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.36 | −2.5% | −1.3333 to +0.0198 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0009 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.2 | −0.2% | −0.5518 to +0.0743 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.2 | −0.2% | −0.5518 to +0.0743 | no |
| response time (ms), mean | 138.7 | 72.62 | −47.7% | −89.8163 to −42.4295 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 108.7 | −65.3% | −271.6339 to −136.7991 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 148.6 | −70.2% | −473.3091 to −226.9495 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0 | −100.0% | −3.1711 to −0.4429 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.8 | +15.800 (native is 0) | +14.7997 to +16.8003 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.05333 | −31.9% | −0.2135 to +0.1635 | no |
| utilisation (used / allocatable) | 0.03571 | 0.03418 | −4.3% | −0.0027 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8204 | −4.3% | −0.0644 to −0.0088 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00573 | +0.006 (native is 0) | +0.0051 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8261 | −3.6% | −0.0583 to −0.0035 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 803.8 | +2.7% | −0.4626 to +42.0015 | no |
| HPA replicas, mean | 8.269 | 8.163 | −1.3% | −0.3670 to +0.1562 | no |
| pods started | 5.6 | 4.4 | −21.4% | −2.5403 to +0.1403 | no |
| pod start wait, total (s) | 8.1 | 7.1 | −12.3% | −3.6336 to +1.6336 | no |
| pod start wait, mean (s) | 1.447 | 1.615 | +11.6% | −0.1006 to +0.4368 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.24 | −3.0% | −1.4464 to −0.1047 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.517 | +0.2% | −0.0030 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.1% | −0.6449 to +0.4714 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.1% | −0.6449 to +0.4714 | no |
| response time (ms), mean | 138.7 | 72.95 | −47.4% | −89.1605 to −42.4190 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 108.5 | −65.3% | −271.4636 to −137.2434 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 143.6 | −71.2% | −474.3254 to −235.9700 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0.0241 | −98.7% | −3.1292 to −0.4365 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.7 | +16.700 (native is 0) | +14.3145 to +19.0855 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1333 | +70.2% | −0.2106 to +0.3206 | no |
| utilisation (used / allocatable) | 0.03571 | 0.03408 | −4.6% | −0.0028 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8178 | −4.6% | −0.0681 to −0.0103 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00625 | +0.006 (native is 0) | +0.0054 to +0.0071 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8241 | −3.8% | −0.0612 to −0.0047 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 804.2 | +2.7% | −0.8618 to +43.2284 | no |
| HPA replicas, mean | 8.269 | 7.657 | −7.4% | −1.3840 to +0.1607 | no |
| pods started | 5.6 | 4.4 | −21.4% | −2.4064 to +0.0064 | no |
| pod start wait, total (s) | 8.1 | 6.7 | −17.3% | −4.4198 to +1.6198 | no |
| pod start wait, mean (s) | 1.447 | 1.59 | +9.9% | −0.4111 to +0.6978 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.32 | −2.7% | −1.3937 to −0.0048 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0036 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | −0.1% | −0.7714 to +0.4344 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | −0.1% | −0.7714 to +0.4344 | no |
| response time (ms), mean | 138.7 | 72.88 | −47.5% | −88.8170 to −42.8982 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 107.9 | −65.5% | −270.6845 to −139.2425 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 149.4 | −70.0% | −472.3897 to −226.3193 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0.0479 | −97.3% | −3.1078 to −0.4103 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.6 | +14.600 (native is 0) | +11.3798 to +17.8202 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.08 | +2.1% | −0.1557 to +0.1591 | no |
| utilisation (used / allocatable) | 0.03571 | 0.0338 | −5.3% | −0.0028 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8112 | −5.3% | −0.0664 to −0.0253 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00679 | +0.007 (native is 0) | +0.0058 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.818 | −4.6% | −0.0587 to −0.0194 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 816.7 | +4.3% | +24.2496 to +43.2285 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.269 | 6.437 | −22.2% | −2.5589 to −1.1050 | yes: GAIN |
| pods started | 5.6 | 3 | −46.4% | −3.6228 to −1.5772 | yes: GAIN |
| pod start wait, total (s) | 8.1 | 4.1 | −49.4% | −6.2367 to −1.7633 | yes: GAIN |
| pod start wait, mean (s) | 1.447 | 1.415 | −2.2% | −0.3032 to +0.2399 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.09 | −3.5% | −1.3718 to −0.4746 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0035 to +0.0071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | −0.1% | −0.7329 to +0.3760 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | −0.1% | −0.7329 to +0.3760 | no |
| response time (ms), mean | 138.7 | 73.01 | −47.4% | −88.6740 to −42.7814 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 108.2 | −65.4% | −270.7582 to −138.6678 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 149.7 | −70.0% | −468.8773 to −229.1329 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0 | −100.0% | −3.1711 to −0.4429 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 | +16.400 (native is 0) | +13.6772 to +19.1228 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.02667 | −66.0% | −0.2008 to +0.0975 | no |
| utilisation (used / allocatable) | 0.03571 | 0.034 | −4.8% | −0.0025 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8159 | −4.8% | −0.0601 to −0.0220 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01287 | +0.013 (native is 0) | +0.0112 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8288 | −3.3% | −0.0457 to −0.0107 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 812.9 | +3.8% | +20.8236 to +39.0601 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.269 | 7.213 | −12.8% | −1.6699 to −0.4417 | yes: GAIN |
| pods started | 5.6 | 4.2 | −25.0% | −2.4228 to −0.3772 | yes: GAIN |
| pod start wait, total (s) | 8.1 | 6.2 | −23.5% | −4.6487 to +0.8487 | no |
| pod start wait, mean (s) | 1.447 | 1.465 | +1.3% | −0.4509 to +0.4876 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.33 | −2.6% | −1.1338 to −0.2309 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0001 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | −0.1% | −0.4223 to +0.0954 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | −0.1% | −0.4223 to +0.0954 | no |
| response time (ms), mean | 138.7 | 73.45 | −47.1% | −88.2692 to −42.3221 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 109.4 | −65.0% | −269.8755 to −137.1765 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 144.2 | −71.1% | −476.5939 to −232.3657 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0.02424 | −98.7% | −3.1261 to −0.4394 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +17.8283 to +20.7717 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0 | −100.0% | −0.2058 to +0.0491 | no |
| utilisation (used / allocatable) | 0.03571 | 0.03431 | −3.9% | −0.0024 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8234 | −3.9% | −0.0583 to −0.0088 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02324 | +0.023 (native is 0) | +0.0204 to +0.0261 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8467 | −1.2% | −0.0336 to +0.0130 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 802.8 | +2.5% | +2.9264 to +36.7631 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.269 | 8.329 | +0.7% | −0.2132 to +0.3333 | no |
| pods started | 5.6 | 4.8 | −14.3% | −1.8556 to +0.2556 | no |
| pod start wait, total (s) | 8.1 | 7.1 | −12.3% | −3.4779 to +1.4779 | no |
| pod start wait, mean (s) | 1.447 | 1.554 | +7.4% | −0.1220 to +0.3373 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 25.99 | −0.1% | −0.4875 to +0.4394 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0002 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.1% | −0.2966 to +0.0928 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.1% | −0.2966 to +0.0928 | no |
| response time (ms), mean | 138.7 | 73.69 | −46.9% | −87.6185 to −42.4762 | yes: GAIN |
| response time (ms), 95th percentile | 312.9 | 110.3 | −64.8% | −268.1808 to −137.0462 | yes: GAIN |
| response time (ms), 99th percentile | 498.7 | 148.5 | −70.2% | −463.0830 to −237.3870 | yes: GAIN |
| time over the response line (% of samples) | 1.807 | 0.0241 | −98.7% | −3.1313 to −0.4344 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3871 to −0.4129 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +17.9626 to +22.6374 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1067 | +36.2% | −0.0774 to +0.1341 | no |
| utilisation (used / allocatable) | 0.03571 | 0.03456 | −3.2% | −0.0018 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.857 | 0.8294 | −3.2% | −0.0442 to −0.0110 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06329 | +0.063 (native is 0) | +0.0553 to +0.0713 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.857 | 0.8927 | +4.2% | +0.0229 to +0.0484 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783 | 800.7 | +2.3% | +7.1476 to +28.3376 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.269 | 8.336 | +0.8% | −0.1879 to +0.3222 | no |
| pods started | 5.6 | 5 | −10.7% | −1.3689 to +0.1689 | no |
| pod start wait, total (s) | 8.1 | 7.2 | −11.1% | −2.7607 to +0.9607 | no |
| pod start wait, mean (s) | 1.447 | 1.483 | +2.5% | −0.3474 to +0.4207 | no |
| host CPU busy, the real machine under kind (%) | 26.01 | 27.33 | +5.0% | +1.0262 to +1.5961 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.515 | −0.1% | −0.0068 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | −0.1% | −0.6369 to +0.2140 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | −0.1% | −0.6369 to +0.2140 | no |
| response time (ms), mean | 73.08 | 72.62 | −0.6% | −1.3078 to +0.3817 | no |
| response time (ms), 95th percentile | 108.7 | 108.7 | −0.1% | −1.6529 to +1.5289 | no |
| response time (ms), 99th percentile | 144.8 | 148.6 | +2.6% | −5.1839 to +12.8433 | no |
| time over the response line (% of samples) | 0.0241 | 0 | −100.0% | −0.0604 to +0.0122 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 15.8 | −10.7% | −3.9358 to +0.1358 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.05333 | −50.0% | −0.1740 to +0.0673 | no |
| utilisation (used / allocatable) | 0.03411 | 0.03418 | +0.2% | −0.0006 to +0.0007 | no |
| CPU used (cores), mean | 0.8187 | 0.8204 | +0.2% | −0.0133 to +0.0167 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.00573 | −29.4% | −0.0028 to −0.0020 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.8261 | −0.1% | −0.0157 to +0.0143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 803.8 | −0.1% | −16.6642 to +14.9162 | no |
| HPA replicas, mean | 7.938 | 8.163 | +2.8% | −0.1841 to +0.6353 | no |
| pods started | 4.5 | 4.4 | −2.2% | −1.8986 to +1.6986 | no |
| pod start wait, total (s) | 5.9 | 7.1 | +20.3% | −1.7163 to +4.1163 | no |
| pod start wait, mean (s) | 1.287 | 1.615 | +25.5% | −0.0206 to +0.6768 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.24 | −0.5% | −0.4268 to +0.1892 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.517 | −0.0% | −0.0025 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.4 | −0.0% | −0.3008 to +0.1818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.4 | −0.0% | −0.3008 to +0.1818 | no |
| response time (ms), mean | 73.08 | 72.95 | −0.2% | −0.9940 to +0.7343 | no |
| response time (ms), 95th percentile | 108.7 | 108.5 | −0.2% | −2.1525 to +1.7545 | no |
| response time (ms), 99th percentile | 144.8 | 143.6 | −0.8% | −18.6369 to +16.2595 | no |
| time over the response line (% of samples) | 0.0241 | 0.0241 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 16.7 | −5.6% | −4.1452 to +2.1452 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1333 | +25.0% | −0.0337 to +0.0870 | no |
| utilisation (used / allocatable) | 0.03411 | 0.03408 | −0.1% | −0.0005 to +0.0004 | no |
| CPU used (cores), mean | 0.8187 | 0.8178 | −0.1% | −0.0112 to +0.0094 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.00625 | −23.0% | −0.0023 to −0.0015 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.8241 | −0.3% | −0.0131 to +0.0076 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 804.2 | −0.1% | −12.0037 to +11.0834 | no |
| HPA replicas, mean | 7.938 | 7.657 | −3.5% | −1.1132 to +0.5517 | no |
| pods started | 4.5 | 4.4 | −2.2% | −2.1358 to +1.9358 | no |
| pod start wait, total (s) | 5.9 | 6.7 | +13.6% | −2.2310 to +3.8310 | no |
| pod start wait, mean (s) | 1.287 | 1.59 | +23.6% | −0.1720 to +0.7787 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.32 | −0.2% | −0.3158 to +0.2307 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.516 | −0.1% | −0.0024 to +0.0001 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.3 | −0.1% | −0.3569 to +0.0744 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.3 | −0.1% | −0.3569 to +0.0744 | no |
| response time (ms), mean | 73.08 | 72.88 | −0.3% | −0.6942 to +0.2987 | no |
| response time (ms), 95th percentile | 108.7 | 107.9 | −0.7% | −3.2834 to +1.6654 | no |
| response time (ms), 99th percentile | 144.8 | 149.4 | +3.2% | −8.0191 to +17.2281 | no |
| time over the response line (% of samples) | 0.0241 | 0.0479 | +98.8% | −0.0648 to +0.1124 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 14.6 | −17.5% | −5.9503 to −0.2497 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08 | −25.0% | −0.2164 to +0.1630 | no |
| utilisation (used / allocatable) | 0.03411 | 0.0338 | −0.9% | −0.0007 to +0.0001 | no |
| CPU used (cores), mean | 0.8187 | 0.8112 | −0.9% | −0.0179 to +0.0029 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.00679 | −16.4% | −0.0016 to −0.0010 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.818 | −1.1% | −0.0194 to +0.0017 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 816.7 | +1.5% | −0.5156 to +24.7068 | no |
| HPA replicas, mean | 7.938 | 6.437 | −18.9% | −2.0790 to −0.9229 | yes: GAIN |
| pods started | 4.5 | 3 | −33.3% | −3.1944 to +0.1944 | no |
| pod start wait, total (s) | 5.9 | 4.1 | −30.5% | −4.3636 to +0.7636 | no |
| pod start wait, mean (s) | 1.287 | 1.415 | +10.0% | −0.1589 to +0.4156 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.09 | −1.1% | −0.5807 to +0.0477 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | −0.1% | −0.0026 to −0.0001 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.3 | −0.1% | −0.3655 to +0.0632 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.3 | −0.1% | −0.3655 to +0.0632 | no |
| response time (ms), mean | 73.08 | 73.01 | −0.1% | −1.3566 to +1.2210 | no |
| response time (ms), 95th percentile | 108.7 | 108.2 | −0.5% | −3.7091 to +2.5921 | no |
| response time (ms), 99th percentile | 144.8 | 149.7 | +3.4% | −5.4282 to +15.3360 | no |
| time over the response line (% of samples) | 0.0241 | 0 | −100.0% | −0.0604 to +0.0122 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 16.4 | −7.3% | −3.8912 to +1.2912 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.02667 | −75.0% | −0.2087 to +0.0487 | no |
| utilisation (used / allocatable) | 0.03411 | 0.034 | −0.3% | −0.0007 to +0.0005 | no |
| CPU used (cores), mean | 0.8187 | 0.8159 | −0.3% | −0.0169 to +0.0114 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.01287 | +58.5% | +0.0041 to +0.0054 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.8288 | +0.2% | −0.0125 to +0.0165 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 812.9 | +1.0% | −7.5234 to +24.1203 | no |
| HPA replicas, mean | 7.938 | 7.213 | −9.1% | −1.3953 to −0.0544 | yes: GAIN |
| pods started | 4.5 | 4.2 | −6.7% | −1.5639 to +0.9639 | no |
| pod start wait, total (s) | 5.9 | 6.2 | +5.1% | −1.9633 to +2.5633 | no |
| pod start wait, mean (s) | 1.287 | 1.465 | +13.9% | −0.2355 to +0.5922 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.33 | −0.1% | −0.4811 to +0.4299 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | −0.1% | −0.0068 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.3 | −0.1% | −0.6173 to +0.3450 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.3 | −0.1% | −0.6173 to +0.3450 | no |
| response time (ms), mean | 73.08 | 73.45 | +0.5% | −0.4123 to +1.1408 | no |
| response time (ms), 95th percentile | 108.7 | 109.4 | +0.6% | −1.5315 to +2.7885 | no |
| response time (ms), 99th percentile | 144.8 | 144.2 | −0.4% | −9.6736 to +8.6320 | no |
| time over the response line (% of samples) | 0.0241 | 0.02424 | +0.6% | −0.0405 to +0.0408 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 19.3 | +9.0% | −1.3046 to +4.5046 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0 | −100.0% | −0.2675 to +0.0542 | no |
| utilisation (used / allocatable) | 0.03411 | 0.03431 | +0.6% | −0.0004 to +0.0008 | no |
| CPU used (cores), mean | 0.8187 | 0.8234 | +0.6% | −0.0087 to +0.0182 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.02324 | +186.2% | +0.0133 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.8467 | +2.4% | +0.0053 to +0.0344 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 802.8 | −0.2% | −12.8311 to +9.2338 | no |
| HPA replicas, mean | 7.938 | 8.329 | +4.9% | −0.0690 to +0.8511 | no |
| pods started | 4.5 | 4.8 | +6.7% | −1.2471 to +1.8471 | no |
| pod start wait, total (s) | 5.9 | 7.1 | +20.3% | −1.2962 to +3.6962 | no |
| pod start wait, mean (s) | 1.287 | 1.554 | +20.8% | −0.0516 to +0.5868 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 25.99 | +2.5% | +0.1853 to +1.0801 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | −0.1% | −0.0077 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.4 | −0.0% | −0.6436 to +0.4944 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.4 | −0.0% | −0.6436 to +0.4944 | no |
| response time (ms), mean | 73.08 | 73.69 | +0.8% | −0.1296 to +1.3547 | no |
| response time (ms), 95th percentile | 108.7 | 110.3 | +1.4% | −0.9399 to +4.0219 | no |
| response time (ms), 99th percentile | 144.8 | 148.5 | +2.6% | −9.4245 to +16.8725 | no |
| time over the response line (% of samples) | 0.0241 | 0.0241 | ±0.0% | −0.0404 to +0.0404 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.7 | 20.3 | +14.7% | +0.0721 to +5.1279 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1067 | ±0.0% | −0.1557 to +0.1557 | no |
| utilisation (used / allocatable) | 0.03411 | 0.03456 | +1.3% | −0.0001 to +0.0010 | no |
| CPU used (cores), mean | 0.8187 | 0.8294 | +1.3% | −0.0021 to +0.0235 | no |
| Omni's own CPU (cores), mean | 0.00812 | 0.06329 | +679.4% | +0.0482 to +0.0621 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8268 | 0.8927 | +8.0% | +0.0471 to +0.0847 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.6 | 800.7 | −0.5% | −17.1743 to +9.3727 | no |
| HPA replicas, mean | 7.938 | 8.336 | +5.0% | +0.0461 to +0.7502 | yes: power given |
| pods started | 4.5 | 5 | +11.1% | −1.1259 to +2.1259 | no |
| pod start wait, total (s) | 5.9 | 7.2 | +22.0% | −1.1093 to +3.7093 | no |
| pod start wait, mean (s) | 1.287 | 1.483 | +15.3% | −0.0479 to +0.4412 | no |
| host CPU busy, the real machine under kind (%) | 25.36 | 27.33 | +7.8% | +1.4206 to +2.5152 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*