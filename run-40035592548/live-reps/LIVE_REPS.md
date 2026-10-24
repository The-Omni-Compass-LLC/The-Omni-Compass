# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.77 |
| node-hours | 2.514 | 2.416 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 266.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 576.8 | 506.8 |
| response time (ms), 95th percentile | 3382 | 3323 |
| response time (ms), 99th percentile | 5020 | 5089 |
| time over the response line (% of samples) | 16.64 | 15.83 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 198.4 | 198.9 |
| utilisation (used / allocatable) | 0.06582 | 0.06801 |
| CPU used (cores), mean | 1.58 | 1.569 |
| Omni's own CPU (cores), mean | 0 | 0.01712 |
| CPU used with Omni's own (cores), mean | 1.58 | 1.586 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418 | 407.9 |
| HPA replicas, mean | 2.285 | 2.387 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 1.1 |
| host CPU busy, the real machine under kind (%) | 44.73 | 45.25 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 612.1 | 612.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.633 |

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
| worker nodes in service, mean | 6 | 5.77 | -3.8% | -0.5223 to +0.06311 | no |
| node-hours | 2.514 | 2.416 | -3.9% | -0.2244 to +0.02783 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274 | -0.2% | -1.681 to +0.5879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 266.8 | -2.8% | -17.67 to +2.162 | no |
| response time (ms), mean | 576.8 | 506.8 | -12.1% | -84.4 to -55.58 | yes: GAIN |
| response time (ms), 95th percentile | 3382 | 3323 | -1.7% | -203.9 to +87.59 | no |
| response time (ms), 99th percentile | 5020 | 5089 | +1.4% | -168.7 to +308.3 | no |
| time over the response line (% of samples) | 16.64 | 15.83 | -4.9% | -1.148 to -0.4725 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +11.23 to +13.77 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 198.4 | 198.9 | +0.3% | -4.421 to +5.588 | no |
| utilisation (used / allocatable) | 0.06582 | 0.06801 | +3.3% | -0.001353 to +0.005734 | no |
| CPU used (cores), mean | 1.58 | 1.569 | -0.7% | -0.04806 to +0.02656 | no |
| Omni's own CPU (cores), mean | 0 | 0.01712 | +0.0171 (native is 0) | +0.01567 to +0.01857 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.58 | 1.586 | +0.4% | -0.03135 to +0.04408 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418 | 407.9 | -2.4% | -27.62 to +7.559 | no |
| HPA replicas, mean | 2.285 | 2.387 | +4.5% | -0.3128 to +0.5171 | no |
| pods started | 0 | 0.9 | +0.9 (native is 0) | +0.6738 to +1.126 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | +0.694 to +1.506 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.1 (native is 0) | +0.694 to +1.506 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.73 | 45.25 | +1.2% | +0.1994 to +0.8441 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 612.1 | 612.6 | +0.1% | -3.363 to +4.363 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.633 | -6.1% | -0.8112 to +0.07791 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*