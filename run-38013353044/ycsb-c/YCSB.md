# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,908 | -0.1% | -17.8 to 14.6 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -16.7 to 13.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.25 | +1.2% | -0.0121 to 0.0181 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.397 | +0.4% | -0.0173 to 0.0206 | no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.18 | -1.0% | -0.0298 to 0.0264 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -81.1 to -48.5 | better |
| bytes in the cache, mean (MB) | 416 | 365 | -12.2% | -76.1 to -25.6 | better |
| pages read into the cache (misses) | 695,640 | 792,270 | +13.9% | -35,179 to 228,441 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.146 | +0.1% | -0.0815 to 0.0818 | no difference beyond the noise |
| host CPU-seconds | 264 | 262 | -0.6% | -175 to 172 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.196 | -0.6% | -0.132 to 0.129 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
