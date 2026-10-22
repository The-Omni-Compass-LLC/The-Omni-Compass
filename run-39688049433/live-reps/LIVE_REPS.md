# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.135 | 5.21 |
| node-hours | 2.514 | 2.517 | 2.153 | 2.184 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.1 | 270.2 | 269.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 270.1 | 243 | 245 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 216.4 | 204.7 | 209.8 | 199.1 |
| response time (ms), 95th percentile | 660.6 | 631 | 656.3 | 618.9 |
| response time (ms), 99th percentile | 993.3 | 982 | 986.6 | 957.6 |
| time over the response line (% of samples) | 8.744 | 6.982 | 7.965 | 7.474 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.9 | 6.5 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 10.5 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.26 | 7.085 | 7.382 | 8.242 |
| utilisation (used / allocatable) | 0.05391 | 0.0542 | 0.06425 | 0.06144 |
| CPU used (cores), mean | 1.294 | 1.301 | 1.3 | 1.275 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01186 | 0.01288 |
| CPU used with Omni's own (cores), mean | 1.294 | 1.301 | 1.312 | 1.288 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 512.6 | 510.7 | 450.2 | 465.5 |
| HPA replicas, mean | 2.054 | 2.011 | 2.275 | 2.359 |
| pods started | 0 | 0 | 0.3 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 0.6 | 0.9 |
| pod start wait, mean (s) | 0 | 0 | 0.6 | 0.9 |
| host CPU busy, the real machine under kind (%) | 37.82 | 38.65 | 38.45 | 39.13 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 742.2 | 741.8 | 740.2 | 742.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.513 | 4.605 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.125 | 0.05417 | 0.1167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.8 | 0.3 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 48.46 | 50.02 | 46.63 | 50.07 |
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
| worker nodes in service, mean | 6 | 5.21 | -13.2% | -1.483 to -0.09663 | yes: GAIN |
| node-hours | 2.517 | 2.184 | -13.2% | -0.6225 to -0.04345 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.1 | 269.9 | -0.1% | -1.315 to +0.8176 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.1 | 245 | -9.3% | -47.09 to -3.126 | yes: GAIN |
| response time (ms), mean | 204.7 | 199.1 | -2.8% | -16.43 to +5.114 | no |
| response time (ms), 95th percentile | 631 | 618.9 | -1.9% | -104.3 to +80.09 | no |
| response time (ms), 99th percentile | 982 | 957.6 | -2.5% | -225.5 to +176.7 | no |
| time over the response line (% of samples) | 6.982 | 7.474 | +7.0% | -0.8697 to +1.854 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 6.3 | +6.8% | -0.8251 to +1.625 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.6 (native is 0) | +9.506 to +15.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.085 | 8.242 | +16.3% | -0.5344 to +2.848 | no |
| utilisation (used / allocatable) | 0.0542 | 0.06144 | +13.4% | +0.0006715 to +0.01382 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.301 | 1.275 | -2.0% | -0.0717 to +0.0204 | no |
| Omni's own CPU (cores), mean | 0 | 0.01288 | +0.0129 (native is 0) | +0.01119 to +0.01457 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.301 | 1.288 | -1.0% | -0.05879 to +0.03325 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.7 | 465.5 | -8.8% | -88.44 to -1.883 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.359 | +17.3% | +0.09427 to +0.6014 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.65 | 39.13 | +1.2% | +0.08848 to +0.8534 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 741.8 | 742.7 | +0.1% | -2.377 to +4.177 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.605 | -23.3% | -2.604 to -0.1869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.1167 | -6.7% | -0.03912 to +0.02245 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.6 | -25.0% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 50.02 | 50.07 | +0.1% | -4.56 to +4.676 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.735e-15 to -4.108e-17 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.517 | +0.1% | -0.004214 to +0.01055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.1 | +0.1% | -0.5788 to +1.272 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 270.1 | +0.1% | -0.5788 to +1.272 | no |
| response time (ms), mean | 216.4 | 204.7 | -5.4% | -33.05 to +9.628 | no |
| response time (ms), 95th percentile | 660.6 | 631 | -4.5% | -122.5 to +63.43 | no |
| response time (ms), 99th percentile | 993.3 | 982 | -1.1% | -211.2 to +188.6 | no |
| time over the response line (% of samples) | 8.744 | 6.982 | -20.1% | -3.821 to +0.2981 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.9 | -10.6% | -1.458 to +0.05776 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.26 | 7.085 | -2.4% | -1.903 to +1.553 | no |
| utilisation (used / allocatable) | 0.05391 | 0.0542 | +0.5% | -0.001624 to +0.002197 | no |
| CPU used (cores), mean | 1.294 | 1.301 | +0.5% | -0.03897 to +0.05272 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.294 | 1.301 | +0.5% | -0.03897 to +0.05272 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 512.6 | 510.7 | -0.4% | -26.21 to +22.37 | no |
| HPA replicas, mean | 2.054 | 2.011 | -2.1% | -0.1659 to +0.07954 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 37.82 | 38.65 | +2.2% | +0.1085 to +1.569 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 742.2 | 741.8 | -0.1% | -5.912 to +5.112 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.125 | +130.8% | +0.02857 to +0.1131 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.8 | +100.0% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 48.46 | 50.02 | +3.2% | -5.006 to +8.122 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.135 | -14.4% | -1.619 to -0.1103 | yes: GAIN |
| node-hours | 2.514 | 2.153 | -14.4% | -0.6798 to -0.04221 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.2 | +0.1% | -0.458 to +1.214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 243 | -9.9% | -50.73 to -2.814 | yes: GAIN |
| response time (ms), mean | 216.4 | 209.8 | -3.0% | -25.05 to +11.86 | no |
| response time (ms), 95th percentile | 660.6 | 656.3 | -0.6% | -73.3 to +64.81 | no |
| response time (ms), 99th percentile | 993.3 | 986.6 | -0.7% | -126.5 to +113.2 | no |
| time over the response line (% of samples) | 8.744 | 7.965 | -8.9% | -2.536 to +0.9781 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.5 | -1.5% | -1.02 to +0.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.5 | +10.5 (native is 0) | +7.517 to +13.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.26 | 7.382 | +1.7% | -2.135 to +2.378 | no |
| utilisation (used / allocatable) | 0.05391 | 0.06425 | +19.2% | +0.0005471 to +0.02013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.294 | 1.3 | +0.5% | -0.02955 to +0.04171 | no |
| Omni's own CPU (cores), mean | 0 | 0.01186 | +0.0119 (native is 0) | +0.01109 to +0.01263 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.294 | 1.312 | +1.4% | -0.01799 to +0.05387 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 512.6 | 450.2 | -12.2% | -120.5 to -4.415 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.054 | 2.275 | +10.7% | +0.01331 to +0.4283 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 37.82 | 38.45 | +1.7% | -0.06655 to +1.346 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 742.2 | 740.2 | -0.3% | -7.732 to +3.732 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.513 | -24.8% | -2.722 to -0.252 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.05417 | +0.0% | -0.03974 to +0.03974 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.46 | 46.63 | -3.8% | -6.972 to +3.322 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.135 | -14.4% | -1.619 to -0.1103 | yes: GAIN |
| node-hours | 2.517 | 2.153 | -14.5% | -0.6816 to -0.04676 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.1 | 270.2 | +0.0% | -0.9627 to +1.025 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.1 | 243 | -10.0% | -51.13 to -3.111 | yes: GAIN |
| response time (ms), mean | 204.7 | 209.8 | +2.5% | -5.859 to +16.09 | no |
| response time (ms), 95th percentile | 631 | 656.3 | +4.0% | -52.98 to +103.6 | no |
| response time (ms), 99th percentile | 982 | 986.6 | +0.5% | -203 to +212.4 | no |
| time over the response line (% of samples) | 6.982 | 7.965 | +14.1% | +0.3122 to +1.653 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 6.5 | +10.2% | -0.3656 to +1.566 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.5 | +10.5 (native is 0) | +7.517 to +13.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.085 | 7.382 | +4.2% | -1.656 to +2.25 | no |
| utilisation (used / allocatable) | 0.0542 | 0.06425 | +18.5% | +0.0009899 to +0.01912 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.301 | 1.3 | -0.1% | -0.02517 to +0.02357 | no |
| Omni's own CPU (cores), mean | 0 | 0.01186 | +0.0119 (native is 0) | +0.01109 to +0.01263 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.301 | 1.312 | +0.9% | -0.01295 to +0.03507 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.7 | 450.2 | -11.8% | -114.6 to -6.397 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.275 | +13.1% | +0.05769 to +0.4702 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 38.65 | 38.45 | -0.5% | -0.5783 to +0.1797 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 741.8 | 740.2 | -0.2% | -5.677 to +2.477 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.513 | -24.8% | -2.722 to -0.252 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.05417 | -56.7% | -0.1322 to -0.00951 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | -62.5% | -1.006 to +0.005799 | no |
| queue: job turnaround, submitted to done, mean (s) | 50.02 | 46.63 | -6.8% | -9.793 to +3.027 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.21 | -13.2% | -1.483 to -0.09663 | yes: GAIN |
| node-hours | 2.514 | 2.184 | -13.1% | -0.6205 to -0.03912 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.9 | +0.0% | -0.8913 to +1.087 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 245 | -9.2% | -46.74 to -2.789 | yes: GAIN |
| response time (ms), mean | 216.4 | 199.1 | -8.0% | -44.06 to +9.319 | no |
| response time (ms), 95th percentile | 660.6 | 618.9 | -6.3% | -137.8 to +54.49 | no |
| response time (ms), 99th percentile | 993.3 | 957.6 | -3.6% | -180.6 to +109.2 | no |
| time over the response line (% of samples) | 8.744 | 7.474 | -14.5% | -4.079 to +1.539 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 6.3 | -4.5% | -1.608 to +1.008 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.6 (native is 0) | +9.506 to +15.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.26 | 8.242 | +13.5% | -1.589 to +3.552 | no |
| utilisation (used / allocatable) | 0.05391 | 0.06144 | +14.0% | +0.0006845 to +0.01438 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.294 | 1.275 | -1.5% | -0.05606 to +0.01851 | no |
| Omni's own CPU (cores), mean | 0 | 0.01288 | +0.0129 (native is 0) | +0.01119 to +0.01457 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.294 | 1.288 | -0.5% | -0.04307 to +0.03129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 512.6 | 465.5 | -9.2% | -87.84 to -6.326 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.054 | 2.359 | +14.8% | +0.06765 to +0.5417 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.82 | 39.13 | +3.5% | +0.7094 to +1.91 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 742.2 | 742.7 | +0.1% | -6.905 to +7.905 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.605 | -23.3% | -2.604 to -0.1869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1167 | +115.4% | +0.01333 to +0.1117 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.46 | 50.08 | +3.3% | -6.313 to +9.546 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*