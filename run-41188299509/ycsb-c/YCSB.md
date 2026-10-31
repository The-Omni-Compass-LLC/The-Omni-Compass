# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,909 | +0.1% | -17.4 to 25.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,913 | +0.1% | -17.7 to 24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.194 | 0.188 | -3.3% | -0.0178 to 0.00514 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.378 | 0.37 | -2.1% | -0.0487 to 0.0327 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.15 | 0.143 | -4.8% | -0.0282 to 0.0137 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 870 | +69.9% | -662 to 1,378 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 693 | +65.8% | -521 to 1,071 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 725,012 | 423,294 | -41.6% | -1,041,857 to 438,421 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.149 | -6.9% | -0.0561 to 0.0341 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 268 | -7.7% | -120 to 75.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.201 | -7.7% | -0.09 to 0.0563 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -4.45 to 10.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 143 | 136 | -4.4% | -23.6 to 11 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 141 | 134 | -4.8% | -24.2 to 10.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.55 | +24.7% | 0.396 to 0.616 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 291 | 268 | -7.7% | -120 to 75.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
