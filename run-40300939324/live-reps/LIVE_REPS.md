# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.511 | 1.511 | 1.51 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | 158.7 | 158.6 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | 158.7 | 158.6 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 147.9 | 145.2 | 146.1 | 145.9 | 77.55 |
| response time (ms), 95th percentile | 329.2 | 311.1 | 318.1 | 321.5 | 112.2 |
| response time (ms), 99th percentile | 511.3 | 498.6 | 512.5 | 513.1 | 147.1 |
| time over the response line (% of samples) | 1.58 | 1.51 | 1.732 | 1.714 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 1.5 | 1.7 | 1.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1317 | 0.02667 | 0.1033 | 0.1067 |
| utilisation (used / allocatable) | 0.0381 | 0.03793 | 0.03814 | 0.03816 | 0.03646 |
| CPU used (cores), mean | 0.9144 | 0.9103 | 0.9155 | 0.9158 | 0.875 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00813 |
| CPU used with Omni's own (cores), mean | 0.9144 | 0.9103 | 0.9155 | 0.9158 | 0.8831 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.6 | 714.4 | 712.1 | 708.7 | 736.6 |
| HPA replicas, mean | 8.696 | 9.013 | 9.521 | 9.945 | 7.981 |
| pods started | 5.1 | 4.3 | 3 | 0.4 | 3.4 |
| pod start wait, total (s) | 7.8 | 6.5 | 4.1 | 0.3 | 4.9 |
| pod start wait, mean (s) | 1.525 | 1.538 | 1.333 | 0.1667 | 1.36 |
| host CPU busy, the real machine under kind (%) | 27.55 | 27.38 | 27.48 | 27.51 | 26.75 |
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
| node-hours | 1.51 | 1.513 | +0.2% | −0.0077 to +0.0127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −1.0471 to +0.8039 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −1.0471 to +0.8039 | no |
| response time (ms), mean | 147.9 | 77.55 | −47.6% | −91.7475 to −48.8853 | yes: GAIN |
| response time (ms), 95th percentile | 329.2 | 112.2 | −65.9% | −269.3400 to −164.8050 | yes: GAIN |
| response time (ms), 99th percentile | 511.3 | 147.1 | −71.2% | −472.5621 to −255.8065 | yes: GAIN |
| time over the response line (% of samples) | 1.58 | 0 | −100.0% | −2.8591 to −0.3005 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | −100.0% | −2.9985 to −0.2015 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +15.3498 to +20.2502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | −0.1833 to +0.2366 | no |
| utilisation (used / allocatable) | 0.0381 | 0.03646 | −4.3% | −0.0031 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9144 | 0.875 | −4.3% | −0.0746 to −0.0043 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00813 | +0.008 (native is 0) | +0.0072 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9144 | 0.8831 | −3.4% | −0.0658 to +0.0032 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.6 | 736.6 | +3.1% | +2.7450 to +41.2978 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.696 | 7.981 | −8.2% | −1.4088 to −0.0216 | yes: GAIN |
| pods started | 5.1 | 3.4 | −33.3% | −3.1717 to −0.2283 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 4.9 | −37.2% | −6.1771 to +0.3771 | no |
| pod start wait, mean (s) | 1.525 | 1.36 | −10.8% | −0.6937 to +0.3637 | no |
| host CPU busy, the real machine under kind (%) | 27.55 | 26.75 | −2.9% | −1.6932 to +0.0889 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 329.2 | 511.3 | 8.696 | 0.9144 | 6 |
| Native tuned, HPA target 40 | 311.1 | 498.6 | 9.013 | 0.9103 | 6 |
| Native tuned, HPA target 30 | 318.1 | 512.5 | 9.521 | 0.9155 | 6 |
| Native tuned, HPA target 20 | 321.5 | 513.1 | 9.945 | 0.9158 | 6 |
| omni | 112.2 | 147.1 | 7.981 | 0.8831 | 6 |

- omni (p95 112.2 ms): no native setting tried reached it; the lowest native p95 is 311.1 ms (Native tuned, HPA target 40).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*