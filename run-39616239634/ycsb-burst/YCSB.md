# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7484 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,804 | 2,764 | -1.4% | -491 to 411 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,819 | 2,777 | -1.5% | -495 to 411 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.339 | +1.1% | -0.0246 to 0.0319 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.569 | 0.534 | -6.1% | -0.133 to 0.0637 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.193 | +1.5% | -0.0371 to 0.0428 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,484 | 7,484 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,431 | 1,402 | -2.0% | -392 to 335 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,262 | 77,146 | -0.2% | -2,518 to 2,285 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.145 | -4.6% | -0.0417 to 0.0278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 104 | -5.7% | -36.1 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.205 | -4.2% | -0.051 to 0.0328 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
