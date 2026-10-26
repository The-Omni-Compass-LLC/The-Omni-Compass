# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -2.97 to 2.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.55 to 2.71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.336 | +2.3% | -0.022 to 0.0373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.54 | +2.4% | -0.0235 to 0.0489 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.2 | +1.4% | -0.00678 to 0.0124 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -2.12 to -0.928 | GAIN |
| bytes in the cache, mean (MB) | 417 | 419 | +0.5% | -4.83 to 8.65 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,857 | 734,771 | +5.6% | -38,770 to 116,596 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.206 | -1.6% | -0.0815 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 363 | -2.3% | -181 to 164 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.273 | -2.3% | -0.136 to 0.123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 203 | +2.0% | -7.05 to 15.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 196 | 200 | +1.8% | -7.72 to 14.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.1 | +23.8% | 0.417 to 0.777 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 371 | 363 | -2.3% | -181 to 164 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
