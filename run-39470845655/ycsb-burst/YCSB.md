# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,899 | +0.0% | -7.67 to 8.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,906 | +0.0% | -5.37 to 6.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.426 | 0.432 | +1.4% | -0.0362 to 0.0482 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.634 | +1.9% | -0.036 to 0.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.163 | +0.8% | -0.0114 to 0.014 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 497 | -3.0% | -19.5 to -10.9 | GAIN |
| bytes in the cache, mean (MB) | 406 | 393 | -3.2% | -21.9 to -4.48 | GAIN |
| pages read into the cache (misses) | 261,304 | 276,274 | +5.7% | -44,044 to 73,983 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.191 | +10.1% | -0.0124 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 127 | 143 | +12.4% | -8.8 to 40.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.268 | +12.3% | -0.0173 to 0.076 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 1.46 to 7.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
