# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,890 | -0.0% | -2.24 to 0.918 | no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,896 | -0.0% | -2.7 to 1.46 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.405 | 0.406 | +0.2% | -0.0104 to 0.0124 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.557 | 0.555 | -0.4% | -0.0158 to 0.0118 | no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | +0.2% | -0.00199 to 0.00268 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 463 | -9.5% | -95 to -2.28 | better |
| bytes in the cache, mean (MB) | 405 | 364 | -10.2% | -72 to -10.2 | better |
| pages read into the cache (misses) | 265,105 | 282,698 | +6.6% | -8,457 to 43,643 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.162 | -8.8% | -0.107 to 0.0752 | no difference beyond the noise |
| host CPU-seconds | 121 | 107 | -11.2% | -89.1 to 62 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.202 | -11.2% | -0.167 to 0.116 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
