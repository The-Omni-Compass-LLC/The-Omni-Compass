# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.747 |
| node-hours | 2.511 | 1.991 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 232 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 444.6 | 393.5 |
| response time (ms), 95th percentile | 2692 | 2696 |
| response time (ms), 99th percentile | 4246 | 4217 |
| time over the response line (% of samples) | 14.53 | 13.72 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.1 | 172.1 |
| utilisation (used / allocatable) | 0.05715 | 0.07091 |
| CPU used (cores), mean | 1.372 | 1.338 |
| Omni's own CPU (cores), mean | 0 | 0.01718 |
| CPU used with Omni's own (cores), mean | 1.372 | 1.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.8 | 421.3 |
| HPA replicas, mean | 1.958 | 2.125 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 2.2 |
| pod start wait, mean (s) | 0 | 1.2 |
| host CPU busy, the real machine under kind (%) | 39.34 | 39.77 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 531.7 | 531.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.092 |

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
| worker nodes in service, mean | 6 | 4.747 | −20.9% | −1.8073 to −0.6996 | yes: GAIN |
| node-hours | 2.511 | 1.991 | −20.7% | −0.7512 to −0.2886 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.4 | +0.1% | −0.5530 to +1.1025 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 232 | −14.4% | −56.5546 to −21.7294 | yes: GAIN |
| response time (ms), mean | 444.6 | 393.5 | −11.5% | −70.0480 to −32.1278 | yes: GAIN |
| response time (ms), 95th percentile | 2692 | 2696 | +0.1% | −88.6712 to +96.2702 | no |
| response time (ms), 99th percentile | 4246 | 4217 | −0.7% | −218.8243 to +161.6555 | no |
| time over the response line (% of samples) | 14.53 | 13.72 | −5.6% | −1.1783 to −0.4412 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.900 (native is 0) | +10.8100 to +12.9900 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.1 | 172.1 | −1.7% | −9.1052 to +3.0785 | no |
| utilisation (used / allocatable) | 0.05715 | 0.07091 | +24.1% | +0.0073 to +0.0202 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.372 | 1.338 | −2.4% | −0.0656 to −0.0016 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01718 | +0.017 (native is 0) | +0.0146 to +0.0198 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.372 | 1.355 | −1.2% | −0.0467 to +0.0139 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.8 | 421.3 | −14.0% | −111.6057 to −25.4427 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.958 | 2.125 | +8.5% | −0.0533 to +0.3872 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | −2.2963 to +6.6963 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | −1.0570 to +3.4570 | no |
| host CPU busy, the real machine under kind (%) | 39.34 | 39.77 | +1.1% | −0.0607 to +0.9255 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 531.7 | 531.5 | −0.0% | −6.2301 to +5.8301 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.092 | −31.8% | −2.6745 to −1.1410 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*