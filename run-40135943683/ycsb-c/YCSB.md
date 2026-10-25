# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -2.39 to 1.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -2.53 to 1.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.315 | 0.315 | -0.2% | -0.00826 to 0.00692 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.494 | -0.1% | -0.00906 to 0.00839 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.192 | -0.7% | -0.00879 to 0.00615 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.1% | -110 to 57.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 401 | -4.8% | -99.7 to 59.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 690,477 | 722,378 | +4.6% | -179,482 to 243,284 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.195 | -2.0% | -0.0774 to 0.0696 | EVEN, no difference beyond the noise |
| host CPU-seconds | 350 | 340 | -2.6% | -169 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.256 | -2.7% | -0.127 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
