# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.682 | 5.959 |
| node-hours | 2.519 | 2.517 | 1.961 | 2.495 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 271.2 | 269.3 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 271.2 | 227.9 | 269.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 215.2 | 119.5 | 185.7 | 89.86 |
| response time (ms), 95th percentile | 639.9 | 199.6 | 674 | 191.6 |
| response time (ms), 99th percentile | 928.8 | 290.2 | 978.4 | 294.2 |
| time over the response line (% of samples) | 9.772 | 0.1856 | 9.459 | 0.1115 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | 5.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 42.3 | 16 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.972 | 842.2 | 7.682 | 899.2 |
| utilisation (used / allocatable) | 0.0527 | 0.05723 | 0.06709 | 0.05825 |
| CPU used (cores), mean | 1.265 | 1.373 | 1.235 | 1.389 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01429 | 0.01153 |
| CPU used with Omni's own (cores), mean | 1.265 | 1.373 | 1.25 | 1.401 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 519.2 | 472.4 | 441.8 | 465.3 |
| HPA replicas, mean | 1.918 | 2.017 | 2.275 | 1.982 |
| pods started | 0 | 0.1 | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.2 | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 35.96 | 41.53 | 36.59 | 43.01 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 735.8 | 1335 | 736.5 | 1362 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.851 | 5.684 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 125.6 | 0.02917 | 110.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 657 | 0.1 | 563.4 |
| queue: job turnaround, submitted to done, mean (s) | 43.32 | 649.6 | 43.43 | 701 |
| queue: jobs unfinished at the window's end | 0 | 5.9 | 0 | 6.5 |

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
| worker nodes in service, mean | 6 | 5.959 | −0.7% | −0.0935 to +0.0118 | no |
| node-hours | 2.517 | 2.495 | −0.9% | −0.0475 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271 | −0.1% | −1.1392 to +0.8125 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 269.8 | −0.5% | −3.7689 to +0.8839 | no |
| response time (ms), mean | 119.5 | 89.86 | −24.8% | −39.8323 to −19.4986 | yes: GAIN |
| response time (ms), 95th percentile | 199.6 | 191.6 | −4.0% | −22.0267 to +6.0277 | no |
| response time (ms), 99th percentile | 290.2 | 294.2 | +1.4% | −28.6826 to +36.6600 | no |
| time over the response line (% of samples) | 0.1856 | 0.1115 | −39.9% | −0.2190 to +0.0708 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16.000 (native is 0) | +14.2479 to +17.7521 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 842.2 | 899.2 | +6.8% | −11.2047 to +125.2481 | no |
| utilisation (used / allocatable) | 0.05723 | 0.05825 | +1.8% | −0.0006 to +0.0026 | no |
| CPU used (cores), mean | 1.373 | 1.389 | +1.1% | −0.0259 to +0.0572 | no |
| Omni's own CPU (cores), mean | 0 | 0.01153 | +0.012 (native is 0) | +0.0105 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.373 | 1.401 | +2.0% | −0.0142 to +0.0685 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.4 | 465.3 | −1.5% | −19.5466 to +5.3535 | no |
| HPA replicas, mean | 2.017 | 1.982 | −1.7% | −0.1437 to +0.0733 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 41.53 | 43.01 | +3.6% | +0.3798 to +2.5741 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1335 | 1362 | +2.1% | −31.4330 to +86.4330 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.684 | −5.3% | −0.6936 to +0.0620 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 125.6 | 110.4 | −12.1% | −60.0100 to +29.5933 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 657 | 563.4 | −14.2% | −331.7108 to +144.5108 | no |
| queue: job turnaround, submitted to done, mean (s) | 649.6 | 701 | +7.9% | −5.9790 to +108.8540 | no |
| queue: jobs unfinished at the window's end | 5.9 | 6.5 | +10.2% | −1.1586 to +2.3586 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.517 | −0.1% | −0.0099 to +0.0063 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 271.2 | +0.4% | −0.4241 to +2.3844 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 271.2 | +0.4% | −0.4241 to +2.3844 | no |
| response time (ms), mean | 215.2 | 119.5 | −44.5% | −156.2632 to −35.1231 | yes: GAIN |
| response time (ms), 95th percentile | 639.9 | 199.6 | −68.8% | −708.5291 to −172.0349 | yes: GAIN |
| response time (ms), 99th percentile | 928.8 | 290.2 | −68.8% | −995.5230 to −281.6222 | yes: GAIN |
| time over the response line (% of samples) | 9.772 | 0.1856 | −98.1% | −17.7622 to −1.4104 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | −100.0% | −10.4607 to −1.5393 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.972 | 842.2 | +10464.3% | +526.2566 to +1142.1067 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0527 | 0.05723 | +8.6% | +0.0007 to +0.0084 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.265 | 1.373 | +8.6% | +0.0160 to +0.2015 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.265 | 1.373 | +8.6% | +0.0160 to +0.2015 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 519.2 | 472.4 | −9.0% | −83.1760 to −10.5108 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.918 | 2.017 | +5.2% | +0.0127 to +0.1850 | yes: power given |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 35.96 | 41.53 | +15.5% | +3.9190 to +7.2316 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 735.8 | 1335 | +81.4% | +470.9988 to +727.2012 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 125.6 | +301380.0% | +69.8834 to +181.2666 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 657 | +218900.0% | +371.0721 to +942.3279 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 43.32 | 649.6 | +1399.6% | +410.7688 to +801.7395 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 5.9 | +5.900 (native is 0) | +0.2833 to +11.5167 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.682 | −22.0% | −2.1828 to −0.4533 | yes: GAIN |
| node-hours | 2.519 | 1.961 | −22.1% | −0.9212 to −0.1936 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 269.3 | −0.3% | −1.9074 to +0.0923 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 227.9 | −15.6% | −69.9802 to −14.5641 | yes: GAIN |
| response time (ms), mean | 215.2 | 185.7 | −13.7% | −42.8041 to −16.1932 | yes: GAIN |
| response time (ms), 95th percentile | 639.9 | 674 | +5.3% | −25.8013 to +94.0523 | no |
| response time (ms), 99th percentile | 928.8 | 978.4 | +5.3% | −71.2006 to +170.4366 | no |
| time over the response line (% of samples) | 9.772 | 9.459 | −3.2% | −1.0536 to +0.4268 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 5.9 | −1.7% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 | +42.300 (native is 0) | +26.1318 to +58.4682 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.972 | 7.682 | −3.6% | −1.9864 to +1.4064 | no |
| utilisation (used / allocatable) | 0.0527 | 0.06709 | +27.3% | +0.0052 to +0.0236 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.265 | 1.235 | −2.3% | −0.0656 to +0.0067 | no |
| Omni's own CPU (cores), mean | 0 | 0.01429 | +0.014 (native is 0) | +0.0124 to +0.0162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.265 | 1.25 | −1.2% | −0.0530 to +0.0227 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 519.2 | 441.8 | −14.9% | −126.2517 to −28.5056 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.918 | 2.275 | +18.6% | +0.0808 to +0.6338 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 35.96 | 36.59 | +1.8% | +0.3502 to +0.9202 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 735.8 | 736.5 | +0.1% | −1.2385 to +2.6385 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.851 | −35.8% | −3.4969 to −0.8005 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.02917 | −30.0% | −0.0370 to +0.0120 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.1 | −66.7% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 43.32 | 43.43 | +0.3% | −1.8398 to +2.0648 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.682 | −22.0% | −2.1828 to −0.4533 | yes: GAIN |
| node-hours | 2.517 | 1.961 | −22.1% | −0.9204 to −0.1906 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 269.3 | −0.7% | −3.8210 to +0.0455 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 227.9 | −15.9% | −71.9518 to −14.5529 | yes: GAIN |
| response time (ms), mean | 119.5 | 185.7 | +55.4% | +11.7043 to +120.6848 | yes: LOSS |
| response time (ms), 95th percentile | 199.6 | 674 | +237.7% | +193.9070 to +754.9080 | yes: LOSS |
| response time (ms), 99th percentile | 290.2 | 978.4 | +237.1% | +281.5811 to +1094.8001 | yes: LOSS |
| time over the response line (% of samples) | 0.1856 | 9.459 | +4996.2% | +1.5243 to +17.0215 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 5.9 | +5.900 (native is 0) | +1.3955 to +10.4045 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 | +42.300 (native is 0) | +26.1318 to +58.4682 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 842.2 | 7.682 | −99.1% | −1143.4790 to −525.4644 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05723 | 0.06709 | +17.2% | +0.0035 to +0.0162 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.373 | 1.235 | −10.1% | −0.2579 to −0.0183 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01429 | +0.014 (native is 0) | +0.0124 to +0.0162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.373 | 1.25 | −9.0% | −0.2455 to −0.0021 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.4 | 441.8 | −6.5% | −51.7681 to −9.3023 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.017 | 2.275 | +12.8% | +0.0354 to +0.4815 | yes: power given |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 41.53 | 36.59 | −11.9% | −6.6127 to −3.2675 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1335 | 736.5 | −44.8% | −726.7839 to −470.0161 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.497 | −58.4% | −4.4912 to −2.5156 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 125.6 | 0.02917 | −100.0% | −181.2856 to −69.8894 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 657 | 0.1 | −100.0% | −942.6784 to −371.1216 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 649.6 | 43.43 | −93.3% | −801.4931 to −410.7902 | yes: GAIN |
| queue: jobs unfinished at the window's end | 5.9 | 0 | −100.0% | −11.5167 to −0.2833 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.959 | −0.7% | −0.0935 to +0.0118 | no |
| node-hours | 2.519 | 2.495 | −0.9% | −0.0519 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 271 | +0.3% | −0.7643 to +2.3979 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 269.8 | −0.2% | −2.8924 to +1.9677 | no |
| response time (ms), mean | 215.2 | 89.86 | −58.2% | −194.8222 to −55.8949 | yes: GAIN |
| response time (ms), 95th percentile | 639.9 | 191.6 | −70.1% | −727.2934 to −169.2696 | yes: GAIN |
| response time (ms), 99th percentile | 928.8 | 294.2 | −68.3% | −1017.9946 to −251.1732 | yes: GAIN |
| time over the response line (% of samples) | 9.772 | 0.1115 | −98.9% | −17.9169 to −1.4040 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | −100.0% | −10.4607 to −1.5393 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16.000 (native is 0) | +14.2479 to +17.7521 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.972 | 899.2 | +11179.6% | +617.3041 to +1165.1026 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0527 | 0.05825 | +10.5% | +0.0011 to +0.0100 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.265 | 1.389 | +9.8% | +0.0207 to +0.2280 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01153 | +0.012 (native is 0) | +0.0105 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.265 | 1.401 | +10.7% | +0.0332 to +0.2386 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 519.2 | 465.3 | −10.4% | −94.7527 to −13.1273 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.918 | 1.982 | +3.3% | −0.0082 to +0.1355 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 35.96 | 43.01 | +19.6% | +5.0635 to +9.0411 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 735.8 | 1362 | +85.2% | +526.8015 to +726.3985 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.684 | −5.3% | −0.6936 to +0.0620 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 110.4 | +264880.0% | +83.5281 to +137.2053 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 563.4 | +187700.0% | +387.3282 to +738.8718 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 43.32 | 701 | +1518.3% | +497.9797 to +817.4036 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 6.5 | +6.500 (native is 0) | +0.4187 to +12.5813 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*