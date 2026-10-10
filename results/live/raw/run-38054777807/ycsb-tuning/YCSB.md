# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,882 | -0.2% | -24.2 to 10.8 | no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,891 | -0.2% | -25.2 to 11.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.366 | 0.365 | -0.3% | -0.001 to -0.001 | better |
| latency, 99th percentile (ms) | 0.613 | 0.61 | -0.5% | -0.0168 to 0.0108 | no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.225 | +0.2% | -0.00202 to 0.00311 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.3% | -64.8 to -60.8 | better |
| bytes in the cache, mean (MB) | 417 | 369 | -11.7% | -50.6 to -46.9 | better |
| pages read into the cache (misses) | 677,075 | 759,667 | +12.2% | 56,298 to 108,886 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.239 | +3.6% | -0.0677 to 0.0841 | no difference beyond the noise |
| host CPU-seconds | 400 | 417 | +4.4% | -156 to 192 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.314 | +4.6% | -0.119 to 0.147 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
