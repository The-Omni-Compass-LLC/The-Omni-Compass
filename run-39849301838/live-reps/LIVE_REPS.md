# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.8 | 174.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.8 | 174.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 394.7 | 239.7 |
| response time (ms), 95th percentile | 1192 | 712.8 |
| response time (ms), 99th percentile | 4115 | 3269 |
| time over the response line (% of samples) | 26.78 | 19.79 |
| failed requests (%) | 15.74 | 14.83 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.16 |
| utilisation (used / allocatable) | 0.1083 | 0.107 |
| CPU used (cores), mean | 2.6 | 2.568 |
| Omni's own CPU (cores), mean | 0 | 0.03342 |
| CPU used with Omni's own (cores), mean | 2.6 | 2.601 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.6 | 293.2 |
| HPA replicas, mean | 9.371 | 11.37 |
| pods started | 5.6 | 11.9 |
| pod start wait, total (s) | 9 | 20.6 |
| pod start wait, mean (s) | 1.616 | 1.797 |
| host CPU busy, the real machine under kind (%) | 74.63 | 75.4 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 63.14 | 66.94 |
| robust: time over the line in the 300 s after the kill (% of samples) | 72.39 | 70.89 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.515 | +0.2% | -0.004868 to +0.009535 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.8 | 174.8 | +0.0% | -0.6105 to +0.6301 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.8 | 174.8 | +0.0% | -0.6105 to +0.6301 | no |
| response time (ms), mean | 394.7 | 239.7 | -39.3% | -220.3 to -89.85 | yes: GAIN |
| response time (ms), 95th percentile | 1192 | 712.8 | -40.2% | -945.2 to -13.14 | yes: GAIN |
| response time (ms), 99th percentile | 4115 | 3269 | -20.6% | -2135 to +443.2 | no |
| time over the response line (% of samples) | 26.78 | 19.79 | -26.1% | -10.77 to -3.216 | yes: GAIN |
| failed requests (%) | 15.74 | 14.83 | -5.8% | -1.789 to -0.03942 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 8.8 | -12.9% | -2.129 to -0.4706 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.5 | +78.5 (native is 0) | +71.22 to +85.78 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.16 | +54.8% | -0.09818 to +0.2115 | no |
| utilisation (used / allocatable) | 0.1083 | 0.107 | -1.2% | -0.002772 to +8.839e-05 | no |
| CPU used (cores), mean | 2.6 | 2.568 | -1.2% | -0.06654 to +0.002121 | no |
| Omni's own CPU (cores), mean | 0 | 0.03342 | +0.0334 (native is 0) | +0.02983 to +0.03701 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.6 | 2.601 | +0.0% | -0.03069 to +0.03311 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.6 | 293.2 | +0.2% | -3.996 to +5.239 | no |
| HPA replicas, mean | 9.371 | 11.37 | +21.3% | +1.681 to +2.308 | yes: power given |
| pods started | 5.6 | 11.9 | +112.5% | +3.34 to +9.26 | yes: power given |
| pod start wait, total (s) | 9 | 20.6 | +128.9% | +6.758 to +16.44 | yes: LOSS |
| pod start wait, mean (s) | 1.616 | 1.797 | +11.2% | -0.1166 to +0.4788 | no |
| host CPU busy, the real machine under kind (%) | 74.63 | 75.4 | +1.0% | +0.1351 to +1.409 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 300 s after the kill (%) | 63.14 | 66.94 | +6.0% | -1.11 to +8.707 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 72.39 | 70.89 | -2.1% | -2.886 to -0.1041 | yes: GAIN |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 7 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 3 | kill | 11 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 5 | kill | 7 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 8 | kill | 8 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 9 | kill | 12 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 10 | kill | 12 | yes | yes | 1 |  | 55 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*