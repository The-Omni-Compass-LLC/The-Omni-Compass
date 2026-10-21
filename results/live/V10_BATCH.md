# Batch queue: 240 CPU jobs and cruise: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39107196814 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115235566 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39122536157 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -9.4% (-17.0 to -1.7) | -6.2% (-11.4 to -1.0) | -13.8% (-21.1 to -6.4) | **GAIN in all three of our runs** |
| node-hours | -9.3% (-17.0 to -1.6) | -6.2% (-11.4 to -1.1) | -13.8% (-21.0 to -6.5) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.3 to +0.6) | +0.0% (-0.2 to +0.3) | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -6.3% (-11.6 to -1.0) | -4.3% (-7.8 to -0.7) | -9.5% (-14.5 to -4.5) | **GAIN in all three of our runs** |
| response time (ms), mean | -9.8% (-12.5 to -7.2) | -12.3% (-14.8 to -9.7) | -11.6% (-15.4 to -7.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -1.7% (-6.4 to +3.1) | -3.5% (-7.9 to +1.0) | -3.8% (-8.5 to +1.0) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +1.2% (-5.2 to +7.6) | -0.8% (-5.5 to +3.9) | -2.7% (-7.2 to +1.9) | EVEN, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -3.7% (-6.7 to -0.7) | -3.2% (-6.5 to +0.2) | -3.2% (-6.0 to -0.5) | EVEN, no difference beyond the noise (1 of 3 runs) |
| failed requests (%) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +0.0% (+0.0 to +0.0) | +0.9% (-1.2 to +3.1) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (all three runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +11.8 (+11.06 to +12.54) | +11.4 (+10.9 to +11.9) | +11.8 (+10.92 to +12.68) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.0% (-1.7 to +3.7) | +1.8% (+0.5 to +3.0) | -0.3% (-2.6 to +2.0) | shown, not judged |
| utilisation (used / allocatable) | +10.3% (+0.7 to +19.9) | +6.4% (+0.3 to +12.5) | +14.1% (+5.9 to +22.4) | shown, not judged |
| CPU used (cores), mean | -0.3% (-3.1 to +2.6) | -0.5% (-2.8 to +1.8) | -1.7% (-4.4 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.02042 (+0.01631 to +0.02453) | +0.02104 (+0.01742 to +0.02466) | +0.02398 (+0.01961 to +0.02835) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.1% (-1.7 to +3.9) | +0.8% (-1.5 to +3.1) | -0.1% (-2.8 to +2.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -6.5% (-13.8 to +0.7) | -3.9% (-8.3 to +0.5) | -8.7% (-14.9 to -2.5) | shown, not judged |
| HPA replicas, mean | +10.0% (-6.2 to +26.2) | +18.7% (+5.2 to +32.2) | +3.5% (-12.8 to +19.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pods started | +500.0% (-107.9 to +1107.9) | +0.9 (+0.3722 to +1.428) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, total (s) | +142.4% (-446.7 to +731.5) | +18 (+1.984 to +34.02) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pod start wait, mean (s) | +27.3% (-336.1 to +390.6) | +13.1 (+1.394 to +24.81) | +0.0% (-337.2 to +337.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy, the real machine under kind (%) | +1.5% (+0.9 to +2.2) | +2.0% (+1.0 to +3.0) | +2.0% (+1.3 to +2.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.5% (-0.1 to +1.2) | +0.9% (+0.2 to +1.6) | +0.8% (+0.2 to +1.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | -14.6% (-25.7 to -3.5) | -10.4% (-18.8 to -2.1) | -22.2% (-33.3 to -11.1) | **GAIN in all three of our runs** |

Readings: 5 GAIN in all three of our runs, 2 EVEN, no difference beyond the noise (1 of 3 runs), 4 EVEN, no difference beyond the noise (2 of 3 runs), 5 EVEN, no difference beyond the noise (all three runs), 2 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
