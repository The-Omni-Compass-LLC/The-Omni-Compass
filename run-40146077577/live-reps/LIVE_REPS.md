# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.836 | 4.972 |
| node-hours | 2.516 | 2.514 | 2.026 | 2.08 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.7 | 271 | 270.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 270.7 | 234.4 | 238.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 262.8 | 281.7 | 241 | 257.1 |
| response time (ms), 95th percentile | 827.8 | 920.3 | 894.3 | 951.8 |
| response time (ms), 99th percentile | 1201 | 1347 | 1299 | 1438 |
| time over the response line (% of samples) | 13.65 | 14.37 | 13.97 | 14.74 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.2 | 7 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38.2 | 57.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 8.782 | 10.48 | 8.355 |
| utilisation (used / allocatable) | 0.05667 | 0.05579 | 0.07081 | 0.0679 |
| CPU used (cores), mean | 1.36 | 1.339 | 1.346 | 1.327 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01564 | 0.017 |
| CPU used with Omni's own (cores), mean | 1.36 | 1.339 | 1.362 | 1.344 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 497.1 | 416.6 | 431.7 |
| HPA replicas, mean | 2.06 | 1.986 | 2.199 | 2.302 |
| pods started | 0 | 0.1 | 0.5 | 0.4 |
| pod start wait, total (s) | 0 | 0.1 | 0.9 | 0.5 |
| pod start wait, mean (s) | 0 | 0.1 | 0.9 | 0.5 |
| host CPU busy, the real machine under kind (%) | 38.43 | 39.31 | 39.46 | 40.32 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 751.4 | 760.8 | 756.5 | 761.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.021 | 4.304 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.1583 | 0.04167 | 0.15 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.7 | 0.3 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 60.01 | 67.13 | 62.67 | 69.11 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

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
| worker nodes in service, mean | 6 | 4.972 | −17.1% | −1.8869 to −0.1685 | yes: GAIN |
| node-hours | 2.514 | 2.08 | −17.3% | −0.7945 to −0.0733 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.4 | −0.1% | −0.9585 to +0.3682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 238.2 | −12.0% | −59.4468 to −5.5977 | yes: GAIN |
| response time (ms), mean | 281.7 | 257.1 | −8.7% | −36.9909 to −12.1755 | yes: GAIN |
| response time (ms), 95th percentile | 920.3 | 951.8 | +3.4% | −19.6791 to +82.7911 | no |
| response time (ms), 99th percentile | 1347 | 1438 | +6.7% | +44.6420 to +136.8316 | yes: LOSS |
| time over the response line (% of samples) | 14.37 | 14.74 | +2.6% | −0.4647 to +1.2140 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.9 | +9.7% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.7 | +57.700 (native is 0) | +34.1780 to +81.2220 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.782 | 8.355 | −4.9% | −1.8079 to +0.9546 | no |
| utilisation (used / allocatable) | 0.05579 | 0.0679 | +21.7% | +0.0016 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 1.327 | −0.9% | −0.0283 to +0.0047 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.0152 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.344 | +0.4% | −0.0112 to +0.0217 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.1 | 431.7 | −13.2% | −124.4929 to −6.4628 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.302 | +15.9% | +0.0921 to +0.5401 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 39.31 | 40.32 | +2.6% | +0.6177 to +1.4161 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 760.8 | 761.3 | +0.1% | −4.2955 to +5.2955 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.304 | −28.3% | −3.0507 to −0.3412 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.15 | −5.3% | −0.0422 to +0.0255 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.13 | 69.11 | +3.0% | −2.7528 to +6.7195 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0104 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.7 | −0.3% | −1.6318 to +0.2421 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 270.7 | −0.3% | −1.6318 to +0.2421 | no |
| response time (ms), mean | 262.8 | 281.7 | +7.2% | +1.0755 to +36.6648 | yes: LOSS |
| response time (ms), 95th percentile | 827.8 | 920.3 | +11.2% | −8.2136 to +193.1286 | no |
| response time (ms), 99th percentile | 1201 | 1347 | +12.1% | −15.4778 to +306.6774 | no |
| time over the response line (% of samples) | 13.65 | 14.37 | +5.2% | +0.0742 to +1.3518 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.2 | +2.9% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 8.782 | −4.3% | −2.7334 to +1.9368 | no |
| utilisation (used / allocatable) | 0.05667 | 0.05579 | −1.6% | −0.0028 to +0.0011 | no |
| CPU used (cores), mean | 1.36 | 1.339 | −1.6% | −0.0681 to +0.0257 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.36 | 1.339 | −1.6% | −0.0681 to +0.0257 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 497.1 | +2.4% | −11.1925 to +34.7262 | no |
| HPA replicas, mean | 2.06 | 1.986 | −3.6% | −0.2340 to +0.0863 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 38.43 | 39.31 | +2.3% | +0.3850 to +1.3791 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.4 | 760.8 | +1.3% | +2.5872 to +16.2128 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.1583 | +533.3% | +0.0634 to +0.2033 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.7 | +600.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.01 | 67.13 | +11.9% | +0.7174 to +13.5243 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.836 | −19.4% | −1.9792 to −0.3492 | yes: GAIN |
| node-hours | 2.516 | 2.026 | −19.5% | −0.8317 to −0.1484 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271 | −0.1% | −0.9967 to +0.3045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 234.4 | −13.6% | −62.7178 to −11.1827 | yes: GAIN |
| response time (ms), mean | 262.8 | 241 | −8.3% | −38.9632 to −4.5604 | yes: GAIN |
| response time (ms), 95th percentile | 827.8 | 894.3 | +8.0% | −31.6774 to +164.6074 | no |
| response time (ms), 99th percentile | 1201 | 1299 | +8.1% | −68.3139 to +263.4777 | no |
| time over the response line (% of samples) | 13.65 | 13.97 | +2.3% | −0.2948 to +0.9321 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 | +38.200 (native is 0) | +26.2744 to +50.1256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 10.48 | +14.2% | −0.6610 to +3.2610 | no |
| utilisation (used / allocatable) | 0.05667 | 0.07081 | +24.9% | +0.0040 to +0.0243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.36 | 1.346 | −1.0% | −0.0501 to +0.0221 | no |
| Omni's own CPU (cores), mean | 0 | 0.01564 | +0.016 (native is 0) | +0.0135 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.36 | 1.362 | +0.1% | −0.0357 to +0.0390 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 416.6 | −14.2% | −118.6693 to −18.9450 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 2.199 | +6.8% | −0.1022 to +0.3806 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| host CPU busy, the real machine under kind (%) | 38.43 | 39.46 | +2.7% | +0.5743 to +1.4881 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.4 | 756.5 | +0.7% | −1.3108 to +11.5108 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.021 | −33.0% | −3.2835 to −0.6749 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.04167 | +66.7% | −0.0154 to +0.0487 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.01 | 62.67 | +4.4% | −2.6861 to +8.0111 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.836 | −19.4% | −1.9792 to −0.3492 | yes: GAIN |
| node-hours | 2.514 | 2.026 | −19.4% | −0.8286 to −0.1461 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271 | +0.1% | −0.6332 to +1.3307 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 234.4 | −13.4% | −61.5633 to −10.9476 | yes: GAIN |
| response time (ms), mean | 281.7 | 241 | −14.4% | −56.8069 to −24.4570 | yes: GAIN |
| response time (ms), 95th percentile | 920.3 | 894.3 | −2.8% | −79.5040 to +27.5190 | no |
| response time (ms), 99th percentile | 1347 | 1299 | −3.6% | −134.8705 to +38.8347 | no |
| time over the response line (% of samples) | 14.37 | 13.97 | −2.7% | −0.9423 to +0.1536 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7 | −2.8% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 | +38.200 (native is 0) | +26.2744 to +50.1256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.782 | 10.48 | +19.3% | +0.2464 to +3.1503 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05579 | 0.07081 | +26.9% | +0.0039 to +0.0262 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.339 | 1.346 | +0.5% | −0.0175 to +0.0318 | no |
| Omni's own CPU (cores), mean | 0 | 0.01564 | +0.016 (native is 0) | +0.0135 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.362 | +1.7% | −0.0010 to +0.0466 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.1 | 416.6 | −16.2% | −143.3989 to −17.7490 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.199 | +10.7% | −0.0427 to +0.4688 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.31 | 39.46 | +0.4% | −0.2180 to +0.5163 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 760.8 | 756.5 | −0.6% | −8.7101 to +0.1101 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.021 | −33.0% | −3.2835 to −0.6749 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.04167 | −73.7% | −0.1759 to −0.0574 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.3 | −57.1% | −0.7694 to −0.0306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 67.13 | 62.67 | −6.6% | −9.0160 to +0.0993 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.972 | −17.1% | −1.8869 to −0.1685 | yes: GAIN |
| node-hours | 2.516 | 2.08 | −17.3% | −0.7982 to −0.0748 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.4 | −0.4% | −2.2112 to +0.2312 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 238.2 | −12.2% | −60.7084 to −5.7257 | yes: GAIN |
| response time (ms), mean | 262.8 | 257.1 | −2.2% | −23.6791 to +12.2531 | no |
| response time (ms), 95th percentile | 827.8 | 951.8 | +15.0% | +28.9317 to +219.0953 | yes: LOSS |
| response time (ms), 99th percentile | 1201 | 1438 | +19.7% | +54.2744 to +418.3988 | yes: LOSS |
| time over the response line (% of samples) | 13.65 | 14.74 | +8.0% | +0.2253 to +1.9500 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.9 | +12.9% | −0.1900 to +1.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.7 | +57.700 (native is 0) | +34.1780 to +81.2220 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 8.355 | −9.0% | −2.5728 to +0.9228 | no |
| utilisation (used / allocatable) | 0.05667 | 0.0679 | +19.8% | +0.0017 to +0.0208 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.36 | 1.327 | −2.4% | −0.0896 to +0.0237 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.0152 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.36 | 1.344 | −1.2% | −0.0734 to +0.0415 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 431.7 | −11.1% | −101.7160 to −5.7060 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 2.302 | +11.8% | −0.0148 to +0.4993 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 38.43 | 40.32 | +4.9% | +1.5597 to +2.2382 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.4 | 761.3 | +1.3% | +1.4670 to +18.3330 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.304 | −28.3% | −3.0507 to −0.3412 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.15 | +500.0% | +0.0671 to +0.1829 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.8 | +700.0% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.01 | 69.11 | +15.2% | +1.2163 to +16.9921 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*