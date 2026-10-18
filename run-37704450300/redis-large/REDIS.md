# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,251 | 1,425 | +13.9% | 172 to 176 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00208 to 0.00477 | same |
| cache hit rate | 0.834 | 0.95 | +13.9% | 0.115 to 0.117 | better |
| latency, 95th percentile (ms) | 5.75 | 2.52 | -56.1% | -9.76 to 3.31 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.78 | -0.6% | -0.0367 to -0.0319 | better |
| latency, mean (ms) | 1.11 | 0.469 | -57.9% | -0.647 to -0.641 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 256 | +300.7% | 190 to 195 | **WORSE** |
| memory used, mean (MB) | 61.2 | 222 | +262.0% | 158 to 163 | **WORSE** |
| keys evicted | 73,285 | 17,277 | -76.4% | -56,757 to -55,259 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0928 | -15.6% | -0.0289 to -0.00544 | better |
| host CPU-seconds | 121 | 103 | -15.0% | -32.7 to -3.66 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.322 | 0.24 | -25.4% | -0.118 to -0.0454 | better |
| ceiling changes written (the knob's moves) | 0 | 159 |  | 157 to 161 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 30.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
