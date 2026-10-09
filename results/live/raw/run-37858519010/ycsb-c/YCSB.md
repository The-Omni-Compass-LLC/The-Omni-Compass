# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,856 | -0.1% | -5.88 to 2.29 | no difference beyond the noise |
| throughput (operations a second) | 2,865 | 2,863 | -0.1% | -6.86 to 3.71 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.464 | 0.464 | -0.1% | -0.0032 to 0.00254 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.609 | 0.61 | +0.2% | -0.0121 to 0.0141 | no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.217 | +1.1% | -0.00321 to 0.00781 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -123 to -123 | better |
| bytes in the cache, mean (MB) | 412 | 320 | -22.3% | -100 to -83 | better |
| pages read into the cache (misses) | 478,884 | 615,567 | +28.5% | 7,299 to 266,068 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.195 | -4.3% | -0.0586 to 0.0408 | no difference beyond the noise |
| host CPU-seconds | 234 | 220 | -5.9% | -85.5 to 57.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.265 | 0.249 | -5.9% | -0.0969 to 0.0655 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
