# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,629 | 2,744 | +4.4% | -873 to 1,103 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,644 | 2,761 | +4.4% | -865 to 1,100 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.315 | +1.1% | -0.0632 to 0.0698 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.574 | 0.606 | +5.6% | -0.373 to 0.437 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.237 | 0.217 | -8.4% | -0.165 to 0.125 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 532 | +4.0% | -33.7 to 74.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 394 | 410 | +4.3% | -22 to 55.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 219,531 | 245,677 | +11.9% | -132,269 to 184,561 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.156 | +3.9% | -0.126 to 0.138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 113 | +3.5% | -104 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.224 | -0.4% | -0.182 to 0.18 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 56.7 | 59.3 | +4.5% | -16.1 to 21.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 56 | 58.4 | +4.2% | -16.1 to 20.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.766 | 0.955 | +24.7% | 0.0141 to 0.364 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 109 | 113 | +3.5% | -104 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
