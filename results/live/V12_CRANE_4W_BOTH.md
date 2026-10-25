# Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on top of Crane against the organism alone (register row 90): the A/B/C three-run table (Omni v12)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

**The comparison.** In this table "omni" stands for Omni-Compass on top of the orchestrator and "native" for the organism alone: each cell is the first against the second, paired within one repetition (the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), and each word is read by the gauge's aim for the first.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39438326588 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| B | 39438344234 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |
| C | 39438362894 | `b1e552d38424` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | =0.0% (−0.0 to +0.0) | =0.0% (−0.0 to +0.0) | =0.0% (+0.0 to +0.0) | EVEN, the same |
| node-hours | =0.0% (−0.5 to +0.4) | =0.2% (−0.6 to +0.2) | =0.1% (−0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.11%) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.7% (+0.2 to +1.2) | +0.6% (+0.1 to +1.0) | +0.6% (+0.1 to +1.1) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.7% (+0.2 to +1.2) | +0.6% (+0.1 to +1.0) | +0.6% (+0.1 to +1.1) | **power given in all three of our runs** |
| response time (ms), mean | −2.2% (−4.4 to +0.1) | −2.4% (−5.1 to +0.2) | −1.7% (−4.4 to +1.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| response time (ms), 95th percentile | −0.6% (−3.5 to +2.4) | −1.0% (−5.1 to +3.0) | +0.7% (−3.6 to +5.0) | **the runs disagree** |
| response time (ms), 99th percentile | +3.1% (−3.4 to +9.7) | −4.6% (−11.1 to +2.0) | +3.8% (+0.3 to +7.4) | **the runs disagree** |
| time over the response line (% of samples) | +21.7% (−15.4 to +58.8) | −4.0% (−39.4 to +31.3) | +23.6% (−6.3 to +53.4) | **the runs disagree** |
| failed requests (%) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | +100.0% (+16.6 to +183.4) | −0.3000 (−0.6455 to +0.0455) | +66.7% (−33.9 to +167.2) | **the runs disagree** |
| settings commands the governor wrote on its own (no person touched either arm) | +2.5 (+1.183 to +3.817) | +3.2 (+1.1 to +5.3) | +2.3 (+0.9076 to +3.692) | shown, not judged |
| pods with no machine to take them (unschedulable) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | =0.0000 (±0.0000 to ±0.0000) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -0.5% (-113.0 to +112.0) | +208.8% (-53.3 to +471.0) | +37.5% (-76.0 to +151.0) | shown, not judged |
| utilisation (used / allocatable) | +13.9% (+11.0 to +16.7) | +13.6% (+11.0 to +16.2) | +14.1% (+12.0 to +16.2) | shown, not judged |
| CPU used (cores), mean | +13.9% (+11.0 to +16.7) | +13.6% (+11.0 to +16.2) | +14.1% (+12.0 to +16.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01025 (+0.008645 to +0.01186) | +0.00995 (+0.007923 to +0.01198) | +0.01016 (+0.008942 to +0.01138) | shown, not judged |
| CPU used with Omni's own (cores), mean | +15.0% (+12.0 to +18.0) | +14.7% (+11.9 to +17.5) | +15.2% (+13.0 to +17.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -11.4% (-13.2 to -9.6) | -11.1% (-12.5 to -9.7) | -11.6% (-13.0 to -10.1) | shown, not judged |
| HPA replicas, mean | +12.5% (+4.9 to +20.1) | +17.5% (+7.3 to +27.7) | +15.0% (+8.9 to +21.0) | **power given in all three of our runs** |
| pods started | +85.4% (+45.7 to +125.0) | +67.3% (+24.3 to +110.4) | +66.7% (+34.9 to +98.5) | **power given in all three of our runs** |
| pod start wait, total (s) | −80.9% (−32.7 to −129.0) | −68.8% (−12.8 to −124.7) | −71.8% (−31.7 to −112.0) | **LOSS in all three of our runs** |
| pod start wait, mean (s) | +3.8% (−11.6 to +19.1) | +2.2% (−20.3 to +24.7) | −0.9% (−13.9 to +12.1) | **the runs disagree** |
| host CPU busy, the real machine under kind (%) | +18.5% (+15.1 to +21.9) | +19.0% (+15.3 to +22.8) | +19.2% (+16.9 to +21.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 EVEN, the same, 1 EVEN, under the floor, 1 LOSS by the mean of our three runs, 1 LOSS in all three of our runs, 4 power given in all three of our runs, 9 shown, not judged, 5 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
