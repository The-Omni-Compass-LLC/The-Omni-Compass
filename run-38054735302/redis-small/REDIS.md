# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 924 | -0.1% | -2.89 to 0.318 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0556 to 0.0724 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.1% | -0.0018 to -1.66e-05 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0123 to 0.012 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.0117 to 0.0231 | no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.2% | -0.00839 to 0.0184 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.0382 to 2 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.0561 to 0.184 | **WORSE** |
| keys evicted | 243,159 | 244,886 | +0.7% | -2,359 to 5,812 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.148 | +8.1% | -0.0232 to 0.0453 | no difference beyond the noise |
| host CPU-seconds | 228 | 249 | +9.4% | -44.9 to 87.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.599 | +9.6% | -0.108 to 0.212 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 18.9 to 26.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
