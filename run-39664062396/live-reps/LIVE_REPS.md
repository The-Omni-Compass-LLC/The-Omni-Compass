# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.152 | 5.227 |
| node-hours | 2.515 | 2.511 | 2.157 | 2.192 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | 273 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.8 | 246.3 | 249.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 388.2 | 405.8 | 362.7 | 387.4 |
| response time (ms), 95th percentile | 1403 | 1483 | 1514 | 1655 |
| response time (ms), 99th percentile | 1989 | 2111 | 2078 | 2315 |
| time over the response line (% of samples) | 18.68 | 19.07 | 18.64 | 18.53 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9 | 9.2 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 40.4 | 39.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.84 | 11.09 | 11.42 | 9.717 |
| utilisation (used / allocatable) | 0.06147 | 0.06197 | 0.07159 | 0.07107 |
| CPU used (cores), mean | 1.475 | 1.487 | 1.48 | 1.488 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.017 | 0.01738 |
| CPU used with Omni's own (cores), mean | 1.475 | 1.487 | 1.497 | 1.506 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 449.4 | 401.9 | 402.8 |
| HPA replicas, mean | 1.935 | 2.011 | 2.066 | 2.257 |
| pods started | 0.2 | 0.3 | 0.2 | 0.6 |
| pod start wait, total (s) | 0.4 | 0.4 | 0.3 | 1 |
| pod start wait, mean (s) | 0.4 | 0.3 | 0.3 | 0.85 |
| host CPU busy, the real machine under kind (%) | 41.98 | 43.04 | 43.07 | 44.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 795.1 | 805.3 | 799.8 | 809.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.374 | 4.537 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.25 | 0.04583 | 0.2583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | 0.5 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 110.3 | 106.6 | 112.7 |
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
| worker nodes in service, mean | 6 | 5.227 | -12.9% | -1.385 to -0.1604 | yes: GAIN |
| node-hours | 2.511 | 2.192 | -12.7% | -0.5752 to -0.06442 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273.3 | +0.2% | -0.08149 to +1.188 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 249.1 | -8.7% | -42.96 to -4.482 | yes: GAIN |
| response time (ms), mean | 405.8 | 387.4 | -4.5% | -59.18 to +22.45 | no |
| response time (ms), 95th percentile | 1483 | 1655 | +11.6% | -141 to +485.8 | no |
| response time (ms), 99th percentile | 2111 | 2315 | +9.7% | -164.5 to +572.9 | no |
| time over the response line (% of samples) | 19.07 | 18.53 | -2.8% | -1.271 to +0.1981 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.5 | +5.6% | -0.1952 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.1 | +39.1 (native is 0) | +19.75 to +58.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.09 | 9.717 | -12.4% | -2.838 to +0.08495 | no |
| utilisation (used / allocatable) | 0.06197 | 0.07107 | +14.7% | +0.002237 to +0.01597 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.488 | +0.1% | -0.025 to +0.02738 | no |
| Omni's own CPU (cores), mean | 0 | 0.01738 | +0.0174 (native is 0) | +0.01654 to +0.01822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.506 | +1.2% | -0.007645 to +0.04479 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.4 | 402.8 | -10.4% | -83.01 to -10.18 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.257 | +12.2% | +0.04205 to +0.4494 | yes: power given |
| pods started | 0.3 | 0.6 | +100.0% | -0.4578 to +1.058 | no |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0.3 | 0.85 | +183.3% | -0.0909 to +1.191 | no |
| host CPU busy, the real machine under kind (%) | 43.04 | 44.02 | +2.3% | +0.5529 to +1.411 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 805.3 | 809.5 | +0.5% | -2.143 to +10.54 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.537 | -24.4% | -2.585 to -0.341 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.2583 | +3.3% | -0.1435 to +0.1602 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.9 | -10.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 112.7 | +2.2% | -2.696 to +7.529 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.431e-15 to -1.676e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.511 | -0.1% | -0.01281 to +0.00581 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.8 | -0.1% | -1.35 to +0.8406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.8 | -0.1% | -1.35 to +0.8406 | no |
| response time (ms), mean | 388.2 | 405.8 | +4.5% | -4.668 to +39.71 | no |
| response time (ms), 95th percentile | 1403 | 1483 | +5.7% | -33.07 to +193 | no |
| response time (ms), 99th percentile | 1989 | 2111 | +6.1% | -74.4 to +317.3 | no |
| time over the response line (% of samples) | 18.68 | 19.07 | +2.1% | -0.3843 to +1.172 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9 | -2.2% | -1.2 to +0.8003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.84 | 11.09 | -6.3% | -1.873 to +0.3795 | no |
| utilisation (used / allocatable) | 0.06147 | 0.06197 | +0.8% | -0.0007854 to +0.001776 | no |
| CPU used (cores), mean | 1.475 | 1.487 | +0.8% | -0.01885 to +0.04262 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.475 | 1.487 | +0.8% | -0.01885 to +0.04262 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 449.4 | -0.8% | -15.2 to +7.635 | no |
| HPA replicas, mean | 1.935 | 2.011 | +3.9% | -0.0522 to +0.2033 | no |
| pods started | 0.2 | 0.3 | +50.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.4 | 0.4 | +0.0% | -0.9537 to +0.9537 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | -25.0% | -0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 41.98 | 43.04 | +2.5% | +0.6302 to +1.48 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.1 | 805.3 | +1.3% | +2.806 to +17.59 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.25 | +172.7% | +0.05819 to +0.2585 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1 | +66.7% | +0.03062 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 110.3 | +8.9% | +0.7183 to +17.26 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.152 | -14.1% | -1.446 to -0.2513 | yes: GAIN |
| node-hours | 2.515 | 2.157 | -14.2% | -0.6089 to -0.1058 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 | -0.0% | -0.9537 to +0.9416 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 246.3 | -9.8% | -45.75 to -7.619 | yes: GAIN |
| response time (ms), mean | 388.2 | 362.7 | -6.6% | -46.64 to -4.418 | yes: GAIN |
| response time (ms), 95th percentile | 1403 | 1514 | +7.9% | -16.23 to +238.8 | no |
| response time (ms), 99th percentile | 1989 | 2078 | +4.4% | -84.95 to +261.5 | no |
| time over the response line (% of samples) | 18.68 | 18.64 | -0.2% | -1.067 to +0.9949 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.2 | +0.0% | -0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 | +40.4 (native is 0) | +19.74 to +61.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.84 | 11.42 | -3.5% | -1.727 to +0.8935 | no |
| utilisation (used / allocatable) | 0.06147 | 0.07159 | +16.5% | +0.003902 to +0.01634 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.475 | 1.48 | +0.3% | -0.02092 to +0.03074 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.01532 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.475 | 1.497 | +1.5% | -0.003481 to +0.04731 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 401.9 | -11.3% | -85.85 to -16.81 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.935 | 2.066 | +6.8% | -0.03597 to +0.2975 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.4 | 0.3 | -25.0% | -0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | -25.0% | -0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 41.98 | 43.07 | +2.6% | +0.6933 to +1.478 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.1 | 799.8 | +0.6% | -1.053 to +10.45 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.374 | -27.1% | -2.725 to -0.5282 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.04583 | -50.0% | -0.09736 to +0.005694 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 106.6 | +5.2% | -0.4903 to +11.11 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.152 | -14.1% | -1.446 to -0.2513 | yes: GAIN |
| node-hours | 2.511 | 2.157 | -14.1% | -0.6009 to -0.1069 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 | +0.1% | -0.3148 to +0.8118 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 246.3 | -9.7% | -44.98 to -7.881 | yes: GAIN |
| response time (ms), mean | 405.8 | 362.7 | -10.6% | -61.66 to -24.43 | yes: GAIN |
| response time (ms), 95th percentile | 1483 | 1514 | +2.1% | -56.79 to +119.4 | no |
| response time (ms), 99th percentile | 2111 | 2078 | -1.6% | -191.5 to +125.2 | no |
| time over the response line (% of samples) | 19.07 | 18.64 | -2.3% | -1.238 to +0.3784 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.2 | +2.2% | -0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 | +40.4 (native is 0) | +19.74 to +61.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.09 | 11.42 | +3.0% | -0.9515 to +1.612 | no |
| utilisation (used / allocatable) | 0.06197 | 0.07159 | +15.5% | +0.003254 to +0.016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.48 | -0.5% | -0.02951 to +0.01556 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.01532 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.497 | +0.7% | -0.01327 to +0.03333 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.4 | 401.9 | -10.6% | -81.33 to -13.77 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.066 | +2.7% | -0.1357 to +0.2461 | no |
| pods started | 0.3 | 0.2 | -33.3% | -0.7263 to +0.5263 | no |
| pod start wait, total (s) | 0.4 | 0.3 | -25.0% | -0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.3 | +0.0% | -0.754 to +0.754 | no |
| host CPU busy, the real machine under kind (%) | 43.04 | 43.07 | +0.1% | -0.2597 to +0.3202 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 805.3 | 799.8 | -0.7% | -9.887 to -1.113 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.374 | -27.1% | -2.725 to -0.5282 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.04583 | -81.7% | -0.3088 to -0.09954 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.5 | -50.0% | -0.877 to -0.123 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 110.3 | 106.6 | -3.3% | -8.214 to +0.8559 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.227 | -12.9% | -1.385 to -0.1604 | yes: GAIN |
| node-hours | 2.515 | 2.192 | -12.9% | -0.5839 to -0.06272 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.3 | +0.1% | -0.6598 to +1.258 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 249.1 | -8.8% | -43.73 to -4.222 | yes: GAIN |
| response time (ms), mean | 388.2 | 387.4 | -0.2% | -42.7 to +41.01 | no |
| response time (ms), 95th percentile | 1403 | 1655 | +18.0% | -46.94 to +551.7 | no |
| response time (ms), 99th percentile | 1989 | 2315 | +16.4% | -22.38 to +673.7 | no |
| time over the response line (% of samples) | 18.68 | 18.53 | -0.8% | -0.9138 to +0.6288 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.5 | +3.3% | -0.5953 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.1 | +39.1 (native is 0) | +19.75 to +58.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.84 | 9.717 | -17.9% | -3.39 to -0.8571 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06147 | 0.07107 | +15.6% | +0.002579 to +0.01662 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.475 | 1.488 | +0.9% | -0.02224 to +0.04839 | no |
| Omni's own CPU (cores), mean | 0 | 0.01738 | +0.0174 (native is 0) | +0.01654 to +0.01822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.475 | 1.506 | +2.1% | -0.00467 to +0.06558 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 402.8 | -11.1% | -89.51 to -11.24 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.935 | 2.257 | +16.6% | +0.1288 to +0.5138 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0.4 | 0.85 | +112.5% | -0.3488 to +1.249 | no |
| host CPU busy, the real machine under kind (%) | 41.98 | 44.02 | +4.9% | +1.573 to +2.502 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.1 | 809.5 | +1.8% | +4.188 to +24.61 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.537 | -24.4% | -2.585 to -0.341 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.2583 | +181.8% | +0.02547 to +0.3079 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 112.7 | +11.3% | +2.28 to +20.53 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*