# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 172.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 511.2 | 461.3 |
| response time (ms), 95th percentile | 2034 | 2040 |
| response time (ms), 99th percentile | 5226 | 5407 |
| time over the response line (% of samples) | 23.49 | 22.39 |
| failed requests (%) | 2.575 | 2.305 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9333 | 0.6067 |
| utilisation (used / allocatable) | 0.09753 | 0.09714 |
| CPU used (cores), mean | 2.341 | 2.331 |
| Omni's own CPU (cores), mean | 0 | 0.01073 |
| CPU used with Omni's own (cores), mean | 2.341 | 2.342 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.3 | 297.3 |
| HPA replicas, mean | 15.23 | 15.12 |
| pods started | 4.4 | 4.7 |
| pod start wait, total (s) | 10.5 | 11.6 |
| pod start wait, mean (s) | 2.14 | 2.298 |
| host CPU busy, the real machine under kind (%) | 67.61 | 67.54 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 276.3 | 288.7 |
| second app: response time (ms), 99th percentile | 2441 | 2169 |
| second app: time over the response line (% of samples) | 14.5 | 14.62 |
| second app: failed requests (%) | 12.17 | 12.37 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.108e-16 to +1.066e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | -0.000783 to +0.004116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.7 | +0.1% | -0.2249 to +0.6534 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 172.7 | +0.1% | -0.2249 to +0.6534 | no |
| response time (ms), mean | 511.2 | 461.3 | -9.8% | -77.91 to -21.95 | yes: GAIN |
| response time (ms), 95th percentile | 2034 | 2040 | +0.3% | -212.4 to +225.2 | no |
| response time (ms), 99th percentile | 5226 | 5407 | +3.5% | -466.8 to +828.7 | no |
| time over the response line (% of samples) | 23.49 | 22.39 | -4.7% | -2.768 to +0.5655 | no |
| failed requests (%) | 2.575 | 2.305 | -10.5% | -1.025 to +0.4864 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.7 | -3.3% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.8 | +32.8 (native is 0) | +30.81 to +34.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9333 | 0.6067 | -35.0% | -1.094 to +0.4406 | no |
| utilisation (used / allocatable) | 0.09753 | 0.09714 | -0.4% | -0.001786 to +0.00102 | no |
| CPU used (cores), mean | 2.341 | 2.331 | -0.4% | -0.04286 to +0.02447 | no |
| Omni's own CPU (cores), mean | 0 | 0.01073 | +0.0107 (native is 0) | +0.009713 to +0.01175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.341 | 2.342 | +0.1% | -0.03197 to +0.03505 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.3 | 297.3 | +0.3% | -3.121 to +5.027 | no |
| HPA replicas, mean | 15.23 | 15.12 | -0.7% | -0.3657 to +0.1565 | no |
| pods started | 4.4 | 4.7 | +6.8% | -0.6567 to +1.257 | no |
| pod start wait, total (s) | 10.5 | 11.6 | +10.5% | -2.953 to +5.153 | no |
| pod start wait, mean (s) | 2.14 | 2.298 | +7.4% | -0.464 to +0.7797 | no |
| host CPU busy, the real machine under kind (%) | 67.61 | 67.54 | -0.1% | -0.8101 to +0.6729 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 276.3 | 288.7 | +4.5% | -29.8 to +54.57 | no |
| second app: response time (ms), 99th percentile | 2441 | 2169 | -11.1% | -1791 to +1248 | no |
| second app: time over the response line (% of samples) | 14.5 | 14.62 | +0.8% | -0.3765 to +0.605 | no |
| second app: failed requests (%) | 12.17 | 12.37 | +1.6% | -0.5635 to +0.9609 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*