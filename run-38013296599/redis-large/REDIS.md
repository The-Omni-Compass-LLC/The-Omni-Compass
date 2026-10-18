# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,308 | +3.2% | 13.6 to 67.4 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00171 to 0.000439 | same |
| cache hit rate | 0.845 | 0.872 | +3.2% | 0.00898 to 0.0447 | better |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.00737 to -0.000917 | better |
| latency, 99th percentile (ms) | 5.24 | 5.23 | -0.1% | -0.0199 to 0.0095 | no difference beyond the noise |
| latency, mean (ms) | 0.869 | 0.731 | -15.9% | -0.233 to -0.0431 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.3 | +3.6% | -1.59 to 6.19 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 63.2 | +3.1% | -1.4 to 5.24 | no difference beyond the noise |
| keys evicted | 103,266 | 85,544 | -17.2% | -29,842 to -5,602 | shown, not judged |
| host CPU busy (share of the run) | 0.0452 | 0.0601 | +33.0% | -0.0183 to 0.0482 | no difference beyond the noise |
| host CPU-seconds | 79 | 107 | +35.4% | -34.2 to 90.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.139 | 0.182 | +31.0% | -0.0601 to 0.146 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 25.5 to 33.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
