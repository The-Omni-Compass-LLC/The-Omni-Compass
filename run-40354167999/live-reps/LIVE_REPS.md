# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.72 | 11.63 |
| node-hours | 5.032 | 5.035 | 4.912 | 4.876 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | 527 | 529.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | 518.2 | 517.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 722.1 | 1046 | 666.7 | 1027 |
| response time (ms), 95th percentile | 2941 | 4548 | 3014 | 5215 |
| response time (ms), 99th percentile | 4221 | 6338 | 4336 | 7031 |
| time over the response line (% of samples) | 27.78 | 34.2 | 27.55 | 31.92 |
| failed requests (%) | 0.01594 | 0.1745 | 0.006969 | 0.4363 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 17.6 | 14.7 | 18.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.5 | 28.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.57 | 55.31 | 15.97 | 26.31 |
| utilisation (used / allocatable) | 0.03631 | 0.03586 | 0.03723 | 0.0403 |
| CPU used (cores), mean | 1.743 | 1.721 | 1.748 | 1.883 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0133 | 0.01103 |
| CPU used with Omni's own (cores), mean | 1.743 | 1.721 | 1.761 | 1.894 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.4 | 747.2 | 713.2 | 664.2 |
| HPA replicas, mean | 4.055 | 4.081 | 4.421 | 4.427 |
| pods started | 0.2 | 0.3 | 0.9 | 0.8 |
| pod start wait, total (s) | 0.6 | 0.9 | 1.5 | 1.7 |
| pod start wait, mean (s) | 0.6 | 0.6 | 0.775 | 1.2 |
| host CPU busy, the real machine under kind (%) | 53.34 | 61.8 | 54.64 | 64.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 893.8 | 1056 | 900.6 | 1084 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.41 | 11.25 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 3.392 | 0.1042 | 4.508 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 33.5 | 0.7 | 32.5 |
| queue: job turnaround, submitted to done, mean (s) | 205.2 | 354.6 | 205.9 | 383.3 |
| queue: jobs unfinished at the window's end | 0 | 0.1 | 0 | 0 |

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
| worker nodes in service, mean | 12 | 11.63 | −3.1% | −0.9487 to +0.2152 | no |
| node-hours | 5.035 | 4.876 | −3.2% | −0.3936 to +0.0750 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 529.1 | +0.3% | −0.9640 to +4.3538 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 517.6 | −1.9% | −28.1259 to +8.4699 | no |
| response time (ms), mean | 1046 | 1027 | −1.8% | −307.0732 to +269.2198 | no |
| response time (ms), 95th percentile | 4548 | 5215 | +14.7% | +192.4368 to +1142.8152 | yes: LOSS |
| response time (ms), 99th percentile | 6338 | 7031 | +10.9% | +224.0441 to +1161.9231 | yes: LOSS |
| time over the response line (% of samples) | 34.2 | 31.92 | −6.7% | −11.1345 to +6.5820 | no |
| failed requests (%) | 0.1745 | 0.4363 | +150.1% | +0.0442 to +0.4794 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 18.2 | +3.4% | −0.6251 to +1.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.400 (native is 0) | +23.7618 to +33.0382 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 55.31 | 26.31 | −52.4% | −98.3485 to +40.3552 | no |
| utilisation (used / allocatable) | 0.03586 | 0.0403 | +12.4% | +0.0006 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.721 | 1.883 | +9.4% | −0.0340 to +0.3566 | no |
| Omni's own CPU (cores), mean | 0 | 0.01103 | +0.011 (native is 0) | +0.0104 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.721 | 1.894 | +10.0% | −0.0231 to +0.3677 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747.2 | 664.2 | −11.1% | −169.2515 to +3.3356 | no |
| HPA replicas, mean | 4.081 | 4.427 | +8.5% | +0.1329 to +0.5585 | yes: power given |
| pods started | 0.3 | 0.8 | +166.7% | −0.5256 to +1.5256 | no |
| pod start wait, total (s) | 0.9 | 1.7 | +88.9% | −1.6733 to +3.2733 | no |
| pod start wait, mean (s) | 0.6 | 1.2 | +100.0% | −1.0588 to +2.2588 | no |
| host CPU busy, the real machine under kind (%) | 61.8 | 64.06 | +3.7% | −0.7693 to +5.2953 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1056 | 1084 | +2.6% | −43.9856 to +98.3856 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 11.17 | −6.9% | −2.1664 to +0.4997 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.392 | 4.508 | +32.9% | −2.0615 to +4.2948 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.5 | 32.5 | −3.0% | −4.0348 to +2.0348 | no |
| queue: job turnaround, submitted to done, mean (s) | 354.6 | 383.3 | +8.1% | −51.8636 to +109.2470 | no |
| queue: jobs unfinished at the window's end | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.032 | 5.035 | +0.1% | −0.0185 to +0.0245 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.4 | +0.0% | −3.4056 to +3.9095 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 527.4 | +0.0% | −3.4056 to +3.9095 | no |
| response time (ms), mean | 722.1 | 1046 | +44.9% | +90.1736 to +558.1196 | yes: LOSS |
| response time (ms), 95th percentile | 2941 | 4548 | +54.6% | +1053.5696 to +2160.1904 | yes: LOSS |
| response time (ms), 99th percentile | 4221 | 6338 | +50.1% | +1430.7036 to +2802.1424 | yes: LOSS |
| time over the response line (% of samples) | 27.78 | 34.2 | +23.1% | −2.9273 to +15.7762 | no |
| failed requests (%) | 0.01594 | 0.1745 | +994.8% | −0.0313 to +0.3484 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 17.6 | +24.8% | +2.4744 to +4.5256 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.57 | 55.31 | +214.8% | −31.0303 to +106.5103 | no |
| utilisation (used / allocatable) | 0.03631 | 0.03586 | −1.2% | −0.0050 to +0.0041 | no |
| CPU used (cores), mean | 1.743 | 1.721 | −1.2% | −0.2381 to +0.1949 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.743 | 1.721 | −1.2% | −0.2381 to +0.1949 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.4 | 747.2 | +2.3% | −82.0008 to +115.5358 | no |
| HPA replicas, mean | 4.055 | 4.081 | +0.6% | −0.1457 to +0.1974 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.6 | 0.9 | +50.0% | −0.9181 to +1.5181 | no |
| pod start wait, mean (s) | 0.6 | 0.6 | ±0.0% | −1.0116 to +1.0116 | no |
| host CPU busy, the real machine under kind (%) | 53.34 | 61.8 | +15.9% | +6.1790 to +10.7340 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 893.8 | 1056 | +18.2% | +88.2729 to +237.1271 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 3.392 | +3291.7% | −3.1597 to +9.7430 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 33.5 | +4685.7% | −40.1386 to +105.7386 | no |
| queue: job turnaround, submitted to done, mean (s) | 205.2 | 354.6 | +72.8% | +74.1641 to +224.6109 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.72 | −2.3% | −0.7211 to +0.1611 | no |
| node-hours | 5.032 | 4.912 | −2.4% | −0.3180 to +0.0781 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527 | −0.0% | −2.3073 to +1.9637 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 518.2 | −1.7% | −24.2437 to +6.3543 | no |
| response time (ms), mean | 722.1 | 666.7 | −7.7% | −120.8014 to +10.0508 | no |
| response time (ms), 95th percentile | 2941 | 3014 | +2.5% | −241.5208 to +388.0488 | no |
| response time (ms), 99th percentile | 4221 | 4336 | +2.7% | −292.2872 to +520.8030 | no |
| time over the response line (% of samples) | 27.78 | 27.55 | −0.8% | −2.8316 to +2.3790 | no |
| failed requests (%) | 0.01594 | 0.006969 | −56.3% | −0.0293 to +0.0113 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 14.7 | +4.3% | −0.5778 to +1.7778 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.5 | +49.500 (native is 0) | +13.5393 to +85.4607 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.57 | 15.97 | −9.1% | −4.8279 to +1.6346 | no |
| utilisation (used / allocatable) | 0.03631 | 0.03723 | +2.5% | −0.0003 to +0.0021 | no |
| CPU used (cores), mean | 1.743 | 1.748 | +0.3% | −0.0257 to +0.0359 | no |
| Omni's own CPU (cores), mean | 0 | 0.0133 | +0.013 (native is 0) | +0.0122 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.743 | 1.761 | +1.1% | −0.0117 to +0.0485 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.4 | 713.2 | −2.4% | −39.0315 to +4.5197 | no |
| HPA replicas, mean | 4.055 | 4.421 | +9.0% | +0.0323 to +0.6997 | yes: power given |
| pods started | 0.2 | 0.9 | +350.0% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 0.6 | 1.5 | +150.0% | −1.1635 to +2.9635 | no |
| pod start wait, mean (s) | 0.6 | 0.775 | +29.2% | −1.0114 to +1.3614 | no |
| host CPU busy, the real machine under kind (%) | 53.34 | 54.64 | +2.4% | +0.1240 to +2.4824 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 893.8 | 900.6 | +0.8% | −10.4921 to +24.0921 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 11.41 | −4.9% | −1.4533 to +0.2804 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.1042 | +4.2% | −0.0681 to +0.0764 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | ±0.0% | −0.5840 to +0.5840 | no |
| queue: job turnaround, submitted to done, mean (s) | 205.2 | 205.9 | +0.3% | −18.4474 to +19.7308 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.72 | −2.3% | −0.7211 to +0.1611 | no |
| node-hours | 5.035 | 4.912 | −2.4% | −0.3038 to +0.0578 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 527 | −0.1% | −3.0083 to +2.1608 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 518.2 | −1.7% | −22.6133 to +4.2200 | no |
| response time (ms), mean | 1046 | 666.7 | −36.3% | −673.6944 to −85.3494 | yes: GAIN |
| response time (ms), 95th percentile | 4548 | 3014 | −33.7% | −2155.5759 to −911.6561 | yes: GAIN |
| response time (ms), 99th percentile | 6338 | 4336 | −31.6% | −2740.3850 to −1263.9452 | yes: GAIN |
| time over the response line (% of samples) | 34.2 | 27.55 | −19.4% | −16.7496 to +3.4481 | no |
| failed requests (%) | 0.1745 | 0.006969 | −96.0% | −0.3753 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 14.7 | −16.5% | −4.0898 to −1.7102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.5 | +49.500 (native is 0) | +13.5393 to +85.4607 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 55.31 | 15.97 | −71.1% | −109.6056 to +30.9323 | no |
| utilisation (used / allocatable) | 0.03586 | 0.03723 | +3.8% | −0.0030 to +0.0057 | no |
| CPU used (cores), mean | 1.721 | 1.748 | +1.6% | −0.1698 to +0.2232 | no |
| Omni's own CPU (cores), mean | 0 | 0.0133 | +0.013 (native is 0) | +0.0122 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.721 | 1.761 | +2.3% | −0.1571 to +0.2371 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747.2 | 713.2 | −4.6% | −128.5616 to +60.5149 | no |
| HPA replicas, mean | 4.081 | 4.421 | +8.3% | −0.0678 to +0.7481 | no |
| pods started | 0.3 | 0.9 | +200.0% | −0.5778 to +1.7778 | no |
| pod start wait, total (s) | 0.9 | 1.5 | +66.7% | −1.9279 to +3.1279 | no |
| pod start wait, mean (s) | 0.6 | 0.775 | +29.2% | −1.1473 to +1.4973 | no |
| host CPU busy, the real machine under kind (%) | 61.8 | 54.64 | −11.6% | −10.3735 to −3.9331 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1056 | 900.6 | −14.8% | −241.0309 to −70.7691 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.45 | −4.6% | −1.5370 to +0.4314 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.392 | 0.1042 | −96.9% | −9.6982 to +3.1232 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.5 | 0.7 | −97.9% | −105.4872 to +39.8872 | no |
| queue: job turnaround, submitted to done, mean (s) | 354.6 | 205.9 | −41.9% | −239.7942 to −57.6974 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.63 | −3.1% | −0.9487 to +0.2152 | no |
| node-hours | 5.032 | 4.876 | −3.1% | −0.4089 to +0.0963 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 529.1 | +0.4% | +0.0176 to +3.8761 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 517.6 | −1.8% | −29.4476 to +10.2955 | no |
| response time (ms), mean | 722.1 | 1027 | +42.3% | +169.9260 to +440.5138 | yes: LOSS |
| response time (ms), 95th percentile | 2941 | 5215 | +77.3% | +1390.4443 to +3158.5677 | yes: LOSS |
| response time (ms), 99th percentile | 4221 | 7031 | +66.6% | +1810.9823 to +3807.8309 | yes: LOSS |
| time over the response line (% of samples) | 27.78 | 31.92 | +14.9% | +1.5522 to +6.7442 | yes: LOSS |
| failed requests (%) | 0.01594 | 0.4363 | +2637.7% | +0.1519 to +0.6888 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 18.2 | +29.1% | +3.3128 to +4.8872 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.400 (native is 0) | +23.7618 to +33.0382 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.57 | 26.31 | +49.8% | +2.0782 to +15.4085 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03631 | 0.0403 | +11.0% | +0.0028 to +0.0052 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.743 | 1.883 | +8.0% | +0.0695 to +0.2098 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01103 | +0.011 (native is 0) | +0.0104 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.743 | 1.894 | +8.6% | +0.0806 to +0.2208 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.4 | 664.2 | −9.1% | −87.6991 to −44.6818 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.055 | 4.427 | +9.2% | +0.1489 to +0.5942 | yes: power given |
| pods started | 0.2 | 0.8 | +300.0% | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0.6 | 1.7 | +183.3% | −0.7910 to +2.9910 | no |
| pod start wait, mean (s) | 0.6 | 1.2 | +100.0% | −0.9526 to +2.1526 | no |
| host CPU busy, the real machine under kind (%) | 53.34 | 64.06 | +20.1% | +8.4204 to +13.0185 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 893.8 | 1084 | +21.2% | +127.4759 to +252.3241 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.25 | −6.2% | −1.9347 to +0.4347 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 4.508 | +4408.3% | −1.8915 to +10.7081 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 32.5 | +4542.9% | −38.1221 to +101.7221 | no |
| queue: job turnaround, submitted to done, mean (s) | 205.2 | 383.3 | +86.8% | +120.0335 to +236.1248 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*