# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,895 | +0.1% | -0.541 to 3.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,900 | +0.1% | -1.17 to 4.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.4% | -0.0138 to 0.0112 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.558 | 0.552 | -1.1% | -0.0151 to 0.00239 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.19 | -1.5% | -0.00647 to 0.00075 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.1% | -0.65 to 2.66 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,602 | 61,646 | +0.1% | -80.5 to 168 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.169 | -5.4% | -0.0859 to 0.0668 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 289 | -6.3% | -174 to 135 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.217 | -6.3% | -0.131 to 0.102 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
