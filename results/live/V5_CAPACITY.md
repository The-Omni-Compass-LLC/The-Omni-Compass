# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v5)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change with its 95% interval (completed work in percent of native; capacity in requests a second). Every judged row gets one of three readings. **Better** or **WORSE in all three of our runs**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero; that is the result. **The runs disagree**: runs clear of the noise point different ways. Every row is shown, losses included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

| Run | GitHub run | Label | Commit | Engine | Pairs per cap |
|---|---|---|---|---|---:|
| A | 38339841468 | A | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |
| B | 38339847249 | B | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |
| C | 38339853176 | C | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |

| Cap (cores) | Measure | A | B | C | Reading |
|---:|---|---|---|---|---|
| 1 | completed work (requests answered within the line over the window; higher is better) | +2.8% (-9.3 to +14.9) | -0.1% (-5.3 to +5.0) | -4.4% (-11.0 to +2.1) | no difference beyond the noise (all three runs) |
| 1 | work inside the response line (requests a second; the capacity test's own gauge, higher is better) | +0.00 req/s (+0.00 to +0.00) | +0.40 req/s (-0.71 to +1.51) | -0.40 req/s (-1.51 to +0.71) | no difference beyond the noise (all three runs) |
| 1.5 | completed work (requests answered within the line over the window; higher is better) | -4.7% (-10.1 to +0.8) | -2.7% (-9.2 to +3.9) | -2.3% (-10.2 to +5.7) | no difference beyond the noise (all three runs) |
| 1.5 | work inside the response line (requests a second; the capacity test's own gauge, higher is better) | -0.40 req/s (-2.48 to +1.68) | -0.40 req/s (-2.48 to +1.68) | +0.80 req/s (-1.42 to +3.02) | no difference beyond the noise (all three runs) |
| 2 | completed work (requests answered within the line over the window; higher is better) | -2.4% (-9.2 to +4.4) | -1.8% (-3.4 to -0.1) | +1.9% (-2.2 to +5.9) | no difference beyond the noise in 2 of 3 runs |
| 2 | work inside the response line (requests a second; the capacity test's own gauge, higher is better) | +0.00 req/s (+0.00 to +0.00) | +0.40 req/s (-0.71 to +1.51) | +0.40 req/s (-0.71 to +1.51) | no difference beyond the noise (all three runs) |
| 3 | completed work (requests answered within the line over the window; higher is better) | -0.5% (-2.6 to +1.5) | +0.6% (-2.0 to +3.1) | -1.6% (-4.3 to +1.1) | no difference beyond the noise (all three runs) |
| 3 | work inside the response line (requests a second; the capacity test's own gauge, higher is better) | -0.80 req/s (-2.16 to +0.56) | +0.40 req/s (-0.71 to +1.51) | -0.40 req/s (-1.51 to +0.71) | no difference beyond the noise (all three runs) |

Readings: 7 no difference beyond the noise (all three runs), 1 no difference beyond the noise in 2 of 3 runs.

How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work from the same capacity; where neither arm can do more under the cap, the rows show no difference beyond the noise, and that is the result. Each run's own table, with its audit lines and what each step up in the cap gives each arm: `CAPACITY.md` in its archived folder.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
