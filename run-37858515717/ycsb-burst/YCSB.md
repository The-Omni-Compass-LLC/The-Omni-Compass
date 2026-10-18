# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,847 | 2,846 | -0.0% | -9.65 to 8.17 | no difference beyond the noise |
| throughput (operations a second) | 2,857 | 2,856 | -0.0% | -9.19 to 7.78 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.453 | 0.454 | +0.1% | -0.00907 to 0.00974 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.674 | 0.669 | -0.8% | -0.0452 to 0.0345 | no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.245 | +1.4% | -0.00525 to 0.0118 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 397 | -22.4% | -116 to -113 | better |
| bytes in the cache, mean (MB) | 395 | 310 | -21.5% | -91.8 to -78.4 | better |
| pages read into the cache (misses) | 178,096 | 216,574 | +21.6% | 22,958 to 53,997 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.224 | +3.6% | -0.066 to 0.0815 | no difference beyond the noise |
| host CPU-seconds | 98.4 | 103 | +4.3% | -37.5 to 46 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.292 | +4.3% | -0.107 to 0.131 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
