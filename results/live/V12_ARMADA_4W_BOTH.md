# Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Armada against the organism alone (register row 94): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39482335827 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 9 |
| B | 39482351075 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39482365814 | `adfabdc8355f` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -39.9% (-44.8 to -35.0) | -40.3% (-43.2 to -37.5) | -42.5% (-44.8 to -40.2) | **GAIN in all three of our runs** |
| node-hours | -39.9% (-44.7 to -35.1) | -40.5% (-43.3 to -37.6) | -42.4% (-44.6 to -40.2) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -4.0% (-5.0 to -3.0) | -4.3% (-4.8 to -3.8) | -3.5% (-4.2 to -2.9) | **GAIN in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -32.6% (-35.7 to -29.4) | -33.1% (-35.0 to -31.2) | -34.2% (-35.5 to -32.8) | **GAIN in all three of our runs** |
| response time (ms), mean | -88.2% (-132.9 to -43.4) | -88.3% (-125.9 to -50.7) | -84.4% (-156.7 to -12.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -96.2% (-147.6 to -44.8) | -96.1% (-138.4 to -53.9) | -94.6% (-182.9 to -6.3) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -96.3% (-147.3 to -45.3) | -96.0% (-136.7 to -55.3) | -94.6% (-179.6 to -9.6) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-146.1 to -53.9) | -100.0% (-137.4 to -62.5) | -100.0% (-192.2 to -7.8) | **GAIN in all three of our runs** |
| failed requests (%) | -100.0% (-330.6 to +130.6) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, no difference beyond the noise (all three runs) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-144.3 to -55.7) | -100.0% (-133.6 to -66.4) | -100.0% (-181.0 to -19.0) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +25.56 (+24.06 to +27.05) | +25.5 (+23.98 to +27.02) | +24.2 (+23.14 to +25.26) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -99.8% (-132.1 to -67.6) | -99.6% (-133.0 to -66.3) | -100.0% (-178.2 to -21.8) | shown, not judged |
| utilisation (used / allocatable) | -74.6% (-88.3 to -60.8) | -73.8% (-83.0 to -64.5) | -74.8% (-85.3 to -64.2) | shown, not judged |
| CPU used (cores), mean | -84.7% (-98.6 to -70.7) | -84.3% (-93.7 to -74.9) | -85.4% (-96.8 to -74.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.008889 (+0.007841 to +0.009937) | +0.00954 (+0.008604 to +0.01048) | +0.0082 (+0.006926 to +0.009474) | shown, not judged |
| CPU used with Omni's own (cores), mean | -84.1% (-98.0 to -70.2) | -83.8% (-93.1 to -74.4) | -84.9% (-96.2 to -73.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +328.6% (+292.7 to +364.5) | +323.2% (+302.1 to +344.3) | +354.0% (+305.0 to +403.0) | shown, not judged |
| HPA replicas, mean | +8.6% (+2.4 to +14.7) | +6.7% (+2.6 to +10.8) | +1.6% (-3.3 to +6.5) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pods started | +650.0% (+128.0 to +1172.0) | +1300.0% (+621.4 to +1978.6) | +450.0% (-144.9 to +1044.9) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, total (s) | +400.0% (+25.3 to +774.7) | +666.7% (+176.7 to +1156.6) | +433.3% (-140.3 to +1007.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pod start wait, mean (s) | +425.0% (+53.6 to +796.4) | +366.7% (+136.3 to +597.0) | +494.4% (-34.9 to +1023.8) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU busy, the real machine under kind (%) | -70.1% (-81.3 to -58.8) | -68.9% (-76.9 to -60.9) | -69.1% (-80.1 to -58.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +72.4% (+61.8 to +82.9) | +68.6% (+58.6 to +78.6) | +86.7% (+75.6 to +97.9) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, mean (s) | +1190995.2% (+1185985.7 to +1196004.8) | +1634917.6% (+1630334.8 to +1639500.5) | +1324419.0% (+1319896.0 to +1328942.1) | **LOSS in all three of our runs** |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | +221050.0% (+220287.4 to +221812.6) | +245633.3% (+245069.1 to +246197.6) | +245750.0% (+245056.6 to +246443.4) | **LOSS in all three of our runs** |
| queue: job turnaround, submitted to done, mean (s) | +528.0% (+478.0 to +578.0) | +469.9% (+426.8 to +513.0) | +904.9% (+825.1 to +984.6) | **LOSS in all three of our runs** |
| queue: jobs unfinished at the window's end | +24 (+24 to +24) | +24 (+24 to +24) | +24 (+24 to +24) | **LOSS in all three of our runs** |

Readings: 9 GAIN in all three of our runs, 5 LOSS in all three of our runs, 4 EVEN, no difference beyond the noise (1 of 3 runs), 1 EVEN, no difference beyond the noise (all three runs), 2 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
