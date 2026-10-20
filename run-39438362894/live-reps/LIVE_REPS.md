# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.512 | 1.518 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.8 | 159.6 | 160.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.8 | 159.6 | 160.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 150.4 | 154.8 | 147.8 | 153 |
| response time (ms), 95th percentile | 308.6 | 302.4 | 294.4 | 306.5 |
| response time (ms), 99th percentile | 429.7 | 416.8 | 405.3 | 413.3 |
| time over the response line (% of samples) | 0.4895 | 0.3875 | 0.373 | 0.3741 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.5 | 2.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.1883 | 0.475 | 0.4767 |
| utilisation (used / allocatable) | 0.03844 | 0.04305 | 0.03907 | 0.04384 |
| CPU used (cores), mean | 0.9225 | 1.033 | 0.9377 | 1.052 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00596 | 0.01016 |
| CPU used with Omni's own (cores), mean | 0.9225 | 1.033 | 0.9437 | 1.062 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.8 | 614.8 | 673.4 | 604.6 |
| HPA replicas, mean | 8.965 | 8.91 | 9.988 | 10.3 |
| pods started | 4.5 | 5 | 7.1 | 7.5 |
| pod start wait, total (s) | 7.1 | 7.9 | 12 | 12.2 |
| pod start wait, mean (s) | 1.58 | 1.58 | 1.704 | 1.594 |
| host CPU busy, the real machine under kind (%) | 27.28 | 31.32 | 28.01 | 32.53 |
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

