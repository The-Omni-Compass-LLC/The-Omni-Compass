# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,877 | +0.1% | -12.5 to 18.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -11.4 to 16.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.503 | 0.502 | -0.2% | -0.0053 to 0.0033 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.67 | 0.665 | -0.7% | -0.0212 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.222 | -0.2% | -0.00714 to 0.00636 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -25.8 to -0.486 | GAIN |
| bytes in the cache, mean (MB) | 399 | 392 | -1.6% | -22.2 to 9.42 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 256,676 | 277,663 | +8.2% | 13,837 to 28,137 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.191 | -6.4% | -0.0848 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 144 | 132 | -7.9% | -74.4 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.271 | 0.249 | -8.0% | -0.139 to 0.0962 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
