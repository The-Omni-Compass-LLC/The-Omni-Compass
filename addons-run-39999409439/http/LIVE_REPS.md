# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 219.6 | 90.2 |
| response time (ms), 95th percentile | 516.2 | 135.2 |
| response time (ms), 99th percentile | 676.2 | 260.1 |
| time over the response line (% of samples) | 5.607 | 0.2072 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07667 | 0.05333 |
| utilisation (used / allocatable) | 0.03082 | 0.04878 |
| CPU used (cores), mean | 0.7398 | 1.171 |
| Omni's own CPU (cores), mean | 0 | 0.01014 |
| CPU used with Omni's own (cores), mean | 0.7398 | 1.181 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 845.8 | 550.2 |
| HPA replicas, mean | 2.955 | 2.509 |
| pods started | 3 | 2.2 |
| pod start wait, total (s) | 3.6 | 3.2 |
| pod start wait, mean (s) | 1.175 | 1.45 |
| host CPU busy, the real machine under kind (%) | 23.56 | 35.85 |
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
| node-hours | 1.518 | 1.516 | -0.2% | -0.01048 to +0.004812 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.7 | +2.4% | +2.862 to +4.724 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.7 | +2.4% | +2.862 to +4.724 | yes: power given |
| response time (ms), mean | 219.6 | 90.2 | -58.9% | -149.7 to -109.1 | yes: GAIN |
| response time (ms), 95th percentile | 516.2 | 135.2 | -73.8% | -425.2 to -336.7 | yes: GAIN |
| response time (ms), 99th percentile | 676.2 | 260.1 | -61.5% | -468.9 to -363.3 | yes: GAIN |
| time over the response line (% of samples) | 5.607 | 0.2072 | -96.3% | -6.994 to -3.806 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 0.1 | -98.3% | -7.954 to -3.646 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 | +4.2 (native is 0) | +3.898 to +4.502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07667 | 0.05333 | -30.4% | -0.1298 to +0.08318 | no |
| utilisation (used / allocatable) | 0.03082 | 0.04878 | +58.3% | +0.01611 to +0.01981 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7398 | 1.171 | +58.3% | +0.3866 to +0.4754 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01014 | +0.0101 (native is 0) | +0.009119 to +0.01116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7398 | 1.181 | +59.6% | +0.396 to +0.4863 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 845.8 | 550.2 | -34.9% | -312.1 to -279 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.955 | 2.509 | -15.1% | -0.6183 to -0.2745 | yes: GAIN |
| pods started | 3 | 2.2 | -26.7% | -1.364 to -0.2358 | yes: GAIN |
| pod start wait, total (s) | 3.6 | 3.2 | -11.1% | -1.715 to +0.9146 | no |
| pod start wait, mean (s) | 1.175 | 1.45 | +23.4% | +0.03982 to +0.5102 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.56 | 35.85 | +52.1% | +10.9 to +13.67 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*