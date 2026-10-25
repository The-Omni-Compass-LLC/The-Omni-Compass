# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.822 | 5.83 |
| node-hours | 2.515 | 2.517 | 2.438 | 2.44 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 | 273 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 273.3 | 267.4 | 267.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 400.3 | 388.4 | 404.6 | 401.2 |
| response time (ms), 95th percentile | 1448 | 1459 | 1530 | 1573 |
| response time (ms), 99th percentile | 2244 | 2352 | 2349 | 2533 |
| time over the response line (% of samples) | 20.91 | 19.03 | 21.1 | 19.73 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 10.9 | 11.3 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 13.8 | 14 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.42 | 13.75 | 12.89 | 13.43 |
| utilisation (used / allocatable) | 0.063 | 0.06301 | 0.0647 | 0.06482 |
| CPU used (cores), mean | 1.512 | 1.512 | 1.509 | 1.512 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01227 | 0.01309 |
| CPU used with Omni's own (cores), mean | 1.512 | 1.512 | 1.521 | 1.525 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 434.6 | 426.4 | 426.1 |
| HPA replicas, mean | 2.169 | 2.002 | 2.618 | 2.503 |
| pods started | 0 | 0 | 0.7 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 1.2 | 1.3 |
| pod start wait, mean (s) | 0 | 0 | 1.2 | 1.3 |
| host CPU busy, the real machine under kind (%) | 43.38 | 44.17 | 43.8 | 44.6 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 789.3 | 793.6 | 791.2 | 795.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.653 | 5.661 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2542 | 0.09167 | 0.2083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | 0.6 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 98.48 | 106.2 | 101.6 | 109.3 |
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
| worker nodes in service, mean | 6 | 5.83 | −2.8% | −0.4511 to +0.1109 | no |
| node-hours | 2.517 | 2.44 | −3.0% | −0.1929 to +0.0408 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.9 | −0.1% | −1.3172 to +0.5932 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 267.6 | −2.1% | −14.8333 to +3.4468 | no |
| response time (ms), mean | 388.4 | 401.2 | +3.3% | −2.2112 to +27.8113 | no |
| response time (ms), 95th percentile | 1459 | 1573 | +7.8% | −13.0546 to +241.6366 | no |
| response time (ms), 99th percentile | 2352 | 2533 | +7.7% | −31.5379 to +393.8427 | no |
| time over the response line (% of samples) | 19.03 | 19.73 | +3.7% | −0.0410 to +1.4473 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11 | +0.9% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14 | +14.000 (native is 0) | +10.3216 to +17.6784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.75 | 13.43 | −2.4% | −1.8993 to +1.2526 | no |
| utilisation (used / allocatable) | 0.06301 | 0.06482 | +2.9% | +0.0001 to +0.0035 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.512 | 1.512 | −0.0% | −0.0356 to +0.0347 | no |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.013 (native is 0) | +0.0120 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.525 | +0.8% | −0.0223 to +0.0475 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.6 | 426.1 | −2.0% | −15.1565 to −1.8946 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.503 | +25.0% | +0.2488 to +0.7537 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.1295 to +2.4705 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.300 (native is 0) | +0.1295 to +2.4705 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.17 | 44.6 | +1.0% | −0.1848 to +1.0476 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.6 | 795.9 | +0.3% | −1.8167 to +6.4167 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.661 | −5.6% | −0.8871 to +0.2101 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.2083 | −18.0% | −0.1208 to +0.0291 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | −11.1% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.2 | 109.3 | +3.0% | −0.2868 to +6.5534 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.517 | +0.1% | −0.0096 to +0.0123 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 | +0.0% | −1.0377 to +1.2129 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 273.3 | +0.0% | −1.0377 to +1.2129 | no |
| response time (ms), mean | 400.3 | 388.4 | −3.0% | −24.5455 to +0.8374 | no |
| response time (ms), 95th percentile | 1448 | 1459 | +0.7% | −71.2526 to +92.7216 | no |
| response time (ms), 99th percentile | 2244 | 2352 | +4.8% | −142.1989 to +359.0285 | no |
| time over the response line (% of samples) | 20.91 | 19.03 | −9.0% | −3.2336 to −0.5263 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 10.9 | −5.2% | −1.3689 to +0.1689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.42 | 13.75 | +10.7% | +0.0979 to +2.5555 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.063 | 0.06301 | +0.0% | −0.0007 to +0.0007 | no |
| CPU used (cores), mean | 1.512 | 1.512 | +0.0% | −0.0164 to +0.0170 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.512 | 1.512 | +0.0% | −0.0164 to +0.0170 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 434.6 | −0.1% | −6.3444 to +5.0833 | no |
| HPA replicas, mean | 2.169 | 2.002 | −7.7% | −0.3290 to −0.0060 | yes: GAIN |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.38 | 44.17 | +1.8% | +0.3642 to +1.1982 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 789.3 | 793.6 | +0.5% | −0.2746 to +8.8746 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2542 | +205.0% | +0.1014 to +0.2403 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.48 | 106.2 | +7.8% | +3.6181 to +11.7402 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.822 | −3.0% | −0.4459 to +0.0904 | no |
| node-hours | 2.515 | 2.438 | −3.1% | −0.1915 to +0.0377 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | −0.1% | −1.2759 to +0.9069 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 267.4 | −2.1% | −14.6743 to +3.1469 | no |
| response time (ms), mean | 400.3 | 404.6 | +1.1% | −9.6081 to +18.1788 | no |
| response time (ms), 95th percentile | 1448 | 1530 | +5.7% | −14.0949 to +177.9579 | no |
| response time (ms), 99th percentile | 2244 | 2349 | +4.7% | −98.7061 to +308.5871 | no |
| time over the response line (% of samples) | 20.91 | 21.1 | +0.9% | −0.5071 to +0.8918 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 11.3 | −1.7% | −1.2556 to +0.8556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.8 | +13.800 (native is 0) | +10.3316 to +17.2684 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.42 | 12.89 | +3.8% | −1.5065 to +2.4432 | no |
| utilisation (used / allocatable) | 0.063 | 0.0647 | +2.7% | −0.0005 to +0.0039 | no |
| CPU used (cores), mean | 1.512 | 1.509 | −0.2% | −0.0310 to +0.0255 | no |
| Omni's own CPU (cores), mean | 0 | 0.01227 | +0.012 (native is 0) | +0.0111 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.521 | +0.6% | −0.0185 to +0.0375 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 426.4 | −2.0% | −20.4234 to +2.6361 | no |
| HPA replicas, mean | 2.169 | 2.618 | +20.7% | +0.2061 to +0.6913 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.3545 to +1.0455 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.38 | 43.8 | +1.0% | +0.0327 to +0.8067 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 789.3 | 791.2 | +0.2% | −3.1292 to +6.9292 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.653 | −5.8% | −0.8711 to +0.1765 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.09167 | +10.0% | −0.0419 to +0.0586 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.48 | 101.6 | +3.1% | −1.6806 to +7.8722 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.822 | −3.0% | −0.4459 to +0.0904 | no |
| node-hours | 2.517 | 2.438 | −3.1% | −0.1911 to +0.0346 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | −0.1% | −0.8565 to +0.3122 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 267.4 | −2.1% | −14.5514 to +2.8487 | no |
| response time (ms), mean | 388.4 | 404.6 | +4.2% | +1.3448 to +30.9341 | yes: LOSS |
| response time (ms), 95th percentile | 1459 | 1530 | +4.9% | −49.7258 to +192.1198 | no |
| response time (ms), 99th percentile | 2352 | 2349 | −0.1% | −142.2906 to +135.3420 | no |
| time over the response line (% of samples) | 19.03 | 21.1 | +10.9% | +0.9575 to +3.1871 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.3 | +3.7% | −0.8707 to +1.6707 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.8 | +13.800 (native is 0) | +10.3316 to +17.2684 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.75 | 12.89 | −6.2% | −2.9394 to +1.2227 | no |
| utilisation (used / allocatable) | 0.06301 | 0.0647 | +2.7% | −0.0006 to +0.0040 | no |
| CPU used (cores), mean | 1.512 | 1.509 | −0.2% | −0.0398 to +0.0336 | no |
| Omni's own CPU (cores), mean | 0 | 0.01227 | +0.012 (native is 0) | +0.0111 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.521 | +0.6% | −0.0275 to +0.0459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.6 | 426.4 | −1.9% | −21.4662 to +4.9400 | no |
| HPA replicas, mean | 2.002 | 2.618 | +30.8% | +0.4231 to +0.8093 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.3545 to +1.0455 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.3879 to +2.0121 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.17 | 43.8 | −0.8% | −1.0201 to +0.2971 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.6 | 791.2 | −0.3% | −8.2034 to +3.4034 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.653 | −5.8% | −0.8711 to +0.1765 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.09167 | −63.9% | −0.2079 to −0.1171 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.6 | −33.3% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.2 | 101.6 | −4.3% | −10.2045 to +1.0378 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.83 | −2.8% | −0.4511 to +0.1109 | no |
| node-hours | 2.515 | 2.44 | −3.0% | −0.1974 to +0.0479 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.9 | −0.1% | −1.3878 to +0.8392 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 267.6 | −2.1% | −15.2968 to +4.0857 | no |
| response time (ms), mean | 400.3 | 401.2 | +0.2% | −8.7338 to +10.6257 | no |
| response time (ms), 95th percentile | 1448 | 1573 | +8.6% | +20.0794 to +229.9716 | yes: LOSS |
| response time (ms), 99th percentile | 2244 | 2533 | +12.9% | +85.6611 to +493.4733 | yes: LOSS |
| time over the response line (% of samples) | 20.91 | 19.73 | −5.6% | −2.1758 to −0.1778 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 11 | −4.3% | −1.2726 to +0.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14 | +14.000 (native is 0) | +10.3216 to +17.6784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.42 | 13.42 | +8.1% | −1.0073 to +3.0140 | no |
| utilisation (used / allocatable) | 0.063 | 0.06482 | +2.9% | −0.0004 to +0.0040 | no |
| CPU used (cores), mean | 1.512 | 1.512 | −0.0% | −0.0267 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.013 (native is 0) | +0.0120 to +0.0142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.525 | +0.9% | −0.0132 to +0.0390 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.3 | 426.1 | −2.1% | −19.4397 to +1.1274 | no |
| HPA replicas, mean | 2.169 | 2.503 | +15.4% | −0.0172 to +0.6846 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.1295 to +2.4705 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.300 (native is 0) | +0.1295 to +2.4705 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.38 | 44.6 | +2.8% | +0.8923 to +1.5329 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 789.3 | 795.9 | +0.8% | +1.8768 to +11.3232 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.661 | −5.6% | −0.8871 to +0.2101 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.2083 | +150.0% | +0.0407 to +0.2093 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.48 | 109.3 | +11.0% | +5.3425 to +16.2825 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*