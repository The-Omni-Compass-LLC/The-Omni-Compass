# The GPU card in simulation: each base alone, and with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (a model, not a meter). Seeds 5000-5009, 600 s each, commit `54b28cf8c`, 2026-10-10 21:24 UTC. Model: `realms/gpu_card.py`; the law: `omnicompass/compass_law.py` and the verdict `omnicompass/verdict.py`.

Omni-Compass never runs the card. It sits on top of what already runs it (the card's own firmware, or an operator's power cap) and moves the clock ceiling that base already accepts (the power limit stays where the base set it): it parks the clock when the work stops and races it back the moment work arrives, and a level is used only after a paired trial on the card shows it adds at most 0.5% to the card's own time on the first request after a rest (docs/GPU_PREREGISTRATION.md, amendment 13). Every comparison below is a base alone against the same base with Omni on top, on the same seeds and the same requests.

## Compute-bound work (matrix products)

### Mean over seeds

| Gauge | The card's firmware alone | Firmware + Omni on top | A fixed 105 W power cap alone | The cap + Omni on top |
|---|---:|---:|---:|---:|
| work per energy (requests per kJ) | 51.7 | 57.5 | 54.4 | 54.7 |
| energy (J) | 68549 | 61681 | 64514 | 64109 |
| requests served | 3547 | 3547 | 3507 | 3510 |
| response, median (ms) | 92.7 | 86.8 | 49134.4 | 48441.8 |
| response, 95th percentile (ms) | 471.9 | 438.3 | 76440.1 | 75760.9 |
| response, 99th percentile (ms) | 827.1 | 776.0 | 81883.7 | 81209.9 |
| requests over the service line (%) | 1.08% | 0.91% | 88.65% | 88.59% |
| first request after a rest, median (ms) | 60.1 | 56.4 | 109.5 | 110.0 |
| the card's own time per request, median (ms) | 76.7 | 74.8 | 166.2 | 166.0 |
| clock, mean share of top | 0.769 | 0.559 | 0.287 | 0.276 |
| clock, standard deviation | 0.277 | 0.157 | 0.213 | 0.184 |
| temperature, peak (C) | 72.9 | 71.7 | 64.4 | 64.4 |
| temperature, mean (C) | 64.3 | 61.4 | 62.0 | 61.8 |

### With Omni on top against the same base alone (ratios: geometric mean over seeds, 95% interval; time over the line: mean difference)

| Gauge | firmware + Omni on top vs the card's firmware alone | the cap + Omni on top vs a fixed 105 W power cap alone |
|---|---:|---:|
| work per energy | +11.14% (+10.80% to +11.47%) | +0.71% (+0.61% to +0.81%) |
| energy | -10.02% (-10.29% to -9.75%) | -0.63% (-0.72% to -0.54%) |
| response, median | -6.31% (-6.82% to -5.80%) | -1.42% (-1.68% to -1.16%) |
| response, p95 | -7.00% (-7.93% to -6.07%) | -0.89% (-1.05% to -0.73%) |
| response, p99 | -6.22% (-7.20% to -5.22%) | -0.82% (-0.97% to -0.68%) |
| time over the line (pp) | -0.173 (-0.313 to -0.032) | -0.054 (-0.115 to +0.008) |
| requests served | +0.00% (+0.00% to +0.00%) | +0.08% (+0.03% to +0.12%) |

Verdict over all Omni runs: 60 trials, 16 steps allowed, 31 refused.

## AI token generation (85% of each request waiting on memory)

### Mean over seeds

| Gauge | The card's firmware alone | Firmware + Omni on top | A fixed 105 W power cap alone | The cap + Omni on top |
|---|---:|---:|---:|---:|
| work per energy (requests per kJ) | 69.2 | 79.0 | 70.6 | 80.3 |
| energy (J) | 51282 | 45031 | 50244 | 44418 |
| requests served | 3547 | 3547 | 3547 | 3547 |
| response, median (ms) | 38.4 | 38.6 | 38.6 | 38.8 |
| response, 95th percentile (ms) | 75.9 | 76.1 | 80.0 | 79.3 |
| response, 99th percentile (ms) | 106.9 | 107.3 | 115.3 | 114.4 |
| requests over the service line (%) | 0.00% | 0.00% | 0.00% | 0.00% |
| first request after a rest, median (ms) | 36.8 | 37.1 | 36.9 | 37.1 |
| the card's own time per request, median (ms) | 36.8 | 37.0 | 37.4 | 37.5 |
| clock, mean share of top | 1.000 | 0.862 | 0.977 | 0.839 |
| clock, standard deviation | 0.000 | 0.109 | 0.067 | 0.114 |
| temperature, peak (C) | 60.1 | 57.6 | 59.0 | 56.9 |
| temperature, mean (C) | 56.5 | 53.8 | 56.0 | 53.5 |

### With Omni on top against the same base alone (ratios: geometric mean over seeds, 95% interval; time over the line: mean difference)

| Gauge | firmware + Omni on top vs the card's firmware alone | the cap + Omni on top vs a fixed 105 W power cap alone |
|---|---:|---:|
| work per energy | +14.03% (+9.63% to +18.61%) | +13.39% (+7.60% to +19.49%) |
| energy | -12.30% (-15.69% to -8.79%) | -11.81% (-16.31% to -7.06%) |
| response, median | +0.63% (+0.06% to +1.20%) | +0.48% (-0.03% to +1.00%) |
| response, p95 | +0.32% (-0.00% to +0.64%) | -0.86% (-1.27% to -0.45%) |
| response, p99 | +0.40% (+0.05% to +0.74%) | -0.85% (-1.25% to -0.44%) |
| time over the line (pp) | +0.000 (+0.000 to +0.000) | +0.000 (+0.000 to +0.000) |
| requests served | +0.00% (+0.00% to +0.00%) | +0.00% (+0.00% to +0.00%) |

Verdict over all Omni runs: 70 trials, 21 steps allowed, 49 refused.

Requests served are the same work in every arm (the stream is the seed's). The compute model is fitted to one A10's own meter (energy within 0.1% of both arms of the paid run); the token-generation model's power and memory share are assumed. A model written by the same people who wrote the brain is not an independent test: the number that counts is a rented card's own meter.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
