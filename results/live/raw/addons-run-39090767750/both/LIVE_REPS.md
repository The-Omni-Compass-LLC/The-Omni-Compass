# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.523 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 162.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 162.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150.5 | 92.43 |
| response time (ms), 95th percentile | 306.4 | 142.2 |
| response time (ms), 99th percentile | 453.6 | 175.6 |
| time over the response line (% of samples) | 0.7493 | 0.04908 |
| failed requests (%) | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.1067 |
| utilisation (used / allocatable) | 0.03759 | 0.05065 |
| CPU used (cores), mean | 0.9021 | 1.215 |
| Omni's own CPU (cores), mean | 0 | 0.01349 |
| CPU used with Omni's own (cores), mean | 0.9021 | 1.229 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 699 | 531.8 |
| HPA replicas, mean | 8.857 | 9.512 |
| pods started | 4.9 | 5.2 |
| pod start wait, total (s) | 14.4 | 11.8 |
| pod start wait, mean (s) | 2.833 | 2.187 |
| host CPU busy, the real machine under kind (%) | 27.87 | 37.13 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.179e-16 to +1.661e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.523 | 1.52 | -0.2% | -0.008414 to +0.001414 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 162.4 | +1.6% | +1.706 to +3.485 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 162.4 | +1.6% | +1.706 to +3.485 | yes: power given |
| response time (ms), mean | 150.5 | 92.43 | -38.6% | -69.06 to -46.99 | yes: GAIN |
| response time (ms), 95th percentile | 306.4 | 142.2 | -53.6% | -189.7 to -138.5 | yes: GAIN |
| response time (ms), 99th percentile | 453.6 | 175.6 | -61.3% | -331.2 to -224.8 | yes: GAIN |
| time over the response line (% of samples) | 0.7493 | 0.04908 | -93.4% | -1.052 to -0.3485 | yes: GAIN |
| failed requests (%) | 0 | 0.01235 | +0.0123 (native is 0) | -0.01558 to +0.04027 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | -100.0% | -0.7694 to -0.03062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20 (native is 0) | +13.95 to +26.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.1067 | -69.5% | -0.4415 to -0.04518 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03759 | 0.05065 | +34.7% | +0.01083 to +0.01529 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9021 | 1.215 | +34.7% | +0.26 to +0.3668 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01349 | +0.0135 (native is 0) | +0.01144 to +0.01554 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9021 | 1.229 | +36.2% | +0.2723 to +0.3815 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 699 | 531.8 | -23.9% | -187.5 to -146.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.857 | 9.512 | +7.4% | -0.01654 to +1.327 | no |
| pods started | 4.9 | 5.2 | +6.1% | -1.247 to +1.847 | no |
| pod start wait, total (s) | 14.4 | 11.8 | -18.1% | -9.454 to +4.254 | no |
| pod start wait, mean (s) | 2.833 | 2.187 | -22.8% | -1.605 to +0.3129 | no |
| host CPU busy, the real machine under kind (%) | 27.87 | 37.13 | +33.2% | +7.757 to +10.77 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*