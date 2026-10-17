# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 628.2 | 522.1 |
| response time (ms), 95th percentile | 2772 | 2698 |
| response time (ms), 99th percentile | 6547 | 6282 |
| time over the response line (% of samples) | 29.48 | 25.16 |
| failed requests (%) | 4.964 | 5.159 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.04 | 1.185 |
| utilisation (used / allocatable) | 0.1055 | 0.1045 |
| CPU used (cores), mean | 2.532 | 2.507 |
| Omni's own CPU (cores), mean | 0 | 0.01157 |
| CPU used with Omni's own (cores), mean | 2.532 | 2.519 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 276.2 |
| HPA replicas, mean | 15.49 | 15.77 |
| pods started | 4 | 2.2 |
| pod start wait, total (s) | 7 | 4.4 |
| pod start wait, mean (s) | 1.597 | 1.708 |
| host CPU busy, the real machine under kind (%) | 73.76 | 73.82 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 226 | 239.4 |
| second app: response time (ms), 99th percentile | 1178 | 889.6 |
| second app: time over the response line (% of samples) | 16.65 | 16.67 |
| second app: failed requests (%) | 15.69 | 15.88 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.147e-15 to +8.087e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.0% | -0.002555 to +0.002888 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.4 | -0.1% | -0.5493 to +0.2387 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.4 | -0.1% | -0.5493 to +0.2387 | no |
| response time (ms), mean | 628.2 | 522.1 | -16.9% | -165.4 to -46.76 | yes: GAIN |
| response time (ms), 95th percentile | 2772 | 2698 | -2.6% | -537 to +390.2 | no |
| response time (ms), 99th percentile | 6547 | 6282 | -4.0% | -1229 to +699.1 | no |
| time over the response line (% of samples) | 29.48 | 25.16 | -14.7% | -5.981 to -2.67 | yes: GAIN |
| failed requests (%) | 4.964 | 5.159 | +3.9% | -1.005 to +1.394 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 9.6 | -5.0% | -1.006 to +0.005799 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.2 (native is 0) | +29.75 to +34.65 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.04 | 1.185 | +13.9% | -0.7504 to +1.04 | no |
| utilisation (used / allocatable) | 0.1055 | 0.1045 | -1.0% | -0.001731 to -0.0003144 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.532 | 2.507 | -1.0% | -0.04154 to -0.007545 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01157 | +0.0116 (native is 0) | +0.01081 to +0.01233 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.532 | 2.519 | -0.5% | -0.03012 to +0.004171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 276.2 | +0.9% | +0.8173 to +4.22 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.49 | 15.77 | +1.8% | -0.08883 to +0.6377 | no |
| pods started | 4 | 2.2 | -45.0% | -3.053 to -0.5474 | yes: GAIN |
| pod start wait, total (s) | 7 | 4.4 | -37.1% | -5.924 to +0.7244 | no |
| pod start wait, mean (s) | 1.597 | 1.708 | +7.0% | -0.5544 to +0.7777 | no |
| host CPU busy, the real machine under kind (%) | 73.76 | 73.82 | +0.1% | -0.4648 to +0.6011 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 226 | 239.4 | +5.9% | -6.813 to +33.46 | no |
| second app: response time (ms), 99th percentile | 1178 | 889.6 | -24.5% | -1418 to +842.6 | no |
| second app: time over the response line (% of samples) | 16.65 | 16.67 | +0.1% | -0.5847 to +0.6302 | no |
| second app: failed requests (%) | 15.69 | 15.88 | +1.2% | -0.293 to +0.6726 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*