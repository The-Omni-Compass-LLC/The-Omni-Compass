# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.02 | 10.05 |
| node-hours | 5.031 | 5.039 | 4.195 | 4.207 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 525.5 | 523.3 | 524.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 525.5 | 461.1 | 463.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 428.5 | 557.3 | 410.7 | 632.4 |
| response time (ms), 95th percentile | 1669 | 2695 | 1765 | 3272 |
| response time (ms), 99th percentile | 2436 | 3949 | 2594 | 4356 |
| time over the response line (% of samples) | 16.31 | 17.98 | 16.29 | 18.61 |
| failed requests (%) | 0 | 0.02034 | 0 | 0.08612 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 11.2 | 8.5 | 12 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 96.2 | 49.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.158 | 15.46 | 11.59 | 17.29 |
| utilisation (used / allocatable) | 0.03223 | 0.03286 | 0.03872 | 0.03988 |
| CPU used (cores), mean | 1.547 | 1.577 | 1.524 | 1.598 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01296 | 0.00956 |
| CPU used with Omni's own (cores), mean | 1.547 | 1.577 | 1.537 | 1.608 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.7 | 825.9 | 726.5 | 707.1 |
| HPA replicas, mean | 4.011 | 3.977 | 4.553 | 4.411 |
| pods started | 0.2 | 0.2 | 1.1 | 1.3 |
| pod start wait, total (s) | 0.4 | 0.4 | 1.6 | 1.9 |
| pod start wait, mean (s) | 0.2 | 0.2 | 0.7333 | 1.033 |
| host CPU busy, the real machine under kind (%) | 46.22 | 51.89 | 48.03 | 54.72 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 811.2 | 888.6 | 821.2 | 929.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.875 | 8.878 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.3708 | 0.06667 | 0.3375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | 0.4 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 121.5 | 187.7 | 127.7 | 234 |
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
| worker nodes in service, mean | 12 | 10.05 | −16.2% | −3.7000 to −0.1964 | yes: GAIN |
| node-hours | 5.039 | 4.207 | −16.5% | −1.5570 to −0.1066 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 524.6 | −0.2% | −2.4517 to +0.4864 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 463.4 | −11.8% | −116.8179 to −7.5183 | yes: GAIN |
| response time (ms), mean | 557.3 | 632.4 | +13.5% | −7.7512 to +158.0796 | no |
| response time (ms), 95th percentile | 2695 | 3272 | +21.4% | +136.2255 to +1018.1985 | yes: LOSS |
| response time (ms), 99th percentile | 3949 | 4356 | +10.3% | +11.9422 to +802.8104 | yes: LOSS |
| time over the response line (% of samples) | 17.98 | 18.61 | +3.5% | −0.0723 to +1.3305 | no |
| failed requests (%) | 0.02034 | 0.08612 | +323.4% | −0.0120 to +0.1436 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12 | +7.1% | +0.2358 to +1.3642 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 | +49.900 (native is 0) | +37.1958 to +62.6042 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.46 | 17.29 | +11.9% | −0.4279 to +4.0946 | no |
| utilisation (used / allocatable) | 0.03286 | 0.03988 | +21.4% | +0.0019 to +0.0122 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.577 | 1.598 | +1.3% | −0.0427 to +0.0838 | no |
| Omni's own CPU (cores), mean | 0 | 0.00956 | +0.010 (native is 0) | +0.0084 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.577 | 1.608 | +1.9% | −0.0341 to +0.0943 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.9 | 707.1 | −14.4% | −205.6389 to −31.8166 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.977 | 4.411 | +10.9% | +0.1930 to +0.6767 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.4 | 1.9 | +375.0% | −0.2276 to +3.2276 | no |
| pod start wait, mean (s) | 0.2 | 1.033 | +416.7% | −0.0373 to +1.7040 | no |
| host CPU busy, the real machine under kind (%) | 51.89 | 54.72 | +5.5% | +1.3985 to +4.2723 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 888.6 | 929.1 | +4.6% | +9.7459 to +71.2541 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.878 | −26.0% | −5.8034 to −0.4401 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.3375 | −9.0% | −0.1335 to +0.0668 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1 | −9.1% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 187.7 | 234 | +24.7% | +11.8083 to +80.9333 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.031 | 5.039 | +0.2% | −0.0091 to +0.0257 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 525.5 | +0.2% | −1.1768 to +3.5521 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 525.5 | +0.2% | −1.1768 to +3.5521 | no |
| response time (ms), mean | 428.5 | 557.3 | +30.1% | +45.8481 to +211.7752 | yes: LOSS |
| response time (ms), 95th percentile | 1669 | 2695 | +61.5% | +314.9369 to +1736.8441 | yes: LOSS |
| response time (ms), 99th percentile | 2436 | 3949 | +62.1% | +463.4364 to +2562.5302 | yes: LOSS |
| time over the response line (% of samples) | 16.31 | 17.98 | +10.3% | −0.2466 to +3.5932 | no |
| failed requests (%) | 0 | 0.02034 | +0.020 (native is 0) | −0.0257 to +0.0663 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 11.2 | +40.0% | +0.6587 to +5.7413 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.158 | 15.46 | +68.8% | +1.4016 to +11.1984 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03223 | 0.03286 | +2.0% | −0.0008 to +0.0021 | no |
| CPU used (cores), mean | 1.547 | 1.577 | +2.0% | −0.0401 to +0.1013 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.547 | 1.577 | +2.0% | −0.0401 to +0.1013 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.7 | 825.9 | +0.0% | −34.9336 to +35.2213 | no |
| HPA replicas, mean | 4.011 | 3.977 | −0.9% | −0.2540 to +0.1850 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −1.3488 to +1.3488 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 46.22 | 51.89 | +12.3% | +3.9104 to +7.4190 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.2 | 888.6 | +9.5% | +23.0479 to +131.7521 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.3708 | +709.1% | +0.1933 to +0.4567 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 121.5 | 187.7 | +54.5% | +23.5470 to +108.8614 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.02 | −16.5% | −3.7868 to −0.1685 | yes: GAIN |
| node-hours | 5.031 | 4.195 | −16.6% | −1.5908 to −0.0814 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 523.3 | −0.2% | −2.4346 to +0.2748 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 461.1 | −12.1% | −120.4399 to −6.0365 | yes: GAIN |
| response time (ms), mean | 428.5 | 410.7 | −4.1% | −39.4887 to +3.9642 | no |
| response time (ms), 95th percentile | 1669 | 1765 | +5.8% | −61.6543 to +253.9083 | no |
| response time (ms), 99th percentile | 2436 | 2594 | +6.5% | −125.8321 to +441.7521 | no |
| time over the response line (% of samples) | 16.31 | 16.29 | −0.1% | −0.6882 to +0.6591 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.5 | +6.2% | −0.1952 to +1.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.2 | +96.200 (native is 0) | +53.3057 to +139.0943 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.158 | 11.59 | +26.5% | +0.2752 to +4.5848 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03223 | 0.03872 | +20.1% | +0.0011 to +0.0119 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.524 | −1.5% | −0.0789 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.01296 | +0.013 (native is 0) | +0.0115 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.537 | −0.6% | −0.0662 to +0.0462 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.7 | 726.5 | −12.0% | −179.8305 to −18.5683 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.011 | 4.553 | +13.5% | +0.0906 to +0.9941 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0.4 | 1.6 | +300.0% | −0.1403 to +2.5403 | no |
| pod start wait, mean (s) | 0.2 | 0.7333 | +266.7% | −0.0714 to +1.1381 | no |
| host CPU busy, the real machine under kind (%) | 46.22 | 48.03 | +3.9% | +1.1796 to +2.4441 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.2 | 821.2 | +1.2% | −2.5218 to +22.5218 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 8.875 | −26.0% | −5.9452 to −0.3048 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.06667 | +45.5% | −0.0283 to +0.0700 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 121.5 | 127.7 | +5.1% | −1.9255 to +14.3338 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.02 | −16.5% | −3.7868 to −0.1685 | yes: GAIN |
| node-hours | 5.039 | 4.195 | −16.8% | −1.5920 to −0.0969 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 523.3 | −0.4% | −3.9524 to −0.5827 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 461.1 | −12.3% | −119.9002 to −8.9516 | yes: GAIN |
| response time (ms), mean | 557.3 | 410.7 | −26.3% | −226.7464 to −66.4013 | yes: GAIN |
| response time (ms), 95th percentile | 2695 | 1765 | −34.5% | −1592.7563 to −266.7707 | yes: GAIN |
| response time (ms), 99th percentile | 3949 | 2594 | −34.3% | −2311.4764 to −398.5702 | yes: GAIN |
| time over the response line (% of samples) | 17.98 | 16.29 | −9.4% | −3.2500 to −0.1258 | yes: GAIN |
| failed requests (%) | 0.02034 | 0 | −100.0% | −0.0663 to +0.0257 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 8.5 | −24.1% | −4.9380 to −0.4620 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.2 | +96.200 (native is 0) | +53.3057 to +139.0943 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.46 | 11.59 | −25.0% | −7.8238 to +0.0838 | no |
| utilisation (used / allocatable) | 0.03286 | 0.03872 | +17.8% | −0.0009 to +0.0126 | no |
| CPU used (cores), mean | 1.577 | 1.524 | −3.4% | −0.0901 to −0.0170 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01296 | +0.013 (native is 0) | +0.0115 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.577 | 1.537 | −2.6% | −0.0772 to −0.0039 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.9 | 726.5 | −12.0% | −212.6077 to +13.9211 | no |
| HPA replicas, mean | 3.977 | 4.553 | +14.5% | +0.1693 to +0.9844 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0.4 | 1.6 | +300.0% | −0.5779 to +2.9779 | no |
| pod start wait, mean (s) | 0.2 | 0.7333 | +266.7% | −0.3074 to +1.3741 | no |
| host CPU busy, the real machine under kind (%) | 51.89 | 48.03 | −7.4% | −5.4667 to −2.2390 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 888.6 | 821.2 | −7.6% | −114.1300 to −20.6700 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.875 | −26.0% | −5.9452 to −0.3048 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.06667 | −82.0% | −0.4283 to −0.1800 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.4 | −63.6% | −1.0455 to −0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 187.7 | 127.7 | −32.0% | −98.9833 to −21.0167 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.05 | −16.2% | −3.7000 to −0.1964 | yes: GAIN |
| node-hours | 5.031 | 4.207 | −16.4% | −1.5563 to −0.0907 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 524.6 | +0.0% | −1.7946 to +2.2046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 463.4 | −11.6% | −117.4246 to −4.5362 | yes: GAIN |
| response time (ms), mean | 428.5 | 632.4 | +47.6% | +52.6315 to +355.3202 | yes: LOSS |
| response time (ms), 95th percentile | 1669 | 3272 | +96.1% | +506.5101 to +2699.6949 | yes: LOSS |
| response time (ms), 99th percentile | 2436 | 4356 | +78.8% | +608.2891 to +3232.4301 | yes: LOSS |
| time over the response line (% of samples) | 16.31 | 18.61 | +14.1% | −0.0253 to +4.6301 | no |
| failed requests (%) | 0 | 0.08612 | +0.086 (native is 0) | +0.0135 to +0.1587 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 12 | +50.0% | +1.3664 to +6.6336 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 | +49.900 (native is 0) | +37.1958 to +62.6042 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.158 | 17.29 | +88.8% | +2.6557 to +13.6110 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03223 | 0.03988 | +23.8% | +0.0037 to +0.0116 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.598 | +3.3% | −0.0722 to +0.1744 | no |
| Omni's own CPU (cores), mean | 0 | 0.00956 | +0.010 (native is 0) | +0.0084 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.608 | +3.9% | −0.0637 to +0.1851 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.7 | 707.1 | −14.4% | −173.8441 to −63.3236 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.011 | 4.411 | +10.0% | +0.1585 to +0.6423 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.4 | 1.9 | +375.0% | +0.2271 to +2.7729 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.033 | +416.7% | +0.1876 to +1.4790 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.22 | 54.72 | +18.4% | +5.6295 to +11.3709 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.2 | 929.1 | +14.5% | +35.4416 to +200.3584 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.878 | −26.0% | −5.8034 to −0.4401 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.3375 | +636.4% | +0.1340 to +0.4494 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | +233.3% | +0.2172 to +1.1828 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 121.5 | 234 | +92.7% | +38.1286 to +187.0214 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*