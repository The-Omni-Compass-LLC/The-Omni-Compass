# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,688 | 5,678 | -0.2% | -61 to 41.3 | no difference beyond the noise |
| throughput (operations a second) | 5,705 | 5,696 | -0.2% | -60.6 to 41.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.439 | 0.443 | +0.9% | -0.0134 to 0.0214 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.664 | 0.673 | +1.3% | -0.0465 to 0.0638 | no difference beyond the noise |
| latency, mean (ms) | 0.255 | 0.257 | +0.9% | -0.008 to 0.0125 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.8% | -77.7 to -52.9 | better |
| bytes in the cache, mean (MB) | 417 | 365 | -12.4% | -63.2 to -40.7 | better |
| pages read into the cache (misses) | 679,207 | 773,228 | +13.8% | 80,320 to 107,722 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.2% | -0.00873 to 0.00964 | no difference beyond the noise |
| host CPU-seconds | 481 | 482 | +0.1% | -27.4 to 28.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.182 | 0.182 | +0.2% | -0.00849 to 0.00916 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
