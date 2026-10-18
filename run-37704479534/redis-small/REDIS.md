# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 1,051 | +26.6% | 207 to 234 | better |
| throughput (requests a second) | 1,499 | 1,499 | +0.0% | -0.0304 to 0.0401 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.702 | +26.5% | 0.139 to 0.156 | better |
| latency, 95th percentile (ms) | 5.73 | 5.71 | -0.4% | -0.029 to -0.0172 | better |
| latency, 99th percentile (ms) | 6.68 | 6.35 | -4.9% | -0.809 to 0.156 | no difference beyond the noise |
| latency, mean (ms) | 2.65 | 1.84 | -30.7% | -0.874 to -0.75 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 272 | +325.0% | 197 to 219 | **WORSE** |
| memory used, mean (MB) | 60.3 | 212 | +250.8% | 148 to 155 | **WORSE** |
| keys evicted | 185,155 | 15,258 | -91.8% | -182,670 to -157,125 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.138 | -11.7% | -0.0434 to 0.00695 | no difference beyond the noise |
| host CPU-seconds | 174 | 154 | -11.4% | -52.7 to 13.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.698 | 0.488 | -30.0% | -0.348 to -0.0701 | better |
| ceiling changes written (the knob's moves) | 0 | 48 |  | 38.1 to 57.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
