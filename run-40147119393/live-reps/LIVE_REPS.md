# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.488 | 5.596 |
| node-hours | 2.516 | 2.518 | 2.302 | 2.344 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.1 | 272.9 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 273.1 | 256.8 | 259.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 334.4 | 410 | 305.6 | 363.3 |
| response time (ms), 95th percentile | 1087 | 1798 | 1154 | 1691 |
| response time (ms), 99th percentile | 1555 | 2766 | 1654 | 2787 |
| time over the response line (% of samples) | 20.56 | 17.85 | 20.84 | 17.52 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.3 | 10.8 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.9 | 40.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.74 | 16.16 | 9.817 | 17.02 |
| utilisation (used / allocatable) | 0.06064 | 0.06063 | 0.06698 | 0.06522 |
| CPU used (cores), mean | 1.455 | 1.455 | 1.456 | 1.453 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01695 | 0.01844 |
| CPU used with Omni's own (cores), mean | 1.455 | 1.455 | 1.473 | 1.472 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 452.6 | 420.6 | 429 |
| HPA replicas, mean | 2.089 | 2.041 | 2.347 | 2.268 |
| pods started | 0.3 | 0.3 | 0.7 | 0.5 |
| pod start wait, total (s) | 0.7 | 0.7 | 1.2 | 0.8 |
| pod start wait, mean (s) | 0.5 | 0.45 | 1.2 | 0.65 |
| host CPU busy, the real machine under kind (%) | 41.27 | 43.8 | 42.5 | 44.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.3 | 800.1 | 769.4 | 806.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.095 | 5.217 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.8833 | 0.075 | 0.8375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.7 | 0.5 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 72.45 | 113.1 | 78.5 | 117.2 |
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
| worker nodes in service, mean | 6 | 5.596 | −6.7% | −0.8993 to +0.0910 | no |
| node-hours | 2.518 | 2.344 | −6.9% | −0.3793 to +0.0322 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.6 | −0.2% | −1.0577 to +0.1966 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 259.9 | −4.8% | −28.7032 to +2.3838 | no |
| response time (ms), mean | 410 | 363.3 | −11.4% | −74.1077 to −19.4006 | yes: GAIN |
| response time (ms), 95th percentile | 1798 | 1691 | −6.0% | −276.7302 to +61.7302 | no |
| response time (ms), 99th percentile | 2766 | 2787 | +0.7% | −199.1068 to +240.3636 | no |
| time over the response line (% of samples) | 17.85 | 17.52 | −1.8% | −1.6964 to +1.0407 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.5 | +1.8% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 | +40.700 (native is 0) | +21.3969 to +60.0031 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.16 | 17.02 | +5.4% | −1.5074 to +3.2407 | no |
| utilisation (used / allocatable) | 0.06063 | 0.06522 | +7.6% | −0.0004 to +0.0096 | no |
| CPU used (cores), mean | 1.455 | 1.453 | −0.1% | −0.0338 to +0.0303 | no |
| Omni's own CPU (cores), mean | 0 | 0.01844 | +0.018 (native is 0) | +0.0167 to +0.0202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.455 | 1.472 | +1.1% | −0.0157 to +0.0491 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.6 | 429 | −5.2% | −50.4621 to +3.2523 | no |
| HPA replicas, mean | 2.041 | 2.268 | +11.1% | −0.0102 to +0.4631 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.7 | 0.8 | +14.3% | −1.3871 to +1.5871 | no |
| pod start wait, mean (s) | 0.45 | 0.65 | +44.4% | −0.6630 to +1.0630 | no |
| host CPU busy, the real machine under kind (%) | 43.8 | 44.8 | +2.3% | +0.5585 to +1.4499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800.1 | 806.4 | +0.8% | −1.5216 to +14.1216 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.217 | −13.0% | −1.6265 to +0.0608 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8833 | 0.8375 | −5.2% | −0.1283 to +0.0366 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.6 | −5.9% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.1 | 117.2 | +3.5% | −4.0467 to +12.0633 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.518 | +0.1% | −0.0052 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.1 | +0.1% | −0.4468 to +1.0983 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 273.1 | +0.1% | −0.4468 to +1.0983 | no |
| response time (ms), mean | 334.4 | 410 | +22.6% | +41.1006 to +110.2355 | yes: LOSS |
| response time (ms), 95th percentile | 1087 | 1798 | +65.5% | +407.6088 to +1015.7302 | yes: LOSS |
| response time (ms), 99th percentile | 1555 | 2766 | +78.0% | +713.5299 to +1710.2693 | yes: LOSS |
| time over the response line (% of samples) | 20.56 | 17.85 | −13.2% | −5.1780 to −0.2472 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.3 | +4.6% | −0.1952 to +1.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.74 | 16.16 | +50.4% | +3.7324 to +7.0976 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06064 | 0.06063 | −0.0% | −0.0011 to +0.0011 | no |
| CPU used (cores), mean | 1.455 | 1.455 | −0.0% | −0.0271 to +0.0266 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.455 | 1.455 | −0.0% | −0.0271 to +0.0266 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 452.6 | +0.2% | −8.0478 to +9.6547 | no |
| HPA replicas, mean | 2.089 | 2.041 | −2.3% | −0.2089 to +0.1136 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.7 | 0.7 | ±0.0% | −1.4698 to +1.4698 | no |
| pod start wait, mean (s) | 0.5 | 0.45 | −10.0% | −0.9804 to +0.8804 | no |
| host CPU busy, the real machine under kind (%) | 41.27 | 43.8 | +6.1% | +2.0752 to +2.9849 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 800.1 | +4.8% | +23.1620 to +50.4380 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.8833 | +1225.0% | +0.7395 to +0.8939 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.7 | +183.3% | +0.6940 to +1.5060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72.45 | 113.1 | +56.2% | +25.8743 to +55.5090 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.488 | −8.5% | −1.1250 to +0.1011 | no |
| node-hours | 2.516 | 2.302 | −8.5% | −0.4702 to +0.0426 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −0.9931 to +1.2779 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 256.8 | −5.8% | −35.3234 to +3.4624 | no |
| response time (ms), mean | 334.4 | 305.6 | −8.6% | −40.7915 to −16.7494 | yes: GAIN |
| response time (ms), 95th percentile | 1087 | 1154 | +6.2% | +17.6429 to +116.6831 | yes: LOSS |
| response time (ms), 99th percentile | 1555 | 1654 | +6.4% | +21.3085 to +176.8637 | yes: LOSS |
| time over the response line (% of samples) | 20.56 | 20.84 | +1.4% | −0.9345 to +1.4940 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.8 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.9 | +36.900 (native is 0) | +23.4059 to +50.3941 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.74 | 9.817 | −8.6% | −2.1935 to +0.3402 | no |
| utilisation (used / allocatable) | 0.06064 | 0.06698 | +10.5% | −0.0015 to +0.0141 | no |
| CPU used (cores), mean | 1.455 | 1.456 | +0.1% | −0.0222 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.01695 | +0.017 (native is 0) | +0.0159 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.455 | 1.473 | +1.2% | −0.0055 to +0.0413 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 420.6 | −6.9% | −70.6612 to +8.2832 | no |
| HPA replicas, mean | 2.089 | 2.347 | +12.3% | −0.0165 to +0.5322 | no |
| pods started | 0.3 | 0.7 | +133.3% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.7 | 1.2 | +71.4% | −0.5256 to +1.5256 | no |
| pod start wait, mean (s) | 0.5 | 1.2 | +140.0% | −0.1294 to +1.5294 | no |
| host CPU busy, the real machine under kind (%) | 41.27 | 42.5 | +3.0% | +1.0754 to +1.3945 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 769.4 | +0.8% | +3.3513 to +8.8487 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.095 | −15.1% | −1.8946 to +0.0856 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.075 | +12.5% | −0.0457 to +0.0624 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.45 | 78.5 | +8.3% | +2.3796 to +9.7038 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.488 | −8.5% | −1.1250 to +0.1011 | no |
| node-hours | 2.518 | 2.302 | −8.6% | −0.4761 to +0.0441 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.9 | −0.1% | −1.2690 to +0.9024 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 256.8 | −6.0% | −35.9878 to +3.4754 | no |
| response time (ms), mean | 410 | 305.6 | −25.5% | −139.4207 to −69.4563 | yes: GAIN |
| response time (ms), 95th percentile | 1798 | 1154 | −35.8% | −932.3330 to −356.6800 | yes: GAIN |
| response time (ms), 99th percentile | 2766 | 1654 | −40.2% | −1592.3739 to −633.2531 | yes: GAIN |
| time over the response line (% of samples) | 17.85 | 20.84 | +16.8% | +1.3445 to +4.6402 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 10.8 | −4.4% | −1.1079 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.9 | +36.900 (native is 0) | +23.4059 to +50.3941 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.16 | 9.817 | −39.2% | −8.6570 to −4.0263 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06063 | 0.06698 | +10.5% | −0.0016 to +0.0143 | no |
| CPU used (cores), mean | 1.455 | 1.456 | +0.1% | −0.0165 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.01695 | +0.017 (native is 0) | +0.0159 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.455 | 1.473 | +1.2% | +0.0008 to +0.0354 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.6 | 420.6 | −7.1% | −72.1286 to +8.1438 | no |
| HPA replicas, mean | 2.041 | 2.347 | +15.0% | +0.0549 to +0.5561 | yes: power given |
| pods started | 0.3 | 0.7 | +133.3% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.7 | 1.2 | +71.4% | −0.8593 to +1.8593 | no |
| pod start wait, mean (s) | 0.45 | 1.2 | +166.7% | −0.1925 to +1.6925 | no |
| host CPU busy, the real machine under kind (%) | 43.8 | 42.5 | −3.0% | −1.8433 to −0.7469 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800.1 | 769.4 | −3.8% | −42.7831 to −18.6169 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.095 | −15.1% | −1.8946 to +0.0856 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8833 | 0.075 | −91.5% | −0.9137 to −0.7030 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.5 | −70.6% | −1.6524 to −0.7476 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 113.1 | 78.5 | −30.6% | −47.1315 to −22.1685 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.596 | −6.7% | −0.8993 to +0.0910 | no |
| node-hours | 2.516 | 2.344 | −6.8% | −0.3745 to +0.0317 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.6 | −0.0% | −0.7650 to +0.5553 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 259.9 | −4.7% | −28.0129 to +2.3449 | no |
| response time (ms), mean | 334.4 | 363.3 | +8.6% | −1.9152 to +59.7430 | no |
| response time (ms), 95th percentile | 1087 | 1691 | +55.6% | +347.0019 to +861.3371 | yes: LOSS |
| response time (ms), 99th percentile | 1555 | 2787 | +79.3% | +757.2007 to +1707.8553 | yes: LOSS |
| time over the response line (% of samples) | 20.56 | 17.52 | −14.8% | −5.9672 to −0.1137 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.5 | +6.5% | +0.3545 to +1.0455 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 | +40.700 (native is 0) | +21.3969 to +60.0031 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.74 | 17.02 | +58.5% | +3.5694 to +8.9939 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06064 | 0.06522 | +7.6% | −0.0007 to +0.0098 | no |
| CPU used (cores), mean | 1.455 | 1.453 | −0.1% | −0.0284 to +0.0244 | no |
| Omni's own CPU (cores), mean | 0 | 0.01844 | +0.018 (native is 0) | +0.0167 to +0.0202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.455 | 1.472 | +1.1% | −0.0106 to +0.0434 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 429 | −5.0% | −52.0613 to +6.4584 | no |
| HPA replicas, mean | 2.089 | 2.268 | +8.6% | −0.0975 to +0.4551 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.7 | 0.8 | +14.3% | −1.1367 to +1.3367 | no |
| pod start wait, mean (s) | 0.5 | 0.65 | +30.0% | −0.8045 to +1.1045 | no |
| host CPU busy, the real machine under kind (%) | 41.27 | 44.8 | +8.6% | +2.9389 to +4.1296 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.3 | 806.4 | +5.6% | +26.9304 to +59.2696 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.217 | −13.0% | −1.6265 to +0.0608 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.8375 | +1156.2% | +0.6426 to +0.8990 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.6 | +166.7% | +0.5231 to +1.4769 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72.45 | 117.2 | +61.7% | +28.5179 to +60.8821 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*