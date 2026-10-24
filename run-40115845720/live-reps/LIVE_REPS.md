# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.339 |
| energy, parked workers still on at idle power (Wh, declared model) | 479.9 | 479.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 479.9 | 479.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 264.4 | 134.8 |
| response time (ms), 95th percentile | 688.7 | 286.9 |
| response time (ms), 99th percentile | 1353 | 730.6 |
| time over the response line (% of samples) | 12.91 | 3.415 |
| failed requests (%) | 1.432 | 1.206 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4217 | 0.505 |
| utilisation (used / allocatable) | 0.07659 | 0.07414 |
| CPU used (cores), mean | 1.838 | 1.779 |
| Omni's own CPU (cores), mean | 0 | 0.00965 |
| CPU used with Omni's own (cores), mean | 1.838 | 1.789 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.1 | 422.2 |
| HPA replicas, mean | 9.613 | 10.94 |
| pods started | 6.6 | 15.7 |
| pod start wait, total (s) | 9 | 26.5 |
| pod start wait, mean (s) | 1.411 | 1.696 |
| host CPU busy, the real machine under kind (%) | 53.02 | 51.79 |
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
| node-hours | 4.333 | 4.339 | +0.1% | −0.0017 to +0.0134 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 479.9 | 479.1 | −0.2% | −1.7344 to +0.1456 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 479.9 | 479.1 | −0.2% | −1.7344 to +0.1456 | no |
| response time (ms), mean | 264.4 | 134.8 | −49.0% | −179.7240 to −79.5480 | yes: GAIN |
| response time (ms), 95th percentile | 688.7 | 286.9 | −58.3% | −540.8074 to −262.8656 | yes: GAIN |
| response time (ms), 99th percentile | 1353 | 730.6 | −46.0% | −844.9173 to −399.8127 | yes: GAIN |
| time over the response line (% of samples) | 12.91 | 3.415 | −73.5% | −14.2627 to −4.7223 | yes: GAIN |
| failed requests (%) | 1.432 | 1.206 | −15.8% | −0.3555 to −0.0966 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23 | 9 | −60.9% | −21.0328 to −6.9672 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.6 | +62.600 (native is 0) | +44.0136 to +81.1864 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4217 | 0.505 | +19.8% | −0.2067 to +0.3733 | no |
| utilisation (used / allocatable) | 0.07659 | 0.07414 | −3.2% | −0.0037 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.838 | 1.779 | −3.2% | −0.0890 to −0.0287 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00965 | +0.010 (native is 0) | +0.0076 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.838 | 1.789 | −2.7% | −0.0783 to −0.0201 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.1 | 422.2 | +2.7% | +3.6500 to +18.6189 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.613 | 10.94 | +13.8% | −0.1777 to +2.8283 | no |
| pods started | 6.6 | 15.7 | +137.9% | +4.5329 to +13.6671 | yes: power given |
| pod start wait, total (s) | 9 | 26.5 | +194.4% | +9.6479 to +25.3521 | yes: LOSS |
| pod start wait, mean (s) | 1.411 | 1.696 | +20.1% | −0.0849 to +0.6536 | no |
| host CPU busy, the real machine under kind (%) | 53.02 | 51.79 | −2.3% | −2.0058 to −0.4687 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*