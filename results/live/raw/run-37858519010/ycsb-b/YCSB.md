# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,907 | +0.0% | -10.5 to 12.8 | no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | -0.0% | -7.7 to 7.52 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.277 | 0.273 | -1.3% | -0.00992 to 0.00259 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.447 | 0.424 | -5.2% | -0.0581 to 0.0115 | no difference beyond the noise |
| latency, mean (ms) | 0.102 | 0.0995 | -2.4% | -0.00908 to 0.00416 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -231 to -55.6 | better |
| bytes in the cache, mean (MB) | 416 | 303 | -27.3% | -184 to -43.6 | better |
| pages read into the cache (misses) | 480,944 | 593,742 | +23.5% | -13,086 to 238,681 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.121 | -2.4% | -0.0684 to 0.0624 | no difference beyond the noise |
| host CPU-seconds | 150 | 146 | -2.5% | -93.9 to 86.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.169 | 0.164 | -2.5% | -0.105 to 0.0969 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
