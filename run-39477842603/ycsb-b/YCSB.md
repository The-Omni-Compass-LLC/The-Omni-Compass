# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,896 | -0.1% | -6.9 to 0.996 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,899 | -0.1% | -6.14 to 0.548 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.316 | +2.9% | -0.0197 to 0.0377 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.439 | 0.451 | +2.8% | -0.0328 to 0.0575 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.184 | +1.4% | -0.000169 to 0.00515 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -3.96 to -2.9 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.1% | -4.09 to 3.07 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,271 | 701,365 | +2.1% | -68,677 to 96,865 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.2 | -5.2% | -0.0708 to 0.0487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 384 | 357 | -7.1% | -165 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.288 | 0.268 | -7.1% | -0.124 to 0.0827 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
