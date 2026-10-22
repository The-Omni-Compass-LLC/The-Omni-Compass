# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.498 |
| node-hours | 2.519 | 2.307 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 259 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 567.9 | 509.7 |
| response time (ms), 95th percentile | 3363 | 3386 |
| response time (ms), 99th percentile | 5035 | 5037 |
| time over the response line (% of samples) | 16.34 | 15.77 |
| failed requests (%) | 0.01015 | 0.01058 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 194.9 | 198.4 |
| utilisation (used / allocatable) | 0.06438 | 0.07145 |
| CPU used (cores), mean | 1.545 | 1.564 |
| Omni's own CPU (cores), mean | 0 | 0.0554 |
| CPU used with Omni's own (cores), mean | 1.545 | 1.62 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.5 | 395.7 |
| HPA replicas, mean | 2.065 | 1.918 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 44.11 | 45.92 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 605.3 | 617.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.17 |

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
| worker nodes in service, mean | 6 | 5.498 | -8.4% | -0.8724 to -0.1313 | yes: GAIN |
| node-hours | 2.519 | 2.307 | -8.4% | -0.3686 to -0.05584 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.8 | +0.1% | -0.5826 to +0.9605 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 259 | -5.7% | -27.42 to -3.786 | yes: GAIN |
| response time (ms), mean | 567.9 | 509.7 | -10.2% | -71.5 to -44.91 | yes: GAIN |
| response time (ms), 95th percentile | 3363 | 3386 | +0.7% | -148.1 to +194.4 | no |
| response time (ms), 99th percentile | 5035 | 5037 | +0.0% | -293.9 to +298.3 | no |
| time over the response line (% of samples) | 16.34 | 15.77 | -3.5% | -1.036 to -0.1034 | yes: GAIN |
| failed requests (%) | 0.01015 | 0.01058 | +4.2% | -0.03453 to +0.03539 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.8 | +7.8 (native is 0) | +6.547 to +9.053 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 194.9 | 198.4 | +1.8% | -0.006117 to +6.883 | no |
| utilisation (used / allocatable) | 0.06438 | 0.07145 | +11.0% | +0.002457 to +0.01168 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.545 | 1.564 | +1.2% | -0.01286 to +0.05101 | no |
| Omni's own CPU (cores), mean | 0 | 0.0554 | +0.0554 (native is 0) | +0.05106 to +0.05974 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.545 | 1.62 | +4.8% | +0.04179 to +0.1072 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.5 | 395.7 | -7.0% | -47.74 to -11.84 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.065 | 1.918 | -7.1% | -0.254 to -0.03988 | yes: GAIN |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 44.11 | 45.92 | +4.1% | +1.522 to +2.097 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 605.3 | 617.1 | +1.9% | +7.605 to +16 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.17 | -13.8% | -1.437 to -0.2229 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*