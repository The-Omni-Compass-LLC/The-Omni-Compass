# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.68 | 11.98 |
| node-hours | 5.029 | 5.02 | 4.902 | 5.022 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 525.6 | 525.9 | 527.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 525.6 | 515.8 | 527.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 455.6 | 724.1 | 459 | 819.2 |
| response time (ms), 95th percentile | 1685 | 2928 | 1976 | 3572 |
| response time (ms), 99th percentile | 2542 | 4091 | 2840 | 4988 |
| time over the response line (% of samples) | 19.15 | 27.39 | 20.77 | 32.17 |
| failed requests (%) | 0 | 0 | 0 | 0.1465 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 15.4 | 12.3 | 16.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 82.1 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.3 | 14.07 | 13.07 | 20.42 |
| utilisation (used / allocatable) | 0.03295 | 0.03597 | 0.03463 | 0.03751 |
| CPU used (cores), mean | 1.582 | 1.727 | 1.62 | 1.799 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01202 | 0.01214 |
| CPU used with Omni's own (cores), mean | 1.582 | 1.727 | 1.632 | 1.811 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.7 | 741.5 | 765.1 | 709.1 |
| HPA replicas, mean | 4.063 | 4.061 | 4.911 | 4.96 |
| pods started | 0.1 | 0.1 | 1.3 | 2.3 |
| pod start wait, total (s) | 0.3 | 0.2 | 1.9 | 4.7 |
| pod start wait, mean (s) | 0.3 | 0.2 | 0.95 | 1.892 |
| host CPU busy, the real machine under kind (%) | 48.32 | 55.49 | 50.25 | 59.07 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.9 | 920.1 | 829.1 | 978.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.37 | 11.97 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 5.783 | 0.09167 | 13.61 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 31.9 | 0.5 | 94.2 |
| queue: job turnaround, submitted to done, mean (s) | 124 | 208.3 | 139.9 | 262.6 |
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
| worker nodes in service, mean | 12 | 11.98 | −0.1% | −0.0516 to +0.0199 | no |
| node-hours | 5.02 | 5.022 | +0.0% | −0.0154 to +0.0202 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 527.7 | +0.4% | −0.0959 to +4.3676 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 527.2 | +0.3% | −0.7256 to +4.0014 | no |
| response time (ms), mean | 724.1 | 819.2 | +13.1% | +1.8011 to +188.4593 | yes: LOSS |
| response time (ms), 95th percentile | 2928 | 3572 | +22.0% | +180.4005 to +1107.4405 | yes: LOSS |
| response time (ms), 99th percentile | 4091 | 4988 | +21.9% | +192.0353 to +1601.6309 | yes: LOSS |
| time over the response line (% of samples) | 27.39 | 32.17 | +17.5% | +0.4211 to +9.1389 | yes: LOSS |
| failed requests (%) | 0 | 0.1465 | +0.146 (native is 0) | −0.0448 to +0.3378 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 16.3 | +5.8% | +0.1887 to +1.6113 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.100 (native is 0) | +43.6450 to +56.5550 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.07 | 20.42 | +45.2% | −2.0036 to +14.7070 | no |
| utilisation (used / allocatable) | 0.03597 | 0.03751 | +4.3% | +0.0003 to +0.0027 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.727 | 1.799 | +4.2% | +0.0135 to +0.1308 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01214 | +0.012 (native is 0) | +0.0111 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.727 | 1.811 | +4.9% | +0.0260 to +0.1425 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 709.1 | −4.4% | −59.0643 to −5.7292 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.061 | 4.96 | +22.1% | +0.6612 to +1.1364 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +1.6358 to +2.7642 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.7 | +2250.0% | +1.9044 to +7.0956 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.892 | +845.8% | +0.8638 to +2.5196 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.49 | 59.07 | +6.4% | +2.0463 to +5.0971 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 920.1 | 978.2 | +6.3% | +25.1502 to +91.0498 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.97 | −0.3% | −0.1041 to +0.0403 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.783 | 13.61 | +135.4% | −1.7184 to +17.3767 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.9 | 94.2 | +195.3% | −39.6697 to +164.2697 | no |
| queue: job turnaround, submitted to done, mean (s) | 208.3 | 262.6 | +26.1% | +20.4597 to +88.1903 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.029 | 5.02 | −0.2% | −0.0214 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 525.6 | +0.2% | −0.4216 to +2.3298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 525.6 | +0.2% | −0.4216 to +2.3298 | no |
| response time (ms), mean | 455.6 | 724.1 | +58.9% | +131.8615 to +405.1436 | yes: LOSS |
| response time (ms), 95th percentile | 1685 | 2928 | +73.8% | +582.5197 to +1904.4353 | yes: LOSS |
| response time (ms), 99th percentile | 2542 | 4091 | +60.9% | +804.2244 to +2293.5816 | yes: LOSS |
| time over the response line (% of samples) | 19.15 | 27.39 | +43.0% | +5.8370 to +10.6277 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 15.4 | +48.1% | +2.6883 to +7.3117 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.3 | 14.07 | +24.5% | −2.3754 to +7.9087 | no |
| utilisation (used / allocatable) | 0.03295 | 0.03597 | +9.2% | +0.0021 to +0.0039 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.582 | 1.727 | +9.2% | +0.1026 to +0.1876 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.582 | 1.727 | +9.2% | +0.1026 to +0.1876 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.7 | 741.5 | −7.6% | −70.4272 to −51.9578 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.063 | 4.061 | −0.0% | −0.1512 to +0.1472 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 48.32 | 55.49 | +14.8% | +5.0924 to +9.2575 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.9 | 920.1 | +13.2% | +49.2618 to +165.1382 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 5.783 | +8064.7% | −0.3027 to +11.7277 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 31.9 | +7875.0% | −16.1242 to +79.1242 | no |
| queue: job turnaround, submitted to done, mean (s) | 124 | 208.3 | +68.0% | +42.1266 to +126.4734 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.68 | −2.7% | −0.7036 to +0.0590 | no |
| node-hours | 5.029 | 4.902 | −2.5% | −0.2926 to +0.0378 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 525.9 | +0.3% | −0.5703 to +3.2183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 515.8 | −1.7% | −21.3812 to +3.7709 | no |
| response time (ms), mean | 455.6 | 459 | +0.7% | −20.7247 to +27.5272 | no |
| response time (ms), 95th percentile | 1685 | 1976 | +17.3% | +132.2539 to +449.6581 | yes: LOSS |
| response time (ms), 99th percentile | 2542 | 2840 | +11.7% | −23.6583 to +619.9705 | no |
| time over the response line (% of samples) | 19.15 | 20.77 | +8.5% | −0.9815 to +4.2214 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 12.3 | +18.3% | −0.0792 to +3.8792 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.1 | +82.100 (native is 0) | +43.2350 to +120.9650 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.3 | 13.07 | +15.6% | −2.2887 to +5.8220 | no |
| utilisation (used / allocatable) | 0.03295 | 0.03463 | +5.1% | +0.0003 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.582 | 1.62 | +2.5% | +0.0163 to +0.0615 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.0116 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.582 | 1.632 | +3.2% | +0.0283 to +0.0736 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.7 | 765.1 | −4.7% | −68.5550 to −6.5654 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.063 | 4.911 | +20.9% | +0.6007 to +1.0952 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.9 | +533.3% | −0.0242 to +3.2242 | no |
| pod start wait, mean (s) | 0.3 | 0.95 | +216.7% | −0.1938 to +1.4938 | no |
| host CPU busy, the real machine under kind (%) | 48.32 | 50.25 | +4.0% | +1.3277 to +2.5341 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.9 | 829.1 | +2.0% | +5.6937 to +26.7063 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.37 | −5.2% | −1.3694 to +0.1137 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.09167 | +29.4% | −0.0322 to +0.0739 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 124 | 139.9 | +12.8% | +6.3533 to +25.4884 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.68 | −2.7% | −0.7036 to +0.0590 | no |
| node-hours | 5.02 | 4.902 | −2.3% | −0.2813 to +0.0458 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 525.9 | +0.1% | −1.4283 to +2.1681 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 515.8 | −1.9% | −21.6818 to +2.1633 | no |
| response time (ms), mean | 724.1 | 459 | −36.6% | −403.9682 to −126.2345 | yes: GAIN |
| response time (ms), 95th percentile | 2928 | 1976 | −32.5% | −1592.5238 to −312.5192 | yes: GAIN |
| response time (ms), 99th percentile | 4091 | 2840 | −30.6% | −2085.7469 to −415.7469 | yes: GAIN |
| time over the response line (% of samples) | 27.39 | 20.77 | −24.1% | −8.6664 to −4.5583 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 12.3 | −20.1% | −5.1077 to −1.0923 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.1 | +82.100 (native is 0) | +43.2350 to +120.9650 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.07 | 13.07 | −7.1% | −4.5300 to +2.5300 | no |
| utilisation (used / allocatable) | 0.03597 | 0.03463 | −3.7% | −0.0033 to +0.0006 | no |
| CPU used (cores), mean | 1.727 | 1.62 | −6.2% | −0.1592 to −0.0532 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.0116 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.727 | 1.632 | −5.5% | −0.1470 to −0.0414 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 741.5 | 765.1 | +3.2% | −9.3676 to +56.6322 | no |
| HPA replicas, mean | 4.061 | 4.911 | +20.9% | +0.5671 to +1.1328 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.9 | +850.0% | +0.1166 to +3.2834 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | −0.0803 to +1.5803 | no |
| host CPU busy, the real machine under kind (%) | 55.49 | 50.25 | −9.4% | −7.2964 to −3.1917 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 920.1 | 829.1 | −9.9% | −144.4532 to −37.5468 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.37 | −5.2% | −1.3694 to +0.1137 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 5.783 | 0.09167 | −98.4% | −11.6939 to +0.3106 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.9 | 0.5 | −98.4% | −79.0576 to +16.2576 | no |
| queue: job turnaround, submitted to done, mean (s) | 208.3 | 139.9 | −32.8% | −108.2405 to −28.5179 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.98 | −0.1% | −0.0516 to +0.0199 | no |
| node-hours | 5.029 | 5.022 | −0.1% | −0.0279 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 527.7 | +0.6% | +0.7798 to +5.4000 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 527.2 | +0.5% | −0.0692 to +5.2532 | no |
| response time (ms), mean | 455.6 | 819.2 | +79.8% | +217.6249 to +509.6406 | yes: LOSS |
| response time (ms), 95th percentile | 1685 | 3572 | +112.0% | +1222.6298 to +2552.1662 | yes: LOSS |
| response time (ms), 99th percentile | 2542 | 4988 | +96.2% | +1615.4775 to +3275.9947 | yes: LOSS |
| time over the response line (% of samples) | 19.15 | 32.17 | +67.9% | +6.9137 to +19.1109 | yes: LOSS |
| failed requests (%) | 0 | 0.1465 | +0.146 (native is 0) | −0.0448 to +0.3378 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 16.3 | +56.7% | +3.4118 to +8.3882 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.100 (native is 0) | +43.6450 to +56.5550 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.3 | 20.42 | +80.7% | −0.2728 to +18.5095 | no |
| utilisation (used / allocatable) | 0.03295 | 0.03751 | +13.9% | +0.0034 to +0.0057 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.582 | 1.799 | +13.7% | +0.1606 to +0.2738 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01214 | +0.012 (native is 0) | +0.0111 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.582 | 1.811 | +14.5% | +0.1725 to +0.2863 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.7 | 709.1 | −11.7% | −119.2261 to −67.9525 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.063 | 4.96 | +22.1% | +0.6321 to +1.1615 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +1.6358 to +2.7642 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.7 | +1466.7% | +1.8947 to +6.9053 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.892 | +530.6% | +0.8630 to +2.3203 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.32 | 59.07 | +22.2% | +8.5108 to +12.9825 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.9 | 978.2 | +20.3% | +103.9195 to +226.6805 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.97 | −0.3% | −0.1041 to +0.0403 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 13.61 | +19117.6% | +2.0365 to +25.0469 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 94.2 | +23450.0% | +0.0448 to +187.5552 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124 | 262.6 | +111.8% | +89.2895 to +187.9605 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*