# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,841 | 5,838 | -0.1% | -31.6 to 25.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,848 | 5,845 | -0.0% | -30.3 to 24.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.153 | 0.171 | +11.5% | -0.0502 to 0.0855 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.36 | 0.386 | +7.1% | -0.0576 to 0.109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0797 | 0.0836 | +4.9% | -0.0211 to 0.0289 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -3.65 to 3.07 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,090 | 63,415 | +0.5% | -72.1 to 721 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.127 | +4.6% | -0.0369 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 232 | +4.6% | -75.6 to 96.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0827 | 0.0865 | +4.7% | -0.0281 to 0.0358 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 102 | 106 | +4.2% | -24.6 to 33.1 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 99 | 103 | +4.1% | -24 to 32 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.63 | 2.85 | +8.4% | -0.622 to 1.07 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 221 | 232 | +4.6% | -75.6 to 96.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
