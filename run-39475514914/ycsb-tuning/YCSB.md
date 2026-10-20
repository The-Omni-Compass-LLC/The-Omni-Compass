# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,905 | +0.6% | -48.8 to 83.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,914 | +0.6% | -46.5 to 79.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.272 | 0.273 | +0.4% | -0.00148 to 0.00348 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.437 | 0.428 | -2.1% | -0.0367 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.18 | -4.8% | -0.0495 to 0.0313 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | -25.7 to 25.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 419 | +0.5% | -20.9 to 24.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,842 | 681,217 | +0.2% | -43,261 to 46,011 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.193 | -4.0% | -0.0432 to 0.0271 | EVEN, no difference beyond the noise |
| host CPU-seconds | 367 | 349 | -4.9% | -90.5 to 54.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.277 | 0.262 | -5.6% | -0.0702 to 0.039 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
