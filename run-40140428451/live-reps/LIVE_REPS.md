# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.513 | 1.513 | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | 158 | 158.3 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | 158 | 158.3 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 131.1 | 128.5 | 126.5 | 124 | 70.63 |
| response time (ms), 95th percentile | 286.6 | 281.5 | 278.1 | 265.9 | 103.1 |
| response time (ms), 99th percentile | 465.2 | 449.2 | 442.9 | 443.5 | 134.7 |
| time over the response line (% of samples) | 1.355 | 1.312 | 1.152 | 1.083 | 0.02395 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 1.3 | 1.2 | 0.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 15.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.05333 | 0 | 0.05167 | 0.025 |
| utilisation (used / allocatable) | 0.03464 | 0.03461 | 0.03466 | 0.03458 | 0.0332 |
| CPU used (cores), mean | 0.8314 | 0.8307 | 0.8319 | 0.8298 | 0.7968 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00738 |
| CPU used with Omni's own (cores), mean | 0.8314 | 0.8307 | 0.8319 | 0.8298 | 0.8042 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 803.2 | 805.5 | 802.7 | 806.5 | 828.3 |
| HPA replicas, mean | 8.157 | 8.807 | 9.34 | 9.88 | 7.293 |
| pods started | 5.6 | 4.7 | 3.3 | 0.7 | 4.2 |
| pod start wait, total (s) | 8.1 | 6 | 4.8 | 0.4 | 6.9 |
| pod start wait, mean (s) | 1.467 | 1.279 | 1.477 | 0.125 | 1.577 |
| host CPU busy, the real machine under kind (%) | 25.12 | 25.15 | 25.2 | 25.06 | 24.57 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0011 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | −0.1% | −0.3655 to −0.0784 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | −0.1% | −0.3655 to −0.0784 | yes: GAIN |
| response time (ms), mean | 131.1 | 70.63 | −46.1% | −82.7181 to −38.2641 | yes: GAIN |
| response time (ms), 95th percentile | 286.6 | 103.1 | −64.0% | −243.9487 to −122.9703 | yes: GAIN |
| response time (ms), 99th percentile | 465.2 | 134.7 | −71.0% | −458.0064 to −202.9530 | yes: GAIN |
| time over the response line (% of samples) | 1.355 | 0.02395 | −98.2% | −2.4331 to −0.2298 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.7985 to −0.0015 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +12.1839 to +19.6161 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.025 | −51.6% | −0.1303 to +0.0770 | no |
| utilisation (used / allocatable) | 0.03464 | 0.0332 | −4.2% | −0.0024 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8314 | 0.7968 | −4.2% | −0.0565 to −0.0127 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00738 | +0.007 (native is 0) | +0.0061 to +0.0086 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8314 | 0.8042 | −3.3% | −0.0480 to −0.0064 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 803.2 | 828.3 | +3.1% | +11.6430 to +38.5205 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.157 | 7.293 | −10.6% | −1.5097 to −0.2180 | yes: GAIN |
| pods started | 5.6 | 4.2 | −25.0% | −2.4228 to −0.3772 | yes: GAIN |
| pod start wait, total (s) | 8.1 | 6.9 | −14.8% | −4.1551 to +1.7551 | no |
| pod start wait, mean (s) | 1.467 | 1.577 | +7.5% | −0.2476 to +0.4676 | no |
| host CPU busy, the real machine under kind (%) | 25.12 | 24.57 | −2.2% | −0.9442 to −0.1664 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 286.6 | 465.2 | 8.157 | 0.8314 | 6 |
| Native tuned, HPA target 40 | 281.5 | 449.2 | 8.807 | 0.8307 | 6 |
| Native tuned, HPA target 30 | 278.1 | 442.9 | 9.34 | 0.8319 | 6 |
| Native tuned, HPA target 20 | 265.9 | 443.5 | 9.88 | 0.8298 | 6 |
| omni | 103.1 | 134.7 | 7.293 | 0.8042 | 6 |

- omni (p95 103.1 ms): no native setting tried reached it; the lowest native p95 is 265.9 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*