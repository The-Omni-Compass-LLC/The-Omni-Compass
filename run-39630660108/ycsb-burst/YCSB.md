# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,810 | 2,828 | +0.6% | -71.4 to 107 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,824 | 2,842 | +0.6% | -73.7 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.304 | 0.308 | +1.1% | -0.0128 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.5 | 0.508 | +1.7% | -0.0199 to 0.0372 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.189 | -3.5% | -0.0247 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 492 | -3.8% | -58.1 to 18.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 397 | 384 | -3.4% | -32.9 to 5.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 251,330 | 261,227 | +3.9% | -65,310 to 85,103 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.16 | +13.9% | -0.0628 to 0.102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.9 | 116 | +16.2% | -55.5 to 87.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.192 | 0.223 | +15.8% | -0.104 to 0.165 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
