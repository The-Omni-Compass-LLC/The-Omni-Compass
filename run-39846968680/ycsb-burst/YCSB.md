# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,937 | -0.1% | -14.7 to 10.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,940 | -0.1% | -11.8 to 7.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.256 | +3.6% | -0.0304 to 0.0484 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.38 | 0.399 | +5.2% | -0.0907 to 0.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0753 | 0.077 | +2.3% | -0.0231 to 0.0266 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,518 | 1,522 | +0.3% | -0.279 to 9.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,564 | 77,669 | +0.1% | -97.3 to 308 | shown, not judged |
| host CPU busy (share of the run) | 0.06 | 0.0829 | +38.2% | -0.0332 to 0.0789 | EVEN, no difference beyond the noise |
| host CPU-seconds | 42.6 | 60.4 | +41.7% | -26.6 to 62.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0795 | 0.113 | +41.8% | -0.0498 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
