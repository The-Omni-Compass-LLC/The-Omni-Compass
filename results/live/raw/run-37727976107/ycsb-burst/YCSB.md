# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,849 | 2,846 | -0.1% | -10.2 to 4.18 | no difference beyond the noise |
| throughput (operations a second) | 2,859 | 2,856 | -0.1% | -10.1 to 4.52 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.449 | 0.456 | +1.6% | -0.00438 to 0.0184 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.672 | 0.682 | +1.5% | -0.018 to 0.038 | no difference beyond the noise |
| latency, mean (ms) | 0.244 | 0.25 | +2.7% | 0.0019 to 0.0115 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 298 | -41.8% | -365 to -63.2 | better |
| bytes in the cache, mean (MB) | 397 | 238 | -40.0% | -282 to -36 | better |
| pages read into the cache (misses) | 176,149 | 264,188 | +50.0% | 22,857 to 153,222 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.218 | +4.8% | -0.0857 to 0.106 | no difference beyond the noise |
| host CPU-seconds | 93.8 | 98.6 | +5.1% | -49.2 to 58.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.28 | +5.1% | -0.14 to 0.167 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
