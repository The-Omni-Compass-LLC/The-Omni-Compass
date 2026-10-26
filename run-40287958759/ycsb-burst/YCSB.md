# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,884 | +0.0% | -1.77 to 3.25 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,890 | +0.0% | -1.82 to 3.59 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.422 | +0.0% | -0.0138 to 0.0138 | EVEN, the same |
| latency, 99th percentile (ms) | 0.565 | 0.566 | +0.2% | -0.0176 to 0.0203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.212 | -0.2% | -0.00534 to 0.00446 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.5% | -19.9 to 45.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 414 | +3.2% | -26.8 to 52.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,079 | 267,174 | +0.0% | -15,690 to 15,880 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.165 | -17.0% | -0.113 to 0.0457 | EVEN, no difference beyond the noise |
| host CPU-seconds | 139 | 112 | -19.6% | -94 to 39.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.211 | -19.6% | -0.177 to 0.0737 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80 | 80.5 | +0.6% | -1.62 to 2.64 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79 | 79.4 | +0.4% | -1.82 to 2.46 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.993 | 1.18 | +19.1% | 0.152 to 0.227 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 112 | -19.6% | -93.9 to 39.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
