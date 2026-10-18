# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,546 | 5,536 | -0.2% | -89 to 69.3 | no difference beyond the noise |
| throughput (operations a second) | 5,566 | 5,555 | -0.2% | -87.8 to 66 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.458 | 0.462 | +0.9% | -0.0115 to 0.0195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.698 | 0.695 | -0.4% | -0.0325 to 0.0272 | no difference beyond the noise |
| latency, mean (ms) | 0.264 | 0.266 | +0.5% | -0.0076 to 0.0105 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -231 to -55.1 | better |
| bytes in the cache, mean (MB) | 415 | 299 | -28.0% | -187 to -45 | better |
| pages read into the cache (misses) | 456,254 | 617,406 | +35.3% | 40,550 to 281,754 | shown, not judged |
| host CPU busy (share of the run) | 0.316 | 0.32 | +1.3% | -0.00761 to 0.0156 | no difference beyond the noise |
| host CPU-seconds | 361 | 364 | +0.9% | -15.5 to 21.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.211 | +0.9% | -0.00575 to 0.00958 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
