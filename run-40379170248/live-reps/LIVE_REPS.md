# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.49 | 7.182 |
| node-hours | 5.034 | 5.022 | 3.977 | 3.001 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 504 | 523.1 | 503.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 504 | 444.2 | 352.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 387.4 | 113.8 | 369.6 | 66.73 |
| response time (ms), 95th percentile | 1404 | 155.1 | 1544 | 82.19 |
| response time (ms), 99th percentile | 2089 | 175.2 | 2381 | 107.5 |
| time over the response line (% of samples) | 14.43 | 0.003846 | 14.71 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 0 | 8.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 103.2 | 25.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.898 | 0 | 11.22 | 0.07667 |
| utilisation (used / allocatable) | 0.03116 | 0.005706 | 0.03839 | 0.008144 |
| CPU used (cores), mean | 1.496 | 0.2739 | 1.445 | 0.2358 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01235 | 0.00792 |
| CPU used with Omni's own (cores), mean | 1.496 | 0.2739 | 1.457 | 0.2437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860 | 4520 | 743.1 | 3704 |
| HPA replicas, mean | 3.976 | 4.017 | 4.082 | 4.312 |
| pods started | 0 | 0.5 | 0.3 | 1.8 |
| pod start wait, total (s) | 0 | 0.9 | 0.3 | 3 |
| pod start wait, mean (s) | 0 | 0.55 | 0.3 | 1.217 |
| host CPU busy, the real machine under kind (%) | 45.28 | 13.42 | 46.85 | 14.36 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 802.3 | 1505 | 812.3 | 1503 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 7.963 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1158 | 0.06667 | 1156 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1474 | 0.4 | 1472 |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 1158 | 119.8 | 1156 |
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
| worker nodes in service, mean | 12 | 7.182 | −40.1% | −5.2958 to −4.3394 | yes: GAIN |
| node-hours | 5.022 | 3.001 | −40.3% | −2.2104 to −1.8331 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504 | 503.1 | −0.2% | −2.3534 to +0.6701 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504 | 352.2 | −30.1% | −165.7775 to −137.8682 | yes: GAIN |
| response time (ms), mean | 113.8 | 66.73 | −41.4% | −59.2653 to −34.9648 | yes: GAIN |
| response time (ms), 95th percentile | 155.1 | 82.19 | −47.0% | −88.0420 to −57.8720 | yes: GAIN |
| response time (ms), 99th percentile | 175.2 | 107.5 | −38.7% | −80.8892 to −54.5972 | yes: GAIN |
| time over the response line (% of samples) | 0.003846 | 0 | −100.0% | −0.0125 to +0.0049 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.4 | +25.400 (native is 0) | +23.2620 to +27.5380 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.07667 | +0.077 (native is 0) | −0.0117 to +0.1650 | no |
| utilisation (used / allocatable) | 0.005706 | 0.008144 | +42.7% | +0.0021 to +0.0027 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2739 | 0.2358 | −13.9% | −0.0449 to −0.0312 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00792 | +0.008 (native is 0) | +0.0069 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2739 | 0.2437 | −11.0% | −0.0375 to −0.0228 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4520 | 3704 | −18.1% | −937.1793 to −695.2307 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.017 | 4.312 | +7.3% | +0.0822 to +0.5078 | yes: power given |
| pods started | 0.5 | 1.8 | +260.0% | −0.2099 to +2.8099 | no |
| pod start wait, total (s) | 0.9 | 3 | +233.3% | −0.8095 to +5.0095 | no |
| pod start wait, mean (s) | 0.55 | 1.217 | +121.2% | −0.4601 to +1.7935 | no |
| host CPU busy, the real machine under kind (%) | 13.42 | 14.36 | +7.0% | +0.6504 to +1.2368 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1503 | −0.1% | −7.0265 to +2.8265 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1156 | −0.2% | −7.2148 to +2.9898 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 1472 | −0.1% | −7.2130 to +3.2130 | no |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1156 | −0.2% | −7.2148 to +2.9898 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.034 | 5.022 | −0.2% | −0.0247 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 504 | −3.8% | −22.4838 to −17.1706 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 504 | −3.8% | −22.4838 to −17.1706 | yes: GAIN |
| response time (ms), mean | 387.4 | 113.8 | −70.6% | −482.7314 to −64.3299 | yes: GAIN |
| response time (ms), 95th percentile | 1404 | 155.1 | −89.0% | −2260.2461 to −238.3849 | yes: GAIN |
| response time (ms), 99th percentile | 2089 | 175.2 | −91.6% | −3370.9974 to −455.8342 | yes: GAIN |
| time over the response line (% of samples) | 14.43 | 0.003846 | −100.0% | −26.5477 to −2.2960 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 0 | −100.0% | −12.8129 to −2.1871 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.898 | 0 | −100.0% | −14.1576 to −5.6391 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03116 | 0.005706 | −81.7% | −0.0289 to −0.0220 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.496 | 0.2739 | −81.7% | −1.3887 to −1.0553 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.496 | 0.2739 | −81.7% | −1.3887 to −1.0553 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860 | 4520 | +425.6% | +3181.9001 to +4139.0431 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.017 | +1.0% | −0.1795 to +0.2626 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.1900 to +1.9900 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.550 (native is 0) | −0.0909 to +1.1909 | no |
| host CPU busy, the real machine under kind (%) | 45.28 | 13.42 | −70.4% | −36.5663 to −27.1573 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.3 | 1505 | +87.6% | +633.6981 to +771.5019 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1158 | +1853353.3% | +1153.9753 to +1162.7164 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1474 | +368500.0% | +1469.8155 to +1478.1845 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 1158 | +922.9% | +972.4150 to +1117.9017 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.49 | −20.9% | −4.2842 to −0.7351 | yes: GAIN |
| node-hours | 5.034 | 3.977 | −21.0% | −1.8000 to −0.3139 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 523.1 | −0.1% | −2.3588 to +0.8682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 444.2 | −15.2% | −135.6642 to −23.5180 | yes: GAIN |
| response time (ms), mean | 387.4 | 369.6 | −4.6% | −38.5489 to +3.0374 | no |
| response time (ms), 95th percentile | 1404 | 1544 | +10.0% | +0.0614 to +279.6796 | yes: LOSS |
| response time (ms), 99th percentile | 2089 | 2381 | +14.0% | +22.5867 to +562.9701 | yes: LOSS |
| time over the response line (% of samples) | 14.43 | 14.71 | +2.0% | −1.5077 to +2.0811 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8.7 | +16.0% | −0.4101 to +2.8101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.2 | +103.200 (native is 0) | +55.2006 to +151.1994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.898 | 11.22 | +13.4% | −0.7406 to +3.3873 | no |
| utilisation (used / allocatable) | 0.03116 | 0.03839 | +23.2% | +0.0022 to +0.0122 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.496 | 1.445 | −3.4% | −0.1122 to +0.0101 | no |
| Omni's own CPU (cores), mean | 0 | 0.01235 | +0.012 (native is 0) | +0.0110 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.496 | 1.457 | −2.6% | −0.0998 to +0.0223 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860 | 743.1 | −13.6% | −199.2753 to −34.5001 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.082 | +2.7% | −0.0978 to +0.3108 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| host CPU busy, the real machine under kind (%) | 45.28 | 46.85 | +3.5% | +0.9174 to +2.2127 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.3 | 812.3 | +1.2% | −1.2949 to +21.2949 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 7.963 | −33.6% | −6.7613 to −1.3137 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.06667 | +6.7% | −0.0474 to +0.0557 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 119.8 | +5.8% | −0.4406 to +13.5073 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.49 | −20.9% | −4.2842 to −0.7351 | yes: GAIN |
| node-hours | 5.022 | 3.977 | −20.8% | −1.7853 to −0.3059 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504 | 523.1 | +3.8% | +16.1550 to +22.0089 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504 | 444.2 | −11.9% | −117.9747 to −1.5531 | yes: GAIN |
| response time (ms), mean | 113.8 | 369.6 | +224.7% | +46.4170 to +465.1327 | yes: LOSS |
| response time (ms), 95th percentile | 155.1 | 1544 | +895.4% | +314.3908 to +2463.9812 | yes: LOSS |
| response time (ms), 99th percentile | 175.2 | 2381 | +1258.9% | +545.3444 to +3867.0440 | yes: LOSS |
| time over the response line (% of samples) | 0.003846 | 14.71 | +382422.5% | +3.5222 to +25.8949 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.7 | +8.700 (native is 0) | +3.3466 to +14.0534 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.2 | +103.200 (native is 0) | +55.2006 to +151.1994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 11.22 | +11.222 (native is 0) | +6.8880 to +15.5553 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005706 | 0.03839 | +572.8% | +0.0304 to +0.0349 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2739 | 1.445 | +427.5% | +0.9560 to +1.3858 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01235 | +0.012 (native is 0) | +0.0110 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2739 | 1.457 | +432.0% | +0.9685 to +1.3980 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4520 | 743.1 | −83.6% | −4325.7421 to −3228.9765 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.017 | 4.082 | +1.6% | −0.0628 to +0.1927 | no |
| pods started | 0.5 | 0.3 | −40.0% | −1.0121 to +0.6121 | no |
| pod start wait, total (s) | 0.9 | 0.3 | −66.7% | −1.8707 to +0.6707 | no |
| pod start wait, mean (s) | 0.55 | 0.3 | −45.5% | −1.0972 to +0.5972 | no |
| host CPU busy, the real machine under kind (%) | 13.42 | 46.85 | +249.1% | +28.4058 to +38.4479 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 812.3 | −46.0% | −770.5289 to −614.6711 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.06667 | −100.0% | −1162.7252 to −1153.9581 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 0.4 | −100.0% | −1478.4223 to −1469.5777 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 119.8 | −89.7% | −1115.6264 to −961.6236 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.182 | −40.1% | −5.2958 to −4.3394 | yes: GAIN |
| node-hours | 5.034 | 3.001 | −40.4% | −2.2274 to −1.8388 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 503.1 | −3.9% | −24.1769 to −17.1608 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 352.2 | −32.8% | −183.9700 to −159.3302 | yes: GAIN |
| response time (ms), mean | 387.4 | 66.73 | −82.8% | −540.7770 to −100.5143 | yes: GAIN |
| response time (ms), 95th percentile | 1404 | 82.19 | −94.1% | −2343.9022 to −300.6428 | yes: GAIN |
| response time (ms), 99th percentile | 2089 | 107.5 | −94.9% | −3442.3737 to −519.9443 | yes: GAIN |
| time over the response line (% of samples) | 14.43 | 0 | −100.0% | −26.5553 to −2.2961 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 0 | −100.0% | −12.8129 to −2.1871 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.4 | +25.400 (native is 0) | +23.2620 to +27.5380 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.898 | 0.07667 | −99.2% | −14.0947 to −5.5486 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03116 | 0.008144 | −73.9% | −0.0264 to −0.0196 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.496 | 0.2358 | −84.2% | −1.4224 to −1.0977 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00792 | +0.008 (native is 0) | +0.0069 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.496 | 0.2437 | −83.7% | −1.4135 to −1.0908 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 860 | 3704 | +330.7% | +2454.4589 to +3234.0743 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.976 | 4.312 | +8.5% | +0.0310 to +0.6420 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.7444 to +2.8556 | yes: power given |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | +0.8674 to +5.1326 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.217 | +1.217 (native is 0) | +0.6984 to +1.7350 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.28 | 14.36 | −68.3% | −35.3697 to −26.4667 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.3 | 1503 | +87.3% | +627.6617 to +773.3383 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1156 | +1849973.3% | +1154.3016 to +1158.1651 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1472 | +368000.0% | +1469.8942 to +1474.1058 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 113.2 | 1156 | +921.0% | +966.2339 to +1119.8578 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*