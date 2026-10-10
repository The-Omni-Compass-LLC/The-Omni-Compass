# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,181 | -0.2% | -3.85 to -1.01 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00401 to 0.00271 | same |
| cache hit rate | 0.789 | 0.788 | -0.2% | -0.00248 to -0.000786 | **WORSE** |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00107 to 0.011 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | -0.00333 to 0.0275 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.36 | +1.0% | 0.00682 to 0.0191 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.5 | -0.8% | -2.41 to 1.4 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 60.8 | -0.7% | -1.95 to 1.07 | no difference beyond the noise |
| keys evicted | 138,149 | 140,340 | +1.6% | 469 to 3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.122 | -5.9% | -0.031 to 0.0157 | no difference beyond the noise |
| host CPU-seconds | 218 | 203 | -6.9% | -60.2 to 30 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.382 | -6.7% | -0.112 to 0.0569 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 15.4 to 28.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
