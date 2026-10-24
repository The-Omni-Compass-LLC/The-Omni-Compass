# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.072 |
| node-hours | 2.52 | 2.122 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 241.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 211.9 | 183.4 |
| response time (ms), 95th percentile | 508.3 | 538.8 |
| response time (ms), 99th percentile | 821.4 | 907.1 |
| time over the response line (% of samples) | 7.401 | 7.61 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.19 | 15.76 |
| utilisation (used / allocatable) | 0.05797 | 0.06824 |
| CPU used (cores), mean | 1.391 | 1.374 |
| Omni's own CPU (cores), mean | 0 | 0.0161 |
| CPU used with Omni's own (cores), mean | 1.391 | 1.39 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.6 | 423.6 |
| HPA replicas, mean | 1.97 | 2.372 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 1.8 |
| pod start wait, mean (s) | 0 | 1.5 |
| host CPU busy, the real machine under kind (%) | 40.21 | 41 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 767.2 | 770.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.407 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6917 | 0.6958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 80.69 | 83.62 |
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
| worker nodes in service, mean | 6 | 5.072 | −15.5% | −1.7149 to −0.1414 | yes: GAIN |
| node-hours | 2.52 | 2.122 | −15.8% | −0.7260 to −0.0686 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271 | −0.4% | −2.0626 to −0.1897 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 241.9 | −11.1% | −55.5829 to −5.0110 | yes: GAIN |
| response time (ms), mean | 211.9 | 183.4 | −13.5% | −41.0808 to −15.9325 | yes: GAIN |
| response time (ms), 95th percentile | 508.3 | 538.8 | +6.0% | −34.7237 to +95.7027 | no |
| response time (ms), 99th percentile | 821.4 | 907.1 | +10.4% | −38.6048 to +210.0154 | no |
| time over the response line (% of samples) | 7.401 | 7.61 | +2.8% | −1.2312 to +1.6484 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.5 | +11.8% | −0.1900 to +1.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 | +27.500 (native is 0) | +17.8957 to +37.1043 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.19 | 15.76 | +29.3% | +1.8998 to +5.2502 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05797 | 0.06824 | +17.7% | +0.0023 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.374 | −1.3% | −0.0805 to +0.0454 | no |
| Omni's own CPU (cores), mean | 0 | 0.0161 | +0.016 (native is 0) | +0.0137 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.39 | −0.1% | −0.0659 to +0.0630 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.6 | 423.6 | −10.7% | −90.9277 to −11.1050 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.372 | +20.4% | +0.1792 to +0.6247 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.2172 to +1.1828 | yes: power given |
| pod start wait, total (s) | 0 | 1.8 | +1.800 (native is 0) | +0.3774 to +3.2226 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | +0.4744 to +2.5256 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.21 | 41 | +2.0% | +0.0245 to +1.5542 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.2 | 770.4 | +0.4% | −1.5424 to +7.9424 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.407 | −26.5% | −2.8486 to −0.3374 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6917 | 0.6958 | +0.6% | −0.1219 to +0.1302 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 | +27.3% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.69 | 83.62 | +3.6% | −3.1148 to +8.9648 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*