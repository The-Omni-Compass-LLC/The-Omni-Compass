# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v10)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 39108180989 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| B | 39115242861 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |
| C | 39123583570 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| node-hours | +0.2% (-0.5 to +0.9) | +0.1% (-0.4 to +0.5) | +0.0% (-0.5 to +0.6) | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.2% (+1.4 to +2.9) | +1.4% (+1.0 to +1.9) | +1.7% (+1.1 to +2.4) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.2% (+1.4 to +2.9) | +1.4% (+1.0 to +1.9) | +1.7% (+1.1 to +2.4) | **power given in all three of our runs** |
| response time (ms), mean | -39.1% (-41.3 to -36.9) | -37.6% (-50.9 to -24.2) | -37.6% (-45.4 to -29.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -50.9% (-53.7 to -48.2) | -53.4% (-67.1 to -39.7) | -51.7% (-59.5 to -43.8) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -57.4% (-63.6 to -51.2) | -62.2% (-77.5 to -46.8) | -58.9% (-67.7 to -50.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -100.0% (-143.3 to -56.7) | -100.0% (-171.6 to -28.4) | -98.3% (-134.2 to -62.4) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | -100.0% (-326.2 to +126.2) | -100.0% (-221.6 to +21.6) | -100.0% (-161.6 to -38.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| settings commands the governor wrote on its own (no person touched either arm) | +17.1 (+16.87 to +17.33) | +17.9 (+16.98 to +18.82) | +17.1 (+16.18 to +18.02) | shown, not judged |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +51.1% (-41.0 to +143.3) | +101.2% (-115.0 to +317.5) | -36.4% (-118.6 to +45.9) | shown, not judged |
| utilisation (used / allocatable) | +36.3% (+34.0 to +38.5) | +25.9% (+15.4 to +36.4) | +31.2% (+26.2 to +36.2) | shown, not judged |
| CPU used (cores), mean | +36.3% (+34.0 to +38.5) | +25.9% (+15.4 to +36.4) | +31.2% (+26.2 to +36.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01346 (+0.0128 to +0.01412) | +0.0117 (+0.01011 to +0.01329) | +0.01284 (+0.01177 to +0.01391) | shown, not judged |
| CPU used with Omni's own (cores), mean | +37.7% (+35.5 to +40.0) | +27.2% (+16.6 to +37.9) | +32.6% (+27.5 to +37.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -25.1% (-26.2 to -24.0) | -18.0% (-23.8 to -12.1) | -22.1% (-24.4 to -19.8) | shown, not judged |
| HPA replicas, mean | +2.9% (-0.3 to +6.1) | +0.8% (-2.1 to +3.6) | +2.3% (+0.1 to +4.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pods started | +0.0% (-27.0 to +27.0) | +0.0% (-19.4 to +19.4) | -4.0% (-17.1 to +9.1) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -24.8% (-77.5 to +27.9) | +16.7% (-38.9 to +72.2) | -12.2% (-43.0 to +18.5) | EVEN, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -16.0% (-61.4 to +29.4) | +18.5% (-22.7 to +59.7) | -5.0% (-28.6 to +18.6) | EVEN, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +34.4% (+32.6 to +36.2) | +26.0% (+16.3 to +35.7) | +31.5% (+27.1 to +35.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN in all three of our runs, 2 power given in all three of our runs, 2 EVEN, no difference beyond the noise (2 of 3 runs), 4 EVEN, no difference beyond the noise (all three runs), 4 EVEN, the same, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
