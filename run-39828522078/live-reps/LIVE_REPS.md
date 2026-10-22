# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.507 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.8 | 171.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.8 | 171.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 292.8 | 185.5 |
| response time (ms), 95th percentile | 802.7 | 577.1 |
| response time (ms), 99th percentile | 2398 | 2013 |
| time over the response line (% of samples) | 16.72 | 11.04 |
| failed requests (%) | 6.401 | 6.05 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 6.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 81.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.155 | 0.3567 |
| utilisation (used / allocatable) | 0.09383 | 0.09338 |
| CPU used (cores), mean | 2.252 | 2.241 |
| Omni's own CPU (cores), mean | 0 | 0.03161 |
| CPU used with Omni's own (cores), mean | 2.252 | 2.273 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 321.5 | 321 |
| HPA replicas, mean | 9.355 | 11.34 |
| pods started | 5.6 | 14.8 |
| pod start wait, total (s) | 7.5 | 23.9 |
| pod start wait, mean (s) | 1.314 | 1.63 |
| host CPU busy, the real machine under kind (%) | 64.25 | 65.32 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 29.61 | 29.39 |
| robust: time over the line in the 300 s after the kill (% of samples) | 50.11 | 51.88 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 1.507 | 1.514 | +0.5% | +0.004354 to +0.009979 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 170.8 | 171.5 | +0.4% | +0.3301 to +1.119 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.8 | 171.5 | +0.4% | +0.3301 to +1.119 | yes: power given |
| response time (ms), mean | 292.8 | 185.5 | -36.7% | -153.7 to -61.04 | yes: GAIN |
| response time (ms), 95th percentile | 802.7 | 577.1 | -28.1% | -436.1 to -15.03 | yes: GAIN |
| response time (ms), 99th percentile | 2398 | 2013 | -16.0% | -1066 to +297.8 | no |
| time over the response line (% of samples) | 16.72 | 11.04 | -34.0% | -8.648 to -2.724 | yes: GAIN |
| failed requests (%) | 6.401 | 6.05 | -5.5% | -0.6881 to -0.01313 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 6.6 | -21.4% | -3.14 to -0.4597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.6 | +83.6 (native is 0) | +73.71 to +93.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.155 | 0.3567 | +130.1% | -0.1915 to +0.5949 | no |
| utilisation (used / allocatable) | 0.09383 | 0.09338 | -0.5% | -0.001516 to +0.0006211 | no |
| CPU used (cores), mean | 2.252 | 2.241 | -0.5% | -0.03639 to +0.01491 | no |
| Omni's own CPU (cores), mean | 0 | 0.03161 | +0.0316 (native is 0) | +0.02925 to +0.03397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.252 | 2.273 | +0.9% | -0.003198 to +0.04493 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 321.5 | 321 | -0.2% | -5.744 to +4.681 | no |
| HPA replicas, mean | 9.355 | 11.34 | +21.3% | +1.758 to +2.221 | yes: power given |
| pods started | 5.6 | 14.8 | +164.3% | +6.507 to +11.89 | yes: power given |
| pod start wait, total (s) | 7.5 | 23.9 | +218.7% | +10.72 to +22.08 | yes: LOSS |
| pod start wait, mean (s) | 1.314 | 1.63 | +24.1% | -0.0282 to +0.6605 | no |
| host CPU busy, the real machine under kind (%) | 64.25 | 65.32 | +1.7% | +0.2823 to +1.863 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 300 s after the kill (%) | 29.61 | 29.39 | -0.8% | -3.826 to +3.378 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 50.11 | 51.88 | +3.5% | -3.988 to +7.522 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 3 | kill | 11 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 5 | kill | 9 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 55 |  |  |  |  |
| omni | 10 | kill | 9 | yes | yes | 1 |  | 55 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*