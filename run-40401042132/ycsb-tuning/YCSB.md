# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,831 | 2,827 | -0.1% | -9.44 to 2.71 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,843 | 2,840 | -0.1% | -10 to 5.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.425 | 0.434 | +2.1% | 4.26e-05 to 0.018 | LOSS |
| latency, 99th percentile (ms) | 0.653 | 0.678 | +3.8% | -0.0594 to 0.109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.234 | 0.239 | +2.1% | -0.0005 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 573 | +11.9% | 35.2 to 86.4 | power given |
| bytes in the cache, mean (MB) | 415 | 462 | +11.4% | 30.3 to 64.1 | power given |
| pages read into the cache (misses) | 455,579 | 423,420 | -7.1% | -47,483 to -16,835 | shown, not judged |
| host CPU busy (share of the run) | 0.293 | 0.312 | +6.6% | 0.000402 to 0.0381 | power given |
| host CPU-seconds | 346 | 376 | +8.7% | -8.03 to 68 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.395 | 0.429 | +8.7% | -0.00894 to 0.0778 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9.33 |  | 5.54 to 13.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 190 | +2.2% | -3.83 to 11.9 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 187 | +1.9% | -4.37 to 11.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.78 | 2.29 | +28.9% | 0.449 to 0.578 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 346 | 376 | +8.7% | -8.03 to 68 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
