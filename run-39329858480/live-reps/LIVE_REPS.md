# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.514 | 1.516 | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.5 | 158.6 | 158.7 | 158.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.5 | 158.6 | 158.7 | 158.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 136.9 | 134 | 134.5 | 133.3 | 73.67 |
| response time (ms), 95th percentile | 299.8 | 292.6 | 292.9 | 294.1 | 109.8 |
| response time (ms), 99th percentile | 472.1 | 472.8 | 468.8 | 472.1 | 150 |
| time over the response line (% of samples) | 1.606 | 1.449 | 1.721 | 1.767 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 1.6 | 1.7 | 1.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1783 | 0.08 | 0.025 | 0.32 |
| utilisation (used / allocatable) | 0.03594 | 0.03591 | 0.03574 | 0.03577 | 0.03451 |
| CPU used (cores), mean | 0.8624 | 0.8619 | 0.8577 | 0.8586 | 0.8282 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00805 |
| CPU used with Omni's own (cores), mean | 0.8624 | 0.8619 | 0.8577 | 0.8586 | 0.8362 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.9 | 794.8 | 799.9 | 796.2 | 813.1 |
| HPA replicas, mean | 8.212 | 8.814 | 9.395 | 9.783 | 8.054 |
| pods started | 5.5 | 4.8 | 3.1 | 1.4 | 4.4 |
| pod start wait, total (s) | 9.4 | 7.7 | 4.6 | 1.9 | 6.9 |
| pod start wait, mean (s) | 1.664 | 1.594 | 1.285 | 0.575 | 1.512 |
| host CPU busy, the real machine under kind (%) | 26.15 | 26.18 | 26.16 | 26.11 | 25.55 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.038e-15 to +3.277e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | -0.007578 to +0.008911 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | -0.2% | -1.161 to +0.6164 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | -0.2% | -1.161 to +0.6164 | no |
| response time (ms), mean | 136.9 | 73.67 | -46.2% | -88.16 to -38.36 | yes: GAIN |
| response time (ms), 95th percentile | 299.8 | 109.8 | -63.4% | -256.1 to -124 | yes: GAIN |
| response time (ms), 99th percentile | 472.1 | 150 | -68.2% | -436.4 to -207.9 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0 | -100.0% | -2.785 to -0.4272 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | -100.0% | -3.223 to -0.3774 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.8 (native is 0) | +16.12 to +19.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.32 | +143.0% | -0.09098 to +0.4676 | no |
| utilisation (used / allocatable) | 0.03594 | 0.03451 | -4.0% | -0.002259 to -0.0005975 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8624 | 0.8282 | -4.0% | -0.05423 to -0.01434 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00805 | +0.00805 (native is 0) | +0.006934 to +0.009166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8624 | 0.8362 | -3.0% | -0.04532 to -0.007148 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 790.9 | 813.1 | +2.8% | +11.59 to +32.7 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.212 | 8.054 | -1.9% | -0.4354 to +0.1196 | no |
| pods started | 5.5 | 4.4 | -20.0% | -1.956 to -0.2436 | yes: GAIN |
| pod start wait, total (s) | 9.4 | 6.9 | -26.6% | -6.592 to +1.592 | no |
| pod start wait, mean (s) | 1.664 | 1.512 | -9.2% | -0.7364 to +0.4311 | no |
| host CPU busy, the real machine under kind (%) | 26.15 | 25.55 | -2.3% | -1.187 to -0.01795 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 299.8 | 472.1 | 8.212 | 0.8624 | 6 |
| Native tuned, HPA target 40 | 292.6 | 472.8 | 8.814 | 0.8619 | 6 |
| Native tuned, HPA target 30 | 292.9 | 468.8 | 9.395 | 0.8577 | 6 |
| Native tuned, HPA target 20 | 294.1 | 472.1 | 9.783 | 0.8586 | 6 |
| omni | 109.8 | 150 | 8.054 | 0.8362 | 6 |

- omni (p95 109.8 ms): no native setting tried reached it; the lowest native p95 is 292.6 ms (Native tuned, HPA target 40).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*