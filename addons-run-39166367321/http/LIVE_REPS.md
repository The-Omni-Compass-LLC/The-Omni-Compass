# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 192 | 84.94 |
| response time (ms), 95th percentile | 462.8 | 132.7 |
| response time (ms), 99th percentile | 632.1 | 278.7 |
| time over the response line (% of samples) | 4.274 | 0.1957 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.4083 |
| utilisation (used / allocatable) | 0.03142 | 0.04751 |
| CPU used (cores), mean | 0.754 | 1.14 |
| Omni's own CPU (cores), mean | 0 | 0.00956 |
| CPU used with Omni's own (cores), mean | 0.754 | 1.15 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 832.4 | 571.1 |
| HPA replicas, mean | 2.989 | 2.482 |
| pods started | 3 | 2.3 |
| pod start wait, total (s) | 24.5 | 21.7 |
| pod start wait, mean (s) | 8.183 | 9.35 |
| host CPU busy, the real machine under kind (%) | 23.76 | 34.88 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.901e-17 to +1.224e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.511 | -0.5% | -0.01189 to -0.004779 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.1 | +1.8% | +1.799 to +3.918 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.1 | +1.8% | +1.799 to +3.918 | yes: power given |
| response time (ms), mean | 192 | 84.94 | -55.8% | -130.9 to -83.14 | yes: GAIN |
| response time (ms), 95th percentile | 462.8 | 132.7 | -71.3% | -387.9 to -272.3 | yes: GAIN |
| response time (ms), 99th percentile | 632.1 | 278.7 | -55.9% | -427.8 to -279 | yes: GAIN |
| time over the response line (% of samples) | 4.274 | 0.1957 | -95.4% | -6.241 to -1.915 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 0.2 | -95.0% | -6.032 to -1.568 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 | +4.3 (native is 0) | +3.954 to +4.646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.4083 | +26.9% | -0.1192 to +0.2925 | no |
| utilisation (used / allocatable) | 0.03142 | 0.04751 | +51.2% | +0.01294 to +0.01925 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.754 | 1.14 | +51.2% | +0.3105 to +0.4619 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00956 | +0.00956 (native is 0) | +0.008453 to +0.01067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.754 | 1.15 | +52.5% | +0.319 to +0.4725 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 832.4 | 571.1 | -31.4% | -283.5 to -239.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.989 | 2.482 | -16.9% | -0.6424 to -0.3702 | yes: GAIN |
| pods started | 3 | 2.3 | -23.3% | -1.183 to -0.2172 | yes: GAIN |
| pod start wait, total (s) | 24.5 | 21.7 | -11.4% | -7.372 to +1.772 | no |
| pod start wait, mean (s) | 8.183 | 9.35 | +14.3% | +0.1304 to +2.203 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.76 | 34.88 | +46.8% | +8.971 to +13.26 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*