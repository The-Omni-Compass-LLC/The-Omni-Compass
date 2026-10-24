# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1324 | 1319 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1324 | 1319 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 184 | 100.9 |
| response time (ms), 95th percentile | 509.7 | 205.2 |
| response time (ms), 99th percentile | 1477 | 757.5 |
| time over the response line (% of samples) | 6.487 | 2.301 |
| failed requests (%) | 1.047 | 0.8751 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.67 | 18 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 188 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 79.37 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.578 | 2.75 |
| utilisation (used / allocatable) | 0.07313 | 0.07019 |
| CPU used (cores), mean | 1.755 | 1.684 |
| Omni's own CPU (cores), mean | 0 | 0.0078 |
| CPU used with Omni's own (cores), mean | 1.755 | 1.692 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 399.2 | 418.1 |
| HPA replicas, mean | 9.859 | 11.47 |
| pods started | 8 | 21 |
| pod start wait, total (s) | 10.33 | 32.67 |
| pod start wait, mean (s) | 1.259 | 1.492 |
| host CPU busy, the real machine under kind (%) | 49.75 | 48.4 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| node-hours | 12.01 | 12.01 | −0.0% | −0.0174 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1324 | 1319 | −0.4% | −9.4309 to −2.0460 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1324 | 1319 | −0.4% | −9.4309 to −2.0460 | yes: GAIN |
| response time (ms), mean | 184 | 100.9 | −45.2% | −207.6027 to +41.4201 | no |
| response time (ms), 95th percentile | 509.7 | 205.2 | −59.7% | −641.4933 to +32.4900 | no |
| response time (ms), 99th percentile | 1477 | 757.5 | −48.7% | −1880.9269 to +441.7856 | no |
| time over the response line (% of samples) | 6.487 | 2.301 | −64.5% | −15.1054 to +6.7339 | no |
| failed requests (%) | 1.047 | 0.8751 | −16.4% | −0.9121 to +0.5681 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.67 | 18 | −46.5% | −43.1445 to +11.8112 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 188 | +188.000 (native is 0) | −1.5926 to +377.5926 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.578 | 2.75 | +74.3% | −1.8206 to +4.1650 | no |
| utilisation (used / allocatable) | 0.07313 | 0.07019 | −4.0% | −0.0060 to +0.0001 | no |
| CPU used (cores), mean | 1.755 | 1.684 | −4.0% | −0.1435 to +0.0022 | no |
| Omni's own CPU (cores), mean | 0 | 0.0078 | +0.008 (native is 0) | +0.0034 to +0.0122 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.755 | 1.692 | −3.6% | −0.1374 to +0.0117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 399.2 | 418.1 | +4.7% | −12.3919 to +50.1588 | no |
| HPA replicas, mean | 9.859 | 11.47 | +16.3% | −5.7724 to +8.9906 | no |
| pods started | 8 | 21 | +162.5% | −4.9148 to +30.9148 | no |
| pod start wait, total (s) | 10.33 | 32.67 | +216.1% | −30.3870 to +75.0536 | no |
| pod start wait, mean (s) | 1.259 | 1.492 | +18.5% | −1.4377 to +1.9031 | no |
| host CPU busy, the real machine under kind (%) | 49.75 | 48.4 | −2.7% | −4.0906 to +1.3844 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.037 | 120 | 100.0% | 0 | 1.09 | yes |
| omni | 2 | long |  |  |  | 0 | 1.036 | 120 | 100.0% | 0 | 1.25 | yes |
| omni | 3 | long |  |  |  | 0 | 1.026 | 120 | 100.0% | 0 | 1.01 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*