# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,916 | 2,918 | +0.1% | -11 to 14.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,921 | +0.1% | -10.9 to 14.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.25 | -0.3% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.382 | 0.382 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, mean (ms) | 0.15 | 0.151 | +0.5% | -0.00427 to 0.00591 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -9.34 to 1.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -6.59 to 7.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 709,392 | 732,075 | +3.2% | -49,964 to 95,329 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.184 | +17.8% | -0.0194 to 0.075 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 342 | +21.0% | -43.1 to 162 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.256 | +21.0% | -0.033 to 0.122 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
