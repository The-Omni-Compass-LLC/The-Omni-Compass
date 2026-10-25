# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.893 | 5.053 |
| node-hours | 2.517 | 2.514 | 2.052 | 2.123 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.7 | 271.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 270.7 | 236.3 | 241.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 254.1 | 276.9 | 222.2 | 261.9 |
| response time (ms), 95th percentile | 788.3 | 1070 | 820.2 | 1139 |
| response time (ms), 99th percentile | 1144 | 1665 | 1179 | 1804 |
| time over the response line (% of samples) | 11.44 | 8.96 | 11.55 | 9.574 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.7 | 6.8 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.8 | 47.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.888 | 15.3 | 8.705 | 14.75 |
| utilisation (used / allocatable) | 0.05546 | 0.05563 | 0.06844 | 0.06721 |
| CPU used (cores), mean | 1.331 | 1.335 | 1.327 | 1.331 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01583 | 0.01751 |
| CPU used with Omni's own (cores), mean | 1.331 | 1.335 | 1.342 | 1.348 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 492.2 | 425.3 | 434.1 |
| HPA replicas, mean | 2.019 | 1.994 | 2.322 | 2.189 |
| pods started | 0.3 | 0.2 | 0.3 | 0.6 |
| pod start wait, total (s) | 0.7 | 0.3 | 0.5 | 0.8 |
| pod start wait, mean (s) | 0.45 | 0.3 | 0.35 | 0.7 |
| host CPU busy, the real machine under kind (%) | 37.93 | 40.36 | 38.91 | 41.24 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 748.1 | 769.3 | 749.3 | 774.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.013 | 4.379 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7542 | 0.05417 | 0.7875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | 0.4 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 55.79 | 77.47 | 56.69 | 83 |
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
| worker nodes in service, mean | 6 | 5.053 | −15.8% | −1.7223 to −0.1718 | yes: GAIN |
| node-hours | 2.514 | 2.123 | −15.5% | −0.7150 to −0.0652 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.7 | +0.4% | +0.0198 to +1.9179 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 241.8 | −10.7% | −53.2686 to −4.5062 | yes: GAIN |
| response time (ms), mean | 276.9 | 261.9 | −5.4% | −42.1786 to +12.1401 | no |
| response time (ms), 95th percentile | 1070 | 1139 | +6.5% | −71.5954 to +209.9384 | no |
| response time (ms), 99th percentile | 1665 | 1804 | +8.4% | −87.2440 to +365.8204 | no |
| time over the response line (% of samples) | 8.96 | 9.574 | +6.8% | −0.5238 to +1.7512 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.2 | −7.5% | −1.1079 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.100 (native is 0) | +33.1583 to +61.0417 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.3 | 14.75 | −3.6% | −2.9895 to +1.8828 | no |
| utilisation (used / allocatable) | 0.05563 | 0.06721 | +20.8% | +0.0018 to +0.0213 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.335 | 1.331 | −0.3% | −0.0348 to +0.0262 | no |
| Omni's own CPU (cores), mean | 0 | 0.01751 | +0.018 (native is 0) | +0.0160 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.335 | 1.348 | +1.0% | −0.0175 to +0.0439 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.2 | 434.1 | −11.8% | −106.4060 to −9.6413 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.994 | 2.189 | +9.8% | +0.0382 to +0.3521 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0.3 | 0.7 | +133.3% | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 40.36 | 41.24 | +2.2% | +0.4417 to +1.3156 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 769.3 | 774.4 | +0.7% | −2.5704 to +12.7704 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.379 | −27.0% | −2.8869 to −0.3545 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.7875 | +4.4% | −0.0530 to +0.1197 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.5 | +15.4% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.47 | 83 | +7.1% | −1.7031 to +12.7614 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0125 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.7 | −0.1% | −1.4136 to +0.7872 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 270.7 | −0.1% | −1.4136 to +0.7872 | no |
| response time (ms), mean | 254.1 | 276.9 | +9.0% | −3.6323 to +49.3207 | no |
| response time (ms), 95th percentile | 788.3 | 1070 | +35.8% | +2.7406 to +560.9184 | yes: LOSS |
| response time (ms), 99th percentile | 1144 | 1665 | +45.5% | −2.2532 to +1042.6682 | no |
| time over the response line (% of samples) | 11.44 | 8.96 | −21.7% | −4.9843 to +0.0281 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.7 | +3.1% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.888 | 15.3 | +94.0% | +5.1795 to +9.6472 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05546 | 0.05563 | +0.3% | −0.0013 to +0.0016 | no |
| CPU used (cores), mean | 1.331 | 1.335 | +0.3% | −0.0305 to +0.0385 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.331 | 1.335 | +0.3% | −0.0305 to +0.0385 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 492.2 | −0.6% | −16.6009 to +10.2004 | no |
| HPA replicas, mean | 2.019 | 1.994 | −1.3% | −0.1317 to +0.0811 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.7 | 0.3 | −57.1% | −1.5778 to +0.7778 | no |
| pod start wait, mean (s) | 0.45 | 0.3 | −33.3% | −0.7820 to +0.4820 | no |
| host CPU busy, the real machine under kind (%) | 37.93 | 40.36 | +6.4% | +2.0884 to +2.7608 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.1 | 769.3 | +2.8% | +6.3832 to +36.0168 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7542 | +1545.5% | +0.6195 to +0.7972 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | +225.0% | +0.4940 to +1.3060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.79 | 77.47 | +38.8% | +4.6470 to +38.7030 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.893 | −18.4% | −1.8160 to −0.3976 | yes: GAIN |
| node-hours | 2.517 | 2.052 | −18.4% | −0.7617 to −0.1667 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.1 | +0.0% | −0.7511 to +0.9872 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 236.3 | −12.8% | −56.9601 to −12.5371 | yes: GAIN |
| response time (ms), mean | 254.1 | 222.2 | −12.5% | −44.4871 to −19.2249 | yes: GAIN |
| response time (ms), 95th percentile | 788.3 | 820.2 | +4.1% | −33.9887 to +97.8907 | no |
| response time (ms), 99th percentile | 1144 | 1179 | +3.1% | −76.5646 to +146.5172 | no |
| time over the response line (% of samples) | 11.44 | 11.55 | +1.0% | −0.5234 to +0.7548 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.8 | +4.6% | −1.0081 to +1.6081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +32.2281 to +51.3719 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.888 | 8.705 | +10.4% | −1.0470 to +2.6803 | no |
| utilisation (used / allocatable) | 0.05546 | 0.06844 | +23.4% | +0.0042 to +0.0218 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.331 | 1.327 | −0.3% | −0.0246 to +0.0158 | no |
| Omni's own CPU (cores), mean | 0 | 0.01583 | +0.016 (native is 0) | +0.0142 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.331 | 1.342 | +0.9% | −0.0089 to +0.0318 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 425.3 | −14.1% | −118.3355 to −21.8378 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.322 | +15.0% | +0.0519 to +0.5540 | yes: power given |
| pods started | 0.3 | 0.3 | ±0.0% | −0.7540 to +0.7540 | no |
| pod start wait, total (s) | 0.7 | 0.5 | −28.6% | −1.7379 to +1.3379 | no |
| pod start wait, mean (s) | 0.45 | 0.35 | −22.2% | −1.0656 to +0.8656 | no |
| host CPU busy, the real machine under kind (%) | 37.93 | 38.91 | +2.6% | +0.5483 to +1.4122 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.1 | 749.3 | +0.2% | −2.3494 to +4.7494 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.013 | −33.1% | −3.2186 to −0.7553 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05417 | +18.2% | −0.0309 to +0.0476 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.79 | 56.69 | +1.6% | −1.7107 to +3.5023 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.893 | −18.4% | −1.8160 to −0.3976 | yes: GAIN |
| node-hours | 2.514 | 2.052 | −18.3% | −0.7557 to −0.1664 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.1 | +0.2% | −0.5612 to +1.4238 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 236.3 | −12.7% | −56.5328 to −12.3379 | yes: GAIN |
| response time (ms), mean | 276.9 | 222.2 | −19.8% | −86.0982 to −23.3021 | yes: GAIN |
| response time (ms), 95th percentile | 1070 | 820.2 | −23.4% | −531.6148 to +31.8578 | no |
| response time (ms), 99th percentile | 1665 | 1179 | −29.1% | −1014.5174 to +44.0550 | no |
| time over the response line (% of samples) | 8.96 | 11.55 | +28.9% | +0.1574 to +5.0301 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.8 | +1.5% | −1.1818 to +1.3818 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +32.2281 to +51.3719 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.3 | 8.705 | −43.1% | −9.0789 to −4.1145 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05563 | 0.06844 | +23.0% | +0.0047 to +0.0210 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.335 | 1.327 | −0.6% | −0.0326 to +0.0158 | no |
| Omni's own CPU (cores), mean | 0 | 0.01583 | +0.016 (native is 0) | +0.0142 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.335 | 1.342 | +0.6% | −0.0175 to +0.0324 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.2 | 425.3 | −13.6% | −109.7793 to −23.9936 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.994 | 2.322 | +16.5% | +0.0393 to +0.6172 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.6793 to +1.0793 | no |
| pod start wait, mean (s) | 0.3 | 0.35 | +16.7% | −0.5909 to +0.6909 | no |
| host CPU busy, the real machine under kind (%) | 40.36 | 38.91 | −3.6% | −1.8626 to −1.0259 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 769.3 | 749.3 | −2.6% | −35.6534 to −4.3466 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.013 | −33.1% | −3.2186 to −0.7553 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7542 | 0.05417 | −92.8% | −0.7981 to −0.6019 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.4 | −69.2% | −1.4278 to −0.3722 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 77.47 | 56.69 | −26.8% | −38.2321 to −3.3262 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.053 | −15.8% | −1.7223 to −0.1718 | yes: GAIN |
| node-hours | 2.517 | 2.123 | −15.6% | −0.7210 to −0.0655 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.7 | +0.2% | +0.1145 to +1.1968 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 241.8 | −10.8% | −53.7767 to −4.6244 | yes: GAIN |
| response time (ms), mean | 254.1 | 261.9 | +3.1% | −31.6430 to +47.2929 | no |
| response time (ms), 95th percentile | 788.3 | 1139 | +44.5% | −7.3786 to +709.3806 | no |
| response time (ms), 99th percentile | 1144 | 1804 | +57.6% | +25.3200 to +1293.6714 | yes: LOSS |
| time over the response line (% of samples) | 11.44 | 9.574 | −16.3% | −3.4669 to −0.2618 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.2 | −4.6% | −1.3690 to +0.7690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.100 (native is 0) | +33.1583 to +61.0417 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.888 | 14.75 | +87.0% | +3.8480 to +9.8720 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05546 | 0.06721 | +21.2% | +0.0016 to +0.0219 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.331 | 1.331 | −0.0% | −0.0233 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.01751 | +0.018 (native is 0) | +0.0160 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.331 | 1.348 | +1.3% | −0.0054 to +0.0399 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 434.1 | −12.4% | −113.1070 to −9.3408 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.189 | +8.4% | −0.0012 to +0.3409 | no |
| pods started | 0.3 | 0.6 | +100.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.7 | 0.8 | +14.3% | −0.7564 to +0.9564 | no |
| pod start wait, mean (s) | 0.45 | 0.7 | +55.6% | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 37.93 | 41.24 | +8.7% | +2.9236 to +3.6829 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 748.1 | 774.4 | +3.5% | +7.2280 to +45.3720 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.379 | −27.0% | −2.8869 to −0.3545 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7875 | +1618.2% | +0.6260 to +0.8574 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | +275.0% | +0.6940 to +1.5060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.79 | 83 | +48.8% | +5.7119 to +48.6964 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*