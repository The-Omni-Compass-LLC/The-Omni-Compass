# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 176.9 | 176.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.9 | 176.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 415.2 | 267.4 |
| response time (ms), 95th percentile | 1144 | 698.4 |
| response time (ms), 99th percentile | 4251 | 4515 |
| time over the response line (% of samples) | 33.12 | 22.23 |
| failed requests (%) | 19.86 | 17.39 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.11 |
| utilisation (used / allocatable) | 0.117 | 0.1152 |
| CPU used (cores), mean | 2.809 | 2.764 |
| Omni's own CPU (cores), mean | 0 | 0.01302 |
| CPU used with Omni's own (cores), mean | 2.809 | 2.777 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 263.8 | 266.3 |
| HPA replicas, mean | 9.436 | 9.651 |
| pods started | 5.2 | 4.8 |
| pod start wait, total (s) | 6.9 | 7.6 |
| pod start wait, mean (s) | 1.318 | 1.53 |
| host CPU busy, the real machine under kind (%) | 80.67 | 80.19 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 73.88 | 70.92 |
| robust: time over the line in the 300 s after the kill (% of samples) | 82.81 | 82.41 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0058 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 176.9 | 176.5 | −0.2% | −1.1282 to +0.4797 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.9 | 176.5 | −0.2% | −1.1282 to +0.4797 | no |
| response time (ms), mean | 415.2 | 267.4 | −35.6% | −212.0374 to −83.5829 | yes: GAIN |
| response time (ms), 95th percentile | 1144 | 698.4 | −38.9% | −686.9732 to −204.1918 | yes: GAIN |
| response time (ms), 99th percentile | 4251 | 4515 | +6.2% | −1386.7760 to +1913.5602 | no |
| time over the response line (% of samples) | 33.12 | 22.23 | −32.9% | −15.1958 to −6.5736 | yes: GAIN |
| failed requests (%) | 19.86 | 17.39 | −12.4% | −3.4157 to −1.5170 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 10.1 | −17.9% | −2.7642 to −1.6358 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.7 | +42.700 (native is 0) | +36.4636 to +48.9364 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.11 | +112.9% | −0.0979 to +0.2146 | no |
| utilisation (used / allocatable) | 0.117 | 0.1152 | −1.6% | −0.0028 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.809 | 2.764 | −1.6% | −0.0668 to −0.0223 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01302 | +0.013 (native is 0) | +0.0113 to +0.0147 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.809 | 2.777 | −1.1% | −0.0531 to −0.0100 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 263.8 | 266.3 | +1.0% | −0.7483 to +5.7971 | no |
| HPA replicas, mean | 9.436 | 9.651 | +2.3% | −0.0787 to +0.5071 | no |
| pods started | 5.2 | 4.8 | −7.7% | −2.3134 to +1.5134 | no |
| pod start wait, total (s) | 6.9 | 7.6 | +10.1% | −2.5527 to +3.9527 | no |
| pod start wait, mean (s) | 1.318 | 1.53 | +16.1% | −0.1472 to +0.5720 | no |
| host CPU busy, the real machine under kind (%) | 80.67 | 80.19 | −0.6% | −0.8784 to −0.0810 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 73.88 | 70.92 | −4.0% | −10.0755 to +4.1566 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 82.81 | 82.41 | −0.5% | −1.8121 to +1.0061 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*