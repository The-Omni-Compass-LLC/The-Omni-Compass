# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,880 | -0.1% | -6.67 to 0.663 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,887 | -0.1% | -5.4 to 0.293 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.346 | +2.6% | -0.0355 to 0.0529 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.589 | +0.2% | -0.018 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.201 | +0.2% | -0.0156 to 0.0164 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -16.5 to 4.78 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 414 | -0.4% | -13.5 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 728,939 | 739,337 | +1.4% | -120,862 to 141,659 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.214 | +1.1% | -0.0403 to 0.0451 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 378 | +1.2% | -92.7 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.285 | +1.3% | -0.0694 to 0.0766 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
