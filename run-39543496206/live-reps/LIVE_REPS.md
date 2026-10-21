# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.145 |
| node-hours | 2.515 | 2.154 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 244.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 330.7 | 298.6 |
| response time (ms), 95th percentile | 1147 | 1206 |
| response time (ms), 99th percentile | 1663 | 1754 |
| time over the response line (% of samples) | 16.75 | 15.98 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.307 | 10.22 |
| utilisation (used / allocatable) | 0.05808 | 0.06812 |
| CPU used (cores), mean | 1.394 | 1.392 |
| Omni's own CPU (cores), mean | 0 | 0.01604 |
| CPU used with Omni's own (cores), mean | 1.394 | 1.408 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.9 | 425.9 |
| HPA replicas, mean | 1.979 | 2.278 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 1.5 |
| pod start wait, mean (s) | 0 | 1.15 |
| host CPU busy, the real machine under kind (%) | 40.6 | 41.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 777.6 | 781.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.57 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2958 | 0.5042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 3.7 |
| queue: job turnaround, submitted to done, mean (s) | 82.88 | 85.96 |
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
| worker nodes in service, mean | 6 | 5.145 | -14.3% | -1.671 to -0.03945 | yes: GAIN |
| node-hours | 2.515 | 2.154 | -14.3% | -0.7015 to -0.01886 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | -0.0% | -1.04 to +0.962 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 244.7 | -9.9% | -52.59 to -1.296 | yes: GAIN |
| response time (ms), mean | 330.7 | 298.6 | -9.7% | -45.06 to -19.11 | yes: GAIN |
| response time (ms), 95th percentile | 1147 | 1206 | +5.2% | -27.06 to +145.8 | no |
| response time (ms), 99th percentile | 1663 | 1754 | +5.5% | -59.63 to +241.4 | no |
| time over the response line (% of samples) | 16.75 | 15.98 | -4.6% | -1.48 to -0.05226 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.8 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 | +41.5 (native is 0) | +21.21 to +61.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.307 | 10.22 | +9.8% | -1.835 to +3.661 | no |
| utilisation (used / allocatable) | 0.05808 | 0.06812 | +17.3% | +0.0006484 to +0.01943 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.392 | -0.2% | -0.0334 to +0.02879 | no |
| Omni's own CPU (cores), mean | 0 | 0.01604 | +0.016 (native is 0) | +0.01477 to +0.01731 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.408 | +1.0% | -0.01789 to +0.04536 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.9 | 425.9 | -11.6% | -109.2 to -2.749 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.278 | +15.1% | +0.04823 to +0.5496 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | -0.09056 to +3.091 | no |
| pod start wait, mean (s) | 0 | 1.15 | +1.15 (native is 0) | +0.1662 to +2.134 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.6 | 41.48 | +2.2% | +0.6624 to +1.097 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 777.6 | 781.1 | +0.5% | -0.9384 to +7.938 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.57 | -23.8% | -2.734 to -0.1268 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2958 | 0.5042 | +70.4% | -0.236 to +0.6526 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 3.7 | +236.4% | -2.787 to +7.987 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.88 | 85.96 | +3.7% | -0.5093 to +6.676 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*