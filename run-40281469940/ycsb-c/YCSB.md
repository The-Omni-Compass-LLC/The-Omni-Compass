# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | +0.0% | -1.31 to 1.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -1.2 to 0.978 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.306 | -0.9% | -0.0107 to 0.00532 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.571 | 0.566 | -0.9% | -0.0205 to 0.0105 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.194 | -0.6% | -0.0116 to 0.00914 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.6 to 0.324 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.3% | -8.69 to 6.56 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 651,796 | 663,393 | +1.8% | -82,164 to 105,356 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.181 | -3.1% | -0.0456 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 325 | 314 | -3.6% | -93.1 to 69.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.244 | 0.236 | -3.6% | -0.0701 to 0.0527 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | -0.838 to 9.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 189 | +0.2% | -14.9 to 15.7 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 186 | -0.1% | -15.4 to 15.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.12 | +22.9% | 0.479 to 0.685 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 325 | 314 | -3.6% | -93.1 to 69.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
