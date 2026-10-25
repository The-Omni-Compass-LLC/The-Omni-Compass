# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,806 | -3.0% | -293 to 121 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,821 | -2.9% | -288 to 121 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.316 | +3.7% | -0.03 to 0.0527 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.528 | +5.9% | -0.0773 to 0.137 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.202 | +8.8% | -0.0151 to 0.0478 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 498 | -2.7% | -23.4 to -3.88 | GAIN |
| bytes in the cache, mean (MB) | 397 | 392 | -1.4% | -31.9 to 20.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,941 | 268,202 | +1.2% | -15,323 to 21,845 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.169 | +3.8% | -0.103 to 0.116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 125 | +5.3% | -90.3 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.242 | +8.8% | -0.18 to 0.219 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
