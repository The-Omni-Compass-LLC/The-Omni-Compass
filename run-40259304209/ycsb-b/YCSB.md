# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -3.19 to 2.43 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | -0.0% | -3.69 to 2.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.5% | -0.00654 to 0.0159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.488 | 0.494 | +1.2% | -0.00891 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.195 | +0.7% | -0.00356 to 0.00624 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -1.91 to -1.51 | GAIN |
| bytes in the cache, mean (MB) | 419 | 420 | +0.2% | -2.41 to 4.18 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 721,546 | 741,544 | +2.8% | -138,277 to 178,273 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.205 | -2.5% | -0.037 to 0.0267 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 362 | -3.2% | -79.5 to 55.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.272 | -3.2% | -0.0596 to 0.0417 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 197 | 199 | +1.3% | -3.7 to 9.01 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 194 | 196 | +1.1% | -4.23 to 8.45 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.04 | +21.7% | 0.432 to 0.651 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374 | 362 | -3.2% | -79.5 to 55.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
