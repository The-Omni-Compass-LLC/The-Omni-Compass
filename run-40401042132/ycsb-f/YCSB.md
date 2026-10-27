# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,496 | 5,508 | +0.2% | -84.9 to 110 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,523 | 5,535 | +0.2% | -83.2 to 108 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.488 | 0.489 | +0.2% | -0.0193 to 0.0213 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.786 | 0.784 | -0.3% | -0.044 to 0.0386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.258 | -0.2% | -0.0163 to 0.0154 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 550 | +7.5% | -117 to 193 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 413 | 442 | +7.2% | -89.2 to 148 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 452,928 | 426,075 | -5.9% | -139,620 to 85,913 | shown, not judged |
| host CPU busy (share of the run) | 0.355 | 0.358 | +0.6% | -0.0297 to 0.0342 | EVEN, no difference beyond the noise |
| host CPU-seconds | 433 | 437 | +0.7% | -46.2 to 52.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.253 | +0.5% | -0.0316 to 0.0341 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9 |  | 4.7 to 13.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 230 | 232 | +0.8% | -8.99 to 12.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 227 | 229 | +0.6% | -9.44 to 12.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.96 | 3.41 | +15.2% | 0.0617 to 0.838 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 433 | 437 | +0.7% | -46.2 to 52.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
