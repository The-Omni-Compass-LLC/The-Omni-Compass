# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,757 | 5,747 | -0.2% | -21.7 to 0.923 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,772 | 5,764 | -0.1% | -16.8 to -0.0361 | LOSS |
| latency, 95th percentile (ms) | 0.321 | 0.321 | +0.2% | -0.00313 to 0.00446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.488 | +3.2% | -0.024 to 0.054 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.185 | +0.9% | -0.00218 to 0.00548 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -20.4 to 4.63 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 413 | -1.1% | -12.7 to 3.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,488 | 693,772 | +0.9% | -11,719 to 24,287 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.251 | +3.7% | -0.0329 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 435 | 457 | +5.1% | -80 to 124 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.172 | +5.2% | -0.0301 to 0.0469 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
