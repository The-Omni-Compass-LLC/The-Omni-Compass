# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.358 |
| node-hours | 2.516 | 2.244 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 252.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 488.4 | 431.1 |
| response time (ms), 95th percentile | 2988 | 2902 |
| response time (ms), 99th percentile | 4454 | 4529 |
| time over the response line (% of samples) | 15.22 | 14.81 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 180.1 | 185.2 |
| utilisation (used / allocatable) | 0.06065 | 0.06836 |
| CPU used (cores), mean | 1.456 | 1.457 |
| Omni's own CPU (cores), mean | 0 | 0.01979 |
| CPU used with Omni's own (cores), mean | 1.456 | 1.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.3 | 416.1 |
| HPA replicas, mean | 2.06 | 2.208 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.3 |
| pod start wait, mean (s) | 0 | 0.3 |
| host CPU busy, the real machine under kind (%) | 41.42 | 42.17 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 561.2 | 566.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.002 |

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
| worker nodes in service, mean | 6 | 5.358 | -10.7% | -1.106 to -0.1777 | yes: GAIN |
| node-hours | 2.516 | 2.244 | -10.8% | -0.4623 to -0.08102 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.6 | -0.1% | -0.7815 to +0.4632 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 252.5 | -7.5% | -34.66 to -6.008 | yes: GAIN |
| response time (ms), mean | 488.4 | 431.1 | -11.7% | -76.14 to -38.48 | yes: GAIN |
| response time (ms), 95th percentile | 2988 | 2902 | -2.9% | -260.8 to +90.5 | no |
| response time (ms), 99th percentile | 4454 | 4529 | +1.7% | -158.9 to +307.7 | no |
| time over the response line (% of samples) | 15.22 | 14.81 | -2.7% | -0.7442 to -0.0694 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 | +12.2 (native is 0) | +10.55 to +13.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 180.1 | 185.2 | +2.8% | +2.253 to +7.907 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06065 | 0.06836 | +12.7% | +0.001857 to +0.01358 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.456 | 1.457 | +0.1% | -0.01784 to +0.01978 | no |
| Omni's own CPU (cores), mean | 0 | 0.01979 | +0.0198 (native is 0) | +0.01575 to +0.02383 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.456 | 1.476 | +1.4% | +0.002185 to +0.03934 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.3 | 416.1 | -8.0% | -62.99 to -9.386 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 2.208 | +7.2% | -0.214 to +0.5104 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 42.17 | +1.8% | +0.3732 to +1.129 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 561.2 | 566.1 | +0.9% | -1.412 to +11.21 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.002 | -16.6% | -1.694 to -0.3013 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*