# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,844 | -1.1% | -290 to 224 | no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,854 | -1.2% | -287 to 220 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.275 | 0.281 | +2.1% | -0.00868 to 0.02 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.446 | 0.456 | +2.2% | -0.0313 to 0.0513 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.209 | +1.4% | -0.0601 to 0.0658 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 465 | -9.3% | -126 to 31.4 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 379 | -8.6% | -88.3 to 17.2 | no difference beyond the noise |
| pages read into the cache (misses) | 675,083 | 719,478 | +6.6% | -80,923 to 169,713 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.196 | -2.9% | -0.0624 to 0.0508 | no difference beyond the noise |
| host CPU-seconds | 367 | 353 | -3.9% | -138 to 109 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.271 | -2.7% | -0.0792 to 0.0642 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
