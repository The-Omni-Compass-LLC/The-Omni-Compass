# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,846 | 5,839 | -0.1% | -17.8 to 3.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,854 | 5,848 | -0.1% | -16.8 to 4.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.158 | 0.161 | +1.9% | -0.00942 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.362 | +3.0% | -0.00863 to 0.03 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.082 | 0.0831 | +1.4% | -0.00185 to 0.00407 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 667 | +30.2% | -178 to 487 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 537 | +28.1% | -136 to 372 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,105 | 533,930 | -23.7% | -517,270 to 184,921 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.124 | +5.5% | -0.0885 to 0.101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 223 | +5.2% | -183 to 205 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0792 | 0.0833 | +5.3% | -0.068 to 0.0764 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 119 | 122 | +1.8% | -6.37 to 10.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 118 | +1.3% | -6.54 to 9.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.14 | +23.0% | 0.0684 to 1.11 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 212 | 223 | +5.2% | -183 to 205 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
