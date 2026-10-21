# The Kubernetes scheduler with the operator's bin-packing profile under the batch stream: Omni-Compass on top (register row 88): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39356578556 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39356594135 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39356608147 | `1ca982cf97db` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -24.2% (-36.5 to -12.0) | -27.5% (-37.6 to -17.3) | -24.9% (-35.2 to -14.7) | **GAIN in all three of our runs** |
| node-hours | -24.3% (-36.6 to -12.1) | -27.5% (-37.7 to -17.3) | -24.9% (-35.3 to -14.5) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.2) | +0.1% (-0.1 to +0.4) | -0.1% (-0.4 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -17.0% (-25.7 to -8.4) | -19.0% (-26.0 to -11.9) | -17.4% (-24.7 to -10.1) | **GAIN in all three of our runs** |
| response time (ms), mean | -24.6% (-31.9 to -17.2) | -28.6% (-33.2 to -24.1) | -27.3% (-34.5 to -20.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -0.7% (-9.0 to +7.5) | -1.8% (-12.3 to +8.6) | -2.8% (-11.1 to +5.4) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +2.9% (-1.2 to +7.0) | +2.4% (-3.4 to +8.3) | +2.7% (-0.4 to +5.7) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | +40.0% (-9.4 to +89.3) | +27.7% (-62.9 to +118.3) | +14.8% (-23.2 to +52.8) | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +75.0% (-11.4 to +161.4) | +44.4% (-123.9 to +212.8) | +0.0% (-44.4 to +44.4) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +40.5 (+26.94 to +54.06) | +39.7 (+30.4 to +49) | +38.7 (+30.61 to +46.79) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -13.1% (-49.3 to +23.0) | -9.3% (-45.8 to +27.1) | -2.7% (-34.5 to +29.0) | shown, not judged |
| utilisation (used / allocatable) | +29.2% (+13.6 to +44.8) | +40.9% (+24.2 to +57.6) | +32.5% (+17.1 to +48.0) | shown, not judged |
| CPU used (cores), mean | -2.8% (-6.6 to +1.0) | +0.9% (-1.3 to +3.1) | -1.9% (-6.1 to +2.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01894 (+0.01587 to +0.02201) | +0.0183 (+0.01685 to +0.01975) | +0.01909 (+0.01766 to +0.02052) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.5% (-5.3 to +2.4) | +2.2% (+0.1 to +4.4) | -0.5% (-4.7 to +3.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -15.8% (-25.1 to -6.6) | -20.8% (-29.6 to -12.0) | -16.7% (-25.2 to -8.2) | shown, not judged |
| HPA replicas, mean | +1.1% (-8.8 to +10.9) | +3.6% (-6.3 to +13.5) | -2.4% (-10.4 to +5.6) | EVEN, no difference beyond the noise (all three runs) |
| pods started | +300.0% (-288.9 to +888.9) | +100.0% (-126.2 to +326.2) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +500.0% (-272.6 to +1272.6) | +400.0% (-179.2 to +979.2) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +400.0% (-291.1 to +1091.1) | +275.0% (-158.6 to +708.5) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +2.7% (+2.2 to +3.3) | +2.1% (+1.8 to +2.4) | +2.6% (+2.0 to +3.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.1% (+0.0 to +0.1) | +0.0% (-0.0 to +0.1) | -0.1% (-0.2 to +0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | -41.5% (-61.7 to -21.4) | -48.1% (-64.2 to -32.0) | -44.4% (-61.5 to -27.3) | **GAIN in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | -28.6% (-134.1 to +77.0) | +14.3% (-61.1 to +89.7) | +20.0% (-122.3 to +162.3) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +0.0% (-337.2 to +337.2) | +0.0% (+0.0 to +0.0) | +0.1 (-0.1262 to +0.3262) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | +1.4% (+0.8 to +1.9) | +1.0% (+0.4 to +1.7) | +1.2% (+0.7 to +1.6) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |

Readings: 5 GAIN in all three of our runs, 1 LOSS in all three of our runs, 1 EVEN, no difference beyond the noise (2 of 3 runs), 11 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
