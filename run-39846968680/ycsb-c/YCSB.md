# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -15.1 to 11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,899 | -0.1% | -13 to 8.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.203 | 0.206 | +1.6% | -0.0155 to 0.0221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.38 | 0.38 | +0.0% | -0.0587 to 0.0587 | EVEN, the same |
| latency, mean (ms) | 0.148 | 0.152 | +2.5% | -0.0104 to 0.0179 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,347 | 1,346 | -0.0% | -4.09 to 2.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,611 | 61,636 | +0.0% | -96 to 146 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.17 | +8.0% | -0.0229 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 308 | +9.3% | -55.2 to 108 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.231 | +9.4% | -0.0409 to 0.0804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
