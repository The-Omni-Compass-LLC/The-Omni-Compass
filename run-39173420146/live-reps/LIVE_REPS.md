# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1410 | 1409 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1410 | 1409 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 472.4 | 302.2 |
| response time (ms), 95th percentile | 1548 | 924.1 |
| response time (ms), 99th percentile | 5088 | 4816 |
| time over the response line (% of samples) | 31.65 | 20.67 |
| failed requests (%) | 16.37 | 14.22 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 99 | 80.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 7.692 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.894 | 2.206 |
| utilisation (used / allocatable) | 0.1209 | 0.1195 |
| CPU used (cores), mean | 2.901 | 2.869 |
| Omni's own CPU (cores), mean | 0 | 0.01043 |
| CPU used with Omni's own (cores), mean | 2.901 | 2.879 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 246.8 | 249.1 |
| HPA replicas, mean | 9.944 | 14.98 |
| pods started | 4.333 | 14.33 |
| pod start wait, total (s) | 7.333 | 27 |
| pod start wait, mean (s) | 1.644 | 1.904 |
| host CPU busy, the real machine under kind (%) | 81.35 | 81.25 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.779e-16 to +1.57e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.02 | +0.1% | -0.006127 to +0.02835 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1410 | 1409 | -0.1% | -4.849 to +2.734 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1410 | 1409 | -0.1% | -4.849 to +2.734 | no |
| response time (ms), mean | 472.4 | 302.2 | -36.0% | -247.9 to -92.59 | yes: GAIN |
| response time (ms), 95th percentile | 1548 | 924.1 | -40.3% | -1185 to -62.31 | yes: GAIN |
| response time (ms), 99th percentile | 5088 | 4816 | -5.4% | -2676 to +2132 | no |
| time over the response line (% of samples) | 31.65 | 20.67 | -34.7% | -18.22 to -3.736 | yes: GAIN |
| failed requests (%) | 16.37 | 14.22 | -13.1% | -6.259 to +1.97 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 99 | 80.33 | -18.9% | -24.92 to -12.41 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.3 | +155 (native is 0) | -95.69 to +406.4 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.894 | 2.206 | +16.4% | -0.85 to +1.472 | no |
| utilisation (used / allocatable) | 0.1209 | 0.1195 | -1.1% | -0.003741 to +0.001087 | no |
| CPU used (cores), mean | 2.901 | 2.869 | -1.1% | -0.08979 to +0.02609 | no |
| Omni's own CPU (cores), mean | 0 | 0.01043 | +0.0104 (native is 0) | +0.00986 to +0.01101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.901 | 2.879 | -0.7% | -0.07965 to +0.03681 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 246.8 | 249.1 | +0.9% | -1.17 to +5.685 | no |
| HPA replicas, mean | 9.944 | 14.98 | +50.7% | +4.646 to +5.434 | yes: power given |
| pods started | 4.333 | 14.33 | +230.8% | -9.403 to +29.4 | no |
| pod start wait, total (s) | 7.333 | 27 | +268.2% | -13.7 to +53.03 | no |
| pod start wait, mean (s) | 1.644 | 1.904 | +15.8% | -1.251 to +1.77 | no |
| host CPU busy, the real machine under kind (%) | 81.35 | 81.25 | -0.1% | -1.285 to +1.09 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.008 | 117 | 97.5% | 0 | 1.12 | yes |
| omni | 2 | long |  |  |  | 0 | 0.997 | 119 | 99.2% | 0 | 0.64 | yes |
| omni | 3 | long |  |  |  | 0 | 1.023 | 117 | 97.5% | 0 | 0.91 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*