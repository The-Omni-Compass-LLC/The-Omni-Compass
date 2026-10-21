# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -4.23 to 3.53 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -3.43 to 2.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.37 | 0.37 | +0.0% | -0.0203 to 0.0203 | EVEN, the same |
| latency, 99th percentile (ms) | 0.521 | 0.519 | -0.5% | -0.0252 to 0.0199 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.0% | -0.00494 to 0.00482 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -58.3 to 22.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 394 | -1.8% | -59.7 to 45.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,331 | 273,888 | +2.8% | -10,443 to 25,557 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.211 | -6.5% | -0.0533 to 0.0242 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 153 | -8.0% | -47.2 to 20.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.312 | 0.287 | -8.0% | -0.0886 to 0.0388 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
