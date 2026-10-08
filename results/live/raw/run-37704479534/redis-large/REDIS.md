# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,252 | 1,424 | +13.7% | 167 to 177 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00163 to 0.00132 | same |
| cache hit rate | 0.835 | 0.95 | +13.7% | 0.111 to 0.118 | better |
| latency, 95th percentile (ms) | 5.63 | 5.27 | -6.5% | -0.38 to -0.352 | better |
| latency, 99th percentile (ms) | 5.73 | 5.67 | -1.1% | -0.0783 to -0.0512 | better |
| latency, mean (ms) | 1.04 | 0.407 | -60.7% | -0.651 to -0.608 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 252 | +294.2% | 181 to 196 | **WORSE** |
| memory used, mean (MB) | 61.3 | 217 | +254.6% | 148 to 164 | **WORSE** |
| keys evicted | 73,077 | 17,809 | -75.6% | -57,067 to -53,468 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0913 | -17.4% | -0.0519 to 0.0133 | no difference beyond the noise |
| host CPU-seconds | 130 | 107 | -17.5% | -65 to 19.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.347 | 0.251 | -27.5% | -0.19 to 5.6e-05 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 161 |  | 160 to 163 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 30.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
