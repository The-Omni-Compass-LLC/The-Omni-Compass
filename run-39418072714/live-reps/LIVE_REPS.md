# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.528 |
| node-hours | 2.517 | 2.316 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 259.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 495.4 | 450.6 |
| response time (ms), 95th percentile | 1858 | 1918 |
| response time (ms), 99th percentile | 2626 | 2769 |
| time over the response line (% of samples) | 27.27 | 25.99 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 12.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.06 | 13.51 |
| utilisation (used / allocatable) | 0.06567 | 0.07122 |
| CPU used (cores), mean | 1.576 | 1.574 |
| Omni's own CPU (cores), mean | 0 | 0.01778 |
| CPU used with Omni's own (cores), mean | 1.576 | 1.592 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.7 | 396.6 |
| HPA replicas, mean | 1.982 | 2.233 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.4 | 0.6 |
| pod start wait, mean (s) | 0.4 | 0.6 |
| host CPU busy, the real machine under kind (%) | 45.41 | 46.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 826.1 | 831.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.098 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3583 | 0.4708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2 |
| queue: job turnaround, submitted to done, mean (s) | 132.4 | 137.2 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.528 | -7.9% | -1.014 to +0.07052 | no |
| node-hours | 2.517 | 2.316 | -8.0% | -0.425 to +0.02257 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.4 | -0.1% | -1.405 to +0.6338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 259.5 | -5.5% | -32.19 to +1.764 | no |
| response time (ms), mean | 495.4 | 450.6 | -9.0% | -64.49 to -25.09 | yes: GAIN |
| response time (ms), 95th percentile | 1858 | 1918 | +3.2% | -37.55 to +157.5 | no |
| response time (ms), 99th percentile | 2626 | 2769 | +5.5% | +10.72 to +276.3 | yes: LOSS |
| time over the response line (% of samples) | 27.27 | 25.99 | -4.7% | -2.045 to -0.5165 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 12.8 | +0.8% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.8 (native is 0) | +20.9 to +46.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.06 | 13.51 | +3.5% | -1.482 to +2.386 | no |
| utilisation (used / allocatable) | 0.06567 | 0.07122 | +8.5% | +0.0001789 to +0.01093 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.576 | 1.574 | -0.1% | -0.02967 to +0.02633 | no |
| Omni's own CPU (cores), mean | 0 | 0.01778 | +0.0178 (native is 0) | +0.016 to +0.01956 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.576 | 1.592 | +1.0% | -0.01213 to +0.04435 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.7 | 396.6 | -6.0% | -52.05 to +1.787 | no |
| HPA replicas, mean | 1.982 | 2.233 | +12.7% | +0.05659 to +0.4463 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | -0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | -0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 45.41 | 46.48 | +2.4% | +0.8348 to +1.305 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 826.1 | 831.1 | +0.6% | -0.6826 to +10.68 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.098 | -15.0% | -1.836 to +0.03192 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3583 | 0.4708 | +31.4% | -0.05903 to +0.284 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2 | +66.7% | -0.1417 to +1.742 | no |
| queue: job turnaround, submitted to done, mean (s) | 132.4 | 137.2 | +3.6% | -1.23 to +10.85 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*