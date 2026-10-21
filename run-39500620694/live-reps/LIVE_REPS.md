# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.509 | 1.511 | 1.513 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 160.2 | 160.3 | 160.5 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 160.2 | 160.3 | 160.5 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 197.1 | 194 | 191.4 | 188.5 | 95.09 |
| response time (ms), 95th percentile | 443 | 447.6 | 447.2 | 433.5 | 147 |
| response time (ms), 99th percentile | 729.7 | 700.4 | 713.9 | 694.2 | 202.4 |
| time over the response line (% of samples) | 3.794 | 3.709 | 3.792 | 3.536 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.9 | 3.4 | 3.5 | 3.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.08 | 0.1333 | 0.105 | 0.5117 |
| utilisation (used / allocatable) | 0.04611 | 0.04604 | 0.04563 | 0.04551 | 0.04335 |
| CPU used (cores), mean | 1.107 | 1.105 | 1.095 | 1.092 | 1.04 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.0097 |
| CPU used with Omni's own (cores), mean | 1.107 | 1.105 | 1.095 | 1.092 | 1.05 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 576.1 | 576.7 | 581.7 | 583.1 | 610.5 |
| HPA replicas, mean | 9.009 | 9.331 | 9.802 | 10 | 9.155 |
| pods started | 4.7 | 3.5 | 1.9 | 0 | 2.8 |
| pod start wait, total (s) | 7.5 | 5.3 | 3.1 | 0 | 4.3 |
| pod start wait, mean (s) | 1.56 | 1.408 | 1.6 | 0 | 1.508 |
| host CPU busy, the real machine under kind (%) | 33.18 | 33.11 | 32.79 | 32.66 | 31.7 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.069e-15 to +2.842e-18 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.511 | +0.0% | -0.001261 to +0.001594 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.8 | -0.4% | -0.79 to -0.4412 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.8 | -0.4% | -0.79 to -0.4412 | yes: GAIN |
| response time (ms), mean | 197.1 | 95.09 | -51.8% | -107 to -97.05 | yes: GAIN |
| response time (ms), 95th percentile | 443 | 147 | -66.8% | -315.7 to -276.2 | yes: GAIN |
| response time (ms), 99th percentile | 729.7 | 202.4 | -72.3% | -598.8 to -455.7 | yes: GAIN |
| time over the response line (% of samples) | 3.794 | 0.01212 | -99.7% | -4.324 to -3.24 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.9 | 0 | -100.0% | -4.526 to -3.274 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.9 (native is 0) | +17.04 to +18.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.5117 | +372.3% | +0.1947 to +0.6119 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04611 | 0.04335 | -6.0% | -0.003261 to -0.002249 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.107 | 1.04 | -6.0% | -0.07826 to -0.05398 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.009348 to +0.01005 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.107 | 1.05 | -5.1% | -0.06831 to -0.04453 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 576.1 | 610.5 | +6.0% | +27.92 to +40.75 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.009 | 9.155 | +1.6% | -0.02171 to +0.3137 | no |
| pods started | 4.7 | 2.8 | -40.4% | -2.756 to -1.044 | yes: GAIN |
| pod start wait, total (s) | 7.5 | 4.3 | -42.7% | -5.58 to -0.8204 | yes: GAIN |
| pod start wait, mean (s) | 1.56 | 1.508 | -3.3% | -0.5059 to +0.4026 | no |
| host CPU busy, the real machine under kind (%) | 33.18 | 31.7 | -4.4% | -1.815 to -1.129 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 443 | 729.7 | 9.009 | 1.107 | 6 |
| Native tuned, HPA target 40 | 447.6 | 700.4 | 9.331 | 1.105 | 6 |
| Native tuned, HPA target 30 | 447.2 | 713.9 | 9.802 | 1.095 | 6 |
| Native tuned, HPA target 20 | 433.5 | 694.2 | 10 | 1.092 | 6 |
| omni | 147 | 202.4 | 9.155 | 1.05 | 6 |

- omni (p95 147 ms): no native setting tried reached it; the lowest native p95 is 433.5 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*