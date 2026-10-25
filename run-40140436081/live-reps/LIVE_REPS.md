# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.18 |
| node-hours | 2.52 | 2.167 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 245.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 304.1 | 288.5 |
| response time (ms), 95th percentile | 1172 | 1309 |
| response time (ms), 99th percentile | 1942 | 2103 |
| time over the response line (% of samples) | 10.88 | 11.47 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.41 | 16.32 |
| utilisation (used / allocatable) | 0.05709 | 0.06765 |
| CPU used (cores), mean | 1.37 | 1.371 |
| Omni's own CPU (cores), mean | 0 | 0.01793 |
| CPU used with Omni's own (cores), mean | 1.37 | 1.389 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 428.5 |
| HPA replicas, mean | 2.115 | 2.232 |
| pods started | 0.4 | 0.5 |
| pod start wait, total (s) | 0.7 | 0.8 |
| pod start wait, mean (s) | 0.55 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.39 | 42.3 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 777.5 | 780.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.644 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.8042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 86.6 | 90.01 |
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
| worker nodes in service, mean | 6 | 5.18 | −13.7% | −1.6041 to −0.0357 | yes: GAIN |
| node-hours | 2.52 | 2.167 | −14.0% | −0.6773 to −0.0292 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.1 | −0.3% | −1.6253 to −0.2068 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 245.3 | −9.8% | −50.8893 to −2.5304 | yes: GAIN |
| response time (ms), mean | 304.1 | 288.5 | −5.1% | −45.8960 to +14.6514 | no |
| response time (ms), 95th percentile | 1172 | 1309 | +11.7% | −47.7857 to +321.3267 | no |
| response time (ms), 99th percentile | 1942 | 2103 | +8.3% | −51.6805 to +372.4637 | no |
| time over the response line (% of samples) | 10.88 | 11.47 | +5.3% | −0.8138 to +1.9781 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.5 | +7.1% | −0.2726 to +1.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 | +39.700 (native is 0) | +25.8500 to +53.5500 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.41 | 16.32 | +13.3% | −0.5166 to +4.3432 | no |
| utilisation (used / allocatable) | 0.05709 | 0.06765 | +18.5% | +0.0006 to +0.0205 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.37 | 1.371 | +0.1% | −0.0287 to +0.0307 | no |
| Omni's own CPU (cores), mean | 0 | 0.01793 | +0.018 (native is 0) | +0.0159 to +0.0200 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.37 | 1.389 | +1.4% | −0.0112 to +0.0491 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 428.5 | −10.8% | −99.2828 to −4.3077 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.115 | 2.232 | +5.5% | −0.0953 to +0.3283 | no |
| pods started | 0.4 | 0.5 | +25.0% | −0.6872 to +0.8872 | no |
| pod start wait, total (s) | 0.7 | 0.8 | +14.3% | −1.3086 to +1.5086 | no |
| pod start wait, mean (s) | 0.55 | 0.6 | +9.1% | −0.9104 to +1.0104 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 42.3 | +2.2% | +0.3635 to +1.4450 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.5 | 780.4 | +0.4% | −2.2741 to +8.0741 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.644 | −22.6% | −2.5919 to −0.1194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.8042 | +1.0% | −0.1056 to +0.1223 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.4 | −6.7% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 86.6 | 90.01 | +3.9% | −2.4223 to +9.2307 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*