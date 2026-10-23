# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,328 | 1,327 | -0.0% | -0.0843 to 0.0201 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.011 to 0.0138 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -1.19e-05 to 9.39e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.55 | -0.3% | -0.0457 to 0.0169 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.67 | -0.2% | -0.049 to 0.0266 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.752 | 0.746 | -0.9% | -0.0243 to 0.0114 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.000882 to 0.0435 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0995 | 0.0786 | -21.0% | -0.093 to 0.0512 | EVEN, no difference beyond the noise |
| host CPU-seconds | 71 | 54.7 | -22.9% | -73.4 to 40.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.229 | -22.9% | -0.307 to 0.171 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.145 to 0.212 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00117 to 0.00186 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -3.11e-06 to 1.14e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.204 | 0.202 | -0.8% | -0.00395 to 0.000525 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0148 to 0.0127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.264 | 0.263 | -0.4% | -0.00333 to 0.00136 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.023 to 0.0354 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0988 | -11.7% | -0.0293 to 0.0031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 170 | -12.9% | -56.2 to 5.66 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.295 | 0.257 | -12.9% | -0.0849 to 0.00856 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.217 to 0.361 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0279 to 0.00587 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | -0.0% | -6.23e-06 to 2.27e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.1% | -0.0336 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.0238 to 0.00826 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.3% | -0.0135 to 0.00462 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00926 to 0.0397 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.116 | +1.1% | -0.0053 to 0.00785 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 194 | +1.6% | -9.03 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.362 | 0.368 | +1.6% | -0.0172 to 0.0288 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,391 | 1,392 | +0.1% | -0.0114 to 1.55 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0256 to 0.0216 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -7.21e-06 to 6.72e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.0183 to 0.0203 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.0% | -0.00919 to 0.0125 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.547 | 0.544 | -0.6% | -0.00624 to -0.000425 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0404 to 0.0799 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.118 | +8.3% | -0.0625 to 0.0806 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 207 | +9.6% | -124 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.302 | 0.331 | +9.6% | -0.199 to 0.257 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
