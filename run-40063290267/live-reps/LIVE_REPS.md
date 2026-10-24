# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.98 |
| node-hours | 2.517 | 2.086 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 239.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 210.8 | 176.7 |
| response time (ms), 95th percentile | 508 | 512.1 |
| response time (ms), 99th percentile | 800.1 | 877.6 |
| time over the response line (% of samples) | 6.858 | 6.927 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.61 | 14.94 |
| utilisation (used / allocatable) | 0.05769 | 0.07095 |
| CPU used (cores), mean | 1.385 | 1.38 |
| Omni's own CPU (cores), mean | 0 | 0.01671 |
| CPU used with Omni's own (cores), mean | 1.385 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.6 | 413.3 |
| HPA replicas, mean | 2.021 | 2.34 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.5 | 1 |
| pod start wait, mean (s) | 0.5 | 1 |
| host CPU busy, the real machine under kind (%) | 40.11 | 41.2 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 764.2 | 767.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.331 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7208 | 0.6792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 77.21 | 80.06 |
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
| worker nodes in service, mean | 6 | 4.98 | −17.0% | −1.8961 to −0.1434 | yes: GAIN |
| node-hours | 2.517 | 2.086 | −17.1% | −0.7985 to −0.0647 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.5 | −0.1% | −1.3449 to +0.7932 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 239.5 | −11.9% | −59.8237 to −4.8738 | yes: GAIN |
| response time (ms), mean | 210.8 | 176.7 | −16.2% | −52.7097 to −15.4299 | yes: GAIN |
| response time (ms), 95th percentile | 508 | 512.1 | +0.8% | −86.2222 to +94.4302 | no |
| response time (ms), 99th percentile | 800.1 | 877.6 | +9.7% | −79.0749 to +234.1127 | no |
| time over the response line (% of samples) | 6.858 | 6.927 | +1.0% | −2.4072 to +2.5451 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.5 | +4.2% | −0.7690 to +1.3690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +23.9174 to +47.6826 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.61 | 14.94 | +2.2% | −2.2868 to +2.9368 | no |
| utilisation (used / allocatable) | 0.05769 | 0.07095 | +23.0% | +0.0018 to +0.0247 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.38 | −0.3% | −0.0228 to +0.0145 | no |
| Omni's own CPU (cores), mean | 0 | 0.01671 | +0.017 (native is 0) | +0.0145 to +0.0189 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.397 | +0.9% | −0.0071 to +0.0322 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.6 | 413.3 | −13.5% | −120.3609 to −8.2198 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.34 | +15.8% | +0.0587 to +0.5795 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.5 | 1 | +100.0% | −0.7729 to +1.7729 | no |
| pod start wait, mean (s) | 0.5 | 1 | +100.0% | −0.7729 to +1.7729 | no |
| host CPU busy, the real machine under kind (%) | 40.11 | 41.2 | +2.7% | +0.6083 to +1.5762 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 764.2 | 767.1 | +0.4% | −4.5753 to +10.3753 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.331 | −27.8% | −3.0509 to −0.2878 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7208 | 0.6792 | −5.8% | −0.1410 to +0.0577 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.3 | −7.1% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.21 | 80.06 | +3.7% | −5.7872 to +11.4872 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*