# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,767 | 5,769 | +0.0% | -8.94 to 12.9 | no difference beyond the noise |
| throughput (operations a second) | 5,781 | 5,781 | +0.0% | -12.8 to 13.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.255 | 0.259 | +1.4% | -0.00637 to 0.0137 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.435 | +0.4% | -0.02 to 0.0234 | no difference beyond the noise |
| latency, mean (ms) | 0.118 | 0.117 | -0.7% | -0.00609 to 0.00455 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -63.8 to -63.8 | better |
| bytes in the cache, mean (MB) | 415 | 370 | -11.0% | -47.9 to -43.5 | better |
| pages read into the cache (misses) | 465,847 | 531,465 | +14.1% | 38,965 to 92,271 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.161 | -6.3% | -0.0563 to 0.0346 | no difference beyond the noise |
| host CPU-seconds | 210 | 194 | -7.8% | -82.4 to 49.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.109 | -7.9% | -0.0466 to 0.0279 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
