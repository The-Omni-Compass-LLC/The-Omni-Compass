# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.184 |
| node-hours | 2.515 | 2.172 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 247.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 497.7 | 440.8 |
| response time (ms), 95th percentile | 2973 | 2917 |
| response time (ms), 99th percentile | 4441 | 4417 |
| time over the response line (% of samples) | 15.6 | 15.11 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 185.1 | 186 |
| utilisation (used / allocatable) | 0.06073 | 0.06948 |
| CPU used (cores), mean | 1.457 | 1.438 |
| Omni's own CPU (cores), mean | 0 | 0.02075 |
| CPU used with Omni's own (cores), mean | 1.457 | 1.459 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.6 | 414 |
| HPA replicas, mean | 2.082 | 2.267 |
| pods started | 0 | 0.5 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.82 | 42.6 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 565.3 | 569.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.768 |

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
| worker nodes in service, mean | 6 | 5.184 | -13.6% | -1.373 to -0.2595 | yes: GAIN |
| node-hours | 2.515 | 2.172 | -13.6% | -0.57 to -0.1159 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 | +0.0% | -0.9222 to +1.148 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 247.1 | -9.4% | -42.23 to -8.889 | yes: GAIN |
| response time (ms), mean | 497.7 | 440.8 | -11.4% | -76.4 to -37.45 | yes: GAIN |
| response time (ms), 95th percentile | 2973 | 2917 | -1.9% | -155 to +42.76 | no |
| response time (ms), 99th percentile | 4441 | 4417 | -0.5% | -211.1 to +162.6 | no |
| time over the response line (% of samples) | 15.6 | 15.11 | -3.1% | -1.028 to +0.04745 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.6 (native is 0) | +11.58 to +13.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 185.1 | 186 | +0.5% | -3.008 to +4.818 | no |
| utilisation (used / allocatable) | 0.06073 | 0.06948 | +14.4% | +0.001629 to +0.01589 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.457 | 1.438 | -1.3% | -0.06305 to +0.02396 | no |
| Omni's own CPU (cores), mean | 0 | 0.02075 | +0.0208 (native is 0) | +0.01721 to +0.02429 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.459 | +0.1% | -0.0422 to +0.0446 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.6 | 414 | -9.1% | -77.53 to -5.635 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.082 | 2.267 | +8.9% | -0.06298 to +0.4339 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.82 | 42.6 | +1.9% | +0.4435 to +1.124 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 565.3 | 569.5 | +0.7% | -0.9005 to +9.301 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.768 | -20.5% | -2.041 to -0.4216 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*