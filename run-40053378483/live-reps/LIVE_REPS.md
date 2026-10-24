# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.219 | 5.13 |
| node-hours | 2.514 | 2.51 | 2.188 | 2.149 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.5 | 272.3 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.5 | 247.7 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 316.7 | 340.2 | 285.9 | 317.2 |
| response time (ms), 95th percentile | 1035 | 1126 | 1091 | 1272 |
| response time (ms), 99th percentile | 1541 | 1687 | 1629 | 1817 |
| time over the response line (% of samples) | 19.15 | 19.91 | 18.41 | 19.62 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.7 | 9.6 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 34.1 | 43.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.572 | 9.663 | 11.08 | 10.05 |
| utilisation (used / allocatable) | 0.05894 | 0.05897 | 0.0688 | 0.07002 |
| CPU used (cores), mean | 1.415 | 1.415 | 1.417 | 1.418 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01554 | 0.01736 |
| CPU used with Omni's own (cores), mean | 1.415 | 1.415 | 1.433 | 1.435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.7 | 471.6 | 417.8 | 413.1 |
| HPA replicas, mean | 1.987 | 1.969 | 2.374 | 2.252 |
| pods started | 0.2 | 0 | 0.5 | 0.2 |
| pod start wait, total (s) | 0.6 | 0 | 1.3 | 0.3 |
| pod start wait, mean (s) | 0.6 | 0 | 1.3 | 0.3 |
| host CPU busy, the real machine under kind (%) | 40.37 | 41.15 | 41.04 | 42.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.5 | 773.2 | 766.4 | 778.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.664 | 4.522 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.2 | 0.05 | 0.225 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | 0.3 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 72.02 | 81.22 | 73.9 | 85.44 |
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
| worker nodes in service, mean | 6 | 5.13 | -14.5% | -1.654 to -0.085 | yes: GAIN |
| node-hours | 2.51 | 2.149 | -14.4% | -0.6918 to -0.02863 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.1 | +0.2% | -0.4435 to +1.668 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 244.8 | -9.8% | -51.5 to -1.929 | yes: GAIN |
| response time (ms), mean | 340.2 | 317.2 | -6.8% | -35.49 to -10.56 | yes: GAIN |
| response time (ms), 95th percentile | 1126 | 1272 | +13.1% | +58.63 to +235.2 | yes: LOSS |
| response time (ms), 99th percentile | 1687 | 1817 | +7.7% | +27.59 to +231.9 | yes: LOSS |
| time over the response line (% of samples) | 19.91 | 19.62 | -1.5% | -0.7836 to +0.1931 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.8 (native is 0) | +21.19 to +66.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.663 | 10.05 | +4.0% | -1.664 to +2.437 | no |
| utilisation (used / allocatable) | 0.05897 | 0.07002 | +18.7% | +0.0005753 to +0.02152 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.418 | +0.2% | -0.01732 to +0.02174 | no |
| Omni's own CPU (cores), mean | 0 | 0.01736 | +0.0174 (native is 0) | +0.01545 to +0.01927 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.435 | +1.4% | +0.000555 to +0.03859 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.6 | 413.1 | -12.4% | -117.3 to +0.2583 | no |
| HPA replicas, mean | 1.969 | 2.252 | +14.4% | +0.06999 to +0.4956 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 41.15 | 42.06 | +2.2% | +0.5897 to +1.218 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.2 | 778.1 | +0.6% | +0.6554 to +9.145 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.522 | -24.6% | -2.694 to -0.261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.225 | +12.5% | -0.03494 to +0.08494 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.22 | 85.44 | +5.2% | +0.5323 to +7.901 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.13e-17 to +1.295e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.51 | -0.2% | -0.01097 to +0.001637 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.5 | -0.2% | -1.181 to +0.1404 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.5 | -0.2% | -1.181 to +0.1404 | no |
| response time (ms), mean | 316.7 | 340.2 | +7.4% | +6.875 to +40.13 | yes: LOSS |
| response time (ms), 95th percentile | 1035 | 1126 | +8.8% | +2.681 to +179.2 | yes: LOSS |
| response time (ms), 99th percentile | 1541 | 1687 | +9.5% | +16.96 to +275.7 | yes: LOSS |
| time over the response line (% of samples) | 19.15 | 19.91 | +4.0% | -0.2483 to +1.777 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.7 | +3.2% | -0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.572 | 9.663 | +1.0% | -1.356 to +1.539 | no |
| utilisation (used / allocatable) | 0.05894 | 0.05897 | +0.1% | -0.0009197 to +0.0009863 | no |
| CPU used (cores), mean | 1.415 | 1.415 | +0.1% | -0.02207 to +0.02367 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.415 | 1.415 | +0.1% | -0.02207 to +0.02367 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.7 | 471.6 | +0.4% | -6.627 to +10.46 | no |
| HPA replicas, mean | 1.987 | 1.969 | -0.9% | -0.1683 to +0.1321 | no |
| pods started | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| host CPU busy, the real machine under kind (%) | 40.37 | 41.15 | +1.9% | +0.4114 to +1.155 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 763.5 | 773.2 | +1.3% | +4.721 to +14.68 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.2 | +182.4% | +0.0641 to +0.1942 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.02 | 81.22 | +12.8% | +3.839 to +14.57 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.219 | -13.0% | -1.553 to -0.009882 | yes: GAIN |
| node-hours | 2.514 | 2.188 | -13.0% | -0.6512 to -0.001941 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 | +0.1% | -0.2733 to +0.8537 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 247.7 | -8.9% | -48.67 to +0.1334 | no |
| response time (ms), mean | 316.7 | 285.9 | -9.7% | -43.11 to -18.53 | yes: GAIN |
| response time (ms), 95th percentile | 1035 | 1091 | +5.5% | -14.4 to +127.4 | no |
| response time (ms), 99th percentile | 1541 | 1629 | +5.7% | -11.96 to +188.2 | no |
| time over the response line (% of samples) | 19.15 | 18.41 | -3.8% | -1.834 to +0.3626 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.6 | +2.1% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.1 (native is 0) | +19.37 to +48.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.572 | 11.08 | +15.8% | -0.3544 to +3.374 | no |
| utilisation (used / allocatable) | 0.05894 | 0.0688 | +16.7% | +0.0002732 to +0.01944 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.417 | +0.2% | -0.03064 to +0.0364 | no |
| Omni's own CPU (cores), mean | 0 | 0.01554 | +0.0155 (native is 0) | +0.01389 to +0.01719 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.433 | +1.3% | -0.0151 to +0.05195 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.7 | 417.8 | -11.1% | -106.7 to +2.811 | no |
| HPA replicas, mean | 1.987 | 2.374 | +19.4% | +0.1624 to +0.6104 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.6 | 1.3 | +116.7% | -0.9877 to +2.388 | no |
| pod start wait, mean (s) | 0.6 | 1.3 | +116.7% | -0.9877 to +2.388 | no |
| host CPU busy, the real machine under kind (%) | 40.37 | 41.04 | +1.6% | +0.3538 to +0.978 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 763.5 | 766.4 | +0.4% | +0.214 to +5.586 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.664 | -22.3% | -2.602 to -0.07017 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.05 | -29.4% | -0.0498 to +0.008131 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.02 | 73.9 | +2.6% | -1.187 to +4.962 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.219 | -13.0% | -1.553 to -0.009882 | yes: GAIN |
| node-hours | 2.51 | 2.188 | -12.8% | -0.6481 to +0.004256 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.3 | +0.3% | +0.191 to +1.43 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 247.7 | -8.7% | -48.03 to +0.5433 | no |
| response time (ms), mean | 340.2 | 285.9 | -16.0% | -72.97 to -35.68 | yes: GAIN |
| response time (ms), 95th percentile | 1126 | 1091 | -3.1% | -93.03 to +24.17 | no |
| response time (ms), 99th percentile | 1687 | 1629 | -3.5% | -162.6 to +46.16 | no |
| time over the response line (% of samples) | 19.91 | 18.41 | -7.5% | -2.49 to -0.5094 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.6 | -1.0% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.1 (native is 0) | +19.37 to +48.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.663 | 11.08 | +14.7% | -1.028 to +3.865 | no |
| utilisation (used / allocatable) | 0.05897 | 0.0688 | +16.7% | -0.0004007 to +0.02005 | no |
| CPU used (cores), mean | 1.415 | 1.417 | +0.1% | -0.02361 to +0.02777 | no |
| Omni's own CPU (cores), mean | 0 | 0.01554 | +0.0155 (native is 0) | +0.01389 to +0.01719 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.433 | +1.2% | -0.007448 to +0.04269 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.6 | 417.8 | -11.4% | -114.2 to +6.426 | no |
| HPA replicas, mean | 1.969 | 2.374 | +20.5% | +0.2038 to +0.6052 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | +0.1791 to +2.421 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.1791 to +2.421 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.15 | 41.04 | -0.3% | -0.3441 to +0.1092 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.2 | 766.4 | -0.9% | -10.95 to -2.645 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.664 | -22.3% | -2.602 to -0.07017 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.05 | -75.0% | -0.2205 to -0.07947 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | -62.5% | -0.877 to -0.123 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 81.22 | 73.9 | -9.0% | -12.49 to -2.147 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.13 | -14.5% | -1.654 to -0.085 | yes: GAIN |
| node-hours | 2.514 | 2.149 | -14.5% | -0.6957 to -0.03405 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 | +0.0% | -0.7349 to +0.9184 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 244.8 | -10.0% | -52.2 to -2.275 | yes: GAIN |
| response time (ms), mean | 316.7 | 317.2 | +0.2% | -16.61 to +17.56 | no |
| response time (ms), 95th percentile | 1035 | 1272 | +23.0% | +101.2 to +374.4 | yes: LOSS |
| response time (ms), 99th percentile | 1541 | 1817 | +17.9% | +78.57 to +473.6 | yes: LOSS |
| time over the response line (% of samples) | 19.15 | 19.62 | +2.4% | -0.3003 to +1.238 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.8 | +4.3% | +0.03062 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.8 (native is 0) | +21.19 to +66.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.572 | 10.05 | +5.0% | -1.448 to +2.404 | no |
| utilisation (used / allocatable) | 0.05894 | 0.07002 | +18.8% | +0.001281 to +0.02088 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.418 | +0.2% | -0.01737 to +0.02339 | no |
| Omni's own CPU (cores), mean | 0 | 0.01736 | +0.0174 (native is 0) | +0.01545 to +0.01927 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.435 | +1.4% | -0.000914 to +0.04165 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.7 | 413.1 | -12.1% | -109.1 to -4.117 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.252 | +13.3% | +0.0527 to +0.4768 | yes: power given |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.6 | 0.3 | -50.0% | -1.471 to +0.8705 | no |
| pod start wait, mean (s) | 0.6 | 0.3 | -50.0% | -1.471 to +0.8705 | no |
| host CPU busy, the real machine under kind (%) | 40.37 | 42.06 | +4.2% | +1.21 to +2.165 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 763.5 | 778.1 | +1.9% | +6.902 to +22.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.522 | -24.6% | -2.694 to -0.261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.225 | +217.6% | +0.08819 to +0.2201 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | +80.0% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72.02 | 85.44 | +18.6% | +6.224 to +20.62 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*