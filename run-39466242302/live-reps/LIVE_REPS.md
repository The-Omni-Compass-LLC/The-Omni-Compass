# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.3 | 170.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.3 | 170.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 290.5 | 170.7 |
| response time (ms), 95th percentile | 867.9 | 459.2 |
| response time (ms), 99th percentile | 2958 | 2257 |
| time over the response line (% of samples) | 17.27 | 11.75 |
| failed requests (%) | 9.307 | 8.705 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.3733 |
| utilisation (used / allocatable) | 0.0886 | 0.08634 |
| CPU used (cores), mean | 2.126 | 2.072 |
| Omni's own CPU (cores), mean | 0 | 0.0117 |
| CPU used with Omni's own (cores), mean | 2.126 | 2.084 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 357.1 | 368.3 |
| HPA replicas, mean | 9.204 | 9.414 |
| pods started | 6 | 5.7 |
| pod start wait, total (s) | 8.7 | 9.4 |
| pod start wait, mean (s) | 1.448 | 1.566 |
| host CPU busy, the real machine under kind (%) | 61.38 | 60.47 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 32.02 | 33.17 |
| robust: time over the line in the 120 s after the kill (% of samples) | 43.51 | 40.8 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.516 | +0.2% | -0.001909 to +0.008575 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170.3 | 170.1 | -0.1% | -0.6709 to +0.3211 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.3 | 170.1 | -0.1% | -0.6709 to +0.3211 | no |
| response time (ms), mean | 290.5 | 170.7 | -41.2% | -187.4 to -52.29 | yes: GAIN |
| response time (ms), 95th percentile | 867.9 | 459.2 | -47.1% | -662.7 to -154.6 | yes: GAIN |
| response time (ms), 99th percentile | 2958 | 2257 | -23.7% | -1618 to +216.6 | no |
| time over the response line (% of samples) | 17.27 | 11.75 | -31.9% | -9.338 to -1.685 | yes: GAIN |
| failed requests (%) | 9.307 | 8.705 | -6.5% | -1.222 to +0.01935 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.1 | -26.1% | -2.457 to -1.143 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 | +44.5 (native is 0) | +39.01 to +49.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.3733 | +28.0% | -0.07674 to +0.2401 | no |
| utilisation (used / allocatable) | 0.0886 | 0.08634 | -2.6% | -0.004099 to -0.0004272 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.126 | 2.072 | -2.6% | -0.09837 to -0.01025 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0117 | +0.0117 (native is 0) | +0.009523 to +0.01388 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.126 | 2.084 | -2.0% | -0.08635 to +0.001126 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 357.1 | 368.3 | +3.1% | +1.358 to +21.08 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.204 | 9.414 | +2.3% | -0.1396 to +0.5578 | no |
| pods started | 6 | 5.7 | -5.0% | -2.268 to +1.668 | no |
| pod start wait, total (s) | 8.7 | 9.4 | +8.0% | -2.933 to +4.333 | no |
| pod start wait, mean (s) | 1.448 | 1.566 | +8.2% | -0.1627 to +0.3999 | no |
| host CPU busy, the real machine under kind (%) | 61.38 | 60.47 | -1.5% | -2.132 to +0.316 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 32.02 | 33.17 | +3.6% | -3.289 to +5.578 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 43.51 | 40.8 | -6.2% | -5.667 to +0.2533 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 12 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*