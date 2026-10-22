# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,925 | 2,926 | +0.0% | -3.69 to 5.31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,929 | 2,929 | +0.0% | -2.61 to 4.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.356 | 0.358 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.5 | -0.3% | -0.0074 to 0.00407 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.139 | -0.1% | -0.00353 to 0.00317 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -14.1 to -3.11 | GAIN |
| bytes in the cache, mean (MB) | 406 | 401 | -1.3% | -5.81 to -4.57 | GAIN |
| pages read into the cache (misses) | 269,181 | 265,850 | -1.2% | -9,266 to 2,604 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.105 | -19.0% | -0.139 to 0.0891 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.8 | 74.3 | -22.4% | -118 to 75.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.139 | -22.4% | -0.221 to 0.14 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
