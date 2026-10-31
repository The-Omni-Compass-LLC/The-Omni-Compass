# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | +0.0% | -2.45 to 3.79 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,915 | +0.0% | -2.08 to 2.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.187 | 0.182 | -2.7% | -0.00997 to -3.13e-05 | GAIN |
| latency, 99th percentile (ms) | 0.352 | 0.348 | -1.2% | -0.0137 to 0.00507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.137 | 0.135 | -1.2% | -0.00564 to 0.00226 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.7% | -341 to 860 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 615 | +46.9% | -262 to 655 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 658,030 | 474,353 | -27.9% | -683,295 to 315,941 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.126 | -17.0% | -0.0616 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 220 | -19.1% | -127 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.165 | -19.1% | -0.0954 to 0.0175 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.3 to 6.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 138 | 135 | -2.5% | -11 to 4.02 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 136 | 132 | -2.9% | -11.6 to 3.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2 | 2.48 | +24.3% | 0.378 to 0.592 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 272 | 220 | -19.1% | -127 to 23.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
