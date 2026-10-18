# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,199 | +1.3% | -16.6 to 48.4 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0118 to 0.00418 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.8 | +1.4% | -0.0102 to 0.0318 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00703 to 0.00715 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.1% | -0.0148 to 0.0232 | no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -4.4% | -0.181 to 0.0783 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.4 | +5.4% | -3.64 to 10.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 64.2 | +5.0% | -3.28 to 9.39 | no difference beyond the noise |
| keys evicted | 138,126 | 132,219 | -4.3% | -20,957 to 9,143 | shown, not judged |
| host CPU busy (share of the run) | 0.0567 | 0.0528 | -6.9% | -0.018 to 0.0102 | no difference beyond the noise |
| host CPU-seconds | 100 | 92.8 | -7.4% | -33.4 to 18.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.188 | 0.172 | -8.5% | -0.0671 to 0.035 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | -2.82 to 48.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
