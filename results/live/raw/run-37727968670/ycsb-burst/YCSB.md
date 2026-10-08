# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,852 | 2,849 | -0.1% | -8.62 to 3.02 | no difference beyond the noise |
| throughput (operations a second) | 2,861 | 2,859 | -0.1% | -6.87 to 2.75 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.457 | 0.458 | +0.1% | -0.0121 to 0.0134 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.669 | 0.67 | +0.1% | -0.0446 to 0.0466 | no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.246 | +2.2% | 0.00195 to 0.0087 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 263 | -48.7% | -249 to -249 | better |
| bytes in the cache, mean (MB) | 399 | 210 | -47.2% | -203 to -174 | better |
| pages read into the cache (misses) | 175,012 | 277,156 | +58.4% | 88,846 to 115,442 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.196 | -3.5% | -0.0585 to 0.0444 | no difference beyond the noise |
| host CPU-seconds | 91.3 | 87 | -4.7% | -32.4 to 23.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.247 | -4.7% | -0.0917 to 0.0674 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
