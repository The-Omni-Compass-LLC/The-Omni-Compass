# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.2 | 480.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.2 | 480.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 273.4 | 142.8 |
| response time (ms), 95th percentile | 700.8 | 306.7 |
| response time (ms), 99th percentile | 1307 | 807.7 |
| time over the response line (% of samples) | 13.08 | 3.46 |
| failed requests (%) | 1.286 | 1.053 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.2 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5917 | 1.275 |
| utilisation (used / allocatable) | 0.08008 | 0.07708 |
| CPU used (cores), mean | 1.922 | 1.85 |
| Omni's own CPU (cores), mean | 0 | 0.00979 |
| CPU used with Omni's own (cores), mean | 1.922 | 1.86 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.3 | 387.1 |
| HPA replicas, mean | 9.754 | 10.85 |
| pods started | 5.8 | 15.3 |
| pod start wait, total (s) | 21.3 | 37.5 |
| pod start wait, mean (s) | 3.461 | 2.591 |
| host CPU busy, the real machine under kind (%) | 55.46 | 54.01 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.65e-15 to -4.82e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.338 | +0.1% | -0.003298 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482.2 | 480.8 | -0.3% | -2.327 to -0.4556 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.2 | 480.8 | -0.3% | -2.327 to -0.4556 | yes: GAIN |
| response time (ms), mean | 273.4 | 142.8 | -47.8% | -166.6 to -94.64 | yes: GAIN |
| response time (ms), 95th percentile | 700.8 | 306.7 | -56.2% | -481.5 to -306.6 | yes: GAIN |
| response time (ms), 99th percentile | 1307 | 807.7 | -38.2% | -606.3 to -391.9 | yes: GAIN |
| time over the response line (% of samples) | 13.08 | 3.46 | -73.5% | -14.06 to -5.183 | yes: GAIN |
| failed requests (%) | 1.286 | 1.053 | -18.1% | -0.384 to -0.08203 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.2 | 8.7 | -60.8% | -18.54 to -8.462 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.5 | +62.5 (native is 0) | +45.78 to +79.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5917 | 1.275 | +115.5% | +0.1986 to +1.168 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08008 | 0.07708 | -3.7% | -0.003583 to -0.002417 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.922 | 1.85 | -3.7% | -0.08599 to -0.05801 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00979 | +0.00979 (native is 0) | +0.008182 to +0.0114 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.922 | 1.86 | -3.2% | -0.07592 to -0.04851 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.3 | 387.1 | +4.0% | +7.229 to +22.3 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.754 | 10.85 | +11.2% | -0.006777 to +2.197 | no |
| pods started | 5.8 | 15.3 | +163.8% | +5.535 to +13.46 | yes: power given |
| pod start wait, total (s) | 21.3 | 37.5 | +76.1% | +9.275 to +23.13 | yes: LOSS |
| pod start wait, mean (s) | 3.461 | 2.591 | -25.1% | -1.509 to -0.231 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 55.46 | 54.01 | -2.6% | -1.811 to -1.095 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*