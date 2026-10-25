# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.521 | 1.517 | 1.517 | 1.52 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 160.1 | 160.2 | 160.4 | 159.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.6 | 160.1 | 160.2 | 160.4 | 159.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 171.2 | 170.8 | 170.9 | 168.1 | 86.36 |
| response time (ms), 95th percentile | 380.6 | 380.9 | 382.7 | 371.5 | 131.8 |
| response time (ms), 99th percentile | 619.9 | 619.5 | 647 | 618.6 | 179.5 |
| time over the response line (% of samples) | 2.608 | 2.705 | 2.832 | 2.55 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 2.6 | 3 | 2.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1067 | 0.105 | 0.16 | 0.2117 |
| utilisation (used / allocatable) | 0.04158 | 0.0418 | 0.04212 | 0.04164 | 0.03957 |
| CPU used (cores), mean | 0.998 | 1.003 | 1.011 | 0.9993 | 0.9497 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00873 |
| CPU used with Omni's own (cores), mean | 0.998 | 1.003 | 1.011 | 0.9993 | 0.9584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.8 | 664.7 | 660.6 | 660.7 | 693.5 |
| HPA replicas, mean | 8.624 | 9.098 | 9.632 | 9.929 | 8.561 |
| pods started | 4.8 | 4.1 | 2.3 | 0.4 | 3.2 |
| pod start wait, total (s) | 6.8 | 5 | 3.2 | 0.5 | 4 |
| pod start wait, mean (s) | 1.42 | 1.274 | 1.35 | 0.125 | 1.3 |
| host CPU busy, the real machine under kind (%) | 29.63 | 29.74 | 30.04 | 29.71 | 28.53 |
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
| node-hours | 1.521 | 1.519 | −0.1% | −0.0080 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 159.9 | −0.4% | −1.2688 to −0.0532 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.6 | 159.9 | −0.4% | −1.2688 to −0.0532 | yes: GAIN |
| response time (ms), mean | 171.2 | 86.36 | −49.5% | −103.6120 to −65.9785 | yes: GAIN |
| response time (ms), 95th percentile | 380.6 | 131.8 | −65.4% | −298.5752 to −198.9878 | yes: GAIN |
| response time (ms), 99th percentile | 619.9 | 179.5 | −71.0% | −537.0615 to −343.7369 | yes: GAIN |
| time over the response line (% of samples) | 2.608 | 0.01212 | −99.5% | −3.5313 to −1.6599 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.3060 to −1.6940 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.100 (native is 0) | +14.1134 to +20.0866 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.2117 | +98.4% | −0.1194 to +0.3294 | no |
| utilisation (used / allocatable) | 0.04158 | 0.03957 | −4.8% | −0.0028 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.998 | 0.9497 | −4.8% | −0.0681 to −0.0286 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00873 | +0.009 (native is 0) | +0.0076 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.998 | 0.9584 | −4.0% | −0.0585 to −0.0206 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.8 | 693.5 | +3.9% | +11.6032 to +39.8429 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.624 | 8.561 | −0.7% | −0.4825 to +0.3560 | no |
| pods started | 4.8 | 3.2 | −33.3% | −2.8251 to −0.3749 | yes: GAIN |
| pod start wait, total (s) | 6.8 | 4 | −41.2% | −4.7892 to −0.8108 | yes: GAIN |
| pod start wait, mean (s) | 1.42 | 1.3 | −8.5% | −0.5240 to +0.2840 | no |
| host CPU busy, the real machine under kind (%) | 29.63 | 28.53 | −3.7% | −1.6750 to −0.5133 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 380.6 | 619.9 | 8.624 | 0.998 | 6 |
| Native tuned, HPA target 40 | 380.9 | 619.5 | 9.098 | 1.003 | 6 |
| Native tuned, HPA target 30 | 382.7 | 647 | 9.632 | 1.011 | 6 |
| Native tuned, HPA target 20 | 371.5 | 618.6 | 9.929 | 0.9993 | 6 |
| omni | 131.8 | 179.5 | 8.561 | 0.9584 | 6 |

- omni (p95 131.8 ms): no native setting tried reached it; the lowest native p95 is 371.5 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*