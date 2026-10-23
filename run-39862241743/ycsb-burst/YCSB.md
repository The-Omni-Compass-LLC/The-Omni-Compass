# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | +0.0% | -5.49 to 5.96 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -3.17 to 4.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.446 | -1.0% | -0.0204 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.684 | 0.69 | +0.9% | -0.0414 to 0.0534 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.219 | -1.4% | -0.011 to 0.00492 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -11.2 to -9.52 | GAIN |
| bytes in the cache, mean (MB) | 400 | 395 | -1.2% | -12.1 to 2.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,598 | 262,280 | -2.0% | -31,948 to 21,313 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.203 | +1.1% | -0.124 to 0.129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 141 | 143 | +1.1% | -112 to 115 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.269 | +1.1% | -0.21 to 0.216 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
