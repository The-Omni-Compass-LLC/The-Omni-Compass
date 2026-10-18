# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.331 | 4.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.7 | 480.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.7 | 480.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 285.1 | 146 |
| response time (ms), 95th percentile | 768.3 | 350.1 |
| response time (ms), 99th percentile | 1398 | 860.4 |
| time over the response line (% of samples) | 13.13 | 3.694 |
| failed requests (%) | 1.11 | 0.9581 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.905 | 0.8633 |
| utilisation (used / allocatable) | 0.0811 | 0.07759 |
| CPU used (cores), mean | 1.946 | 1.862 |
| Omni's own CPU (cores), mean | 0 | 0.00926 |
| CPU used with Omni's own (cores), mean | 1.946 | 1.871 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 365 | 378.5 |
| HPA replicas, mean | 9.789 | 10.52 |
| pods started | 5.4 | 13.1 |
| pod start wait, total (s) | 24.5 | 30.8 |
| pod start wait, mean (s) | 3.983 | 2.365 |
| host CPU busy, the real machine under kind (%) | 56 | 54.26 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 4.331 | 4.334 | +0.1% | -0.00483 to +0.01116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482.7 | 480.7 | -0.4% | -3.009 to -0.922 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.7 | 480.7 | -0.4% | -3.009 to -0.922 | yes: GAIN |
| response time (ms), mean | 285.1 | 146 | -48.8% | -174.7 to -103.5 | yes: GAIN |
| response time (ms), 95th percentile | 768.3 | 350.1 | -54.4% | -513.2 to -323.1 | yes: GAIN |
| response time (ms), 99th percentile | 1398 | 860.4 | -38.4% | -702 to -372.5 | yes: GAIN |
| time over the response line (% of samples) | 13.13 | 3.694 | -71.9% | -13.24 to -5.636 | yes: GAIN |
| failed requests (%) | 1.11 | 0.9581 | -13.7% | -0.2749 to -0.02809 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 7.8 | -66.5% | -19.52 to -11.48 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.6 | +52.6 (native is 0) | +34.57 to +70.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.905 | 0.8633 | -4.6% | -0.5537 to +0.4704 | no |
| utilisation (used / allocatable) | 0.0811 | 0.07759 | -4.3% | -0.004464 to -0.002566 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.946 | 1.862 | -4.3% | -0.1071 to -0.06158 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00926 | +0.00926 (native is 0) | +0.007194 to +0.01133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.946 | 1.871 | -3.9% | -0.09712 to -0.05308 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 365 | 378.5 | +3.7% | +9.399 to +17.5 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.789 | 10.52 | +7.4% | -0.3532 to +1.805 | no |
| pods started | 5.4 | 13.1 | +142.6% | +4.147 to +11.25 | yes: power given |
| pod start wait, total (s) | 24.5 | 30.8 | +25.7% | -4.884 to +17.48 | no |
| pod start wait, mean (s) | 3.983 | 2.365 | -40.6% | -2.703 to -0.5338 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 56 | 54.26 | -3.1% | -2.305 to -1.182 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*