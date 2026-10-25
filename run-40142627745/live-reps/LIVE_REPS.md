# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.881 |
| node-hours | 2.514 | 2.047 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 235.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 222.5 | 188.7 |
| response time (ms), 95th percentile | 731.8 | 742.4 |
| response time (ms), 99th percentile | 1142 | 1163 |
| time over the response line (% of samples) | 7.745 | 7.627 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.293 | 8.813 |
| utilisation (used / allocatable) | 0.05415 | 0.06756 |
| CPU used (cores), mean | 1.3 | 1.289 |
| Omni's own CPU (cores), mean | 0 | 0.01555 |
| CPU used with Omni's own (cores), mean | 1.3 | 1.304 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.4 | 436.8 |
| HPA replicas, mean | 1.991 | 2.209 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.1 | 0.9 |
| pod start wait, mean (s) | 0.1 | 0.8 |
| host CPU busy, the real machine under kind (%) | 37.3 | 38.25 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 740.8 | 745 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.141 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 50.84 | 53.94 |
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
| worker nodes in service, mean | 6 | 4.881 | −18.6% | −1.8881 to −0.3492 | yes: GAIN |
| node-hours | 2.514 | 2.047 | −18.6% | −0.7892 to −0.1453 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.6 | +0.1% | −0.3891 to +0.8390 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 235.4 | −12.9% | −59.2042 to −10.7333 | yes: GAIN |
| response time (ms), mean | 222.5 | 188.7 | −15.2% | −48.3307 to −19.1979 | yes: GAIN |
| response time (ms), 95th percentile | 731.8 | 742.4 | +1.4% | −71.3628 to +92.5038 | no |
| response time (ms), 99th percentile | 1142 | 1163 | +1.8% | −74.4011 to +116.4043 | no |
| time over the response line (% of samples) | 7.745 | 7.627 | −1.5% | −0.8040 to +0.5675 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.7 | +5.6% | −0.4578 to +1.0578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.900 (native is 0) | +26.9712 to +48.8288 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.293 | 8.813 | −5.2% | −2.7462 to +1.7862 | no |
| utilisation (used / allocatable) | 0.05415 | 0.06756 | +24.8% | +0.0035 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.3 | 1.289 | −0.8% | −0.0398 to +0.0178 | no |
| Omni's own CPU (cores), mean | 0 | 0.01555 | +0.016 (native is 0) | +0.0134 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.3 | 1.304 | +0.4% | −0.0249 to +0.0340 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.4 | 436.8 | −13.4% | −117.5799 to −17.6756 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.991 | 2.209 | +11.0% | +0.0158 to +0.4205 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.3 | 38.25 | +2.5% | +0.5348 to +1.3676 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 740.8 | 745 | +0.6% | −2.0250 to +10.4250 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.141 | −31.0% | −3.0093 to −0.7087 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 | −15.4% | −0.0422 to +0.0255 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | −60.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 50.84 | 53.94 | +6.1% | −3.8494 to +10.0410 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*