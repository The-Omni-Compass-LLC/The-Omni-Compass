# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1416 | 1412 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1416 | 1412 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 541.4 | 331 |
| response time (ms), 95th percentile | 1965 | 1145 |
| response time (ms), 99th percentile | 5890 | 5502 |
| time over the response line (% of samples) | 36.53 | 23.28 |
| failed requests (%) | 19.02 | 16.61 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 106 | 83 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 126 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 9.091 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.333 | 2.167 |
| utilisation (used / allocatable) | 0.1239 | 0.1223 |
| CPU used (cores), mean | 2.974 | 2.934 |
| Omni's own CPU (cores), mean | 0 | 0.01147 |
| CPU used with Omni's own (cores), mean | 2.974 | 2.946 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 242.1 | 245.4 |
| HPA replicas, mean | 9.932 | 15.14 |
| pods started | 5.333 | 13.33 |
| pod start wait, total (s) | 9.667 | 28 |
| pod start wait, mean (s) | 1.8 | 2.051 |
| host CPU busy, the real machine under kind (%) | 83.26 | 83.1 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 12.02 | 12.01 | −0.1% | −0.0436 to +0.0191 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1416 | 1412 | −0.3% | −13.5351 to +5.1143 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1416 | 1412 | −0.3% | −13.5351 to +5.1143 | no |
| response time (ms), mean | 541.4 | 331 | −38.9% | −390.5307 to −30.3295 | yes: GAIN |
| response time (ms), 95th percentile | 1965 | 1145 | −41.7% | −1493.3321 to −146.3312 | yes: GAIN |
| response time (ms), 99th percentile | 5890 | 5502 | −6.6% | −2183.6825 to +1409.0391 | no |
| time over the response line (% of samples) | 36.53 | 23.28 | −36.3% | −20.4090 to −6.0854 | yes: GAIN |
| failed requests (%) | 19.02 | 16.61 | −12.7% | −6.4472 to +1.6197 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 106 | 83 | −21.7% | −44.6580 to −1.3420 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 126 | +126.000 (native is 0) | +75.5734 to +176.4266 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.333 | 2.167 | −7.1% | −3.0410 to +2.7077 | no |
| utilisation (used / allocatable) | 0.1239 | 0.1223 | −1.3% | −0.0056 to +0.0023 | no |
| CPU used (cores), mean | 2.974 | 2.934 | −1.3% | −0.1343 to +0.0552 | no |
| Omni's own CPU (cores), mean | 0 | 0.01147 | +0.011 (native is 0) | +0.0089 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.974 | 2.946 | −0.9% | −0.1243 to +0.0682 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 242.1 | 245.4 | +1.3% | −4.8447 to +11.3619 | no |
| HPA replicas, mean | 9.932 | 15.14 | +52.5% | +5.0194 to +5.4048 | yes: power given |
| pods started | 5.333 | 13.33 | +150.0% | −17.8180 to +33.8180 | no |
| pod start wait, total (s) | 9.667 | 28 | +189.7% | −36.9025 to +73.5691 | no |
| pod start wait, mean (s) | 1.8 | 2.051 | +14.0% | −0.0738 to +0.5763 | no |
| host CPU busy, the real machine under kind (%) | 83.26 | 83.1 | −0.2% | −2.4475 to +2.1228 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.023 | 120 | 100.0% | 0 | 1.14 | yes |
| omni | 2 | long |  |  |  | 0 | 1.008 | 120 | 100.0% | 0 | 1.07 | yes |
| omni | 3 | long |  |  |  | 0 | 1.023 | 120 | 100.0% | 0 | 1.14 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*