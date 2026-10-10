# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | -19.9 to 39.7 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000273 to 0.00699 | no difference beyond the noise |
| cache hit rate | 0.79 | 0.796 | +0.8% | -0.0131 to 0.0264 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0143 to 0.0076 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.0% | -0.0103 to 0.0131 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.5% | -0.146 to 0.0779 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | -4.12 to 6.67 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | -3.75 to 6.4 | no difference beyond the noise |
| keys evicted | 137,957 | 135,118 | -2.1% | -16,156 to 10,478 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.116 | -4.6% | -0.0586 to 0.0474 | no difference beyond the noise |
| host CPU-seconds | 204 | 193 | -5.2% | -112 to 91.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.359 | -6.1% | -0.205 to 0.159 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 12.3 to 31.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
