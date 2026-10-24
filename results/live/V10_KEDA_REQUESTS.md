# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39108180989 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115242861 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39123583570 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | EVEN, the same |
| node-hours | =0.3% (−0.7 to +0.2) | =0.2% (−0.6 to +0.2) | =0.4% (−0.9 to +0.1) | EVEN, under the floor (the three runs' mean 0.29%) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.0% (+1.4 to +2.6) | +2.2% (+1.7 to +2.8) | +2.0% (+1.3 to +2.8) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.0% (+1.4 to +2.6) | +2.2% (+1.7 to +2.8) | +2.0% (+1.3 to +2.8) | **power given in all three of our runs** |
| response time (ms), mean | +57.2% (+46.2 to +68.2) | +57.8% (+48.7 to +66.9) | +57.2% (+47.0 to +67.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | +72.4% (+61.5 to +83.3) | +72.9% (+62.8 to +82.9) | +72.8% (+60.7 to +84.8) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | +56.9% (+49.9 to +63.9) | +56.9% (+46.8 to +67.0) | +56.4% (+50.2 to +62.7) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | +96.2% (+45.4 to +147.1) | +97.3% (+64.4 to +130.1) | +96.9% (+54.2 to +139.5) | **GAIN in all three of our runs** |
| failed requests (%) | −0.0123 (−0.0403 to +0.0156) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +97.9% (+53.5 to +142.2) | +98.4% (+70.2 to +126.5) | +100.0% (+60.8 to +139.2) | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.2 (+3.748 to +4.652) | +5 (+3.651 to +6.349) | +4.4 (+4.031 to +4.769) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -14.8% (-49.9 to +20.4) | -46.2% (-98.3 to +5.9) | +3.8% (-65.7 to +73.2) | shown, not judged |
| utilisation (used / allocatable) | +50.4% (+41.6 to +59.3) | +52.5% (+45.9 to +59.1) | +53.6% (+43.7 to +63.5) | shown, not judged |
| CPU used (cores), mean | +50.4% (+41.6 to +59.3) | +52.5% (+45.9 to +59.1) | +53.6% (+43.7 to +63.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00918 (+0.007923 to +0.01044) | +0.00977 (+0.008715 to +0.01082) | +0.0095 (+0.008281 to +0.01072) | shown, not judged |
| CPU used with Omni's own (cores), mean | +51.7% (+42.7 to +60.6) | +53.8% (+47.1 to +60.6) | +54.9% (+44.9 to +65.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -31.4% (-34.2 to -28.6) | -32.4% (-34.1 to -30.8) | -32.5% (-35.5 to -29.5) | shown, not judged |
| HPA replicas, mean | +18.7% (+10.2 to +27.2) | +18.6% (+13.6 to +23.7) | +12.6% (+5.8 to +19.4) | **GAIN in all three of our runs** |
| pods started | +24.1% (+7.5 to +40.8) | +24.1% (+12.2 to +36.1) | +17.2% (+4.2 to +30.2) | **GAIN in all three of our runs** |
| pod start wait, total (s) | +15.7% (−4.0 to +35.4) | +13.8% (−2.6 to +30.3) | −3.3% (−27.1 to +20.6) | **the runs disagree** |
| pod start wait, mean (s) | −13.0% (−0.2 to −25.9) | −14.1% (−4.4 to −23.7) | −21.1% (−4.8 to −37.3) | **LOSS in all three of our runs** |
| host CPU busy, the real machine under kind (%) | +45.4% (+37.9 to +53.0) | +48.6% (+42.5 to +54.6) | +50.1% (+41.1 to +59.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 EVEN, the same, 1 EVEN, under the floor, 7 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 1 LOSS in all three of our runs, 2 power given in all three of our runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
