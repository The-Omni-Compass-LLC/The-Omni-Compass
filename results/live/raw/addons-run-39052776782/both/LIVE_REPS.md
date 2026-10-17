# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 162.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 162.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.8 | 95.5 |
| response time (ms), 95th percentile | 315.6 | 148.4 |
| response time (ms), 99th percentile | 460 | 189.8 |
| time over the response line (% of samples) | 0.6817 | 0.02439 |
| failed requests (%) | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.1617 |
| utilisation (used / allocatable) | 0.03825 | 0.05154 |
| CPU used (cores), mean | 0.918 | 1.237 |
| Omni's own CPU (cores), mean | 0 | 0.0134 |
| CPU used with Omni's own (cores), mean | 0.918 | 1.25 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 687 | 519.7 |
| HPA replicas, mean | 8.915 | 9.135 |
| pods started | 4.8 | 4.7 |
| pod start wait, total (s) | 13.4 | 12.7 |
| pod start wait, mean (s) | 2.655 | 2.625 |
| host CPU busy, the real machine under kind (%) | 28.13 | 37.73 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.52 | 1.518 | -0.2% | -0.009659 to +0.004659 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 162.4 | +1.7% | +2.062 to +3.435 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 162.4 | +1.7% | +2.062 to +3.435 | yes: power given |
| response time (ms), mean | 157.8 | 95.5 | -39.5% | -67.26 to -57.32 | yes: GAIN |
| response time (ms), 95th percentile | 315.6 | 148.4 | -53.0% | -179.7 to -154.8 | yes: GAIN |
| response time (ms), 99th percentile | 460 | 189.8 | -58.7% | -297.1 to -243.2 | yes: GAIN |
| time over the response line (% of samples) | 0.6817 | 0.02439 | -96.4% | -0.9394 to -0.3751 | yes: GAIN |
| failed requests (%) | 0 | 0.01235 | +0.0123 (native is 0) | -0.01558 to +0.04027 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.7 (native is 0) | +16.74 to +18.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.1617 | -59.4% | -0.5148 to +0.04144 | no |
| utilisation (used / allocatable) | 0.03825 | 0.05154 | +34.7% | +0.01245 to +0.01413 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.918 | 1.237 | +34.7% | +0.2988 to +0.3391 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0134 | +0.0134 (native is 0) | +0.01244 to +0.01436 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.918 | 1.25 | +36.2% | +0.3116 to +0.3531 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 687 | 519.7 | -24.4% | -175.5 to -159.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.915 | 9.135 | +2.5% | +0.08314 to +0.3566 | yes: power given |
| pods started | 4.8 | 4.7 | -2.1% | -0.7263 to +0.5263 | no |
| pod start wait, total (s) | 13.4 | 12.7 | -5.2% | -6.272 to +4.872 | no |
| pod start wait, mean (s) | 2.655 | 2.625 | -1.1% | -0.8834 to +0.8234 | no |
| host CPU busy, the real machine under kind (%) | 28.13 | 37.73 | +34.1% | +8.962 to +10.25 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*