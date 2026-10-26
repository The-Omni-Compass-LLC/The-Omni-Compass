# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,889 | +0.0% | -0.411 to 3.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% | -0.274 to 2.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.302 | -0.3% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.487 | +0.0% | -0.00657 to 0.00657 | EVEN, the same |
| latency, mean (ms) | 0.188 | 0.189 | +0.6% | -0.00406 to 0.00646 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -3.87 to -0.29 | GAIN |
| bytes in the cache, mean (MB) | 419 | 420 | +0.3% | -2.81 to 4.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,735 | 714,771 | +5.2% | -100,464 to 170,537 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.191 | -3.8% | -0.0361 to 0.0211 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 335 | -4.7% | -81.5 to 48.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.251 | -4.7% | -0.0612 to 0.0362 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 183 | 186 | +1.1% | -4.65 to 8.81 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 181 | 183 | +0.9% | -5.19 to 8.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 2.97 | +19.9% | 0.423 to 0.566 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351 | 335 | -4.7% | -81.6 to 48.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
