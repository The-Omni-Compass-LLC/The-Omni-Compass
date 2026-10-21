# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 175.9 | 175.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.9 | 175.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 445.3 | 258.6 |
| response time (ms), 95th percentile | 1304 | 803.1 |
| response time (ms), 99th percentile | 4844 | 3148 |
| time over the response line (% of samples) | 28.32 | 18.36 |
| failed requests (%) | 13.66 | 12.56 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2283 |
| utilisation (used / allocatable) | 0.1118 | 0.1104 |
| CPU used (cores), mean | 2.684 | 2.649 |
| Omni's own CPU (cores), mean | 0 | 0.01353 |
| CPU used with Omni's own (cores), mean | 2.684 | 2.662 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 275.8 |
| HPA replicas, mean | 9.414 | 9.766 |
| pods started | 5.5 | 5.8 |
| pod start wait, total (s) | 9.5 | 8.7 |
| pod start wait, mean (s) | 1.732 | 1.751 |
| host CPU busy, the real machine under kind (%) | 76.34 | 76.1 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 47.46 | 50.31 |
| robust: time over the line in the 120 s after the kill (% of samples) | 72.08 | 71.69 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.933e-16 to +5.15e-18 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.515 | -0.1% | -0.007746 to +0.005413 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 175.9 | 175.5 | -0.3% | -1.152 to +0.2554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.9 | 175.5 | -0.3% | -1.152 to +0.2554 | no |
| response time (ms), mean | 445.3 | 258.6 | -41.9% | -262.8 to -110.4 | yes: GAIN |
| response time (ms), 95th percentile | 1304 | 803.1 | -38.4% | -803 to -198.1 | yes: GAIN |
| response time (ms), 99th percentile | 4844 | 3148 | -35.0% | -3276 to -115.6 | yes: GAIN |
| time over the response line (% of samples) | 28.32 | 18.36 | -35.2% | -13.19 to -6.721 | yes: GAIN |
| failed requests (%) | 13.66 | 12.56 | -8.0% | -1.893 to -0.3039 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 9.2 | -23.3% | -3.457 to -2.143 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 | +47.6 (native is 0) | +37.85 to +57.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2283 | +179.6% | -0.03263 to +0.326 | no |
| utilisation (used / allocatable) | 0.1118 | 0.1104 | -1.3% | -0.002574 to -0.0003894 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.684 | 2.649 | -1.3% | -0.06177 to -0.009345 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01353 | +0.0135 (native is 0) | +0.01179 to +0.01527 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.684 | 2.662 | -0.8% | -0.04809 to +0.004044 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 275.8 | +0.8% | -0.008743 to +4.171 | no |
| HPA replicas, mean | 9.414 | 9.766 | +3.7% | +0.1527 to +0.5517 | yes: power given |
| pods started | 5.5 | 5.8 | +5.5% | -2.66 to +3.26 | no |
| pod start wait, total (s) | 9.5 | 8.7 | -8.4% | -5.637 to +4.037 | no |
| pod start wait, mean (s) | 1.732 | 1.751 | +1.1% | -0.5768 to +0.6144 | no |
| host CPU busy, the real machine under kind (%) | 76.34 | 76.1 | -0.3% | -0.7253 to +0.2499 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 47.46 | 50.31 | +6.0% | -7.742 to +13.44 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 72.08 | 71.69 | -0.5% | -3.517 to +2.743 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 12 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*