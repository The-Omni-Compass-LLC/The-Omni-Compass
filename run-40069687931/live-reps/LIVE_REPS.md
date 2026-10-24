# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.794 |
| node-hours | 2.512 | 2.012 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 232.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 235.2 | 207.8 |
| response time (ms), 95th percentile | 707.6 | 766 |
| response time (ms), 99th percentile | 1031 | 1130 |
| time over the response line (% of samples) | 9.091 | 9.588 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.303 | 8.093 |
| utilisation (used / allocatable) | 0.05377 | 0.06702 |
| CPU used (cores), mean | 1.291 | 1.268 |
| Omni's own CPU (cores), mean | 0 | 0.01722 |
| CPU used with Omni's own (cores), mean | 1.291 | 1.286 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.4 | 438 |
| HPA replicas, mean | 1.922 | 2.217 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.3 | 0.4 |
| pod start wait, mean (s) | 0.3 | 0.4 |
| host CPU busy, the real machine under kind (%) | 37.86 | 38.72 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 746.4 | 750 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.898 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.175 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 52.08 | 54.86 |
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
| worker nodes in service, mean | 6 | 4.794 | −20.1% | −1.9685 to −0.4432 | yes: GAIN |
| node-hours | 2.512 | 2.012 | −19.9% | −0.8255 to −0.1739 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.2 | +0.2% | −0.7328 to +1.5534 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 232.3 | −13.9% | −62.3048 to −12.6788 | yes: GAIN |
| response time (ms), mean | 235.2 | 207.8 | −11.7% | −36.1953 to −18.6384 | yes: GAIN |
| response time (ms), 95th percentile | 707.6 | 766 | +8.2% | −0.5340 to +117.2090 | no |
| response time (ms), 99th percentile | 1031 | 1130 | +9.7% | −77.3754 to +276.4576 | no |
| time over the response line (% of samples) | 9.091 | 9.588 | +5.5% | −0.1569 to +1.1514 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 6.4 | +30.6% | −0.8179 to +3.8179 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.8 | +59.800 (native is 0) | +38.1094 to +81.4906 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.303 | 8.093 | +10.8% | −0.5887 to +2.1687 | no |
| utilisation (used / allocatable) | 0.05377 | 0.06702 | +24.6% | +0.0047 to +0.0218 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.291 | 1.268 | −1.7% | −0.0688 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.01722 | +0.017 (native is 0) | +0.0158 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.291 | 1.286 | −0.4% | −0.0525 to +0.0428 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.4 | 438 | −14.0% | −118.5127 to −24.4015 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.217 | +15.4% | +0.0902 to +0.5005 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.8204 to +1.0204 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.8204 to +1.0204 | no |
| host CPU busy, the real machine under kind (%) | 37.86 | 38.72 | +2.3% | +0.5459 to +1.1756 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.4 | 750 | +0.5% | +0.3273 to +6.8727 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.898 | −35.0% | −3.3626 to −0.8419 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.175 | +27.3% | −0.0195 to +0.0945 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 52.08 | 54.86 | +5.3% | −0.3817 to +5.9317 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*