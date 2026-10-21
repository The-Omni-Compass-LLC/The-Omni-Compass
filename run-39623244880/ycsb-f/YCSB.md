# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,736 | 5,733 | -0.1% | -31.5 to 25 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,751 | 5,748 | -0.1% | -30.2 to 24.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.375 | -0.4% | -0.0065 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.595 | 0.596 | +0.2% | -0.00557 to 0.00757 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.203 | -0.3% | -0.00491 to 0.00382 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.77 to -1.62 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -3.93 to -0.0723 | GAIN |
| pages read into the cache (misses) | 688,625 | 692,655 | +0.6% | -35,761 to 43,820 | shown, not judged |
| host CPU busy (share of the run) | 0.273 | 0.276 | +1.2% | -0.0452 to 0.0517 | EVEN, no difference beyond the noise |
| host CPU-seconds | 496 | 504 | +1.6% | -111 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.19 | +1.6% | -0.0409 to 0.0468 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
