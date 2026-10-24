# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1395 | 1393 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1395 | 1393 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 525.8 | 309 |
| response time (ms), 95th percentile | 2132 | 958.3 |
| response time (ms), 99th percentile | 5170 | 4495 |
| time over the response line (% of samples) | 37.02 | 24.19 |
| failed requests (%) | 21.5 | 18.32 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 84.33 | 71 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 32.05 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.628 | 1.828 |
| utilisation (used / allocatable) | 0.1128 | 0.1107 |
| CPU used (cores), mean | 2.708 | 2.657 |
| Omni's own CPU (cores), mean | 0 | 0.01017 |
| CPU used with Omni's own (cores), mean | 2.708 | 2.667 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294 | 299.2 |
| HPA replicas, mean | 9.904 | 13.3 |
| pods started | 6.333 | 10.67 |
| pod start wait, total (s) | 9 | 21.33 |
| pod start wait, mean (s) | 1.444 | 2.349 |
| host CPU busy, the real machine under kind (%) | 76.4 | 75.97 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.095e-15 to +1.318e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.02 | +0.1% | -0.01179 to +0.02735 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1395 | 1393 | -0.2% | -7.663 to +2.366 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1395 | 1393 | -0.2% | -7.663 to +2.366 | no |
| response time (ms), mean | 525.8 | 309 | -41.2% | -578.2 to +144.6 | no |
| response time (ms), 95th percentile | 2132 | 958.3 | -55.1% | -3239 to +890.6 | no |
| response time (ms), 99th percentile | 5170 | 4495 | -13.1% | -1293 to -58.29 | yes: GAIN |
| time over the response line (% of samples) | 37.02 | 24.19 | -34.7% | -37.52 to +11.85 | no |
| failed requests (%) | 21.5 | 18.32 | -14.8% | -10.31 to +3.939 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 84.33 | 71 | -15.8% | -21.32 to -5.347 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123 | +123 (native is 0) | +58.41 to +187.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.628 | 1.828 | -30.4% | -3.367 to +1.767 | no |
| utilisation (used / allocatable) | 0.1128 | 0.1107 | -1.9% | -0.004169 to -0.0001055 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.708 | 2.657 | -1.9% | -0.1001 to -0.002531 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01017 | +0.0102 (native is 0) | +0.003875 to +0.01646 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.708 | 2.667 | -1.5% | -0.08474 to +0.002486 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294 | 299.2 | +1.8% | -2.565 to +13.05 | no |
| HPA replicas, mean | 9.904 | 13.3 | +34.3% | -4.066 to +10.85 | no |
| pods started | 6.333 | 10.67 | +68.4% | -2.838 to +11.5 | no |
| pod start wait, total (s) | 9 | 21.33 | +137.0% | -3.831 to +28.5 | no |
| pod start wait, mean (s) | 1.444 | 2.349 | +62.7% | -1.409 to +3.219 | no |
| host CPU busy, the real machine under kind (%) | 76.4 | 75.97 | -0.6% | -1.068 to +0.2065 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.009 | 120 | 100.0% | 0 | 1.01 | yes |
| omni | 2 | long |  |  |  | 0 | 1.017 | 120 | 100.0% | 0 | 1.13 | yes |
| omni | 3 | long |  |  |  | 0 | 1.043 | 120 | 100.0% | 0 | 1.28 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*