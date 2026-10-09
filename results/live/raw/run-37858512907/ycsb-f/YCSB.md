# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,656 | 5,601 | -1.0% | -238 to 128 | no difference beyond the noise |
| throughput (operations a second) | 5,675 | 5,618 | -1.0% | -233 to 120 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.347 | +0.8% | -0.0101 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.546 | -0.8% | -0.0508 to 0.0415 | no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.214 | +1.7% | -0.00491 to 0.0121 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 328 | -35.9% | -186 to -182 | better |
| bytes in the cache, mean (MB) | 413 | 266 | -35.6% | -154 to -141 | better |
| pages read into the cache (misses) | 472,245 | 674,851 | +42.9% | 146,641 to 258,570 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.275 | +2.6% | -0.0278 to 0.0417 | no difference beyond the noise |
| host CPU-seconds | 326 | 337 | +3.4% | -52.3 to 74.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.194 | +4.4% | -0.022 to 0.0384 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
