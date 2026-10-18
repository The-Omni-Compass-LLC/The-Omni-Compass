# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 920 | -0.5% | -8.62 to 0.269 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0587 to 0.0847 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.614 | -0.5% | -0.00518 to -0.000828 | **WORSE** |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.0119 to 0.0106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.28 | +0.4% | -0.017 to 0.0571 | no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.06 | +0.7% | -0.00621 to 0.0365 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.5 | -0.7% | -0.96 to 0.0596 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.1 | -1.0% | -1.21 to 0.0572 | no difference beyond the noise |
| keys evicted | 243,216 | 247,401 | +1.7% | -1,862 to 10,231 | shown, not judged |
| host CPU busy (share of the run) | 0.0657 | 0.0554 | -15.7% | -0.0373 to 0.0166 | no difference beyond the noise |
| host CPU-seconds | 117 | 97 | -16.8% | -70.2 to 31.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.234 | -16.4% | -0.167 to 0.075 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23.7 |  | 17.4 to 29.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
