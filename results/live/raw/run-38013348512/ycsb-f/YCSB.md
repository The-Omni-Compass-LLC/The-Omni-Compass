# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,774 | 5,769 | -0.1% | -17.2 to 5.84 | no difference beyond the noise |
| throughput (operations a second) | 5,788 | 5,784 | -0.1% | -20.7 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.2% | -0.00651 to 0.00784 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.5 | 0.502 | +0.5% | -0.0122 to 0.0169 | no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.19 | +0.8% | -0.00844 to 0.0115 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 443 | -13.4% | -81.1 to -56.1 | better |
| bytes in the cache, mean (MB) | 418 | 365 | -12.7% | -62.7 to -43.7 | better |
| pages read into the cache (misses) | 699,679 | 787,955 | +12.6% | 62,986 to 113,566 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.245 | +2.6% | -0.0347 to 0.047 | no difference beyond the noise |
| host CPU-seconds | 433 | 445 | +2.9% | -80.1 to 105 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.167 | +2.9% | -0.0301 to 0.0396 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
