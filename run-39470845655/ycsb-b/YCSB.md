# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,913 | -0.0% | -4.2 to 1.56 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,916 | -0.0% | -4.22 to 1.47 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.268 | 0.267 | -0.4% | -0.0124 to 0.0104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.434 | -1.5% | -0.0241 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.119 | +0.0% | -0.00688 to 0.00698 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -6.27 to -0.716 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -12.7 to 9.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,051 | 711,588 | +1.5% | -169,692 to 190,766 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.146 | +5.8% | -0.0698 to 0.0858 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 266 | +6.6% | -146 to 179 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.2 | +6.6% | -0.11 to 0.134 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
