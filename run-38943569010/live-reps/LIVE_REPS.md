# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 173 | 173.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173 | 173.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 571 | 519 |
| response time (ms), 95th percentile | 2398 | 2559 |
| response time (ms), 99th percentile | 5960 | 6119 |
| time over the response line (% of samples) | 26.06 | 22.95 |
| failed requests (%) | 4.014 | 3.02 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9617 | 1.263 |
| utilisation (used / allocatable) | 0.1002 | 0.09891 |
| CPU used (cores), mean | 2.404 | 2.374 |
| Omni's own CPU (cores), mean | 0 | 0.01154 |
| CPU used with Omni's own (cores), mean | 2.404 | 2.385 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 295.4 |
| HPA replicas, mean | 15.3 | 15.4 |
| pods started | 4.4 | 3.5 |
| pod start wait, total (s) | 9.8 | 7.7 |
| pod start wait, mean (s) | 2.068 | 1.73 |
| host CPU busy, the real machine under kind (%) | 70.08 | 69.99 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 256.9 | 272.2 |
| second app: response time (ms), 99th percentile | 1443 | 1839 |
| second app: time over the response line (% of samples) | 15.16 | 15.46 |
| second app: failed requests (%) | 13.9 | 13.95 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.518 | +0.3% | +0.002142 to +0.006524 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 173 | 173.3 | +0.2% | -0.1312 to +0.7938 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173 | 173.3 | +0.2% | -0.1312 to +0.7938 | no |
| response time (ms), mean | 571 | 519 | -9.1% | -104.4 to +0.394 | no |
| response time (ms), 95th percentile | 2398 | 2559 | +6.7% | -420.6 to +743.4 | no |
| response time (ms), 99th percentile | 5960 | 6119 | +2.7% | -630.7 to +948.5 | no |
| time over the response line (% of samples) | 26.06 | 22.95 | -11.9% | -4.968 to -1.248 | yes: GAIN |
| failed requests (%) | 4.014 | 3.02 | -24.8% | -1.702 to -0.2867 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 8.7 | -8.4% | -1.457 to -0.1427 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.8 | +32.8 (native is 0) | +30.33 to +35.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9617 | 1.263 | +31.4% | -0.8769 to +1.48 | no |
| utilisation (used / allocatable) | 0.1002 | 0.09891 | -1.3% | -0.00257 to +3.596e-05 | no |
| CPU used (cores), mean | 2.404 | 2.374 | -1.3% | -0.06169 to +0.000863 | no |
| Omni's own CPU (cores), mean | 0 | 0.01154 | +0.0115 (native is 0) | +0.01037 to +0.01271 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.404 | 2.385 | -0.8% | -0.05067 to +0.01292 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 295.4 | +1.6% | -1.09 to +10.44 | no |
| HPA replicas, mean | 15.3 | 15.4 | +0.7% | -0.2471 to +0.448 | no |
| pods started | 4.4 | 3.5 | -20.5% | -2.268 to +0.4676 | no |
| pod start wait, total (s) | 9.8 | 7.7 | -21.4% | -5.723 to +1.523 | no |
| pod start wait, mean (s) | 2.068 | 1.73 | -16.3% | -0.9595 to +0.2843 | no |
| host CPU busy, the real machine under kind (%) | 70.08 | 69.99 | -0.1% | -0.9534 to +0.766 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 256.9 | 272.2 | +6.0% | -12.45 to +43.09 | no |
| second app: response time (ms), 99th percentile | 1443 | 1839 | +27.4% | -655.1 to +1447 | no |
| second app: time over the response line (% of samples) | 15.16 | 15.46 | +2.0% | -0.4658 to +1.057 | no |
| second app: failed requests (%) | 13.9 | 13.95 | +0.4% | -0.3877 to +0.4939 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*