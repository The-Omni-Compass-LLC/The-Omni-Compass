# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,933 | -0.1% | -3.43 to -0.584 | LOSS |
| throughput (operations a second) | 2,939 | 2,937 | -0.1% | -2.69 to -1.21 | LOSS |
| latency, 95th percentile (ms) | 0.153 | 0.158 | +2.8% | -0.0294 to 0.0381 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.367 | 0.37 | +0.7% | -0.0547 to 0.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0789 | 0.0787 | -0.2% | -0.00474 to 0.00437 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -6.01 to -2.79 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.4% | -2.98 to -0.708 | GAIN |
| pages read into the cache (misses) | 687,277 | 690,320 | +0.4% | -29,545 to 35,631 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.104 | -14.5% | -0.0416 to 0.00621 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 187 | -16.2% | -85.6 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.139 | -16.2% | -0.0639 to 0.0101 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
