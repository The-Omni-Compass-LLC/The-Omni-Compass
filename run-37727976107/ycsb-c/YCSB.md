# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,912 | -0.1% | -6.86 to 1.17 | no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,915 | -0.1% | -5.53 to -0.166 | **WORSE** |
| latency, 95th percentile (ms) | 0.254 | 0.256 | +1.1% | -0.00113 to 0.00646 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.392 | +0.9% | -0.01 to 0.0173 | no difference beyond the noise |
| latency, mean (ms) | 0.0843 | 0.088 | +4.4% | -0.00241 to 0.00984 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 258 | -49.6% | -254 to -253 | better |
| bytes in the cache, mean (MB) | 418 | 217 | -48.1% | -210 to -192 | better |
| pages read into the cache (misses) | 472,121 | 721,837 | +52.9% | 141,280 to 358,151 | shown, not judged |
| host CPU busy (share of the run) | 0.0958 | 0.106 | +11.0% | -0.0172 to 0.0383 | no difference beyond the noise |
| host CPU-seconds | 115 | 128 | +11.6% | -22.7 to 49.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.129 | 0.144 | +11.7% | -0.0256 to 0.0557 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
