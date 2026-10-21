# Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39173416105 | `8de24035ac07` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| B | 39177935888 | `0d11e5ab281c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| C | 39182898753 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.1% (-0.3 to +0.5) | +0.2% (+0.1 to +0.3) | +0.3% (-0.1 to +0.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.0% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | +0.1% (-0.2 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.0% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | +0.1% (-0.2 to +0.3) | EVEN, no difference beyond the noise (all three runs) |
| response time (ms), mean | -28.9% (-42.9 to -14.8) | -44.3% (-60.3 to -28.3) | -41.3% (-56.5 to -26.2) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -39.1% (-66.2 to -12.0) | -58.1% (-93.0 to -23.3) | -52.6% (-88.8 to -16.5) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +25.2% (+7.7 to +42.7) | -27.3% (-60.1 to +5.5) | -24.5% (-55.7 to +6.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| time over the response line (% of samples) | -30.1% (-39.0 to -21.2) | -30.8% (-38.8 to -22.9) | -31.4% (-43.5 to -19.4) | **GAIN in all three of our runs** |
| failed requests (%) | -11.6% (-16.3 to -6.8) | -7.3% (-12.7 to -1.9) | -7.2% (-14.2 to -0.2) | **GAIN in all three of our runs** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -15.9% (-21.3 to -10.5) | -19.7% (-25.2 to -14.2) | -22.6% (-31.0 to -14.2) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +44.8 (+39.36 to +50.24) | +44.9 (+38.04 to +51.76) | +49.1 (+40.73 to +57.47) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -100.0% (-326.2 to +126.2) | -20.5% (-102.0 to +61.1) | -25.4% (-126.4 to +75.6) | shown, not judged |
| utilisation (used / allocatable) | -1.1% (-2.2 to +0.1) | -1.4% (-1.7 to -1.0) | -1.7% (-2.7 to -0.8) | shown, not judged |
| CPU used (cores), mean | -1.1% (-2.2 to +0.1) | -1.4% (-1.7 to -1.0) | -1.7% (-2.7 to -0.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01329 (+0.01245 to +0.01413) | +0.01263 (+0.01152 to +0.01374) | +0.01317 (+0.01198 to +0.01436) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.6% (-1.8 to +0.5) | -0.9% (-1.2 to -0.6) | -1.2% (-2.1 to -0.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.3% (-1.8 to +2.4) | +1.6% (+0.1 to +3.1) | +1.8% (+0.1 to +3.6) | shown, not judged |
| HPA replicas, mean | +3.4% (+0.9 to +5.9) | +3.9% (+0.9 to +6.8) | +6.4% (+1.6 to +11.1) | **power given in all three of our runs** |
| pods started | -30.6% (-75.3 to +14.1) | -18.5% (-52.7 to +15.7) | +25.5% (-34.0 to +85.0) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -32.3% (-79.7 to +15.1) | -23.5% (-74.3 to +27.4) | +68.7% (-28.0 to +165.4) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -7.4% (-43.5 to +28.6) | -9.8% (-34.6 to +15.0) | +32.6% (+9.4 to +55.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy, the real machine under kind (%) | -0.2% (-1.2 to +0.7) | -0.6% (-0.9 to -0.3) | -0.7% (-1.4 to +0.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: failed requests in the 120 s after the kill (%) | -9.5% (-24.9 to +5.9) | -8.3% (-20.3 to +3.6) | +9.7% (-13.3 to +32.7) | EVEN, no difference beyond the noise (all three runs) |
| robust: time over the line in the 120 s after the kill (% of samples) | -0.1% (-0.2 to +0.1) | -3.4% (-8.7 to +2.0) | +2.8% (-2.6 to +8.3) | EVEN, no difference beyond the noise (all three runs) |
| robust: every setting back at the operator's within 60 s of the kill, every repetition (the governor killed outright; the watchdog's hand-back) | yes (10 reps; mean 10 s, max 11 s) | yes (10 reps; mean 9 s, max 10 s) | yes (10 reps; mean 8 s, max 10 s) | **handed back within the allowance in every repetition, in all three of our runs** |
| robust: a second governor started after the hand-back and governed to the end, every repetition | yes | yes | yes | **the same in all three of our runs** |

Readings: 5 GAIN in all three of our runs, 1 handed back within the allowance in every repetition, in all three of our runs, 1 power given in all three of our runs, 1 the same in all three of our runs, 3 EVEN, no difference beyond the noise (2 of 3 runs), 6 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
