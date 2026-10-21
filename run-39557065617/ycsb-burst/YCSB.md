# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,891 | -0.0% | -3.98 to 1.55 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% | -3.12 to 0.881 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.427 | +1.3% | 0.000495 to 0.0108 | LOSS |
| latency, 99th percentile (ms) | 0.559 | 0.572 | +2.3% | -0.00908 to 0.0351 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.22 | +2.2% | -0.00101 to 0.0104 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -4.9% | -62.9 to 13.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 385 | -4.1% | -49.6 to 17 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 268,415 | 275,488 | +2.6% | -35,900 to 50,046 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.184 | +9.6% | -0.0266 to 0.0588 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 127 | +11.4% | -24.6 to 50.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.238 | +11.4% | -0.0461 to 0.0948 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
