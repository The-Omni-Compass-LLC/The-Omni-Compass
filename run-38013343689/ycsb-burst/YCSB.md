# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,804 | 2,686 | -4.2% | -454 to 217 | no difference beyond the noise |
| throughput (operations a second) | 2,815 | 2,698 | -4.1% | -449 to 216 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.351 | +2.1% | -0.0103 to 0.025 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.529 | 0.572 | +8.2% | -0.0299 to 0.117 | no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.25 | +10.9% | -0.0337 to 0.0828 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 455 | -11.1% | -151 to 37.3 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 397 | 353 | -11.1% | -102 to 14.1 | no difference beyond the noise |
| pages read into the cache (misses) | 260,725 | 238,666 | -8.5% | -67,463 to 23,345 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.141 | +0.6% | -0.0927 to 0.0946 | no difference beyond the noise |
| host CPU-seconds | 101 | 102 | +1.4% | -76.6 to 79.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.207 | +5.8% | -0.119 to 0.141 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
