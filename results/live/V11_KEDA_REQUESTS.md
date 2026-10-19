# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39173411511 | `8de24035ac07` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| B | 39176842679 | `2a2cfc67147e` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |
| C | 39180252225 | `7b7dd69870e7` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | -0.2% (-0.7 to +0.3) | -0.5% (-1.0 to -0.0) | -0.3% (-0.8 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.2% (+1.5 to +2.9) | +1.6% (+0.8 to +2.4) | +2.2% (+1.4 to +2.9) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.2% (+1.5 to +2.9) | +1.6% (+0.8 to +2.4) | +2.2% (+1.4 to +2.9) | **power given in all three of our runs** |
| response time (ms), mean | -56.7% (-70.0 to -43.3) | -56.7% (-71.8 to -41.5) | -57.3% (-68.2 to -46.3) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -72.1% (-85.7 to -58.5) | -73.5% (-91.1 to -56.0) | -71.8% (-81.7 to -62.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -58.6% (-69.8 to -47.3) | -57.5% (-70.8 to -44.2) | -62.0% (-75.0 to -48.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -98.4% (-151.1 to -45.8) | -98.2% (-169.3 to -27.1) | -99.2% (-139.2 to -59.1) | **GAIN in all three of our runs** |
| failed requests (%) | +0.01198 (-0.01511 to +0.03907) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-150.2 to -49.8) | -100.0% (-172.9 to -27.1) | -100.0% (-143.7 to -56.3) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.7 (+4.354 to +5.046) | +4.1 (+3.694 to +4.506) | +4.1 (+3.694 to +4.506) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +50.0% (-153.3 to +253.3) | +113.3% (-309.7 to +536.3) | +0.0% (-168.6 to +168.6) | shown, not judged |
| utilisation (used / allocatable) | +53.9% (+46.0 to +61.7) | +47.4% (+37.2 to +57.6) | +55.7% (+46.9 to +64.4) | shown, not judged |
| CPU used (cores), mean | +53.9% (+46.0 to +61.7) | +47.4% (+37.2 to +57.6) | +55.7% (+46.9 to +64.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00975 (+0.008496 to +0.011) | +0.00873 (+0.007301 to +0.01016) | +0.00939 (+0.008148 to +0.01063) | shown, not judged |
| CPU used with Omni's own (cores), mean | +55.2% (+47.2 to +63.2) | +48.7% (+38.3 to +59.0) | +57.0% (+48.1 to +65.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -33.0% (-34.9 to -31.0) | -29.9% (-33.1 to -26.7) | -33.6% (-35.3 to -31.8) | shown, not judged |
| HPA replicas, mean | -10.6% (-17.7 to -3.4) | -19.8% (-28.5 to -11.0) | -18.6% (-25.9 to -11.4) | **GAIN in all three of our runs** |
| pods started | -3.6% (-22.4 to +15.3) | -25.0% (-46.0 to -4.0) | -27.6% (-43.2 to -12.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, total (s) | -6.5% (-33.0 to +20.0) | -15.2% (-60.0 to +29.7) | -19.0% (-46.6 to +8.5) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -2.0% (-25.6 to +21.5) | +10.0% (-26.4 to +46.4) | +9.3% (-21.5 to +40.1) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +44.0% (+37.3 to +50.7) | +42.8% (+32.6 to +53.0) | +50.3% (+42.4 to +58.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 6 GAIN in all three of our runs, 2 power given in all three of our runs, 1 EVEN, no difference beyond the noise (1 of 3 runs), 1 EVEN, no difference beyond the noise (2 of 3 runs), 3 EVEN, no difference beyond the noise (all three runs), 3 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
