# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.919 | 5.917 |
| node-hours | 1.5 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.6 | 165.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.1 | 163.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 189.5 | 113.6 |
| response time (ms), 95th percentile | 359.7 | 133.3 |
| response time (ms), 99th percentile | 909.1 | 534.5 |
| time over the response line (% of samples) | 7.859 | 5.665 |
| failed requests (%) | 5.246 | 4.687 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.6967 |
| utilisation (used / allocatable) | 0.072 | 0.07107 |
| CPU used (cores), mean | 1.704 | 1.682 |
| Omni's own CPU (cores), mean | 0 | 0.00972 |
| CPU used with Omni's own (cores), mean | 1.704 | 1.692 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.5 | 390.4 |
| HPA replicas, mean | 8.898 | 10.05 |
| pods started | 4.3 | 6 |
| pod start wait, total (s) | 19.2 | 16.3 |
| pod start wait, mean (s) | 3.563 | 2.713 |
| host CPU busy, the real machine under kind (%) | 48.62 | 48.23 |
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
| worker nodes in service, mean | 5.919 | 5.917 | -0.0% | -0.01126 to +0.006688 | no |
| node-hours | 1.5 | 1.491 | -0.6% | -0.0165 to -0.0004484 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 166.6 | 165.4 | -0.7% | -2.194 to -0.2208 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.1 | 163.9 | -0.8% | -2.118 to -0.3676 | yes: GAIN |
| response time (ms), mean | 189.5 | 113.6 | -40.1% | -91.48 to -60.4 | yes: GAIN |
| response time (ms), 95th percentile | 359.7 | 133.3 | -62.9% | -269.4 to -183.4 | yes: GAIN |
| response time (ms), 99th percentile | 909.1 | 534.5 | -41.2% | -588.2 to -160.8 | yes: GAIN |
| time over the response line (% of samples) | 7.859 | 5.665 | -27.9% | -3.545 to -0.8426 | yes: GAIN |
| failed requests (%) | 5.246 | 4.687 | -10.7% | -1.102 to -0.01765 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.9 | -20.3% | -2.631 to -0.369 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.1 (native is 0) | +24.71 to +33.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.6967 | +101.0% | -0.3461 to +1.046 | no |
| utilisation (used / allocatable) | 0.072 | 0.07107 | -1.3% | -0.002587 to +0.0007335 | no |
| CPU used (cores), mean | 1.704 | 1.682 | -1.3% | -0.05993 to +0.01526 | no |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.00972 (native is 0) | +0.008644 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.704 | 1.692 | -0.7% | -0.04971 to +0.02448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.5 | 390.4 | +0.8% | -4.259 to +10.08 | no |
| HPA replicas, mean | 8.898 | 10.05 | +12.9% | +0.3225 to +1.976 | yes: power given |
| pods started | 4.3 | 6 | +39.5% | +0.4819 to +2.918 | yes: power given |
| pod start wait, total (s) | 19.2 | 16.3 | -15.1% | -22.22 to +16.42 | no |
| pod start wait, mean (s) | 3.563 | 2.713 | -23.9% | -3.967 to +2.266 | no |
| host CPU busy, the real machine under kind (%) | 48.62 | 48.23 | -0.8% | -1.291 to +0.5079 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 68 | 14.2 |  |
| machine down | omni | 47 | 9.6 | -20 s (-30%) |
| spike | native | 261 | 61.6 |  |
| spike | omni | 262 | 59.2 | +1 s (+1%) |
| runaway pod started | native | 106 | 11.0 |  |
| runaway pod started | omni | 88 | 7.4 | -18 s (-17%) |
| probe blind | native | 67 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -7 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*