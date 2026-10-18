# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 927 | +0.3% | -23.8 to 29.9 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0163 to -0.00549 | **WORSE** |
| cache hit rate | 0.617 | 0.619 | +0.3% | -0.016 to 0.0196 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.0119 to 0.0116 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.1% | -0.0433 to 0.0527 | no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.03 | -0.6% | -0.11 to 0.0841 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | -6.2 to 9.67 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 62.3 | +2.6% | -6.64 to 9.8 | no difference beyond the noise |
| keys evicted | 243,120 | 241,958 | -0.5% | -21,058 to 18,735 | shown, not judged |
| host CPU busy (share of the run) | 0.0597 | 0.0638 | +7.0% | -0.0461 to 0.0544 | no difference beyond the noise |
| host CPU-seconds | 105 | 113 | +7.8% | -85 to 101 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.253 | 0.271 | +7.2% | -0.204 to 0.241 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 1.61 to 36.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
