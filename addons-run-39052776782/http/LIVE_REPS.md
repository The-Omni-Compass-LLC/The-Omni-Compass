# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.9 | 88.75 |
| response time (ms), 95th percentile | 484.2 | 135 |
| response time (ms), 99th percentile | 657.4 | 306.5 |
| time over the response line (% of samples) | 4.522 | 0.2068 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.35 |
| utilisation (used / allocatable) | 0.03148 | 0.04888 |
| CPU used (cores), mean | 0.7555 | 1.173 |
| Omni's own CPU (cores), mean | 0 | 0.00941 |
| CPU used with Omni's own (cores), mean | 0.7555 | 1.183 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.3 | 552.1 |
| HPA replicas, mean | 2.887 | 2.408 |
| pods started | 2.8 | 2 |
| pod start wait, total (s) | 23.9 | 18.8 |
| pod start wait, mean (s) | 8.45 | 9.25 |
| host CPU busy, the real machine under kind (%) | 23.77 | 35.54 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.009434 to +0.004434 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.6 | +2.3% | +2.672 to +4.735 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.6 | +2.3% | +2.672 to +4.735 | yes: power given |
| response time (ms), mean | 204.9 | 88.75 | -56.7% | -132.8 to -99.43 | yes: GAIN |
| response time (ms), 95th percentile | 484.2 | 135 | -72.1% | -396.2 to -302.2 | yes: GAIN |
| response time (ms), 99th percentile | 657.4 | 306.5 | -53.4% | -404 to -297.9 | yes: GAIN |
| time over the response line (% of samples) | 4.522 | 0.2068 | -95.4% | -6.274 to -2.356 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 0.1 | -97.9% | -6.834 to -2.566 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4 (native is 0) | +3.523 to +4.477 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.35 | -6.2% | -0.208 to +0.1614 | no |
| utilisation (used / allocatable) | 0.03148 | 0.04888 | +55.3% | +0.01511 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7555 | 1.173 | +55.3% | +0.3627 to +0.4728 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.00941 (native is 0) | +0.008306 to +0.01051 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7555 | 1.183 | +56.5% | +0.3711 to +0.4832 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.3 | 552.1 | -33.5% | -293.8 to -262.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.887 | 2.408 | -16.6% | -0.7588 to -0.2004 | yes: GAIN |
| pods started | 2.8 | 2 | -28.6% | -1.364 to -0.2358 | yes: GAIN |
| pod start wait, total (s) | 23.9 | 18.8 | -21.3% | -10.13 to -0.07076 | yes: GAIN |
| pod start wait, mean (s) | 8.45 | 9.25 | +9.5% | +0.2734 to +1.327 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.77 | 35.54 | +49.5% | +10.16 to +13.38 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*