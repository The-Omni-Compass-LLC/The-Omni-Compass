# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39171064099 | `f445e205073f` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| B | 39175675418 | `df871e4396dc` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| C | 39177950720 | `0d11e5ab281c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.1% (-0.7 to +0.4) | -0.3% (-0.9 to +0.4) | +0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.3% (+1.7 to +2.9) | +1.7% (+1.0 to +2.5) | +2.0% (+1.5 to +2.5) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.3% (+1.7 to +2.9) | +1.7% (+1.0 to +2.5) | +2.0% (+1.5 to +2.5) | **power given in all three of our runs** |
| response time (ms), mean | -47.9% (-57.6 to -38.2) | -47.4% (-61.5 to -33.4) | -48.4% (-59.6 to -37.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -61.4% (-71.9 to -51.0) | -62.2% (-75.2 to -49.2) | -64.3% (-75.0 to -53.5) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -68.3% (-79.6 to -57.0) | -69.3% (-85.7 to -52.9) | -70.0% (-80.0 to -59.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -99.2% (-150.7 to -47.7) | -97.7% (-169.4 to -26.0) | -100.0% (-168.2 to -31.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-172.0 to -28.0) | -100.0% (-188.0 to -12.0) | -100.0% (-192.3 to -7.7) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +15.9 (+12.99 to +18.81) | +17 (+14.39 to +19.61) | +17.5 (+15.11 to +19.89) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -42.3% (-195.1 to +110.5) | -50.6% (-181.9 to +80.7) | -70.6% (-217.4 to +76.2) | shown, not judged |
| utilisation (used / allocatable) | +50.5% (+41.6 to +59.4) | +43.3% (+32.2 to +54.4) | +42.7% (+33.6 to +51.9) | shown, not judged |
| CPU used (cores), mean | +50.5% (+41.6 to +59.4) | +43.3% (+32.2 to +54.4) | +42.7% (+33.6 to +51.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00824 (+0.007439 to +0.009041) | +0.00789 (+0.006932 to +0.008848) | +0.00736 (+0.00656 to +0.00816) | shown, not judged |
| CPU used with Omni's own (cores), mean | +51.5% (+42.6 to +60.5) | +44.3% (+33.1 to +55.5) | +43.7% (+34.5 to +52.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -31.4% (-36.0 to -26.8) | -27.9% (-32.6 to -23.2) | -27.9% (-32.4 to -23.3) | shown, not judged |
| HPA replicas, mean | +1.5% (+0.2 to +2.9) | +1.3% (+0.3 to +2.2) | +1.4% (-0.3 to +3.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pods started | -60.7% (-118.5 to -2.9) | -53.3% (-83.5 to -23.2) | -55.3% (-77.8 to -32.7) | **GAIN in all three of our runs** |
| pod start wait, total (s) | -63.4% (-126.2 to -0.7) | -48.0% (-93.3 to -2.7) | -58.6% (-84.1 to -33.1) | **GAIN in all three of our runs** |
| pod start wait, mean (s) | -43.0% (-108.7 to +22.7) | -24.2% (-68.9 to +20.5) | -20.1% (-52.0 to +11.8) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +45.2% (+37.8 to +52.6) | +40.2% (+29.6 to +50.8) | +38.8% (+30.9 to +46.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 GAIN in all three of our runs, 2 power given in all three of our runs, 1 EVEN, no difference beyond the noise (1 of 3 runs), 2 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
