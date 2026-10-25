# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.954 |
| node-hours | 2.511 | 2.494 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 269.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 121.3 | 88.37 |
| response time (ms), 95th percentile | 210.5 | 187.9 |
| response time (ms), 99th percentile | 308.6 | 286.8 |
| time over the response line (% of samples) | 0.1147 | 0.09622 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 955 | 950.5 |
| utilisation (used / allocatable) | 0.05827 | 0.05893 |
| CPU used (cores), mean | 1.399 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0.01158 |
| CPU used with Omni's own (cores), mean | 1.399 | 1.416 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.9 | 460.1 |
| HPA replicas, mean | 2.022 | 1.97 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.88 | 43.2 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1380 | 1382 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.533 |
| queue: job wait, submitted to its first pod running, mean (s) | 113.5 | 119.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 540.3 | 542.7 |
| queue: job turnaround, submitted to done, mean (s) | 742.5 | 730.6 |
| queue: jobs unfinished at the window's end | 8.3 | 6.5 |

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
| worker nodes in service, mean | 6 | 5.954 | −0.8% | −0.1152 to +0.0233 | no |
| node-hours | 2.511 | 2.494 | −0.7% | −0.0497 to +0.0166 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.3 | +0.1% | −1.4687 to +1.8591 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 269.9 | −0.5% | −4.4207 to +1.9278 | no |
| response time (ms), mean | 121.3 | 88.37 | −27.2% | −37.6631 to −28.2748 | yes: GAIN |
| response time (ms), 95th percentile | 210.5 | 187.9 | −10.7% | −35.0514 to −10.1306 | yes: GAIN |
| response time (ms), 99th percentile | 308.6 | 286.8 | −7.0% | −49.6709 to +6.1605 | no |
| time over the response line (% of samples) | 0.1147 | 0.09622 | −16.1% | −0.0681 to +0.0312 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.1 | +13.100 (native is 0) | +11.0642 to +15.1358 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 955 | 950.5 | −0.5% | −86.1772 to +77.1772 | no |
| utilisation (used / allocatable) | 0.05827 | 0.05893 | +1.1% | −0.0010 to +0.0023 | no |
| CPU used (cores), mean | 1.399 | 1.404 | +0.4% | −0.0373 to +0.0480 | no |
| Omni's own CPU (cores), mean | 0 | 0.01158 | +0.012 (native is 0) | +0.0107 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.416 | +1.2% | −0.0258 to +0.0598 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.9 | 460.1 | −0.8% | −14.9420 to +7.3273 | no |
| HPA replicas, mean | 2.022 | 1.97 | −2.6% | −0.2095 to +0.1047 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 42.88 | 43.2 | +0.7% | −0.9609 to +1.6008 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1380 | 1382 | +0.2% | −60.3743 to +65.5743 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.533 | −7.8% | −1.3265 to +0.3917 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 113.5 | 119.2 | +5.1% | −29.9259 to +41.4426 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 540.3 | 542.7 | +0.4% | −98.9776 to +103.7776 | no |
| queue: job turnaround, submitted to done, mean (s) | 742.5 | 730.6 | −1.6% | −86.9163 to +63.1663 | no |
| queue: jobs unfinished at the window's end | 8.3 | 6.5 | −21.7% | −4.3413 to +0.7413 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*