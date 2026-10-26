# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% | -8.97 to 2.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,935 | -0.1% | -8.2 to 3.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.266 | +3.8% | -0.0176 to 0.0369 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.445 | +4.9% | 0.00413 to 0.0372 | LOSS |
| latency, mean (ms) | 0.0832 | 0.0883 | +6.2% | 0.00367 to 0.00658 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -11.4 to -0.519 | GAIN |
| bytes in the cache, mean (MB) | 406 | 407 | +0.1% | -4.23 to 5.33 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 271,839 | 274,828 | +1.1% | -28,054 to 34,032 | shown, not judged |
| host CPU busy (share of the run) | 0.081 | 0.1 | +23.6% | -0.0788 to 0.117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 58.2 | 73.5 | +26.3% | -62.5 to 93.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.109 | 0.137 | +26.4% | -0.117 to 0.174 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -2.92 to 12.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 26.4 | 28 | +6.1% | -1.91 to 5.12 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 25.7 | 27.1 | +5.3% | -2.21 to 4.92 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.67 | 0.924 | +37.9% | 0.163 to 0.345 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 58.2 | 73.5 | +26.3% | -62.5 to 93.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
