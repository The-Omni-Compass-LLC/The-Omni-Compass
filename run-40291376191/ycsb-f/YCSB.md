# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,751 | 5,745 | -0.1% | -25.3 to 13.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,763 | -0.1% | -26.9 to 18.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.321 | +1.0% | -0.00384 to 0.0105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.494 | +2.6% | -0.05 to 0.0747 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.191 | +1.7% | -0.00338 to 0.00964 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 569 | +11.2% | -11.6 to 126 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 457 | +10.0% | -16.6 to 99.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,498 | 631,501 | -8.3% | -121,924 to 7,929 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.258 | +3.9% | -0.0217 to 0.041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 452 | 474 | +5.0% | -54.1 to 99.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.169 | 0.178 | +5.0% | -0.0203 to 0.0372 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 271 | 274 | +1.1% | 1.1 to 4.8 | power given |
| the server's own CPU-seconds (mongod) | 267 | 270 | +0.9% | 0.742 to 3.97 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.42 | 4.02 | +17.2% | 0.231 to 0.95 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 452 | 474 | +5.0% | -54.1 to 99.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
