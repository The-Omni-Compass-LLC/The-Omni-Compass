# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,252 | +5.9% | 60 to 78.8 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00364 to 0.00546 | same |
| cache hit rate | 0.789 | 0.835 | +5.9% | 0.0397 to 0.0526 | better |
| latency, 95th percentile (ms) | 5.52 | 5.49 | -0.6% | -0.0559 to -0.0114 | better |
| latency, 99th percentile (ms) | 5.6 | 5.59 | -0.2% | -0.0285 to 0.00721 | no difference beyond the noise |
| latency, mean (ms) | 1.24 | 0.996 | -20.0% | -0.287 to -0.21 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 85.7 | +33.9% | 17.3 to 26.1 | **WORSE** |
| memory used, mean (MB) | 61.2 | 78.8 | +28.8% | 13.5 to 21.8 | **WORSE** |
| keys evicted | 138,277 | 107,939 | -21.9% | -34,681 to -25,995 | shown, not judged |
| host CPU busy (share of the run) | 0.0929 | 0.102 | +10.3% | 0.000434 to 0.0187 | **WORSE** |
| host CPU-seconds | 162 | 181 | +12.1% | 3.18 to 35.9 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.304 | 0.322 | +5.9% | -0.0158 to 0.0516 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 54.3 |  | 48.1 to 60.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 25.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
