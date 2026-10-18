# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
