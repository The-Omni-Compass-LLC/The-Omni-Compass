# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107187219 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39114214725 | `3b9fc76017ad` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122525181 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge) | +47.4% (+32.5 to +62.2) | +53.3% (+41.0 to +65.6) | +78.9% (+52.3 to +105.6) | **GAIN in all three of our runs** |
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.0% (-0.1 to +0.2) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.4 to -0.2) | -0.1% (-0.4 to +0.2) | -0.2% (-0.4 to -0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.3% (-0.4 to -0.2) | -0.1% (-0.4 to +0.2) | -0.2% (-0.4 to -0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| response time (ms), mean | -45.5% (-56.8 to -34.2) | -42.5% (-54.0 to -31.0) | -37.7% (-44.4 to -31.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -61.1% (-76.6 to -45.6) | -55.7% (-70.4 to -41.1) | -57.7% (-73.0 to -42.4) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -28.0% (-57.4 to +1.4) | -37.7% (-73.7 to -1.7) | -5.7% (-28.2 to +16.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| time over the response line (% of samples) | -45.8% (-64.1 to -27.5) | -34.9% (-47.9 to -21.9) | -36.5% (-39.1 to -33.8) | **GAIN in all three of our runs** |
| failed requests (%) | -14.1% (-28.2 to -0.1) | -9.3% (-16.3 to -2.3) | -13.9% (-15.9 to -12.0) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -34.3% (-41.4 to -27.2) | -18.4% (-22.5 to -14.3) | -15.7% (-19.0 to -12.4) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +39.2 (+30.46 to +47.94) | +34.5 (+25.84 to +43.16) | +37.9 (+30.43 to +45.37) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -18.8% (-67.5 to +29.8) | -9.2% (-66.0 to +47.6) | -37.4% (-85.6 to +10.7) | shown, not judged |
| utilisation (used / allocatable) | -2.9% (-3.8 to -2.0) | -0.9% (-2.1 to +0.3) | -1.5% (-2.1 to -1.0) | shown, not judged |
| CPU used (cores), mean | -2.9% (-3.8 to -2.0) | -0.9% (-2.1 to +0.3) | -1.5% (-2.1 to -1.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00808 (+0.00675 to +0.00941) | +0.00895 (+0.00767 to +0.01023) | +0.00998 (+0.009706 to +0.01025) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.6% (-3.5 to -1.7) | -0.5% (-1.7 to +0.7) | -1.2% (-1.7 to -0.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +3.6% (+1.2 to +6.1) | +0.5% (-0.8 to +1.7) | +1.4% (+0.9 to +1.8) | shown, not judged |
| HPA replicas, mean | +0.5% (-4.9 to +5.8) | +1.3% (-4.4 to +6.9) | +1.9% (+0.9 to +3.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pods started | +36.5% (-18.3 to +91.4) | +42.5% (-14.1 to +99.1) | +5.6% (-51.3 to +62.4) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +9.2% (-39.6 to +57.9) | +7.8% (-50.1 to +65.8) | -14.9% (-66.2 to +36.3) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -13.4% (-39.6 to +12.8) | -23.3% (-47.1 to +0.4) | -18.3% (-48.4 to +11.8) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -2.3% (-3.4 to -1.2) | -0.4% (-1.5 to +0.6) | -1.1% (-1.5 to -0.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 6 GAIN in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 2 EVEN, no difference beyond the noise (2 of 3 runs), 4 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
