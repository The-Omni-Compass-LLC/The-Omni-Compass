# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,727 | 5,601 | -2.2% | -401 to 151 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,742 | 5,618 | -2.2% | -404 to 155 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.328 | +0.8% | -0.00492 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.502 | +0.9% | -0.0126 to 0.0212 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.211 | +2.7% | -0.0168 to 0.0281 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.82 to -1.82 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.7% | -5.27 to -0.543 | GAIN |
| pages read into the cache (misses) | 692,284 | 686,082 | -0.9% | -16,431 to 4,026 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.243 | +3.5% | -0.0194 to 0.0357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 422 | 442 | +4.8% | -43.5 to 84.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.159 | 0.171 | +7.0% | -0.00766 to 0.03 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
