# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 478.2 | 476.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.2 | 476.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 245.1 | 126 |
| response time (ms), 95th percentile | 629.9 | 262.2 |
| response time (ms), 99th percentile | 1169 | 653.8 |
| time over the response line (% of samples) | 11.2 | 2.814 |
| failed requests (%) | 1.039 | 0.9043 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.3 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9483 | 0.7483 |
| utilisation (used / allocatable) | 0.07371 | 0.07132 |
| CPU used (cores), mean | 1.769 | 1.712 |
| Omni's own CPU (cores), mean | 0 | 0.00854 |
| CPU used with Omni's own (cores), mean | 1.769 | 1.72 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 428.9 |
| HPA replicas, mean | 9.558 | 10.12 |
| pods started | 6.2 | 12.9 |
| pod start wait, total (s) | 23.2 | 35.2 |
| pod start wait, mean (s) | 3.179 | 2.782 |
| host CPU busy, the real machine under kind (%) | 51 | 50.04 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.318e-16 to +1.009e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.334 | 4.334 | -0.0% | -0.007103 to +0.006103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 478.2 | 476.6 | -0.3% | -2.286 to -0.8064 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.2 | 476.6 | -0.3% | -2.286 to -0.8064 | yes: GAIN |
| response time (ms), mean | 245.1 | 126 | -48.6% | -167.8 to -70.22 | yes: GAIN |
| response time (ms), 95th percentile | 629.9 | 262.2 | -58.4% | -497.7 to -237.7 | yes: GAIN |
| response time (ms), 99th percentile | 1169 | 653.8 | -44.1% | -739.4 to -290.6 | yes: GAIN |
| time over the response line (% of samples) | 11.2 | 2.814 | -74.9% | -13.34 to -3.427 | yes: GAIN |
| failed requests (%) | 1.039 | 0.9043 | -13.0% | -0.2577 to -0.01262 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.3 | 7.7 | -60.1% | -17.6 to -5.604 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.1 (native is 0) | +34.97 to +65.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9483 | 0.7483 | -21.1% | -0.8176 to +0.4176 | no |
| utilisation (used / allocatable) | 0.07371 | 0.07132 | -3.2% | -0.003768 to -0.001012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.769 | 1.712 | -3.2% | -0.09042 to -0.0243 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00854 | +0.00854 (native is 0) | +0.006845 to +0.01024 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.72 | -2.8% | -0.08056 to -0.01708 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 428.9 | +1.9% | -0.3355 to +16.24 | no |
| HPA replicas, mean | 9.558 | 10.12 | +5.9% | -0.6265 to +1.747 | no |
| pods started | 6.2 | 12.9 | +108.1% | +2.695 to +10.7 | yes: power given |
| pod start wait, total (s) | 23.2 | 35.2 | +51.7% | -0.4581 to +24.46 | no |
| pod start wait, mean (s) | 3.179 | 2.782 | -12.5% | -1.115 to +0.322 | no |
| host CPU busy, the real machine under kind (%) | 51 | 50.04 | -1.9% | -1.838 to -0.0764 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*