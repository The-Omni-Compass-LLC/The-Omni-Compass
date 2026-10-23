# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.518 | 1.517 | 1.52 | 1.517 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | 159 | 158.7 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | 159 | 158.7 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 140.6 | 136.3 | 132 | 132 | 73.38 |
| response time (ms), 95th percentile | 314.8 | 305.4 | 289.3 | 284 | 107.7 |
| response time (ms), 99th percentile | 535.4 | 502.5 | 474.2 | 466.6 | 147.9 |
| time over the response line (% of samples) | 2.033 | 1.998 | 1.595 | 1.665 | 0.0122 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 1.9 | 1.6 | 1.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.07833 | 0.05333 | 0.02667 | 0.16 |
| utilisation (used / allocatable) | 0.03586 | 0.03589 | 0.03552 | 0.03581 | 0.0343 |
| CPU used (cores), mean | 0.8607 | 0.8614 | 0.8524 | 0.8595 | 0.8233 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.02225 |
| CPU used with Omni's own (cores), mean | 0.8607 | 0.8614 | 0.8524 | 0.8595 | 0.8455 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.7 | 799.5 | 809.4 | 793.9 | 826.4 |
| HPA replicas, mean | 8.179 | 8.767 | 9.411 | 9.786 | 8.456 |
| pods started | 5.2 | 4.6 | 3 | 1.3 | 4.1 |
| pod start wait, total (s) | 7.1 | 6.9 | 3.7 | 1.8 | 5.7 |
| pod start wait, mean (s) | 1.372 | 1.568 | 1.033 | 0.5667 | 1.368 |
| host CPU busy, the real machine under kind (%) | 26.05 | 25.96 | 25.78 | 26.02 | 25.76 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.518 | 1.518 | +0.0% | -0.007207 to +0.008207 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | -0.2% | -1.135 to +0.4944 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.6 | -0.2% | -1.135 to +0.4944 | no |
| response time (ms), mean | 140.6 | 73.38 | -47.8% | -97.99 to -36.44 | yes: GAIN |
| response time (ms), 95th percentile | 314.8 | 107.7 | -65.8% | -290 to -124.1 | yes: GAIN |
| response time (ms), 99th percentile | 535.4 | 147.9 | -72.4% | -551.3 to -223.7 | yes: GAIN |
| time over the response line (% of samples) | 2.033 | 0.0122 | -99.4% | -3.453 to -0.5891 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.5 | 0 | -100.0% | -4.415 to -0.5851 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.7 (native is 0) | +16.91 to +20.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.16 | +50.0% | -0.2134 to +0.3201 | no |
| utilisation (used / allocatable) | 0.03586 | 0.0343 | -4.3% | -0.002522 to -0.0005922 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8607 | 0.8233 | -4.3% | -0.06052 to -0.01421 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02225 | +0.0222 (native is 0) | +0.01881 to +0.02569 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8607 | 0.8455 | -1.8% | -0.03559 to +0.005362 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.7 | 826.4 | +3.3% | +5.071 to +48.2 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.179 | 8.456 | +3.4% | -0.1524 to +0.7064 | no |
| pods started | 5.2 | 4.1 | -21.2% | -2.425 to +0.2254 | no |
| pod start wait, total (s) | 7.1 | 5.7 | -19.7% | -3.882 to +1.082 | no |
| pod start wait, mean (s) | 1.372 | 1.368 | -0.3% | -0.3311 to +0.3239 | no |
| host CPU busy, the real machine under kind (%) | 26.05 | 25.76 | -1.1% | -0.912 to +0.3325 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 314.8 | 535.4 | 8.179 | 0.8607 | 6 |
| Native tuned, HPA target 40 | 305.4 | 502.5 | 8.767 | 0.8614 | 6 |
| Native tuned, HPA target 30 | 289.3 | 474.2 | 9.411 | 0.8524 | 6 |
| Native tuned, HPA target 20 | 284 | 466.6 | 9.786 | 0.8595 | 6 |
| omni | 107.7 | 147.9 | 8.456 | 0.8455 | 6 |

- omni (p95 107.7 ms): no native setting tried reached it; the lowest native p95 is 284 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*