# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,892 | -0.0% | -4.88 to 4.83 | no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,896 | +0.0% | -3.91 to 4.05 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.356 | 0.35 | -1.7% | -0.0254 to 0.0134 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.519 | 0.519 | +0.1% | -0.0336 to 0.0342 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.204 | -1.1% | -0.00823 to 0.00376 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -63.5 to -60.7 | better |
| bytes in the cache, mean (MB) | 419 | 367 | -12.5% | -58.6 to -46.2 | better |
| pages read into the cache (misses) | 725,227 | 747,456 | +3.1% | -16,221 to 60,679 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.174 | -9.4% | -0.0748 to 0.0387 | no difference beyond the noise |
| host CPU-seconds | 328 | 292 | -11.0% | -153 to 80.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.247 | 0.22 | -11.0% | -0.115 to 0.0603 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
