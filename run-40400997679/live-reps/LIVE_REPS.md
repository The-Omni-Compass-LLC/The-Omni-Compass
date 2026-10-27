# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.5 | 174.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.5 | 174.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 383.1 | 240.3 |
| response time (ms), 95th percentile | 1093 | 620.6 |
| response time (ms), 99th percentile | 4174 | 3460 |
| time over the response line (% of samples) | 26.64 | 17.82 |
| failed requests (%) | 14.43 | 12.73 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.215 |
| utilisation (used / allocatable) | 0.1079 | 0.1064 |
| CPU used (cores), mean | 2.59 | 2.554 |
| Omni's own CPU (cores), mean | 0 | 0.01339 |
| CPU used with Omni's own (cores), mean | 2.59 | 2.567 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 291.5 | 293 |
| HPA replicas, mean | 9.389 | 9.963 |
| pods started | 5.7 | 6.5 |
| pod start wait, total (s) | 9.6 | 9.8 |
| pod start wait, mean (s) | 1.684 | 1.388 |
| host CPU busy, the real machine under kind (%) | 74.05 | 73.8 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 57.22 | 55.9 |
| robust: time over the line in the 300 s after the kill (% of samples) | 71.05 | 71.6 |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.514 | +0.2% | +0.0005 to +0.0045 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 174.5 | 174.4 | −0.0% | −0.4463 to +0.3118 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.5 | 174.4 | −0.0% | −0.4463 to +0.3118 | no |
| response time (ms), mean | 383.1 | 240.3 | −37.3% | −195.9815 to −89.5831 | yes: GAIN |
| response time (ms), 95th percentile | 1093 | 620.6 | −43.2% | −730.7600 to −213.1940 | yes: GAIN |
| response time (ms), 99th percentile | 4174 | 3460 | −17.1% | −1842.0642 to +414.3956 | no |
| time over the response line (% of samples) | 26.64 | 17.82 | −33.1% | −12.6763 to −4.9641 | yes: GAIN |
| failed requests (%) | 14.43 | 12.73 | −11.8% | −2.9402 to −0.4721 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 8.7 | −17.9% | −2.6872 to −1.1128 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.5 | +48.500 (native is 0) | +40.6696 to +56.3304 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.215 | +316.1% | −0.0789 to +0.4056 | no |
| utilisation (used / allocatable) | 0.1079 | 0.1064 | −1.4% | −0.0027 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.59 | 2.554 | −1.4% | −0.0652 to −0.0071 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01339 | +0.013 (native is 0) | +0.0122 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.59 | 2.567 | −0.9% | −0.0513 to +0.0058 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 291.5 | 293 | +0.5% | −2.6171 to +5.5720 | no |
| HPA replicas, mean | 9.389 | 9.963 | +6.1% | +0.1535 to +0.9938 | yes: power given |
| pods started | 5.7 | 6.5 | +14.0% | −1.9353 to +3.5353 | no |
| pod start wait, total (s) | 9.6 | 9.8 | +2.1% | −4.6608 to +5.0608 | no |
| pod start wait, mean (s) | 1.684 | 1.388 | −17.6% | −0.6895 to +0.0969 | no |
| host CPU busy, the real machine under kind (%) | 74.05 | 73.8 | −0.3% | −0.8808 to +0.3843 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 57.22 | 55.9 | −2.3% | −6.9471 to +4.2928 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 71.05 | 71.6 | +0.8% | −1.2609 to +2.3518 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 3 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*