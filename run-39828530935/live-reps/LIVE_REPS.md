# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1346 | 1344 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1346 | 1344 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 288.4 | 187.7 |
| response time (ms), 95th percentile | 1100 | 610.9 |
| response time (ms), 99th percentile | 2861 | 2328 |
| time over the response line (% of samples) | 16.27 | 11.44 |
| failed requests (%) | 9.201 | 8.333 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 48.67 | 35.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70.74 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.417 | 2.817 |
| utilisation (used / allocatable) | 0.0848 | 0.08412 |
| CPU used (cores), mean | 2.035 | 2.019 |
| Omni's own CPU (cores), mean | 0 | 0.02587 |
| CPU used with Omni's own (cores), mean | 2.035 | 2.045 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 377.7 | 378.6 |
| HPA replicas, mean | 9.86 | 11.54 |
| pods started | 9 | 20.67 |
| pod start wait, total (s) | 9 | 29.33 |
| pod start wait, mean (s) | 1 | 1.448 |
| host CPU busy, the real machine under kind (%) | 58.18 | 58.95 |
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
| node-hours | 12.02 | 12.01 | -0.0% | -0.04086 to +0.03086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1346 | 1344 | -0.1% | -10.67 to +7.681 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1346 | 1344 | -0.1% | -10.67 to +7.681 | no |
| response time (ms), mean | 288.4 | 187.7 | -34.9% | -336.9 to +135.5 | no |
| response time (ms), 95th percentile | 1100 | 610.9 | -44.5% | -1779 to +800.6 | no |
| response time (ms), 99th percentile | 2861 | 2328 | -18.6% | -1421 to +353.7 | no |
| time over the response line (% of samples) | 16.27 | 11.44 | -29.7% | -20.33 to +10.66 | no |
| failed requests (%) | 9.201 | 8.333 | -9.4% | -4.6 to +2.865 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 48.67 | 35.33 | -27.4% | -18.5 to -8.162 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.7 | +166 (native is 0) | -26.55 to +357.9 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.417 | 2.817 | +98.8% | -3.389 to +6.189 | no |
| utilisation (used / allocatable) | 0.0848 | 0.08412 | -0.8% | -0.00374 to +0.002384 | no |
| CPU used (cores), mean | 2.035 | 2.019 | -0.8% | -0.08976 to +0.05721 | no |
| Omni's own CPU (cores), mean | 0 | 0.02587 | +0.0259 (native is 0) | +0.002709 to +0.04902 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.035 | 2.045 | +0.5% | -0.0408 to +0.05999 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 377.7 | 378.6 | +0.2% | -4.475 to +6.237 | no |
| HPA replicas, mean | 9.86 | 11.54 | +17.1% | -7.514 to +10.88 | no |
| pods started | 9 | 20.67 | +129.6% | -2.46 to +25.79 | no |
| pod start wait, total (s) | 9 | 29.33 | +225.9% | -0.7957 to +41.46 | no |
| pod start wait, mean (s) | 1 | 1.448 | +44.8% | +0.08039 to +0.8153 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.18 | 58.95 | +1.3% | +0.4901 to +1.047 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.060 | 480 | 100.0% | 0 | 1.16 | yes |
| omni | 2 | long |  |  |  | 0 | 1.054 | 480 | 100.0% | 0 | 1.12 | yes |
| omni | 3 | long |  |  |  | 0 | 1.031 | 480 | 100.0% | 0 | 1.12 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*