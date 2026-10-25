# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% | -3.45 to 2.62 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -4.04 to 2.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.435 | -0.5% | -0.0235 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.591 | +0.0% | -0.024 to 0.024 | EVEN, the same |
| latency, mean (ms) | 0.218 | 0.216 | -1.0% | -0.013 to 0.00872 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -22.6 to 2.26 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 394 | -1.3% | -16.9 to 6.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,402 | 272,507 | +3.5% | -20,209 to 38,418 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.198 | +6.2% | -0.0279 to 0.0509 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 138 | +7.4% | -21.8 to 41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.26 | +7.4% | -0.0411 to 0.0771 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
