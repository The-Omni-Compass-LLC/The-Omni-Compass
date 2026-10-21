# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.332 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.9 | 480.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.9 | 480.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 282.3 | 149.6 |
| response time (ms), 95th percentile | 729.2 | 318.4 |
| response time (ms), 99th percentile | 1389 | 867.5 |
| time over the response line (% of samples) | 13.95 | 3.827 |
| failed requests (%) | 1.499 | 1.224 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.91 |
| utilisation (used / allocatable) | 0.0807 | 0.07831 |
| CPU used (cores), mean | 1.937 | 1.88 |
| Omni's own CPU (cores), mean | 0 | 0.0105 |
| CPU used with Omni's own (cores), mean | 1.937 | 1.89 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 379 | 387.3 |
| HPA replicas, mean | 9.746 | 11.44 |
| pods started | 6.4 | 16.3 |
| pod start wait, total (s) | 10.7 | 31.1 |
| pod start wait, mean (s) | 1.664 | 1.872 |
| host CPU busy, the real machine under kind (%) | 56.07 | 54.92 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.586e-16 to +6.033e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.336 | 4.332 | -0.1% | -0.0132 to +0.00353 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482.9 | 480.8 | -0.4% | -3.067 to -1.093 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.9 | 480.8 | -0.4% | -3.067 to -1.093 | yes: GAIN |
| response time (ms), mean | 282.3 | 149.6 | -47.0% | -176 to -89.41 | yes: GAIN |
| response time (ms), 95th percentile | 729.2 | 318.4 | -56.3% | -532.1 to -289.5 | yes: GAIN |
| response time (ms), 99th percentile | 1389 | 867.5 | -37.5% | -777.3 to -264.7 | yes: GAIN |
| time over the response line (% of samples) | 13.95 | 3.827 | -72.6% | -14.87 to -5.375 | yes: GAIN |
| failed requests (%) | 1.499 | 1.224 | -18.4% | -0.4458 to -0.1044 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.5 | 10.3 | -56.2% | -18.71 to -7.692 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.5 | +66.5 (native is 0) | +46.87 to +86.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.91 | +80.2% | -0.1812 to +0.9912 | no |
| utilisation (used / allocatable) | 0.0807 | 0.07831 | -3.0% | -0.003449 to -0.001333 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.937 | 1.88 | -3.0% | -0.08277 to -0.03198 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0105 | +0.0105 (native is 0) | +0.008554 to +0.01245 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.937 | 1.89 | -2.4% | -0.07085 to -0.0229 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 379 | 387.3 | +2.2% | +4.993 to +11.51 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.746 | 11.44 | +17.4% | +0.2506 to +3.139 | yes: power given |
| pods started | 6.4 | 16.3 | +154.7% | +4.974 to +14.83 | yes: power given |
| pod start wait, total (s) | 10.7 | 31.1 | +190.7% | +9.488 to +31.31 | yes: LOSS |
| pod start wait, mean (s) | 1.664 | 1.872 | +12.4% | -0.04325 to +0.4574 | no |
| host CPU busy, the real machine under kind (%) | 56.07 | 54.92 | -2.1% | -1.734 to -0.575 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*