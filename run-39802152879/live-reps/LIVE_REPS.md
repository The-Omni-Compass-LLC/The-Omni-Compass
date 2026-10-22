# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 156.8 | 81.81 |
| response time (ms), 95th percentile | 351.7 | 121.7 |
| response time (ms), 99th percentile | 593.1 | 173.5 |
| time over the response line (% of samples) | 2.466 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.2917 |
| utilisation (used / allocatable) | 0.03952 | 0.03812 |
| CPU used (cores), mean | 0.9484 | 0.9148 |
| Omni's own CPU (cores), mean | 0 | 0.02596 |
| CPU used with Omni's own (cores), mean | 0.9484 | 0.9407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.6 | 751.9 |
| HPA replicas, mean | 8.369 | 9.109 |
| pods started | 5 | 3.9 |
| pod start wait, total (s) | 7.2 | 5.1 |
| pod start wait, mean (s) | 1.416 | 1.338 |
| host CPU busy, the real machine under kind (%) | 28.83 | 28.92 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.518 | +0.2% | -0.002271 to +0.009271 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.4 | +0.0% | -0.5719 to +0.6726 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.4 | +0.0% | -0.5719 to +0.6726 | no |
| response time (ms), mean | 156.8 | 81.81 | -47.8% | -102.4 to -47.65 | yes: GAIN |
| response time (ms), 95th percentile | 351.7 | 121.7 | -65.4% | -304.9 to -155.2 | yes: GAIN |
| response time (ms), 99th percentile | 593.1 | 173.5 | -70.8% | -562 to -277.3 | yes: GAIN |
| time over the response line (% of samples) | 2.466 | 0.0122 | -99.5% | -3.701 to -1.206 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | -100.0% | -4.913 to -1.487 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20 (native is 0) | +17.79 to +22.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.2917 | +40.0% | -0.1195 to +0.2861 | no |
| utilisation (used / allocatable) | 0.03952 | 0.03812 | -3.5% | -0.0026 to -0.0002016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9484 | 0.9148 | -3.5% | -0.06241 to -0.004839 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02596 | +0.026 (native is 0) | +0.02207 to +0.02985 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9484 | 0.9407 | -0.8% | -0.03488 to +0.01955 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.6 | 751.9 | +2.5% | +2.166 to +34.48 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.369 | 9.109 | +8.8% | +0.2333 to +1.247 | yes: power given |
| pods started | 5 | 3.9 | -22.0% | -2.337 to +0.1367 | no |
| pod start wait, total (s) | 7.2 | 5.1 | -29.2% | -4.588 to +0.3882 | no |
| pod start wait, mean (s) | 1.416 | 1.338 | -5.5% | -0.3781 to +0.2219 | no |
| host CPU busy, the real machine under kind (%) | 28.83 | 28.92 | +0.3% | -0.5758 to +0.7562 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*