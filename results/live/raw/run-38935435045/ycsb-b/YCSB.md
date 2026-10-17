# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -3.19 to -0.41 | LOSS |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -3.06 to -0.305 | LOSS |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.6% | -0.00361 to 0.0136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.492 | +2.0% | -0.0224 to 0.0417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.202 | +2.5% | -0.00323 to 0.0132 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -22.4 to 4.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 411 | -1.7% | -21.6 to 7.13 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 697,708 | 688,177 | -1.4% | -152,316 to 133,255 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.189 | +6.3% | -0.0511 to 0.0733 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 325 | +6.9% | -107 to 149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.244 | +6.9% | -0.0801 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
