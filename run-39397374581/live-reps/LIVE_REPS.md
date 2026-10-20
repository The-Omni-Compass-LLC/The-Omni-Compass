# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.51 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 502.4 | 501.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 502.4 | 501.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 210.4 | 111.7 |
| response time (ms), 95th percentile | 559.1 | 204 |
| response time (ms), 99th percentile | 1636 | 853.1 |
| time over the response line (% of samples) | 10.31 | 4.61 |
| failed requests (%) | 4.004 | 3.366 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.1 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.58 |
| utilisation (used / allocatable) | 0.08101 | 0.07875 |
| CPU used (cores), mean | 1.944 | 1.89 |
| Omni's own CPU (cores), mean | 0 | 0.00819 |
| CPU used with Omni's own (cores), mean | 1.944 | 1.898 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 368.2 | 377.9 |
| HPA replicas, mean | 9.43 | 9.834 |
| pods started | 6.2 | 9.6 |
| pod start wait, total (s) | 8.8 | 13.6 |
| pod start wait, mean (s) | 1.425 | 1.381 |
| host CPU busy, the real machine under kind (%) | 55.46 | 54.4 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.066e-16 to +1.162e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.51 | 4.518 | +0.2% | +0.002794 to +0.01321 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 502.4 | 501.8 | -0.1% | -1.368 to +0.1091 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 502.4 | 501.8 | -0.1% | -1.368 to +0.1091 | no |
| response time (ms), mean | 210.4 | 111.7 | -46.9% | -132.9 to -64.46 | yes: GAIN |
| response time (ms), 95th percentile | 559.1 | 204 | -63.5% | -440.1 to -270 | yes: GAIN |
| response time (ms), 99th percentile | 1636 | 853.1 | -47.8% | -1448 to -116.5 | yes: GAIN |
| time over the response line (% of samples) | 10.31 | 4.61 | -55.3% | -8.504 to -2.895 | yes: GAIN |
| failed requests (%) | 4.004 | 3.366 | -15.9% | -1.346 to +0.0705 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.1 | 9.7 | -46.4% | -11.53 to -5.269 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45 | +45 (native is 0) | +34.68 to +55.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.58 | +8.7% | -0.2625 to +0.3558 | no |
| utilisation (used / allocatable) | 0.08101 | 0.07875 | -2.8% | -0.003209 to -0.001316 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.944 | 1.89 | -2.8% | -0.07702 to -0.03158 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00819 | +0.00819 (native is 0) | +0.0072 to +0.00918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.944 | 1.898 | -2.4% | -0.06838 to -0.02384 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 368.2 | 377.9 | +2.7% | +5.391 to +14.13 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.43 | 9.834 | +4.3% | -0.07054 to +0.8776 | no |
| pods started | 6.2 | 9.6 | +54.8% | +1.707 to +5.093 | yes: power given |
| pod start wait, total (s) | 8.8 | 13.6 | +54.5% | +0.2534 to +9.347 | yes: LOSS |
| pod start wait, mean (s) | 1.425 | 1.381 | -3.1% | -0.3837 to +0.2943 | no |
| host CPU busy, the real machine under kind (%) | 55.46 | 54.4 | -1.9% | -1.683 to -0.4492 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*