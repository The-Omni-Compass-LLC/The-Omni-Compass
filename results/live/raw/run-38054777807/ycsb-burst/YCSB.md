# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,889 | -0.0% | -4 to 1.55 | no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,895 | -0.0% | -3.8 to 1.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.423 | 0.43 | +1.7% | 0.00203 to 0.012 | **WORSE** |
| latency, 99th percentile (ms) | 0.559 | 0.565 | +1.2% | 0.000929 to 0.0124 | **WORSE** |
| latency, mean (ms) | 0.219 | 0.223 | +1.4% | -0.00358 to 0.00991 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 452 | -11.7% | -60.6 to -59.6 | better |
| bytes in the cache, mean (MB) | 408 | 355 | -12.9% | -61 to -44.3 | better |
| pages read into the cache (misses) | 275,598 | 299,411 | +8.6% | -27,500 to 75,126 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.172 | -5.5% | -0.0693 to 0.0494 | no difference beyond the noise |
| host CPU-seconds | 125 | 116 | -7.2% | -55.8 to 37.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.218 | -7.1% | -0.105 to 0.0714 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
