# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.1% | -2.6 to -0.996 | LOSS |
| throughput (operations a second) | 2,894 | 2,892 | -0.1% | -2.57 to -0.848 | LOSS |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.2% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.436 | -0.9% | -0.013 to 0.00496 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.177 | 0.177 | +0.1% | -0.00552 to 0.00601 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -8.48 to 0.522 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 417 | -0.1% | -13.7 to 12.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,071 | 698,577 | -0.4% | -159,064 to 154,076 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.196 | +6.0% | -0.0525 to 0.0746 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 350 | +7.4% | -113 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.245 | 0.263 | +7.4% | -0.0846 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
