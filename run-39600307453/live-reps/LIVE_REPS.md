# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 189.4 | 93.04 |
| response time (ms), 95th percentile | 427.4 | 143.3 |
| response time (ms), 99th percentile | 695.2 | 200.5 |
| time over the response line (% of samples) | 3.403 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.4817 |
| utilisation (used / allocatable) | 0.0446 | 0.04236 |
| CPU used (cores), mean | 1.07 | 1.017 |
| Omni's own CPU (cores), mean | 0 | 0.00937 |
| CPU used with Omni's own (cores), mean | 1.07 | 1.026 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 597.3 | 626.2 |
| HPA replicas, mean | 8.946 | 9.141 |
| pods started | 5.1 | 2.8 |
| pod start wait, total (s) | 8.9 | 4.5 |
| pod start wait, mean (s) | 1.753 | 1.667 |
| host CPU busy, the real machine under kind (%) | 32.2 | 30.91 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.995e-16 to +8.895e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.511 | -0.1% | -0.007576 to +0.005242 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 159.6 | -0.4% | -1.468 to +0.08865 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 159.6 | -0.4% | -1.468 to +0.08865 | no |
| response time (ms), mean | 189.4 | 93.04 | -50.9% | -105.6 to -87.1 | yes: GAIN |
| response time (ms), 95th percentile | 427.4 | 143.3 | -66.5% | -320.2 to -247.9 | yes: GAIN |
| response time (ms), 99th percentile | 695.2 | 200.5 | -71.2% | -568.8 to -420.7 | yes: GAIN |
| time over the response line (% of samples) | 3.403 | 0.01212 | -99.6% | -4.339 to -2.443 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | -100.0% | -4.366 to -2.434 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.4 (native is 0) | +16.5 to +18.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.4817 | +261.2% | -0.02422 to +0.7209 | no |
| utilisation (used / allocatable) | 0.0446 | 0.04236 | -5.0% | -0.003166 to -0.00131 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.07 | 1.017 | -5.0% | -0.07598 to -0.03143 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00937 | +0.00937 (native is 0) | +0.008826 to +0.009914 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.07 | 1.026 | -4.1% | -0.06659 to -0.02208 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 597.3 | 626.2 | +4.8% | +17.58 to +40.2 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.946 | 9.141 | +2.2% | -0.04217 to +0.4339 | no |
| pods started | 5.1 | 2.8 | -45.1% | -3.257 to -1.343 | yes: GAIN |
| pod start wait, total (s) | 8.9 | 4.5 | -49.4% | -6.692 to -2.108 | yes: GAIN |
| pod start wait, mean (s) | 1.753 | 1.667 | -4.9% | -0.4131 to +0.2397 | no |
| host CPU busy, the real machine under kind (%) | 32.2 | 30.91 | -4.0% | -1.94 to -0.6406 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*