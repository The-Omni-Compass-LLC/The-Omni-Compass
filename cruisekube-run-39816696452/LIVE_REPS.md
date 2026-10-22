# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.8 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.8 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 84.88 | 85.83 |
| response time (ms), 95th percentile | 129.3 | 131.6 |
| response time (ms), 99th percentile | 147.9 | 156.2 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.135 |
| utilisation (used / allocatable) | 0.04963 | 0.04959 |
| CPU used (cores), mean | 1.191 | 1.19 |
| Omni's own CPU (cores), mean | 0 | 0.03533 |
| CPU used with Omni's own (cores), mean | 1.191 | 1.225 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 542.6 | 543.6 |
| HPA replicas, mean | 2.766 | 2.827 |
| pods started | 1.2 | 1.5 |
| pod start wait, total (s) | 2 | 2.1 |
| pod start wait, mean (s) | 1.733 | 1.35 |
| host CPU busy, the real machine under kind (%) | 37.1 | 38.47 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +5.794e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.1% | -0.008675 to +0.01034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.8 | 161.8 | +0.0% | -0.8621 to +0.9212 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.8 | 161.8 | +0.0% | -0.8621 to +0.9212 | no |
| response time (ms), mean | 84.88 | 85.83 | +1.1% | -0.569 to +2.483 | no |
| response time (ms), 95th percentile | 129.3 | 131.6 | +1.8% | -0.7994 to +5.459 | no |
| response time (ms), 99th percentile | 147.9 | 156.2 | +5.6% | -1.001 to +17.54 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4 (native is 0) | +4 to +4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.135 | +0.135 (native is 0) | -0.05661 to +0.3266 | no |
| utilisation (used / allocatable) | 0.04963 | 0.04959 | -0.1% | -0.001197 to +0.001116 | no |
| CPU used (cores), mean | 1.191 | 1.19 | -0.1% | -0.02872 to +0.02679 | no |
| Omni's own CPU (cores), mean | 0 | 0.03533 | +0.0353 (native is 0) | +0.03149 to +0.03917 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.191 | 1.225 | +2.9% | +0.004595 to +0.06414 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 542.6 | 543.6 | +0.2% | -10.77 to +12.76 | no |
| HPA replicas, mean | 2.766 | 2.827 | +2.2% | -0.1565 to +0.2778 | no |
| pods started | 1.2 | 1.5 | +25.0% | -0.3786 to +0.9786 | no |
| pod start wait, total (s) | 2 | 2.1 | +5.0% | -1.137 to +1.337 | no |
| pod start wait, mean (s) | 1.733 | 1.35 | -22.1% | -1.074 to +0.3074 | no |
| host CPU busy, the real machine under kind (%) | 37.1 | 38.47 | +3.7% | +0.7254 to +2.008 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*