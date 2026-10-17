# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1387 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1387 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 432.6 | 258.6 |
| response time (ms), 95th percentile | 1684 | 937 |
| response time (ms), 99th percentile | 4976 | 4077 |
| time over the response line (% of samples) | 30.04 | 19.9 |
| failed requests (%) | 18.06 | 14.95 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 82.67 | 66.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.717 | 1.978 |
| utilisation (used / allocatable) | 0.1107 | 0.1077 |
| CPU used (cores), mean | 2.658 | 2.584 |
| Omni's own CPU (cores), mean | 0 | 0.009233 |
| CPU used with Omni's own (cores), mean | 2.658 | 2.593 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.6 | 305.7 |
| HPA replicas, mean | 9.913 | 13.19 |
| pods started | 6 | 11 |
| pod start wait, total (s) | 20.33 | 22.33 |
| pod start wait, mean (s) | 2.833 | 1.93 |
| host CPU busy, the real machine under kind (%) | 74.36 | 73.22 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.866e-15 to +6.818e-16 | EVEN, the same (under one part in a million) |
| node-hours | 12.02 | 12.02 | -0.0% | -0.0361 to +0.0361 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1387 | -0.4% | -13.31 to +2.217 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1387 | -0.4% | -13.31 to +2.217 | no |
| response time (ms), mean | 432.6 | 258.6 | -40.2% | -472.8 to +124.8 | no |
| response time (ms), 95th percentile | 1684 | 937 | -44.3% | -2165 to +672.4 | no |
| response time (ms), 99th percentile | 4976 | 4077 | -18.1% | -2353 to +555.9 | no |
| time over the response line (% of samples) | 30.04 | 19.9 | -33.8% | -32.02 to +11.73 | no |
| failed requests (%) | 18.06 | 14.95 | -17.3% | -10.82 to +4.585 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 82.67 | 66.33 | -19.8% | -19.2 to -13.46 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102 | +102 (native is 0) | +89.58 to +114.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.717 | 1.978 | -27.2% | -2.257 to +0.7793 | no |
| utilisation (used / allocatable) | 0.1107 | 0.1077 | -2.8% | -0.005193 to -0.0009565 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.658 | 2.584 | -2.8% | -0.1246 to -0.02296 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.009233 | +0.00923 (native is 0) | +0.004207 to +0.01426 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.658 | 2.593 | -2.4% | -0.1127 to -0.01642 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.6 | 305.7 | +3.1% | -10.78 to +29.05 | no |
| HPA replicas, mean | 9.913 | 13.19 | +33.1% | -4.797 to +11.36 | no |
| pods started | 6 | 11 | +83.3% | +0.697 to +9.303 | yes: power given |
| pod start wait, total (s) | 20.33 | 22.33 | +9.8% | -18.34 to +22.34 | no |
| pod start wait, mean (s) | 2.833 | 1.93 | -31.9% | -3.532 to +1.724 | no |
| host CPU busy, the real machine under kind (%) | 74.36 | 73.22 | -1.5% | -2.125 to -0.1653 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.018 | 117 | 97.5% | 0 | 1.17 | yes |
| omni | 2 | long |  |  |  | 0 | 1.043 | 120 | 100.0% | 0 | 1.14 | yes |
| omni | 3 | long |  |  |  | 0 | 1.028 | 118 | 98.3% | 0 | 0.77 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*