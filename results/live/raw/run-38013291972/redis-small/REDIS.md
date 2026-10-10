# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 920 | -0.6% | -6.15 to -4.83 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00856 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.614 | -0.6% | -0.00392 to -0.00329 | **WORSE** |
| latency, 95th percentile (ms) | 5.51 | 5.52 | +0.1% | -0.0237 to 0.0318 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.1% | -0.0117 to 0.0269 | no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.17 | +1.1% | 0.00834 to 0.0378 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.4 | -0.9% | -0.684 to -0.451 | better |
| memory used, mean (MB) | 60.7 | 60 | -1.2% | -0.797 to -0.644 | better |
| keys evicted | 243,254 | 248,936 | +2.3% | 5,485 to 5,880 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.111 | +1.2% | -0.00734 to 0.0101 | no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +1.2% | -15.6 to 20.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.469 | +1.8% | -0.0354 to 0.0523 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25.7 |  | 22.8 to 28.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
