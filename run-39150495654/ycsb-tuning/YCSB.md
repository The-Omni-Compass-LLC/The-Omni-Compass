# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,865 | 2,843 | -0.8% | -204 to 160 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,874 | 2,851 | -0.8% | -203 to 158 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.267 | 0.266 | -0.6% | -0.0104 to 0.00706 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.428 | -0.5% | -0.0111 to 0.00639 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.209 | -2.1% | -0.0389 to 0.0299 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,338 | -0.8% | -70.3 to 47.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,011 | 62,028 | -1.6% | -5,534 to 3,568 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.174 | +1.1% | -0.0918 to 0.0956 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 316 | +1.5% | -197 to 206 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.242 | +2.0% | -0.147 to 0.156 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
