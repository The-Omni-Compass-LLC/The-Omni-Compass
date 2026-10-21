# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 194.2 | 82.55 |
| response time (ms), 95th percentile | 456.1 | 128.5 |
| response time (ms), 99th percentile | 601 | 267.6 |
| time over the response line (% of samples) | 4.434 | 0.1829 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08333 |
| utilisation (used / allocatable) | 0.02968 | 0.0457 |
| CPU used (cores), mean | 0.7123 | 1.097 |
| Omni's own CPU (cores), mean | 0 | 0.01011 |
| CPU used with Omni's own (cores), mean | 0.7123 | 1.107 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 880.5 | 593 |
| HPA replicas, mean | 2.803 | 2.501 |
| pods started | 2.7 | 2.5 |
| pod start wait, total (s) | 3.5 | 3.2 |
| pod start wait, mean (s) | 1.317 | 1.283 |
| host CPU busy, the real machine under kind (%) | 22.99 | 34.15 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.439e-17 to +1.367e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.516 | -0.1% | -0.009127 to +0.005461 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.2 | +2.2% | +2.355 to +4.535 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.2 | +2.2% | +2.355 to +4.535 | yes: power given |
| response time (ms), mean | 194.2 | 82.55 | -57.5% | -136.4 to -86.82 | yes: GAIN |
| response time (ms), 95th percentile | 456.1 | 128.5 | -71.8% | -390.8 to -264.4 | yes: GAIN |
| response time (ms), 99th percentile | 601 | 267.6 | -55.5% | -397.2 to -269.5 | yes: GAIN |
| time over the response line (% of samples) | 4.434 | 0.1829 | -95.9% | -6.588 to -1.914 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 0.2 | -95.7% | -7.029 to -1.971 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5 | +5 (native is 0) | +3.694 to +6.306 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08333 | -21.9% | -0.216 to +0.1693 | no |
| utilisation (used / allocatable) | 0.02968 | 0.0457 | +54.0% | +0.01292 to +0.01913 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7123 | 1.097 | +54.0% | +0.3101 to +0.4592 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01011 | +0.0101 (native is 0) | +0.008653 to +0.01157 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7123 | 1.107 | +55.4% | +0.3188 to +0.4707 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 880.5 | 593 | -32.6% | -307 to -268 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.803 | 2.501 | -10.8% | -0.531 to -0.0736 | yes: GAIN |
| pods started | 2.7 | 2.5 | -7.4% | -0.6524 to +0.2524 | no |
| pod start wait, total (s) | 3.5 | 3.2 | -8.6% | -1.257 to +0.6567 | no |
| pod start wait, mean (s) | 1.317 | 1.283 | -2.5% | -0.4137 to +0.347 | no |
| host CPU busy, the real machine under kind (%) | 22.99 | 34.15 | +48.5% | +9.063 to +13.25 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*