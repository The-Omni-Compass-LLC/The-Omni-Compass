# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 510.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 279.9 | 157.9 |
| response time (ms), 95th percentile | 763.8 | 307.1 |
| response time (ms), 99th percentile | 2504 | 1936 |
| time over the response line (% of samples) | 16.37 | 8.829 |
| failed requests (%) | 7.154 | 6.566 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 16.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.375 | 0.3967 |
| utilisation (used / allocatable) | 0.09497 | 0.09282 |
| CPU used (cores), mean | 2.279 | 2.228 |
| Omni's own CPU (cores), mean | 0 | 0.02846 |
| CPU used with Omni's own (cores), mean | 2.279 | 2.256 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 320.2 | 329.9 |
| HPA replicas, mean | 9.59 | 10.91 |
| pods started | 4.9 | 9.8 |
| pod start wait, total (s) | 7.2 | 45.1 |
| pod start wait, mean (s) | 1.495 | 4.094 |
| host CPU busy, the real machine under kind (%) | 64.22 | 63.88 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.13e-15 to +2.421e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.51 | -0.0% | -0.006861 to +0.002861 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 510.5 | -0.3% | -2.237 to -0.9206 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.5 | -0.3% | -2.237 to -0.9206 | yes: GAIN |
| response time (ms), mean | 279.9 | 157.9 | -43.6% | -161.1 to -82.91 | yes: GAIN |
| response time (ms), 95th percentile | 763.8 | 307.1 | -59.8% | -585.1 to -328.4 | yes: GAIN |
| response time (ms), 99th percentile | 2504 | 1936 | -22.7% | -1615 to +479 | no |
| time over the response line (% of samples) | 16.37 | 8.829 | -46.1% | -10.19 to -4.893 | yes: GAIN |
| failed requests (%) | 7.154 | 6.566 | -8.2% | -1.215 to +0.03966 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 16.9 | -34.0% | -11.36 to -6.044 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.5 | +51.5 (native is 0) | +42.66 to +60.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.375 | 0.3967 | +5.8% | -0.1273 to +0.1707 | no |
| utilisation (used / allocatable) | 0.09497 | 0.09282 | -2.3% | -0.003062 to -0.001254 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.279 | 2.228 | -2.3% | -0.07349 to -0.0301 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02846 | +0.0285 (native is 0) | +0.0239 to +0.03302 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.279 | 2.256 | -1.0% | -0.04761 to +0.0009464 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 320.2 | 329.9 | +3.0% | +1.75 to +17.53 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.59 | 10.91 | +13.8% | +0.1402 to +2.506 | yes: power given |
| pods started | 4.9 | 9.8 | +100.0% | +2.864 to +6.936 | yes: power given |
| pod start wait, total (s) | 7.2 | 45.1 | +526.4% | -26.6 to +102.4 | no |
| pod start wait, mean (s) | 1.495 | 4.094 | +173.9% | -2.726 to +7.923 | no |
| host CPU busy, the real machine under kind (%) | 64.22 | 63.88 | -0.5% | -0.9515 to +0.2597 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*