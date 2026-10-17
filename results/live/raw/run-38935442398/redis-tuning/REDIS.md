# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,194 | +1.1% | 6.84 to 18.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00454 to 0.00206 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00314 to 0.0131 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0162 to 0.0194 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.28 | -0.1% | -0.0696 to 0.0571 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.13 | -4.0% | -0.0682 to -0.027 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 0.975 to 2.43 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.798 to 1.65 | power given |
| keys evicted | 138,150 | 133,510 | -3.4% | -7,971 to -1,310 | shown, not judged |
| host CPU busy (share of the run) | 0.0645 | 0.0558 | -13.4% | -0.0419 to 0.0246 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 97.7 | -14.2% | -78.5 to 46.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.182 | -15.1% | -0.149 to 0.0846 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
