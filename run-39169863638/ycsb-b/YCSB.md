# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,911 | +0.0% | -1.74 to 4.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,917 | +0.0% | -3.49 to 5.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.262 | +1.8% | -0.025 to 0.0343 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.414 | 0.414 | -0.1% | -0.0145 to 0.0138 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.18 | +1.0% | -0.0142 to 0.0177 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,361 | -0.1% | -2.13 to 0.216 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,802 | 61,837 | +0.1% | -271 to 343 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.141 | -8.4% | -0.111 to 0.0851 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 253 | -10.1% | -234 to 177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.189 | -10.1% | -0.175 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
