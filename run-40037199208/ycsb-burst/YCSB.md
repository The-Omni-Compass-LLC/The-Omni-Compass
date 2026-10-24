# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,938 | -0.0% | -2.2 to 0.335 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -2.01 to 0.321 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.251 | -0.1% | -0.0248 to 0.0242 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.396 | 0.391 | -1.4% | -0.0256 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0785 | 0.0774 | -1.4% | -0.00517 to 0.00293 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -19.9 to -1.81 | GAIN |
| bytes in the cache, mean (MB) | 406 | 400 | -1.5% | -23.8 to 11.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,661 | 269,322 | +1.8% | -19,403 to 28,724 | shown, not judged |
| host CPU busy (share of the run) | 0.0666 | 0.0753 | +13.0% | -0.0783 to 0.0957 | EVEN, no difference beyond the noise |
| host CPU-seconds | 47.3 | 54.2 | +14.5% | -59.7 to 73.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0884 | 0.101 | +14.5% | -0.111 to 0.137 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
