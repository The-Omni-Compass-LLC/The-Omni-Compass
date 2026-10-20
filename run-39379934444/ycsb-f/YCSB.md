# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,815 | 5,809 | -0.1% | -28 to 15.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,826 | 5,821 | -0.1% | -27.9 to 16.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.229 | 0.234 | +2.0% | -0.0136 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.439 | +1.5% | -0.0192 to 0.0325 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.114 | 0.116 | +1.6% | -0.00725 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -6.53 to -3.03 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.6% | -5.35 to 0.403 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,152 | 710,603 | +1.6% | -23,488 to 46,391 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.166 | +13.2% | -0.0201 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 304 | +15.4% | -41.2 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0984 | 0.114 | +15.4% | -0.0156 to 0.0459 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
