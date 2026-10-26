# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 158.8 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 158.8 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 161.6 | 82.88 | 86.73 |
| response time (ms), 95th percentile | 359.6 | 123.2 | 106.8 |
| response time (ms), 99th percentile | 580.3 | 168.5 | 137.7 |
| time over the response line (% of samples) | 2.263 | 0.03636 | 0.3278 |
| failed requests (%) | 0 | 0 | 0.07362 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | 0.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | 70.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1883 | 0.08 |
| utilisation (used / allocatable) | 0.0403 | 0.0384 | 0.03749 |
| CPU used (cores), mean | 0.9673 | 0.9216 | 0.8998 |
| Omni's own CPU (cores), mean | 0 | 0.00849 | 0.01204 |
| CPU used with Omni's own (cores), mean | 0.9673 | 0.9301 | 0.9118 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 680.3 | 708.6 | 723.6 |
| HPA replicas, mean | 8.619 | 8.369 | 1 |
| pods started | 4.8 | 3.8 | 0 |
| pod start wait, total (s) | 8.2 | 5.8 | 0 |
| pod start wait, mean (s) | 1.695 | 1.468 | 0 |
| host CPU busy, the real machine under kind (%) | 29.02 | 27.97 | 27.41 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0083 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 158.8 | −0.4% | −1.3263 to +0.0995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 158.8 | −0.4% | −1.3263 to +0.0995 | no |
| response time (ms), mean | 161.6 | 82.88 | −48.7% | −97.7144 to −59.6863 | yes: GAIN |
| response time (ms), 95th percentile | 359.6 | 123.2 | −65.7% | −290.8786 to −181.9664 | yes: GAIN |
| response time (ms), 99th percentile | 580.3 | 168.5 | −71.0% | −506.6194 to −316.9846 | yes: GAIN |
| time over the response line (% of samples) | 2.263 | 0.03636 | −98.4% | −3.3869 to −1.0673 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | −100.0% | −4.0775 to −1.1225 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +14.8449 to +20.7551 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1883 | +41.2% | −0.2299 to +0.3399 | no |
| utilisation (used / allocatable) | 0.0403 | 0.0384 | −4.7% | −0.0028 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9673 | 0.9216 | −4.7% | −0.0683 to −0.0231 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00849 | +0.008 (native is 0) | +0.0072 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9673 | 0.9301 | −3.8% | −0.0591 to −0.0153 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 680.3 | 708.6 | +4.2% | +17.6365 to +39.0125 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.619 | 8.369 | −2.9% | −0.8232 to +0.3239 | no |
| pods started | 4.8 | 3.8 | −20.8% | −2.2617 to +0.2617 | no |
| pod start wait, total (s) | 8.2 | 5.8 | −29.3% | −4.8595 to +0.0595 | no |
| pod start wait, mean (s) | 1.695 | 1.468 | −13.4% | −0.5357 to +0.0824 | no |
| host CPU busy, the real machine under kind (%) | 29.02 | 27.97 | −3.6% | −1.5484 to −0.5541 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.2% | −0.0066 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.5 | +0.0% | −0.9208 to +0.9388 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.5 | +0.0% | −0.9208 to +0.9388 | no |
| response time (ms), mean | 161.6 | 86.73 | −46.3% | −94.7986 to −54.9099 | yes: GAIN |
| response time (ms), 95th percentile | 359.6 | 106.8 | −70.3% | −315.7387 to −189.9183 | yes: GAIN |
| response time (ms), 99th percentile | 580.3 | 137.7 | −76.3% | −554.0455 to −331.1959 | yes: GAIN |
| time over the response line (% of samples) | 2.263 | 0.3278 | −85.5% | −3.1353 to −0.7361 | yes: GAIN |
| failed requests (%) | 0 | 0.07362 | +0.074 (native is 0) | +0.0283 to +0.1189 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0.6 | −76.9% | −3.5816 to −0.4184 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.6 | +70.600 (native is 0) | +69.1225 to +72.0775 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08 | −40.0% | −0.2038 to +0.0971 | no |
| utilisation (used / allocatable) | 0.0403 | 0.03749 | −7.0% | −0.0040 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9673 | 0.8998 | −7.0% | −0.0962 to −0.0389 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01204 | +0.012 (native is 0) | +0.0106 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9673 | 0.9118 | −5.7% | −0.0831 to −0.0279 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 680.3 | 723.6 | +6.4% | +29.8865 to +56.6992 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.619 | 1 | −88.4% | −8.2046 to −7.0331 | yes: GAIN |
| pods started | 4.8 | 0 | −100.0% | −5.2524 to −4.3476 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 0 | −100.0% | −9.8450 to −6.5550 | yes: GAIN |
| pod start wait, mean (s) | 1.695 | 0 | −100.0% | −1.9373 to −1.4527 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.02 | 27.41 | −5.5% | −2.2363 to −0.9747 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.517 | +0.3% | −0.0060 to +0.0147 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.5 | +0.4% | −0.4311 to +1.6760 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.5 | +0.4% | −0.4311 to +1.6760 | no |
| response time (ms), mean | 82.88 | 86.73 | +4.6% | +1.8076 to +5.8847 | yes: LOSS |
| response time (ms), 95th percentile | 123.2 | 106.8 | −13.3% | −25.5423 to −7.2697 | yes: GAIN |
| response time (ms), 99th percentile | 168.5 | 137.7 | −18.3% | −51.9508 to −9.6866 | yes: GAIN |
| time over the response line (% of samples) | 0.03636 | 0.3278 | +801.3% | +0.1626 to +0.4202 | yes: LOSS |
| failed requests (%) | 0 | 0.07362 | +0.074 (native is 0) | +0.0283 to +0.1189 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 70.6 | +296.6% | +50.0031 to +55.5969 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.08 | −57.5% | −0.3166 to +0.0999 | no |
| utilisation (used / allocatable) | 0.0384 | 0.03749 | −2.4% | −0.0016 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9216 | 0.8998 | −2.4% | −0.0387 to −0.0049 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00849 | 0.01204 | +41.8% | +0.0032 to +0.0039 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9301 | 0.9118 | −2.0% | −0.0352 to −0.0014 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 708.6 | 723.6 | +2.1% | +4.8030 to +25.1337 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.369 | 1 | −88.1% | −8.3556 to −6.3828 | yes: GAIN |
| pods started | 3.8 | 0 | −100.0% | −4.9081 to −2.6919 | yes: GAIN |
| pod start wait, total (s) | 5.8 | 0 | −100.0% | −7.9801 to −3.6199 | yes: GAIN |
| pod start wait, mean (s) | 1.468 | 0 | −100.0% | −1.7476 to −1.1891 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.97 | 27.41 | −2.0% | −0.9219 to −0.1866 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*