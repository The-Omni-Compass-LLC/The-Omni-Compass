# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.999 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1439 | 1435 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1439 | 1435 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 631.8 | 426.2 |
| response time (ms), 95th percentile | 2310 | 1536 |
| response time (ms), 99th percentile | 7094 | 6562 |
| time over the response line (% of samples) | 47.25 | 33.21 |
| failed requests (%) | 28.75 | 24.96 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 118.3 | 102.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 63.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.928 | 2.783 |
| utilisation (used / allocatable) | 0.137 | 0.1342 |
| CPU used (cores), mean | 3.289 | 3.22 |
| Omni's own CPU (cores), mean | 0 | 0.03553 |
| CPU used with Omni's own (cores), mean | 3.289 | 3.255 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 218.6 | 222.5 |
| HPA replicas, mean | 9.94 | 15.85 |
| pods started | 5 | 8.667 |
| pod start wait, total (s) | 6.667 | 13.67 |
| pod start wait, mean (s) | 1.333 | 1.567 |
| host CPU busy, the real machine under kind (%) | 92.02 | 92.19 |
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
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.005399 to +0.003363 | no |
| node-hours | 12.01 | 12.02 | +0.0% | -0.03939 to +0.04642 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1439 | 1435 | -0.3% | -11.88 to +3.798 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1439 | 1435 | -0.3% | -12.54 to +4.143 | no |
| response time (ms), mean | 631.8 | 426.2 | -32.5% | -409.9 to -1.237 | yes: GAIN |
| response time (ms), 95th percentile | 2310 | 1536 | -33.5% | -2859 to +1312 | no |
| response time (ms), 99th percentile | 7094 | 6562 | -7.5% | -5865 to +4802 | no |
| time over the response line (% of samples) | 47.25 | 33.21 | -29.7% | -16.86 to -11.22 | yes: GAIN |
| failed requests (%) | 28.75 | 24.96 | -13.2% | -5.134 to -2.447 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 118.3 | 102.3 | -13.5% | -20.3 to -11.7 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113 (native is 0) | +95.61 to +130.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.928 | 2.783 | +44.4% | -2.321 to +4.032 | no |
| utilisation (used / allocatable) | 0.137 | 0.1342 | -2.1% | -0.004651 to -0.001036 | yes, down (shown, not judged) |
| CPU used (cores), mean | 3.289 | 3.22 | -2.1% | -0.1134 to -0.02416 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03553 | +0.0355 (native is 0) | +0.03345 to +0.03762 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.289 | 3.255 | -1.0% | -0.07712 to +0.01061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 218.6 | 222.5 | +1.8% | +1.356 to +6.505 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.94 | 15.85 | +59.5% | +5.893 to +5.934 | yes: power given |
| pods started | 5 | 8.667 | +73.3% | +0.798 to +6.535 | yes: power given |
| pod start wait, total (s) | 6.667 | 13.67 | +105.0% | -0.453 to +14.45 | no |
| pod start wait, mean (s) | 1.333 | 1.567 | +17.5% | -0.5256 to +0.9923 | no |
| host CPU busy, the real machine under kind (%) | 92.02 | 92.19 | +0.2% | -1.298 to +1.622 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.033 | 480 | 100.0% | 0 | 1.02 | yes |
| omni | 2 | long |  |  |  | 0 | 1.026 | 480 | 100.0% | 0 | 0.98 | yes |
| omni | 3 | long |  |  |  | 0 | 1.037 | 480 | 100.0% | 0 | 1.02 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*