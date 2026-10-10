# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,889 | -0.1% | -5.03 to 1.42 | no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -3.47 to 0.269 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.426 | +0.5% | -0.000484 to 0.00448 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.575 | 0.589 | +2.6% | 0.00293 to 0.0264 | **WORSE** |
| latency, mean (ms) | 0.219 | 0.219 | -0.1% | -0.00703 to 0.00668 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -76.4 to -52 | better |
| bytes in the cache, mean (MB) | 404 | 350 | -13.4% | -63.3 to -44.9 | better |
| pages read into the cache (misses) | 265,564 | 286,686 | +8.0% | -8,142 to 50,385 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.171 | -1.2% | -0.0548 to 0.0508 | no difference beyond the noise |
| host CPU-seconds | 117 | 116 | -1.2% | -44.8 to 41.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.217 | -1.2% | -0.0841 to 0.0788 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
