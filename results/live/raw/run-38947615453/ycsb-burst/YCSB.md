# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,916 | -0.0% | -2.11 to -0.37 | LOSS |
| throughput (operations a second) | 2,922 | 2,921 | -0.0% | -2.29 to 0.153 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.332 | -0.2% | -0.00354 to 0.0022 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.422 | 0.422 | +0.0% | -0.0131 to 0.0131 | EVEN, the same |
| latency, mean (ms) | 0.161 | 0.16 | -0.4% | -0.00703 to 0.00569 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 497 | -2.9% | -29.8 to -0.374 | GAIN |
| bytes in the cache, mean (MB) | 407 | 393 | -3.4% | -27.2 to -0.677 | GAIN |
| pages read into the cache (misses) | 264,459 | 267,096 | +1.0% | -22,970 to 28,246 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.171 | -0.8% | -0.199 to 0.196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 130 | 126 | -2.9% | -170 to 163 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.235 | -2.9% | -0.319 to 0.305 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
