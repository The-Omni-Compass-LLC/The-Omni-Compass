# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -5.39 to 4.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -4.54 to 3.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.15 | -1.1% | -0.0415 to 0.0382 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.345 | 0.345 | -0.1% | -0.044 to 0.0433 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0801 | 0.079 | -1.3% | -0.00888 to 0.00684 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.31 to -1.52 | GAIN |
| bytes in the cache, mean (MB) | 419 | 419 | -0.0% | -3.56 to 3.31 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 694,123 | 702,215 | +1.2% | -29,225 to 45,410 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.119 | -2.3% | -0.124 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 218 | -3.0% | -259 to 245 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.168 | 0.163 | -3.0% | -0.193 to 0.183 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 106 | 106 | +0.1% | -6.34 to 6.54 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 104 | 104 | -0.3% | -6.64 to 5.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.69 | 2.14 | +26.6% | 0.227 to 0.672 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 224 | 218 | -3.0% | -259 to 245 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
