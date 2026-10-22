# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,881 | -0.1% | -9.24 to 4.66 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,887 | -0.1% | -5.27 to 2.26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.361 | +3.2% | -0.0315 to 0.0542 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.538 | 0.554 | +3.0% | -0.0447 to 0.0767 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.205 | +2.1% | -0.00559 to 0.0139 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -19 to 9.48 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.3% | -12.7 to 10.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,831 | 724,988 | +4.8% | 9,160 to 57,154 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.211 | +4.7% | -0.056 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 369 | +5.2% | -123 to 159 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.277 | +5.3% | -0.0927 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
