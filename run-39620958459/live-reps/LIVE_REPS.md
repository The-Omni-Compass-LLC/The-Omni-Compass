# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.288 |
| node-hours | 2.516 | 2.215 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 250 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 409.6 | 357 |
| response time (ms), 95th percentile | 1523 | 1462 |
| response time (ms), 99th percentile | 2205 | 2163 |
| time over the response line (% of samples) | 21.76 | 20.47 |
| failed requests (%) | 0 | 0.00995 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 10.52 |
| utilisation (used / allocatable) | 0.06015 | 0.06784 |
| CPU used (cores), mean | 1.444 | 1.437 |
| Omni's own CPU (cores), mean | 0 | 0.01635 |
| CPU used with Omni's own (cores), mean | 1.444 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 421.6 |
| HPA replicas, mean | 1.931 | 2.244 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 1.7 |
| pod start wait, mean (s) | 0 | 1.7 |
| host CPU busy, the real machine under kind (%) | 42.05 | 42.56 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 801.3 | 799.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.725 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.2042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 104.7 |
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
| worker nodes in service, mean | 6 | 5.288 | -11.9% | -1.463 to +0.03806 | no |
| node-hours | 2.516 | 2.215 | -12.0% | -0.6143 to +0.01225 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.5 | -0.1% | -1.173 to +0.8326 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 250 | -8.3% | -45.8 to +0.5828 | no |
| response time (ms), mean | 409.6 | 357 | -12.8% | -91.97 to -13.17 | yes: GAIN |
| response time (ms), 95th percentile | 1523 | 1462 | -4.0% | -258.5 to +136.3 | no |
| response time (ms), 99th percentile | 2205 | 2163 | -1.9% | -381.4 to +297.9 | no |
| time over the response line (% of samples) | 21.76 | 20.47 | -5.9% | -2.466 to -0.1066 | yes: GAIN |
| failed requests (%) | 0 | 0.00995 | +0.00995 (native is 0) | -0.01256 to +0.03246 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.9 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.1 | +39.1 (native is 0) | +15.29 to +62.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.79 | 10.52 | -2.5% | -1.474 to +0.9307 | no |
| utilisation (used / allocatable) | 0.06015 | 0.06784 | +12.8% | -0.0009454 to +0.01632 | no |
| CPU used (cores), mean | 1.444 | 1.437 | -0.4% | -0.04969 to +0.0371 | no |
| Omni's own CPU (cores), mean | 0 | 0.01635 | +0.0163 (native is 0) | +0.01565 to +0.01705 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.444 | 1.454 | +0.7% | -0.03328 to +0.05338 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 421.6 | -11.1% | -118.1 to +13.25 | no |
| HPA replicas, mean | 1.931 | 2.244 | +16.2% | +0.1116 to +0.5132 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 1.7 | +1.7 (native is 0) | +0.3919 to +3.008 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.7 | +1.7 (native is 0) | +0.3919 to +3.008 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.05 | 42.56 | +1.2% | -0.3284 to +1.348 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 801.3 | 799.5 | -0.2% | -15.68 to +12.08 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.725 | -21.3% | -2.59 to +0.03951 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.2042 | -21.0% | -0.1259 to +0.01754 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 104.7 | -3.3% | -16.09 to +8.898 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*