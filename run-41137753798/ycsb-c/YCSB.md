# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -12.7 to 8.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -12.1 to 7.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.298 | 0.305 | +2.6% | -0.0154 to 0.0308 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.593 | 0.598 | +1.0% | -0.034 to 0.0453 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.19 | +1.1% | -0.00536 to 0.00964 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | -0.1% | -2.96 to 1.35 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,689 | 61,613 | -0.1% | -237 to 85.3 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.193 | +6.8% | -0.00847 to 0.0332 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 338 | +7.9% | -17.9 to 67.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.255 | +7.9% | -0.0134 to 0.0508 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 178 | +1.8% | -7.21 to 13.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 175 | +1.7% | -7.1 to 13.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 2.73 | +9.4% | -0.172 to 0.64 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 338 | +7.9% | -17.9 to 67.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
