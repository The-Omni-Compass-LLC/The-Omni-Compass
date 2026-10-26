# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.514 | 1.511 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.7 | 158.5 | 158.3 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.7 | 158.5 | 158.3 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 148.2 | 143.6 | 142.5 | 139.4 | 76.65 |
| response time (ms), 95th percentile | 325 | 310 | 302.3 | 293.5 | 109.1 |
| response time (ms), 99th percentile | 532.9 | 507 | 502.5 | 471.1 | 142.2 |
| time over the response line (% of samples) | 1.894 | 1.669 | 1.618 | 1.409 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 1.6 | 1.7 | 1.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 16.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.05333 | 0.05333 | 0.05333 | 0.08 |
| utilisation (used / allocatable) | 0.03744 | 0.03742 | 0.03749 | 0.03717 | 0.03603 |
| CPU used (cores), mean | 0.8985 | 0.898 | 0.8997 | 0.892 | 0.8646 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00767 |
| CPU used with Omni's own (cores), mean | 0.8985 | 0.898 | 0.8997 | 0.892 | 0.8723 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.6 | 745.9 | 743.9 | 752.4 | 768.8 |
| HPA replicas, mean | 8.512 | 8.991 | 9.429 | 9.88 | 7.818 |
| pods started | 5.4 | 4.4 | 2.7 | 0.7 | 4.1 |
| pod start wait, total (s) | 9 | 6.4 | 4.4 | 1.1 | 6.2 |
| pod start wait, mean (s) | 1.708 | 1.491 | 1.373 | 0.3 | 1.517 |
| host CPU busy, the real machine under kind (%) | 27.18 | 27.06 | 27.12 | 26.81 | 26.32 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| node-hours | 1.513 | 1.51 | −0.2% | −0.0080 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.1 | −0.4% | −1.2055 to −0.1068 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.1 | −0.4% | −1.2055 to −0.1068 | yes: GAIN |
| response time (ms), mean | 148.2 | 76.65 | −48.3% | −95.1595 to −47.8912 | yes: GAIN |
| response time (ms), 95th percentile | 325 | 109.1 | −66.4% | −282.3813 to −149.4317 | yes: GAIN |
| response time (ms), 99th percentile | 532.9 | 142.2 | −73.3% | −514.8740 to −266.4100 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.01212 | −99.4% | −3.1109 to −0.6521 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | −100.0% | −4.3237 to −0.6763 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | +16.900 (native is 0) | +13.5884 to +20.2116 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.08 | −39.2% | −0.1728 to +0.0695 | no |
| utilisation (used / allocatable) | 0.03744 | 0.03603 | −3.8% | −0.0020 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8985 | 0.8646 | −3.8% | −0.0476 to −0.0202 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00767 | +0.008 (native is 0) | +0.0064 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8985 | 0.8723 | −2.9% | −0.0392 to −0.0133 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.6 | 768.8 | +3.8% | +13.8560 to +42.6055 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.512 | 7.818 | −8.1% | −1.4797 to +0.0927 | no |
| pods started | 5.4 | 4.1 | −24.1% | −2.4705 to −0.1295 | yes: GAIN |
| pod start wait, total (s) | 9 | 6.2 | −31.1% | −5.3636 to −0.2364 | yes: GAIN |
| pod start wait, mean (s) | 1.708 | 1.517 | −11.2% | −0.5808 to +0.1975 | no |
| host CPU busy, the real machine under kind (%) | 27.18 | 26.32 | −3.2% | −1.2208 to −0.5063 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 325 | 532.9 | 8.512 | 0.8985 | 6 |
| Native tuned, HPA target 40 | 310 | 507 | 8.991 | 0.898 | 6 |
| Native tuned, HPA target 30 | 302.3 | 502.5 | 9.429 | 0.8997 | 6 |
| Native tuned, HPA target 20 | 293.5 | 471.1 | 9.88 | 0.892 | 6 |
| omni | 109.1 | 142.2 | 7.818 | 0.8723 | 6 |

- omni (p95 109.1 ms): no native setting tried reached it; the lowest native p95 is 293.5 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*