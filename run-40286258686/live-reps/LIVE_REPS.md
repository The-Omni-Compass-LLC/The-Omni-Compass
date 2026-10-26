# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1367 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1367 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 348.9 | 209.8 |
| response time (ms), 95th percentile | 1083 | 642.6 |
| response time (ms), 99th percentile | 3394 | 3016 |
| time over the response line (% of samples) | 21.79 | 12.96 |
| failed requests (%) | 10.52 | 9.193 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 69 | 49.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 176.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 57.58 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.222 | 1.689 |
| utilisation (used / allocatable) | 0.09851 | 0.0966 |
| CPU used (cores), mean | 2.364 | 2.318 |
| Omni's own CPU (cores), mean | 0 | 0.0094 |
| CPU used with Omni's own (cores), mean | 2.364 | 2.328 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 320.8 | 329.2 |
| HPA replicas, mean | 9.896 | 13.33 |
| pods started | 6.333 | 20.67 |
| pod start wait, total (s) | 8.333 | 35.33 |
| pod start wait, mean (s) | 1.38 | 1.732 |
| host CPU busy, the real machine under kind (%) | 66.63 | 66.16 |
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
| node-hours | 12.01 | 12.01 | +0.0% | −0.0308 to +0.0319 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1367 | −0.2% | −7.1920 to +0.5962 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1367 | −0.2% | −7.1920 to +0.5962 | no |
| response time (ms), mean | 348.9 | 209.8 | −39.9% | −364.9137 to +86.6362 | no |
| response time (ms), 95th percentile | 1083 | 642.6 | −40.7% | −983.9560 to +103.4326 | no |
| response time (ms), 99th percentile | 3394 | 3016 | −11.1% | −781.8333 to +25.2893 | no |
| time over the response line (% of samples) | 21.79 | 12.96 | −40.5% | −25.9803 to +8.3271 | no |
| failed requests (%) | 10.52 | 9.193 | −12.6% | −5.7738 to +3.1181 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 69 | 49.67 | −28.0% | −50.7907 to +12.1241 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 176.3 | +176.333 (native is 0) | −6.4021 to +359.0688 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.222 | 1.689 | −24.0% | −4.6220 to +3.5554 | no |
| utilisation (used / allocatable) | 0.09851 | 0.0966 | −1.9% | −0.0037 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.364 | 2.318 | −1.9% | −0.0893 to −0.0022 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0094 | +0.009 (native is 0) | +0.0055 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.364 | 2.328 | −1.5% | −0.0837 to +0.0111 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 320.8 | 329.2 | +2.6% | −13.5438 to +30.4388 | no |
| HPA replicas, mean | 9.896 | 13.33 | +34.7% | −4.0607 to +10.9203 | no |
| pods started | 6.333 | 20.67 | +226.3% | −11.7621 to +40.4287 | no |
| pod start wait, total (s) | 8.333 | 35.33 | +324.0% | −20.3982 to +74.3982 | no |
| pod start wait, mean (s) | 1.38 | 1.732 | +25.6% | −0.4491 to +1.1546 | no |
| host CPU busy, the real machine under kind (%) | 66.63 | 66.16 | −0.7% | −2.1036 to +1.1814 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.021 | 120 | 100.0% | 0 | 1.03 | yes |
| omni | 2 | long |  |  |  | 0 | 1.039 | 120 | 100.0% | 0 | 1.12 | yes |
| omni | 3 | long |  |  |  | 0 | 1.016 | 120 | 100.0% | 0 | 1.03 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*