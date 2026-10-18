# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 1,049 | +26.0% | 214 to 220 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00375 to 0.00706 | better |
| cache hit rate | 0.555 | 0.7 | +26.1% | 0.143 to 0.147 | better |
| latency, 95th percentile (ms) | 5.64 | 5.6 | -0.6% | -0.046 to -0.0214 | better |
| latency, 99th percentile (ms) | 5.7 | 5.68 | -0.3% | -0.0294 to -0.00766 | better |
| latency, mean (ms) | 2.54 | 1.75 | -31.1% | -0.79 to -0.787 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 270 | +322.5% | 198 to 215 | **WORSE** |
| memory used, mean (MB) | 60.3 | 211 | +249.2% | 150 to 151 | **WORSE** |
| keys evicted | 185,038 | 16,311 | -91.2% | -173,975 to -163,478 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.125 | -12.5% | -0.0218 to -0.0141 | better |
| host CPU-seconds | 170 | 148 | -12.7% | -26.4 to -16.6 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.68 | 0.471 | -30.7% | -0.235 to -0.183 | better |
| ceiling changes written (the knob's moves) | 0 | 50.3 |  | 34.4 to 66.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
