# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,886 | +0.0% | -1.68 to 2.15 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -0.742 to 1.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.294 | 0.293 | -0.5% | -0.0262 to 0.0236 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.582 | 0.581 | -0.2% | -0.0189 to 0.0169 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.186 | -0.7% | -0.00898 to 0.00649 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,347 | 1,348 | +0.1% | -1.93 to 4.35 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,604 | 61,665 | +0.1% | -138 to 260 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.172 | -12.0% | -0.0403 to -0.00653 | GAIN |
| host CPU-seconds | 347 | 297 | -14.6% | -94.4 to -6.77 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.223 | -14.6% | -0.0709 to -0.00516 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 175 | 174 | -0.4% | -10.3 to 8.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 172 | -0.5% | -10.2 to 8.5 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.54 | +2.8% | -0.0904 to 0.226 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 347 | 297 | -14.6% | -94.4 to -6.77 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
