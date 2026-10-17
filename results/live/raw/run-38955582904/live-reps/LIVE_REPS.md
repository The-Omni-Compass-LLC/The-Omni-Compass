# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.095 |
| node-hours | 2.516 | 2.132 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 243.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 468.5 | 424.3 |
| response time (ms), 95th percentile | 2811 | 2836 |
| response time (ms), 99th percentile | 4279 | 4281 |
| time over the response line (% of samples) | 15.39 | 14.71 |
| failed requests (%) | 0.02168 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 179.8 | 181.8 |
| utilisation (used / allocatable) | 0.05973 | 0.07082 |
| CPU used (cores), mean | 1.433 | 1.433 |
| Omni's own CPU (cores), mean | 0 | 0.01905 |
| CPU used with Omni's own (cores), mean | 1.433 | 1.452 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 408.2 |
| HPA replicas, mean | 2.031 | 2.185 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 4.1 | 0.5 |
| pod start wait, mean (s) | 4.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 40.86 | 41.78 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 555.1 | 561.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 |

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
| worker nodes in service, mean | 6 | 5.095 | -15.1% | -1.57 to -0.239 | yes: GAIN |
| node-hours | 2.516 | 2.132 | -15.2% | -0.6609 to -0.1055 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 | -0.0% | -0.8447 to +0.5924 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 243.9 | -10.5% | -49.33 to -7.76 | yes: GAIN |
| response time (ms), mean | 468.5 | 424.3 | -9.4% | -65.7 to -22.78 | yes: GAIN |
| response time (ms), 95th percentile | 2811 | 2836 | +0.9% | -155.4 to +206.1 | no |
| response time (ms), 99th percentile | 4279 | 4281 | +0.1% | -202.5 to +207 | no |
| time over the response line (% of samples) | 15.39 | 14.71 | -4.4% | -1.158 to -0.2086 | yes: GAIN |
| failed requests (%) | 0.02168 | 0 | -100.0% | -0.05437 to +0.01101 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.6 (native is 0) | +10.52 to +12.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 179.8 | 181.8 | +1.1% | -3.269 to +7.179 | no |
| utilisation (used / allocatable) | 0.05973 | 0.07082 | +18.6% | +0.002829 to +0.01935 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.433 | 1.433 | -0.0% | -0.0199 to +0.019 | no |
| Omni's own CPU (cores), mean | 0 | 0.01905 | +0.0191 (native is 0) | +0.01556 to +0.02254 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.452 | +1.3% | -0.001 to +0.0382 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 408.2 | -11.7% | -95.68 to -12.11 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.031 | 2.185 | +7.6% | -0.1516 to +0.459 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 4.1 | 0.5 | -87.8% | -12.76 to +5.562 | no |
| pod start wait, mean (s) | 4.1 | 0.5 | -87.8% | -12.76 to +5.562 | no |
| host CPU busy, the real machine under kind (%) | 40.86 | 41.78 | +2.3% | +0.3741 to +1.473 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 555.1 | 561.5 | +1.2% | -2.762 to +15.56 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 | -22.4% | -2.303 to -0.3851 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*