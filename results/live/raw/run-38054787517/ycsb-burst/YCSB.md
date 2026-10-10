# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,921 | 2,920 | -0.0% | -2.16 to -0.308 | **WORSE** |
| throughput (operations a second) | 2,926 | 2,925 | -0.0% | -2.7 to 0.181 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.388 | 0.393 | +1.4% | -0.00471 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.547 | 0.553 | +1.2% | -0.0245 to 0.0372 | no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.156 | +0.8% | -0.000949 to 0.00333 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 461 | -10.0% | -83.6 to -19 | better |
| bytes in the cache, mean (MB) | 404 | 364 | -10.0% | -56.9 to -23.7 | better |
| pages read into the cache (misses) | 269,798 | 281,893 | +4.5% | -79,042 to 103,233 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.157 | -2.1% | -0.188 to 0.181 | no difference beyond the noise |
| host CPU-seconds | 120 | 116 | -3.0% | -163 to 156 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.218 | -3.0% | -0.305 to 0.292 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.97 to 7.97 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
