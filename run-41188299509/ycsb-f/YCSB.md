# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,781 | 5,789 | +0.1% | -0.0705 to 15.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,795 | 5,802 | +0.1% | 0.731 to 14.3 | GAIN |
| latency, 95th percentile (ms) | 0.274 | 0.261 | -4.7% | -0.0304 to 0.00439 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.511 | 0.5 | -2.0% | -0.0394 to 0.0188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.133 | -5.2% | -0.0112 to -0.00354 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.9% | 154 to 367 | power given |
| bytes in the cache, mean (MB) | 417 | 615 | +47.5% | 112 to 284 | power given |
| pages read into the cache (misses) | 680,585 | 440,691 | -35.2% | -298,018 to -181,772 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.187 | -9.4% | -0.0526 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 376 | 337 | -10.2% | -110 to 33.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.141 | 0.126 | -10.3% | -0.0412 to 0.0123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 188 | -5.8% | -16.4 to -6.69 | GAIN |
| the server's own CPU-seconds (mongod) | 196 | 184 | -6.1% | -16.8 to -7.14 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.56 | 3.94 | +10.9% | 0.31 to 0.462 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 376 | 337 | -10.2% | -110 to 33.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
