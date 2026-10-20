# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,698 | 5,697 | -0.0% | -17.5 to 15.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,714 | 5,713 | -0.0% | -17.1 to 16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.435 | 0.436 | +0.3% | -0.0252 to 0.0279 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.644 | +0.1% | -0.0216 to 0.0229 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.253 | 0.254 | +0.4% | -0.0164 to 0.0184 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -21.5 to 0.543 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 410 | -1.8% | -16.8 to 2.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,956 | 691,489 | +2.0% | -6,298 to 33,363 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.288 | +3.8% | 0.00475 to 0.0163 | power given |
| host CPU-seconds | 467 | 491 | +5.0% | 6.32 to 40.7 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.185 | +5.0% | 0.00283 to 0.0147 | power given |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
