# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.341 |
| energy, parked workers still on at idle power (Wh, declared model) | 481.1 | 479.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.1 | 479.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 271.5 | 142.3 |
| response time (ms), 95th percentile | 707.7 | 280.9 |
| response time (ms), 99th percentile | 1459 | 862.5 |
| time over the response line (% of samples) | 13.19 | 3.357 |
| failed requests (%) | 1.415 | 1.193 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.4 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.81 | 0.95 |
| utilisation (used / allocatable) | 0.07772 | 0.07489 |
| CPU used (cores), mean | 1.865 | 1.797 |
| Omni's own CPU (cores), mean | 0 | 0.00968 |
| CPU used with Omni's own (cores), mean | 1.865 | 1.807 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.3 | 408.6 |
| HPA replicas, mean | 9.66 | 11.09 |
| pods started | 5.5 | 16.1 |
| pod start wait, total (s) | 16 | 34.6 |
| pod start wait, mean (s) | 2.502 | 2.242 |
| host CPU busy, the real machine under kind (%) | 53.8 | 52.56 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.771e-16 to -8.869e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.337 | 4.341 | +0.1% | -0.003776 to +0.01244 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 481.1 | 479.7 | -0.3% | -2.229 to -0.4346 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.1 | 479.7 | -0.3% | -2.229 to -0.4346 | yes: GAIN |
| response time (ms), mean | 271.5 | 142.3 | -47.6% | -174.8 to -83.5 | yes: GAIN |
| response time (ms), 95th percentile | 707.7 | 280.9 | -60.3% | -564.8 to -288.7 | yes: GAIN |
| response time (ms), 99th percentile | 1459 | 862.5 | -40.9% | -852.2 to -340.1 | yes: GAIN |
| time over the response line (% of samples) | 13.19 | 3.357 | -74.5% | -14.57 to -5.091 | yes: GAIN |
| failed requests (%) | 1.415 | 1.193 | -15.7% | -0.3753 to -0.06954 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.4 | 9 | -61.5% | -21.04 to -7.756 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66 | +66 (native is 0) | +47.31 to +84.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.81 | 0.95 | +17.3% | -0.4373 to +0.7173 | no |
| utilisation (used / allocatable) | 0.07772 | 0.07489 | -3.6% | -0.003824 to -0.001841 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.865 | 1.797 | -3.6% | -0.09177 to -0.04418 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00968 | +0.00968 (native is 0) | +0.007803 to +0.01156 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.865 | 1.807 | -3.1% | -0.08071 to -0.03588 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.3 | 408.6 | +3.1% | +6.006 to +18.62 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.66 | 11.09 | +14.8% | +0.0904 to +2.764 | yes: power given |
| pods started | 5.5 | 16.1 | +192.7% | +5.288 to +15.91 | yes: power given |
| pod start wait, total (s) | 16 | 34.6 | +116.3% | +4.981 to +32.22 | yes: LOSS |
| pod start wait, mean (s) | 2.502 | 2.242 | -10.4% | -1.241 to +0.7208 | no |
| host CPU busy, the real machine under kind (%) | 53.8 | 52.56 | -2.3% | -1.772 to -0.7195 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*