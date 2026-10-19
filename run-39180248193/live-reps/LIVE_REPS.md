# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 483.5 | 482 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.5 | 482 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 288.4 | 144.2 |
| response time (ms), 95th percentile | 748.8 | 308.5 |
| response time (ms), 99th percentile | 1413 | 700.5 |
| time over the response line (% of samples) | 14.49 | 3.57 |
| failed requests (%) | 1.49 | 1.294 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.51 | 1.233 |
| utilisation (used / allocatable) | 0.08195 | 0.07953 |
| CPU used (cores), mean | 1.967 | 1.909 |
| Omni's own CPU (cores), mean | 0 | 0.00991 |
| CPU used with Omni's own (cores), mean | 1.967 | 1.919 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 369.7 | 379.3 |
| HPA replicas, mean | 9.751 | 11.35 |
| pods started | 5.9 | 16.2 |
| pod start wait, total (s) | 9 | 28.9 |
| pod start wait, mean (s) | 1.541 | 1.778 |
| host CPU busy, the real machine under kind (%) | 56.79 | 55.58 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.173e-16 to +2.194e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.334 | 4.335 | +0.0% | -0.008289 to +0.01029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 483.5 | 482 | -0.3% | -2.567 to -0.3924 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.5 | 482 | -0.3% | -2.567 to -0.3924 | yes: GAIN |
| response time (ms), mean | 288.4 | 144.2 | -50.0% | -188.4 to -100.2 | yes: GAIN |
| response time (ms), 95th percentile | 748.8 | 308.5 | -58.8% | -565 to -315.6 | yes: GAIN |
| response time (ms), 99th percentile | 1413 | 700.5 | -50.4% | -941.1 to -484.5 | yes: GAIN |
| time over the response line (% of samples) | 14.49 | 3.57 | -75.4% | -15.44 to -6.394 | yes: GAIN |
| failed requests (%) | 1.49 | 1.294 | -13.2% | -0.3449 to -0.04736 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 9.4 | -62.1% | -21.2 to -9.597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64 | +64 (native is 0) | +44.98 to +83.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.51 | 1.233 | +141.8% | +0.2501 to +1.197 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08195 | 0.07953 | -3.0% | -0.003076 to -0.001782 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.967 | 1.909 | -3.0% | -0.07381 to -0.04277 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00991 | +0.00991 (native is 0) | +0.0082 to +0.01162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.967 | 1.919 | -2.5% | -0.06292 to -0.03385 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 369.7 | 379.3 | +2.6% | +7.238 to +11.87 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.751 | 11.35 | +16.4% | +0.2734 to +2.928 | yes: power given |
| pods started | 5.9 | 16.2 | +174.6% | +5.864 to +14.74 | yes: power given |
| pod start wait, total (s) | 9 | 28.9 | +221.1% | +11.85 to +27.95 | yes: LOSS |
| pod start wait, mean (s) | 1.541 | 1.778 | +15.4% | +0.0227 to +0.4505 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.79 | 55.58 | -2.1% | -1.715 to -0.7181 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*