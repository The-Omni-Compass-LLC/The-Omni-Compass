# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.312 |
| node-hours | 2.515 | 2.226 |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 252.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 559.6 | 499.6 |
| response time (ms), 95th percentile | 3320 | 3394 |
| response time (ms), 99th percentile | 4901 | 5053 |
| time over the response line (% of samples) | 16.25 | 15.42 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.2 | 196.8 |
| utilisation (used / allocatable) | 0.06401 | 0.07269 |
| CPU used (cores), mean | 1.536 | 1.537 |
| Omni's own CPU (cores), mean | 0 | 0.02086 |
| CPU used with Omni's own (cores), mean | 1.536 | 1.558 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.3 | 393.7 |
| HPA replicas, mean | 2.315 | 2.241 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 4.8 | 7.1 |
| pod start wait, mean (s) | 4.8 | 3.85 |
| host CPU busy, the real machine under kind (%) | 44.06 | 44.67 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 604 | 604.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.883 |

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
| worker nodes in service, mean | 6 | 5.312 | -11.5% | -1.147 to -0.2281 | yes: GAIN |
| node-hours | 2.515 | 2.226 | -11.5% | -0.4792 to -0.098 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.2 | +0.1% | -0.9345 to +1.26 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 252.6 | -7.8% | -36.12 to -6.801 | yes: GAIN |
| response time (ms), mean | 559.6 | 499.6 | -10.7% | -71.62 to -48.45 | yes: GAIN |
| response time (ms), 95th percentile | 3320 | 3394 | +2.2% | -33.37 to +182.1 | no |
| response time (ms), 99th percentile | 4901 | 5053 | +3.1% | -64.61 to +369.7 | no |
| time over the response line (% of samples) | 16.25 | 15.42 | -5.1% | -1.443 to -0.2267 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.6 (native is 0) | +11.1 to +12.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.2 | 196.8 | +0.3% | -2.912 to +4.182 | no |
| utilisation (used / allocatable) | 0.06401 | 0.07269 | +13.6% | +0.003674 to +0.01369 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.536 | 1.537 | +0.1% | -0.02485 to +0.02701 | no |
| Omni's own CPU (cores), mean | 0 | 0.02086 | +0.0209 (native is 0) | +0.01601 to +0.02571 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.536 | 1.558 | +1.4% | -0.004754 to +0.04864 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.3 | 393.7 | -8.3% | -57.96 to -13.25 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.315 | 2.241 | -3.2% | -0.4269 to +0.2782 | no |
| pods started | 0.1 | 0.6 | +500.0% | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 4.8 | 7.1 | +47.9% | -16.9 to +21.5 | no |
| pod start wait, mean (s) | 4.8 | 3.85 | -19.8% | -14.77 to +12.87 | no |
| host CPU busy, the real machine under kind (%) | 44.06 | 44.67 | +1.4% | +0.2637 to +0.9463 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 604 | 604.6 | +0.1% | -3.876 to +5.076 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.883 | -18.6% | -1.817 to -0.4176 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*