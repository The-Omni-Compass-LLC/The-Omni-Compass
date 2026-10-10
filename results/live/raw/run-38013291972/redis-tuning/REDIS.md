# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.5% | -24.2 to 36.1 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0112 to 0.0156 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.793 | +0.5% | -0.0162 to 0.0242 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.00954 to 0.00284 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.00845 to 0.0161 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.5% | -0.128 to 0.0873 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -5.51 to 7.42 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -5.17 to 7.24 | no difference beyond the noise |
| keys evicted | 138,116 | 137,044 | -0.8% | -14,660 to 12,517 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.117 | -9.5% | -0.0473 to 0.0227 | no difference beyond the noise |
| host CPU-seconds | 217 | 194 | -10.8% | -89.5 to 42.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.408 | 0.362 | -11.2% | -0.178 to 0.0867 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 10.9 to 34.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
