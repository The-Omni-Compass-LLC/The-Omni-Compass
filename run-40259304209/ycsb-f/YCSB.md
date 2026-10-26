# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,677 | 5,686 | +0.1% | -17.9 to 34.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,703 | +0.2% | -18.3 to 35.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.428 | -0.7% | -0.0129 to 0.00694 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.656 | 0.657 | +0.2% | -0.0119 to 0.0139 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.244 | -0.9% | -0.00979 to 0.00555 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -36.2 to 92.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 439 | +5.4% | -28.7 to 73.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,148 | 654,260 | -3.7% | -108,492 to 58,716 | shown, not judged |
| host CPU busy (share of the run) | 0.325 | 0.321 | -1.4% | -0.0385 to 0.0294 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 577 | -1.9% | -96.3 to 73.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.217 | -2.0% | -0.0373 to 0.0283 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 6.03 to 16 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 354 | 352 | -0.7% | -14.4 to 9.41 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 350 | 347 | -0.9% | -14.8 to 8.68 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.35 | 4.91 | +12.9% | 0.0835 to 1.04 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 577 | -1.9% | -96.3 to 73.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
