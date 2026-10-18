# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,726 | 2,757 | +1.1% | -33.4 to 94.5 | no difference beyond the noise |
| throughput (operations a second) | 2,735 | 2,765 | +1.1% | -32.6 to 93.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.312 | +1.4% | -0.00192 to 0.0106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.48 | +0.5% | -0.0191 to 0.0238 | no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.235 | -2.6% | -0.0284 to 0.0157 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 377 | -26.5% | -318 to 46.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 412 | 310 | -24.9% | -253 to 47.8 | no difference beyond the noise |
| pages read into the cache (misses) | 479,449 | 586,126 | +22.2% | -9,698 to 223,053 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.181 | -0.9% | -0.0508 to 0.0475 | no difference beyond the noise |
| host CPU-seconds | 225 | 221 | -1.8% | -74 to 65.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.26 | -2.8% | -0.0856 to 0.0707 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
