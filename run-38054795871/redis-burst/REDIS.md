# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.74 to 0.653 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0057 to -0.000311 | **WORSE** |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00104 to 0.000435 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | -0.0157 to 0.0195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.63 | +0.1% | -0.0102 to 0.0218 | no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.63 | +0.2% | 0.00117 to 0.00682 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.3 | -4.1% | -2.99 to -2.31 | better |
| memory used, mean (MB) | 57.1 | 55.5 | -3.0% | -2.13 to -1.27 | better |
| keys evicted | 71,650 | 71,741 | +0.1% | -115 to 297 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.114 | +2.8% | -0.0698 to 0.076 | no difference beyond the noise |
| host CPU-seconds | 78.5 | 80.8 | +2.9% | -56.3 to 60.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.405 | 0.417 | +2.9% | -0.29 to 0.314 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
