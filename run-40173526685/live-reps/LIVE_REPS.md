# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.59 | 7.399 |
| node-hours | 5.029 | 5.018 | 4.435 | 3.093 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 503.7 | 524.5 | 503.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 503.7 | 480.3 | 359.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 500.6 | 122.6 | 488 | 71.62 |
| response time (ms), 95th percentile | 2003 | 166.3 | 2115 | 92.96 |
| response time (ms), 99th percentile | 2841 | 187.7 | 3131 | 124 |
| time over the response line (% of samples) | 19.71 | 0.007605 | 20.04 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 0 | 11 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 93 | 25.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 0.02667 | 12.84 | 0.05333 |
| utilisation (used / allocatable) | 0.03302 | 0.006088 | 0.03821 | 0.008477 |
| CPU used (cores), mean | 1.585 | 0.2922 | 1.597 | 0.2526 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01334 | 0.00834 |
| CPU used with Omni's own (cores), mean | 1.585 | 0.2922 | 1.611 | 0.261 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.9 | 4236 | 721.7 | 3543 |
| HPA replicas, mean | 4.077 | 4.266 | 4.596 | 4.435 |
| pods started | 0.4 | 0.5 | 1.5 | 1.2 |
| pod start wait, total (s) | 0.9 | 0.8 | 2 | 2.1 |
| pod start wait, mean (s) | 0.65 | 0.65 | 1.05 | 1.317 |
| host CPU busy, the real machine under kind (%) | 48.15 | 13.62 | 50.1 | 14.48 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 831.1 | 1502 | 841.9 | 1504 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.738 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1156 | 0.1 | 1157 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1472 | 0.7 | 1473 |
| queue: job turnaround, submitted to done, mean (s) | 143.5 | 1156 | 150.9 | 1157 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.399 | −38.3% | −5.2032 to −3.9990 | yes: GAIN |
| node-hours | 5.018 | 3.093 | −38.4% | −2.1795 to −1.6706 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 503.7 | 503.8 | +0.0% | −1.2467 to +1.3234 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.7 | 359.5 | −28.6% | −163.4660 to −125.0657 | yes: GAIN |
| response time (ms), mean | 122.6 | 71.62 | −41.6% | −61.9948 to −39.8574 | yes: GAIN |
| response time (ms), 95th percentile | 166.3 | 92.96 | −44.1% | −87.1331 to −59.6039 | yes: GAIN |
| response time (ms), 99th percentile | 187.7 | 124 | −33.9% | −78.6325 to −48.6817 | yes: GAIN |
| time over the response line (% of samples) | 0.007605 | 0 | −100.0% | −0.0191 to +0.0039 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.7 | +25.700 (native is 0) | +23.8210 to +27.5790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 | +100.0% | −0.0816 to +0.1349 | no |
| utilisation (used / allocatable) | 0.006088 | 0.008477 | +39.2% | +0.0020 to +0.0028 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2922 | 0.2526 | −13.5% | −0.0513 to −0.0278 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00834 | +0.008 (native is 0) | +0.0072 to +0.0095 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2922 | 0.261 | −10.7% | −0.0429 to −0.0196 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4236 | 3543 | −16.4% | −803.2691 to −582.8302 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.266 | 4.435 | +4.0% | −0.0654 to +0.4030 | no |
| pods started | 0.5 | 1.2 | +140.0% | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0.8 | 2.1 | +162.5% | −0.2471 to +2.8471 | no |
| pod start wait, mean (s) | 0.65 | 1.317 | +102.6% | −0.4346 to +1.7680 | no |
| host CPU busy, the real machine under kind (%) | 13.62 | 14.48 | +6.3% | +0.3275 to +1.3948 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1502 | 1504 | +0.1% | −1.1326 to +3.1326 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1157 | +0.1% | −1.2210 to +3.0043 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 1473 | +0.1% | −1.3273 to +2.9273 | no |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1157 | +0.1% | −1.2210 to +3.0043 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.029 | 5.018 | −0.2% | −0.0307 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 503.7 | −4.0% | −23.8877 to −17.7489 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 503.7 | −4.0% | −23.8877 to −17.7489 | yes: GAIN |
| response time (ms), mean | 500.6 | 122.6 | −75.5% | −583.4081 to −172.6374 | yes: GAIN |
| response time (ms), 95th percentile | 2003 | 166.3 | −91.7% | −2878.4975 to −794.6645 | yes: GAIN |
| response time (ms), 99th percentile | 2841 | 187.7 | −93.4% | −4112.1745 to −1193.8749 | yes: GAIN |
| time over the response line (% of samples) | 19.71 | 0.007605 | −100.0% | −31.3393 to −8.0654 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 0 | −100.0% | −14.6827 to −4.5173 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 0.02667 | −99.8% | −16.8238 to −9.5362 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03302 | 0.006088 | −81.6% | −0.0301 to −0.0237 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.585 | 0.2922 | −81.6% | −1.4458 to −1.1395 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.585 | 0.2922 | −81.6% | −1.4458 to −1.1395 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.9 | 4236 | +422.4% | +2968.1180 to +3882.0407 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.077 | 4.266 | +4.6% | −0.0350 to +0.4123 | no |
| pods started | 0.4 | 0.5 | +25.0% | −0.6872 to +0.8872 | no |
| pod start wait, total (s) | 0.9 | 0.8 | −11.1% | −1.6617 to +1.4617 | no |
| pod start wait, mean (s) | 0.65 | 0.65 | ±0.0% | −0.9974 to +0.9974 | no |
| host CPU busy, the real machine under kind (%) | 48.15 | 13.62 | −71.7% | −39.1766 to −29.8909 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 831.1 | 1502 | +80.8% | +604.7256 to +738.0744 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1156 | +2312075.0% | +1153.2932 to +1158.7818 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1472 | +490666.7% | +1469.1990 to +1474.8010 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.5 | 1156 | +705.4% | +941.8360 to +1083.2390 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.9677 to +0.1482 | no |
| node-hours | 5.029 | 4.435 | −11.8% | −1.2508 to +0.0619 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 524.5 | −0.0% | −1.8341 to +1.7488 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 480.3 | −8.4% | −93.5089 to +4.9069 | no |
| response time (ms), mean | 500.6 | 488 | −2.5% | −35.7812 to +10.7062 | no |
| response time (ms), 95th percentile | 2003 | 2115 | +5.6% | −46.5731 to +270.7471 | no |
| response time (ms), 99th percentile | 2841 | 3131 | +10.2% | +54.1260 to +525.7306 | yes: LOSS |
| time over the response line (% of samples) | 19.71 | 20.04 | +1.7% | −1.0487 to +1.7098 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 11 | +14.6% | −0.2588 to +3.0588 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93 | +93.000 (native is 0) | +48.4655 to +137.5345 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 12.84 | −2.8% | −2.8846 to +2.1479 | no |
| utilisation (used / allocatable) | 0.03302 | 0.03821 | +15.7% | −0.0005 to +0.0108 | no |
| CPU used (cores), mean | 1.585 | 1.597 | +0.8% | −0.0241 to +0.0492 | no |
| Omni's own CPU (cores), mean | 0 | 0.01334 | +0.013 (native is 0) | +0.0121 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.585 | 1.611 | +1.6% | −0.0101 to +0.0619 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.9 | 721.7 | −11.0% | −185.5637 to +7.1470 | no |
| HPA replicas, mean | 4.077 | 4.596 | +12.7% | +0.2443 to +0.7924 | yes: power given |
| pods started | 0.4 | 1.5 | +275.0% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.9 | 2 | +122.2% | −0.1818 to +2.3818 | no |
| pod start wait, mean (s) | 0.65 | 1.05 | +61.5% | −0.4728 to +1.2728 | no |
| host CPU busy, the real machine under kind (%) | 48.15 | 50.1 | +4.0% | +1.4148 to +2.4853 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 831.1 | 841.9 | +1.3% | −0.6290 to +22.2290 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.738 | −18.9% | −4.6730 to +0.1480 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1 | +100.0% | −0.0003 to +0.1003 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.5 | 150.9 | +5.1% | −0.4531 to +15.1281 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.9677 to +0.1482 | no |
| node-hours | 5.018 | 4.435 | −11.6% | −1.2422 to +0.0754 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 503.7 | 524.5 | +4.1% | +17.6332 to +23.9180 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.7 | 480.3 | −4.7% | −75.2559 to +28.2905 | no |
| response time (ms), mean | 122.6 | 488 | +298.2% | +157.4144 to +573.5561 | yes: LOSS |
| response time (ms), 95th percentile | 166.3 | 2115 | +1171.6% | +873.6812 to +3023.6548 | yes: LOSS |
| response time (ms), 99th percentile | 187.7 | 3131 | +1567.9% | +1377.5477 to +4508.3583 | yes: LOSS |
| time over the response line (% of samples) | 0.007605 | 20.04 | +263431.4% | +9.2017 to +30.8640 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11 | +11.000 (native is 0) | +6.2194 to +15.7806 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93 | +93.000 (native is 0) | +48.4655 to +137.5345 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 12.84 | +48043.8% | +7.9719 to +17.6514 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006088 | 0.03821 | +527.7% | +0.0289 to +0.0354 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2922 | 1.597 | +446.7% | +1.1410 to +1.4694 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01334 | +0.013 (native is 0) | +0.0121 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2922 | 1.611 | +451.2% | +1.1544 to +1.4827 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4236 | 721.7 | −83.0% | −4064.1108 to −2964.4646 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.266 | 4.596 | +7.7% | +0.0829 to +0.5766 | yes: power given |
| pods started | 0.5 | 1.5 | +200.0% | +0.1740 to +1.8260 | yes: power given |
| pod start wait, total (s) | 0.8 | 2 | +150.0% | −0.1403 to +2.5403 | no |
| pod start wait, mean (s) | 0.65 | 1.05 | +61.5% | −0.4890 to +1.2890 | no |
| host CPU busy, the real machine under kind (%) | 13.62 | 50.1 | +267.9% | +31.8159 to +41.1516 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1502 | 841.9 | −44.0% | −734.5114 to −586.6886 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 0.1 | −100.0% | −1158.7554 to −1153.2196 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 0.7 | −100.0% | −1474.5046 to −1468.6954 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 150.9 | −86.9% | −1078.7302 to −931.6698 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.399 | −38.3% | −5.2032 to −3.9990 | yes: GAIN |
| node-hours | 5.029 | 3.093 | −38.5% | −2.1937 to −1.6785 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 503.8 | −4.0% | −23.4809 to −18.0790 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 359.5 | −31.5% | −182.9387 to −147.2295 | yes: GAIN |
| response time (ms), mean | 500.6 | 71.62 | −85.7% | −643.6093 to −214.2885 | yes: GAIN |
| response time (ms), 95th percentile | 2003 | 92.96 | −95.4% | −2960.7910 to −859.1080 | yes: GAIN |
| response time (ms), 99th percentile | 2841 | 124 | −95.6% | −4176.0322 to −1257.3314 | yes: GAIN |
| time over the response line (% of samples) | 19.71 | 0 | −100.0% | −31.3515 to −8.0684 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 0 | −100.0% | −14.6827 to −4.5173 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.7 | +25.700 (native is 0) | +23.8210 to +27.5790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.21 | 0.05333 | −99.6% | −16.8017 to −9.5049 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03302 | 0.008477 | −74.3% | −0.0276 to −0.0215 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.585 | 0.2526 | −84.1% | −1.4805 to −1.1839 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00834 | +0.008 (native is 0) | +0.0072 to +0.0095 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.585 | 0.261 | −83.5% | −1.4713 to −1.1765 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.9 | 3543 | +336.9% | +2298.9215 to +3165.1379 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.077 | 4.435 | +8.8% | +0.1898 to +0.5251 | yes: power given |
| pods started | 0.4 | 1.2 | +200.0% | −0.1417 to +1.7417 | no |
| pod start wait, total (s) | 0.9 | 2.1 | +133.3% | −0.5456 to +2.9456 | no |
| pod start wait, mean (s) | 0.65 | 1.317 | +102.6% | −0.3681 to +1.7014 | no |
| host CPU busy, the real machine under kind (%) | 48.15 | 14.48 | −69.9% | −37.9271 to −29.4180 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 831.1 | 1504 | +80.9% | +605.8118 to +738.9882 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1157 | +2313858.3% | +1154.8381 to +1159.0203 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1473 | +490933.3% | +1470.7268 to +1474.8732 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.5 | 1157 | +706.0% | +942.9859 to +1083.8724 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*