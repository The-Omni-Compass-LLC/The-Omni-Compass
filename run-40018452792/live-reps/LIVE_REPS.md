# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 171.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 171.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 486.3 | 439.8 |
| response time (ms), 95th percentile | 1946 | 1880 |
| response time (ms), 99th percentile | 5102 | 5115 |
| time over the response line (% of samples) | 22.75 | 22.33 |
| failed requests (%) | 3.449 | 2.653 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.148 | 0.5617 |
| utilisation (used / allocatable) | 0.09401 | 0.09414 |
| CPU used (cores), mean | 2.256 | 2.259 |
| Omni's own CPU (cores), mean | 0 | 0.01263 |
| CPU used with Omni's own (cores), mean | 2.256 | 2.272 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.6 | 308.1 |
| HPA replicas, mean | 14.93 | 15.09 |
| pods started | 5.8 | 5.1 |
| pod start wait, total (s) | 10.1 | 9 |
| pod start wait, mean (s) | 1.749 | 1.682 |
| host CPU busy, the real machine under kind (%) | 65.47 | 65.69 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 356.2 | 477.1 |
| second app: response time (ms), 99th percentile | 2234 | 2847 |
| second app: time over the response line (% of samples) | 13.95 | 14.21 |
| second app: failed requests (%) | 11.62 | 11.51 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.338e-16 to +4.785e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.514 | -0.2% | -0.009389 to +0.004389 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 171.7 | -0.1% | -1.151 to +0.638 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 171.7 | -0.1% | -1.151 to +0.638 | no |
| response time (ms), mean | 486.3 | 439.8 | -9.6% | -71.23 to -21.85 | yes: GAIN |
| response time (ms), 95th percentile | 1946 | 1880 | -3.4% | -304.1 to +172.2 | no |
| response time (ms), 99th percentile | 5102 | 5115 | +0.3% | -499.7 to +525.5 | no |
| time over the response line (% of samples) | 22.75 | 22.33 | -1.8% | -2.135 to +1.295 | no |
| failed requests (%) | 3.449 | 2.653 | -23.1% | -1.694 to +0.1024 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 | -5.7% | -1.408 to +0.4079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.5 | +45.5 (native is 0) | +34.48 to +56.52 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.148 | 0.5617 | -51.1% | -1.891 to +0.7178 | no |
| utilisation (used / allocatable) | 0.09401 | 0.09414 | +0.1% | -0.001803 to +0.002065 | no |
| CPU used (cores), mean | 2.256 | 2.259 | +0.1% | -0.04327 to +0.04957 | no |
| Omni's own CPU (cores), mean | 0 | 0.01263 | +0.0126 (native is 0) | +0.01186 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.256 | 2.272 | +0.7% | -0.03027 to +0.06183 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.6 | 308.1 | -0.5% | -10.58 to +7.452 | no |
| HPA replicas, mean | 14.93 | 15.09 | +1.1% | -0.2305 to +0.5543 | no |
| pods started | 5.8 | 5.1 | -12.1% | -1.458 to +0.05776 | no |
| pod start wait, total (s) | 10.1 | 9 | -10.9% | -3.89 to +1.69 | no |
| pod start wait, mean (s) | 1.749 | 1.682 | -3.8% | -0.4769 to +0.3431 | no |
| host CPU busy, the real machine under kind (%) | 65.47 | 65.69 | +0.3% | -0.5108 to +0.9408 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 356.2 | 477.1 | +34.0% | -107.8 to +349.7 | no |
| second app: response time (ms), 99th percentile | 2234 | 2847 | +27.5% | -172.2 to +1400 | no |
| second app: time over the response line (% of samples) | 13.95 | 14.21 | +1.9% | -0.2752 to +0.8067 | no |
| second app: failed requests (%) | 11.62 | 11.51 | -1.0% | -0.7176 to +0.4882 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*