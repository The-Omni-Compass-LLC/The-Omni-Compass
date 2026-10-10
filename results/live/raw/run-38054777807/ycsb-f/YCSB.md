# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,696 | 5,697 | +0.0% | -25.7 to 27 | no difference beyond the noise |
| throughput (operations a second) | 5,711 | 5,711 | +0.0% | -26.4 to 26.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.433 | -1.1% | -0.0212 to 0.0119 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.635 | 0.629 | -1.0% | -0.0188 to 0.00617 | no difference beyond the noise |
| latency, mean (ms) | 0.254 | 0.251 | -1.2% | -0.0134 to 0.00745 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -80.1 to -56 | better |
| bytes in the cache, mean (MB) | 417 | 364 | -12.8% | -59.7 to -47.3 | better |
| pages read into the cache (misses) | 677,539 | 785,502 | +15.9% | 76,489 to 139,436 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% | -0.0195 to 0.0171 | no difference beyond the noise |
| host CPU-seconds | 473 | 471 | -0.4% | -45.2 to 41.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.178 | -0.5% | -0.0181 to 0.0162 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
