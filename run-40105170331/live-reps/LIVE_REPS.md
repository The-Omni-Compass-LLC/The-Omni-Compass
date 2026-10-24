# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.968 |
| node-hours | 4.153 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 447.7 | 447.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 446.1 | 445.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 174.5 | 98.72 |
| response time (ms), 95th percentile | 346 | 123 |
| response time (ms), 99th percentile | 585.9 | 220.7 |
| time over the response line (% of samples) | 3.613 | 2.287 |
| failed requests (%) | 2.08 | 1.857 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4 | 0.525 |
| utilisation (used / allocatable) | 0.05389 | 0.05217 |
| CPU used (cores), mean | 1.287 | 1.245 |
| Omni's own CPU (cores), mean | 0 | 0.00862 |
| CPU used with Omni's own (cores), mean | 1.287 | 1.254 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 507.2 | 521.4 |
| HPA replicas, mean | 8.866 | 9.073 |
| pods started | 7.9 | 8.9 |
| pod start wait, total (s) | 12.8 | 16.8 |
| pod start wait, mean (s) | 1.625 | 1.818 |
| host CPU busy, the real machine under kind (%) | 38.37 | 37.56 |
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
| worker nodes in service, mean | 5.97 | 5.968 | −0.0% | −0.0056 to +0.0020 | no |
| node-hours | 4.153 | 4.159 | +0.1% | +0.0014 to +0.0107 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 447.7 | 447.6 | −0.0% | −0.9530 to +0.7800 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 446.1 | 445.9 | −0.0% | −0.9964 to +0.6317 | no |
| response time (ms), mean | 174.5 | 98.72 | −43.4% | −87.4583 to −64.0697 | yes: GAIN |
| response time (ms), 95th percentile | 346 | 123 | −64.5% | −250.1783 to −195.8177 | yes: GAIN |
| response time (ms), 99th percentile | 585.9 | 220.7 | −62.3% | −431.4910 to −298.9168 | yes: GAIN |
| time over the response line (% of samples) | 3.613 | 2.287 | −36.7% | −1.8058 to −0.8481 | yes: GAIN |
| failed requests (%) | 2.08 | 1.857 | −10.7% | −0.3934 to −0.0528 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 8 | −20.0% | −3.0663 to −0.9337 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.100 (native is 0) | +42.9796 to +55.2204 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4 | 0.525 | +31.2% | −0.4474 to +0.6974 | no |
| utilisation (used / allocatable) | 0.05389 | 0.05217 | −3.2% | −0.0026 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.287 | 1.245 | −3.2% | −0.0628 to −0.0200 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00862 | +0.009 (native is 0) | +0.0082 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.287 | 1.254 | −2.5% | −0.0540 to −0.0116 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 507.2 | 521.4 | +2.8% | +7.3620 to +21.1685 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.866 | 9.073 | +2.3% | −0.3644 to +0.7780 | no |
| pods started | 7.9 | 8.9 | +12.7% | −0.7194 to +2.7194 | no |
| pod start wait, total (s) | 12.8 | 16.8 | +31.2% | −1.5202 to +9.5202 | no |
| pod start wait, mean (s) | 1.625 | 1.818 | +11.8% | −0.1834 to +0.5683 | no |
| host CPU busy, the real machine under kind (%) | 38.37 | 37.56 | −2.1% | −1.2803 to −0.3492 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 77 | 4.3 |  |
| machine down | omni | 41 | 1.3 | -36 s (-47%) |
| spike | native | 282 | 83.2 |  |
| spike | omni | 281 | 80.5 | -1 s (-0%) |
| runaway pod started | native | 5 | 0.1 |  |
| runaway pod started | omni | 3 | 0.0 | -2 s (-49%) |
| probe blind | native | 84 | 1.2 |  |
| probe blind | omni | 60 | 0.1 | -24 s (-28%) |
| api frozen | native | 10 | 0.3 |  |
| api frozen | omni | 4 | 0.0 | -6 s (-62%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-54%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*