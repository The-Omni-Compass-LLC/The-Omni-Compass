# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,936 | -0.1% | -10.8 to 6.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,938 | -0.1% | -8.9 to 4.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.127 | 0.155 | +22.6% | -0.0335 to 0.0908 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.333 | 0.351 | +5.2% | -0.00718 to 0.0418 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0621 | 0.0647 | +4.2% | -0.0109 to 0.0161 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | +0.0% | -1.79 to 2.32 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,804 | 61,901 | +0.2% | -245 to 439 | shown, not judged |
| host CPU busy (share of the run) | 0.0894 | 0.0732 | -18.1% | -0.0415 to 0.00917 | EVEN, no difference beyond the noise |
| host CPU-seconds | 163 | 131 | -19.9% | -80.3 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.122 | 0.0977 | -19.9% | -0.0602 to 0.0116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.7 | 54.6 | +5.7% | -6.34 to 12.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.1 | 52.8 | +5.4% | -6.24 to 11.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.59 | 1.81 | +14.3% | -0.105 to 0.56 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 163 | 131 | -19.9% | -80.3 to 15.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
