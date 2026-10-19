# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% | -4.71 to -1.41 | LOSS |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -4.32 to -0.963 | LOSS |
| latency, 95th percentile (ms) | 0.344 | 0.354 | +3.0% | -0.0234 to 0.0441 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.588 | 0.592 | +0.7% | -0.00496 to 0.013 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.3% | -0.00714 to 0.00822 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.71 to -1.27 | GAIN |
| bytes in the cache, mean (MB) | 419 | 416 | -0.7% | -10.7 to 5.17 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 706,284 | 751,298 | +6.4% | -47,068 to 137,097 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.183 | +1.4% | -0.0384 to 0.0434 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 311 | +1.3% | -77.9 to 86.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.234 | +1.4% | -0.0584 to 0.0646 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
