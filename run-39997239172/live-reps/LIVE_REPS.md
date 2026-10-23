# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 169.8 | 170.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.8 | 170.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 382 | 334 |
| response time (ms), 95th percentile | 1592 | 1507 |
| response time (ms), 99th percentile | 4110 | 3776 |
| time over the response line (% of samples) | 16.22 | 15.27 |
| failed requests (%) | 1.853 | 1.781 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.027 | 1.372 |
| utilisation (used / allocatable) | 0.08487 | 0.08406 |
| CPU used (cores), mean | 2.037 | 2.018 |
| Omni's own CPU (cores), mean | 0 | 0.01114 |
| CPU used with Omni's own (cores), mean | 2.037 | 2.029 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.2 | 347.8 |
| HPA replicas, mean | 14.57 | 14.78 |
| pods started | 6.2 | 5.8 |
| pod start wait, total (s) | 10.8 | 12 |
| pod start wait, mean (s) | 1.75 | 1.992 |
| host CPU busy, the real machine under kind (%) | 58.6 | 58.58 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 319 | 331.7 |
| second app: response time (ms), 99th percentile | 1775 | 2259 |
| second app: time over the response line (% of samples) | 10.98 | 10.96 |
| second app: failed requests (%) | 8.427 | 8.394 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.788e-16 to +3.235e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.52 | +0.3% | +0.0009104 to +0.006756 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 169.8 | 170.1 | +0.1% | -0.3987 to +0.8934 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.8 | 170.1 | +0.1% | -0.3987 to +0.8934 | no |
| response time (ms), mean | 382 | 334 | -12.6% | -82.85 to -13.19 | yes: GAIN |
| response time (ms), 95th percentile | 1592 | 1507 | -5.3% | -296.3 to +126.4 | no |
| response time (ms), 99th percentile | 4110 | 3776 | -8.1% | -1174 to +505.1 | no |
| time over the response line (% of samples) | 16.22 | 15.27 | -5.9% | -2.283 to +0.3733 | no |
| failed requests (%) | 1.853 | 1.781 | -3.9% | -0.3484 to +0.2044 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.9 | -3.3% | -0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.1 (native is 0) | +41.27 to +58.93 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.027 | 1.372 | +33.6% | -0.6351 to +1.325 | no |
| utilisation (used / allocatable) | 0.08487 | 0.08406 | -1.0% | -0.002728 to +0.00111 | no |
| CPU used (cores), mean | 2.037 | 2.018 | -1.0% | -0.06547 to +0.02663 | no |
| Omni's own CPU (cores), mean | 0 | 0.01114 | +0.0111 (native is 0) | +0.009994 to +0.01229 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.037 | 2.029 | -0.4% | -0.05459 to +0.03803 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.2 | 347.8 | +1.0% | -6.615 to +13.76 | no |
| HPA replicas, mean | 14.57 | 14.78 | +1.4% | -0.1799 to +0.5981 | no |
| pods started | 6.2 | 5.8 | -6.5% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 10.8 | 12 | +11.1% | -1.755 to +4.155 | no |
| pod start wait, mean (s) | 1.75 | 1.992 | +13.8% | -0.2072 to +0.691 | no |
| host CPU busy, the real machine under kind (%) | 58.6 | 58.58 | -0.0% | -0.7098 to +0.6694 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 319 | 331.7 | +4.0% | -60.83 to +86.2 | no |
| second app: response time (ms), 99th percentile | 1775 | 2259 | +27.3% | -416.5 to +1386 | no |
| second app: time over the response line (% of samples) | 10.98 | 10.96 | -0.2% | -1.099 to +1.046 | no |
| second app: failed requests (%) | 8.427 | 8.394 | -0.4% | -0.4443 to +0.3774 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*