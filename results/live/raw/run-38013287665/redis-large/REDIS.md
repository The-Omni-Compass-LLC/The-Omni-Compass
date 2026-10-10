# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | -17.4 to 58.5 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00675 to 0.00574 | same |
| cache hit rate | 0.845 | 0.859 | +1.6% | -0.0113 to 0.0388 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.0218 to 0.0371 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% | -0.0164 to 0.0526 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.984 | -6.5% | -0.212 to 0.0741 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64 | +0.0% | -3.34 to 3.38 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.9 | -0.7% | -3.47 to 2.62 | no difference beyond the noise |
| keys evicted | 103,325 | 94,452 | -8.6% | -25,245 to 7,500 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.122 | +3.4% | -0.029 to 0.037 | no difference beyond the noise |
| host CPU-seconds | 197 | 205 | +3.8% | -54.9 to 69.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.354 | +2.1% | -0.11 to 0.125 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 20.1 to 35.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
