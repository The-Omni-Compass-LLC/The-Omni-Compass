# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,901 | -0.0% | -2.13 to 0.598 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,905 | -0.0% | -1.46 to 0.228 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.289 | 0.291 | +0.6% | -0.00954 to 0.0129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.485 | 0.485 | +0.0% | -0.0361 to 0.0361 | EVEN, the same |
| latency, mean (ms) | 0.149 | 0.149 | -0.2% | -0.00347 to 0.00297 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,348 | -0.1% | -5.02 to 2.63 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,696 | 61,631 | -0.1% | -306 to 177 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.163 | -13.8% | -0.0683 to 0.016 | EVEN, no difference beyond the noise |
| host CPU-seconds | 353 | 294 | -16.5% | -152 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.265 | 0.221 | -16.5% | -0.114 to 0.0268 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 134 | 134 | -0.3% | -2.86 to 2.11 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 132 | 131 | -0.4% | -2.9 to 1.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.65 | +4.7% | 0.0261 to 0.21 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 353 | 294 | -16.5% | -152 to 35.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
