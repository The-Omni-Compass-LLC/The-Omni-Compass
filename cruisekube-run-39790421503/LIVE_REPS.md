# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.83 |
| node-hours | 1.514 | 1.471 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 162.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 85.66 | 84.78 |
| response time (ms), 95th percentile | 131.7 | 127.2 |
| response time (ms), 99th percentile | 147.1 | 148.7 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 |
| utilisation (used / allocatable) | 0.04909 | 0.0508 |
| CPU used (cores), mean | 1.178 | 1.175 |
| Omni's own CPU (cores), mean | 0 | 0.03344 |
| CPU used with Omni's own (cores), mean | 1.178 | 1.208 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 553.9 | 543.5 |
| HPA replicas, mean | 2.731 | 2.75 |
| pods started | 1.5 | 1.4 |
| pod start wait, total (s) | 2 | 1.8 |
| pod start wait, mean (s) | 1.3 | 1.25 |
| host CPU busy, the real machine under kind (%) | 36.67 | 37.75 |
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
| worker nodes in service, mean | 6 | 5.83 | -2.8% | -0.4996 to +0.1598 | no |
| node-hours | 1.514 | 1.471 | -2.8% | -0.1234 to +0.03772 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 162.4 | +0.5% | -0.5536 to +2.219 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 159.1 | -1.5% | -8.102 to +3.289 | no |
| response time (ms), mean | 85.66 | 84.78 | -1.0% | -8.664 to +6.904 | no |
| response time (ms), 95th percentile | 131.7 | 127.2 | -3.4% | -23.99 to +15.01 | no |
| response time (ms), 99th percentile | 147.1 | 148.7 | +1.1% | -19.37 to +22.62 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 | +4.1 (native is 0) | +3.874 to +4.326 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 | +200.0% | -0.1548 to +0.3681 | no |
| utilisation (used / allocatable) | 0.04909 | 0.0508 | +3.5% | -0.0003032 to +0.003731 | no |
| CPU used (cores), mean | 1.178 | 1.175 | -0.3% | -0.05192 to +0.04474 | no |
| Omni's own CPU (cores), mean | 0 | 0.03344 | +0.0334 (native is 0) | +0.02937 to +0.03751 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.178 | 1.208 | +2.5% | -0.01662 to +0.07633 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 553.9 | 543.5 | -1.9% | -23.97 to +3.264 | no |
| HPA replicas, mean | 2.731 | 2.75 | +0.7% | -0.239 to +0.2783 | no |
| pods started | 1.5 | 1.4 | -6.7% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 2 | 1.8 | -10.0% | -1.256 to +0.8556 | no |
| pod start wait, mean (s) | 1.3 | 1.25 | -3.8% | -0.5102 to +0.4102 | no |
| host CPU busy, the real machine under kind (%) | 36.67 | 37.75 | +2.9% | -0.07627 to +2.232 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*