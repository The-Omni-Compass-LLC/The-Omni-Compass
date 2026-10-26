# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.034 | 5.843 |
| node-hours | 2.514 | 2.514 | 1.69 | 2.446 |
| energy, parked workers still on at idle power (Wh, declared model) | 267.7 | 270.2 | 267.6 | 270 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 267.7 | 270.2 | 205.8 | 265 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 155.3 | 98.95 | 129.3 | 73.03 |
| response time (ms), 95th percentile | 441.9 | 167.4 | 455.8 | 153.5 |
| response time (ms), 99th percentile | 674.7 | 249.8 | 675.6 | 239.1 |
| time over the response line (% of samples) | 3.466 | 0.0912 | 3.667 | 0.05204 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | 3.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 60 | 15.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.02 | 671.8 | 7.508 | 719.4 |
| utilisation (used / allocatable) | 0.04741 | 0.05541 | 0.06927 | 0.05648 |
| CPU used (cores), mean | 1.138 | 1.33 | 1.104 | 1.322 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01455 | 0.0116 |
| CPU used with Omni's own (cores), mean | 1.138 | 1.33 | 1.118 | 1.334 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.5 | 489.1 | 448.6 | 481 |
| HPA replicas, mean | 1.9 | 1.938 | 1.973 | 1.992 |
| pods started | 0.1 | 0.3 | 0 | 0.1 |
| pod start wait, total (s) | 0.3 | 0.5 | 0 | 0.2 |
| pod start wait, mean (s) | 0.3 | 0.3 | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 32.95 | 40.35 | 33.73 | 40.82 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 727 | 1268 | 727.2 | 1273 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 2.8 | 5.141 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 86.55 | 0.02083 | 89.59 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 429.7 | 0.1 | 405.6 |
| queue: job turnaround, submitted to done, mean (s) | 33.37 | 542 | 32.67 | 568.9 |
| queue: jobs unfinished at the window's end | 0 | 2.5 | 0 | 3.9 |

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
| worker nodes in service, mean | 6 | 5.843 | −2.6% | −0.3454 to +0.0315 | no |
| node-hours | 2.514 | 2.446 | −2.7% | −0.1461 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 270 | −0.1% | −1.1814 to +0.7502 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 265 | −1.9% | −11.0415 to +0.7687 | no |
| response time (ms), mean | 98.95 | 73.03 | −26.2% | −32.8406 to −18.9902 | yes: GAIN |
| response time (ms), 95th percentile | 167.4 | 153.5 | −8.3% | −21.2998 to −6.5572 | yes: GAIN |
| response time (ms), 99th percentile | 249.8 | 239.1 | −4.3% | −26.3065 to +4.9841 | no |
| time over the response line (% of samples) | 0.0912 | 0.05204 | −42.9% | −0.0692 to −0.0091 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.3 | +15.300 (native is 0) | +11.8112 to +18.7888 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 671.8 | 719.4 | +7.1% | −12.5253 to +107.6053 | no |
| utilisation (used / allocatable) | 0.05541 | 0.05648 | +1.9% | −0.0010 to +0.0031 | no |
| CPU used (cores), mean | 1.33 | 1.322 | −0.6% | −0.0389 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.0116 | +0.012 (native is 0) | +0.0108 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.33 | 1.334 | +0.3% | −0.0269 to +0.0354 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.1 | 481 | −1.7% | −23.8687 to +7.6465 | no |
| HPA replicas, mean | 1.938 | 1.992 | +2.8% | −0.0645 to +0.1722 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.5 | 0.2 | −60.0% | −1.3690 to +0.7690 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.8113 to +0.6113 | no |
| host CPU busy, the real machine under kind (%) | 40.35 | 40.82 | +1.2% | −0.2618 to +1.2015 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1268 | 1273 | +0.4% | −9.9855 to +19.9855 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.141 | −14.3% | −1.5650 to −0.1522 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 86.55 | 89.59 | +3.5% | −16.5221 to +22.5971 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 429.7 | 405.6 | −5.6% | −110.0351 to +61.8351 | no |
| queue: job turnaround, submitted to done, mean (s) | 542 | 568.9 | +5.0% | −0.5230 to +54.1897 | no |
| queue: jobs unfinished at the window's end | 2.5 | 3.9 | +56.0% | −0.2242 to +3.0242 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.514 | =0.0% | −0.0095 to +0.0095 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 267.7 | 270.2 | +0.9% | +1.1368 to +3.8698 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 267.7 | 270.2 | +0.9% | +1.1368 to +3.8698 | yes: power given |
| response time (ms), mean | 155.3 | 98.95 | −36.3% | −117.5408 to +4.8110 | no |
| response time (ms), 95th percentile | 441.9 | 167.4 | −62.1% | −569.6090 to +20.7160 | no |
| response time (ms), 99th percentile | 674.7 | 249.8 | −63.0% | −876.4157 to +26.4567 | no |
| time over the response line (% of samples) | 3.466 | 0.0912 | −97.4% | −9.3057 to +2.5564 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −5.6599 to +0.2599 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.02 | 671.8 | +9470.1% | +417.4644 to +912.1390 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04741 | 0.05541 | +16.9% | +0.0056 to +0.0104 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.138 | 1.33 | +16.9% | +0.1337 to +0.2500 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.138 | 1.33 | +16.9% | +0.1337 to +0.2500 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.5 | 489.1 | −14.9% | −119.1350 to −51.6445 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.9 | 1.938 | +2.0% | −0.1037 to +0.1789 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −1.0064 to +1.4064 | no |
| pod start wait, mean (s) | 0.3 | 0.3 | ±0.0% | −0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 32.95 | 40.35 | +22.5% | +6.1618 to +8.6407 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 727 | 1268 | +74.4% | +388.0813 to +693.7187 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 86.55 | +346116.7% | +39.8302 to +133.2281 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 429.7 | +214750.0% | +254.5914 to +604.4086 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 33.37 | 542 | +1524.5% | +339.6826 to +677.6424 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 2.5 | +2.500 (native is 0) | −1.0245 to +6.0245 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.034 | −32.8% | −2.6226 to −1.3094 | yes: GAIN |
| node-hours | 2.514 | 1.69 | −32.8% | −1.0975 to −0.5500 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 267.7 | 267.6 | −0.0% | −0.6736 to +0.4778 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 267.7 | 205.8 | −23.1% | −82.3412 to −41.4171 | yes: GAIN |
| response time (ms), mean | 155.3 | 129.3 | −16.8% | −42.4441 to −9.6709 | yes: GAIN |
| response time (ms), 95th percentile | 441.9 | 455.8 | +3.1% | −43.8730 to +71.6820 | no |
| response time (ms), 99th percentile | 674.7 | 675.6 | +0.1% | −115.8063 to +117.6147 | no |
| time over the response line (% of samples) | 3.466 | 3.667 | +5.8% | −0.4524 to +0.8548 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 3.6 | +33.3% | −0.0802 to +1.8802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 | +60.000 (native is 0) | +45.0145 to +74.9855 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.02 | 7.508 | +7.0% | −1.8533 to +2.8300 | no |
| utilisation (used / allocatable) | 0.04741 | 0.06927 | +46.1% | +0.0136 to +0.0301 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.138 | 1.104 | −3.0% | −0.0675 to −0.0010 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01455 | +0.015 (native is 0) | +0.0128 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.138 | 1.118 | −1.7% | −0.0534 to +0.0141 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.5 | 448.6 | −21.9% | −177.9532 to −73.9202 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.9 | 1.973 | +3.8% | −0.0297 to +0.1742 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 32.95 | 33.73 | +2.4% | +0.4644 to +1.1077 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 727 | 727.2 | +0.0% | −1.8456 to +2.2456 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.8 | −53.3% | −4.1806 to −2.2201 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.02083 | −16.7% | −0.0338 to +0.0255 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 33.37 | 32.68 | −2.1% | −2.8331 to +1.4498 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.034 | −32.8% | −2.6226 to −1.3094 | yes: GAIN |
| node-hours | 2.514 | 1.69 | −32.8% | −1.0984 to −0.5491 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 267.6 | −1.0% | −3.6660 to −1.5364 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 205.8 | −23.8% | −85.4084 to −43.3565 | yes: GAIN |
| response time (ms), mean | 98.95 | 129.3 | +30.6% | −15.8306 to +76.4454 | no |
| response time (ms), 95th percentile | 167.4 | 455.8 | +172.2% | +44.8229 to +531.8791 | yes: LOSS |
| response time (ms), 99th percentile | 249.8 | 675.6 | +170.5% | +88.0037 to +763.7637 | yes: LOSS |
| time over the response line (% of samples) | 0.0912 | 3.667 | +3921.1% | −1.7847 to +8.9365 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 3.6 | +3.600 (native is 0) | +0.7748 to +6.4252 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 | +60.000 (native is 0) | +45.0145 to +74.9855 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 671.8 | 7.508 | −98.9% | −912.7692 to −415.8574 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05541 | 0.06927 | +25.0% | +0.0074 to +0.0204 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.33 | 1.104 | −17.0% | −0.2897 to −0.1625 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01455 | +0.015 (native is 0) | +0.0128 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.33 | 1.118 | −15.9% | −0.2759 to −0.1472 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.1 | 448.6 | −8.3% | −64.9653 to −16.1287 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 1.973 | +1.8% | −0.0929 to +0.1622 | no |
| pods started | 0.3 | 0 | −100.0% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.4079 to +0.4079 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.7828 to +0.1828 | no |
| host CPU busy, the real machine under kind (%) | 40.35 | 33.73 | −16.4% | −7.8318 to −5.3985 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1268 | 727.2 | −42.6% | −693.9955 to −387.4045 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.014 | −66.4% | −4.0214 to −3.9514 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 86.55 | 0.02083 | −100.0% | −133.2488 to −39.8178 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 429.7 | 0.1 | −100.0% | −604.6794 to −254.5206 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 542 | 32.68 | −94.0% | −679.5072 to −339.2012 | yes: GAIN |
| queue: jobs unfinished at the window's end | 2.5 | 0 | −100.0% | −6.0245 to +1.0245 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.843 | −2.6% | −0.3454 to +0.0315 | no |
| node-hours | 2.514 | 2.446 | −2.7% | −0.1466 to +0.0114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 267.7 | 270 | +0.9% | +0.8704 to +3.7050 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 267.7 | 265 | −1.0% | −8.7017 to +3.4354 | no |
| response time (ms), mean | 155.3 | 73.03 | −53.0% | −148.6709 to −15.8897 | yes: GAIN |
| response time (ms), 95th percentile | 441.9 | 153.5 | −65.3% | −587.7576 to +11.0076 | no |
| response time (ms), 99th percentile | 674.7 | 239.1 | −64.6% | −896.2794 to +24.9980 | no |
| time over the response line (% of samples) | 3.466 | 0.05204 | −98.5% | −9.3604 to +2.5327 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −5.6599 to +0.2599 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.3 | +15.300 (native is 0) | +11.8112 to +18.7888 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.02 | 719.4 | +10147.3% | +418.9578 to +1005.7255 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04741 | 0.05648 | +19.1% | +0.0051 to +0.0131 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.138 | 1.322 | +16.2% | +0.1043 to +0.2648 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0116 | +0.012 (native is 0) | +0.0108 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.138 | 1.334 | +17.2% | +0.1164 to +0.2759 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.5 | 481 | −16.3% | −140.7186 to −46.2831 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.9 | 1.992 | +4.8% | −0.0441 to +0.2272 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 32.95 | 40.82 | +23.9% | +6.2804 to +9.4618 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 727 | 1273 | +75.1% | +392.3657 to +699.4343 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.141 | −14.3% | −1.5650 to −0.1522 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 89.59 | +358266.7% | +57.7748 to +121.3585 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 405.6 | +202700.0% | +264.9230 to +545.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 33.37 | 568.9 | +1604.9% | +346.6629 to +724.3287 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 3.9 | +3.900 (native is 0) | −0.5918 to +8.3918 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*