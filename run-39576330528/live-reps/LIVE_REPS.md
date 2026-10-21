# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.51 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 508.8 | 508.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.8 | 508.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 252.6 | 136.2 |
| response time (ms), 95th percentile | 682.3 | 292.4 |
| response time (ms), 99th percentile | 2249 | 1241 |
| time over the response line (% of samples) | 14.36 | 8.434 |
| failed requests (%) | 7.408 | 6.389 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 15.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.5667 |
| utilisation (used / allocatable) | 0.09048 | 0.08815 |
| CPU used (cores), mean | 2.171 | 2.116 |
| Omni's own CPU (cores), mean | 0 | 0.0088 |
| CPU used with Omni's own (cores), mean | 2.171 | 2.124 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.8 | 355.7 |
| HPA replicas, mean | 9.501 | 9.6 |
| pods started | 5.7 | 6.8 |
| pod start wait, total (s) | 8.1 | 10.5 |
| pod start wait, mean (s) | 1.44 | 1.463 |
| host CPU busy, the real machine under kind (%) | 61.59 | 60.45 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.471e-16 to +9.471e-16 | no |
| node-hours | 4.51 | 4.518 | +0.2% | +0.0008988 to +0.01577 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 508.8 | 508.2 | -0.1% | -1.649 to +0.4196 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.8 | 508.2 | -0.1% | -1.649 to +0.4196 | no |
| response time (ms), mean | 252.6 | 136.2 | -46.1% | -156.4 to -76.4 | yes: GAIN |
| response time (ms), 95th percentile | 682.3 | 292.4 | -57.1% | -536.4 to -243.5 | yes: GAIN |
| response time (ms), 99th percentile | 2249 | 1241 | -44.8% | -1524 to -491.8 | yes: GAIN |
| time over the response line (% of samples) | 14.36 | 8.434 | -41.3% | -8.981 to -2.881 | yes: GAIN |
| failed requests (%) | 7.408 | 6.389 | -13.8% | -1.815 to -0.2237 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 15.6 | -30.7% | -9.198 to -4.602 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.9 (native is 0) | +28.4 to +47.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.5667 | +41.1% | -0.1567 to +0.4867 | no |
| utilisation (used / allocatable) | 0.09048 | 0.08815 | -2.6% | -0.002975 to -0.001678 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.171 | 2.116 | -2.6% | -0.07139 to -0.04026 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0088 | +0.0088 (native is 0) | +0.00716 to +0.01044 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.171 | 2.124 | -2.2% | -0.06305 to -0.031 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.8 | 355.7 | +3.1% | +4.544 to +17.06 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.501 | 9.6 | +1.0% | -0.3022 to +0.5012 | no |
| pods started | 5.7 | 6.8 | +19.3% | -0.8792 to +3.079 | no |
| pod start wait, total (s) | 8.1 | 10.5 | +29.6% | -3.071 to +7.871 | no |
| pod start wait, mean (s) | 1.44 | 1.463 | +1.6% | -0.437 to +0.483 | no |
| host CPU busy, the real machine under kind (%) | 61.59 | 60.45 | -1.8% | -1.565 to -0.7071 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*