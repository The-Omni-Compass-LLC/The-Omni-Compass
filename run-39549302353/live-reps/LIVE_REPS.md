# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 511.6 | 510.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.6 | 510.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 249.7 | 139.9 |
| response time (ms), 95th percentile | 622.4 | 280.4 |
| response time (ms), 99th percentile | 2443 | 1392 |
| time over the response line (% of samples) | 16.62 | 10.87 |
| failed requests (%) | 10.02 | 8.76 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.45 |
| utilisation (used / allocatable) | 0.09409 | 0.09213 |
| CPU used (cores), mean | 2.258 | 2.211 |
| Omni's own CPU (cores), mean | 0 | 0.00868 |
| CPU used with Omni's own (cores), mean | 2.258 | 2.22 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.6 | 352.4 |
| HPA replicas, mean | 9.479 | 9.391 |
| pods started | 5.8 | 6.4 |
| pod start wait, total (s) | 8.3 | 11 |
| pod start wait, mean (s) | 1.46 | 1.768 |
| host CPU busy, the real machine under kind (%) | 63.95 | 62.97 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.115e-15 to +7.599e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.516 | +0.1% | -0.002459 to +0.009792 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 511.6 | 510.7 | -0.2% | -1.978 to +0.1546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.6 | 510.7 | -0.2% | -1.978 to +0.1546 | no |
| response time (ms), mean | 249.7 | 139.9 | -44.0% | -154 to -65.78 | yes: GAIN |
| response time (ms), 95th percentile | 622.4 | 280.4 | -54.9% | -456.9 to -227 | yes: GAIN |
| response time (ms), 99th percentile | 2443 | 1392 | -43.0% | -1936 to -166 | yes: GAIN |
| time over the response line (% of samples) | 16.62 | 10.87 | -34.6% | -8.749 to -2.746 | yes: GAIN |
| failed requests (%) | 10.02 | 8.76 | -12.6% | -2.124 to -0.4055 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.7 | -21.1% | -6.47 to -3.53 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 | +34.8 (native is 0) | +26.46 to +43.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2383 | 0.45 | +88.8% | -0.02954 to +0.4529 | no |
| utilisation (used / allocatable) | 0.09409 | 0.09213 | -2.1% | -0.002841 to -0.001074 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.258 | 2.211 | -2.1% | -0.06818 to -0.02578 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00868 | +0.00868 (native is 0) | +0.006902 to +0.01046 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.258 | 2.22 | -1.7% | -0.05926 to -0.01734 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.6 | 352.4 | +2.3% | +0.7678 to +14.81 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.479 | 9.391 | -0.9% | -0.4274 to +0.2509 | no |
| pods started | 5.8 | 6.4 | +10.3% | -0.8385 to +2.039 | no |
| pod start wait, total (s) | 8.3 | 11 | +32.5% | -0.8051 to +6.205 | no |
| pod start wait, mean (s) | 1.46 | 1.768 | +21.1% | +0.04371 to +0.5723 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 63.95 | 62.97 | -1.5% | -1.547 to -0.404 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*