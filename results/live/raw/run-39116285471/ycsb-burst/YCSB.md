# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.1% | -4.26 to 1.21 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -4.05 to -0.409 | LOSS |
| latency, 95th percentile (ms) | 0.428 | 0.427 | -0.2% | -0.0152 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.565 | -3.7% | -0.0668 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.22 | 0.221 | +0.5% | -0.0069 to 0.00928 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -19.3 to -3.32 | GAIN |
| bytes in the cache, mean (MB) | 401 | 395 | -1.4% | -20.3 to 8.69 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 273,008 | 271,852 | -0.4% | -43,642 to 41,330 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.175 | +17.6% | -0.0116 to 0.0642 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.5 | 119 | +20.7% | -8.53 to 49.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.185 | 0.223 | +20.6% | -0.016 to 0.0924 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
