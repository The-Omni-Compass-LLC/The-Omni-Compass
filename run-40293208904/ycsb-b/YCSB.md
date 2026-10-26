# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,910 | +0.2% | -6.13 to 15.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,915 | +0.1% | -6.31 to 14.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.219 | 0.208 | -5.0% | -0.0372 to 0.0152 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.375 | -3.4% | -0.0227 to -0.00393 | GAIN |
| latency, mean (ms) | 0.156 | 0.152 | -2.5% | -0.0123 to 0.00439 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 556 | +8.5% | -20 to 107 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 450 | +8.1% | -11.9 to 79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,493 | 652,271 | -8.5% | -138,382 to 17,937 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.151 | -11.3% | -0.0451 to 0.00686 | EVEN, no difference beyond the noise |
| host CPU-seconds | 310 | 270 | -13.0% | -91.3 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.202 | -13.0% | -0.0685 to 0.00804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 3.54 to 11.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 150 | 148 | -1.3% | -5.3 to 1.31 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 148 | 146 | -1.6% | -5.78 to 0.918 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.03 | 2.46 | +21.6% | 0.39 to 0.486 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 310 | 270 | -13.0% | -91.3 to 10.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
