# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,192 | +13.9% | 118 to 174 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0664 to 0.127 | no difference beyond the noise |
| cache hit rate | 0.697 | 0.795 | +13.9% | 0.0787 to 0.116 | better |
| latency, 95th percentile (ms) | 5.65 | 5.62 | -0.6% | -0.0497 to -0.0228 | better |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.2% | -0.0241 to 0.0049 | no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.23 | -30.1% | -0.625 to -0.431 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 195 | +204.8% | 89.7 to 172 | **WORSE** |
| memory used, mean (MB) | 56.9 | 155 | +171.4% | 77.6 to 118 | **WORSE** |
| keys evicted | 49,932 | 11,192 | -77.6% | -44,262 to -33,217 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.106 | -2.7% | -0.0655 to 0.0596 | no difference beyond the noise |
| host CPU-seconds | 51.4 | 50.3 | -2.2% | -34.8 to 32.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.41 | 0.352 | -14.1% | -0.314 to 0.198 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 30.7 |  | 10.4 to 50.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 10.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,251 | 1,424 | +13.8% | 170 to 176 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0364 to 0.0601 | no difference beyond the noise |
| cache hit rate | 0.834 | 0.95 | +13.8% | 0.113 to 0.117 | better |
| latency, 95th percentile (ms) | 5.74 | 5.54 | -3.4% | -0.248 to -0.146 | better |
| latency, 99th percentile (ms) | 5.8 | 5.77 | -0.5% | -0.0472 to -0.0151 | better |
| latency, mean (ms) | 1.11 | 0.467 | -57.8% | -0.657 to -0.623 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 254 | +297.0% | 182 to 198 | **WORSE** |
| memory used, mean (MB) | 61.3 | 219 | +257.8% | 151 to 165 | **WORSE** |
| keys evicted | 73,279 | 17,630 | -75.9% | -56,642 to -54,657 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.3% | -0.0473 to 0.0355 | no difference beyond the noise |
| host CPU-seconds | 123 | 118 | -3.6% | -55.7 to 47 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.327 | 0.277 | -15.3% | -0.179 to 0.079 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 160 |  | 159 to 162 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 30.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 1,048 | +26.0% | 214 to 219 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0397 to 0.0248 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.699 | +26.0% | 0.143 to 0.146 | better |
| latency, 95th percentile (ms) | 5.51 | 5.48 | -0.6% | -0.0452 to -0.0158 | better |
| latency, 99th percentile (ms) | 5.57 | 5.56 | -0.2% | -0.013 to -0.00623 | better |
| latency, mean (ms) | 2.47 | 1.71 | -30.9% | -0.785 to -0.744 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 269 | +319.9% | 196 to 213 | **WORSE** |
| memory used, mean (MB) | 60.3 | 210 | +248.4% | 150 to 150 | **WORSE** |
| keys evicted | 185,132 | 18,693 | -89.9% | -167,219 to -165,659 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.106 | -2.6% | -0.0693 to 0.0636 | no difference beyond the noise |
| host CPU-seconds | 127 | 125 | -1.5% | -87.7 to 83.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.397 | -21.8% | -0.412 to 0.191 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 49.7 |  | 37.4 to 61.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,302 | +15.2% | 163 to 180 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00428 to 0.00185 | same |
| cache hit rate | 0.754 | 0.869 | +15.2% | 0.109 to 0.12 | better |
| latency, 95th percentile (ms) | 5.53 | 5.46 | -1.2% | -0.0773 to -0.0583 | better |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0174 to -0.00885 | better |
| latency, mean (ms) | 1.43 | 0.82 | -42.5% | -0.638 to -0.572 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 296 | +362.6% | 228 to 236 | **WORSE** |
| memory used, mean (MB) | 61.1 | 266 | +336.1% | 201 to 210 | **WORSE** |
| keys evicted | 106,664 | 29,399 | -72.4% | -81,227 to -73,303 | shown, not judged |
| host CPU busy (share of the run) | 0.0981 | 0.0905 | -7.8% | -0.0483 to 0.033 | no difference beyond the noise |
| host CPU-seconds | 114 | 106 | -7.6% | -61 to 43.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.27 | -19.8% | -0.215 to 0.0818 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 101 |  | 95.5 to 106 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
