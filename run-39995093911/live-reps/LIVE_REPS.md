# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 519.5 | 518 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.5 | 518 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 284.9 | 167.2 |
| response time (ms), 95th percentile | 727.7 | 322.8 |
| response time (ms), 99th percentile | 2536 | 1999 |
| time over the response line (% of samples) | 20.12 | 13.13 |
| failed requests (%) | 12.05 | 10.51 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.3 | 23 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.1567 |
| utilisation (used / allocatable) | 0.1051 | 0.1036 |
| CPU used (cores), mean | 2.523 | 2.486 |
| Omni's own CPU (cores), mean | 0 | 0.00909 |
| CPU used with Omni's own (cores), mean | 2.523 | 2.495 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.7 | 298.8 |
| HPA replicas, mean | 9.584 | 9.943 |
| pods started | 5.4 | 4.6 |
| pod start wait, total (s) | 7.5 | 6.5 |
| pod start wait, mean (s) | 1.378 | 1.349 |
| host CPU busy, the real machine under kind (%) | 70.85 | 70.08 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.516 | 4.512 | -0.1% | -0.01265 to +0.003317 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 519.5 | 518 | -0.3% | -2.287 to -0.7153 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.5 | 518 | -0.3% | -2.287 to -0.7153 | yes: GAIN |
| response time (ms), mean | 284.9 | 167.2 | -41.3% | -152.4 to -82.93 | yes: GAIN |
| response time (ms), 95th percentile | 727.7 | 322.8 | -55.6% | -511.7 to -297.9 | yes: GAIN |
| response time (ms), 99th percentile | 2536 | 1999 | -21.2% | -1255 to +180.7 | no |
| time over the response line (% of samples) | 20.12 | 13.13 | -34.7% | -9.19 to -4.783 | yes: GAIN |
| failed requests (%) | 12.05 | 10.51 | -12.8% | -2.428 to -0.6458 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.3 | 23 | -21.5% | -7.608 to -4.992 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.3 | +39.3 (native is 0) | +30.11 to +48.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.1567 | -28.2% | -0.1785 to +0.05515 | no |
| utilisation (used / allocatable) | 0.1051 | 0.1036 | -1.5% | -0.002608 to -0.0005232 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.523 | 2.486 | -1.5% | -0.06259 to -0.01256 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00909 | +0.00909 (native is 0) | +0.007856 to +0.01032 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.523 | 2.495 | -1.1% | -0.05277 to -0.004202 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.7 | 298.8 | +1.0% | +1.259 to +4.772 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.584 | 9.943 | +3.7% | -0.2439 to +0.9618 | no |
| pods started | 5.4 | 4.6 | -14.8% | -2.671 to +1.071 | no |
| pod start wait, total (s) | 7.5 | 6.5 | -13.3% | -3.739 to +1.739 | no |
| pod start wait, mean (s) | 1.378 | 1.349 | -2.1% | -0.4326 to +0.375 | no |
| host CPU busy, the real machine under kind (%) | 70.85 | 70.08 | -1.1% | -1.403 to -0.1372 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*