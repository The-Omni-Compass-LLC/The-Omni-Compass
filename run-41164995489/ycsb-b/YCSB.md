# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,922 | 2,921 | -0.0% | -1.84 to 0.646 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,924 | 2,924 | -0.0% | -2.35 to 0.931 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.198 | +0.5% | -0.0189 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.388 | +0.4% | -0.0436 to 0.047 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.103 | -1.3% | -0.00497 to 0.00228 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 835 | +63.1% | -106 to 752 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 666 | +58.4% | -86.6 to 578 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 724,920 | 463,477 | -36.1% | -472,958 to -49,928 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.123 | +5.9% | -0.0348 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 223 | +7.1% | -71.2 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.156 | 0.167 | +7.1% | -0.0533 to 0.0754 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 99 | 95.8 | -3.3% | -7.39 to 0.872 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 97 | 93.1 | -3.9% | -8.1 to 0.444 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.07 | 2.64 | +27.7% | 0.401 to 0.745 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 208 | 223 | +7.1% | -71.2 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
