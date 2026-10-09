# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,611 | 2,737 | +4.8% | -373 to 625 | no difference beyond the noise |
| throughput (operations a second) | 2,625 | 2,747 | +4.6% | -365 to 609 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.346 | -0.2% | -0.0321 to 0.0308 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.629 | 0.549 | -12.7% | -0.328 to 0.168 | no difference beyond the noise |
| latency, mean (ms) | 0.252 | 0.231 | -8.2% | -0.0902 to 0.0487 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 404 | -21.0% | -123 to -91.6 | better |
| bytes in the cache, mean (MB) | 387 | 305 | -21.2% | -112 to -52.1 | better |
| pages read into the cache (misses) | 178,538 | 200,667 | +12.4% | -46,169 to 90,427 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.183 | +7.0% | -0.0846 to 0.109 | no difference beyond the noise |
| host CPU-seconds | 83.7 | 89.7 | +7.2% | -49.2 to 61.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.268 | +3.0% | -0.127 to 0.143 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
