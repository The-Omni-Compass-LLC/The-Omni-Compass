# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1376 | 1371 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1376 | 1371 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 360.8 | 192.5 |
| response time (ms), 95th percentile | 1047 | 480.9 |
| response time (ms), 99th percentile | 3556 | 2204 |
| time over the response line (% of samples) | 18.79 | 7.229 |
| failed requests (%) | 5.039 | 2.627 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 86.67 | 52.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 232.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 21.38 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.311 | 2.689 |
| utilisation (used / allocatable) | 0.1017 | 0.09894 |
| CPU used (cores), mean | 2.442 | 2.375 |
| Omni's own CPU (cores), mean | 0 | 0.0097 |
| CPU used with Omni's own (cores), mean | 2.442 | 2.384 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.6 | 288.3 |
| HPA replicas, mean | 9.932 | 14.85 |
| pods started | 5.333 | 21.33 |
| pod start wait, total (s) | 19.33 | 50.67 |
| pod start wait, mean (s) | 3.533 | 2.28 |
| host CPU busy, the real machine under kind (%) | 68.1 | 66.74 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.844e-15 to +2.252e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.02 | 12.01 | -0.0% | -0.03744 to +0.03299 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1376 | 1371 | -0.4% | -27.18 to +16.63 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1376 | 1371 | -0.4% | -27.18 to +16.63 | no |
| response time (ms), mean | 360.8 | 192.5 | -46.7% | -323.3 to -13.34 | yes: GAIN |
| response time (ms), 95th percentile | 1047 | 480.9 | -54.1% | -1299 to +165.7 | no |
| response time (ms), 99th percentile | 3556 | 2204 | -38.0% | -4358 to +1655 | no |
| time over the response line (% of samples) | 18.79 | 7.229 | -61.5% | -26.7 to +3.581 | no |
| failed requests (%) | 5.039 | 2.627 | -47.9% | -11.6 to +6.775 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 86.67 | 52.33 | -39.6% | -87.05 to +18.39 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 232.7 | +233 (native is 0) | +142.7 to +322.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.311 | 2.689 | +16.3% | -9.522 to +10.28 | no |
| utilisation (used / allocatable) | 0.1017 | 0.09894 | -2.7% | -0.01424 to +0.008663 | no |
| CPU used (cores), mean | 2.442 | 2.375 | -2.7% | -0.3419 to +0.2079 | no |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.008562 to +0.01084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.442 | 2.384 | -2.3% | -0.3312 to +0.2167 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.6 | 288.3 | +2.4% | -20.6 to +33.98 | no |
| HPA replicas, mean | 9.932 | 14.85 | +49.5% | +4.745 to +5.089 | yes: power given |
| pods started | 5.333 | 21.33 | +300.0% | +2.854 to +29.15 | yes: power given |
| pod start wait, total (s) | 19.33 | 50.67 | +162.1% | -53.33 to +116 | no |
| pod start wait, mean (s) | 3.533 | 2.28 | -35.5% | -6.265 to +3.758 | no |
| host CPU busy, the real machine under kind (%) | 68.1 | 66.74 | -2.0% | -8.634 to +5.906 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.023 | 119 | 99.2% | 0 | 0.69 | yes |
| omni | 2 | long |  |  |  | 0 | 1.035 | 119 | 99.2% | 0 | 0.75 | yes |
| omni | 3 | long |  |  |  | 0 | 1.036 | 119 | 99.2% | 0 | 0.80 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*