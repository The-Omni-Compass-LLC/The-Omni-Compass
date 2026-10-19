# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 178.8 | 88.36 |
| response time (ms), 95th percentile | 413.9 | 135.8 |
| response time (ms), 99th percentile | 636 | 189.9 |
| time over the response line (% of samples) | 3.042 | 0.02389 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.245 |
| utilisation (used / allocatable) | 0.04286 | 0.03979 |
| CPU used (cores), mean | 1.029 | 0.9548 |
| Omni's own CPU (cores), mean | 0 | 0.00882 |
| CPU used with Omni's own (cores), mean | 1.029 | 0.9637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626.8 | 670.3 |
| HPA replicas, mean | 9.047 | 8.685 |
| pods started | 4.1 | 2.8 |
| pod start wait, total (s) | 14 | 6.9 |
| pod start wait, mean (s) | 2.99 | 2.223 |
| host CPU busy, the real machine under kind (%) | 30.61 | 29.13 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.517 | -0.1% | -0.01156 to +0.009227 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.7 | -0.5% | -1.845 to +0.3162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.7 | -0.5% | -1.845 to +0.3162 | no |
| response time (ms), mean | 178.8 | 88.36 | -50.6% | -105.7 to -75.2 | yes: GAIN |
| response time (ms), 95th percentile | 413.9 | 135.8 | -67.2% | -333.2 to -222.9 | yes: GAIN |
| response time (ms), 99th percentile | 636 | 189.9 | -70.1% | -540.7 to -351.5 | yes: GAIN |
| time over the response line (% of samples) | 3.042 | 0.02389 | -99.2% | -4.343 to -1.693 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | -100.0% | -4.845 to -1.555 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.2 | +18.2 (native is 0) | +16.02 to +20.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.245 | -24.2% | -0.2714 to +0.1147 | no |
| utilisation (used / allocatable) | 0.04286 | 0.03979 | -7.2% | -0.003868 to -0.002278 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.029 | 0.9548 | -7.2% | -0.09284 to -0.05468 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00882 | +0.00882 (native is 0) | +0.00817 to +0.00947 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.029 | 0.9637 | -6.3% | -0.08353 to -0.04635 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626.8 | 670.3 | +6.9% | +35.55 to +51.57 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.047 | 8.685 | -4.0% | -0.9767 to +0.2522 | no |
| pods started | 4.1 | 2.8 | -31.7% | -2.954 to +0.3537 | no |
| pod start wait, total (s) | 14 | 6.9 | -50.7% | -12.93 to -1.275 | yes: GAIN |
| pod start wait, mean (s) | 2.99 | 2.223 | -25.6% | -2.185 to +0.6514 | no |
| host CPU busy, the real machine under kind (%) | 30.61 | 29.13 | -4.9% | -2.017 to -0.9535 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*