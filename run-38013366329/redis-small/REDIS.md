# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 922 | -0.4% | -12.8 to 5.35 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00854 to 0.00271 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.615 | -0.4% | -0.00846 to 0.00356 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.54 | 5.54 | +0.0% | -0.00711 to 0.00958 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.000539 to 0.00811 | no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.15 | +0.7% | -0.0156 to 0.0445 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.8 | -0.3% | -1.54 to 1.1 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.3 | -0.7% | -1.59 to 0.761 | no difference beyond the noise |
| keys evicted | 243,069 | 246,886 | +1.6% | -4,817 to 12,451 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.115 | +3.0% | -0.00573 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 200 | 206 | +3.2% | -12.5 to 25.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.48 | 0.497 | +3.7% | -0.0271 to 0.0622 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 4.76 to 38.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
