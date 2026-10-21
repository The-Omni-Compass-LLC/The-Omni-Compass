# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -9.57 to 9.24 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,909 | +0.0% | -3.21 to 3.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.321 | +1.2% | -0.039 to 0.0463 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.504 | 0.505 | +0.2% | -0.128 to 0.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.177 | -2.5% | -0.0284 to 0.0191 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -10.3 to 0.549 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 400 | +0.2% | -3.25 to 4.59 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,591 | 274,502 | +3.0% | -21,557 to 37,380 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.161 | -8.0% | -0.0732 to 0.0452 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 116 | -9.6% | -62.7 to 38.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.218 | -9.7% | -0.118 to 0.0713 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
