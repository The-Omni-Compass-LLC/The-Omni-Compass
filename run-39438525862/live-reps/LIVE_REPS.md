# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.9 | 10.94 |
| node-hours | 5.024 | 5.029 | 4.568 | 4.588 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.1 | 526.2 | 528.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 526.1 | 491.7 | 494.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 555 | 709.8 | 563.2 | 808.5 |
| response time (ms), 95th percentile | 2164 | 3269 | 2439 | 3923 |
| response time (ms), 99th percentile | 3077 | 4767 | 3538 | 5337 |
| time over the response line (% of samples) | 21.93 | 24.64 | 23.4 | 25.85 |
| failed requests (%) | 0.0157 | 0.08233 | 0 | 0.159 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.33 | 15.22 | 13 | 16.44 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 68.22 | 43.11 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 41.67 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.02 | 26.94 | 13.16 | 20.75 |
| utilisation (used / allocatable) | 0.03468 | 0.03522 | 0.03899 | 0.04041 |
| CPU used (cores), mean | 1.665 | 1.691 | 1.694 | 1.771 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0133 | 0.0099 |
| CPU used with Omni's own (cores), mean | 1.665 | 1.691 | 1.707 | 1.781 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.9 | 757.9 | 699.4 | 678.2 |
| HPA replicas, mean | 3.911 | 4.052 | 4.461 | 4.526 |
| pods started | 0.2222 | 0.4444 | 1.222 | 1.778 |
| pod start wait, total (s) | 0.5556 | 1.111 | 2.222 | 3.889 |
| pod start wait, mean (s) | 0.5556 | 0.8333 | 1.389 | 1.101 |
| host CPU busy, the real machine under kind (%) | 50.73 | 56.65 | 52.94 | 59.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 852.7 | 952.2 | 875.9 | 993.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.924 | 10.02 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07407 | 3.431 | 0.1019 | 1.963 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 36.89 | 0.6667 | 1.556 |
| queue: job turnaround, submitted to done, mean (s) | 163.2 | 258.1 | 182 | 298.7 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | -8.9% | -2.283 to +0.1539 | no |
| node-hours | 5.029 | 4.588 | -8.8% | -0.9506 to +0.06889 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 528.3 | +0.4% | -0.2748 to +4.735 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 494.7 | -6.0% | -70.12 to +7.403 | no |
| response time (ms), mean | 709.8 | 808.5 | +13.9% | -2.849 to +200.2 | no |
| response time (ms), 95th percentile | 3269 | 3923 | +20.0% | +135.6 to +1173 | yes: LOSS |
| response time (ms), 99th percentile | 4767 | 5337 | +12.0% | +87.34 to +1053 | yes: LOSS |
| time over the response line (% of samples) | 24.64 | 25.85 | +4.9% | -0.03646 to +2.461 | no |
| failed requests (%) | 0.08233 | 0.159 | +93.2% | -0.002873 to +0.1563 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.22 | 16.44 | +8.0% | +0.02043 to +2.424 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.11 | +43.1 (native is 0) | +37.35 to +48.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.94 | 20.75 | -23.0% | -25.44 to +13.06 | no |
| utilisation (used / allocatable) | 0.03522 | 0.04041 | +14.7% | +0.001332 to +0.00905 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.691 | 1.771 | +4.8% | -0.03064 to +0.1924 | no |
| Omni's own CPU (cores), mean | 0 | 0.0099 | +0.0099 (native is 0) | +0.008994 to +0.01081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.691 | 1.781 | +5.4% | -0.02106 to +0.2026 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757.9 | 678.2 | -10.5% | -137.9 to -21.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.052 | 4.526 | +11.7% | +0.08524 to +0.8628 | yes: power given |
| pods started | 0.4444 | 1.778 | +300.0% | -0.7004 to +3.367 | no |
| pod start wait, total (s) | 1.111 | 3.889 | +250.0% | -2.361 to +7.917 | no |
| pod start wait, mean (s) | 0.8333 | 1.101 | +32.1% | -1.225 to +1.76 | no |
| host CPU busy, the real machine under kind (%) | 56.65 | 59.29 | +4.7% | +1.687 to +3.59 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 952.2 | 993.1 | +4.3% | +16.71 to +65.07 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.02 | -16.5% | -4.128 to +0.1636 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.431 | 1.963 | -42.8% | -4.961 to +2.026 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 36.89 | 1.556 | -95.8% | -117.7 to +47.01 | no |
| queue: job turnaround, submitted to done, mean (s) | 258.1 | 298.7 | +15.7% | +15.17 to +66.06 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -5.235e-15 to -2.912e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.024 | 5.029 | +0.1% | -0.01381 to +0.0227 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.1 | +0.2% | -0.526 to +2.284 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 526.1 | +0.2% | -0.526 to +2.284 | no |
| response time (ms), mean | 555 | 709.8 | +27.9% | +74.86 to +234.8 | yes: LOSS |
| response time (ms), 95th percentile | 2164 | 3269 | +51.1% | +474.7 to +1735 | yes: LOSS |
| response time (ms), 99th percentile | 3077 | 4767 | +54.9% | +727.7 to +2651 | yes: LOSS |
| time over the response line (% of samples) | 21.93 | 24.64 | +12.4% | +0.1048 to +5.324 | yes: LOSS |
| failed requests (%) | 0.0157 | 0.08233 | +424.2% | -0.01642 to +0.1497 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.33 | 15.22 | +34.3% | +1.506 to +6.272 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.02 | 26.94 | +124.1% | -1.481 to +31.32 | no |
| utilisation (used / allocatable) | 0.03468 | 0.03522 | +1.6% | -0.00113 to +0.002211 | no |
| CPU used (cores), mean | 1.665 | 1.691 | +1.6% | -0.05422 to +0.1061 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.665 | 1.691 | +1.6% | -0.05422 to +0.1061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.9 | 757.9 | -1.2% | -37.12 to +18.93 | no |
| HPA replicas, mean | 3.911 | 4.052 | +3.6% | -0.006695 to +0.2881 | no |
| pods started | 0.2222 | 0.4444 | +100.0% | -0.5248 to +0.9692 | no |
| pod start wait, total (s) | 0.5556 | 1.111 | +100.0% | -1.332 to +2.443 | no |
| pod start wait, mean (s) | 0.5556 | 0.8333 | +50.0% | -1.249 to +1.804 | no |
| host CPU busy, the real machine under kind (%) | 50.73 | 56.65 | +11.7% | +3.919 to +7.918 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 852.7 | 952.2 | +11.7% | +43.49 to +155.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07407 | 3.431 | +4531.3% | -3.652 to +10.36 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 36.89 | +6540.0% | -46.3 to +119 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.2 | 258.1 | +58.2% | +47.09 to +142.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.9 | -9.1% | -2.306 to +0.11 | no |
| node-hours | 5.024 | 4.568 | -9.1% | -0.9585 to +0.0456 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.2 | +0.2% | -0.4832 to +2.52 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 491.7 | -6.4% | -71.37 to +4.327 | no |
| response time (ms), mean | 555 | 563.2 | +1.5% | -14.54 to +30.94 | no |
| response time (ms), 95th percentile | 2164 | 2439 | +12.7% | +128.7 to +421.8 | yes: LOSS |
| response time (ms), 99th percentile | 3077 | 3538 | +15.0% | +107.4 to +814.6 | yes: LOSS |
| time over the response line (% of samples) | 21.93 | 23.4 | +6.7% | -0.1192 to +3.072 | no |
| failed requests (%) | 0.0157 | 0 | -100.0% | -0.05192 to +0.02051 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.33 | 13 | +14.7% | -0.2931 to +3.626 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.22 | +68.2 (native is 0) | +39.17 to +97.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.02 | 13.16 | +9.5% | -1.66 to +3.953 | no |
| utilisation (used / allocatable) | 0.03468 | 0.03899 | +12.4% | +0.0001283 to +0.008502 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.665 | 1.694 | +1.7% | -0.01714 to +0.07527 | no |
| Omni's own CPU (cores), mean | 0 | 0.0133 | +0.0133 (native is 0) | +0.01188 to +0.01472 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.665 | 1.707 | +2.5% | -0.003015 to +0.08775 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.9 | 699.4 | -8.8% | -128.3 to -6.738 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.911 | 4.461 | +14.1% | +0.3152 to +0.7847 | yes: power given |
| pods started | 0.2222 | 1.222 | +450.0% | +0.05858 to +1.941 | yes: power given |
| pod start wait, total (s) | 0.5556 | 2.222 | +300.0% | -0.403 to +3.736 | no |
| pod start wait, mean (s) | 0.5556 | 1.389 | +150.0% | -0.5524 to +2.219 | no |
| host CPU busy, the real machine under kind (%) | 50.73 | 52.94 | +4.3% | +1.484 to +2.925 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 852.7 | 875.9 | +2.7% | +8.368 to +38.08 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.924 | -17.3% | -4.224 to +0.07221 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07407 | 0.1019 | +37.5% | -0.02286 to +0.07842 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 0.6667 | +20.0% | -0.3508 to +0.573 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.2 | 182 | +11.6% | +7.996 to +29.74 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.9 | -9.1% | -2.306 to +0.11 | no |
| node-hours | 5.029 | 4.568 | -9.2% | -0.9698 to +0.04797 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 526.2 | +0.0% | -0.9117 to +1.19 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 491.7 | -6.5% | -72.57 to +3.77 | no |
| response time (ms), mean | 709.8 | 563.2 | -20.7% | -219 to -74.17 | yes: GAIN |
| response time (ms), 95th percentile | 3269 | 2439 | -25.4% | -1409 to -250.2 | yes: GAIN |
| response time (ms), 99th percentile | 4767 | 3538 | -25.8% | -1968 to -489.5 | yes: GAIN |
| time over the response line (% of samples) | 24.64 | 23.4 | -5.0% | -3.426 to +0.9491 | no |
| failed requests (%) | 0.08233 | 0 | -100.0% | -0.1987 to +0.03403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.22 | 13 | -14.6% | -3.596 to -0.8484 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.22 | +68.2 (native is 0) | +39.17 to +97.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.94 | 13.16 | -51.1% | -29.09 to +1.538 | no |
| utilisation (used / allocatable) | 0.03522 | 0.03899 | +10.7% | -0.001164 to +0.008712 | no |
| CPU used (cores), mean | 1.691 | 1.694 | +0.2% | -0.08645 to +0.09267 | no |
| Omni's own CPU (cores), mean | 0 | 0.0133 | +0.0133 (native is 0) | +0.01188 to +0.01472 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.691 | 1.707 | +1.0% | -0.07308 to +0.1059 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757.9 | 699.4 | -7.7% | -133.8 to +17 | no |
| HPA replicas, mean | 4.052 | 4.461 | +10.1% | +0.2096 to +0.6088 | yes: power given |
| pods started | 0.4444 | 1.222 | +175.0% | -0.0623 to +1.618 | no |
| pod start wait, total (s) | 1.111 | 2.222 | +100.0% | -0.5395 to +2.762 | no |
| pod start wait, mean (s) | 0.8333 | 1.389 | +66.7% | -0.2918 to +1.403 | no |
| host CPU busy, the real machine under kind (%) | 56.65 | 52.94 | -6.6% | -5.102 to -2.326 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 952.2 | 875.9 | -8.0% | -119.2 to -33.5 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.924 | -17.3% | -4.224 to +0.07221 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.431 | 0.1019 | -97.0% | -10.32 to +3.664 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 36.89 | 0.6667 | -98.2% | -118.9 to +46.44 | no |
| queue: job turnaround, submitted to done, mean (s) | 258.1 | 182 | -29.5% | -115.4 to -36.66 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | -8.9% | -2.283 to +0.1539 | no |
| node-hours | 5.024 | 4.588 | -8.7% | -0.9393 to +0.06656 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 528.3 | +0.6% | +0.9584 to +5.26 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 494.7 | -5.8% | -68.92 to +7.961 | no |
| response time (ms), mean | 555 | 808.5 | +45.7% | +87.82 to +419.1 | yes: LOSS |
| response time (ms), 95th percentile | 2164 | 3923 | +81.3% | +723.6 to +2794 | yes: LOSS |
| response time (ms), 99th percentile | 3077 | 5337 | +73.4% | +1057 to +3462 | yes: LOSS |
| time over the response line (% of samples) | 21.93 | 25.85 | +17.9% | +1.921 to +5.933 | yes: LOSS |
| failed requests (%) | 0.0157 | 0.159 | +912.6% | +0.01193 to +0.2747 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.33 | 16.44 | +45.1% | +2.409 to +7.814 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.11 | +43.1 (native is 0) | +37.35 to +48.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.02 | 20.75 | +72.7% | +0.4615 to +17 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03468 | 0.04041 | +16.5% | +0.002644 to +0.008819 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.665 | 1.771 | +6.4% | +0.01001 to +0.2037 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0099 | +0.0099 (native is 0) | +0.008994 to +0.01081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.665 | 1.781 | +7.0% | +0.01969 to +0.2138 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.9 | 678.2 | -11.6% | -132.3 to -45.24 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.911 | 4.526 | +15.7% | +0.2409 to +0.9886 | yes: power given |
| pods started | 0.2222 | 1.778 | +700.0% | -0.2921 to +3.403 | no |
| pod start wait, total (s) | 0.5556 | 3.889 | +600.0% | -1.436 to +8.103 | no |
| pod start wait, mean (s) | 0.5556 | 1.101 | +98.1% | -0.8107 to +1.901 | no |
| host CPU busy, the real machine under kind (%) | 50.73 | 59.29 | +16.9% | +5.729 to +11.39 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 852.7 | 993.1 | +16.5% | +62.94 to +217.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.02 | -16.5% | -4.128 to +0.1636 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07407 | 1.963 | +2550.0% | -1.628 to +5.406 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1.556 | +180.0% | +0.4565 to +1.544 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 163.2 | 298.7 | +83.0% | +65.2 to +205.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*