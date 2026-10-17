# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38843268161 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| B | 38843270386 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |
| C | 38843272786 | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| node-hours | -0.1% (-0.7 to +0.5) | -0.3% (-0.8 to +0.3) | -0.1% (-0.6 to +0.5) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +1.7% (+0.9 to +2.5) | +1.1% (+0.3 to +1.9) | +1.6% (+0.7 to +2.5) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.7% (+0.9 to +2.5) | +1.1% (+0.3 to +1.9) | +1.6% (+0.7 to +2.5) | **power given in all three of our runs** |
| response time (ms), mean | -38.2% (-45.7 to -30.8) | -36.0% (-46.6 to -25.3) | -37.7% (-48.4 to -27.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -52.3% (-60.0 to -44.5) | -53.2% (-65.5 to -40.9) | -53.5% (-64.8 to -42.2) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -58.5% (-69.1 to -47.8) | -57.4% (-69.6 to -45.2) | -57.7% (-69.9 to -45.5) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-157.2 to -42.8) | -100.0% (-173.3 to -26.7) | -97.9% (-151.0 to -44.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | -3.7% (-334.7 to +327.3) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-225.0 to +25.0) | -100.0% (-192.3 to -7.7) | -100.0% (-215.2 to +15.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +16.7 (+15.69 to +17.71) | +17.4 (+16.38 to +18.42) | +19.7 (+14.03 to +25.37) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -29.3% (-99.3 to +40.7) | -15.5% (-61.6 to +30.5) | +70.5% (-143.9 to +285.0) | shown, not judged |
| utilisation (used / allocatable) | +33.0% (+27.7 to +38.3) | +27.3% (+18.2 to +36.3) | +31.9% (+23.9 to +39.9) | shown, not judged |
| CPU used (cores), mean | +33.0% (+27.7 to +38.3) | +27.3% (+18.2 to +36.3) | +31.9% (+23.9 to +39.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01253 (+0.01131 to +0.01375) | +0.01192 (+0.01044 to +0.0134) | +0.01287 (+0.01058 to +0.01516) | shown, not judged |
| CPU used with Omni's own (cores), mean | +34.4% (+28.9 to +39.8) | +28.6% (+19.4 to +37.8) | +33.4% (+25.1 to +41.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -23.1% (-25.7 to -20.5) | -19.1% (-23.9 to -14.4) | -22.0% (-26.1 to -17.9) | shown, not judged |
| HPA replicas, mean | +2.6% (-0.2 to +5.5) | +2.6% (+0.1 to +5.1) | +5.6% (-3.6 to +14.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pods started | +0.0% (-23.3 to +23.3) | -3.8% (-16.5 to +8.8) | +17.0% (-13.2 to +47.3) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +21.4% (-52.8 to +95.5) | -6.4% (-49.6 to +36.9) | +35.2% (-15.6 to +86.0) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +22.2% (-30.6 to +75.1) | -4.0% (-38.8 to +30.7) | +17.3% (-21.1 to +55.7) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +32.6% (+27.9 to +37.3) | +26.9% (+18.6 to +35.3) | +30.7% (+23.3 to +38.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 2 power given in all three of our runs, 2 EVEN, no difference beyond the noise (2 of 3 runs), 5 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
