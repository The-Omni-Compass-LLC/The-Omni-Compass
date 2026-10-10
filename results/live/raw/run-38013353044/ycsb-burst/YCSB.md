# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.0% | -2.29 to -0.211 | **WORSE** |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -1.52 to -1.07 | **WORSE** |
| latency, 95th percentile (ms) | 0.495 | 0.498 | +0.5% | -0.00392 to 0.00859 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.625 | 0.626 | +0.2% | -0.0033 to 0.0053 | no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.228 | +1.0% | 0.000899 to 0.00379 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 436 | -14.8% | -115 to -37 | better |
| bytes in the cache, mean (MB) | 402 | 341 | -15.2% | -97.2 to -25.1 | better |
| pages read into the cache (misses) | 266,113 | 286,450 | +7.6% | -30,281 to 70,955 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.161 | -9.5% | -0.187 to 0.153 | no difference beyond the noise |
| host CPU-seconds | 124 | 108 | -12.7% | -151 to 119 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.203 | -12.7% | -0.284 to 0.224 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
