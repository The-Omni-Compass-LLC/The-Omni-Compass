# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,236 | +4.4% | 31.1 to 72.4 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00293 to 0.00249 | same |
| cache hit rate | 0.789 | 0.824 | +4.4% | 0.0208 to 0.0483 | better |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0179 to 0.00753 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0107 to 0.0177 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.15 | -14.0% | -0.27 to -0.107 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.3 | +19.2% | 4.38 to 20.2 | **WORSE** |
| memory used, mean (MB) | 61.2 | 71.2 | +16.3% | 2.74 to 17.2 | **WORSE** |
| keys evicted | 138,104 | 116,177 | -15.9% | -30,035 to -13,819 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.113 | -8.1% | -0.0401 to 0.0203 | no difference beyond the noise |
| host CPU-seconds | 205 | 187 | -8.6% | -76 to 40.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.385 | 0.337 | -12.5% | -0.151 to 0.0551 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36.7 |  | 27.9 to 45.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
