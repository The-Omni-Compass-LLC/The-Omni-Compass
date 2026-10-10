# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -1.34 to 0.441 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0128 to 0.022 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000887 to 0.000304 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.56 | -0.2% | -0.0426 to 0.0199 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0219 to 0.0209 | no difference beyond the noise |
| latency, mean (ms) | 1.6 | 1.6 | -0.1% | -0.0184 to 0.0155 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.53 to -1.98 | better |
| memory used, mean (MB) | 57.1 | 55.3 | -3.2% | -2.49 to -1.14 | better |
| keys evicted | 71,668 | 71,754 | +0.1% | -86.4 to 258 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.109 | +6.7% | -0.0894 to 0.103 | no difference beyond the noise |
| host CPU-seconds | 72.8 | 78.5 | +7.8% | -70.8 to 82.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.405 | +7.8% | -0.365 to 0.424 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
