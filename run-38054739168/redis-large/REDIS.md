# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,301 | +2.9% | 23.4 to 49.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000312 to 0.00271 | same |
| cache hit rate | 0.844 | 0.868 | +2.9% | 0.0166 to 0.0321 | better |
| latency, 95th percentile (ms) | 5.65 | 5.61 | -0.6% | -0.0887 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.76 | -0.9% | -0.259 to 0.156 | no difference beyond the noise |
| latency, mean (ms) | 1.04 | 0.898 | -13.4% | -0.214 to -0.0648 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.7% | -0.237 to 3.75 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +0.9% | -0.981 to 2.1 | no difference beyond the noise |
| keys evicted | 103,930 | 88,150 | -15.2% | -21,020 to -10,540 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.13 | +6.2% | -0.0147 to 0.0299 | no difference beyond the noise |
| host CPU-seconds | 215 | 232 | +8.0% | -31.7 to 66.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.396 | +5.0% | -0.0653 to 0.103 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33 |  | 30.5 to 35.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
