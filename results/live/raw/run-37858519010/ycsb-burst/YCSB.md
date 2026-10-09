# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,859 | 2,860 | +0.0% | -4.91 to 6.96 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,865 | +0.0% | -4.13 to 6.12 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.402 | 0.403 | +0.2% | -0.0033 to 0.0053 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.566 | -0.3% | -0.0253 to 0.0219 | no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.227 | +1.1% | -0.00639 to 0.0113 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 378 | -26.2% | -215 to -52.6 | better |
| bytes in the cache, mean (MB) | 401 | 294 | -26.6% | -178 to -35.8 | better |
| pages read into the cache (misses) | 183,243 | 223,388 | +21.9% | 19,101 to 61,189 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.195 | -11.9% | -0.0781 to 0.0257 | no difference beyond the noise |
| host CPU-seconds | 103 | 87.5 | -15.0% | -45.4 to 14.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.292 | 0.248 | -15.0% | -0.129 to 0.0415 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
