# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39173420146 | `8de24035ac07` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| B | 39177939062 | `0d11e5ab281c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| C | 39182902844 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (+0.0 to +0.0) | EVEN, the same |
| node-hours | =0.1% (−0.1 to +0.2) | =0.0% (−0.1 to +0.1) | =0.0% (−0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.04%) |
| energy, parked workers still on at idle power (Wh, declared model) | =0.1% (−0.3 to +0.2) | =0.2% (−0.6 to +0.3) | =0.2% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.13%) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | =0.1% (−0.3 to +0.2) | =0.2% (−0.6 to +0.3) | =0.2% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.13%) |
| response time (ms), mean | +36.0% (+19.6 to +52.5) | +34.1% (+7.4 to +60.7) | +34.6% (+26.4 to +42.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +40.3% (+4.0 to +76.6) | +23.6% (+5.1 to +42.1) | +33.5% (−10.2 to +77.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| response time (ms), 99th percentile | +5.4% (−41.9 to +52.6) | +8.3% (−32.1 to +48.7) | +8.2% (−18.2 to +34.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| time over the response line (% of samples) | +34.7% (+11.8 to +57.6) | +32.1% (+8.5 to +55.7) | +31.7% (+25.4 to +37.9) | **GAIN in all three of our runs** |
| failed requests (%) | +13.1% (−12.0 to +38.2) | +11.7% (−13.8 to +37.3) | +14.3% (+4.2 to +24.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +18.9% (+12.5 to +25.2) | +18.0% (+5.8 to +30.3) | +13.6% (+13.6 to +13.6) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +155.3 (-95.69 to +406.4) | +170.7 (-75.32 to +416.7) | +107 (+86.66 to +127.3) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +16.4% (-44.9 to +77.7) | +74.2% (-177.5 to +325.8) | -23.8% (-76.9 to +29.2) | shown, not judged |
| utilisation (used / allocatable) | -1.1% (-3.1 to +0.9) | -0.8% (-3.6 to +2.0) | -1.3% (-2.2 to -0.4) | shown, not judged |
| CPU used (cores), mean | -1.1% (-3.1 to +0.9) | -0.8% (-3.6 to +2.0) | -1.3% (-2.2 to -0.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01043 (+0.00986 to +0.01101) | +0.0108 (+0.01014 to +0.01146) | +0.01073 (+0.01059 to +0.01088) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.7% (-2.7 to +1.3) | -0.4% (-3.3 to +2.4) | -1.0% (-1.9 to -0.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.9% (-0.5 to +2.3) | +0.6% (-1.3 to +2.6) | +1.1% (+0.4 to +1.9) | shown, not judged |
| HPA replicas, mean | +50.7% (+46.7 to +54.6) | +49.0% (+37.3 to +60.7) | +51.7% (+51.1 to +52.3) | **power given in all three of our runs** |
| pods started | +230.8% (−217.0 to +678.5) | +143.8% (−193.2 to +480.7) | +80.0% (+30.3 to +129.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | −268.2% (−723.1 to +186.8) | −135.7% (−466.4 to +195.0) | −138.1% (−64.2 to −212.0) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | −15.8% (−107.7 to +76.1) | +5.1% (−29.9 to +40.2) | −32.5% (−89.1 to +24.1) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | -0.1% (-1.6 to +1.3) | +0.3% (-2.0 to +2.5) | -0.3% (-1.5 to +0.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.023 | 1.015 | 1.023 | **no leak (every repetition under 1.25)** |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 97.5% | 97.5% | 97.5% | **valid (every repetition at 95% of the expected or more)** |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 0 | 0 | 0 | **none in any repetition** |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 1.12 | 1.13 | 0.94 | **no growth beyond the limit (every repetition under 1.5)** |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **every setting handed back at the end of every repetition, in all three of our runs** |

Readings: 3 EVEN, the same, 3 EVEN, under the floor, 3 GAIN by the mean of our three runs, 3 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 every setting handed back at the end of every repetition, in all three of our runs, 1 no growth beyond the limit, 1 no leak, 1 none in any repetition, 1 power given by the mean of our three runs, 1 power given in all three of our runs, 9 shown, not judged, 1 the runs disagree, 1 valid.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
