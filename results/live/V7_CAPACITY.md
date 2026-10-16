# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v5)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change with its 95% interval (completed work in percent of native; capacity in requests a second). Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero; completed work and capacity are work done, so more is GAIN and less is LOSS. **EVEN, no difference beyond the noise**: in the runs counted, the interval includes zero; that is the result. **The runs disagree**: runs clear of the noise point different ways. Every row is shown, LOSS included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Label | Commit | Engine | Pairs per cap |
|---|---|---|---|---|---:|
| A | 38843275163 | A | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| B | 38843278442 | B | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| C | 38843281639 | C | `b1eb8294f4a7` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |

| Cap (cores) | Measure | A | B | C | Reading |
|---:|---|---|---|---|---|
| 1 | completed work (requests answered within the line over the window) | +3.8% (+0.2 to +7.3) | +1.5% (-14.3 to +17.3) | -6.1% (-21.2 to +8.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| 1 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (+0.00 to +0.00) | -0.40 req/s (-1.51 to +0.71) | -0.40 req/s (-1.51 to +0.71) | EVEN, no difference beyond the noise (all three runs) |
| 1.5 | completed work (requests answered within the line over the window) | +1.5% (-6.1 to +9.2) | -1.7% (-9.1 to +5.7) | +0.5% (-8.6 to +9.6) | EVEN, no difference beyond the noise (all three runs) |
| 1.5 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (+0.00 to +0.00) | -0.40 req/s (-2.48 to +1.68) | -0.80 req/s (-2.16 to +0.56) | EVEN, no difference beyond the noise (all three runs) |
| 2 | completed work (requests answered within the line over the window) | -0.7% (-6.9 to +5.5) | -1.9% (-8.8 to +5.1) | +2.4% (-3.0 to +7.7) | EVEN, no difference beyond the noise (all three runs) |
| 2 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (+0.00 to +0.00) | +0.00 req/s (+0.00 to +0.00) | -0.40 req/s (-1.51 to +0.71) | EVEN, no difference beyond the noise (all three runs) |
| 3 | completed work (requests answered within the line over the window) | -0.9% (-2.5 to +0.7) | -0.3% (-1.2 to +0.6) | -1.2% (-5.0 to +2.6) | EVEN, no difference beyond the noise (all three runs) |
| 3 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (+0.00 to +0.00) | +0.00 req/s (-1.76 to +1.76) | -1.20 req/s (-2.56 to +0.16) | EVEN, no difference beyond the noise (all three runs) |

Readings: 1 EVEN, no difference beyond the noise (2 of 3 runs), 7 EVEN, no difference beyond the noise (all three runs).

How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work from the same capacity, a GAIN; where neither arm can do more under the cap, the rows read EVEN, no difference beyond the noise, and that is the result. Each run's own table, with its audit lines and what each step up in the cap gives each arm: `CAPACITY.md` in its archived folder.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
