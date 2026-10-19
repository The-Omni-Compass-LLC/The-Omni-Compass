# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1438 | 1436 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1438 | 1436 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 618.5 | 404.5 |
| response time (ms), 95th percentile | 2268 | 1509 |
| response time (ms), 99th percentile | 7192 | 6604 |
| time over the response line (% of samples) | 46.53 | 31.8 |
| failed requests (%) | 27.89 | 23.91 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 117.7 | 101.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 11.11 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.706 | 2.061 |
| utilisation (used / allocatable) | 0.1363 | 0.1345 |
| CPU used (cores), mean | 3.272 | 3.229 |
| Omni's own CPU (cores), mean | 0 | 0.01073 |
| CPU used with Omni's own (cores), mean | 3.272 | 3.239 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 219.5 | 222 |
| HPA replicas, mean | 9.939 | 15.08 |
| pods started | 5 | 9 |
| pod start wait, total (s) | 7 | 16.67 |
| pod start wait, mean (s) | 1.4 | 1.855 |
| host CPU busy, the real machine under kind (%) | 91.58 | 91.33 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.882e-16 to +8.882e-16 | EVEN, the same (under one part in a million) |
| node-hours | 12.02 | 12.02 | +0.0% | -0.03633 to +0.04744 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1438 | 1436 | -0.2% | -9.054 to +4.408 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1438 | 1436 | -0.2% | -9.054 to +4.408 | no |
| response time (ms), mean | 618.5 | 404.5 | -34.6% | -264.5 to -163.3 | yes: GAIN |
| response time (ms), 95th percentile | 2268 | 1509 | -33.5% | -1750 to +231.8 | no |
| response time (ms), 99th percentile | 7192 | 6604 | -8.2% | -2488 to +1312 | no |
| time over the response line (% of samples) | 46.53 | 31.8 | -31.7% | -17.63 to -11.83 | yes: GAIN |
| failed requests (%) | 27.89 | 23.91 | -14.3% | -6.787 to -1.177 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 117.7 | 101.7 | -13.6% | -16 to -16 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107 | +107 (native is 0) | +86.66 to +127.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.706 | 2.061 | -23.8% | -2.08 to +0.7913 | no |
| utilisation (used / allocatable) | 0.1363 | 0.1345 | -1.3% | -0.003009 to -0.0005866 | yes, down (shown, not judged) |
| CPU used (cores), mean | 3.272 | 3.229 | -1.3% | -0.07221 to -0.01408 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01073 | +0.0107 (native is 0) | +0.01059 to +0.01088 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.272 | 3.239 | -1.0% | -0.0616 to -0.003222 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 219.5 | 222 | +1.1% | +0.8202 to +4.117 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.939 | 15.08 | +51.7% | +5.082 to +5.198 | yes: power given |
| pods started | 5 | 9 | +80.0% | +1.516 to +6.484 | yes: power given |
| pod start wait, total (s) | 7 | 16.67 | +138.1% | +4.495 to +14.84 | yes: LOSS |
| pod start wait, mean (s) | 1.4 | 1.855 | +32.5% | -0.3378 to +1.247 | no |
| host CPU busy, the real machine under kind (%) | 91.58 | 91.33 | -0.3% | -1.331 to +0.8128 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.014 | 117 | 97.5% | 0 | 0.85 | yes |
| omni | 2 | long |  |  |  | 0 | 1.023 | 117 | 97.5% | 0 | 0.76 | yes |
| omni | 3 | long |  |  |  | 0 | 1.014 | 117 | 97.5% | 0 | 0.94 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*