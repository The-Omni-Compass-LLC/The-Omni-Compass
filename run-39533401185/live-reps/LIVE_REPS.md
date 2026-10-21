# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.34 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.7 | 479.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.7 | 479.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 267.4 | 137.3 |
| response time (ms), 95th percentile | 698.6 | 284.8 |
| response time (ms), 99th percentile | 1298 | 751.5 |
| time over the response line (% of samples) | 13.05 | 3.218 |
| failed requests (%) | 1.237 | 1.064 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.5 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 1.127 |
| utilisation (used / allocatable) | 0.07763 | 0.07512 |
| CPU used (cores), mean | 1.863 | 1.803 |
| Omni's own CPU (cores), mean | 0 | 0.00994 |
| CPU used with Omni's own (cores), mean | 1.863 | 1.813 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.9 | 404.5 |
| HPA replicas, mean | 9.686 | 10.99 |
| pods started | 6.5 | 16.1 |
| pod start wait, total (s) | 10.3 | 28.6 |
| pod start wait, mean (s) | 1.545 | 1.689 |
| host CPU busy, the real machine under kind (%) | 54.04 | 52.92 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.334 | 4.34 | +0.1% | -0.00245 to +0.01478 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.7 | 479.9 | -0.2% | -1.925 to +0.1526 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.7 | 479.9 | -0.2% | -1.925 to +0.1526 | no |
| response time (ms), mean | 267.4 | 137.3 | -48.6% | -176.4 to -83.67 | yes: GAIN |
| response time (ms), 95th percentile | 698.6 | 284.8 | -59.2% | -545.3 to -282.3 | yes: GAIN |
| response time (ms), 99th percentile | 1298 | 751.5 | -42.1% | -717.9 to -374.1 | yes: GAIN |
| time over the response line (% of samples) | 13.05 | 3.218 | -75.3% | -14.8 to -4.863 | yes: GAIN |
| failed requests (%) | 1.237 | 1.064 | -14.0% | -0.2991 to -0.04618 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.5 | 8.9 | -58.6% | -18.5 to -6.699 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.2 | +61.2 (native is 0) | +39.82 to +82.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 1.127 | +229.8% | +0.2121 to +1.358 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07763 | 0.07512 | -3.2% | -0.003266 to -0.001757 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.863 | 1.803 | -3.2% | -0.07839 to -0.04217 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00994 | +0.00994 (native is 0) | +0.008006 to +0.01187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.863 | 1.813 | -2.7% | -0.06733 to -0.03335 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.9 | 404.5 | +2.9% | +5.724 to +17.36 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.686 | 10.99 | +13.4% | -0.1626 to +2.765 | no |
| pods started | 6.5 | 16.1 | +147.7% | +3.885 to +15.31 | yes: power given |
| pod start wait, total (s) | 10.3 | 28.6 | +177.7% | +4.74 to +31.86 | yes: LOSS |
| pod start wait, mean (s) | 1.545 | 1.689 | +9.3% | -0.2641 to +0.5527 | no |
| host CPU busy, the real machine under kind (%) | 54.04 | 52.92 | -2.1% | -1.616 to -0.622 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*