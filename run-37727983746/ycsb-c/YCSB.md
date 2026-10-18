# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,861 | 2,861 | +0.0% | -17.9 to 18.7 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,865 | +0.0% | -17.1 to 17.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.392 | 0.391 | -0.2% | -0.0196 to 0.0183 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.503 | -0.3% | -0.0451 to 0.0417 | no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.211 | +3.2% | -0.0097 to 0.0226 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 259 | -49.5% | -253 to -253 | better |
| bytes in the cache, mean (MB) | 415 | 216 | -48.0% | -209 to -189 | better |
| pages read into the cache (misses) | 456,407 | 719,563 | +57.7% | 210,652 to 315,661 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.215 | +10.7% | -0.00527 to 0.0469 | no difference beyond the noise |
| host CPU-seconds | 219 | 247 | +12.8% | -8.16 to 64.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.28 | +12.8% | -0.00898 to 0.0725 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
