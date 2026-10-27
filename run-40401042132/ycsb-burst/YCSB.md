# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | +0.0% | -3.89 to 4.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,916 | +0.0% | -3.56 to 4.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.27 | 0.272 | +0.7% | -0.00297 to 0.00697 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.459 | +1.7% | -0.0111 to 0.0265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.091 | 0.0913 | +0.4% | -0.00111 to 0.00177 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.65 to -1.16 | GAIN |
| bytes in the cache, mean (MB) | 403 | 398 | -1.1% | -20.6 to 11.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 187,354 | 178,027 | -5.0% | -56,662 to 38,008 | shown, not judged |
| host CPU busy (share of the run) | 0.0789 | 0.0987 | +25.0% | -0.0378 to 0.0773 | EVEN, no difference beyond the noise |
| host CPU-seconds | 37.1 | 47.5 | +28.2% | -19.8 to 40.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.104 | 0.134 | +28.2% | -0.0556 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 18 | 18.1 | +0.4% | -0.919 to 1.07 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 17.6 | 17.5 | -0.3% | -1 to 0.907 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.453 | 0.575 | +26.9% | 0.08 to 0.164 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 37.1 | 47.5 | +28.2% | -19.8 to 40.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
