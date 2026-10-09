# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | -0.0% | -3.13 to 2.48 | no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,907 | -0.0% | -2.98 to 0.267 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.276 | 0.279 | +1.1% | -0.00197 to 0.00797 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.447 | 0.445 | -0.3% | -0.0524 to 0.0497 | no difference beyond the noise |
| latency, mean (ms) | 0.101 | 0.103 | +2.1% | -0.00264 to 0.00676 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 328 | -35.9% | -184 to -184 | better |
| bytes in the cache, mean (MB) | 420 | 268 | -36.2% | -164 to -139 | better |
| pages read into the cache (misses) | 504,732 | 667,884 | +32.3% | 96,428 to 229,878 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.139 | +0.9% | -0.0808 to 0.0833 | no difference beyond the noise |
| host CPU-seconds | 169 | 170 | +0.5% | -115 to 117 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.19 | 0.191 | +0.5% | -0.129 to 0.131 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
