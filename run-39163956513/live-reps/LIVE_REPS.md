# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 501 | 499.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 501 | 499.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 189.3 | 100.4 |
| response time (ms), 95th percentile | 496.9 | 180.2 |
| response time (ms), 99th percentile | 1671 | 693.2 |
| time over the response line (% of samples) | 9.91 | 5.491 |
| failed requests (%) | 5.373 | 4.617 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.59 | 1.002 |
| utilisation (used / allocatable) | 0.07788 | 0.07525 |
| CPU used (cores), mean | 1.869 | 1.806 |
| Omni's own CPU (cores), mean | 0 | 0.0071 |
| CPU used with Omni's own (cores), mean | 1.869 | 1.813 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.5 | 419.3 |
| HPA replicas, mean | 9.334 | 9.302 |
| pods started | 5.6 | 6.8 |
| pod start wait, total (s) | 25 | 28 |
| pod start wait, mean (s) | 3.925 | 3.981 |
| host CPU busy, the real machine under kind (%) | 53.09 | 51.66 |
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
| node-hours | 4.516 | 4.515 | -0.0% | -0.007678 to +0.007011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 501 | 499.2 | -0.4% | -2.684 to -0.875 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 501 | 499.2 | -0.4% | -2.684 to -0.875 | yes: GAIN |
| response time (ms), mean | 189.3 | 100.4 | -46.9% | -129.6 to -48.13 | yes: GAIN |
| response time (ms), 95th percentile | 496.9 | 180.2 | -63.7% | -429.8 to -203.7 | yes: GAIN |
| response time (ms), 99th percentile | 1671 | 693.2 | -58.5% | -1714 to -241.8 | yes: GAIN |
| time over the response line (% of samples) | 9.91 | 5.491 | -44.6% | -7.524 to -1.313 | yes: GAIN |
| failed requests (%) | 5.373 | 4.617 | -14.1% | -1.57 to +0.05816 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16 | 10.7 | -33.1% | -7.512 to -3.088 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 | +31.3 (native is 0) | +21.3 to +41.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.59 | 1.002 | +69.8% | -0.113 to +0.9364 | no |
| utilisation (used / allocatable) | 0.07788 | 0.07525 | -3.4% | -0.003385 to -0.001876 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.869 | 1.806 | -3.4% | -0.08125 to -0.04503 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0071 | +0.0071 (native is 0) | +0.005416 to +0.008784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.869 | 1.813 | -3.0% | -0.07436 to -0.03771 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 402.5 | 419.3 | +4.2% | +7.073 to +26.57 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.334 | 9.302 | -0.3% | -0.916 to +0.8525 | no |
| pods started | 5.6 | 6.8 | +21.4% | -0.445 to +2.845 | no |
| pod start wait, total (s) | 25 | 28 | +12.0% | -0.6317 to +6.632 | no |
| pod start wait, mean (s) | 3.925 | 3.981 | +1.4% | -0.3433 to +0.4545 | no |
| host CPU busy, the real machine under kind (%) | 53.09 | 51.66 | -2.7% | -2.077 to -0.7833 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*