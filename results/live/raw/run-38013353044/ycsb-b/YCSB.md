# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.1% | -4.53 to 1.02 | no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -4.67 to 0.599 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.328 | +2.8% | -0.00729 to 0.0253 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.559 | 0.561 | +0.4% | -0.0154 to 0.0194 | no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.202 | +1.5% | -0.00856 to 0.0146 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.2% | -63.5 to -61.7 | better |
| bytes in the cache, mean (MB) | 419 | 368 | -12.0% | -53.7 to -47 | better |
| pages read into the cache (misses) | 717,723 | 751,917 | +4.8% | -113,495 to 181,883 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.166 | -7.8% | -0.134 to 0.105 | no difference beyond the noise |
| host CPU-seconds | 309 | 279 | -9.7% | -271 to 211 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.21 | -9.7% | -0.204 to 0.159 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
