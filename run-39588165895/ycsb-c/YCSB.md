# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,936 | -0.1% | -4.55 to -0.379 | LOSS |
| throughput (operations a second) | 2,940 | 2,938 | -0.1% | -4.55 to -0.383 | LOSS |
| latency, 95th percentile (ms) | 0.098 | 0.0983 | +0.3% | -0.01 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.299 | 0.301 | +0.7% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0597 | 0.0591 | -0.9% | -0.0016 to 0.000532 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -24.4 to 6.92 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 412 | -1.7% | -30.6 to 16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,267 | 674,432 | -1.4% | -104,010 to 84,340 | shown, not judged |
| host CPU busy (share of the run) | 0.083 | 0.0674 | -18.8% | -0.0775 to 0.0464 | EVEN, no difference beyond the noise |
| host CPU-seconds | 151 | 121 | -19.9% | -150 to 89.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.113 | 0.0902 | -19.9% | -0.112 to 0.0668 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
