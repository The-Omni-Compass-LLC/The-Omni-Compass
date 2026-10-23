# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 176.1 | 175.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.1 | 175.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 412.1 | 255.4 |
| response time (ms), 95th percentile | 1208 | 667 |
| response time (ms), 99th percentile | 4037 | 3669 |
| time over the response line (% of samples) | 28.64 | 18.99 |
| failed requests (%) | 14.28 | 13.59 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.05333 |
| utilisation (used / allocatable) | 0.1135 | 0.1123 |
| CPU used (cores), mean | 2.724 | 2.695 |
| Omni's own CPU (cores), mean | 0 | 0.01355 |
| CPU used with Omni's own (cores), mean | 2.724 | 2.708 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 264.1 | 266.7 |
| HPA replicas, mean | 9.432 | 9.961 |
| pods started | 5.6 | 6.7 |
| pod start wait, total (s) | 9.4 | 11.6 |
| pod start wait, mean (s) | 1.67 | 1.527 |
| host CPU busy, the real machine under kind (%) | 77.55 | 77.43 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 58.94 | 61.98 |
| robust: time over the line in the 300 s after the kill (% of samples) | 77.01 | 75.38 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.788e-16 to +3.235e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.515 | +0.1% | -0.004325 to +0.005992 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 176.1 | 175.9 | -0.1% | -0.7601 to +0.4829 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.1 | 175.9 | -0.1% | -0.7601 to +0.4829 | no |
| response time (ms), mean | 412.1 | 255.4 | -38.0% | -222.5 to -90.9 | yes: GAIN |
| response time (ms), 95th percentile | 1208 | 667 | -44.8% | -887 to -195.2 | yes: GAIN |
| response time (ms), 99th percentile | 4037 | 3669 | -9.1% | -1921 to +1185 | no |
| time over the response line (% of samples) | 28.64 | 18.99 | -33.7% | -12.61 to -6.675 | yes: GAIN |
| failed requests (%) | 14.28 | 13.59 | -4.8% | -1.598 to +0.2238 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 9.6 | -20.7% | -3.273 to -1.727 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 | +48.4 (native is 0) | +37.29 to +59.51 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.05333 | -60.0% | -0.207 to +0.04702 | no |
| utilisation (used / allocatable) | 0.1135 | 0.1123 | -1.1% | -0.002287 to -0.0001113 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.724 | 2.695 | -1.1% | -0.05488 to -0.002671 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01355 | +0.0135 (native is 0) | +0.01223 to +0.01487 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.724 | 2.708 | -0.6% | -0.04215 to +0.0117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 264.1 | 266.7 | +1.0% | -0.5114 to +5.629 | no |
| HPA replicas, mean | 9.432 | 9.961 | +5.6% | +0.1876 to +0.8711 | yes: power given |
| pods started | 5.6 | 6.7 | +19.6% | -2.089 to +4.289 | no |
| pod start wait, total (s) | 9.4 | 11.6 | +23.4% | -3.792 to +8.192 | no |
| pod start wait, mean (s) | 1.67 | 1.527 | -8.6% | -0.6874 to +0.4011 | no |
| host CPU busy, the real machine under kind (%) | 77.55 | 77.43 | -0.2% | -0.6053 to +0.3585 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 300 s after the kill (%) | 58.94 | 61.98 | +5.2% | -1.096 to +7.184 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 77.01 | 75.38 | -2.1% | -6.545 to +3.281 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*