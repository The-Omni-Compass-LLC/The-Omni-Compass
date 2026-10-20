# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.332 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 483.7 | 481.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.7 | 481.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 295.1 | 144.9 |
| response time (ms), 95th percentile | 765.7 | 302.1 |
| response time (ms), 99th percentile | 1519 | 766 |
| time over the response line (% of samples) | 13.9 | 3.339 |
| failed requests (%) | 1.232 | 1.026 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.9 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.76 |
| utilisation (used / allocatable) | 0.08249 | 0.07927 |
| CPU used (cores), mean | 1.98 | 1.903 |
| Omni's own CPU (cores), mean | 0 | 0.00976 |
| CPU used with Omni's own (cores), mean | 1.98 | 1.912 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 358.7 | 369.7 |
| HPA replicas, mean | 9.822 | 11.15 |
| pods started | 5.3 | 16.1 |
| pod start wait, total (s) | 7.6 | 29.6 |
| pod start wait, mean (s) | 1.381 | 1.826 |
| host CPU busy, the real machine under kind (%) | 56.87 | 55.28 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.246e-16 to +1.102e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.332 | 4.333 | +0.0% | -0.00607 to +0.006736 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 483.7 | 481.7 | -0.4% | -3.222 to -0.767 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.7 | 481.7 | -0.4% | -3.222 to -0.767 | yes: GAIN |
| response time (ms), mean | 295.1 | 144.9 | -50.9% | -190.9 to -109.5 | yes: GAIN |
| response time (ms), 95th percentile | 765.7 | 302.1 | -60.6% | -578.8 to -348.5 | yes: GAIN |
| response time (ms), 99th percentile | 1519 | 766 | -49.6% | -957 to -548.2 | yes: GAIN |
| time over the response line (% of samples) | 13.9 | 3.339 | -76.0% | -14.81 to -6.307 | yes: GAIN |
| failed requests (%) | 1.232 | 1.026 | -16.7% | -0.3508 to -0.06096 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.9 | 9.2 | -63.1% | -20.64 to -10.76 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.8 | +64.8 (native is 0) | +51.41 to +78.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.76 | +78.1% | -0.06801 to +0.7347 | no |
| utilisation (used / allocatable) | 0.08249 | 0.07927 | -3.9% | -0.004538 to -0.001901 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.98 | 1.903 | -3.9% | -0.1089 to -0.04562 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00976 | +0.00976 (native is 0) | +0.008164 to +0.01136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.98 | 1.912 | -3.4% | -0.09857 to -0.03645 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 358.7 | 369.7 | +3.1% | +5.305 to +16.75 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.822 | 11.15 | +13.6% | +0.3646 to +2.299 | yes: power given |
| pods started | 5.3 | 16.1 | +203.8% | +6.432 to +15.17 | yes: power given |
| pod start wait, total (s) | 7.6 | 29.6 | +289.5% | +12.93 to +31.07 | yes: LOSS |
| pod start wait, mean (s) | 1.381 | 1.826 | +32.2% | +0.1852 to +0.7051 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.87 | 55.28 | -2.8% | -2.487 to -0.693 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*