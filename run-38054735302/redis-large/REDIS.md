# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,299 | +2.6% | 27.5 to 38.2 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00362 to 0.00166 | same |
| cache hit rate | 0.845 | 0.867 | +2.6% | 0.0183 to 0.0256 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0148 to -0.00745 | better |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0128 to 0.00951 | no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.935 | -11.6% | -0.137 to -0.108 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.2 | +3.4% | -2.24 to 6.65 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.6 | +2.2% | -2.92 to 5.62 | no difference beyond the noise |
| keys evicted | 103,312 | 89,028 | -13.8% | -16,531 to -12,035 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.108 | -7.0% | -0.0228 to 0.00651 | no difference beyond the noise |
| host CPU-seconds | 193 | 179 | -7.4% | -41 to 12.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.339 | 0.307 | -9.7% | -0.0782 to 0.0123 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 14.9 to 41.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
