# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,191 | +13.9% | 117 to 174 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0558 to 0.128 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.794 | +13.9% | 0.0775 to 0.116 | better |
| latency, 95th percentile (ms) | 5.7 | 5.68 | -0.3% | -0.0225 to -0.0134 | better |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.00722 to -0.00531 | better |
| latency, mean (ms) | 1.83 | 1.29 | -29.4% | -0.648 to -0.429 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 195 | +204.9% | 89 to 173 | **WORSE** |
| memory used, mean (MB) | 56.9 | 154 | +171.1% | 77 to 118 | **WORSE** |
| keys evicted | 49,909 | 11,212 | -77.5% | -43,997 to -33,397 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.137 | -8.5% | -0.0575 to 0.0322 | no difference beyond the noise |
| host CPU-seconds | 69.2 | 63.7 | -8.0% | -29.7 to 18.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.551 | 0.446 | -19.2% | -0.28 to 0.0682 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.7 |  | 11.4 to 48 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 10.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
