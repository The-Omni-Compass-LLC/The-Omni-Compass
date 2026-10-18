# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% | -2.05 to -0.384 | LOSS |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% | -1.74 to -0.245 | LOSS |
| latency, 95th percentile (ms) | 0.322 | 0.326 | +1.2% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.478 | 0.483 | +1.0% | -0.00742 to 0.0174 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.201 | +0.4% | -0.00485 to 0.00652 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.67 to -3.23 | GAIN |
| bytes in the cache, mean (MB) | 419 | 415 | -0.8% | -9.86 to 3.43 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 709,938 | 704,361 | -0.8% | -150,345 to 139,191 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.162 | -9.0% | -0.0485 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 270 | -10.9% | -105 to 38.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.202 | -10.9% | -0.0786 to 0.0289 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
