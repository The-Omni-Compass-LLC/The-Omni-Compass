# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.5 | 170.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.5 | 170.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 276.1 | 176 |
| response time (ms), 95th percentile | 750.7 | 430.7 |
| response time (ms), 99th percentile | 2661 | 2144 |
| time over the response line (% of samples) | 14.15 | 8.867 |
| failed requests (%) | 5.476 | 5.269 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1783 |
| utilisation (used / allocatable) | 0.08873 | 0.0865 |
| CPU used (cores), mean | 2.13 | 2.076 |
| Omni's own CPU (cores), mean | 0 | 0.01351 |
| CPU used with Omni's own (cores), mean | 2.13 | 2.09 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 340 | 349.6 |
| HPA replicas, mean | 9.269 | 10.04 |
| pods started | 5.9 | 8 |
| pod start wait, total (s) | 8.3 | 13.1 |
| pod start wait, mean (s) | 1.458 | 1.513 |
| host CPU busy, the real machine under kind (%) | 60.61 | 60.07 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 300 s after the kill (%) | 22.99 | 23.23 |
| robust: time over the line in the 300 s after the kill (% of samples) | 39.58 | 38.69 |

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
| node-hours | 1.515 | 1.515 | +0.0% | −0.0024 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170.5 | 170.1 | −0.2% | −0.9446 to +0.1546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.5 | 170.1 | −0.2% | −0.9446 to +0.1546 | no |
| response time (ms), mean | 276.1 | 176 | −36.3% | −159.1680 to −41.0520 | yes: GAIN |
| response time (ms), 95th percentile | 750.7 | 430.7 | −42.6% | −491.3975 to −148.5245 | yes: GAIN |
| response time (ms), 99th percentile | 2661 | 2144 | −19.4% | −1635.1391 to +600.9493 | no |
| time over the response line (% of samples) | 14.15 | 8.867 | −37.3% | −8.2673 to −2.3008 | yes: GAIN |
| failed requests (%) | 5.476 | 5.269 | −3.8% | −0.5579 to +0.1430 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 5.3 | −27.4% | −2.6744 to −1.3256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.1 | +53.100 (native is 0) | +44.9830 to +61.2170 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1783 | +12.6% | −0.1665 to +0.2065 | no |
| utilisation (used / allocatable) | 0.08873 | 0.0865 | −2.5% | −0.0034 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.13 | 2.076 | −2.5% | −0.0822 to −0.0248 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01351 | +0.014 (native is 0) | +0.0109 to +0.0161 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.13 | 2.09 | −1.9% | −0.0695 to −0.0105 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 340 | 349.6 | +2.8% | +2.1968 to +16.9366 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.269 | 10.04 | +8.3% | +0.3057 to +1.2354 | yes: power given |
| pods started | 5.9 | 8 | +35.6% | −0.5860 to +4.7860 | no |
| pod start wait, total (s) | 8.3 | 13.1 | +57.8% | −0.9798 to +10.5798 | no |
| pod start wait, mean (s) | 1.458 | 1.513 | +3.8% | −0.5115 to +0.6220 | no |
| host CPU busy, the real machine under kind (%) | 60.61 | 60.07 | −0.9% | −1.2843 to +0.2139 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 22.99 | 23.23 | +1.0% | −1.3856 to +1.8673 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 39.58 | 38.69 | −2.3% | −3.7847 to +2.0010 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*