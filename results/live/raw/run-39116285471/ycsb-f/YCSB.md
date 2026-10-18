# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,699 | 5,711 | +0.2% | -116 to 139 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,716 | 5,727 | +0.2% | -117 to 139 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.504 | 0.501 | -0.6% | -0.0138 to 0.00783 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.204 | -2.6% | -0.0111 to 0.000173 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -21.8 to 1.54 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 409 | -1.3% | -11.9 to 1.48 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 692,274 | 701,426 | +1.3% | -22,885 to 41,189 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.239 | +0.8% | -0.0326 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 431 | +0.8% | -79.5 to 86 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.163 | +0.5% | -0.0331 to 0.0348 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