Omni-Compass stayed native in 2 of 10 repetitions (repetitions 2, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.092e-16 to +7.789e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.513 | +0.1% | -0.009051 to +0.01205 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 160.1 | +0.2% | -0.7499 to +1.43 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 160.1 | +0.2% | -0.7499 to +1.43 | no |
| response time (ms), mean | 154.8 | 153 | -1.2% | -4.639 to +1.04 | no |
| response time (ms), 95th percentile | 302.4 | 306.5 | +1.3% | -7.25 to +15.29 | no |
| response time (ms), 99th percentile | 416.8 | 413.3 | -0.9% | -22.44 to +15.26 | no |
| time over the response line (% of samples) | 0.3875 | 0.3741 | -3.5% | -0.1151 to +0.08815 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.3 | +2.3 (native is 0) | +0.9076 to +3.692 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.4767 | +153.1% | -0.01043 to +0.5871 | no |
| utilisation (used / allocatable) | 0.04305 | 0.04384 | +1.9% | +0.0001965 to +0.001397 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.033 | 1.052 | +1.9% | +0.004716 to +0.03353 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01016 | +0.0102 (native is 0) | +0.008942 to +0.01138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 1.062 | +2.8% | +0.01431 to +0.04425 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 614.8 | 604.6 | -1.7% | -17.76 to -2.698 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.91 | 10.3 | +15.7% | +0.7845 to +2.005 | yes: power given |
| pods started | 5 | 7.5 | +50.0% | +1.227 to +3.773 | yes: power given |
| pod start wait, total (s) | 7.9 | 12.2 | +54.4% | +1.58 to +7.02 | yes: LOSS |
| pod start wait, mean (s) | 1.58 | 1.594 | +0.9% | -0.2364 to +0.265 | no |
| host CPU busy, the real machine under kind (%) | 31.32 | 32.53 | +3.8% | +0.7181 to +1.691 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.512 | -0.2% | -0.01179 to +0.004454 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.8 | +0.4% | -0.2117 to +1.497 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.8 | +0.4% | -0.2117 to +1.497 | no |
| response time (ms), mean | 150.4 | 154.8 | +2.9% | +1.342 to +7.486 | yes: LOSS |
| response time (ms), 95th percentile | 308.6 | 302.4 | -2.0% | -15.17 to +2.872 | no |
| response time (ms), 99th percentile | 429.7 | 416.8 | -3.0% | -25.2 to -0.572 | yes: GAIN |
| time over the response line (% of samples) | 0.4895 | 0.3875 | -20.8% | -0.2995 to +0.09558 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | -100.0% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.1883 | -45.7% | -0.5324 to +0.2158 | no |
| utilisation (used / allocatable) | 0.03844 | 0.04305 | +12.0% | +0.004116 to +0.005102 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9225 | 1.033 | +12.0% | +0.09879 to +0.1225 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9225 | 1.033 | +12.0% | +0.09879 to +0.1225 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.8 | 614.8 | -10.1% | -74.83 to -63.04 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.965 | 8.91 | -0.6% | -0.1809 to +0.07145 | no |
| pods started | 4.5 | 5 | +11.1% | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 7.1 | 7.9 | +11.3% | -0.7004 to +2.3 | no |
| pod start wait, mean (s) | 1.58 | 1.58 | +0.0% | -0.2634 to +0.2634 | EVEN, the same (under one part in a million) |
| host CPU busy, the real machine under kind (%) | 27.28 | 31.32 | +14.8% | +3.564 to +4.518 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.718e-16 to +4.495e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.518 | +0.2% | +0.0006531 to +0.005014 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.6 | +0.3% | +0.07053 to +0.7428 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.6 | +0.3% | +0.07053 to +0.7428 | yes: power given |
| response time (ms), mean | 150.4 | 147.8 | -1.7% | -4.835 to -0.4275 | yes: GAIN |
| response time (ms), 95th percentile | 308.6 | 294.4 | -4.6% | -25.45 to -2.885 | yes: GAIN |
| response time (ms), 99th percentile | 429.7 | 405.3 | -5.7% | -40.67 to -8.255 | yes: GAIN |
| time over the response line (% of samples) | 0.4895 | 0.373 | -23.8% | -0.2708 to +0.03766 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | -100.0% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.5315 to +2.469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.475 | +37.0% | -0.2003 to +0.457 | no |
| utilisation (used / allocatable) | 0.03844 | 0.03907 | +1.7% | +2.583e-05 to +0.001248 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9225 | 0.9377 | +1.7% | +0.0006199 to +0.02996 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00596 | +0.00596 (native is 0) | +0.005506 to +0.006414 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9225 | 0.9437 | +2.3% | +0.006469 to +0.03603 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.8 | 673.4 | -1.5% | -20.07 to -0.5901 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.965 | 9.988 | +11.4% | +0.4167 to +1.63 | yes: power given |
| pods started | 4.5 | 7.1 | +57.8% | +0.8093 to +4.391 | yes: power given |
| pod start wait, total (s) | 7.1 | 12 | +69.0% | +2.193 to +7.607 | yes: LOSS |
| pod start wait, mean (s) | 1.58 | 1.704 | +7.8% | -0.1588 to +0.4067 | no |
| host CPU busy, the real machine under kind (%) | 27.28 | 28.01 | +2.7% | +0.3064 to +1.155 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.518 | +0.4% | -0.002251 to +0.01525 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.6 | -0.1% | -1.174 to +0.7026 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.6 | -0.1% | -1.174 to +0.7026 | no |
| response time (ms), mean | 154.8 | 147.8 | -4.6% | -10.21 to -3.884 | yes: GAIN |
| response time (ms), 95th percentile | 302.4 | 294.4 | -2.7% | -16.18 to +0.1455 | no |
| response time (ms), 99th percentile | 416.8 | 405.3 | -2.8% | -23.97 to +0.8192 | no |
| time over the response line (% of samples) | 0.3875 | 0.373 | -3.8% | -0.1488 to +0.1197 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.5315 to +2.469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.475 | +152.2% | -0.006425 to +0.5798 | no |
| utilisation (used / allocatable) | 0.04305 | 0.03907 | -9.2% | -0.004461 to -0.003483 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.033 | 0.9377 | -9.2% | -0.1071 to -0.0836 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00596 | +0.00596 (native is 0) | +0.005506 to +0.006414 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.033 | 0.9437 | -8.7% | -0.1009 to -0.0778 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 614.8 | 673.4 | +9.5% | +51.39 to +65.83 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.91 | 9.988 | +12.1% | +0.426 to +1.731 | yes: power given |
| pods started | 5 | 7.1 | +42.0% | +0.5383 to +3.662 | yes: power given |
| pod start wait, total (s) | 7.9 | 12 | +51.9% | +1.612 to +6.588 | yes: LOSS |
| pod start wait, mean (s) | 1.58 | 1.704 | +7.8% | -0.1359 to +0.3838 | no |
| host CPU busy, the real machine under kind (%) | 31.32 | 28.01 | -10.6% | -3.671 to -2.95 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +9.868e-17 to +1.145e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.513 | -0.1% | -0.009602 to +0.005269 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.1 | +0.6% | +0.2299 to +1.735 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.1 | +0.6% | +0.2299 to +1.735 | yes: power given |
| response time (ms), mean | 150.4 | 153 | +1.7% | -1.464 to +6.692 | no |
| response time (ms), 95th percentile | 308.6 | 306.5 | -0.7% | -15.47 to +11.22 | no |
| response time (ms), 99th percentile | 429.7 | 413.3 | -3.8% | -31.72 to -1.218 | yes: GAIN |
| time over the response line (% of samples) | 0.4895 | 0.3741 | -23.6% | -0.2615 to +0.03061 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | -66.7% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.3 | +2.3 (native is 0) | +0.9076 to +3.692 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.4767 | +37.5% | -0.2635 to +0.5235 | no |
| utilisation (used / allocatable) | 0.03844 | 0.04384 | +14.1% | +0.004594 to +0.006218 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9225 | 1.052 | +14.1% | +0.1103 to +0.1492 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01016 | +0.0102 (native is 0) | +0.008942 to +0.01138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9225 | 1.062 | +15.2% | +0.1195 to +0.1603 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 683.8 | 604.6 | -11.6% | -88.94 to -69.39 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.965 | 10.3 | +15.0% | +0.8017 to +1.879 | yes: power given |
| pods started | 4.5 | 7.5 | +66.7% | +1.569 to +4.431 | yes: power given |
| pod start wait, total (s) | 7.1 | 12.2 | +71.8% | +2.25 to +7.95 | yes: LOSS |
| pod start wait, mean (s) | 1.58 | 1.594 | +0.9% | -0.191 to +0.2196 | no |
| host CPU busy, the real machine under kind (%) | 27.28 | 32.53 | +19.2% | +4.619 to +5.873 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*