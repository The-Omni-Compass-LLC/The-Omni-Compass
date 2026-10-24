# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 148.6 | 77.18 |
| response time (ms), 95th percentile | 302.5 | 116.8 |
| response time (ms), 99th percentile | 458.1 | 147 |
| time over the response line (% of samples) | 1.012 | 0.02432 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.3317 |
| utilisation (used / allocatable) | 0.03229 | 0.04675 |
| CPU used (cores), mean | 0.775 | 1.122 |
| Omni's own CPU (cores), mean | 0 | 0.00925 |
| CPU used with Omni's own (cores), mean | 0.775 | 1.131 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.8 | 581.6 |
| HPA replicas, mean | 9.646 | 11.73 |
| pods started | 3.4 | 4.8 |
| pod start wait, total (s) | 5.3 | 8.6 |
| pod start wait, mean (s) | 1.558 | 1.573 |
| host CPU busy, the real machine under kind (%) | 23.62 | 33.18 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.513 | −0.2% | −0.0117 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.8 | +1.9% | +1.6276 to +4.3788 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.8 | +1.9% | +1.6276 to +4.3788 | yes: power given |
| response time (ms), mean | 148.6 | 77.18 | −48.1% | −92.2436 to −50.5799 | yes: GAIN |
| response time (ms), 95th percentile | 302.5 | 116.8 | −61.4% | −225.3889 to −146.1481 | yes: GAIN |
| response time (ms), 99th percentile | 458.1 | 147 | −67.9% | −361.7455 to −260.4395 | yes: GAIN |
| time over the response line (% of samples) | 1.012 | 0.02432 | −97.6% | −1.6419 to −0.3343 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 | −100.0% | −2.0410 to +0.2410 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.7 | +28.700 (native is 0) | +22.6864 to +34.7136 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.3317 | +77.7% | −0.3730 to +0.6630 | no |
| utilisation (used / allocatable) | 0.03229 | 0.04675 | +44.8% | +0.0106 to +0.0184 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.775 | 1.122 | +44.8% | +0.2533 to +0.4408 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00925 | +0.009 (native is 0) | +0.0077 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.775 | 1.131 | +46.0% | +0.2613 to +0.4512 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.8 | 581.6 | −28.6% | −281.8016 to −184.5890 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.646 | 11.73 | +21.7% | +0.8945 to +3.2836 | yes: power given |
| pods started | 3.4 | 4.8 | +41.2% | −0.4221 to +3.2221 | no |
| pod start wait, total (s) | 5.3 | 8.6 | +62.3% | −2.0852 to +8.6852 | no |
| pod start wait, mean (s) | 1.558 | 1.573 | +1.0% | −0.6241 to +0.6541 | no |
| host CPU busy, the real machine under kind (%) | 23.62 | 33.18 | +40.5% | +7.1746 to +11.9386 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*