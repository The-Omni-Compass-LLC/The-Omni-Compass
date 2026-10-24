# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -9.72 to 8.28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% | -8.19 to 7.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.174 | 0.177 | +1.7% | -0.0746 to 0.0806 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.358 | 0.371 | +3.6% | -0.0562 to 0.0822 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0715 | 0.0722 | +0.9% | -0.0109 to 0.0122 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -6.83 to -0.19 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -12.7 to 10.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 731,719 | 721,905 | -1.3% | -54,241 to 34,613 | shown, not judged |
| host CPU busy (share of the run) | 0.0914 | 0.11 | +20.7% | -0.0379 to 0.0757 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 203 | +22.7% | -75.3 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.124 | 0.152 | +22.7% | -0.0561 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
