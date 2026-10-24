# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.971 |
| node-hours | 4.156 | 4.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.3 | 444.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 442.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 155.7 | 90.02 |
| response time (ms), 95th percentile | 304.8 | 113 |
| response time (ms), 99th percentile | 615.6 | 278.3 |
| time over the response line (% of samples) | 2.922 | 1.771 |
| failed requests (%) | 1.52 | 1.338 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6917 | 0.5467 |
| utilisation (used / allocatable) | 0.04795 | 0.0466 |
| CPU used (cores), mean | 1.145 | 1.113 |
| Omni's own CPU (cores), mean | 0 | 0.00783 |
| CPU used with Omni's own (cores), mean | 1.145 | 1.121 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 583.5 | 598.1 |
| HPA replicas, mean | 8.478 | 8.72 |
| pods started | 8.9 | 10.6 |
| pod start wait, total (s) | 13.2 | 19.7 |
| pod start wait, mean (s) | 1.502 | 1.854 |
| host CPU busy, the real machine under kind (%) | 34.46 | 33.78 |
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
| worker nodes in service, mean | 5.97 | 5.971 | +0.0% | −0.0007 to +0.0022 | no |
| node-hours | 4.156 | 4.161 | +0.1% | +0.0007 to +0.0099 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 444.3 | 444.1 | −0.1% | −0.8592 to +0.3848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 442.5 | −0.0% | −0.8241 to +0.4205 | no |
| response time (ms), mean | 155.7 | 90.02 | −42.2% | −78.1967 to −53.1915 | yes: GAIN |
| response time (ms), 95th percentile | 304.8 | 113 | −62.9% | −226.0351 to −157.6089 | yes: GAIN |
| response time (ms), 99th percentile | 615.6 | 278.3 | −54.8% | −464.6700 to −209.8768 | yes: GAIN |
| time over the response line (% of samples) | 2.922 | 1.771 | −39.4% | −1.5595 to −0.7418 | yes: GAIN |
| failed requests (%) | 1.52 | 1.338 | −11.9% | −0.3402 to −0.0226 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.8 | −20.9% | −2.7417 to −0.8583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.6 | +51.600 (native is 0) | +42.6837 to +60.5163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6917 | 0.5467 | −21.0% | −0.8075 to +0.5175 | no |
| utilisation (used / allocatable) | 0.04795 | 0.0466 | −2.8% | −0.0021 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.145 | 1.113 | −2.8% | −0.0490 to −0.0155 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00783 | +0.008 (native is 0) | +0.0065 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.145 | 1.121 | −2.1% | −0.0406 to −0.0082 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 583.5 | 598.1 | +2.5% | +0.4299 to +28.7517 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.478 | 8.72 | +2.9% | −0.7108 to +1.1945 | no |
| pods started | 8.9 | 10.6 | +19.1% | −0.6374 to +4.0374 | no |
| pod start wait, total (s) | 13.2 | 19.7 | +49.2% | +1.9980 to +11.0020 | yes: LOSS |
| pod start wait, mean (s) | 1.502 | 1.854 | +23.5% | +0.0346 to +0.6708 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 34.46 | 33.78 | −2.0% | −1.1371 to −0.2285 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 76 | 3.9 |  |
| machine down | omni | 36 | 1.2 | -40 s (-53%) |
| spike | native | 257 | 58.3 |  |
| spike | omni | 239 | 54.7 | -17 s (-7%) |
| runaway pod started | native | 4 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -1 s (-31%) |
| probe blind | native | 64 | 0.7 |  |
| probe blind | omni | 54 | 0.0 | -10 s (-16%) |
| api frozen | native | 8 | 0.2 |  |
| api frozen | omni | 3 | 0.0 | -5 s (-61%) |
| metrics down | native | 3 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-37%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*