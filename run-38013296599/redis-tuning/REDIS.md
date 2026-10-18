# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,203 | +1.5% | 8.15 to 28.5 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00211 to 0.00351 | same |
| cache hit rate | 0.79 | 0.802 | +1.5% | 0.00544 to 0.019 | better |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0616 to 0.0367 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.65 | -0.0% | -0.029 to 0.0252 | no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.16 | -5.3% | -0.0887 to -0.0415 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.1 | +4.8% | 0.311 to 5.88 | **WORSE** |
| memory used, mean (MB) | 61.2 | 64.3 | +5.1% | 0.29 to 5.94 | **WORSE** |
| keys evicted | 137,942 | 131,053 | -5.0% | -10,711 to -3,067 | shown, not judged |
| host CPU busy (share of the run) | 0.0864 | 0.0926 | +7.2% | -0.0161 to 0.0285 | no difference beyond the noise |
| host CPU-seconds | 152 | 164 | +8.2% | -31.4 to 56.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.285 | 0.304 | +6.5% | -0.0641 to 0.101 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 17.9 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
