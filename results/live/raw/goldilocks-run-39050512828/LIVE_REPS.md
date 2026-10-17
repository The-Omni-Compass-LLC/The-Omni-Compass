# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 172.3 | 88.56 |
| response time (ms), 95th percentile | 359.8 | 140.7 |
| response time (ms), 99th percentile | 520.3 | 175 |
| time over the response line (% of samples) | 1.436 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 |
| utilisation (used / allocatable) | 0.03351 | 0.04994 |
| CPU used (cores), mean | 0.8043 | 1.199 |
| Omni's own CPU (cores), mean | 0 | 0.00846 |
| CPU used with Omni's own (cores), mean | 0.8043 | 1.207 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.8 | 539.3 |
| HPA replicas, mean | 9.798 | 9.886 |
| pods started | 2 | 0.8 |
| pod start wait, total (s) | 3.1 | 1.1 |
| pod start wait, mean (s) | 1.125 | 0.6 |
| host CPU busy, the real machine under kind (%) | 24.16 | 34.93 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.869e-17 to +9.771e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.1% | -0.007393 to +0.009059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.9 | +2.4% | +2.9 to +4.753 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.9 | +2.4% | +2.9 to +4.753 | yes: power given |
| response time (ms), mean | 172.3 | 88.56 | -48.6% | -102.4 to -65.09 | yes: GAIN |
| response time (ms), 95th percentile | 359.8 | 140.7 | -60.9% | -254.5 to -183.7 | yes: GAIN |
| response time (ms), 99th percentile | 520.3 | 175 | -66.4% | -400.5 to -290.2 | yes: GAIN |
| time over the response line (% of samples) | 1.436 | 0 | -100.0% | -2.02 to -0.8518 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 | -100.0% | -2.595 to -0.8047 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.2 | +15.2 (native is 0) | +13.05 to +17.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 | +200.0% | -0.0777 to +0.291 | no |
| utilisation (used / allocatable) | 0.03351 | 0.04994 | +49.0% | +0.01359 to +0.01926 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8043 | 1.199 | +49.0% | +0.3263 to +0.4623 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00846 | +0.00846 (native is 0) | +0.007532 to +0.009388 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8043 | 1.207 | +50.1% | +0.334 to +0.4714 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.8 | 539.3 | -30.9% | -278.3 to -204.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.798 | 9.886 | +0.9% | -0.02801 to +0.204 | no |
| pods started | 2 | 0.8 | -60.0% | -2.256 to -0.1444 | yes: GAIN |
| pod start wait, total (s) | 3.1 | 1.1 | -64.5% | -3.937 to -0.06294 | yes: GAIN |
| pod start wait, mean (s) | 1.125 | 0.6 | -46.7% | -1.326 to +0.2757 | no |
| host CPU busy, the real machine under kind (%) | 24.16 | 34.93 | +44.6% | +8.988 to +12.55 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*