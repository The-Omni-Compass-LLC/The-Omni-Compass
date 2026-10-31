# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,897 | +0.0% | -0.856 to 2.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,907 | +0.0% | -0.382 to 1.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.331 | -6.5% | -0.0385 to -0.00749 | GAIN |
| latency, 99th percentile (ms) | 0.614 | 0.599 | -2.4% | -0.0367 to 0.00666 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.152 | -6.1% | -0.0195 to -9.55e-05 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,606 | +213.7% | 1,074 to 1,114 | power given |
| bytes in the cache, mean (MB) | 417 | 1,235 | +196.0% | 804 to 831 | power given |
| pages read into the cache (misses) | 680,649 | 125,495 | -81.6% | -568,720 to -541,588 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.4% | -0.0333 to 0.0319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 342 | +0.6% | -71.1 to 75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.257 | +0.6% | -0.0533 to 0.0562 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 193 | 179 | -7.2% | -14.8 to -13.1 | GAIN |
| the server's own CPU-seconds (mongod) | 190 | 176 | -7.6% | -15.4 to -13.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 3.08 | +24.8% | 0.45 to 0.773 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 340 | 342 | +0.6% | -71.1 to 75 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
