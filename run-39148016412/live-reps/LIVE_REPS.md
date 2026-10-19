# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.162 |
| node-hours | 2.512 | 2.162 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 247.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 543 | 487.4 |
| response time (ms), 95th percentile | 3250 | 3235 |
| response time (ms), 99th percentile | 5007 | 4922 |
| time over the response line (% of samples) | 15.77 | 15.23 |
| failed requests (%) | 0.02151 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.8 | 193.5 |
| utilisation (used / allocatable) | 0.06321 | 0.07323 |
| CPU used (cores), mean | 1.517 | 1.514 |
| Omni's own CPU (cores), mean | 0 | 0.02334 |
| CPU used with Omni's own (cores), mean | 1.517 | 1.537 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.3 | 394.6 |
| HPA replicas, mean | 2.011 | 2.119 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 43.25 | 44.04 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 589.6 | 593.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.662 |

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
| worker nodes in service, mean | 6 | 5.162 | -14.0% | -1.296 to -0.381 | yes: GAIN |
| node-hours | 2.512 | 2.162 | -13.9% | -0.5421 to -0.158 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.7 | +0.1% | -1.017 to +1.402 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 247.4 | -9.6% | -40.51 to -11.76 | yes: GAIN |
| response time (ms), mean | 543 | 487.4 | -10.2% | -64.28 to -46.93 | yes: GAIN |
| response time (ms), 95th percentile | 3250 | 3235 | -0.5% | -115.5 to +85.05 | no |
| response time (ms), 99th percentile | 5007 | 4922 | -1.7% | -306.5 to +136.8 | no |
| time over the response line (% of samples) | 15.77 | 15.23 | -3.4% | -0.958 to -0.1247 | yes: GAIN |
| failed requests (%) | 0.02151 | 0 | -100.0% | -0.05394 to +0.01093 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.4 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 | +12.3 (native is 0) | +11.82 to +12.78 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.8 | 193.5 | +1.4% | -1.782 to +7.066 | no |
| utilisation (used / allocatable) | 0.06321 | 0.07323 | +15.9% | +0.004708 to +0.01533 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 1.514 | -0.2% | -0.03309 to +0.02646 | no |
| Omni's own CPU (cores), mean | 0 | 0.02334 | +0.0233 (native is 0) | +0.0193 to +0.02738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.537 | +1.3% | -0.01235 to +0.05239 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.3 | 394.6 | -10.2% | -75.58 to -13.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.119 | +5.4% | -0.1482 to +0.3645 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 43.25 | 44.04 | +1.8% | +0.5296 to +1.058 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 589.6 | 593.8 | +0.7% | +1.113 to +7.287 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.662 | -22.3% | -1.972 to -0.7052 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*