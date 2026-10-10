# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -2.66 to 1.29 | no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% | -2.54 to 1.34 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.218 | 0.219 | +0.5% | -0.0443 to 0.0463 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.357 | +1.5% | -0.0511 to 0.0618 | no difference beyond the noise |
| latency, mean (ms) | 0.083 | 0.0839 | +1.1% | -0.00254 to 0.0044 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 445 | -13.1% | -80.1 to -54.1 | better |
| bytes in the cache, mean (MB) | 420 | 366 | -12.8% | -79.2 to -28.5 | better |
| pages read into the cache (misses) | 694,101 | 794,493 | +14.5% | -47,216 to 248,000 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.125 | +10.8% | -0.0171 to 0.0414 | no difference beyond the noise |
| host CPU-seconds | 207 | 232 | +12.4% | -37.4 to 88.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.173 | +12.4% | -0.028 to 0.0661 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
