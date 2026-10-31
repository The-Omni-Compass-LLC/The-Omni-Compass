# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,879 | +0.0% | -3.06 to 4.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -2.56 to 3.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.415 | 0.416 | +0.4% | -0.00774 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.586 | 0.587 | +0.2% | -0.0138 to 0.0165 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.217 | +0.8% | -0.00548 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 401 | 402 | +0.2% | -12.7 to 14.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 257,543 | 276,939 | +7.5% | -4,156 to 42,947 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.19 | -10.7% | -0.142 to 0.0967 | EVEN, no difference beyond the noise |
| host CPU-seconds | 151 | 131 | -13.3% | -124 to 83.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.284 | 0.246 | -13.3% | -0.233 to 0.157 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.1 | 83.1 | +1.2% | -1.78 to 3.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81 | 81.8 | +0.9% | -1.96 to 3.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.03 | 1.27 | +23.2% | 0.17 to 0.308 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 151 | 131 | -13.3% | -124 to 83.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
