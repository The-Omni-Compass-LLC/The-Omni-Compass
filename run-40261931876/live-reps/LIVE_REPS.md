# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 175.6 | 175.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.6 | 175.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 425.7 | 257.5 |
| response time (ms), 95th percentile | 1428 | 738.3 |
| response time (ms), 99th percentile | 4216 | 3471 |
| time over the response line (% of samples) | 31.08 | 20.46 |
| failed requests (%) | 16.85 | 15.26 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.2167 |
| utilisation (used / allocatable) | 0.1114 | 0.1093 |
| CPU used (cores), mean | 2.673 | 2.622 |
| Omni's own CPU (cores), mean | 0 | 0.01278 |
| CPU used with Omni's own (cores), mean | 2.673 | 2.635 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.4 | 287.7 |
| HPA replicas, mean | 9.442 | 10.13 |
| pods started | 5.1 | 5.8 |
| pod start wait, total (s) | 8.2 | 10.2 |
| pod start wait, mean (s) | 1.64 | 1.625 |
| host CPU busy, the real machine under kind (%) | 76.8 | 76.35 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 66.42 | 63.55 |
| robust: time over the line in the 300 s after the kill (% of samples) | 75.83 | 73.85 |

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
| node-hours | 1.514 | 1.515 | +0.1% | −0.0026 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 175.6 | 175.3 | −0.2% | −0.8268 to +0.1493 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.6 | 175.3 | −0.2% | −0.8268 to +0.1493 | no |
| response time (ms), mean | 425.7 | 257.5 | −39.5% | −267.5946 to −68.8560 | yes: GAIN |
| response time (ms), 95th percentile | 1428 | 738.3 | −48.3% | −1242.0906 to −136.9144 | yes: GAIN |
| response time (ms), 99th percentile | 4216 | 3471 | −17.7% | −2536.6877 to +1047.4625 | no |
| time over the response line (% of samples) | 31.08 | 20.46 | −34.2% | −14.6269 to −6.6053 | yes: GAIN |
| failed requests (%) | 16.85 | 15.26 | −9.4% | −2.6434 to −0.5374 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 9.1 | −19.5% | −2.8573 to −1.5427 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48.000 (native is 0) | +37.5959 to +58.4041 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.2167 | +103.1% | −0.0873 to +0.3073 | no |
| utilisation (used / allocatable) | 0.1114 | 0.1093 | −1.9% | −0.0030 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.673 | 2.622 | −1.9% | −0.0721 to −0.0283 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01278 | +0.013 (native is 0) | +0.0115 to +0.0140 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.673 | 2.635 | −1.4% | −0.0587 to −0.0161 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.4 | 287.7 | +1.5% | +1.2912 to +7.2121 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.442 | 10.13 | +7.3% | +0.2223 to +1.1515 | yes: power given |
| pods started | 5.1 | 5.8 | +13.7% | −2.6047 to +4.0047 | no |
| pod start wait, total (s) | 8.2 | 10.2 | +24.4% | −5.1769 to +9.1769 | no |
| pod start wait, mean (s) | 1.64 | 1.625 | −1.0% | −0.4111 to +0.3796 | no |
| host CPU busy, the real machine under kind (%) | 76.8 | 76.35 | −0.6% | −0.9663 to +0.0601 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 66.42 | 63.55 | −4.3% | −9.6774 to +3.9406 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 75.83 | 73.85 | −2.6% | −4.8699 to +0.9050 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 6 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*