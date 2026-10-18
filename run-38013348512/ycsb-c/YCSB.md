# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,917 | -0.0% | -5.75 to 4.74 | no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,920 | -0.0% | -4.62 to 3.95 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.233 | 0.231 | -1.0% | -0.0095 to 0.00484 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.38 | -0.8% | -0.00797 to 0.00197 | no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.162 | +5.2% | -0.0152 to 0.0314 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -109 to 64.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 400 | -4.8% | -86 to 46.1 | no difference beyond the noise |
| pages read into the cache (misses) | 696,621 | 722,119 | +3.7% | -105,183 to 156,180 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.156 | +12.1% | -0.0663 to 0.1 | no difference beyond the noise |
| host CPU-seconds | 247 | 283 | +14.4% | -137 to 209 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.185 | 0.212 | +14.3% | -0.103 to 0.156 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
