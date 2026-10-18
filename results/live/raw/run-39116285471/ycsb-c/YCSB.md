# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,916 | -0.1% | -7.88 to 4.43 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,921 | 2,919 | -0.1% | -7.4 to 4.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.236 | -0.3% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.387 | 0.386 | -0.2% | -0.0064 to 0.00507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.157 | +1.3% | -0.00832 to 0.0123 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -20.3 to 7.35 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 411 | -1.4% | -24.2 to 12.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 728,397 | 700,664 | -3.8% | -232,284 to 176,816 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.171 | +24.9% | -0.0313 to 0.0994 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 315 | +30.0% | -66.3 to 212 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.236 | +30.0% | -0.0498 to 0.159 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
