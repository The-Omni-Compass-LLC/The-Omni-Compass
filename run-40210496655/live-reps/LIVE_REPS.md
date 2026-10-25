# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.517 | 1.515 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.7 | 161.1 | 160.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.7 | 161.1 | 160.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 125.3 | 124.6 | 80.23 | 80.35 |
| response time (ms), 95th percentile | 252.4 | 255 | 130.5 | 130.7 |
| response time (ms), 99th percentile | 360.1 | 360.1 | 168.8 | 160.1 |
| time over the response line (% of samples) | 0.2687 | 0.2935 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 28.9 | 24.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0 | 0.1333 | 0.1867 |
| utilisation (used / allocatable) | 0.03597 | 0.03585 | 0.04681 | 0.04638 |
| CPU used (cores), mean | 0.8633 | 0.8603 | 1.124 | 1.113 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00827 | 0.00822 |
| CPU used with Omni's own (cores), mean | 0.8633 | 0.8603 | 1.132 | 1.121 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.4 | 732 | 576.3 | 581.9 |
| HPA replicas, mean | 8.881 | 9.542 | 9.729 | 10.04 |
| pods started | 4.7 | 3.9 | 7 | 3.5 |
| pod start wait, total (s) | 7.4 | 6 | 10.9 | 6.2 |
| pod start wait, mean (s) | 1.565 | 1.547 | 1.539 | 1.767 |
| host CPU busy, the real machine under kind (%) | 25.57 | 25.67 | 32.77 | 33.12 |
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

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.51 | −0.5% | −0.0146 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 160.4 | +1.0% | +1.2654 to +2.0452 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 160.4 | +1.0% | +1.2654 to +2.0452 | yes: power given |
| response time (ms), mean | 124.6 | 80.35 | −35.5% | −57.6857 to −30.8679 | yes: GAIN |
| response time (ms), 95th percentile | 255 | 130.7 | −48.8% | −152.6442 to −95.9948 | yes: GAIN |
| response time (ms), 99th percentile | 360.1 | 160.1 | −55.5% | −241.1645 to −158.8577 | yes: GAIN |
| time over the response line (% of samples) | 0.2935 | 0 | −100.0% | −0.5004 to −0.0866 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.9 | +24.900 (native is 0) | +20.1858 to +29.6142 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1867 | +0.187 (native is 0) | −0.0984 to +0.4717 | no |
| utilisation (used / allocatable) | 0.03585 | 0.04638 | +29.4% | +0.0076 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8603 | 1.113 | +29.4% | +0.1822 to +0.3233 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00822 | +0.008 (native is 0) | +0.0069 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8603 | 1.121 | +30.3% | +0.1893 to +0.3327 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732 | 581.9 | −20.5% | −179.3303 to −120.8638 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.542 | 10.04 | +5.2% | −0.3574 to +1.3525 | no |
| pods started | 3.9 | 3.5 | −10.3% | −1.8775 to +1.0775 | no |
| pod start wait, total (s) | 6 | 6.2 | +3.3% | −2.9234 to +3.3234 | no |
| pod start wait, mean (s) | 1.547 | 1.767 | +14.2% | −0.2709 to +0.7109 | no |
| host CPU busy, the real machine under kind (%) | 25.67 | 33.12 | +29.0% | +5.4820 to +9.4207 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.517 | −0.0% | −0.0052 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.7 | −0.0% | −0.6446 to +0.5127 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.7 | −0.0% | −0.6446 to +0.5127 | no |
| response time (ms), mean | 125.3 | 124.6 | −0.5% | −3.5165 to +2.1706 | no |
| response time (ms), 95th percentile | 252.4 | 255 | +1.0% | −11.8470 to +17.1390 | no |
| response time (ms), 99th percentile | 360.1 | 360.1 | +0.0% | −30.1421 to +30.1669 | no |
| time over the response line (% of samples) | 0.2687 | 0.2935 | +9.2% | −0.1860 to +0.2356 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0 | −100.0% | −0.2657 to +0.0023 | no |
| utilisation (used / allocatable) | 0.03597 | 0.03585 | −0.3% | −0.0007 to +0.0005 | no |
| CPU used (cores), mean | 0.8633 | 0.8603 | −0.3% | −0.0180 to +0.0120 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8633 | 0.8603 | −0.3% | −0.0180 to +0.0120 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.4 | 732 | +0.4% | −9.6000 to +14.7419 | no |
| HPA replicas, mean | 8.881 | 9.542 | +7.5% | +0.5232 to +0.8006 | yes: power given |
| pods started | 4.7 | 3.9 | −17.0% | −1.4573 to −0.1427 | yes: GAIN |
| pod start wait, total (s) | 7.4 | 6 | −18.9% | −3.4288 to +0.6288 | no |
| pod start wait, mean (s) | 1.565 | 1.547 | −1.2% | −0.4161 to +0.3795 | no |
| host CPU busy, the real machine under kind (%) | 25.57 | 25.67 | +0.4% | −0.2743 to +0.4692 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.515 | −0.1% | −0.0093 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.1 | +1.4% | +1.3680 to +3.2227 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 161.1 | +1.4% | +1.3680 to +3.2227 | yes: power given |
| response time (ms), mean | 125.3 | 80.23 | −36.0% | −58.2222 to −31.9097 | yes: GAIN |
| response time (ms), 95th percentile | 252.4 | 130.5 | −48.3% | −140.3726 to −103.3894 | yes: GAIN |
| response time (ms), 99th percentile | 360.1 | 168.8 | −53.1% | −224.0461 to −158.5695 | yes: GAIN |
| time over the response line (% of samples) | 0.2687 | 0 | −100.0% | −0.5067 to −0.0307 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.9 | +28.900 (native is 0) | +22.7149 to +35.0851 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1333 | +1.3% | −0.1573 to +0.1607 | no |
| utilisation (used / allocatable) | 0.03597 | 0.04681 | +30.1% | +0.0079 to +0.0138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8633 | 1.124 | +30.1% | +0.1887 to +0.3317 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00827 | +0.008 (native is 0) | +0.0067 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8633 | 1.132 | +31.1% | +0.1957 to +0.3413 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.4 | 576.3 | −21.0% | −184.1520 to −122.0590 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.881 | 9.729 | +9.6% | −0.1128 to +1.8103 | no |
| pods started | 4.7 | 7 | +48.9% | +0.7901 to +3.8099 | yes: power given |
| pod start wait, total (s) | 7.4 | 10.9 | +47.3% | +0.5555 to +6.4445 | yes: LOSS |
| pod start wait, mean (s) | 1.565 | 1.539 | −1.7% | −0.3630 to +0.3102 | no |
| host CPU busy, the real machine under kind (%) | 25.57 | 32.77 | +28.2% | +5.2985 to +9.1092 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.515 | −0.1% | −0.0080 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 161.1 | +1.5% | +1.5418 to +3.1808 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 161.1 | +1.5% | +1.5418 to +3.1808 | yes: power given |
| response time (ms), mean | 124.6 | 80.23 | −35.6% | −57.2461 to −31.5399 | yes: GAIN |
| response time (ms), 95th percentile | 255 | 130.5 | −48.8% | −151.3373 to −97.7167 | yes: GAIN |
| response time (ms), 99th percentile | 360.1 | 168.8 | −53.1% | −234.0251 to −148.6153 | yes: GAIN |
| time over the response line (% of samples) | 0.2935 | 0 | −100.0% | −0.5004 to −0.0866 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.9 | +28.900 (native is 0) | +22.7149 to +35.0851 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1333 | +0.133 (native is 0) | −0.0520 to +0.3187 | no |
| utilisation (used / allocatable) | 0.03585 | 0.04681 | +30.6% | +0.0082 to +0.0138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8603 | 1.124 | +30.6% | +0.1956 to +0.3308 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00827 | +0.008 (native is 0) | +0.0067 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8603 | 1.132 | +31.6% | +0.2026 to +0.3404 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732 | 576.3 | −21.3% | −183.4085 to −127.9444 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.542 | 9.729 | +2.0% | −0.7793 to +1.1531 | no |
| pods started | 3.9 | 7 | +79.5% | +1.2393 to +4.9607 | yes: power given |
| pod start wait, total (s) | 6 | 10.9 | +81.7% | +1.1534 to +8.6466 | yes: LOSS |
| pod start wait, mean (s) | 1.547 | 1.539 | −0.5% | −0.3698 to +0.3537 | no |
| host CPU busy, the real machine under kind (%) | 25.67 | 32.77 | +27.7% | +5.1342 to +9.0787 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.51 | −0.5% | −0.0150 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160.4 | +1.0% | +1.2613 to +1.9175 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160.4 | +1.0% | +1.2613 to +1.9175 | yes: power given |
| response time (ms), mean | 125.3 | 80.35 | −35.9% | −58.7409 to −31.1585 | yes: GAIN |
| response time (ms), 95th percentile | 252.4 | 130.7 | −48.2% | −142.1065 to −101.2405 | yes: GAIN |
| response time (ms), 99th percentile | 360.1 | 160.1 | −55.5% | −235.2269 to −164.7705 | yes: GAIN |
| time over the response line (% of samples) | 0.2687 | 0 | −100.0% | −0.5067 to −0.0307 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.9 | +24.900 (native is 0) | +20.1858 to +29.6142 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1867 | +41.8% | −0.1602 to +0.2702 | no |
| utilisation (used / allocatable) | 0.03597 | 0.04638 | +28.9% | +0.0073 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8633 | 1.113 | +28.9% | +0.1750 to +0.3245 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00822 | +0.008 (native is 0) | +0.0069 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8633 | 1.121 | +29.9% | +0.1820 to +0.3339 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.4 | 581.9 | −20.2% | −180.0381 to −115.0142 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.881 | 10.04 | +13.1% | +0.3302 to +1.9886 | yes: power given |
| pods started | 4.7 | 3.5 | −25.5% | −2.6226 to +0.2226 | no |
| pod start wait, total (s) | 7.4 | 6.2 | −16.2% | −4.2868 to +1.8868 | no |
| pod start wait, mean (s) | 1.565 | 1.767 | +12.9% | −0.1101 to +0.5134 | no |
| host CPU busy, the real machine under kind (%) | 25.57 | 33.12 | +29.5% | +5.6686 to +9.4290 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*