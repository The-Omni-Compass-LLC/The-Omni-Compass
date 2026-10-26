# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.653 | 6 |
| node-hours | 2.516 | 2.51 | 1.946 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 285.1 | 268.9 | 285.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 285.1 | 226.7 | 285.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 188.4 | 485.9 | 154.2 | 509.5 |
| response time (ms), 95th percentile | 496.6 | 1087 | 514.5 | 1149 |
| response time (ms), 99th percentile | 698.2 | 1527 | 754.4 | 1598 |
| time over the response line (% of samples) | 5.747 | 39.52 | 5.747 | 42.36 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 23.3 | 4.9 | 23.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 50.4 | 23 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.02 | 1.908 | 7.468 | 2.145 |
| utilisation (used / allocatable) | 0.05249 | 0.09513 | 0.06767 | 0.09517 |
| CPU used (cores), mean | 1.26 | 2.283 | 1.237 | 2.284 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0147 | 0.0081 |
| CPU used with Omni's own (cores), mean | 1.26 | 2.283 | 1.252 | 2.292 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.3 | 300.2 | 438.4 | 299.8 |
| HPA replicas, mean | 1.925 | 2.005 | 2.037 | 2.583 |
| pods started | 0.2 | 0.2 | 0.2 | 0.7 |
| pod start wait, total (s) | 0.5 | 0.5 | 0.4 | 1.9 |
| pod start wait, mean (s) | 0.5 | 0.25 | 0.4 | 1.1 |
| host CPU busy, the real machine under kind (%) | 36.1 | 71.92 | 36.42 | 72.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 732.3 | 1411 | 732.5 | 1416 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.677 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 435.6 | 0.05417 | 442.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 959 | 0.5 | 949.2 |
| queue: job turnaround, submitted to done, mean (s) | 39.16 | 825.7 | 39 | 817.1 |
| queue: jobs unfinished at the window's end | 0 | 9.8 | 0 | 10.1 |

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
| node-hours | 2.51 | 2.516 | +0.2% | −0.0047 to +0.0161 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.1 | 285.7 | +0.2% | −0.4192 to +1.6876 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.1 | 285.7 | +0.2% | −0.4192 to +1.6876 | no |
| response time (ms), mean | 485.9 | 509.5 | +4.8% | −2.5936 to +49.6914 | no |
| response time (ms), 95th percentile | 1087 | 1149 | +5.7% | +0.2071 to +124.1239 | yes: LOSS |
| response time (ms), 99th percentile | 1527 | 1598 | +4.7% | −26.2840 to +168.9272 | no |
| time over the response line (% of samples) | 39.52 | 42.36 | +7.2% | +0.2099 to +5.4629 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 23.5 | +0.9% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | +23.000 (native is 0) | +18.1838 to +27.8162 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.908 | 2.145 | +12.4% | −0.2443 to +0.7176 | no |
| utilisation (used / allocatable) | 0.09513 | 0.09517 | +0.0% | −0.0016 to +0.0017 | no |
| CPU used (cores), mean | 2.283 | 2.284 | +0.0% | −0.0389 to +0.0409 | no |
| Omni's own CPU (cores), mean | 0 | 0.0081 | +0.008 (native is 0) | +0.0071 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.283 | 2.292 | +0.4% | −0.0307 to +0.0489 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.2 | 299.8 | −0.1% | −6.0791 to +5.3256 | no |
| HPA replicas, mean | 2.005 | 2.583 | +28.9% | +0.3133 to +0.8436 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0.5 | 1.9 | +280.0% | +0.0854 to +2.7146 | yes: LOSS |
| pod start wait, mean (s) | 0.25 | 1.1 | +340.0% | −0.0742 to +1.7742 | no |
| host CPU busy, the real machine under kind (%) | 71.92 | 72.27 | +0.5% | −0.8463 to +1.5375 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1411 | 1416 | +0.4% | −15.4435 to +27.2435 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 435.6 | 442.4 | +1.6% | −62.6517 to +76.2569 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 959 | 949.2 | −1.0% | −76.4523 to +56.8153 | no |
| queue: job turnaround, submitted to done, mean (s) | 825.7 | 817.1 | −1.0% | −37.7636 to +20.5803 | no |
| queue: jobs unfinished at the window's end | 9.8 | 10.1 | +3.1% | −1.1326 to +1.7326 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.51 | −0.2% | −0.0150 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 285.1 | +5.7% | +13.6467 to +16.8894 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 285.1 | +5.7% | +13.6467 to +16.8894 | yes: power given |
| response time (ms), mean | 188.4 | 485.9 | +158.0% | +227.9087 to +367.2677 | yes: LOSS |
| response time (ms), 95th percentile | 496.6 | 1087 | +118.8% | +409.5325 to +770.8105 | yes: LOSS |
| response time (ms), 99th percentile | 698.2 | 1527 | +118.7% | +610.7175 to +1046.3967 | yes: LOSS |
| time over the response line (% of samples) | 5.747 | 39.52 | +587.7% | +24.2643 to +43.2829 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 23.3 | +441.9% | +16.1190 to +21.8810 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.02 | 1.908 | −76.2% | −7.7747 to −4.4486 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05249 | 0.09513 | +81.2% | +0.0376 to +0.0477 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.26 | 2.283 | +81.2% | +0.9030 to +1.1440 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.26 | 2.283 | +81.2% | +0.9030 to +1.1440 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.3 | 300.2 | −41.9% | −247.0645 to −185.0787 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.005 | +4.1% | +0.0038 to +0.1555 | yes: power given |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.5 | 0.5 | ±0.0% | −1.4698 to +1.4698 | no |
| pod start wait, mean (s) | 0.5 | 0.25 | −50.0% | −1.2790 to +0.7790 | no |
| host CPU busy, the real machine under kind (%) | 36.1 | 71.92 | +99.2% | +31.7671 to +39.8678 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 732.3 | 1411 | +92.6% | +568.5061 to +788.0939 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 435.6 | +804003.2% | +212.0593 to +658.9442 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 959 | +239660.0% | +537.6985 to +1379.5812 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 39.16 | 825.7 | +2008.6% | +607.2894 to +965.7689 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.8 | +9.800 (native is 0) | +4.2511 to +15.3489 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.653 | −22.4% | −2.0537 to −0.6402 | yes: GAIN |
| node-hours | 2.516 | 1.946 | −22.7% | −0.8670 to −0.2734 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 268.9 | −0.3% | −1.8884 to +0.1566 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 226.7 | −16.0% | −65.5150 to −20.6501 | yes: GAIN |
| response time (ms), mean | 188.4 | 154.2 | −18.1% | −43.5018 to −24.7276 | yes: GAIN |
| response time (ms), 95th percentile | 496.6 | 514.5 | +3.6% | −15.6533 to +51.4003 | no |
| response time (ms), 99th percentile | 698.2 | 754.4 | +8.0% | −0.1788 to +112.5454 | no |
| time over the response line (% of samples) | 5.747 | 5.747 | +0.0% | −0.9411 to +0.9428 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 4.9 | +14.0% | −0.3048 to +1.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | +50.400 (native is 0) | +36.8859 to +63.9141 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.02 | 7.468 | −6.9% | −1.3603 to +0.2569 | no |
| utilisation (used / allocatable) | 0.05249 | 0.06767 | +28.9% | +0.0068 to +0.0236 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.26 | 1.237 | −1.8% | −0.0521 to +0.0066 | no |
| Omni's own CPU (cores), mean | 0 | 0.0147 | +0.015 (native is 0) | +0.0129 to +0.0165 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.26 | 1.252 | −0.6% | −0.0381 to +0.0220 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.3 | 438.4 | −15.1% | −120.3768 to −35.2636 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.037 | +5.8% | −0.0501 to +0.2746 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.5 | 0.4 | −20.0% | −0.8113 to +0.6113 | no |
| pod start wait, mean (s) | 0.5 | 0.4 | −20.0% | −0.8113 to +0.6113 | no |
| host CPU busy, the real machine under kind (%) | 36.1 | 36.42 | +0.9% | −0.4829 to +1.1174 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 732.3 | 732.5 | +0.0% | −1.2621 to +1.6621 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.677 | −38.7% | −3.4591 to −1.1868 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.05417 | ±0.0% | −0.0526 to +0.0526 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 39.16 | 39 | −0.4% | −0.8981 to +0.5731 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.653 | −22.4% | −2.0537 to −0.6402 | yes: GAIN |
| node-hours | 2.51 | 1.946 | −22.5% | −0.8613 to −0.2668 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.1 | 268.9 | −5.7% | −17.7994 to −14.4685 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.1 | 226.7 | −20.5% | −80.8056 to −35.8957 | yes: GAIN |
| response time (ms), mean | 485.9 | 154.2 | −68.3% | −406.4602 to −256.9456 | yes: GAIN |
| response time (ms), 95th percentile | 1087 | 514.5 | −52.7% | −739.4229 to −405.1731 | yes: GAIN |
| response time (ms), 99th percentile | 1527 | 754.4 | −50.6% | −1024.7082 to −520.0394 | yes: GAIN |
| time over the response line (% of samples) | 39.52 | 5.747 | −85.5% | −43.3978 to −24.1478 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 4.9 | −79.0% | −20.9279 to −15.8721 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | +50.400 (native is 0) | +36.8859 to +63.9141 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.908 | 7.468 | +291.4% | +3.9644 to +7.1556 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09513 | 0.06767 | −28.9% | −0.0377 to −0.0173 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.283 | 1.237 | −45.8% | −1.1656 to −0.9268 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0147 | +0.015 (native is 0) | +0.0129 to +0.0165 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.283 | 1.252 | −45.2% | −1.1509 to −0.9122 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300.2 | 438.4 | +46.1% | +107.7834 to +168.7195 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.037 | +1.6% | −0.1410 to +0.2061 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.5 | 0.4 | −20.0% | −1.4676 to +1.2676 | no |
| pod start wait, mean (s) | 0.25 | 0.4 | +60.0% | −0.7429 to +1.0429 | no |
| host CPU busy, the real machine under kind (%) | 71.92 | 36.42 | −49.4% | −38.9249 to −32.0755 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1411 | 732.5 | −48.1% | −787.1439 to −569.0561 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 435.6 | 0.05417 | −100.0% | −658.9253 to −212.0781 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 959 | 0.5 | −99.9% | −1379.3936 to −537.6860 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 825.7 | 39 | −95.3% | −965.5200 to −607.8633 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.8 | 0 | −100.0% | −15.3489 to −4.2511 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.516 | −0.0% | −0.0067 to +0.0057 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 285.7 | +5.9% | +14.1269 to +17.6776 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 285.7 | +5.9% | +14.1269 to +17.6776 | yes: power given |
| response time (ms), mean | 188.4 | 509.5 | +170.5% | +249.7766 to +392.4977 | yes: LOSS |
| response time (ms), 95th percentile | 496.6 | 1149 | +131.4% | +512.3903 to +792.2837 | yes: LOSS |
| response time (ms), 99th percentile | 698.2 | 1598 | +128.9% | +708.2622 to +1091.4952 | yes: LOSS |
| time over the response line (% of samples) | 5.747 | 42.36 | +637.1% | +27.6088 to +45.6112 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 23.5 | +446.5% | +16.3229 to +22.0771 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | +23.000 (native is 0) | +18.1838 to +27.8162 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.02 | 2.145 | −73.3% | −7.6125 to −4.1375 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05249 | 0.09517 | +81.3% | +0.0380 to +0.0473 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.26 | 2.284 | +81.3% | +0.9129 to +1.1361 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0081 | +0.008 (native is 0) | +0.0071 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.26 | 2.292 | +82.0% | +0.9211 to +1.1441 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.3 | 299.8 | −41.9% | −246.6708 to −186.2261 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.583 | +34.2% | +0.3969 to +0.9193 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.5 | 1.9 | +280.0% | −0.9410 to +3.7410 | no |
| pod start wait, mean (s) | 0.5 | 1.1 | +120.0% | −0.6707 to +1.8707 | no |
| host CPU busy, the real machine under kind (%) | 36.1 | 72.27 | +100.2% | +32.5331 to +39.7930 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 732.3 | 1416 | +93.4% | +580.1820 to +788.2180 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 442.4 | +816561.8% | +212.6179 to +671.9908 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 949.2 | +237205.3% | +568.1297 to +1329.5129 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 39.16 | 817.1 | +1986.6% | +607.3263 to +948.5487 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.1 | +10.100 (native is 0) | +4.5444 to +15.6556 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*