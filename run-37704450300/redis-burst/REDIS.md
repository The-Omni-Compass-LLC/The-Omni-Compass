# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,200 | +14.7% | 118 to 190 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0744 to 0.127 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.8 | +14.7% | 0.0796 to 0.126 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0172 to -0.00676 | better |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% | -0.0301 to 0.0243 | no difference beyond the noise |
| latency, mean (ms) | 1.86 | 1.3 | -30.5% | -0.711 to -0.426 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 201 | +214.6% | 93.3 to 181 | **WORSE** |
| memory used, mean (MB) | 56.9 | 156 | +173.6% | 76.8 to 121 | **WORSE** |
| keys evicted | 49,913 | 9,703 | -80.6% | -46,280 to -34,140 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.129 | -8.7% | -0.055 to 0.0305 | no difference beyond the noise |
| host CPU-seconds | 63.2 | 58.1 | -8.1% | -27.5 to 17.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.404 | -19.9% | -0.269 to 0.068 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33 |  | 12.7 to 53.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 11.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
