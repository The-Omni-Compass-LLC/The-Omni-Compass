# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,841 | 2,837 | -0.1% | -11.1 to 2.93 | no difference beyond the noise |
| throughput (operations a second) | 2,852 | 2,848 | -0.2% | -11.8 to 2.73 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.426 | +2.0% | -0.0106 to 0.0273 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.631 | +1.5% | -0.0245 to 0.0432 | no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.236 | +2.2% | -0.0089 to 0.0192 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 409 | -20.0% | -189 to -16.1 | better |
| bytes in the cache, mean (MB) | 415 | 335 | -19.3% | -150 to -9.92 | better |
| pages read into the cache (misses) | 458,125 | 569,667 | +24.3% | 32,940 to 190,144 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.27 | +7.0% | -0.0197 to 0.055 | no difference beyond the noise |
| host CPU-seconds | 287 | 313 | +8.8% | -30 to 80.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.328 | 0.357 | +8.9% | -0.0337 to 0.0918 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
