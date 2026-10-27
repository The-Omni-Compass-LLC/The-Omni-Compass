# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,852 | 2,851 | -0.0% | -3.39 to 1.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,858 | 2,857 | -0.0% | -3.07 to 2.01 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.392 | 0.393 | +0.2% | -0.00313 to 0.00446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.542 | 0.55 | +1.4% | -0.0113 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.2 | +0.3% | -0.00253 to 0.00358 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 529 | +3.3% | -61.9 to 95.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 431 | +3.4% | -53 to 81.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 479,768 | 463,252 | -3.4% | -129,751 to 96,718 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.209 | -0.2% | -0.02 to 0.019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 242 | -0.2% | -27.8 to 26.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.275 | -0.2% | -0.0314 to 0.0302 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 125 | 126 | +0.2% | -5.09 to 5.49 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 124 | 124 | -0.1% | -5.4 to 5.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.62 | 1.97 | +21.8% | 0.311 to 0.392 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 243 | 242 | -0.2% | -27.8 to 26.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
