# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.7 | 155 |
| response time (ms), 95th percentile | 796.8 | 341 |
| response time (ms), 99th percentile | 1534 | 806 |
| time over the response line (% of samples) | 15.81 | 4.127 |
| failed requests (%) | 1.495 | 1.266 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.6 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4783 | 0.7117 |
| utilisation (used / allocatable) | 0.08503 | 0.0823 |
| CPU used (cores), mean | 2.041 | 1.975 |
| Omni's own CPU (cores), mean | 0 | 0.01015 |
| CPU used with Omni's own (cores), mean | 2.041 | 1.985 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 350.8 | 360.6 |
| HPA replicas, mean | 9.79 | 12.06 |
| pods started | 5.7 | 14.8 |
| pod start wait, total (s) | 8.5 | 26.4 |
| pod start wait, mean (s) | 1.506 | 1.767 |
| host CPU busy, the real machine under kind (%) | 58.5 | 57.1 |
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
| node-hours | 4.337 | 4.338 | +0.0% | −0.0086 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.1 | −0.3% | −3.0915 to −0.3006 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.1 | −0.3% | −3.0915 to −0.3006 | yes: GAIN |
| response time (ms), mean | 306.7 | 155 | −49.5% | −189.5712 to −113.8902 | yes: GAIN |
| response time (ms), 95th percentile | 796.8 | 341 | −57.2% | −561.4270 to −350.0720 | yes: GAIN |
| response time (ms), 99th percentile | 1534 | 806 | −47.4% | −1017.0802 to −438.3720 | yes: GAIN |
| time over the response line (% of samples) | 15.81 | 4.127 | −73.9% | −15.7757 to −7.5914 | yes: GAIN |
| failed requests (%) | 1.495 | 1.266 | −15.3% | −0.3576 to −0.0999 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.6 | 10.9 | −59.0% | −20.5285 to −10.8715 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.9 | +63.900 (native is 0) | +47.3173 to +80.4827 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4783 | 0.7117 | +48.8% | +0.0385 to +0.4282 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08503 | 0.0823 | −3.2% | −0.0039 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.041 | 1.975 | −3.2% | −0.0926 to −0.0386 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01015 | +0.010 (native is 0) | +0.0084 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.041 | 1.985 | −2.7% | −0.0821 to −0.0289 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 350.8 | 360.6 | +2.8% | +6.3539 to +13.3259 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.79 | 12.06 | +23.2% | +0.7186 to +3.8304 | yes: power given |
| pods started | 5.7 | 14.8 | +159.6% | +6.0755 to +12.1245 | yes: power given |
| pod start wait, total (s) | 8.5 | 26.4 | +210.6% | +11.7889 to +24.0111 | yes: LOSS |
| pod start wait, mean (s) | 1.506 | 1.767 | +17.3% | −0.1224 to +0.6437 | no |
| host CPU busy, the real machine under kind (%) | 58.5 | 57.1 | −2.4% | −1.9518 to −0.8331 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*