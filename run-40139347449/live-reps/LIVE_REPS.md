# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.518 | 1.518 | 1.517 | 1.52 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 160 | 160 | 160.2 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 160 | 160 | 160.2 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 166.9 | 165.1 | 165.3 | 161.6 | 84.68 |
| response time (ms), 95th percentile | 375.1 | 373.9 | 366.9 | 361 | 129.6 |
| response time (ms), 99th percentile | 625.2 | 638.6 | 593.1 | 613.4 | 176.3 |
| time over the response line (% of samples) | 2.478 | 2.596 | 2.397 | 2.133 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 2.7 | 2.6 | 2.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.02667 | 0.1067 | 0.1067 | 0.08 |
| utilisation (used / allocatable) | 0.04107 | 0.04087 | 0.04109 | 0.04046 | 0.03899 |
| CPU used (cores), mean | 0.9856 | 0.981 | 0.9861 | 0.971 | 0.9357 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00885 |
| CPU used with Omni's own (cores), mean | 0.9856 | 0.981 | 0.9861 | 0.971 | 0.9445 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 671.8 | 670.7 | 668.5 | 678.5 | 698.5 |
| HPA replicas, mean | 8.741 | 9.118 | 9.652 | 9.964 | 8.596 |
| pods started | 4.7 | 3.9 | 2.5 | 0.3 | 3 |
| pod start wait, total (s) | 7 | 5.5 | 3.7 | 0.6 | 4.6 |
| pod start wait, mean (s) | 1.487 | 1.394 | 1.35 | 0.2 | 1.575 |
| host CPU busy, the real machine under kind (%) | 29.37 | 29.28 | 29.45 | 29.15 | 28.34 |
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
| node-hours | 1.518 | 1.516 | −0.1% | −0.0072 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 159.4 | −0.4% | −1.1995 to −0.1013 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 159.4 | −0.4% | −1.1995 to −0.1013 | yes: GAIN |
| response time (ms), mean | 166.9 | 84.68 | −49.3% | −101.3237 to −63.2178 | yes: GAIN |
| response time (ms), 95th percentile | 375.1 | 129.6 | −65.5% | −299.4964 to −191.5296 | yes: GAIN |
| response time (ms), 99th percentile | 625.2 | 176.3 | −71.8% | −553.1854 to −344.6798 | yes: GAIN |
| time over the response line (% of samples) | 2.478 | 0.01212 | −99.5% | −3.4108 to −1.5211 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −3.8251 to −1.3749 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.900 (native is 0) | +15.2140 to +20.5860 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08 | −40.0% | −0.2286 to +0.1220 | no |
| utilisation (used / allocatable) | 0.04107 | 0.03899 | −5.1% | −0.0032 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9856 | 0.9357 | −5.1% | −0.0758 to −0.0240 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00885 | +0.009 (native is 0) | +0.0078 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9856 | 0.9445 | −4.2% | −0.0662 to −0.0158 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 671.8 | 698.5 | +4.0% | +6.7305 to +46.8112 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.741 | 8.596 | −1.7% | −0.7483 to +0.4592 | no |
| pods started | 4.7 | 3 | −36.2% | −3.0081 to −0.3919 | yes: GAIN |
| pod start wait, total (s) | 7 | 4.6 | −34.3% | −5.2252 to +0.4252 | no |
| pod start wait, mean (s) | 1.487 | 1.575 | +5.9% | −0.3618 to +0.5384 | no |
| host CPU busy, the real machine under kind (%) | 29.37 | 28.34 | −3.5% | −1.5670 to −0.4812 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 375.1 | 625.2 | 8.741 | 0.9856 | 6 |
| Native tuned, HPA target 40 | 373.9 | 638.6 | 9.118 | 0.981 | 6 |
| Native tuned, HPA target 30 | 366.9 | 593.1 | 9.652 | 0.9861 | 6 |
| Native tuned, HPA target 20 | 361 | 613.4 | 9.964 | 0.971 | 6 |
| omni | 129.6 | 176.3 | 8.596 | 0.9445 | 6 |

- omni (p95 129.6 ms): no native setting tried reached it; the lowest native p95 is 361 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*