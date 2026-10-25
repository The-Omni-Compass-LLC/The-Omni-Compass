# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.508 | 1.518 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.3 | 159.5 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.3 | 159.5 | 160.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 137.5 | 144.7 | 138.1 | 138.4 |
| response time (ms), 95th percentile | 279.9 | 289 | 286.4 | 276.3 |
| response time (ms), 99th percentile | 397.1 | 419.8 | 401.5 | 372.8 |
| time over the response line (% of samples) | 0.3594 | 0.7328 | 0.4371 | 0.1539 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.5 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2 | 2.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.2133 | 0.3983 | 0.4367 |
| utilisation (used / allocatable) | 0.03775 | 0.04233 | 0.03844 | 0.04322 |
| CPU used (cores), mean | 0.9059 | 1.016 | 0.9227 | 1.037 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0058 | 0.00982 |
| CPU used with Omni's own (cores), mean | 0.9059 | 1.016 | 0.9285 | 1.047 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.8 | 625 | 685 | 613.7 |
| HPA replicas, mean | 8.869 | 8.871 | 10.23 | 10.11 |
| pods started | 4.9 | 4.7 | 7.7 | 7.6 |
| pod start wait, total (s) | 6.4 | 6.8 | 12 | 11.4 |
| pod start wait, mean (s) | 1.292 | 1.462 | 1.521 | 1.531 |
| host CPU busy, the real machine under kind (%) | 26.44 | 30.45 | 27.44 | 31.78 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 3 of 10 repetitions (repetitions 1, 7, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.518 | +0.6% | +0.0023 to +0.0167 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 160.5 | +0.8% | +0.3784 to +2.0707 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 160.5 | +0.8% | +0.3784 to +2.0707 | yes: power given |
| response time (ms), mean | 144.7 | 138.4 | −4.4% | −16.0449 to +3.4451 | no |
| response time (ms), 95th percentile | 289 | 276.3 | −4.4% | −45.0575 to +19.7025 | no |
| response time (ms), 99th percentile | 419.8 | 372.8 | −11.2% | −112.6437 to +18.5933 | no |
| time over the response line (% of samples) | 0.7328 | 0.1539 | −79.0% | −1.2649 to +0.1070 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0.1 | −80.0% | −1.3048 to +0.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.2 | +2.200 (native is 0) | +0.6996 to +3.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.4367 | +104.7% | −0.0224 to +0.4690 | no |
| utilisation (used / allocatable) | 0.04233 | 0.04322 | +2.1% | +0.0001 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.016 | 1.037 | +2.1% | +0.0023 to +0.0403 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00982 | +0.010 (native is 0) | +0.0081 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 1.047 | +3.1% | +0.0110 to +0.0512 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 625 | 613.7 | −1.8% | −21.0823 to −1.5142 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.871 | 10.11 | +14.0% | +0.4680 to +2.0143 | yes: power given |
| pods started | 4.7 | 7.6 | +61.7% | +1.3383 to +4.4617 | yes: power given |
| pod start wait, total (s) | 6.8 | 11.4 | +67.6% | +2.2834 to +6.9166 | yes: LOSS |
| pod start wait, mean (s) | 1.462 | 1.531 | +4.7% | −0.2317 to +0.3705 | no |
| host CPU busy, the real machine under kind (%) | 30.45 | 31.78 | +4.4% | +0.4681 to +2.1858 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.508 | −0.6% | −0.0155 to −0.0029 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.3 | +0.0% | −0.6092 to +0.7407 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.3 | +0.0% | −0.6092 to +0.7407 | no |
| response time (ms), mean | 137.5 | 144.7 | +5.3% | −1.5940 to +16.1256 | no |
| response time (ms), 95th percentile | 279.9 | 289 | +3.3% | −19.9270 to +38.1870 | no |
| response time (ms), 99th percentile | 397.1 | 419.8 | +5.7% | −55.4952 to +100.9138 | no |
| time over the response line (% of samples) | 0.3594 | 0.7328 | +103.9% | −0.4899 to +1.2367 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.5 | +400.0% | −0.7778 to +1.5778 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.2133 | +700.0% | +0.0057 to +0.3676 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03775 | 0.04233 | +12.1% | +0.0043 to +0.0049 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9059 | 1.016 | +12.1% | +0.1021 to +0.1178 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9059 | 1.016 | +12.1% | +0.1021 to +0.1178 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.8 | 625 | −10.3% | −80.2248 to −63.4478 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.869 | 8.871 | +0.0% | −0.1221 to +0.1263 | no |
| pods started | 4.9 | 4.7 | −4.1% | −0.9388 to +0.5388 | no |
| pod start wait, total (s) | 6.4 | 6.8 | +6.3% | −1.1888 to +1.9888 | no |
| pod start wait, mean (s) | 1.292 | 1.462 | +13.2% | −0.1276 to +0.4676 | no |
| host CPU busy, the real machine under kind (%) | 26.44 | 30.45 | +15.2% | +3.6131 to +4.4156 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.518 | +0.1% | −0.0033 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.5 | +0.2% | −0.2092 to +0.7137 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.5 | +0.2% | −0.2092 to +0.7137 | no |
| response time (ms), mean | 137.5 | 138.1 | +0.5% | −2.3099 to +3.6522 | no |
| response time (ms), 95th percentile | 279.9 | 286.4 | +2.3% | −4.3187 to +17.3337 | no |
| response time (ms), 99th percentile | 397.1 | 401.5 | +1.1% | −30.8598 to +39.5812 | no |
| time over the response line (% of samples) | 0.3594 | 0.4371 | +21.6% | −0.2348 to +0.3901 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.3983 | +1393.8% | +0.0828 to +0.6605 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03775 | 0.03844 | +1.8% | +0.0002 to +0.0012 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9059 | 0.9227 | +1.8% | +0.0037 to +0.0297 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0058 | +0.006 (native is 0) | +0.0050 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9059 | 0.9285 | +2.5% | +0.0094 to +0.0357 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.8 | 685 | −1.7% | −21.0084 to −2.6249 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.869 | 10.23 | +15.3% | +0.6712 to +2.0407 | yes: power given |
| pods started | 4.9 | 7.7 | +57.1% | +0.8396 to +4.7604 | yes: power given |
| pod start wait, total (s) | 6.4 | 12 | +87.5% | +1.4950 to +9.7050 | yes: LOSS |
| pod start wait, mean (s) | 1.292 | 1.521 | +17.8% | −0.0544 to +0.5139 | no |
| host CPU busy, the real machine under kind (%) | 26.44 | 27.44 | +3.8% | +0.5027 to +1.5120 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.518 | +0.7% | +0.0033 to +0.0167 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.5 | +0.1% | −0.5168 to +0.8899 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.5 | +0.1% | −0.5168 to +0.8899 | no |
| response time (ms), mean | 144.7 | 138.1 | −4.6% | −15.9229 to +2.7335 | no |
| response time (ms), 95th percentile | 289 | 286.4 | −0.9% | −34.8748 to +29.6298 | no |
| response time (ms), 99th percentile | 419.8 | 401.5 | −4.4% | −86.4198 to +49.7226 | no |
| time over the response line (% of samples) | 0.7328 | 0.4371 | −40.4% | −1.0670 to +0.4756 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0.1 | −80.0% | −1.3048 to +0.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.3983 | +86.7% | −0.0966 to +0.4666 | no |
| utilisation (used / allocatable) | 0.04233 | 0.03844 | −9.2% | −0.0044 to −0.0034 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9227 | −9.2% | −0.1048 to −0.0817 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0058 | +0.006 (native is 0) | +0.0050 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9285 | −8.6% | −0.0993 to −0.0756 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 625 | 685 | +9.6% | +50.4426 to +69.5967 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.871 | 10.23 | +15.3% | +0.6420 to +2.0658 | yes: power given |
| pods started | 4.7 | 7.7 | +63.8% | +1.3481 to +4.6519 | yes: power given |
| pod start wait, total (s) | 6.8 | 12 | +76.5% | +1.1006 to +9.2994 | yes: LOSS |
| pod start wait, mean (s) | 1.462 | 1.521 | +4.1% | −0.3255 to +0.4449 | no |
| host CPU busy, the real machine under kind (%) | 30.45 | 27.44 | −9.9% | −3.4193 to −2.5947 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.518 | +0.0% | −0.0038 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.5 | +0.8% | +0.7788 to +1.8017 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.5 | +0.8% | +0.7788 to +1.8017 | yes: power given |
| response time (ms), mean | 137.5 | 138.4 | +0.7% | −2.7772 to +4.7091 | no |
| response time (ms), 95th percentile | 279.9 | 276.3 | −1.3% | −18.0754 to +10.9804 | no |
| response time (ms), 99th percentile | 397.1 | 372.8 | −6.1% | −53.2130 to +4.5812 | no |
| time over the response line (% of samples) | 0.3594 | 0.1539 | −57.2% | −0.5180 to +0.1070 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.2 | +2.200 (native is 0) | +0.6996 to +3.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.4367 | +1537.5% | +0.1582 to +0.6618 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03775 | 0.04322 | +14.5% | +0.0048 to +0.0062 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9059 | 1.037 | +14.5% | +0.1147 to +0.1479 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00982 | +0.010 (native is 0) | +0.0081 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9059 | 1.047 | +15.6% | +0.1234 to +0.1588 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.8 | 613.7 | −11.9% | −92.1564 to −74.1127 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.869 | 10.11 | +14.0% | +0.5210 to +1.9655 | yes: power given |
| pods started | 4.9 | 7.6 | +55.1% | +1.0463 to +4.3537 | yes: power given |
| pod start wait, total (s) | 6.4 | 11.4 | +78.1% | +2.1190 to +7.8810 | yes: LOSS |
| pod start wait, mean (s) | 1.292 | 1.531 | +18.5% | −0.1060 to +0.5848 | no |
| host CPU busy, the real machine under kind (%) | 26.44 | 31.78 | +20.2% | +4.3580 to +6.3245 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*