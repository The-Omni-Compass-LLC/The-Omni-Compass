# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.689 | 10.17 |
| node-hours | 5.022 | 5.036 | 4.053 | 4.267 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 525.1 | 522 | 525.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 525.1 | 449.6 | 467.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 380.9 | 579.8 | 361.9 | 670.1 |
| response time (ms), 95th percentile | 1439 | 2293 | 1541 | 2830 |
| response time (ms), 99th percentile | 2097 | 3223 | 2312 | 3847 |
| time over the response line (% of samples) | 14.02 | 19.37 | 14.02 | 21.72 |
| failed requests (%) | 0 | 0.02228 | 0 | 0.07989 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 9.9 | 8.3 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 102.1 | 78.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 12.17 | 10.81 | 13.67 |
| utilisation (used / allocatable) | 0.03064 | 0.0328 | 0.03816 | 0.03916 |
| CPU used (cores), mean | 1.471 | 1.575 | 1.462 | 1.59 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01256 | 0.01224 |
| CPU used with Omni's own (cores), mean | 1.471 | 1.575 | 1.475 | 1.602 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 874.2 | 827.8 | 740.9 | 715.8 |
| HPA replicas, mean | 4.027 | 3.896 | 4.163 | 3.954 |
| pods started | 0.2 | 0.1 | 0.9 | 0.3 |
| pod start wait, total (s) | 0.3 | 0.2 | 1.5 | 0.4 |
| pod start wait, mean (s) | 0.3 | 0.2 | 1.15 | 0.4 |
| host CPU busy, the real machine under kind (%) | 44.81 | 51.33 | 46.46 | 53.61 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 797.7 | 881.7 | 805.1 | 914.7 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.249 | 9.175 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 7.771 | 0.05 | 1.688 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 61.9 | 0.4 | 11.7 |
| queue: job turnaround, submitted to done, mean (s) | 107.7 | 171.9 | 111.7 | 211.3 |
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
| worker nodes in service, mean | 12 | 10.17 | −15.2% | −3.4819 to −0.1752 | yes: GAIN |
| node-hours | 5.036 | 4.267 | −15.3% | −1.4617 to −0.0766 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 525.4 | +0.1% | −1.7712 to +2.5305 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 467.9 | −10.9% | −109.5196 to −4.8377 | yes: GAIN |
| response time (ms), mean | 579.8 | 670.1 | +15.6% | −8.0048 to +188.7393 | no |
| response time (ms), 95th percentile | 2293 | 2830 | +23.4% | +123.6705 to +950.7935 | yes: LOSS |
| response time (ms), 99th percentile | 3223 | 3847 | +19.4% | +130.0043 to +1117.7457 | yes: LOSS |
| time over the response line (% of samples) | 19.37 | 21.72 | +12.2% | −1.7232 to +6.4355 | no |
| failed requests (%) | 0.02228 | 0.07989 | +258.6% | −0.0328 to +0.1480 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.7 | +8.1% | +0.3476 to +1.2524 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.6 | +78.600 (native is 0) | +37.4545 to +119.7455 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 13.67 | +12.3% | −0.9240 to +3.9173 | no |
| utilisation (used / allocatable) | 0.0328 | 0.03916 | +19.4% | +0.0015 to +0.0112 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.575 | 1.59 | +1.0% | −0.0503 to +0.0803 | no |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0113 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.575 | 1.602 | +1.7% | −0.0378 to +0.0922 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827.8 | 715.8 | −13.5% | −193.1759 to −30.8725 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.896 | 3.954 | +1.5% | −0.1586 to +0.2752 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 51.33 | 53.61 | +4.4% | +1.0829 to +3.4728 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 881.7 | 914.7 | +3.7% | +12.0855 to +53.9145 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.175 | −23.5% | −5.3136 to −0.3367 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 7.771 | 1.687 | −78.3% | −13.6936 to +1.5269 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 61.9 | 11.7 | −81.1% | −112.7873 to +12.3873 | no |
| queue: job turnaround, submitted to done, mean (s) | 171.9 | 211.3 | +22.9% | +10.2652 to +68.4431 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.022 | 5.036 | +0.3% | −0.0062 to +0.0335 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 525.1 | +0.6% | +0.7971 to +4.9547 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 525.1 | +0.6% | +0.7971 to +4.9547 | yes: power given |
| response time (ms), mean | 380.9 | 579.8 | +52.2% | +43.0636 to +354.7468 | yes: LOSS |
| response time (ms), 95th percentile | 1439 | 2293 | +59.3% | +186.7835 to +1519.9115 | yes: LOSS |
| response time (ms), 99th percentile | 2097 | 3223 | +53.7% | +230.8001 to +2020.6919 | yes: LOSS |
| time over the response line (% of samples) | 14.02 | 19.37 | +38.1% | +1.4986 to +9.1890 | yes: LOSS |
| failed requests (%) | 0 | 0.02228 | +0.022 (native is 0) | −0.0034 to +0.0479 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 9.9 | +37.5% | +0.2907 to +5.1093 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 12.17 | +10.8% | −0.7000 to +3.0634 | no |
| utilisation (used / allocatable) | 0.03064 | 0.0328 | +7.1% | +0.0010 to +0.0034 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.471 | 1.575 | +7.1% | +0.0466 to +0.1616 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.471 | 1.575 | +7.1% | +0.0466 to +0.1616 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 874.2 | 827.8 | −5.3% | −65.3114 to −27.3537 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.027 | 3.896 | −3.3% | −0.2955 to +0.0332 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.8113 to +0.6113 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.8113 to +0.6113 | no |
| host CPU busy, the real machine under kind (%) | 44.81 | 51.33 | +14.6% | +4.5440 to +8.5040 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.7 | 881.7 | +10.5% | +18.2765 to +149.7235 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 7.771 | +13221.4% | −2.2924 to +17.7174 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 61.9 | +15375.0% | −18.3487 to +141.3487 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.7 | 171.9 | +59.6% | +15.4567 to +113.0266 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.689 | −19.3% | −3.9968 to −0.6252 | yes: GAIN |
| node-hours | 5.022 | 4.053 | −19.3% | −1.6805 to −0.2575 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 522 | −0.0% | −2.4796 to +2.1151 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 449.6 | −13.9% | −126.2491 to −18.9154 | yes: GAIN |
| response time (ms), mean | 380.9 | 361.9 | −5.0% | −37.2299 to −0.7278 | yes: GAIN |
| response time (ms), 95th percentile | 1439 | 1541 | +7.1% | +3.6753 to +199.4507 | yes: LOSS |
| response time (ms), 99th percentile | 2097 | 2312 | +10.3% | −71.9577 to +502.0335 | no |
| time over the response line (% of samples) | 14.02 | 14.02 | +0.0% | −0.8749 to +0.8782 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 8.3 | +15.3% | −0.9358 to +3.1358 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.1 | +102.100 (native is 0) | +56.7264 to +147.4736 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 10.81 | −1.6% | −1.7722 to +1.4156 | no |
| utilisation (used / allocatable) | 0.03064 | 0.03816 | +24.6% | +0.0022 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.471 | 1.462 | −0.6% | −0.0481 to +0.0311 | no |
| Omni's own CPU (cores), mean | 0 | 0.01256 | +0.013 (native is 0) | +0.0119 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.471 | 1.475 | +0.3% | −0.0358 to +0.0439 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 874.2 | 740.9 | −15.2% | −224.2482 to −42.2717 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.027 | 4.163 | +3.4% | −0.0305 to +0.3027 | no |
| pods started | 0.2 | 0.9 | +350.0% | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.5 | +400.0% | +0.0919 to +2.3081 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.15 | +283.3% | +0.0951 to +1.6049 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.81 | 46.46 | +3.7% | +1.1787 to +2.1165 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.7 | 805.1 | +0.9% | −2.0126 to +16.8126 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 8.249 | −31.3% | −6.3533 to −1.1481 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05 | −14.3% | −0.0523 to +0.0357 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.7 | 111.7 | +3.7% | −2.3691 to +10.2858 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.689 | −19.3% | −3.9968 to −0.6252 | yes: GAIN |
| node-hours | 5.036 | 4.053 | −19.5% | −1.6912 to −0.2741 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 522 | −0.6% | −4.9964 to −1.1199 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 449.6 | −14.4% | −128.0839 to −22.8325 | yes: GAIN |
| response time (ms), mean | 579.8 | 361.9 | −37.6% | −373.4227 to −62.3454 | yes: GAIN |
| response time (ms), 95th percentile | 2293 | 1541 | −32.8% | −1374.6639 to −128.9051 | yes: GAIN |
| response time (ms), 99th percentile | 3223 | 2312 | −28.3% | −1673.1893 to −148.2269 | yes: GAIN |
| time over the response line (% of samples) | 19.37 | 14.02 | −27.6% | −9.3182 to −1.3662 | yes: GAIN |
| failed requests (%) | 0.02228 | 0 | −100.0% | −0.0479 to +0.0034 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 8.3 | −16.2% | −2.9146 to −0.2854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.1 | +102.100 (native is 0) | +56.7264 to +147.4736 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.17 | 10.81 | −11.2% | −4.0835 to +1.3635 | no |
| utilisation (used / allocatable) | 0.0328 | 0.03816 | +16.3% | −0.0010 to +0.0117 | no |
| CPU used (cores), mean | 1.575 | 1.462 | −7.2% | −0.1517 to −0.0735 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01256 | +0.013 (native is 0) | +0.0119 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.575 | 1.475 | −6.4% | −0.1393 to −0.0608 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827.8 | 740.9 | −10.5% | −189.9607 to +16.1058 | no |
| HPA replicas, mean | 3.896 | 4.163 | +6.9% | +0.0685 to +0.4661 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | +0.1427 to +1.4573 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.5 | +650.0% | −0.0081 to +2.6081 | no |
| pod start wait, mean (s) | 0.2 | 1.15 | +475.0% | −0.0955 to +1.9955 | no |
| host CPU busy, the real machine under kind (%) | 51.33 | 46.46 | −9.5% | −6.9557 to −2.7970 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 881.7 | 805.1 | −8.7% | −136.4471 to −16.7529 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.249 | −31.3% | −6.3533 to −1.1481 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 7.771 | 0.05 | −99.4% | −17.7405 to +2.2988 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 61.9 | 0.4 | −99.4% | −141.4206 to +18.4206 | no |
| queue: job turnaround, submitted to done, mean (s) | 171.9 | 111.7 | −35.1% | −106.8530 to −13.7137 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.17 | −15.2% | −3.4819 to −0.1752 | yes: GAIN |
| node-hours | 5.022 | 4.267 | −15.0% | −1.4532 to −0.0576 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 525.4 | +0.6% | +0.8241 to +5.6870 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 467.9 | −10.4% | −107.7960 to −0.8095 | yes: GAIN |
| response time (ms), mean | 380.9 | 670.1 | +76.0% | +61.7100 to +516.8349 | yes: LOSS |
| response time (ms), 95th percentile | 1439 | 2830 | +96.6% | +394.2100 to +2386.9490 | yes: LOSS |
| response time (ms), 99th percentile | 2097 | 3847 | +83.4% | +512.0216 to +2987.2204 | yes: LOSS |
| time over the response line (% of samples) | 14.02 | 21.72 | +54.9% | +1.5567 to +13.8432 | yes: LOSS |
| failed requests (%) | 0 | 0.07989 | +0.080 (native is 0) | −0.0307 to +0.1905 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 10.7 | +48.6% | +0.8826 to +6.1174 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.6 | +78.600 (native is 0) | +37.4545 to +119.7455 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.99 | 13.67 | +24.4% | −0.3702 to +5.7268 | no |
| utilisation (used / allocatable) | 0.03064 | 0.03916 | +27.8% | +0.0045 to +0.0125 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.471 | 1.59 | +8.1% | +0.0189 to +0.2193 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0113 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.471 | 1.602 | +8.9% | +0.0313 to +0.2313 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 874.2 | 715.8 | −18.1% | −230.3914 to −86.3221 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.027 | 3.954 | −1.8% | −0.2989 to +0.1532 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.6872 to +0.8872 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.6872 to +0.8872 | no |
| host CPU busy, the real machine under kind (%) | 44.81 | 53.61 | +19.6% | +6.0833 to +11.5203 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.7 | 914.7 | +14.7% | +36.9665 to +197.0335 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.175 | −23.5% | −5.3136 to −0.3367 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1.688 | +2792.9% | −1.4966 to +4.7550 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 11.7 | +2825.0% | −12.2607 to +34.8607 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.7 | 211.3 | +96.2% | +30.9415 to +176.2501 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*