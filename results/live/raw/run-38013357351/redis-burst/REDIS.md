# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.07 to 0.478 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0342 to 0.0227 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000674 to 0.000351 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.0144 to 0.0159 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.00896 to 0.0204 | no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.74 | +0.2% | -0.0041 to 0.0117 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.48 to -2.03 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% | -2.62 to -1.06 | better |
| keys evicted | 71,743 | 71,798 | +0.1% | -150 to 260 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.139 | +3.6% | -0.00899 to 0.0186 | no difference beyond the noise |
| host CPU-seconds | 90.2 | 93.8 | +4.0% | -6.78 to 14 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.484 | +4.0% | -0.035 to 0.0726 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
