# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -18.1 to 19.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,894 | +0.0% | -17.8 to 19.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.371 | 0.371 | -0.2% | -0.0101 to 0.00874 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.558 | 0.559 | +0.3% | -0.00837 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.224 | +0.3% | -0.00366 to 0.00518 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -5.08 to -3.64 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -5.51 to 0.584 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,185 | 678,707 | -0.1% | -24,246 to 23,288 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.235 | +4.5% | -0.039 to 0.0592 | EVEN, no difference beyond the noise |
| host CPU-seconds | 384 | 405 | +5.5% | -85.6 to 128 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.289 | 0.305 | +5.4% | -0.0659 to 0.0972 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
