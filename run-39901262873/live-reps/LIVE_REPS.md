# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.511 | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.2 | 158.6 | 159.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.2 | 158.6 | 159.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 109.2 | 111.4 | 107.5 | 110.4 |
| response time (ms), 95th percentile | 234 | 231.8 | 226.8 | 225.6 |
| response time (ms), 99th percentile | 328.3 | 323.6 | 324.9 | 315.2 |
| time over the response line (% of samples) | 0.18 | 0.2591 | 0.1281 | 0.129 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.5 | 5.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 | 0.1867 | 0.1867 |
| utilisation (used / allocatable) | 0.03648 | 0.04055 | 0.03698 | 0.04089 |
| CPU used (cores), mean | 0.8754 | 0.9732 | 0.8874 | 0.9814 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01717 | 0.02738 |
| CPU used with Omni's own (cores), mean | 0.8754 | 0.9732 | 0.9046 | 1.009 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 651.5 | 711 | 647.7 |
| HPA replicas, mean | 8.86 | 8.857 | 9.609 | 9.602 |
| pods started | 5 | 4.9 | 6.2 | 5.9 |
| pod start wait, total (s) | 6.8 | 7.5 | 8.5 | 8.8 |
| pod start wait, mean (s) | 1.338 | 1.527 | 1.281 | 1.476 |
| host CPU busy, the real machine under kind (%) | 25.8 | 29.39 | 26.82 | 30.52 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 1.511 | 1.515 | +0.3% | -0.002032 to +0.01003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.7 | +0.3% | -0.1655 to +1.117 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.7 | +0.3% | -0.1655 to +1.117 | no |
| response time (ms), mean | 111.4 | 110.4 | -0.8% | -3.201 to +1.379 | no |
| response time (ms), 95th percentile | 231.8 | 225.6 | -2.7% | -18.97 to +6.393 | no |
| response time (ms), 99th percentile | 323.6 | 315.2 | -2.6% | -31.29 to +14.48 | no |
| time over the response line (% of samples) | 0.2591 | 0.129 | -50.2% | -0.4004 to +0.1404 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.5 (native is 0) | +3.839 to +7.161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1867 | +600.0% | -0.04505 to +0.365 | no |
| utilisation (used / allocatable) | 0.04055 | 0.04089 | +0.8% | -0.0005354 to +0.00122 | no |
| CPU used (cores), mean | 0.9732 | 0.9814 | +0.8% | -0.01285 to +0.02929 | no |
| Omni's own CPU (cores), mean | 0 | 0.02738 | +0.0274 (native is 0) | +0.02301 to +0.03175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9732 | 1.009 | +3.7% | +0.01085 to +0.06035 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 651.5 | 647.7 | -0.6% | -16.88 to +9.367 | no |
| HPA replicas, mean | 8.857 | 9.602 | +8.4% | -0.05819 to +1.547 | no |
| pods started | 4.9 | 5.9 | +20.4% | -0.6519 to +2.652 | no |
| pod start wait, total (s) | 7.5 | 8.8 | +17.3% | -1.641 to +4.241 | no |
| pod start wait, mean (s) | 1.527 | 1.476 | -3.3% | -0.3128 to +0.2117 | no |
| host CPU busy, the real machine under kind (%) | 29.39 | 30.52 | +3.8% | +0.3675 to +1.892 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.338e-16 to +4.785e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | -0.1% | -0.009377 to +0.006377 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.2 | +0.5% | -0.01817 to +1.514 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.2 | +0.5% | -0.01817 to +1.514 | no |
| response time (ms), mean | 109.2 | 111.4 | +2.0% | -1.741 to +6.133 | no |
| response time (ms), 95th percentile | 234 | 231.8 | -0.9% | -13.3 to +8.971 | no |
| response time (ms), 99th percentile | 328.3 | 323.6 | -1.4% | -33.31 to +23.79 | no |
| time over the response line (% of samples) | 0.18 | 0.2591 | +43.9% | -0.1818 to +0.34 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 | -50.0% | -0.1349 to +0.08161 | no |
| utilisation (used / allocatable) | 0.03648 | 0.04055 | +11.2% | +0.003447 to +0.004696 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8754 | 0.9732 | +11.2% | +0.08272 to +0.1127 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.8754 | 0.9732 | +11.2% | +0.08272 to +0.1127 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 651.5 | -9.6% | -81.61 to -56.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.86 | 8.857 | -0.0% | -0.1047 to +0.09984 | no |
| pods started | 5 | 4.9 | -2.0% | -0.7263 to +0.5263 | no |
| pod start wait, total (s) | 6.8 | 7.5 | +10.3% | -1.46 to +2.86 | no |
| pod start wait, mean (s) | 1.338 | 1.527 | +14.1% | -0.1987 to +0.5754 | no |
| host CPU busy, the real machine under kind (%) | 25.8 | 29.39 | +13.9% | +3.033 to +4.147 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.279e-15 to +2.128e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.513 | +0.0% | -0.005535 to +0.005535 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.6 | +0.1% | -0.5533 to +0.7426 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.6 | +0.1% | -0.5533 to +0.7426 | no |
| response time (ms), mean | 109.2 | 107.5 | -1.5% | -4.875 to +1.523 | no |
| response time (ms), 95th percentile | 234 | 226.8 | -3.1% | -16.97 to +2.472 | no |
| response time (ms), 99th percentile | 328.3 | 324.9 | -1.0% | -21.97 to +15.19 | no |
| time over the response line (% of samples) | 0.18 | 0.1281 | -28.8% | -0.1502 to +0.04651 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.5 (native is 0) | +3.839 to +7.161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.1867 | +250.0% | -0.1814 to +0.4481 | no |
| utilisation (used / allocatable) | 0.03648 | 0.03698 | +1.4% | +4.226e-05 to +0.0009566 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8754 | 0.8874 | +1.4% | +0.001014 to +0.02296 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01717 | +0.0172 (native is 0) | +0.01463 to +0.01971 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8754 | 0.9046 | +3.3% | +0.01832 to +0.03999 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 711 | -1.3% | -18.39 to -0.623 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.86 | 9.609 | +8.5% | +0.009852 to +1.488 | yes: power given |
| pods started | 5 | 6.2 | +24.0% | -0.5128 to +2.913 | no |
| pod start wait, total (s) | 6.8 | 8.5 | +25.0% | -1.837 to +5.237 | no |
| pod start wait, mean (s) | 1.338 | 1.281 | -4.3% | -0.3937 to +0.278 | no |
| host CPU busy, the real machine under kind (%) | 25.8 | 26.82 | +4.0% | +0.6678 to +1.375 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.69e-16 to +2.585e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.513 | +0.1% | -0.007323 to +0.01032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | -0.4% | -1.537 to +0.2304 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | -0.4% | -1.537 to +0.2304 | no |
| response time (ms), mean | 111.4 | 107.5 | -3.5% | -8.028 to +0.2834 | no |
| response time (ms), 95th percentile | 231.8 | 226.8 | -2.2% | -20.38 to +10.21 | no |
| response time (ms), 99th percentile | 323.6 | 324.9 | +0.4% | -24.05 to +26.78 | no |
| time over the response line (% of samples) | 0.2591 | 0.1281 | -50.5% | -0.4647 to +0.2028 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.5 (native is 0) | +3.839 to +7.161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1867 | +600.0% | -0.08128 to +0.4013 | no |
| utilisation (used / allocatable) | 0.04055 | 0.03698 | -8.8% | -0.004178 to -0.002966 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9732 | 0.8874 | -8.8% | -0.1003 to -0.07118 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01717 | +0.0172 (native is 0) | +0.01463 to +0.01971 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9732 | 0.9046 | -7.0% | -0.08367 to -0.05344 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 651.5 | 711 | +9.1% | +48.21 to +70.89 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.857 | 9.609 | +8.5% | +0.07346 to +1.429 | yes: power given |
| pods started | 4.9 | 6.2 | +26.5% | -0.5174 to +3.117 | no |
| pod start wait, total (s) | 7.5 | 8.5 | +13.3% | -3.06 to +5.06 | no |
| pod start wait, mean (s) | 1.527 | 1.281 | -16.1% | -0.578 to +0.08564 | no |
| host CPU busy, the real machine under kind (%) | 29.39 | 26.82 | -8.7% | -2.958 to -2.18 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.515 | +0.2% | -0.007958 to +0.01296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.7 | +0.8% | +0.1327 to +2.314 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.7 | +0.8% | +0.1327 to +2.314 | yes: power given |
| response time (ms), mean | 109.2 | 110.4 | +1.2% | -1.809 to +4.379 | no |
| response time (ms), 95th percentile | 234 | 225.6 | -3.6% | -17.1 to +0.1912 | no |
| response time (ms), 99th percentile | 328.3 | 315.2 | -4.0% | -29.17 to +2.842 | no |
| time over the response line (% of samples) | 0.18 | 0.129 | -28.3% | -0.1591 to +0.05718 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.5 (native is 0) | +3.839 to +7.161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.1867 | +250.0% | -0.001546 to +0.2682 | no |
| utilisation (used / allocatable) | 0.03648 | 0.04089 | +12.1% | +0.003578 to +0.005249 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8754 | 0.9814 | +12.1% | +0.08588 to +0.126 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02738 | +0.0274 (native is 0) | +0.02301 to +0.03175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8754 | 1.009 | +15.2% | +0.11 to +0.1566 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 647.7 | -10.1% | -82.48 to -63.15 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.86 | 9.602 | +8.4% | -0.1239 to +1.608 | no |
| pods started | 5 | 5.9 | +18.0% | -0.6617 to +2.462 | no |
| pod start wait, total (s) | 6.8 | 8.8 | +29.4% | -0.7186 to +4.719 | no |
| pod start wait, mean (s) | 1.338 | 1.476 | +10.3% | -0.1961 to +0.4717 | no |
| host CPU busy, the real machine under kind (%) | 25.8 | 30.52 | +18.3% | +3.923 to +5.516 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*