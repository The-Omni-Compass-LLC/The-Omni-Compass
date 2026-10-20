# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 478.5 | 476.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.5 | 476.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 248 | 125.8 |
| response time (ms), 95th percentile | 631.9 | 256.6 |
| response time (ms), 99th percentile | 1213 | 636.2 |
| time over the response line (% of samples) | 11.36 | 2.645 |
| failed requests (%) | 1.088 | 0.8844 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.6 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4717 | 0.73 |
| utilisation (used / allocatable) | 0.0741 | 0.07144 |
| CPU used (cores), mean | 1.778 | 1.715 |
| Omni's own CPU (cores), mean | 0 | 0.00929 |
| CPU used with Omni's own (cores), mean | 1.778 | 1.724 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.1 | 431.5 |
| HPA replicas, mean | 9.621 | 10.38 |
| pods started | 7.1 | 14.3 |
| pod start wait, total (s) | 11.8 | 24 |
| pod start wait, mean (s) | 1.738 | 1.592 |
| host CPU busy, the real machine under kind (%) | 51.56 | 50.23 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | no |
| node-hours | 4.334 | 4.333 | -0.0% | -0.01092 to +0.00825 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 478.5 | 476.6 | -0.4% | -3.111 to -0.5874 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.5 | 476.6 | -0.4% | -3.111 to -0.5874 | yes: GAIN |
| response time (ms), mean | 248 | 125.8 | -49.3% | -169.4 to -75.06 | yes: GAIN |
| response time (ms), 95th percentile | 631.9 | 256.6 | -59.4% | -504.4 to -246.3 | yes: GAIN |
| response time (ms), 99th percentile | 1213 | 636.2 | -47.5% | -811.8 to -341.2 | yes: GAIN |
| time over the response line (% of samples) | 11.36 | 2.645 | -76.7% | -13.77 to -3.656 | yes: GAIN |
| failed requests (%) | 1.088 | 0.8844 | -18.7% | -0.3746 to -0.03228 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.6 | 7 | -66.0% | -20.41 to -6.787 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55 | +55 (native is 0) | +35.29 to +74.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4717 | 0.73 | +54.8% | -0.05534 to +0.572 | no |
| utilisation (used / allocatable) | 0.0741 | 0.07144 | -3.6% | -0.003596 to -0.001725 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.778 | 1.715 | -3.6% | -0.08631 to -0.0414 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00929 | +0.00929 (native is 0) | +0.007137 to +0.01144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.778 | 1.724 | -3.1% | -0.07588 to -0.03325 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.1 | 431.5 | +3.2% | +5.519 to +21.24 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.621 | 10.38 | +7.9% | -0.7429 to +2.263 | no |
| pods started | 7.1 | 14.3 | +101.4% | +2.201 to +12.2 | yes: power given |
| pod start wait, total (s) | 11.8 | 24 | +103.4% | +1.726 to +22.67 | yes: LOSS |
| pod start wait, mean (s) | 1.738 | 1.592 | -8.4% | -0.4147 to +0.1222 | no |
| host CPU busy, the real machine under kind (%) | 51.56 | 50.23 | -2.6% | -1.973 to -0.6863 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*