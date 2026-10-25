# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.241 | 5.349 |
| node-hours | 2.515 | 2.517 | 2.193 | 2.241 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.8 | 270 | 270 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.8 | 246.1 | 249.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 251.8 | 254.1 | 243.5 | 266.2 |
| response time (ms), 95th percentile | 811.8 | 896.7 | 800 | 951.4 |
| response time (ms), 99th percentile | 1247 | 1386 | 1268 | 1573 |
| time over the response line (% of samples) | 10.77 | 9.73 | 9.705 | 10.85 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7 | 6.9 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 10.9 | 14.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.333 | 10.03 | 8.135 | 9.545 |
| utilisation (used / allocatable) | 0.05603 | 0.05607 | 0.06388 | 0.06049 |
| CPU used (cores), mean | 1.345 | 1.346 | 1.322 | 1.295 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01061 | 0.01175 |
| CPU used with Omni's own (cores), mean | 1.345 | 1.346 | 1.333 | 1.307 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.2 | 489.1 | 447.7 | 469.7 |
| HPA replicas, mean | 2.009 | 2.065 | 2.546 | 2.452 |
| pods started | 0.1 | 0.1 | 0.4 | 0.3 |
| pod start wait, total (s) | 0.2 | 0.2 | 1.3 | 1.2 |
| pod start wait, mean (s) | 0.2 | 0.2 | 0.95 | 1.2 |
| host CPU busy, the real machine under kind (%) | 38.39 | 39.16 | 38.58 | 39.92 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 752.3 | 755.6 | 751.8 | 759.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.741 | 4.875 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1458 | 0.04583 | 0.1292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | 0.2 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 58.64 | 65.19 | 57.38 | 68.27 |
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
| worker nodes in service, mean | 6 | 5.349 | −10.8% | −1.3556 to +0.0537 | no |
| node-hours | 2.517 | 2.241 | −11.0% | −0.5708 to +0.0184 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270 | −0.3% | −2.1238 to +0.4910 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 249.5 | −7.9% | −44.2175 to +1.5597 | no |
| response time (ms), mean | 254.1 | 266.2 | +4.8% | −13.9545 to +38.1536 | no |
| response time (ms), 95th percentile | 896.7 | 951.4 | +6.1% | −143.6703 to +253.0243 | no |
| response time (ms), 99th percentile | 1386 | 1573 | +13.5% | −206.4013 to +580.1411 | no |
| time over the response line (% of samples) | 9.73 | 10.85 | +11.5% | −0.3997 to +2.6346 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.7 | +10.0% | −0.4209 to +1.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.100 (native is 0) | +9.6976 to +18.5024 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.03 | 9.545 | −4.9% | −1.7370 to +0.7604 | no |
| utilisation (used / allocatable) | 0.05607 | 0.06049 | +7.9% | −0.0005 to +0.0093 | no |
| CPU used (cores), mean | 1.346 | 1.295 | −3.7% | −0.1281 to +0.0274 | no |
| Omni's own CPU (cores), mean | 0 | 0.01175 | +0.012 (native is 0) | +0.0104 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.346 | 1.307 | −2.9% | −0.1171 to +0.0399 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.1 | 469.7 | −4.0% | −41.6051 to +2.7449 | no |
| HPA replicas, mean | 2.065 | 2.452 | +18.7% | +0.2220 to +0.5514 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | −0.9371 to +2.9371 | no |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | −0.9371 to +2.9371 | no |
| host CPU busy, the real machine under kind (%) | 39.16 | 39.92 | +1.9% | +0.1792 to +1.3389 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.6 | 759.4 | +0.5% | +0.2828 to +7.3172 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.875 | −18.8% | −2.2937 to +0.0434 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.1292 | −11.4% | −0.0593 to +0.0259 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.19 | 68.27 | +4.7% | −0.6315 to +6.7982 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.517 | +0.1% | −0.0054 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.8 | +0.0% | −0.7636 to +0.9466 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.8 | +0.0% | −0.7636 to +0.9466 | no |
| response time (ms), mean | 251.8 | 254.1 | +0.9% | −18.7203 to +23.3160 | no |
| response time (ms), 95th percentile | 811.8 | 896.7 | +10.5% | −93.2017 to +262.9237 | no |
| response time (ms), 99th percentile | 1247 | 1386 | +11.2% | −122.8100 to +400.8428 | no |
| time over the response line (% of samples) | 10.77 | 9.73 | −9.6% | −2.3997 to +0.3249 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7 | −2.8% | −1.0121 to +0.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.333 | 10.03 | +20.4% | +0.3368 to +3.0632 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05603 | 0.05607 | +0.1% | −0.0007 to +0.0008 | no |
| CPU used (cores), mean | 1.345 | 1.346 | +0.1% | −0.0177 to +0.0197 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.345 | 1.346 | +0.1% | −0.0177 to +0.0197 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.2 | 489.1 | −0.0% | −6.1681 to +5.9587 | no |
| HPA replicas, mean | 2.009 | 2.065 | +2.8% | −0.1345 to +0.2474 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 39.16 | +2.0% | +0.3027 to +1.2418 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 752.3 | 755.6 | +0.4% | −2.5312 to +9.1312 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1458 | +288.9% | +0.0407 to +0.1760 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.64 | 65.19 | +11.2% | −2.0690 to +15.1607 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | −12.6% | −1.5040 to −0.0133 | yes: GAIN |
| node-hours | 2.515 | 2.193 | −12.8% | −0.6349 to −0.0100 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270 | −0.3% | −1.4935 to +0.0082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 246.1 | −9.1% | −48.1620 to −0.9899 | yes: GAIN |
| response time (ms), mean | 251.8 | 243.5 | −3.3% | −32.8782 to +16.2533 | no |
| response time (ms), 95th percentile | 811.8 | 800 | −1.5% | −131.1933 to +107.4873 | no |
| response time (ms), 99th percentile | 1247 | 1268 | +1.7% | −196.0398 to +238.3100 | no |
| time over the response line (% of samples) | 10.77 | 9.705 | −9.9% | −3.5916 to +1.4672 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 6.9 | −4.2% | −1.5639 to +0.9639 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.900 (native is 0) | +6.3453 to +15.4547 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.333 | 8.135 | −2.4% | −1.7647 to +1.3681 | no |
| utilisation (used / allocatable) | 0.05603 | 0.06388 | +14.0% | −0.0005 to +0.0162 | no |
| CPU used (cores), mean | 1.345 | 1.322 | −1.7% | −0.0566 to +0.0117 | no |
| Omni's own CPU (cores), mean | 0 | 0.01061 | +0.011 (native is 0) | +0.0093 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.333 | −0.9% | −0.0462 to +0.0226 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.2 | 447.7 | −8.5% | −85.0004 to +2.0256 | no |
| HPA replicas, mean | 2.009 | 2.546 | +26.7% | +0.2933 to +0.7813 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | −0.4977 to +2.6977 | no |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | −0.1618 to +1.6618 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 38.58 | +0.5% | −0.4055 to +0.7922 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 752.3 | 751.8 | −0.1% | −4.8084 to +3.8084 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.741 | −21.0% | −2.4408 to −0.0772 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04583 | +22.2% | −0.0378 to +0.0545 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.64 | 57.38 | −2.2% | −7.3820 to +4.8570 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | −12.6% | −1.5040 to −0.0133 | yes: GAIN |
| node-hours | 2.517 | 2.193 | −12.9% | −0.6355 to −0.0127 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270 | −0.3% | −1.8564 to +0.1882 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 246.1 | −9.1% | −48.1357 to −1.1992 | yes: GAIN |
| response time (ms), mean | 254.1 | 243.5 | −4.2% | −33.3196 to +12.0989 | no |
| response time (ms), 95th percentile | 896.7 | 800 | −10.8% | −303.5489 to +110.1209 | no |
| response time (ms), 99th percentile | 1386 | 1268 | −8.5% | −356.5622 to +120.7996 | no |
| time over the response line (% of samples) | 9.73 | 9.705 | −0.3% | −1.4063 to +1.3567 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 6.9 | −1.4% | −1.1900 to +0.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.900 (native is 0) | +6.3453 to +15.4547 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.03 | 8.135 | −18.9% | −4.0350 to +0.2384 | no |
| utilisation (used / allocatable) | 0.05607 | 0.06388 | +13.9% | −0.0005 to +0.0161 | no |
| CPU used (cores), mean | 1.346 | 1.322 | −1.7% | −0.0536 to +0.0068 | no |
| Omni's own CPU (cores), mean | 0 | 0.01061 | +0.011 (native is 0) | +0.0093 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.346 | 1.333 | −1.0% | −0.0432 to +0.0176 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.1 | 447.7 | −8.5% | −83.9407 to +1.1753 | no |
| HPA replicas, mean | 2.065 | 2.546 | +23.3% | +0.2508 to +0.7109 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | −0.7607 to +2.9607 | no |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | −0.5695 to +2.0695 | no |
| host CPU busy, the real machine under kind (%) | 39.16 | 38.58 | −1.5% | −0.9512 to −0.2067 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.6 | 751.8 | −0.5% | −8.7189 to +1.1189 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.741 | −21.0% | −2.4408 to −0.0772 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.04583 | −68.6% | −0.1759 to −0.0241 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.2 | −66.7% | −0.7694 to −0.0306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 65.19 | 57.38 | −12.0% | −15.5071 to −0.1096 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.349 | −10.8% | −1.3556 to +0.0537 | no |
| node-hours | 2.515 | 2.241 | −10.9% | −0.5691 to +0.0201 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270 | −0.3% | −1.6774 to +0.2276 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 249.5 | −7.8% | −44.1016 to +1.6269 | no |
| response time (ms), mean | 251.8 | 266.2 | +5.7% | −9.5013 to +38.2962 | no |
| response time (ms), 95th percentile | 811.8 | 951.4 | +17.2% | −19.5934 to +298.6694 | no |
| response time (ms), 99th percentile | 1247 | 1573 | +26.1% | −125.4034 to +777.1760 | no |
| time over the response line (% of samples) | 10.77 | 10.85 | +0.7% | −0.5085 to +0.6687 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.7 | +6.9% | −0.4685 to +1.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.100 (native is 0) | +9.6976 to +18.5024 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.333 | 9.545 | +14.5% | −1.0199 to +3.4433 | no |
| utilisation (used / allocatable) | 0.05603 | 0.06049 | +8.0% | −0.0004 to +0.0093 | no |
| CPU used (cores), mean | 1.345 | 1.295 | −3.7% | −0.1222 to +0.0235 | no |
| Omni's own CPU (cores), mean | 0 | 0.01175 | +0.012 (native is 0) | +0.0104 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.307 | −2.8% | −0.1113 to +0.0362 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.2 | 469.7 | −4.0% | −41.0016 to +1.9320 | no |
| HPA replicas, mean | 2.009 | 2.452 | +22.1% | +0.1658 to +0.7206 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | −0.3903 to +2.3903 | no |
| pod start wait, mean (s) | 0.2 | 1.2 | +500.0% | −0.3903 to +2.3903 | no |
| host CPU busy, the real machine under kind (%) | 38.39 | 39.92 | +4.0% | +0.9587 to +2.1039 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 752.3 | 759.4 | +0.9% | +0.0554 to +14.1446 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.875 | −18.8% | −2.2937 to +0.0434 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.1292 | +244.4% | +0.0307 to +0.1526 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.64 | 68.27 | +16.4% | −0.0965 to +19.3549 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*