# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.291 |
| node-hours | 2.514 | 2.218 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 249.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 281.7 | 243.6 |
| response time (ms), 95th percentile | 1016 | 1016 |
| response time (ms), 99th percentile | 1499 | 1563 |
| time over the response line (% of samples) | 12.29 | 11.93 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 10.32 |
| utilisation (used / allocatable) | 0.05728 | 0.06663 |
| CPU used (cores), mean | 1.375 | 1.381 |
| Omni's own CPU (cores), mean | 0 | 0.01622 |
| CPU used with Omni's own (cores), mean | 1.375 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 432.6 |
| HPA replicas, mean | 2.046 | 2.202 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.7 |
| host CPU busy, the real machine under kind (%) | 39.35 | 40.07 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 753.1 | 756.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.788 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 63.81 | 66.33 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.291 | −11.8% | −1.4167 to −0.0008 | yes: GAIN |
| node-hours | 2.514 | 2.218 | −11.8% | −0.5924 to +0.0008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.8 | +0.1% | −0.6195 to +1.2174 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 249.5 | −8.1% | −44.1811 to +0.2331 | no |
| response time (ms), mean | 281.7 | 243.6 | −13.5% | −56.3879 to −19.7769 | yes: GAIN |
| response time (ms), 95th percentile | 1016 | 1016 | −0.0% | −133.6068 to +133.2048 | no |
| response time (ms), 99th percentile | 1499 | 1563 | +4.3% | −96.6123 to +225.5579 | no |
| time over the response line (% of samples) | 12.29 | 11.93 | −3.0% | −1.5574 to +0.8272 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 | +2.5% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.4 | +37.400 (native is 0) | +29.6944 to +45.1056 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.82 | 10.32 | −4.6% | −2.3838 to +1.3838 | no |
| utilisation (used / allocatable) | 0.05728 | 0.06663 | +16.3% | −0.0002 to +0.0189 | no |
| CPU used (cores), mean | 1.375 | 1.381 | +0.5% | −0.0166 to +0.0291 | no |
| Omni's own CPU (cores), mean | 0 | 0.01622 | +0.016 (native is 0) | +0.0139 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.375 | 1.397 | +1.6% | −0.0008 to +0.0457 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 432.6 | −9.6% | −93.9578 to +1.7709 | no |
| HPA replicas, mean | 2.046 | 2.202 | +7.6% | +0.0074 to +0.3044 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.3144 to +1.7144 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.1952 to +1.1952 | no |
| host CPU busy, the real machine under kind (%) | 39.35 | 40.07 | +1.8% | +0.3676 to +1.0735 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.1 | 756.3 | +0.4% | −0.5820 to +6.9820 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.788 | −20.2% | −2.3148 to −0.1094 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | −18.7% | −0.0370 to +0.0120 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.81 | 66.33 | +3.9% | −0.9288 to +5.9622 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*