# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 120.8 | 76.63 |
| response time (ms), 95th percentile | 248.1 | 114.8 |
| response time (ms), 99th percentile | 356 | 150.6 |
| time over the response line (% of samples) | 0.2822 | 0.01227 |
| failed requests (%) | 0.01266 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.2167 |
| utilisation (used / allocatable) | 0.03616 | 0.04646 |
| CPU used (cores), mean | 0.8678 | 1.115 |
| Omni's own CPU (cores), mean | 0 | 0.01153 |
| CPU used with Omni's own (cores), mean | 0.8678 | 1.127 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726.9 | 581.5 |
| HPA replicas, mean | 8.795 | 8.917 |
| pods started | 5.5 | 4.9 |
| pod start wait, total (s) | 17 | 13.1 |
| pod start wait, mean (s) | 3.017 | 2.627 |
| host CPU busy, the real machine under kind (%) | 27.14 | 34.23 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.087e-17 to +1.147e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.514 | -0.4% | -0.01252 to +0.00152 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 160.8 | +1.1% | +0.7059 to +2.828 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160.8 | +1.1% | +0.7059 to +2.828 | yes: power given |
| response time (ms), mean | 120.8 | 76.63 | -36.6% | -58.34 to -30.06 | yes: GAIN |
| response time (ms), 95th percentile | 248.1 | 114.8 | -53.7% | -160.4 to -106.1 | yes: GAIN |
| response time (ms), 99th percentile | 356 | 150.6 | -57.7% | -246.6 to -164.2 | yes: GAIN |
| time over the response line (% of samples) | 0.2822 | 0.01227 | -95.7% | -0.5098 to -0.03006 | yes: GAIN |
| failed requests (%) | 0.01266 | 0 | -100.0% | -0.04129 to +0.01597 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.7 (native is 0) | +17.11 to +18.29 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.2167 | -31.9% | -0.4868 to +0.2834 | no |
| utilisation (used / allocatable) | 0.03616 | 0.04646 | +28.5% | +0.007438 to +0.01316 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8678 | 1.115 | +28.5% | +0.1785 to +0.3159 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01153 | +0.0115 (native is 0) | +0.009999 to +0.01306 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8678 | 1.127 | +29.8% | +0.1886 to +0.3288 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 726.9 | 581.5 | -20.0% | -170.8 to -120.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.795 | 8.917 | +1.4% | -0.09707 to +0.3393 | no |
| pods started | 5.5 | 4.9 | -10.9% | -1.1 to -0.09985 | yes: GAIN |
| pod start wait, total (s) | 17 | 13.1 | -22.9% | -8.872 to +1.072 | no |
| pod start wait, mean (s) | 3.017 | 2.627 | -12.9% | -1.2 to +0.4198 | no |
| host CPU busy, the real machine under kind (%) | 27.14 | 34.23 | +26.1% | +4.871 to +9.316 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*