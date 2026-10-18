# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1407 | 1405 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1407 | 1405 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 494.3 | 301 |
| response time (ms), 95th percentile | 1531 | 870.1 |
| response time (ms), 99th percentile | 6051 | 4464 |
| time over the response line (% of samples) | 34.42 | 22.96 |
| failed requests (%) | 19.91 | 16.57 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 98.33 | 79 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 26.11 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.661 | 2.511 |
| utilisation (used / allocatable) | 0.1197 | 0.1176 |
| CPU used (cores), mean | 2.873 | 2.824 |
| Omni's own CPU (cores), mean | 0 | 0.0109 |
| CPU used with Omni's own (cores), mean | 2.873 | 2.834 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 255.6 | 259.8 |
| HPA replicas, mean | 9.935 | 14.98 |
| pods started | 5.333 | 16.33 |
| pod start wait, total (s) | 18.67 | 36.33 |
| pod start wait, mean (s) | 3.5 | 2.082 |
| host CPU busy, the real machine under kind (%) | 80.42 | 80.04 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.207e-15 to +2.207e-15 | no |
| node-hours | 12.01 | 12.02 | +0.1% | -0.007794 to +0.02668 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1407 | 1405 | -0.1% | -4.133 to -0.02824 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1407 | 1405 | -0.1% | -4.133 to -0.02824 | yes: GAIN |
| response time (ms), mean | 494.3 | 301 | -39.1% | -381.6 to -5.098 | yes: GAIN |
| response time (ms), 95th percentile | 1531 | 870.1 | -43.2% | -1363 to +40.1 | no |
| response time (ms), 99th percentile | 6051 | 4464 | -26.2% | -2940 to -234.5 | yes: GAIN |
| time over the response line (% of samples) | 34.42 | 22.96 | -33.3% | -26.32 to +3.403 | no |
| failed requests (%) | 19.91 | 16.57 | -16.8% | -10.8 to +4.112 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 98.33 | 79 | -19.7% | -33.89 to -4.776 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.7 | +165 (native is 0) | -120.1 to +449.4 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.661 | 2.511 | -5.6% | -6.116 to +5.816 | no |
| utilisation (used / allocatable) | 0.1197 | 0.1176 | -1.7% | -0.002744 to -0.00134 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.873 | 2.824 | -1.7% | -0.06585 to -0.03216 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0109 | +0.0109 (native is 0) | +0.009349 to +0.01245 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.873 | 2.834 | -1.3% | -0.05641 to -0.0198 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 255.6 | 259.8 | +1.6% | -0.8078 to +9.053 | no |
| HPA replicas, mean | 9.935 | 14.98 | +50.8% | +4.57 to +5.521 | yes: power given |
| pods started | 5.333 | 16.33 | +206.2% | -25.6 to +47.6 | no |
| pod start wait, total (s) | 18.67 | 36.33 | +94.6% | -71.3 to +106.6 | no |
| pod start wait, mean (s) | 3.5 | 2.082 | -40.5% | -2.357 to -0.4788 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 80.42 | 80.04 | -0.5% | -1.168 to +0.4102 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.038 | 119 | 99.2% | 0 | 0.75 | yes |
| omni | 2 | long |  |  |  | 0 | 1.017 | 117 | 97.5% | 0 | 0.79 | yes |
| omni | 3 | long |  |  |  | 0 | 1.008 | 117 | 97.5% | 0 | 0.89 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*