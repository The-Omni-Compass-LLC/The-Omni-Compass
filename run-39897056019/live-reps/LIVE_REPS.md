# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.511 | 1.52 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.6 | 159.7 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.6 | 159.7 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 140.3 | 146.8 | 141.3 | 146.7 |
| response time (ms), 95th percentile | 282.3 | 300.7 | 285 | 287.8 |
| response time (ms), 99th percentile | 412.2 | 415.7 | 432.3 | 400 |
| time over the response line (% of samples) | 0.4485 | 0.595 | 0.5807 | 0.4257 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | 0.4 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 7.9 | 7.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 80 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | 0.1583 | 0.47 |
| utilisation (used / allocatable) | 0.03794 | 0.04254 | 0.03875 | 0.04393 |
| CPU used (cores), mean | 0.9106 | 1.021 | 0.9299 | 1.054 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01994 | 0.0328 |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.021 | 0.9498 | 1.087 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.2 | 622.8 | 680.5 | 605.4 |
| HPA replicas, mean | 8.836 | 8.902 | 10.94 | 10.88 |
| pods started | 5 | 4.8 | 7.7 | 8.7 |
| pod start wait, total (s) | 7.2 | 7.4 | 12.6 | 14.1 |
| pod start wait, mean (s) | 1.437 | 1.527 | 1.666 | 1.589 |
| host CPU busy, the real machine under kind (%) | 26.57 | 30.7 | 27.95 | 32.87 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 1.511 | 1.52 | +0.6% | +0.0009443 to +0.01672 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 160.8 | +0.8% | +0.3042 to +2.145 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 160.8 | +0.8% | +0.3042 to +2.145 | yes: power given |
| response time (ms), mean | 146.8 | 146.7 | -0.0% | -2.962 to +2.817 | no |
| response time (ms), 95th percentile | 300.7 | 287.8 | -4.3% | -29.9 to +4.07 | no |
| response time (ms), 99th percentile | 415.7 | 400 | -3.8% | -45.67 to +14.41 | no |
| time over the response line (% of samples) | 0.595 | 0.4257 | -28.4% | -0.5085 to +0.1699 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.4 | +7.4 (native is 0) | +5.811 to +8.989 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.47 | +340.6% | +0.02195 to +0.7047 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04254 | 0.04393 | +3.3% | +0.0006196 to +0.002172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.021 | 1.054 | +3.3% | +0.01487 to +0.05212 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0328 | +0.0328 (native is 0) | +0.02835 to +0.03725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.021 | 1.087 | +6.5% | +0.04434 to +0.08825 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 622.8 | 605.4 | -2.8% | -27.31 to -7.622 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.902 | 10.88 | +22.2% | +1.071 to +2.889 | yes: power given |
| pods started | 4.8 | 8.7 | +81.2% | +2.663 to +5.137 | yes: power given |
| pod start wait, total (s) | 7.4 | 14.1 | +90.5% | +1.991 to +11.41 | yes: LOSS |
| pod start wait, mean (s) | 1.527 | 1.589 | +4.1% | -0.4246 to +0.5489 | no |
| host CPU busy, the real machine under kind (%) | 30.7 | 32.87 | +7.1% | +1.477 to +2.873 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.431e-16 to +1.356e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.511 | -0.4% | -0.01003 to -0.001306 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.6 | +0.3% | +0.06687 to +0.7803 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.6 | +0.3% | +0.06687 to +0.7803 | yes: power given |
| response time (ms), mean | 140.3 | 146.8 | +4.6% | +2.986 to +9.96 | yes: LOSS |
| response time (ms), 95th percentile | 282.3 | 300.7 | +6.5% | +2.764 to +33.95 | yes: LOSS |
| response time (ms), 99th percentile | 412.2 | 415.7 | +0.9% | -20.84 to +27.86 | no |
| time over the response line (% of samples) | 0.4485 | 0.595 | +32.7% | -0.161 to +0.454 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | -0.08161 to +0.1349 | no |
| utilisation (used / allocatable) | 0.03794 | 0.04254 | +12.1% | +0.003951 to +0.005243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 1.021 | +12.1% | +0.09482 to +0.1258 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.021 | +12.1% | +0.09482 to +0.1258 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.2 | 622.8 | -10.2% | -77.74 to -63.09 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.836 | 8.902 | +0.8% | -0.06952 to +0.2026 | no |
| pods started | 5 | 4.8 | -4.0% | -0.7642 to +0.3642 | no |
| pod start wait, total (s) | 7.2 | 7.4 | +2.8% | -1.578 to +1.978 | no |
| pod start wait, mean (s) | 1.437 | 1.527 | +6.3% | -0.1849 to +0.3649 | no |
| host CPU busy, the real machine under kind (%) | 26.57 | 30.7 | +15.5% | +3.56 to +4.699 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.52 | +0.2% | +0.0005038 to +0.005829 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.7 | +0.3% | +0.08397 to +0.892 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.7 | +0.3% | +0.08397 to +0.892 | yes: power given |
| response time (ms), mean | 140.3 | 141.3 | +0.7% | -5.514 to +7.538 | no |
| response time (ms), 95th percentile | 282.3 | 285 | +0.9% | -15.41 to +20.67 | no |
| response time (ms), 99th percentile | 412.2 | 432.3 | +4.9% | -66.22 to +106.6 | no |
| time over the response line (% of samples) | 0.4485 | 0.5807 | +29.5% | -0.4081 to +0.6724 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.4 | +100.0% | -0.8003 to +1.2 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.9 | +7.9 (native is 0) | +5.602 to +10.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1583 | +97.9% | -0.1761 to +0.3328 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03875 | +2.1% | +6.82e-05 to +0.001544 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 0.9299 | +2.1% | +0.001637 to +0.03706 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01994 | +0.0199 (native is 0) | +0.01757 to +0.02231 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9106 | 0.9498 | +4.3% | +0.02005 to +0.05853 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.2 | 680.5 | -1.8% | -24.74 to -0.6376 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.836 | 10.94 | +23.8% | +1.234 to +2.977 | yes: power given |
| pods started | 5 | 7.7 | +54.0% | +0.9141 to +4.486 | yes: power given |
| pod start wait, total (s) | 7.2 | 12.6 | +75.0% | +1.582 to +9.218 | yes: LOSS |
| pod start wait, mean (s) | 1.437 | 1.666 | +16.0% | -0.07721 to +0.5367 | no |
| host CPU busy, the real machine under kind (%) | 26.57 | 27.95 | +5.2% | +0.7692 to +1.996 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.112e-15 to -3.087e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.52 | +0.6% | +0.002278 to +0.01539 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.7 | +0.0% | -0.6275 to +0.7564 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.7 | +0.0% | -0.6275 to +0.7564 | no |
| response time (ms), mean | 146.8 | 141.3 | -3.7% | -12.67 to +1.75 | no |
| response time (ms), 95th percentile | 300.7 | 285 | -5.2% | -34.39 to +2.934 | no |
| response time (ms), 99th percentile | 415.7 | 432.3 | +4.0% | -79.91 to +113.2 | no |
| time over the response line (% of samples) | 0.595 | 0.5807 | -2.4% | -0.741 to +0.7124 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.4 | +100.0% | -0.8556 to +1.256 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.9 | +7.9 (native is 0) | +5.602 to +10.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1583 | +48.4% | -0.164 to +0.2673 | no |
| utilisation (used / allocatable) | 0.04254 | 0.03875 | -8.9% | -0.004382 to -0.0032 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.021 | 0.9299 | -8.9% | -0.1052 to -0.07679 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01994 | +0.0199 (native is 0) | +0.01757 to +0.02231 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.021 | 0.9498 | -7.0% | -0.08549 to -0.05658 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 622.8 | 680.5 | +9.3% | +47.37 to +68.08 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.902 | 10.94 | +22.9% | +1.127 to +2.951 | yes: power given |
| pods started | 4.8 | 7.7 | +60.4% | +1.166 to +4.634 | yes: power given |
| pod start wait, total (s) | 7.4 | 12.6 | +70.3% | +1.227 to +9.173 | yes: LOSS |
| pod start wait, mean (s) | 1.527 | 1.666 | +9.2% | -0.1712 to +0.4506 | no |
| host CPU busy, the real machine under kind (%) | 30.7 | 27.95 | -8.9% | -3.18 to -2.315 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.002e-16 to +1.499e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.52 | +0.2% | -0.003727 to +0.01006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.8 | +1.0% | +0.9211 to +2.375 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.8 | +1.0% | +0.9211 to +2.375 | yes: power given |
| response time (ms), mean | 140.3 | 146.7 | +4.6% | +3.115 to +9.686 | yes: LOSS |
| response time (ms), 95th percentile | 282.3 | 287.8 | +1.9% | -4.143 to +15.03 | no |
| response time (ms), 99th percentile | 412.2 | 400 | -2.9% | -41.83 to +17.58 | no |
| time over the response line (% of samples) | 0.4485 | 0.4257 | -5.1% | -0.2824 to +0.2369 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | -50.0% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.4 | +7.4 (native is 0) | +5.811 to +8.989 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.47 | +487.5% | +0.04611 to +0.7339 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03794 | 0.04393 | +15.8% | +0.00491 to +0.007076 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9106 | 1.054 | +15.8% | +0.1178 to +0.1698 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0328 | +0.0328 (native is 0) | +0.02835 to +0.03725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9106 | 1.087 | +19.4% | +0.1465 to +0.2067 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.2 | 605.4 | -12.7% | -98.78 to -76.98 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.836 | 10.88 | +23.2% | +1.138 to +2.955 | yes: power given |
| pods started | 5 | 8.7 | +74.0% | +2.267 to +5.133 | yes: power given |
| pod start wait, total (s) | 7.2 | 14.1 | +95.8% | +2.296 to +11.5 | yes: LOSS |
| pod start wait, mean (s) | 1.437 | 1.589 | +10.6% | -0.3154 to +0.6197 | no |
| host CPU busy, the real machine under kind (%) | 26.57 | 32.87 | +23.7% | +5.16 to +7.449 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*