# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.6 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 85.59 | 86.78 |
| response time (ms), 95th percentile | 130.6 | 130.8 |
| response time (ms), 99th percentile | 150.2 | 148.7 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.11 | 0.02667 |
| utilisation (used / allocatable) | 0.04961 | 0.0493 |
| CPU used (cores), mean | 1.191 | 1.183 |
| Omni's own CPU (cores), mean | 0 | 0.03393 |
| CPU used with Omni's own (cores), mean | 1.191 | 1.217 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.9 | 550.3 |
| HPA replicas, mean | 2.962 | 2.943 |
| pods started | 1.8 | 1.7 |
| pod start wait, total (s) | 2.7 | 3 |
| pod start wait, mean (s) | 1.6 | 1.7 |
| host CPU busy, the real machine under kind (%) | 37.08 | 38.1 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.121e-16 to +2.897e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.518 | +0.3% | -0.005524 to +0.01352 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.6 | 162 | +0.2% | -0.6055 to +1.387 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 162 | +0.2% | -0.6055 to +1.387 | no |
| response time (ms), mean | 85.59 | 86.78 | +1.4% | +0.2827 to +2.093 | yes: LOSS |
| response time (ms), 95th percentile | 130.6 | 130.8 | +0.2% | -1.855 to +2.312 | no |
| response time (ms), 99th percentile | 150.2 | 148.7 | -1.0% | -6.538 to +3.545 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4 (native is 0) | +4 to +4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.11 | 0.02667 | -75.8% | -0.1794 to +0.0127 | no |
| utilisation (used / allocatable) | 0.04961 | 0.0493 | -0.6% | -0.00117 to +0.000549 | no |
| CPU used (cores), mean | 1.191 | 1.183 | -0.6% | -0.02808 to +0.01318 | no |
| Omni's own CPU (cores), mean | 0 | 0.03393 | +0.0339 (native is 0) | +0.02931 to +0.03855 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.191 | 1.217 | +2.2% | +0.00323 to +0.04972 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.9 | 550.3 | +1.0% | -5.296 to +16.15 | no |
| HPA replicas, mean | 2.962 | 2.943 | -0.7% | -0.2466 to +0.2071 | no |
| pods started | 1.8 | 1.7 | -5.6% | -0.8113 to +0.6113 | no |
| pod start wait, total (s) | 2.7 | 3 | +11.1% | -1.283 to +1.883 | no |
| pod start wait, mean (s) | 1.6 | 1.7 | +6.3% | -0.3397 to +0.5397 | no |
| host CPU busy, the real machine under kind (%) | 37.08 | 38.1 | +2.8% | +0.2913 to +1.758 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*