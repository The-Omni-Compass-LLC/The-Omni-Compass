# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,875 | +0.1% | -23.8 to 27.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,884 | 2,885 | +0.1% | -23.5 to 27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.366 | 0.364 | -0.5% | -0.00857 to 0.00457 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.581 | 0.574 | -1.1% | -0.0287 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.217 | -0.8% | -0.00718 to 0.00388 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.67 to -0.292 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -3.8 to 1.09 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,907 | 683,763 | +1.3% | -13,323 to 31,035 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.247 | +2.8% | -0.0606 to 0.074 | EVEN, no difference beyond the noise |
| host CPU-seconds | 416 | 433 | +4.0% | -138 to 171 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.314 | 0.326 | +3.9% | -0.102 to 0.126 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
